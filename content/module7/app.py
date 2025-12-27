import os
# Fix for MPS 'aten::isin' error: Enable fallback to CPU for unsupported ops
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
# Suppress huggingface/tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, Response
from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import io
import socket
import qrcode
import sys
import torch
import pathlib
import pathlib
import time
import warnings # Added for warning suppression

# Filter out specific library warnings to keep console clean for students
warnings.filterwarnings("ignore", message=".*To copy construct from a tensor.*")
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

# 1. 初始化 FastAPI 应用
app = FastAPI(title="Lesson 25 Vision Demo (Florence-2)")

# Mock flash_attn for Mac compatibility
from unittest.mock import MagicMock
sys.modules["flash_attn"] = MagicMock()
sys.modules["flash_attn"].__spec__ = MagicMock()

# Helper: Get Local IP
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# 2. 预加载模型 (使用 Microsoft Florence-2-base)
# 优先检查本地模型
local_model_path = "./models/florence-2-base"
if os.path.exists(local_model_path):
    print(f"📂 发现本地模型 path: {local_model_path}")
    model_id = local_model_path
else:
    print(f"⚠️ 未找到本地模型，准备从 HuggingFace 下载...")
    model_id = "microsoft/Florence-2-base"
# 自动检测设备: 优先 MPS (Mac), 其次 CPU
device = "mps" if torch.backends.mps.is_available() else "cpu"
# Florence-2 在 GPU/MPS 上通常使用 float16，但在 CPU 上使用 float32
torch_dtype = torch.float16 if device != "cpu" else torch.float32

model = None
processor = None

try:
    print("="*50)
    print(f"🚀 正在加载 Florence-2 模型...")
    print(f"📂 模型来源: {model_id}")
    print(f"🖥️  运行设备: {device.upper()}")
    
    # 如果发现是本地路径，强制离线模式
    local_files_only = False
    if os.path.isdir(model_id):
        print(f"🔌 检测到本地路径，启用离线模式 (local_files_only=True)")
        local_files_only = True
        os.environ["HF_DATASETS_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
    
    if model_id == "microsoft/Florence-2-base" and not local_files_only:
        print("第一次运行需要下载模型 (约 1.5GB)，请耐心等待...")
    
    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        trust_remote_code=True, 
        torch_dtype=torch_dtype,
        local_files_only=local_files_only
    ).to(device)
    
    processor = AutoProcessor.from_pretrained(
        model_id, 
        trust_remote_code=True,
        local_files_only=local_files_only
    )
    
    print("✨ Florence-2 模型加载成功！")
    print("="*50)
except Exception as e:
    import traceback
    print(f"\n❌ 模型加载失败: {e}")
    print("可能是 transformer 版本过低或依赖缺失。请尝试运行: pip install -U transformers timm einops")
    traceback.print_exc()

# 3. 模型预热 (Warmup) - 消除第一次运行的卡顿
def warmup_model():
    if not model or not processor: return
    print("🔥 正在预热模型... (消除首次推理卡顿)")
    try:
        # 创建一个极其微小的 Dummy 输入
        dummy_img = Image.new('RGB', (64, 64), color='white')
        dummy_prompt = "<CAPTION>"
        inputs = processor(text=dummy_prompt, images=dummy_img, return_tensors="pt").to(device, torch_dtype)
        # 强制运行一次生成
        model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=5, 
            do_sample=False,
            num_beams=1,
        )
        print("✅ 模型预热完成！")
    except Exception as e:
        print(f"⚠️ 预热失败 (不影响主功能): {e}")

# 执行预热
warmup_model()

@app.get("/", response_class=HTMLResponse)
def home():
    """Serve the frontend HTML"""
    return pathlib.Path("index.html").read_text(encoding="utf-8")

@app.get("/qrcode")
def get_qr_image():
    """Generate QR Code for the server URL"""
    ip = get_local_ip()
    url = f"http://{ip}:8000"
    print(f"📱 QR Code URL: {url}")
    
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.getvalue(), media_type="image/png")

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    """
    接收手机上传的图片，并返回详细描述 (Detailed Caption)
    """
    global model, processor
    
    if not model or not processor:
        return {"error": "Model not loaded. Check server logs."}

    try:
        # 读取图片数据
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # 构造提示词 task
        prompt = "<MORE_DETAILED_CAPTION>"
        
        # 打印日志到控制台
        print(f"\n📸 收到图片: {file.filename}")
        
        # 计时开始
        start_time = time.time()
        
        # 预处理输入
        inputs = processor(text=prompt, images=image, return_tensors="pt").to(device, torch_dtype)

        # 生成描述
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            do_sample=False,
            num_beams=3,
        )
        
        # 解码输出
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        
        # 后处理 (Florence-2 特有)
        parsed_answer = processor.post_process_generation(
            generated_text, 
            task=prompt, 
            image_size=(image.width, image.height)
        )
        
        # 计时结束
        end_time = time.time()
        cost_time = round(end_time - start_time, 2)
        
        # 获取最终文本
        caption = parsed_answer[prompt]
        
        # 打印日志到控制台
        print(f"⏱️ 推理耗时: {cost_time}s")
        print(f"🤖 Florence-2 描述:\n{caption}")
        
        return {
            "label": caption,
            "cost_time": cost_time
        }
    except Exception as e:
        import traceback
        print(f"❌ 处理图片时发生错误: {e}")
        traceback.print_exc()
        return {"error": str(e)}

def get_local_ip():
    """获取本机局域网IP"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def print_qr_code(url):
    """在终端打印二维码"""
    try:
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.print_ascii(invert=True)
        print(f"\n📱 手机扫码体验: {url}")
    except Exception:
        print(f"\n⚠️ 无法生成二维码，请手动访问: {url}")

if __name__ == "__main__":
    ip = get_local_ip()
    port = 8000
    url = f"http://{ip}:{port}/docs"
    
    print("\n" + "="*50)
    print(f"🚀 服务启动中...")
    print(f"Running on: {url}")
    print("="*50)
    
    # 打印二维码供扫描
    print_qr_code(url)
    
    print("\n按 Ctrl+C 停止服务")
    
    uvicorn.run(app, host="0.0.0.0", port=port)
