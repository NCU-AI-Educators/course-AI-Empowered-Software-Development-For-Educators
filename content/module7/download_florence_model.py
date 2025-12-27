import logging
import os
import shutil
import sys
from unittest.mock import MagicMock

# 1. Mock flash_attn 模块，绕过 Mac 上无法安装的限制
# Florence-2 代码中有检测 flash_attn 的逻辑，但我们可以强制让它以为存在，
# 然后实际上它会由于 import 成功但功能缺失而 fallback 或者我们需要后续处理。
# 但通常 transformers 的 check_imports 只要能 import 就行。
sys.modules["flash_attn"] = MagicMock()
sys.modules["flash_attn"].__spec__ = MagicMock()  # transformers check usually checks __spec__

from transformers import AutoModelForCausalLM, AutoProcessor
from transformers.utils import logging as hf_logging

# 设置详细日志以显示下载进度
hf_logging.set_verbosity_info()
logging.basicConfig(level=logging.INFO)

# 建议使用 Base 版本，速度快且效果足够好
# Large 版本 (microsoft/Florence-2-large) 更大更慢，但在 Macbook 上如果不使用量化可能会比较卡顿
model_name = "microsoft/Florence-2-base"
save_directory = "./models/florence-2-base"

print(f"Plan to download {model_name}...")
print(f"Target directory: {save_directory}")

if os.path.exists(save_directory):
    print(f"Directory {save_directory} already exists.")
    choice = input("Redownload? (y/n): ")
    if choice.lower() != 'y':
        print("Skipping download.")
        exit()
    else:
        shutil.rmtree(save_directory)

print(f"Downloading {model_name} to {save_directory}...")
print("Note: This requires 'transformers>=4.42.0', 'timm', and 'einops'.")
print("Trying to connect to Hugging Face Hub... (If this hangs, check your proxy)")

try:
    # Florence-2 需要 trust_remote_code=True
    # resume_download=True 允许断点续传
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True, resume_download=True)
    processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True, resume_download=True)

    print("Saving model and processor locally...")
    model.save_pretrained(save_directory)
    processor.save_pretrained(save_directory)

    print("Download complete!")
    print(f"You can now load the model from: {save_directory}")

except Exception as e:
    print(f"Error downloading model: {e}")
    print("Please ensure you have installed the required dependencies:")
    print("pip install -U transformers timm einops")
