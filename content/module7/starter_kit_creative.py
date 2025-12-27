import os
import time
from hackathon_utils import (
    load_vision_model, 
    analyze_image, 
    call_llm, 
    call_tts,
    setup_environment
)

# 1. 初始化 (One-time Setup)
setup_environment()
print("🎨正在加载视觉模型 (Florence-2)...")
vision_model, vision_processor = load_vision_model()

def generate_picture_book(image_path: str):
    """
    核心流程: 图片 -> 故事 -> 语音
    """
    print(f"\n📸 正在读取图片: {image_path}")
    
    # Step 1: Vision (看)
    # 使用 '<MORE_DETAILED_CAPTION>' 获取丰富细节，利于生成故事
    print("👀 AI正在观察图片细节...")
    start = time.time()
    caption = analyze_image(vision_model, vision_processor, image_path, "<MORE_DETAILED_CAPTION>")
    print(f"   [视觉结果]: {caption[:100]}... (耗时 {time.time()-start:.1f}s)")

    # Step 2: Story (想)
    print("🧠 AI正在构思童话故事...")
    prompt = f"""
    你是一位不仅充满想象力还非常有爱心的童话作家。
    请根据这张图片的描述，创作一个适合 5-8 岁儿童阅读的短篇童话故事。
    
    图片描述: {caption}
    
    要求:
    1. 故事要有起承转合，大约 150 字左右。
    2. 语言生动活泼，富有画面感。
    3. 最后给故事起一个可爱的标题。
    
    输出格式:
    标题: [标题]
    正文: [故事内容]
    """
    story_text = call_llm(prompt)
    print(f"\n📖 [生成的绘本故事]:\n{'-'*30}\n{story_text}\n{'-'*30}")

    # Extract clean text for TTS (remove label headers if present)
    tts_text = story_text.replace("标题:", "").replace("正文:", "").replace("\n", " ").strip()

    # Step 3: Speech (说)
    print("🎙️ AI正在朗读故事 (CosyVoice2)...")
    try:
        # 使用 'anna' 音色，适合讲故事
        audio_file = call_tts(tts_text[:500], output_filename="story_audio.mp3") 
        print(f"✅ 音频已生成: {audio_file}")
        
        # 自动播放 (Mac)
        os.system(f"afplay {audio_file}")
    except Exception as e:
        print(f"⚠️ 语音生成失败: {e}")

if __name__ == "__main__":
    # 示例图片 (请准备一张 capture.jpg 或修改路径)
    test_image = "capture.jpg"
    
    if not os.path.exists(test_image):
        print(f"❌ 未找到图片 {test_image}，请先拍一张照片！")
    else:
        generate_picture_book(test_image)
