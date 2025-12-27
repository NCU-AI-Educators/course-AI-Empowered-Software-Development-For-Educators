import os
# Fix for MPS 'aten::isin' error: Enable fallback to CPU for unsupported ops
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"
# Suppress huggingface/tokenizers parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import uvicorn
from fastapi import FastAPI, UploadFile, File, Body
from fastapi.responses import HTMLResponse, Response
from pydantic import BaseModel
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
from openai import OpenAI  # <--- New Import for Lesson 26
from fastapi.responses import StreamingResponse # For Audio Stream

# Filter out specific library warnings to keep console clean for students
warnings.filterwarnings("ignore", message=".*To copy construct from a tensor.*")
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")

# 1. 初始化 FastAPI 应用
app = FastAPI(title="Lesson 26 AI Vision Translator")

# ==========================================
# ☁️ Cloud API Configuration (Lesson 26 New)
# ==========================================
# 尝试从环境变量获取 Key，如果没有则留空 (会报错提示)
# 尝试从环境变量获取 Key
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 检查是否有可用的 Key
VALID_API_KEY = SILICONFLOW_API_KEY or OPENAI_API_KEY

SILICONFLOW_BASE_URL = "https://api.siliconflow.cn/v1"
CLOUD_MODEL_NAME = "deepseek-ai/DeepSeek-V3.2" 

if not VALID_API_KEY:
    print("\n" + "!"*50)
    print("⛔️ 致命错误: 未检测到 API Key！")
    print("--------------------------------------------------")
    print("请至少设置以下其中一个环境变量:")
    print("1. export SILICONFLOW_API_KEY='sk-...' (推荐)")
    print("2. export OPENAI_API_KEY='sk-...' (备选)")
    print("!"*50 + "\n")
    sys.exit(1) # Fail fast: 缺少核心依赖直接退出

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
local_model_path = "./models/florence-2-base"
if os.path.exists(local_model_path):
    print(f"📂 发现本地模型 path: {local_model_path}")
    model_id = local_model_path
else:
    print(f"⚠️ 未找到本地模型，准备从 HuggingFace 下载...")
    model_id = "microsoft/Florence-2-base"

device = "mps" if torch.backends.mps.is_available() else "cpu"
torch_dtype = torch.float16 if device != "cpu" else torch.float32

model = None
processor = None

try:
    print("="*50)
    print(f"🚀 正在加载 Florence-2 模型...")
    print(f"📂 模型来源: {model_id}")
    print(f"🖥️  运行设备: {device.upper()}")
    
    local_files_only = False
    if os.path.isdir(model_id):
        print(f"🔌 检测到本地路径，启用离线模式 (local_files_only=True)")
        local_files_only = True
        os.environ["HF_DATASETS_OFFLINE"] = "1"
        os.environ["TRANSFORMERS_OFFLINE"] = "1"
    
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
    print(f"\n❌ 模型加载失败: {e}")

# 3. 模型预热
def warmup_model():
    if not model or not processor: return
    print("🔥 正在预热模型... (消除首次推理卡顿)")
    try:
        dummy_img = Image.new('RGB', (64, 64), color='white')
        dummy_prompt = "<CAPTION>"
        inputs = processor(text=dummy_prompt, images=dummy_img, return_tensors="pt").to(device, torch_dtype)
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

warmup_model()

# ==========================================
# 🧠 new helper: Cloud Translation
# ==========================================
def translate_text(text: str) -> str:
    """调用云端大模型将英文翻译成中文"""
    # 尝试多种方式获取 Key
    api_key = SILICONFLOW_API_KEY or os.getenv("OPENAI_API_KEY")
    
    # 即使 api_key 为 None，我们也尝试初始化，因为 OpenAI SDK 可能有自己的配置加载机制
    try:
        client = OpenAI(api_key=api_key, base_url=SILICONFLOW_BASE_URL)
        response = client.chat.completions.create(
            model=CLOUD_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个专业的翻译助手。请将用户的英文输入直接翻译成中文，不要添加任何解释。"},
                {"role": "user", "content": text},
            ],
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ 翻译出错: {e}")
        return f"翻译失败: {str(e)} (可能是 API Key 未配置)"

        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ 翻译出错: {e}")
        return f"翻译失败: {str(e)} (可能是 API Key 未配置)"

# Pydantic Model for API
class TranslationRequest(BaseModel):
    text: str

class TTSRequest(BaseModel):
    text: str

# ==========================================
# 🚦 Routes
# ==========================================

@app.get("/", response_class=HTMLResponse)
def home():
    """Serve the frontend HTML"""
    return pathlib.Path("lesson26.html").read_text(encoding="utf-8")

@app.get("/qrcode")
def get_qr_image():
    ip = get_local_ip()
    url = f"http://{ip}:8000"
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
    Step 1: 视觉识别 (Vision Only)
    接收图片 -> Florence-2 生成英文描述 -> 返回英文
    """
    global model, processor
    
    if not model or not processor:
        return {"error": "Model not loaded."}

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # 构造提示词 task
        prompt = "<MORE_DETAILED_CAPTION>"
        
        # 打印日志
        print(f"\n📸 收到图片: {file.filename}")
        
        # 计时开始
        start_time = time.time()
        
        # 1. 本地视觉推理 (Florence-2)
        inputs = processor(text=prompt, images=image, return_tensors="pt").to(device, torch_dtype)
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            do_sample=False,
            num_beams=3,
        )
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = processor.post_process_generation(
            generated_text, 
            task=prompt, 
            image_size=(image.width, image.height)
        )
        caption_en = parsed_answer[prompt]
        
        # 计时结束
        end_time = time.time()
        cost_time = round(end_time - start_time, 2)
        
        # 打印日志
        print(f"⏱️ 视觉耗时: {cost_time}s")
        print(f"🤖 EN: {caption_en}")
        
        return {
            "label": caption_en,     # 兼容旧逻辑，前端如果是旧版也会直接显示英文
            "caption_en": caption_en, # 显式字段
            "cost_time": cost_time
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/translate")
async def translate_endpoint(request: TranslationRequest):
    """
    Step 2: 云端翻译 (Language Only)
    接收英文 -> 调用 API -> 返回中文
    """
    print(f"☁️ 收到翻译请求: {request.text[:50]}...")
    start_time = time.time()
    
    caption_zh = translate_text(request.text)
    
    end_time = time.time()
    cost_time = round(end_time - start_time, 2)
    
    print(f"🇨🇳 ZH: {caption_zh}")
    print(f"⏱️ 翻译耗时: {cost_time}s")
    
    return {
        "caption_zh": caption_zh,
        "cost_time": cost_time
    }

@app.post("/speak")
async def speak_endpoint(request: TTSRequest):
    """
    Step 3: 文本转语音 (TTS)
    接收中文 -> 调用 SiliconFlow API -> 返回 MP3 音频流
    """
    print(f"🔈 收到 TTS 请求: {request.text[:50]}...")
    
    # 尝试多种方式获取 Key
    api_key = SILICONFLOW_API_KEY or OPENAI_API_KEY
    client = OpenAI(api_key=api_key, base_url=SILICONFLOW_BASE_URL)

    def generate_audio():
        with client.audio.speech.with_streaming_response.create(
            model="FunAudioLLM/CosyVoice2-0.5B", 
            voice="FunAudioLLM/CosyVoice2-0.5B:anna", # 音色
            input=request.text, 
            response_format="mp3"
        ) as response:
            for chunk in response.iter_bytes():
                yield chunk

    return StreamingResponse(generate_audio(), media_type="audio/mpeg")

if __name__ == "__main__":
    ip = get_local_ip()
    port = 8000
    url = f"http://{ip}:{port}/docs"
    
    print("\n" + "="*50)
    print(f"🚀 Lesson 26 AI Vision Translator 启动中...")
    print(f"Running on: {url}")
    print("="*50)
    
    # 打印二维码供扫描
    try:
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.print_ascii(invert=True)
        print(f"\n📱 手机扫码体验: {url}")
    except:
        pass
    
    print("\n按 Ctrl+C 停止服务")
    
    uvicorn.run(app, host="0.0.0.0", port=port)
