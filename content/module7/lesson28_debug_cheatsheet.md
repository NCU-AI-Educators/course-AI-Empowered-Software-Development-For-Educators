# 🚑 模块7 紧急调试手册 (Debug Cheat Sheet)

当你的代码跑不通时，请按顺序检查以下项目。

## 1. 常见报错：ModuleNotFoundError
**现象**: `ModuleNotFoundError: No module named 'openai'`  
**原因**: 没安装库，或者安装到了错误的 Python 环境。  
**解法**:
```bash
# 确保在 VS Code 的终端运行
pip install openai transformers pillow torch
```

## 2. 常见报错：API Key Error
**现象**: `AuthenticationError: Incorrect API key provided`  
**原因**: Key 填错了，或者复制时多了空格。  
**解法**:
*   检查 `api_key = "sk-..."` 引号里有没有多余空格。
*   检查是否欠费（SiliconFlow/DeepSeek 也有额度限制）。

## 3. 常见报错：Model Load Error
**现象**: `OSError: Can't load the configuration of './models/...'`  
**原因**: 本地模型路径不对，或者文件夹是空的。  
**解法**:
*   确认 `models` 文件夹就在你的 `.py` 文件旁边。
*   确认文件夹里有 `config.json`, `model.safetensors` 等文件，而不是空的。

## 4. 常见报错：JSONDecodeError
**现象**: `json.decoder.JSONDecodeError`  
**原因**: 你想解析 AI 的回复，但 AI 回复了多余的话（例如 "好的，这是 JSON..."）。  
**解法**:
*   修改 Prompt：**"只输出 JSON，不要废话。"**
*   把 `temperature` 调低到 `0.1`。
*   在代码里用 `.replace()` 清理 ` ```json ` 标记。

## 5. 常见现象：程序卡住不动
**现象**: 终端显示 `Processing...` 然后几分钟没反应。  
**原因**: 
*   **本地**: 图片太大，或者电脑在下载模型。
*   **云端**: 网络不通，或者 DeepSeek 服务繁忙。  
**解法**:
*   加 `print()`！在每一行关键代码前加 `print("Step 1 done")`，看它卡在哪一步。
*   如果是第一次运行本地模型，它可能在后台联网验证，断网试试。
