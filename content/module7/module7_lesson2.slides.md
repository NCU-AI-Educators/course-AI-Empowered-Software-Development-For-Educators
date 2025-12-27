---
marp: true
theme: default
paginate: true
size: 16:9
math: katex
---

<style>
/* --- 布局辅助样式 --- */
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.columns pre code {
  white-space: pre-wrap !important;
  overflow-wrap: break-word !important;
}
/* --- 列表缩进样式修正 --- */
ul, ol {
  padding-inline-start: 25px; /* 减小列表的左侧缩进 */
}
.columns.ratio-4-6 { grid-template-columns: 4fr 6fr; }
.columns.ratio-6-4 { grid-template-columns: 6fr 4fr; }
.columns.ratio-3-7 { grid-template-columns: 3fr 7fr; }
.columns.ratio-7-3 { grid-template-columns: 7fr 3fr; }
.align-top    { display: flex; align-items: flex-start; }
.align-middle { display: flex; align-items: center; }
.align-bottom { display: flex; align-items: flex-end; }
.align-left   { display: flex; justify-content: flex-start; }
.align-center { display: flex; justify-content: center; }
.align-right  { display: flex; justify-content: flex-end; }
.align-top-left     { display: flex; justify-content: flex-start; align-items: flex-start; }
.align-top-center   { display: flex; justify-content: center;  align-items: flex-start; }
.align-top-right    { display: flex; justify-content: flex-end;   align-items: flex-start; }
.align-middle-left  { display: flex; justify-content: flex-start; align-items: center; }
.align-middle-center{ display: flex; justify-content: center;  align-items: center; }
.align-middle-right { display: flex; justify-content: flex-end;   align-items: center; }
.align-bottom-left  { display: flex; justify-content: flex-start; align-items: flex-end; }
.align-bottom-center{ display: flex; justify-content: center;  align-items: flex-end; }
.align-bottom-right { display: flex; justify-content: flex-end;   align-items: flex-end; }
.tip {
  background-color: #f0f8ff;
  border-left: 5px solid #1e90ff;
  padding: 15px;
}
.insight {
  background-color: #eefcff; 
  border-left: 5px solid #17a2b8; 
  padding: 15px; 
}
.key-point {
  background-color: #fffbe6; 
  border-left: 5px solid #ffc107; 
  padding: 15px; 
}
.tip p, .tip li,
.insight p, .insight li,
.key-point p, .key-point li {
  font-size: inherit !important;
}
.styled-div p, 
.styled-div li, 
.styled-div ol, 
.styled-div ul, 
.styled-div blockquote {
  font-size: inherit !important;
}
.styled-div h3 {
  font-size: 1.2em; 
}

</style>

![bg blur:3px brightness:60%](image/module7_lesson2.master/1766159260202.png)

<style scoped>
h1{
  color: #F5F5F5;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}
h2 {
  color: #E0E0E0;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}
.course-title {
  position: absolute;
  top: 60px;
  left: 80px;
  background-color: rgba(0, 0, 0, 0.4);
  color: #fff;
  padding: 8px 15px;
  border-radius: 5px;
  font-size: 22px;
  font-weight: bold;
  letter-spacing: 1px;
  border-left: 5px solid #4CAF50;
}
</style>

<div class="course-title">AI赋能软件开发</div>

# 模块七: AI 应用黑客松
## 第26节: AI 协作与流水线思维 (Pipeline)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<!--
(1分钟) 各位老师好！欢迎回来。
上节课我们成功让电脑“看懂”了图片，但大家可能发现了一个小遗憾：
Florence-2 是个“外国人”，它生成的描述全是英文。
如果我们想做一个给中国学生用的识图工具，甚至想让它用中文朗读出来，该怎么办？
是重新训练一个懂中文的模型吗？太难了。
这节课，我们要学习一种更聪明的做法——**Pipeline（流水线）思维**。
既然它只会说英文，那我们就给它配一个翻译官，再配一个播音员。
-->

---

## **本节目标: 搭建你的第一条 AI 流水线**

<div class="columns">
<div>

1.  **Pipeline 思维**: 理解如何像搭积木一样串联多个 AI 模型。
2.  **体验 Translation API**: 学习如何调用擅长文本处理的 LLM (如 DeepSeek/GPT)。
3.  **动手实践**: 编写 `lesson26_ai_vision_translator.py`，实现“看图 -> 英文 -> 中文 -> 语音”的全自动流程。

</div>
<div>

![1766160140340](image/module7_lesson2.master/1766160140340.png)
</div>
</div>

<!--
(1分钟) 这节课的目标非常明确：我们要把几个独立的 AI 模型串起来。
就像搭积木一样。
第一块积木是“眼睛”（Florence-2），负责看。
第二块积木是“大脑”（DeepSeek），负责翻译和润色。
我们甚至可以加第三块积木——“嘴巴”（CosyVoice），负责读出来。
作为开发者，你的工作不是去造积木，而是设计这条流水线，让它们配合好。
-->

---

## **1. 痛点分析: 单体模型的局限**
### **Florence-2 的长板与短板**
<div class="columns ratio-6-4" style="font-size:0.9em">
<div>

*   ✅ **长板**: 视觉理解能力极强 (SOTA级别)，且能本地运行，速度快。
*   ❌ **短板 1**: 中文支持较弱，生成的描述主要是英文。
*   ❌ **短板 2**: **没有“嘴巴”**。它只能输出文字，无法直接生成语音（TTS）。

<div class="tip">

**不要试图让一个 AI 做所有事**
就像我们不要求语文老师也会修电脑一样。
专业的 AI 做专业的事，然后通过 **Python** 把它们粘合起来。

</div>
</div>
<div>

![1766162289812](image/module7_lesson2.master/1766162289812.png)

</div>
</div>

<!--
(2分钟) 我们先来分析一下为什么要这么做。
Florence-2 虽然看图很准，但它有两个致命的短板：
第一，它是微软在英文数据集上训练的，中文能力很弱。
第二，它只有“眼睛”和“手”，没有“嘴巴”。它写出的描述只能看，不能听。
如果我们非要强迫一个视觉模型去练口语或者说中文，效果会非常差。
这就像学校里，你不能要求体育老师教数学。
正确的做法是：**专业的人做专业的事**。
看图交给 Florence-2，翻译交给 DeepSeek，说话交给 CosyVoice。
这就是软件架构中的**“关注点分离” (Separation of Concerns)**。
-->

---

## **2. 解决方案: 接力赛 (Relay)**

<div class="align-center">

![width:850px](image/module7_lesson2.master/1766159918734.png)
</div>

*   **第一棒 (Vision)**: Florence-2，负责“看”。
*   **第二棒 (Language)**: Translation Model (如 DeepSeek)，负责“翻译”和“润色”。
*   **第三棒 (Voice)**: TTS Model (如 CosyVoice)，负责“说话”。

<!--
(1分钟) 这张图展示了我们的方案：一场接力赛。
第一棒 Florence-2 拿到图片，跑出一段英文描述。
然后它把接力棒（英文文本）传给第二棒 DeepSeek，DeepSeek 把它加工成优美的中文。
最后，第三棒 CosyVoice 接过中文文本，把它变成悦耳的语音读出来。
我们的 Python 代码，就是那个负责传递接力棒的运动员。
-->

---

## **3. 验证第二棒的可行性**
### **Prompt Strategy (Translation Task)**
<div class="columns" style="font-size:0.8em">
<div>

把你的需求描述给 DeepSeek/ChatGPT：
> "请帮我写一个 Python 脚本，调用 SiliconFlow 的 API 进行文本翻译。
> **要求**:
> 1. 使用 `openai` 官方 SDK (不要用 requests)。
> 2. Base URL 设置为 `https://api.siliconflow.cn/v1`。
> 3. 模型使用 `deepseek-ai/DeepSeek-V3.2`。
> 4. 封装一个函数 `translate(text)`，输入英文，返回中文。
> 5. **注意**: API Key 请从环境变量读取，不要硬编码。"

</div>
<div>

<div class="tip">

**Tips for Prompting**:
*   **明确 SDK**: 指定 `openai` SDK 可以避免 AI 生成 `requests` 这种底层的 HTTP 请求代码。
*   **指定厂商参数**: 不同的模型服务商 (SiliconFlow, DeepSeek, Moonshot) 只有 Base URL 和 Model Name 不同，代码逻辑是一模一样的。
*   **安全意识**: 始终告诉 AI "从环境变量读取 Key"，养成好习惯。

</div>

</div>
</div>

<!--
(2分钟) 我们先单独测试第二棒。
我们要写一个 Python 脚本来调用 DeepSeek 进行翻译。
注意看这个 Prompt，我有几个特殊要求：
第一，用 `openai` 官方库。虽然我们调用的不是 OpenAI 的模型，但这个库是通用的，学会了它，你就能调用几乎所有的大模型。
第二，**API Key 不要写死在代码里**。这很重要，万一你把代码发给别人，Key 就泄露了。我们要从环境变量里读取。
-->

---

## **4. 代码解析: OpenAI SDK (通用语)**

为了调用第二棒的翻译能力，我们需要使用一套标准接口。

<div class="columns">
<div>

```python
from openai import OpenAI
import os

# SiliconFlow (硅基流动) 配置
# 最佳实践: 从环境变量读取 Key，不直接写在代码里
client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"), 
    base_url="https://api.siliconflow.cn/v1"
)

def translate(text):
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2", # 选择了便宜又强大的模型
        messages=[
            {"role": "user", "content": f"翻译成中文: {text}"}
        ]
    )
    return response.choices[0].message.content
```

</div>
<div>

<div class="insight">

**为什么是 OpenAI SDK?**
虽然我们用的是 DeepSeek 或其他国产模型，但 `openai` Python 库已经成为业界标准。
**学会这一个库，你就能调用世界上 99% 的大模型。**

</div>

</div>
</div>

<!--
(3分钟) 这段代码是所有大模型开发的通用模板。请大家把它刻在脑子里，或者收藏起来。
1.  `client = OpenAI(...)`: 建立连接。这里我们连的是 SiliconFlow 的服务器，而不是美国的 OpenAI。
2.  `chat.completions.create(...)`: 发送任务。
    - `model`: 告诉它你要点哪个“厨师”（这里是 DeepSeek-V3.2）。
    - `messages`: 你的指令。`role: user` 代表你，`content` 是你要说的话。
只要替换 `base_url` 和 `model`，这段代码可以用来调用 Kimi, 智谱, 阿里通义千问等任何模型。
-->

---

## **5. 运行测试: 你的第一个云端调用**

在开始复杂的 Pipeline 之前，先确保我们的“翻译官”能正常工作。

<div class="columns">
<div>

### **Terminal (执行)**
```bash
# 1. 确保已设置 Key (Mac/Linux)
export SILICONFLOW_API_KEY="sk-..."

# Windows PowerShell:
# $env:SILICONFLOW_API_KEY="sk-..."

# 2. 运行脚本
python lesson26_cloud_api.py
```

</div>
<div>

### **Output (预期结果)**
```text
当前使用的模型: deepseek-ai/DeepSeek-V3.2
------------------------------
🔤 原文: Artificial Intelligence is the new electricity.
☁️ 正在请求 SiliconFlow 翻译...
🇨🇳 译文: 人工智能是新时代的电力。
------------------------------
```

<div class="insight" style="font-size:0.8em">

**Success!** 
看到这行中文，说明你的 Python 代码已经成功连接到了云端的 DeepSeek 大脑。
接下来，我们只需要把这个 `translate()` 函数，拼接到 Florence-2 的后面即可。

</div>

</div>
</div>

<!--
(2分钟) 现在动手试一下。
首先在终端设置好环境变量（根据你的操作系统选择命令）。
然后运行脚本。
如果你看到了中文输出，恭喜你！你已经打通了云端大脑的连接。
现在我们手里有两块积木了：
积木A：看图（Lesson 25 代码）。
积木B：翻译（现在的代码）。
下一步，拼起来！
-->

---

## **6. 执行集成方案**
### **Prompt Strategy (Integration)**
<div class="columns" style="font-size:0.8em">
<div>

现在我们需要把第一棒 (Florence-2) 和第二棒 (Translation) 粘合起来。
请指挥 AI ：
> "**我现有的代码 (`lesson25_mobile_demo.py`) 只能生成英文描述。**
> **请帮我修改它:**
> 1. 引入 `openai` 库。
> 2. 增加一个 `translate_text(text)` 函数，调用 SiliconFlow API。
> 3. 在 `upload_image` 函数中，拿到 Florence-2 的结果后，立即调用翻译函数。
> 4. API 返回的 JSON中 `label` 字段需要包含中英双语。"

</div>
<div>

<div class="tip">

**为什么这么问？**
*   **提供上下文**: 告诉 AI 你手里已经有什么 (Base Code)。
*   **明确目标**: 告诉 AI 具体的修改点 (Add Function, Modify Logic)。
*   **指定格式**: 告诉 AI 期望的输出格式 (Bilingual)。

</div>

</div>
</div>

<!--
(2分钟) 这一步是关键。我们要让 AI 帮我们合并代码。
打开你上节课写的 `lesson25_mobile_demo.py`。
然后把 Prompt 发给 AI。
注意我是怎么提问的：
“我现有的代码是...请帮我修改...”
这种基于**现有代码 (Context)** 的提问方式，能让 AI 生成的结果直接可用，不需要你再去手动拼贴。
-->

---

## **7. 代码解析: AI Vison Translator**
**任务清单**:
<div class="columns ratio-4-6">
<div>

1.  **拆分**: 将原来的单一接口拆分为视觉与翻译两个独立服务。
2.  **视觉接口**: `/upload` 只负责“看”，虽然慢但**免费且隐私** (运行在本地)。
3.  **翻译接口**: `/translate` 只负责“想”，虽然要花钱但**智能** (运行在云端)。

</div>
<div>

```python
# 1. 视觉接口 (本地/免费)
@app.post("/upload")
async def upload_image(file: UploadFile):
    # Florence-2 ...
    return {"caption_en": "A tree..."}

# 2. 翻译接口 (云端/智能)
@app.post("/translate")
async def translate_text(request: TranslationRequest):
    # DeepSeek-V3.2 ...
    zh = call_cloud_api(request.text)
    return {"caption_zh": zh}
```

</div>
</div>

<!--
(3分钟) AI 可能会给你生成一个大函数，但更优雅的设计是拆分成两个接口。
为什么？
想象一下，如果用户觉得翻译得不好，想换个说法。
如果合在一起，用户得重新上传图片、重新识别（很慢），才能得到新翻译。
如果分开：
1. `/upload`: 传图 -> 得到英文 (本地跑，不要钱)。
2. `/translate`: 发送英文 -> 得到中文 (云端跑，极快)。
用户可以对同一段英文反复请求翻译，而不需要重复识别图片。这就是架构设计的**灵活性**。
-->

---

## **8. 再次迭代: 引入语音合成 (TTS)**

<div class="columns">
<div style="font-size:0.9em">

### **Prompt Strategy (Iteration)**
现在我们已经有了中文翻译，最后一步是把它变成语音。请向 AI 提问：
> "**在现有的 `lesson26_ai_vision_translator.py` 基础上:**
> 1. 请引入 `CosyVoice2-0.5B` 模型 (SiliconFlow API)。
> 2. 增加一个 `/speak` 接口，接收文本，返回 MP3 音频流。
> 3. 更新 `lesson26.html`，在显示中文后自动播放音频。"

</div>
<div>

<div class="tip" style="font-size:0.8em">

**迭代技巧**:
*   **增量开发**: 不要从头重写，而是在现有代码上 "Add functionality"。
*   **指定模型**: 明确指定使用 `CosyVoice2` (支持方言、情感控制和音色自定义)。
*   **前端联动**: 提醒 AI 记得更新前端逻辑 (Autoplay)。

</div>

<div class="insight" style="font-size:0.8em">

**高手挑战 (Optional)**:
如果是配置较高的电脑 (NVIDIA GPU)，可以尝试本地部署 **Fun-CosyVoice 3.0** (2025年12月发布)。
它是目前开源界最强的语音模型，音质和情感表现力甚至超过云端版本。

</div>

</div>
</div>

<!--
(2分钟) 我们再加一块积木：语音合成 (TTS)。
我们要让这个应用不仅能看、能写，还能说。
我们选用 `CosyVoice2` 模型，这是阿里出的，声音非常自然，不像传统的机器人音。
继续向 AI 提问，要求在现有代码上增加 `/speak` 接口。
注意，这次我们要处理的是**音频流 (Stream)**，不是文本。
-->

---

## **9. 终极形态: 看图说话 (TTS)**

<div class="columns">
<div>

**代码解析**:
1.  **引入**: CosyVoice2 (阿里/SiliconFlow)。
2.  **流式响应**: 使用 `StreamingResponse` 实现边生成边播放 (降低延迟)。
3.  **闭环**: `Vision` -> `Text` -> `Speech`。

```python
# 3. 语音接口 (让它说话!)
@app.post("/speak")
async def speak(request: TTSRequest):
    # CosyVoice2-0.5B (支持情感)
    client = OpenAI(base_url=SILICONFLOW_BASE_URL, ...)
    # 返回音频流
    return StreamingResponse(
        generate_audio(request.text), 
        media_type="audio/mpeg"
    )
```
</div>
<div>

![1766160768363](image/module7_lesson2.master/1766160768363.png)

</div>
</div>

<!--
(3分钟) 看一下这段代码。
这里有个新概念：`StreamingResponse`。
音频文件通常比较大，如果等生成完了再发给用户，用户要等好几秒。
流式响应就像流水一样，生成一点发一点，用户可以一边下载一边听，体验非常丝滑。
现在，运行你的终极代码。
打开网页，传一张照片。
闭上眼睛，听。你的电脑正在用流利的中文告诉你，它看到了什么。
-->

---

## **课程小结**

<div class="columns" style="font-size:0.8em">
<div>

### **关键点**
1.  **Pipeline 思维**: 复杂问题拆解，让专业的模型做专业的事。
2.  **端云结合**: 本地模型 (Florence) 负责隐私/重资产任务，云端模型 (API) 负责高智商/文本任务。
3.  **无限可能**: 一旦学会了串联，你就可以像搭积木一样创造无限的应用。

### **下节预告**
有了想法，如何快速把它们变成现实？
接下来，我们将进行 **Ideation Workshop (创意工坊)**，尝试用“工程思维”来解构教学场景中的真痛点。

</div>
<div class="align-middle">

![1766161386096](image/module7_lesson2.master/1766161386096.png)

</div>
</div>

<!--
(1分钟) 第二节课的内容就到这里。
这节课我们不仅写了一个翻译功能，更重要的是掌握了“集众智”的能力。
本地的 Florence 就像是你的眼睛，云端的 DeepSeek 就像是你的大脑，而 CosyVoice 则是你的嘴巴。
当你把它们连起来的时候，你就拥有了一个完整的数字生命体。
保持这份兴奋，稍事休息，下一节课我们要开始搞创意了！
-->