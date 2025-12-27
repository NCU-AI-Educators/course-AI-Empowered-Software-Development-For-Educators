from openai import OpenAI
import os

# ==========================================
# 🎯 配置区域 (Hands-on Area)
# ==========================================

# 1. 设置 API Key (这是你的云端通行证)
# 教学提示: 实际开发中，千万不要把 Key 直接写在代码里传到 GitHub！
# 推荐使用环境变量: os.getenv("SILICONFLOW_API_KEY") 或 os.getenv("OPENAI_API_KEY")
api_key = os.getenv("SILICONFLOW_API_KEY") or os.getenv("OPENAI_API_KEY") 

# 2. 设置 Base URL (指向国内服务商，例如 SiliconFlow 或 DeepSeek)
# SiliconFlow 示例: https://api.siliconflow.cn/v1
# DeepSeek 示例: https://api.deepseek.com
base_url = "https://api.siliconflow.cn/v1"

# 3. 选择模型 (Model Name)
# 免费/低价模型示例: "deepseek-ai/DeepSeek-V3.2", "Qwen/Qwen2.5-7B-Instruct"
model_name = "deepseek-ai/DeepSeek-V3.2"

# ==========================================
# 🚀 核心逻辑 (Core Logic)
# ==========================================

def translate(text):
    """
    我们将上面 "Code Analysis" 中学到的代码直接拿来用
    """
    # 初始化客户端
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    print(f"☁️ 正在请求 SiliconFlow 翻译: '{text}' ...")
    
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "user", "content": f"翻译成中文: {text}"},
            ],
            stream=False
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ 翻译失败: {str(e)}"

# ==========================================
# 🎮 运行测试 (Main)
# ==========================================

if __name__ == "__main__":
    print(f"当前使用的模型: {model_name}")
    print("-" * 30)
    
    english_text = "Artificial Intelligence is the new electricity."
    print(f"🔤 原文: {english_text}")
    
    chinese_text = translate(english_text)
    print(f"🇨🇳 译文: {chinese_text}")
    print("-" * 30)
