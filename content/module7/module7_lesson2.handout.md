---
marp: true
theme: A4
paginate: true
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
<style>
/* 盒子通用样式 */
.styled-box {
  display: block; padding: 0.2em 1.2em; margin-top: 1em; border-left: 5px solid;
  font-size: 0.42em; color: #333; border-radius: 5px; line-height: 1.6;
}
.styled-box p, .styled-box ul, .styled-box ol, .styled-box li {
  font-size: inherit !important; margin-block-start: 0.5em !important; margin-block-end: 0.5em !important;
}
/* 减小盒子内列表的左侧缩进 */
.styled-box ul, .styled-box ol {
  padding-inline-start: 18px;
}
.styled-box .box-title { display: block; margin-bottom: 0.5em; font-size: 1.1em; font-weight: bold; }

/* 不同盒子内的内容高亮(strong)分别定义颜色 */
.explanation-box { background: #fffbe6; border-color: #ffd33a; }
.explanation-box .box-title { color: #d98200; }
.explanation-box p strong, .explanation-box li strong { color: #BF7F00; font-weight: bold; }

.note-box { background: #e6f7ff; border-color: #1890ff; }
.note-box .box-title { color: #0050b3; }
.note-box p strong, .note-box li strong { color: #003a8c; font-weight: bold; }

.activity-box { background: #f6ffed; border-color: #52c41a; }
.activity-box .box-title { color: #237804; }
.activity-box p strong, .activity-box li strong { color: #135200; font-weight: bold; }

.design-box { background: #fdf2f8; border-color: #eb4899; }
.design-box .box-title { color: #9d2667; }
.design-box p strong, .design-box li strong { color: #780650; font-weight: bold; }

/* --- 专门为盒子内的H3标题设计的样式 --- */
.styled-box h3 {
  font-size: 1.2em; /* 相对于盒子的基础字号，比正文稍大 */
  color: #d98200; /* 与解释盒子的主题色一致 */
  margin-top: 0.8em;
  margin-bottom: 0.4em;
  padding-bottom: 0.2em;
  border-bottom: 1px solid #ffd33a; /* 添加一条细下划线 */
  font-weight: bold;
}

/* --- A4主题 H1 字体大小修正 --- */
h1 {
  font-size: 1.5em;
}

/* --- 列表缩进样式修正 --- */
.columns table {
  font-size: 14px; /* 调整为更合适的字体大小 */
  width: 100%;
}
.columns table th, .columns table td {
  padding: 6px 8px; /* 适当减小内边距 */
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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是 Pipeline (流水线)?
在软件工程中，Pipeline 指的是将多个处理步骤串联起来，前一个步骤的输出作为后一个步骤的输入。
就像工厂流水线：
1.  **原材料**: 图片
2.  **第一站 (Florence-2)**: 变成英文描述
3.  **第二站 (DeepSeek)**: 变成中文翻译
4.  **第三站 (TTS)**: 变成语音
这种思维方式能让我们组合现有工具，构建出复杂的应用。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 集成 (Integration) vs 创造 (Creation)
在现代软件开发中，我们很少从零开始写算法（造轮子）。
更多时候，我们是在做**集成**：把别人写好的、顶尖的轮子（模型/API）组装成一辆车。
这种能力被称为“集成能力”，它是 AI 时代开发者最重要的核心竞争力。

</div>

---

## **1. 痛点分析: 单体模型的局限**
### **Florence-2 的长板与短板**
<div class="columns ratio-6-4" style="font-size:0.9em">
<div>

*   ✅ **长板**: 视觉理解能力极强 (SOTA级别)，且能本地运行，速度快。
*   ❌ **短板 1**: 中文支持较弱，生成的描述主要是英文。
*   ❌ **短板 2**: **没有“嘴巴”**。它只能输出文字，无法直接生成语音（TTS）。

<div class="tip" style="font-size: 0.6em;">

**不要试图让一个 AI 做所有事**
就像我们不要求语文老师也会修电脑一样。
专业的 AI 做专业的事，然后通过 **Python** 把它们粘合起来。

</div>
</div>
<div>

![1766162289812](image/module7_lesson2.master/1766162289812.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要组合模型？
现在的 AI 发展趋势是**MoE (Mixture of Experts)**，即专家混合。
虽然 GPT-5 这样的模型很全能，但它很贵且慢。
在实际开发中，我们更倾向于用小而精的模型组合：
- 一个小模型专门看图（快、便宜）。
- 一个小模型专门翻译（准、便宜）。
组合起来的效果往往比一个超大模型更好，而且成本更低。

</div>

---

## **2. 解决方案: 接力赛 (Relay)**

<div class="align-center">

![width:850px](image/module7_lesson2.master/1766159918734.png)
</div>

*   **第一棒 (Vision)**: Florence-2，负责“看”。
*   **第二棒 (Language)**: Translation Model (如 DeepSeek)，负责“翻译”和“润色”。
*   **第三棒 (Voice)**: TTS Model (如 CosyVoice)，负责“说话”。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据流 (Data Flow)
在 Pipeline 中，数据就像水管里的水。
- Florence-2 的**输出**（英文文本），必须变成 DeepSeek 的**输入**。
- DeepSeek 的**输出**（中文文本），又是 CosyVoice 的**输入**。
确保这些“接口”对接严丝合缝（格式正确），是 Pipeline 能跑通的关键。

</div>

---

## **3. 验证第二棒的可行性**
### **Prompt Strategy (Translation Task)**
<div class="columns" style="font-size:0.8em">
<div class="styled-div" style="font-size: 0.6em;">

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

<div class="tip" style="font-size: 0.6em;">

**Tips for Prompting**:
*   **明确 SDK**: 指定 `openai` SDK 可以避免 AI 生成 `requests` 这种底层的 HTTP 请求代码。
*   **指定厂商参数**: 不同的模型服务商 (SiliconFlow, DeepSeek, Moonshot) 只有 Base URL 和 Model Name 不同，代码逻辑是一模一样的。
*   **安全意识**: 始终告诉 AI "从环境变量读取 Key"，养成好习惯。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### SDK vs API
- **API (接口)**: 是服务员。你对他喊话（发送 HTTP 请求）。
- **SDK (工具包)**: 是你的私人助理。他帮你去喊服务员。
直接用 `requests` 库调用 API 比较麻烦（要自己处理格式、错误）。
使用官方提供的 SDK（这里是 `openai` 库），就像有了私人助理，你只管下命令，脏活累活他都包了。

</div>

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

<div class="insight" style="font-size: 0.6em;">

**为什么是 OpenAI SDK?**
虽然我们用的是 DeepSeek 或其他国产模型，但 `openai` Python 库已经成为业界标准。
**学会这一个库，你就能调用世界上 99% 的大模型。**

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是 OpenAI 兼容接口?
OpenAI 是 AI 界的领头羊，它的接口格式定义得非常好。
后来所有的 AI 公司（包括国内的 DeepSeek, 阿里等）为了方便开发者迁移，都主动兼容了这个格式。
这就像 USB 接口一样，不管是哪个牌子的鼠标，只要是 USB 接口插上就能用。

</div>

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

<div class="insight" style="font-size: 0.6em;">

**Success!** 
看到这行中文，说明你的 Python 代码已经成功连接到了云端的 DeepSeek 大脑。
接下来，我们只需要把这个 `translate()` 函数，拼接到 Florence-2 的后面即可。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 环境变量 (Environment Variables)
这是操作系统层面的一种“便签条”。
我们把密码写在操作系统的设置里，而不是写在代码文件里。
代码运行时，会去问操作系统：“那个叫 API_KEY 的密码是多少？”
这样做的好处是，代码文件可以安全地分享给别人，而不会泄露你的私人密码。

</div>

---

## **6. 执行集成方案**
### **Prompt Strategy (Integration)**
<div class="columns" style="font-size:0.8em">
<div class="styled-div" style="font-size: 0.6em;">

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

<div class="tip" style="font-size: 0.6em;">

**为什么这么问？**
*   **提供上下文**: 告诉 AI 你手里已经有什么 (Base Code)。
*   **明确目标**: 告诉 AI 具体的修改点 (Add Function, Modify Logic)。
*   **指定格式**: 告诉 AI 期望的输出格式 (Bilingual)。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要单独测试？
新手常犯的错误是写完几百行代码再运行，结果报错了不知道是哪里的问题。
**模块化测试**（先测翻译，再测视觉，最后测拼装）是软件工程的黄金法则。
这就像造汽车，先把发动机点火试一下，确认能转，再把它装进车身里。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 接口拆分的意义
在真实的 App 开发中，网络环境是不稳定的。
上传图片（大文件）很容易失败。
如果把所有功能捆绑在一个接口里，一旦最后一步翻译超时，前面的图片上传也白费了。
拆分后，每一步都是独立的存档点，程序更健壮。

</div>

---

## **8. 再次迭代: 引入语音合成 (TTS)**

<div class="columns">
<div style="font-size:0.7em;">

### **Prompt Strategy (Iteration)**
现在我们已经有了中文翻译，最后一步是把它变成语音。请向 AI 提问：
> "**在现有的 `lesson26_ai_vision_translator.py` 基础上:**
> 1. 请引入 `CosyVoice2-0.5B` 模型 (SiliconFlow API)。
> 2. 增加一个 `/speak` 接口，接收文本，返回 MP3 音频流。
> 3. 更新 `lesson26.html`，在显示中文后自动播放音频。"

</div>
<div>

<div class="tip" style="font-size: 0.6em;">

**迭代技巧**:
*   **增量开发**: 不要从头重写，而是在现有代码上 "Add functionality"。
*   **指定模型**: 明确指定使用 `CosyVoice2` (支持方言、情感控制和音色自定义)。
*   **前端联动**: 提醒 AI 记得更新前端逻辑 (Autoplay)。

</div>

<div class="insight" style="font-size: 0.6em;">

**高手挑战 (Optional)**:
如果是配置较高的电脑 (NVIDIA GPU)，可以尝试本地部署 **Fun-CosyVoice 3.0** (2025年12月发布)。
它是目前开源界最强的语音模型，音质和情感表现力甚至超过云端版本。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 语音合成 (TTS - Text to Speech)
这是让机器“开口说话”的技术。
早期的 TTS 听起来像机器人（单调、无感情）。
现在的 TTS（如 CosyVoice）利用大模型技术，能理解文本的情感色彩，甚至可以模仿特定的音色。
引入 TTS 是实现“无障碍访问”的重要一步。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 流式处理 (Streaming)
就像看在线视频一样。
你不需要把整部电影下载完才能看，而是缓冲一点看一点。
对于语音生成，流式处理能让首字延迟 (TTFB) 降到毫秒级，实现即时对话的感觉。

</div>

---

## **课程小结**

<div class="columns" style="font-size:0.8em">
<div class="styled-div" style="font-size:0.7em;">

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 端云协同 (Edge-Cloud Collaboration)
本节课演示了一个典型的端云协同架构：
- **端 (Edge)**: 本地 PC 运行视觉模型，保护隐私（图片不上传到公有云 AI），无需网络也能识别。
- **云 (Cloud)**: 调用云端大模型进行深加工（翻译、语音），利用云端强大的算力。
这是未来 AI 应用的主流架构。

</div>