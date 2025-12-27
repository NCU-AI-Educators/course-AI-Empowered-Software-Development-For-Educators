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
![bg blur:0px brightness:60%](image/module7_lesson1.master/1766150351495.png)

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

# 模块七: AI应用黑客松 (AI App Hackathon)
## 第25节: AI之眼——计算机视觉初体验 (Computer Vision)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 自学指南
本节课标志着我们从“文本处理”正式跨越到“多模态应用”开发。
“多模态”是指计算机不仅能读文字，还能看图片、听声音。
本模块我们将从最直观的“视觉”开始，利用微软的 Florence-2 模型，让 Python 脚本具备“看图说话”的能力。

</div>

---

## **模块七 设计理念: 为什么是黑客松?**

<div class="columns" style="font-size: 0.6em;">

<div>

### 💡 核心理念: 以赛促学
我们要的不是答卷，而是**作品**。

*   **打破“完美主义”**: 
    在这里，**"Done is better than perfect"**。我们接受不完美的代码，只求解决真实的问题 (MVP)。
*   **构建实践共同体**:
    编程不是孤独的修行。在接下来的8节课里，我们将**组队**，在互相 Debug 中建立战友般的情谊。

</div>
<div>

### 🚀 AI 带来的红利
过去，黑客松是程序员的专利。 
现在，**AI 抹平了技术鸿沟**。

*   **门槛降维**: 
    你不需要背诵算法。你只需要有**创意**和**Prompt能力**。
*   **角色升级**:
    你不再是技术的**旁观者**，你是指挥 AI 干活的 **“产品经理”**。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是 MVP (最小可行性产品)?
MVP (Minimum Viable Product) 是黑客松和创业界的核心概念。
它意味着不要试图一开始就做一个完美的软件（比如微信），而是先做一个能跑通核心功能的简陋版本（比如只能发文字的聊天工具）。
在黑客松中，我们的目标就是 MVP：代码可以乱，界面可以丑，但必须能解决核心问题。

</div>

---

## **什么是黑客松 (Hackathon)?**
### **一场思想与技术的马拉松**

<div class="columns">
<div>

### 🧩 词源解密
*   **Hack (钻研)**: 不是“攻击电脑”，而是指用巧妙、非常规的方法解决难题。
*   **Marathon (马拉松)**: 指在集中的短时间内（如24-48小时），高强度地冲刺一个目标。

</div>
<div>

### 💡 核心定义
**“一群人，在有限的时间内，为了解决一个具体问题，把想法变成原型的活动。”**

它不是单纯的编程比赛，更像是一个 **“48小时创业实验”**。
在这里，想法 (Idea) 和 执行 (Execution) 同等重要。

</div>
</div>

<div class="tip" style="font-size: 0.6em;">

**为什么适合老师？**
因为**教学就是一场持续的 Hack**。
我们每天都在用有限的资源去解决（Hack）无穷尽的学生问题（Marathon）。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Hack 的本意
在 MIT 的文化里，Hack 代表的是一种**高智商的恶作剧**或者**巧妙的工程解决方案**。
它强调的是**巧妙性 (Cleverness)** 和 **创造力 (Creativity)**，而不是破坏。
对于老师来说，针对一个特定的教学痛点（如批改作业慢），快速用工具搭建一个解决方案，这就是一次成功的 Hack。

</div>

---

## **案例 1: MIT Hacking Medicine (Grand Hack)**
### **核心逻辑: 痛点比代码更值钱**
<div class="columns" style="font-size:0.86em">
<div>

**“全球最大的医疗吐槽大会”**
*   **现场直击**: 每年春季，波士顿。台上站的不是黑客，而是医生、护士，甚至是推着轮椅的病人。
*   **游戏规则**: 
    1.  **痛点路演 (Pitch)**: 医生抱怨“医院里这点事太烦了”。
    2.  **认领任务**: 工程师和设计师举手：“这事我能用技术解决”。
*   **成功故事**: PillPack (被亚马逊$10亿收购) 就诞生于此——它的创始人不是去写复杂的算法，而是解决了“老年人记不住吃药”这个简单的痛点。

</div>

<div>

<div class="align-middle-center">

![width:400px](image/module7_lesson1.master/1766147559672.png)
</div>

*(MIT Grand Hack 现场，跨学科团队正在便利贴墙前讨论)*

</div>

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 痛点驱动创新
很多技术人员容易陷入“拿着锤子找钉子”的误区（先有技术，硬找场景）。
而 MIT 黑客松的成功秘诀在于：**先找痛点**。
对于非 CS 专业的老师，你们最大的优势就是**你们就在痛点之中**。
你们知道学生哪里学不懂，知道教务哪里最繁琐。这就是比写代码更宝贵的“行业洞察”。

</div>

---

## **MIT 的跨学科黑客松宇宙**

<div class="columns">
<div>

### **不仅仅是医学，万物皆可 Hack**
### **🎨 MIT Hacking Arts (艺术黑客松)**
*   **核心**: 探索**科技与创意产业**的边界。
*   **参与者**: 艺术家、设计师、音乐人与工程师混搭。
*   **挑战**: 如何用 AI 辅助作曲？如何用 VR 重塑舞台表演？
*   **启示**: 艺术教育 + 技术 = 新的感官体验。

</div>
<div>

### **⚖️ MIT Policy Hackathon (政策黑客松)**
*   **核心**: 用**数据科学**解决**社会问题**。
*   **参与者**: 政治学、法学、社会学与数据专家组队。
*   **挑战**: 城市交通公平性分析、公共卫生资源分配。
*   **启示**: 这里的“产品”是**政策建议书**，而不仅是代码。

</div>
</div>

<div class="tip" style="font-size: 0.6em;">

**给老师们的启示**
无论你是教**美术、音乐**，还是**思政、管理**，黑客松都是你们 **“打破边界”** 的工具。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 跨学科融合 (Interdisciplinary)
未来的创新往往发生在学科的交叉点上。
AI 是一个通用的“胶水”。
- 文科 + AI = 数字人文 (Digital Humanities)
- 艺术 + AI = 生成式艺术 (Generative Art)
- 社科 + AI = 计算社会科学 (Computational Social Science)
本课程的目标，就是帮大家找到这个结合点。

</div>

---

## **案例 2: Stanford Green AI Hackathon**
### **核心逻辑: 领域专家 (Domain Experts) 的胜利**

<div class="columns" style="font-size:0.95em">
<div>

**“懂环境比懂 AI 更重要”**
*   **跨界现场**: 
    这是一场**能源政策系**学生与 **CS系** 学生的联谊。
    *   **专业学生**: 提供“森林火灾蔓延模型”的专业知识。
    *   **程序员**: 用 AI 去训练卫星图像模型。
*   **启示**: 
    在 AI 时代，**掌握领域知识 (Domain Knowledge)** 的人才是拿着地图的人，程序员只是负责开车的司机。

</div>
<div class="align-center">

![width:420px](image/module7_lesson1.master/1766148309946.png)
![width:420px](image/module7_lesson1.master/1766148566918.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是领域专家 (Domain Expert)?
在软件开发中，我们把精通某个具体行业业务的人称为 **SME (Subject Matter Expert)**。
AI 只是一个强大的工具箱（锤子、锯子）。
但具体要盖什么房子（解决什么问题）、怎么盖才符合规范（行业标准），这完全取决于 SME。
在 AI 时代，不懂业务的程序员很容易被替代，但**懂业务并会用 AI 的专家**将不可替代。

</div>

---

## **案例 3: Harvard GenAI Hackathon**

<div class="columns" style="font-size:0.95em">
<div>

### **核心逻辑: 英语是新的编程语言**
**“No Coding Experience Required”**
*   **口号**: 这是一个**不允许**写复杂底层代码的比赛。
*   **玩法**: 
    *   参赛者使用 **AI Sandbox** (类似我们课上的平台)。
    *   比拼谁的 **Prompt** 写得好，谁的**创意**（Use Case）更落地。
*   **你的角色**: 
    你不需要成为架构师，你只需要成为最好的 **“AI 驯化师”**。

</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap:10px 10px; align-content: center; line-height: 0; height: 100%;">
  <img src="image/module7_lesson1.master/1766148881923.png" style="width: 100%; object-fit: cover; display: block;" />
  <img src="image/module7_lesson1.master/1766148921985.png" style="width: 100%; object-fit: cover; display: block;" />
  <img src="image/module7_lesson1.master/1766149005102.png" style="width: 100%; object-fit: cover; display: block;" />
  <img src="image/module7_lesson1.master/1766148973707.png" style="width: 100%; object-fit: cover; display: block;" />
  <img src="image/module7_lesson1.master/1766149220723.png" style="width: 100%; object-fit: cover; display: block;" />
  <img src="image/module7_lesson1.master/1766149324122.png" style="width: 100%; object-fit: cover; display: block;" />
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么说自然语言是新编程语言？
传统编程需要把逻辑翻译成 `if/else/for`。
现在的大模型（LLM）能直接听懂人类语言。
你写下一段清晰的 Prompt（提示词），本质上就是在对 AI 的大脑进行编程。
所以，**逻辑思维能力**和**语言表达能力**，比背诵 Python 语法更重要。

</div>

---

## **模块七 学习路线图: 从“看懂”到“创造”**

<div class="columns">
<div>

我们将用4节课的时间，完成AI应用黑客松的**启动**阶段：

*   **Step 1: AI之眼 (Vision)** <span style="color: #666; font-size: 0.9em;">*(Lesson 25)*</span>
    让计算机学会“看图”，这是感知的起点。
*   **Step 2: 云端大脑 (Brain)** <span style="color: #666; font-size: 0.9em;">*(Lesson 26)*</span>
    接入 DeepSeek/GPT，获得逻辑推理能力。
*   **Step 3: 创意组合 (Idea)** <span style="color: #666; font-size: 0.9em;">*(Lesson 27)*</span>
    **黑客松组队**！混合智能（感知+大脑）构思产品。
*   **Step 4: 工程落地 (Build)** <span style="color: #666; font-size: 0.9em;">*(Lesson 28)*</span>
    调试、优化、准备 Demo。

</div>
<div>

![](image/module7_lesson1.master/1766150706733.png)
<div class="tip" style="font-size: 0.6em;">

**通关目标**
本模块结束时，每组将产出一个 **MVP (最小可行性产品)** 的原型代码。
我们将在 **Module 8** 的 Demo Day 上分享作品！

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 模块结构解析
这个模块模拟了一个真实 AI 产品的开发流程：
1.  **能力储备**: 先掌握核心技术组件（视觉 + 语言）。
2.  **产品构思**: 组队碰撞火花，确定要解决什么问题。
3.  **原型开发**: 动手把想法变成可运行的代码。
这套流程不仅适用于本课程，也适用于我们未来的任何科研或教学项目开发。

</div>

---

## **本节课学习目标**

<div class="columns" style="font-size:0.95em">
<div>

1.  **原理**: 理解 AI 视觉模型(VLM)是如何“看图说话”的。
2.  **体验 Florence-2**: 运行 Microsoft 的 **Florence-2-base** 模型，生成详细的图像描述。
3.  **视觉提示词 (Visual Prompting)**: 学习如何通过 Task Token (如 `<MORE_DETAILED_CAPTION>`) 精确控制 AI 的输出。

### **课前准备**
请确认项目根目录下的 `models/florence-2-base` 文件夹已准备就绪。

</div>
<div>

![1766150827419](image/module7_lesson1.master/1766150827419.png)

<div class="tip" style="font-size: 0.6em;">

**什么是 VLM (Vision-Language Model)?**
它是一个打破了视觉和语言界限的超级大脑。
它不仅“看见”了像素，还理解了像素背后的**语义**，并能像人类一样用语言表达出来。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是多模态 (Multimodal)?
人类是多模态的：我们同时使用视觉、听觉、语言来理解世界。
早期的 AI 往往是单模态的（只能处理文本或只能处理图像）。
**VLM (Vision-Language Model)** 是这两年的技术突破，它架起了一座桥梁，让 AI 能够同时理解图片和文字，从而实现“看图说话”甚至“看图回答问题”。

</div>

---

## **1. 思考: 计算机怎么“看”世界？**

<div class="columns">
<div>

当你看到右边这张图，你会说：
**"这是一只双色猫。"**

但在计算机眼里，它其实是一个巨大的数字矩阵：
`[[255, 128, 0], [254, 130, 5], ...]`

**AI 的工作，就是找到这堆数字背后的规律，然后告诉我们：这是猫。**

</div>
<div>

![width:550px](https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500&q=80)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 语义鸿沟 (Semantic Gap)
这页展示了一个核心难题：**像素与含义之间的巨大鸿沟**。
底层特征（颜色、纹理、边缘）很容易提取，但高层语义（“猫”、“可爱”、“正在观察”）很难直接从像素中推导出来。
深度学习模型（如 CNN 和 Transformer）的作用，就是层层抽象，填平这个鸿沟。

</div>

---

## **2. 核心工具: Hugging Face Transformers**

<div class="columns"  style="font-size:0.83em">
<div>

这节课我们要认识两个新朋友：`AutoModel` 和 `AutoProcessor`。
它们是 Hugging Face 的两员大将：
*   **Processor (翻译官)**: 负责把图片和提示词“翻译”成电脑能懂的数字。
*   **Model (大脑)**: 负责用这些数字进行思考和生成。

我们通过简明的三步走方式来完成任务：

1.  **准备 (Processor)**: 把图片和提示词转化成电脑能懂的数字。
2.  **生成 (Generate)**: 运行模型，生成一串代表答案的数字代码 (Token IDs)。
3.  **翻译 (Decode)**: 查字典，把这些数字代码变回人类的文字。

</div>
<div>

![1766150959962](image/module7_lesson1.master/1766150959962.png)
</div>

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要分两步？(Processor + Model)
这体现了软件设计的**解耦**思想。
- **Processor**: 专门处理杂活（调整图片大小、归一化颜色、分词）。它让模型可以专注于核心计算。
- **Model**: 这是一个通用的数学大脑，它不关心输入是图片还是文字，它只关心数学运算。
Hugging Face 库把这些复杂操作封装成了两个简单的对象，让我们只需调用几行代码即可。

</div>

---

## **3. 你的第一个视觉脚本:看图说话**

<div class="columns ratio-4-6" style="font-size:0.9em">
<div>

**任务目标**: 
编写 `lesson25_vision_demo.py`，识别当前目录下的一张图片 `test_image.jpg`。

### **🧠 Prompt 策略 (Strategy)**

*   **Role**: Python 开发者
*   **Model**: `microsoft/Florence-2-base` (VLM)
*   **Task**: `image-to-text` (详细描述)
*   **Path**: 本地路径 (`./models/florence-2-base`)

</div>
<div>

**Prompt 指令**:
> "请帮我写一个 Python 脚本。
> 1. **场景**: 我已经把 Florence-2 模型下载到了本地文件夹 `./models/florence-2-base`。
> 2. **任务**: 请加载这个本地模型，并对 `test_image.jpg` 进行**详细描述** (使用 `<MORE_DETAILED_CAPTION>`)。
> 3. **注意**: 加载时请允许运行远程代码 (`trust_remote_code=True`)。"
<div class="insight" style="font-size: 0.6em;">

**关键提示**:
Florence-2 是一个**生成式模型**，它不是在做选择题（分类），而是在做**问答题**（看图说话）。

</div>
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是 Task Token?
Florence-2 是一个多功能模型。它既能做检测，也能做分割，还能做描述。
怎么告诉它你想做什么？就是通过 **Task Token**。
- `<CAPTION>`: 简单描述。
- `<MORE_DETAILED_CAPTION>`: 详细描述。
- `<OD>`: 物体检测 (Object Detection)。
这就像给万能机器人下达具体的指令代码。

</div>

---

<style scoped>
pre code {
  font-size: 40px !important; /* 尝试设置一个更大的值 */
  line-height: 1.3 !important; /* 压缩行间距，防止被挤出屏幕 */
}
</style>

## **4. 代码解析 (Code Analysis)**

<div class="columns">
<div>

```python
from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image

# 1. 加载大脑 (VLM)
model_id = "./models/florence-2-base"
model = AutoModelForCausalLM.from_pretrained(model_id, 
            trust_remote_code=True).eval()
processor = AutoProcessor.from_pretrained(model_id, 
            trust_remote_code=True)

# 2. 睁开眼睛 (Image)
image = Image.open("test_image.jpg")

# 3. 思考 (Generate)
prompt = "<MORE_DETAILED_CAPTION>"
inputs = processor(text=prompt, images=image, return_tensors="pt")

generated_ids = model.generate(
    input_ids=inputs["input_ids"],
    pixel_values=inputs["pixel_values"],
    max_new_tokens=1024,
    num_beams=3
)

# 4. 说话 (Decode)
text = processor.batch_decode(generated_ids, 
    skip_special_tokens=False)[0]
print(text)
```

</div>
<div>

### **关键点解读**

1.  **`eval()`**: 
    告诉模型“现在是考试时间”，不要学习（训练），全心全意做题（推理）。
2.  **`trust_remote_code=True`**:
    允许加载微软编写的自定义模型代码（因为它是新架构，不是标准库的一部分）。
3.  **`<MORE_DETAILED_CAPTION>`**:
    这是**咒语** (Task Token)。你告诉模型“我要更详细的”，它就会详细描述画面细节。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要 trust_remote_code?
通常为了安全，Hugging Face 只运行官方审核过的代码。
但 Florence-2 是新出的模型，它的架构非常新颖，官方库还没来得及集成。
所以我们需要显式地设置 `trust_remote_code=True`，意思是：“我知道我在做什么，我信任微软提供的这段模型代码。”
**注意**: 除非是知名机构的模型，否则不要轻易开启此选项，以防恶意代码。

</div>

---

## **5. 进阶挑战: 把刚才的脚本变成手机能用的 App**

<div class="columns"  style="font-size:0.95em">
<div>

### **编写提示词 (Prompting)**
### **🧠 提示词策略 (Thinking)**
1.  **明确角色**: 你是 Python 全栈工程师。
2.  **融合知识**: 显式告知 AI 要结合 **Module 6 (FastAPI)** 和 **Module 7 (VLM)**。
3.  **约束条件**:
    *   接收 `UploadFile` (手机传图片)。
    *   使用 `processor` 处理图片和文本 (`<MORE_DETAILED_CAPTION>`)。
    *   **关键**: 只要返回生成的文本描述即可，不要复杂的 HTML。

</div>
<div style="font-size:0.92em">

### **📝 提示词示范 (Action)**

> "**我需要把刚才的 Florence-2 脚本封装成一个 API。**
>
> 1. 使用 `FastAPI` 创建一个 POST 接口 `/upload`。
> 2. 接收手机上传的图片 (`UploadFile`)。
> 3. **核心逻辑**: 读取文件字节流，用 `PIL.Image` 打开，然后喂给 `model` 和 `processor`。
> 4. 不需要写前端页面，我直接用 Swagger UI 测试。
> 5. 打印出启动命令 (host=0.0.0.0)。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要封装成 API?
脚本 (Script) 只能在开发者的电脑上跑。
服务 (Service/API) 可以在任何设备上跑。
通过 FastAPI，我们将 Florence-2 变成了一个**公共服务**。你的手机、平板、甚至其他软件都可以通过网络调用它，而不需要知道它内部是怎么工作的。

</div>

---

<style scoped>
pre code {
  font-size: 40px !important; /* 尝试设置一个更大的值 */
  line-height: 1.1 !important; /* 压缩行间距，防止被挤出屏幕 */
}
</style>

## **6. 手机扫码体验**

<div class="columns">

<div>

### **连接 Module 6 + Module 7**
```python
# lesson25_mobile_demo.py
from fastapi import FastAPI, UploadFile, File
# ... (省略 import)

# 1. 预加载 Florence-2 (全局变量)
# ... (加载代码略) ...

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # 2. 读取 + 转换
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    
    # 3. 运行 VLM
    inputs = processor(text="<MORE_DETAILED_CAPTION>", 
        images=image, return_tensors="pt")
    # ... (generate 代码) ...
    
    return {"label": caption}
```

</div>

<div>

### **体验步骤**

1.  **运行服务**: 确保电脑和手机在同一 WiFi。
2.  **生成二维码**: 使用我们的工具脚本 (或此时手动输入 http://电脑IP:8000/docs)。
3.  **手机扫码**: 打开 Swagger UI，点击 `/upload` -> `Try it out`。
4.  **拍照上传**: 从图库选择文件上传，或者直接调用手机摄像头拍照。

</div>
</div>

<div class="tip" style="font-size:0.6em">

**原理揭秘**
*   **FastAPI**: 负责接收 HTTP 请求（就像 Module 6 讲的点餐服务）。
*   **io.BytesIO**: **内存里的“虚拟文件”**。它把下载到的数据在内存中直接转换成文件格式，这样不需要存到硬盘上，程序就能直接读取图片。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要用 io.BytesIO?
通常 `Image.open()` 是打开硬盘上的文件（如 "C:\photo.jpg"）。
但在这里，图片是通过网络传过来的**一串二进制数据流 (Bytes)**，并没有保存到硬盘上。
`io.BytesIO` 的作用就是**把这串数据流包装一下，假装成一个文件**，这样 `Image.open()` 就能处理它了。
这在 Web 开发中非常常用，因为存硬盘太慢了，直接在内存里处理更快。

</div>

---

## **7. 迭代优化：给 API 穿上外衣**

光有 API 还不够，Swagger UI 给开发者看还行，给用户看太简陋了。
让我们用 AI **一句话生成** 一个漂亮的前端界面。

### **Prompt Strategy (Frontend)**
<div class="columns" style="font-size:0.7em">
<div>

描述需求：
> "我有一个 FastAPI 后端，地址是 `/upload` (POST)，接收 `file` 字段。
> 请帮我写一个单文件的 `index.html`。
> **要求**:
> 1.  **暗黑模式 (Dark Mode)**，科技感 UI。
> 2.  中间有一个大大的**相机图标**，手机点击可以调起摄像头。
> 3.  使用 `fetch` 异步上传图片，并在下方显示返回的 `label` 文字。
> 4.  增加 Loading 动画。"

</div>
<div>

<div class="tip" style="font-size: 0.8em;">

**为什么这样做？**
*   **前后端分离**: 我们专注于写好 Python 逻辑 (后端)。
*   **AI 赋能**: 繁琐的 HTML/CSS/JS 让 AI 去写，它有超越人类的前端开发能力。
*   **快速原型**: 5分钟就能把一个 API 变成一个 App。

</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 前端的“单文件”策略
在专业开发中，前端的 HTML（结构）、CSS（样式）和 JavaScript（脚本）通常是分开的。
但为了黑客松的极致速度，我们可以采用**单文件 HTML** 策略：将这三者全部写在一个 `index.html` 里。
这样，前端就只有一个文件，它通过网络“点单”，后端的 Python 负责“做菜”。这种方式最适合快速验证你的 AI 创意。

</div>

---

## **8. 代码揭秘：如何托管前端？**

只需要增加 **3行代码**，FastAPI 就能变成 Web 服务器。

```python
from fastapi.responses import HTMLResponse
import pathlib

# 新增路由: 访问根目录 "/" 时
@app.get("/", response_class=HTMLResponse)
def home():
    # 就像读txt文件一样读取 html
    html_content = pathlib.Path("index.html").read_text(encoding="utf-8")
    return html_content
```

<div class="insight" style="font-size: 0.6em;">

**原理解析**:
当用户访问 `http://ip:8000/` 时，FastAPI 读取本地的 `index.html` 文件内容，并告诉浏览器："这是一段 HTML 代码 (`response_class=HTMLResponse`)，请渲染它，而不是把它当成文本显示。"

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 静态资源服务
平时我们打开一个网页，浏览器其实是下载了一个 HTML 文件。
这里我们用 FastAPI 充当了 Web 服务器的角色。
`pathlib.Path("index.html").read_text()` 就像是你用记事本打开文件并全选复制。
`HTMLResponse` 就像是把复制的内容粘贴给浏览器，并告诉它：“这是网页，请渲染。”

</div>

---

## **9. 最终实验: 你的第一个 AI App**

请运行 **Web应用化** 的脚本，拿起手机扫描屏幕上的二维码（或手动输入网址），然后把镜头对准身边的万物！

**思考题 (Think-Pair-Share)**:
1.  **细节**: 它不仅仅说 "Laptop" (笔记本)，它有没有说颜色、品牌、或者是屏幕上的内容？
2.  **关系**: 试着拍两个人，它能说出 "Two people talking" (两个人在交谈) 吗？
3.  **幻觉**: 拍一张复杂的抽象画，听听它是怎么一本正经胡说八道的。

<div class="key-point" style="font-size: 0.6em;">

**实验观察**:
Florence-2 是一个强力的 VLM。与计算机视觉技术早期的分类模型不同，它试图**理解**整个场景。
你会发现它不仅能识别**物体 (Objects)**，还能识别**属性 (Attributes)** 和 **关系 (Relationships)**。
这就是现代 AI 的魅力——它开始有了“语义理解”能力。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 关于 AI 幻觉 (Hallucination)
你会发现 AI 有时会看走眼，或者对模糊的图像胡编乱造。
这是生成式 AI 的通病。它不是在“查找真理”，而是在“预测概率最大的下一个词”。
在黑客松中，我们需要思考如何用产品设计来规避这个问题（比如人工复核，或者限制应用场景）。

</div>

---

## **课程小结**
### **关键点**
<div class="columns" style="font-size:0.8em">
<div>

1.  **VLM (Vision-Language Model)**: AI 的能力从简单的物体分类 (Tagging) 进化到了场景理解与描述 (Captioning)。
2.  **Florence-2**: 微软的小型神级模型，证明了小模型也能有大智慧。
3.  **本地部署**: 即使是这么强的生成模型，在你的笔记本上也能流畅运行。

### **下节预告**
我们的 VLM 虽然能看懂图，但它生成的是**英文**描述，这对我们的中文教学场景不够友好。
下节课，我们将学习**Pipeline 思维 (流水线)**：把 VLM 的输出，喂给另一个擅长翻译的 AI。
搭建一条 **“视觉 -> 翻译”** 的自动化流水线！

</div>
<div>

![1766151267797](image/module7_lesson1.master/1766151267797.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 课后思考
这节课的代码虽然只有几十行，但它其实已经具备了“视障辅助眼镜”的核心功能。
想一想，如果把这段代码再改进一下，能用语音说出文字描述，那么最终程序装进树莓派，挂在胸前，连上耳机，它能不能帮助盲人朋友“听见”这个世界？
这就是黑客松的意义——**用技术温暖生活**。

</div>