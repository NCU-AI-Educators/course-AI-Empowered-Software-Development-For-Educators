import os
import torch
import warnings
import sys
from unittest.mock import MagicMock
from PIL import Image
from transformers import AutoProcessor, AutoModelForCausalLM
from openai import OpenAI

# ==========================================
# 🔧 Environment Setup (Hidden from students)
# ==========================================

# 1. Enable MPS Fallback for Mac
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

# 2. Mock flash_attn for Mac compatibility
sys.modules["flash_attn"] = MagicMock()
sys.modules["flash_attn"].__spec__ = MagicMock()

# 3. Suppress Warnings
warnings.filterwarnings("ignore", category=UserWarning)

# ==========================================
# 🤖 Vision Model (Local Florence-2)
# ==========================================

def load_vision_model(model_path="./models/florence-2-base"):
    """
    Load Florence-2 model with automatic device detection (MPS/CPU).
    """
    print(f"🚀 Loading Vision Model from: {model_path} ...")
    
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    torch_dtype = torch.float16 if device != "cpu" else torch.float32
    
    try:
        if os.path.isdir(model_path):
             # Offline mode if local path exists
            model = AutoModelForCausalLM.from_pretrained(
                model_path, 
                trust_remote_code=True, 
                torch_dtype=torch_dtype,
                local_files_only=True
            ).to(device)
            processor = AutoProcessor.from_pretrained(
                model_path, 
                trust_remote_code=True,
                local_files_only=True
            )
        else:
            # Fallback to HuggingFace hub (not recommended for classroom)
            model_id = "microsoft/Florence-2-base"
            print(f"⚠️ Local model not found. Downloading {model_id}...")
            model = AutoModelForCausalLM.from_pretrained(
                model_id, trust_remote_code=True, torch_dtype=torch_dtype
            ).to(device)
            processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

        print(f"✅ Vision Model Loaded on {device.upper()}")
        return model, processor, device, torch_dtype
        
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return None, None, None, None

def analyze_image(model, processor, device, torch_dtype, image_path, prompt="<MORE_DETAILED_CAPTION>"):
    """
    Run inference on a single image.
    """
    if not os.path.exists(image_path):
        return f"Error: Image '{image_path}' not found."
        
    try:
        image = Image.open(image_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
            
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
        return parsed_answer[prompt]
        
    except Exception as e:
        return f"Error analyzing image: {e}"

# ==========================================
# 🧠 Language Model (Cloud API)
# ==========================================

def call_llm(system_prompt, user_prompt, model_name="deepseek-ai/DeepSeek-V3.2"):
    """
    Call Cloud API (SiliconFlow / DeepSeek) with robust key handling.
    """
    # Try both key names for compatibility
    api_key = os.getenv("SILICONFLOW_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = "https://api.siliconflow.cn/v1"
    
    print(f"☁️ Calling Cloud LLM ({model_name})...")
    
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Call Failed: {e} (Check API Key)"

# ==========================================
# 🔈 Speech Synthesis (Cloud API)
# ==========================================

def call_tts(text, output_filename="output.mp3", voice="FunAudioLLM/CosyVoice2-0.5B:anna"):
    """
    Call SiliconFlow TTS API (CosyVoice2).
    """
    api_key = os.getenv("SILICONFLOW_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = "https://api.siliconflow.cn/v1"
    
    print(f"🔈 Generating Speech ({len(text)} chars)...")
    
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        with client.audio.speech.with_streaming_response.create(
            model="FunAudioLLM/CosyVoice2-0.5B", 
            voice=voice,
            input=text, 
            response_format="mp3"
        ) as response:
            response.stream_to_file(output_filename)
            
        print(f"✅ Audio saved to: {output_filename}")
        return output_filename
    except Exception as e:
        print(f"❌ TTS Failed: {e}")
        return None
