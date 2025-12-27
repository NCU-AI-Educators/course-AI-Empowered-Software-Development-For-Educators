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
![bg blur:3px brightness:60%](image/module7_lesson3.master/1766169777940.png)

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
## 第27节: 创意工坊——跨学科融合与AI共创 (Ideation & Fusion)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 破冰 (Ice Breaking)
**去中心化**: 将课堂焦点从“讲师”转移到“学员共创”。
强调“跨学科融合”，鼓励不同背景的老师互动。

</div>

---

## **🎯 本课目标 (Goals)**

<div class="columns ratio-4-6">

<div>

### **1. 明确赛题**
了解三大赛道，选择适合自己学科的方向。

### **2. 跨学科组队**
找到不同背景的老师，碰撞出单一学科无法实现的火花。

### **3. 立项 MVP**
完成《产品一页纸》，定义我们要做的最小可行性产品。

</div>
<div>

<div class="tip" style="margin-top:1.0em;font-size: 0.6em;">

### **💡 什么是 Slow Hackathon?**
我们不搞 48 小时通宵开发。我们将黑客松拉长到这一周的课后时间。

- **这节课 (L27)**: 点子爆发，确定做什么。
- **下节课 (L28)**: 现场 写 Prompt，开发原型。

</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 规则说明 (Rules)
**降压**: 用 "Slow Hackathon" 的概念减轻学员的焦虑感，强调这是一个长周期的创造过程，而非短跑。

</div>

---

## **🛠️ 我们的智能工具箱 (Our AI Toolkit)**

在开始狂想之前，先看看我们手里有什么“积木”。**我们只需懂功能，无需懂代码！**

<div class="columns">

<div class="scaffold">

### **👁️ AI 之眼 (Vision)**
**能力**: 能够“看懂”图片并生成文字描述。

- **模型**: Florence-2-base (本地运行)
- **输入**: 手机拍照 / 上传图片
- **输出**: 详细的文字 Caption / 甚至是检测框
- **应用场景**: 阅卷、识物、看图说话...

</div>

<div class="scaffold">

### **🧠 AI 之脑 (Reasoning)**
**能力**: 能够进行逻辑推理、创作和格式化输出。

- **模型**: DeepSeek (云端最强大脑)
- **输入**: 文本 (提示词/Prompt) + 图片描述
- **输出**: 诗歌、结构化数据、建议、故事...
- **应用场景**: 判分、写评语、编故事...

</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 能力边界 (Capability Boundary)
**约束即创造**: 明确告知学员技术边界（只能做 Vision+Language），避免产生无法实现的天马行空的想法。

</div>

---

## **🏁 三大赛道 (The 3 Tracks)**

我们为大家提供了三个“赛道”，请根据兴趣选择。

<div class="track-card track-a">

### **Track A: 效率黑客**
**Efficiency/Productivity**
*"把重复劳动交给 AI，把时间还给自己。"*

- **场景**: 考勤、统计、初筛、办公
- **示例**: 
    - 上课前拍大屏幕上的动态加密内容上传，AI自动生成签到表。
    - 自动录音整理会议纪要。

</div>

---

<div class="track-card track-b">

### **Track B: 创意大师**
**Creative Muse**
*"让教学不仅有用，更有趣。"*

- **场景**: 英语、语文、历史、艺术
- **示例**: 
    - AI口语教练、AI听力教练、AI写作教练。
    - 拍古建筑，生成导游解说词。

</div>

---

<div class="track-card track-c">

### **Track C: 暖心助教**
**Empathy/Assistive**
*"科技不仅有智商，更有温度。"*

- **场景**: 心理健康、面试模拟
- **示例**: 
    - AI观察学生的肢体语言、眼神、表情，形成文字描述，进行心理健康评估。
    - AI与学生语音互动，分析学生语音，进行心理健康评估或模拟面试。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 分类引导 (Categorization)
通过三个赛道的划分，覆盖不同学科背景老师的需求：
- 理工科/行政 -> 效率
- 文史哲/艺术 -> 创意
- 心理/辅导员 -> 关怀

</div>

---

## **🌟 更多灵感 (Inspiration Hub)**

如果你还没有思路，看看这些“高玩”场景：

<div class="insight" style="font-size: 0.8em;">

### **🎙️ 场景一：AI 双人播客生成器（Track B: 创意大师）**
**输入**: 一个枯燥的学科知识点。  

**AI 流程**（可借助ComfyUI等内容生成工作流工具）:

1. **LLM**: 将知识点改编成对话脚本。
2. **TTS**: 调用两种不同音色（如 CosyVoice的自定义音色），生成双人对话音频。

**输出**: 一段生动有趣的 5 分钟教学播客。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 场景拓展 (Scenario)
**多模态组合**: 展示 "Text -> Script -> Audio" 的复杂工作流。
**价值点**: 解决教学资源制作成本高、周期长的痛点。

</div>

---

<div class="insight" style="font-size: 0.8em;">

### **👨‍🏫 场景二：AI 数字分身演讲（Track B: 创意大师）**
**输入**: 你的逐字稿 + 你的声音样本。  

**AI 流程**（可借助ComfyUI等内容生成工作流工具）:

1. **Voice Cloning**: AI 学习并模拟你的音色。
2. **Presentation**: 生成对应的 PPT 页面（可结合 Marp）。
3. **Synthesis**: 合成你的语音解说。

**输出**: 你不用出镜，也能做一个完美的 5 分钟微课。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 场景拓展 (Scenario)
**前沿技术**: 介绍 Voice Cloning 和 Digital Avatar 技术。
**效率革命**: 强调“一次采集，无限生成”的效率优势。

</div>

---

<div class="insight" style="font-size: 0.8em;">

### **🧠 场景三：AI 思维导图生成器（Track A: 效率黑客）**
**输入**: 一篇长文章或一段复杂的知识点文本。  

**AI 流程**:

1. **LLM**: 分析文本结构，提取关键节点，生成 Markdown/JSON 树状结构。
2. **Visualization**: 前端使用 Markmap/D3.js 将结构转化为可交互的导图。

**输出**: 一个可缩放、可折叠的 Web 思维导图。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 场景拓展 (Scenario)
**数据转换**: 展示 AI 在“非结构化文本 -> 结构化图表”转换中的能力。
**认知工具**: 强调思维导图在认知减负中的作用。

</div>

---

<div class="insight" style="font-size: 0.8em;">

### **🧠 场景四：AI 组卷（Track A: 效率黑客）**
**输入**: 一本教材和教学大纲。  

**AI 流程**（可借助 Dify 等低代码平台）:

1. **LLM**: 程序事先借助LLM分析教材和教学大纲提取知识点和文本块，然后程序按知识点搜索相关文本块，LLM再组合文本块生成题库。
2. **Visualization**: 网页前端。

**输出**: 一张符合教学设计的试卷。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 灵感激发 (Inspiration)
**案例教学**: 提供具体、可落地的案例，展示“现有技术”能组合出什么新花样。
**去魅**: 强调这些“高大上”的应用底层逻辑其实很简单。

</div>

---

## **🧠 疯狂 8 分钟 (Crazy 8s)**

现在的任务：**不要评判，只管想！** 拿出白纸，折成 8 格。

<div class="columns" style="font-size:0.95em">

<div>

### **规则：**

1.  **每格 1 分钟**: 强迫自己在 1 分钟内画出一个点子草图（火柴人也行！）。
2.  **不要停**: 哪怕是再离谱的想法也要画下来。
3.  **结合技术**: 想想 "识图 或 推理" 能解决什么以前解决不了的问题？

</div>

<div>

![width:500px](image/module7_lesson3.master/1766170113538.png)

</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 8分钟
### 环节: 头脑风暴 (Brainstorming)
**Design Sprint**: 引入设计冲刺方法论。
**时间压力**: 通过紧迫的时间限制，逼迫学员跳过“自我审查”，激发潜意识里的创意。

</div>

---

## **🤝 模拟组队 & 互评 (Peer Review)**

虽然学生不在现场，但我们可以先**模拟**这个过程。请和你的同桌（也是老师）组成临时搭档。

<div class="columns">

<div class="tip" style="font-size: 0.8em;">

### **推荐配置 (2人/组)**

- **A 老师 (领域专家)**: 提供核心痛点和学科知识（如：想解决古诗词画面感不强的问题）。
- **B 老师 (跨界顾问)**: 提供不同视角的思维激荡（如：物理老师建议用“光影变化”来解析古诗）。
- **AI (技术合伙人)**: 负责将创意转化为代码实现。

</div>

<div>

### 寻找队友：
🤝 **请寻找一位与你学科背景尽可能“反差大”的老师！**

文科 ⚡ 理科 | 艺术 ⚡ 工程

👉 **现在，只有 5 分钟，打破壁垒，找到你的搭档！**

</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 社交学习 (Social Learning)
**强制社交**: 逼迫学员走出舒适区，与其他学科的同事交流。
**角色互补**: 强调“反差”带来的价值。

</div>

---

## **📝 立项：产品一页纸 (The One-Pager)**

确定了队友和方向？请填写这张表，这就是你们的 **MVP (最小可行性产品)** 定义。

<div class="scaffold" style="font-size: 0.9em;">

### **📋 AI Hackathon MVP 定义表**

1.  **项目名称**: (e.g., "实验室里的“全能记录员” (The Lab Scribe)")
2.  **所属赛道**: (A/B/C)
3.  **用户是谁**: (e.g., 老师/学生)
4.  **核心痛点**: (e.g., 做实验时手忙脚乱，实验记录本记不全)
5.  **解决方案 (AI流)**:
    - **Input**: (手机在实验室录像，研究员口述操作)
    - **Vision AI**: (识别实验步骤，记录实验过程)
    - **Logic AI**: (对比标准过程，违规时给出提示)
    - **Output**: (在手机上显示违规提示，TTS报警)
6.  **我们不做什么 (Out of Scope)**: (e.g., 不做复杂的后台管理)

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 范围界定 (Scoping)
**工程管理**: 引入 "Out of Scope" (不做之事) 的概念，教会学员做减法，这是项目管理中最重要的一课。

</div>

---

## **📥 课后任务 (Homework)**

<div class="columns">

<div>

### **👨‍🏫 老师 A & B**
1.  **完善 Prompt**: 你们的 AI 角色是什么？语气要怎么样？
2.  **准备测试数据**: 准备 3-5 张典型的测试图片。
3.  **招募/自研**: 
    -   方案一：课后寻找学生协助实现。
    -   方案二：挑战自我，利用 AI 编程助手独立完成（鼓励！）。

</div>

<div class="align-middle-center">

![width:450px](image/module7_lesson3.master/1766170291747.png)
</div>

</div>

<center>
<h1>🚀 下节课我们尝试开发MVP！</h1>
</center>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 结课 (Closing)
**行动呼吁 (Call to Action)**: 鼓励学员课后行动，将课堂的热情转化为实际的产出。

</div>