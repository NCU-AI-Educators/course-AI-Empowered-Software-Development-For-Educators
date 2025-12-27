import os
from transformers import pipeline
from PIL import Image
from openai import OpenAI

# ==========================================
# 🔧 配置区域
# ==========================================
# 1. 视觉模型路径 (Local)
VISION_MODEL_PATH = "./models/vit-base-patch16-224"

# 2. 云端 API 配置 (Cloud)
# 推荐使用 SiliconFlow (硅基流动) 或 DeepSeek
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # ⚠️ 请替换为你的真实 Key
BASE_URL = "https://api.siliconflow.cn/v1"
LLM_MODEL = "deepseek-ai/DeepSeek-V2.5"

# ==========================================
# 🧠 核心函数
# ==========================================

def init_vision_model():
    """初始化本地视觉模型"""
    print("👁️ 正在加载本地视觉模型 (ViT)...")
    try:
        return pipeline("image-classification", model=VISION_MODEL_PATH)
    except Exception as e:
        print(f"❌ 视觉模型加载失败: {e}")
        return None

def identify_image(classifier, image_path):
    """步骤 1: 看图 (Local)"""
    print(f"📸 正在观察: {image_path}")
    image = Image.open(image_path)
    preds = classifier(image)
    # 取置信度最高的结果
    top_label = preds[0]['label']
    print(f"✅ 识别结果: {top_label}")
    return top_label

def generate_creative_content(label):
    """步骤 2: 思考 (Cloud)"""
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # 🔥 核心：Prompt Engineering (提示词工程)
    # 我们把视觉识别到的 label 填入 prompt 模板中
    prompt = f"""
    我给你看了一张照片，AI识别出它是 "{label}"。
    请你以“万物有灵”为主题，以这个物品的口吻，写一首三行俳句。
    要幽默、有趣。
    """
    
    print(f"☁️ 正在请求云端大脑创作 (关于 {label})...")
    
    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 云端调用失败: {e}"

# ==========================================
# 🚀 主程序
# ==========================================

if __name__ == "__main__":
    # 0. 准备工作
    if not os.path.exists("test_image.jpg"):
        print("⚠️ 请先找一张图片，重命名为 'test_image.jpg' 放在当前目录下")
        exit()
        
    # 1. 加载本地模型
    vision_brain = init_vision_model()
    
    if vision_brain:
        # 2. 识别图片 (Edge)
        object_name = identify_image(vision_brain, "test_image.jpg")
        
        # 3. 生成内容 (Cloud)
        # 只有识别成功了，才去问 LLM
        creative_text = generate_creative_content(object_name)
        
        # 4. 展示结果
        print("\n" + "="*30)
        print("✨ AI 图咏 (AI Haiku) ✨")
        print("="*30)
        print(creative_text)
        print("="*30)
