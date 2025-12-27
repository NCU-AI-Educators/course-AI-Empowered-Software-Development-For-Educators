from hackathon_utils import load_vision_model, analyze_image, call_llm
import os

# ==========================================
# 🎓 Hackathon Track A: AI 助教 (作业批改)
# ==========================================

def main():
    print("="*50)
    print("🤖 Track A: AI Teaching Assistant Starting...")
    print("="*50)

    # 1. 准备工作: 加载眼睛 (Florence-2)
    api_key = os.getenv("SILICONFLOW_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ 错误: 请先设置环境变量 SILICONFLOW_API_KEY")
        return

    model, processor, device, dtype = load_vision_model()
    if not model:
        return

    # 2. 读取学生作业 (模拟)
    image_path = "student_homework.jpg"
    if not os.path.exists(image_path):
        print(f"⚠️ 找不到 {image_path}, 请放入一张图片!")
        # 这里为了演示，我们先不报错退出，而是提示用户
        return

    # 3. 步骤一: 识别 (OCR)
    print(f"\n📸 正在“阅读”学生作业: {image_path}...")
    ocr_result = analyze_image(model, processor, device, dtype, image_path, prompt="<OCR>")
    print(f"👁️ OCR 识别结果:\n{ocr_result[:200]}...") # 只打印前200个字符

    # 4. 步骤二: 批改 (LLM)
    print(f"\n🧠 正在“批改”作业 (调用 AI 老师)...")
    
    system_prompt = """
    你是一位耐心、专业的初中语文老师。
    你的任务是批改学生的作文片段。
    请按以下格式输出 Markdown 报告：
    1. **评分**: (满分100)
    2. **错别字/语病**: (指出具体位置和修改建议)
    3. **点评**: (先鼓励，再指出不足，最后给出一个具体的改进建议)
    """
    
    user_prompt = f"这是学生作业的 OCR 识别结果（可能包含识别错误，请自动忽略 OCR 乱码）：\n\n{ocr_result}"
    
    feedback = call_llm(system_prompt, user_prompt)
    
    # 5. 输出结果
    print("\n" + "="*30)
    print("📝 批改报告")
    print("="*30)
    print(feedback)
    
    # (可选) 保存为文件
    with open("grading_report.md", "w", encoding="utf-8") as f:
        f.write(feedback)
    print(f"\n✅ 报告已保存为 grading_report.md")

if __name__ == "__main__":
    main()
