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
![bg blur:3px brightness:60%](image/module8_lesson4.master/1766775787919.png)

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

# 模块八: 总结与展望
## 第32节: 展望未来与社区 —— 星火燎原 (Future & Community)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 开场致辞 (Opening)
**策略**: **情感连接**。作为最后一课，不需要冗长的寒暄，直接定下"传承"和"社区"的基调，唤起学员的使命感。

</div>

---

## **1. 理论引领：第四范式与软件工程 (Theory)**

<div class="columns" style="font-size:0.75em">
<div>

### **科学范式的演进 (The Evolution)**
**Jim Gray (Turing Award Winner)** 将科学发展总结为四个阶段：

1.  **第一范式 (实验)**: **"钻木取火"**。记录自然现象 (Empirical)。
2.  **第二范式 (理论)**: **"牛顿定律"**。用数学模型描述规律 (Theoretical)。
3.  **第三范式 (计算)**: **"气象模拟"**。用计算机仿真复杂系统 (Computational)。
4.  **第四范式 (数据)**: **AI for Science**。从海量数据中**自动涌现**未知规律 (Data-Intensive)。

</div>
<div>

### **软件角色的跃迁 (The Shift)**
*   **In P3 (Simulation)**: 软件是**计算器**。我们写代码去*验证*已知的公式 (如纳维-斯托克斯方程)。
*   **In P4 (AI for Science)**: 软件是**探索者**。我们写代码(AI)去*发现*未知的规律 (如 GNoME 发现 220 万种新晶体)。
*   **结论**: 软件不再只是工具，它变成了**科学发现的本体**。因此，我们需要软件工程来驾驭系统的复杂性。

</div>
</div>

<div class="insight" style="font-size: 0.6em;">
<strong>💡 核心洞见</strong><br>
软件工程不仅是“写代码”，它是管理<strong>复杂性 (Complexity)</strong> 和 <strong>变化 (Change)</strong> 的学科。<br>
将 SE 引入科研，是为了驾驭日益庞杂的数据和算法。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 宏观视角 (Big Picture)
**策略**: **升维思考**。从科学哲学的高度来定位"软件工程"的意义，让学员意识到这不仅是技术课，更是认知升级课。

</div>

---

## **2. 警钟：AlphaFold 与结构生物学的变局 (The Wake Up Call)**

<div class="columns" style="font-size:0.9em">
<div>

### **Google DeepMind vs. "Yan Ning"**
*   **The Shock**: AlphaFold 2 在短短数月内，解出了人类 98.5% 的蛋白质结构。
*   **The Reality**: 颜宁团队并没有“失业”，但 **“解结构” (Structure Determination)** 这件事本身，从一个需要耗时数年的 *科研难题*，变成了一个*基础设施*。
*   **The Shift**: 现在的竞争，变成了 **"谁能更好地使用 AI 预测模型去做下游的药物设计"**。

</div>
<div>

### **Software: The Entrance Ticket (入场券)**
*   **Research (生死时速)**: 科研如果不拥抱 AI 软件化，是**降维打击**。你还在手工钓鱼，别人已经开着捕鱼船来了。**没有自动发现能力，就没有新时代的入场券。**
*   **Teaching (温水煮青蛙)**: 教学如果不改变，影响是滞后的（学生4年后才毕业）。但科研的滞后，意味着**Funding 和 Discovery 的直接归零**。

</div>
</div>

<div class="insight" style="font-size: 0.6em;">
<strong>🚨 结论</strong><br>
对于高校教师而言，<strong>AI 赋能科研的迫切性 > AI 赋能教学</strong>。

因为科研是 **赢家通吃(Winner-takes-all)** 的战场。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 危机意识 (Wake Up Call)
**策略**: **制造紧迫感**。用一个具体的、颠覆性的案例（AlphaFold）来打破学员可能的"舒适区"心态。

</div>

---

## **1. 科研新范式 (1/3)：大脑 —— 选题与文献**
<div class="columns">
<div>

### **Stage 1: 选题 (Ideation)**
*   **运作方式**: **"AI 蓝军演练"**。在正式开题前，用 AI 模拟最刁钻的审稿人，攻击你的 Hypothesis。
*   **核心工具**:
    *   **OpenReviewer / paperreview.ai**: 审稿大模型，专门找逻辑漏洞。
    *   **Consensus**: 科学界的 Google，只基于真实论文回答问题。

</div>
<div>

### **Stage 2: 文献 (Literature)**
*   **运作方式**: **"知识图谱挖掘"**。不要只读 Text，要读 Graph。让 Agent 顺藤摸瓜，找出“鼻祖”和“新星”。
*   **核心工具**:
    *   **Elicit**: 从 100 篇论文中自动提取表格（方法、结论、样本数）。
    *   **Connected Papers**: 可视化引用关系网，一眼看穿领域脉络。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 工具清单 (Toolbox)
**策略**: **快速扫描**。用"大脑-双手-面孔"的比喻把科研流程拟人化，让学员快速建立记忆锚点。

</div>

---

## **1. 科研新范式 (2/3)：双手 —— 实验与分析**
<div class="columns">
<div>

### **Stage 3: 实验 (Experiment)**
*   **运作方式**: **"Pipeline as Code"**。只要是重复两次以上的动作（洗数据、跑模型），必须写成各类脚本，通过 Workflow 引擎串联。
*   **核心工具**:
    *   **Snakemake** (Python): 生物/AI 界最流行的流水线工具，断点续跑，自动并行。
    *   **AutoGLM**: 只要一句话，自动尝试 100 种模型组合。

</div>
<div>

### **Stage 4: 分析 (Analysis)**
*   **运作方式**: **"环境容器化"**。不要只传代码，要传“电脑”。解决 "It works on my machine" 的千古难题。
*   **核心工具**:
    *   **Docker**: 将操作系统、依赖库、数据打包成一个镜像。
    *   **Code Ocean**: 云端可复现计算平台，审稿人点一下就能复现结果。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 可复现性 (Reproducibility)
**策略**: **痛点共鸣**。"It works on my machine"是所有做过科研的人都经历过的噩梦，用这个切入点引发共鸣。

</div>

---

## **1. 科研新范式 (3/3)：面孔 —— 写作与发表**

<div class="columns">
<div>

### **Stage 5: 写作 (Writing)**
*   **运作方式**: **"Single Source of Truth"**。论文不是 Word 文档，而是代码仓库。图表、数据、引用全部自动化同步。
    *   *Note: 这与第29节课提到的“教学内容自动装配”逻辑完全一致！*
*   **核心工具**:
    *   **VS Code + Markdown + LaTex**: 一切皆文本，AI 辅助润色语法。
    *   **Manubot**: **Git-based Writing**。像写代码一样写论文，PR 审稿，CI/CD 自动发布网页版论文。

</div>
<div>

<div class="insight" style="margin-top:1em;font-size: 0.6em;">

<strong>总结：PI (Principal Investigator) 的进化</strong>

未来的科研竞争力，不只是比拼智力，更是比拼<strong>“自动化系统的构建能力”</strong>。

当你还在手工画图时，你的竞争对手已经用 Python 脚本批量生成了实验对比图，并自动插入了论文。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 知识迁移 (Transfer)
**策略**: **呼应前文**。显式关联第29节的"自动装配"概念，让学员看到教学和科研之间的共性，强化学习效果。

</div>

---

## **1. 科研与教学的交汇点：本地知识库 (The Foundation)**

<div class="columns" style="font-size:0.8em">
<div class="styled-div" style="font-size: 0.8em;">

### **为何必须建本地库？(Why Local RAG?)**
*   **隐私安全**: 你的未发表论文、学生数据、独家课件，不应直接喂给公有云 AI。
*   **融会贯通**: **Teaching** 需要最新的 **Research** 案例；**Research** 需要 **Teaching** 时的灵感。两者在知识库中是连通的。

### **核心方案: RAG (检索增强生成)**
*   **原理**: 不微调模型，而是"外挂大脑"。
*   **工具推荐**:
    *   **AnythingLLM**: 零门槛，一键扫描本地文件夹，离线运行。
    *   **Obsidian + Copilot**: 在你的双链笔记里直接与 AI 对话。

</div>
<div style="margin-top:1em">

> "Whether you are a researcher or a teacher, your digital assets (notes, papers, slides) are your second brain."

<div class="insight">
<strong>🧠 第二大脑的终极形态</strong><br>
打造一个<strong>"懂这一行所有黑话"</strong>的私人助理。<br>
当你备课或写论文时，它能瞬间检索你过去 5 年读过的 1000 篇论文及上过的 200 堂课。<br>
这才是<strong>知识复利</strong>的开始。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 方法论总结 (Methodology Summary)
**策略**: **收束**。将前面分散的工具和理念，收束到"本地知识库"这个核心载体上，形成完整闭环。

</div>

---

## **2. 从“课程群”到“学习社区” (Community)**

我们的微信群不会解散。它将升级为我们的 **"AI 教育者开发者社区"**。

<div class="columns">
<div>

### **我们在这里做什么？**
*   **技术互助**: 遇到 Python 报错，群里有人帮你看。
*   **Prompt 分享**: 发现新的好用的 Prompt，第一时间共享。
*   **AI 创意分享**: 及时分享可 AI 赋能开发的产品或工具的创意。

</div>
<div>

### **开源共建 (Open Source)**
*   我们将建立一个 GitHub Organization: `AI-for-Educators`。
*   **你的作品就是开源项目**: 鼓励大家把黑客松的作品上传，供后来的老师参考。
*   **贡献者精神**: 帮助别人，是提升自己最快的方式。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 社区构建 (Community Building)
**策略**: **延续感**。强调"课程结束不是终点"，建立持续学习的心理预期。

</div>

---

## **3. 薪火相传：如何教你的学生？(Teaching)**

你们是第一批火种。现在，轮到你们去点燃学生了。

<div class="columns">
<div>

### **不要教什么 (Don'ts)**
*   ❌ 不要一开始就讲复杂的语法和算法细节。
*   ❌ 不要禁止使用 AI。

</div>
<div>

### **要教什么 (Dos)**
*   ✅ **教提问**: 如何把模糊的想法变成精确的 Prompt。
*   ✅ **教鉴别**: AI 给了答案，如何去验证它对不对。
*   ✅ **教系统思维**: 输入-处理-输出 (Input-Process-Output)。

</div>
</div>

<div class="insight" style="font-size: 0.6em;">

**建议**: 在你的专业课中，布置一次 **"AI+学科"** 的作业。
例如：历史课让学生用 AI 生成年表网页；文学课让学生训练风格化写作 Bot。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 行动号召 (Call to Action)
**策略**: **赋能转化**。将学员从"学习者"身份转化为"传播者"，强调他们的使命感。

</div>

---

## **4. 贵在坚持：关于“学不会”的真相 (The Truth)**

<div class="columns">
<div>

### **一个真相**
*   **感到吃力是正常的**: 软件工程是一门**实践性极强的学科**，没人能光靠听课学会游泳。
*   **“似懂非懂”也是收获**: 你可能暂时写不出代码，但你已经听懂了程序员的“黑话”，这本身就是沟通能力的质变。

</div>
<div>

### **两个目标**
1.  **Be Confident (信心)**: 建立“我能行”的各种微小胜利。打破对代码的恐惧，是本课程的第一使命。
2.  **Be Complete (全景)**: 我们展示了**全栈开发**的完整地图。哪怕现在只能看懂 30%，但你知道“路”在哪里，不再是盲人摸象。

</div>
</div>

<div class="insight" style="font-size: 0.6em;">

**未来已来**: 这些“硬核知识”是通往未来的门票。虽然现在很难，但请相信：
依靠 **AI 协作** + **大量实战**，你终将从“踉踉跄跄”走向“得心应手”。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 心理支持 (Emotional Support)
**策略**: **正视困难**。承认学习的难度，避免"鸡汤式"的盲目乐观，同时给予真实可行的信心。

</div>

---

## **5. 课程资源库 (The Library)**

为了支持大家持续学习，我们整理了以下资源：

1.  **Awesome-AI-Education**: 精选的全球 AI 教育项目列表。
2.  **Prompt 模板库**: 针对教学和科研场景 (出题、批改、解释、实验、写作等) 的高阶 Prompt。
3.  **高效开发工具 (Tools)**: 常用的 AI 辅助工具 (ComfyUI, Dify, 以及常用的 Python 代码块)。

*(链接将发送至群公告)*

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 资源指引 (Resource Pointer)
**策略**: **授人以渔**。给出持续学习的资源入口，而不是让学员依赖课程。

</div>

---

## **🚀 倡议：NCU 智慧课程平台共建计划**

<div class="columns">
<div>

### **Why: 为什么要做？**
*   **知行合一**: 只有在真实的炮火中（项目开发），才能真正掌握“AI 放大一切”的能力。
*   **数据孤岛**: 打破各门课程的壁垒，建立 NCU 专属的智能学习平台。

### **How: 我们怎么做？**
*   **组建团队**: 寻找 5-10 位**种子教师** + **学生开发者**。
*   **技术栈**: Gemini/Qwen + Python + ComfyUI + Dify (全员 AI 辅助开发)。
*   **MVP**: 一个月内上线 `NCU-Course-GPT` (专属助教平台)。

</div>
<div>

### **What: 期望的收获**
*   🧰 **打造一套智慧课程工具箱**
*   🌏 **建设一批国际化的智慧课程**
*   📚 **开发一系列新型数字化教材**

<div class="key-point" style="font-size: 0.6em;">
<strong>🌟 英雄帖</strong><br>
如果你厌倦了“单打独斗”，如果你想亲手打造一款属于南昌大学的顶尖软件。<br>
<strong>Join Us!</strong><br>
让我们用 AI 把南昌大学的智慧课程推向世界。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 招募号召 (Recruitment)
**策略**: **从学到做**。将课程学习转化为实际项目参与，提供一个"立刻行动"的出口。

</div>

---

## **6. 寄语 (Final Message)**

<div class="tip">

> **"Education is not the filling of a pail, but the lighting of a fire."**
> —— William Butler Yeats （著名诗人）
> **“教育不是灌满一桶水，而是点燃一团火。”**

<br>

> **"In the age of AI, coding is the new literacy."**
> —— Satya Nadella （微软现任CEO）
> **“在 AI 时代，编程是新时代的读写能力。”**

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 情感升华 (Emotional Lift)
**策略**: **金句收尾**。用两句权威人士的名言来锚定课程的核心价值，让学员带着使命感离开。

</div>

---

## **最后的致谢**

感谢大家的开放心态，感谢大家的无数次 Debug。
未来的软件工程，不再属于少数精英工程师，而属于每一个拥有**创造力**和**解决问题意愿**的人。

**Keep Coding. Keep Creating.**
**去改变我们的世界吧！**

*(未完待续)*

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 30秒
### 环节: 收尾 (Closing)
**策略**: **简洁有力**。用口号式的结尾激发行动力，不做冗长总结。

</div>