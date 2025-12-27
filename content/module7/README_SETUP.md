# 黑客松启动指南 (Hackathon Setup Guide)

## 0. 环境准备
在开始之前，请确保你的电脑上安装了 `openai` 库。这是连接云端大脑的钥匙。

打开终端 (Terminal) 或 VS Code 的终端，运行：
```bash
pip install openai
```

## 1. 填入你的 Key
打开 `hackathon_utils.py`，找到 `API_KEY` 这一行，填入你的 DeepSeek 或 SiliconFlow 的 Key。

```python
API_KEY = "sk-xxxxxxxxxxxx" 
```

## 2. 选择你的赛道
- **赛道 A (效率)**: 运行 `python starter_kit_productivity.py`
- **赛道 B (创意)**: 运行 `python starter_kit_creative.py`
- **赛道 C (暖心)**: 运行 `python starter_kit_empathy.py`

## 3. 开始你的创作
不要修改 `hackathon_utils.py`。
你的战场在 `starter_kit_*.py` 里。
去修改 `prompt`，指挥 AI 完成你想要的任务！
