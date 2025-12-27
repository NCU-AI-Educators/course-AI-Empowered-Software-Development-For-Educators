import json
from openai import OpenAI

# ==========================================
# 🔧 配置区域
# ==========================================
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # ⚠️ 替换你的 Key
BASE_URL = "https://api.siliconflow.cn/v1"
MODEL_NAME = "deepseek-ai/DeepSeek-V2.5"

def get_json_response(item_name):
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    
    # 💡 核心技巧: System Prompt 强力约束
    system_prompt = """
    你是一个数据提取助手。
    请务必只输出合法的 JSON 格式，不要包含任何 Markdown 标记（如 ```json），也不要任何多余的解释。
    格式要求: {"dish_name": "菜名", "ingredients": ["食材1", "食材2"], "difficulty": "难度(1-5)"}
    """
    
    user_prompt = f"我这儿有 {item_name}，推荐一道菜。"
    
    print(f"☁️ 正在询问云端 (Target: JSON Mode)...")
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            # 部分模型支持 response_format={"type": "json_object"}，这更稳
            # 这里为了通用性，主要靠 Prompt 约束
            temperature=0.1 # 温度低一点，输出更稳定
        )
        content = response.choices[0].message.content
        
        # 清洗数据 (防止 AI 还是加了 ```json )
        content = content.replace("```json", "").replace("```", "").strip()
        
        return content
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None

# ==========================================
# 🚀 测试解析
# ==========================================
if __name__ == "__main__":
    input_item = "Eggs and Tomatoes"
    json_str = get_json_response(input_item)
    
    if json_str:
        print("\n🔍 原始返回:")
        print(json_str)
        
        print("\n🧩 解析为 Python 字典:")
        try:
            # 尝试解析 JSON
            data = json.loads(json_str)
            print(f"菜名: {data['dish_name']}")
            print(f"难度: {'⭐' * int(data['difficulty'])}")
            print(f"食材: {', '.join(data['ingredients'])}")
            print("✅ 解析成功！可以传给前端显示了。")
        except json.JSONDecodeError:
            print("❌ 解析失败：AI 返回的不是标准 JSON。")
