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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 课程设计意图
本节课（Module 8 Lesson 4）是整个培训的 Final Chapter。
前 7 个模块讲了"术"（Python, Prompt, Agents, RAG），这一模块讲"道"（Computational Thinking for Educators）。
本节课的核心目的是帮助您建立**持续学习系统**（社区）和**教学转化意识**（传承），确保课程结束不是学习的终点。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Jim Gray 的四范式理论
Jim Gray 是图灵奖得主，微软研究院科学家。他在 2007 年提出了科学研究的"第四范式"理论：
1. **第一范式 (Empirical)**: 基于观察和实验的经验科学。
2. **第二范式 (Theoretical)**: 基于数学模型的理论科学。
3. **第三范式 (Computational)**: 基于计算机仿真的模拟科学。
4. **第四范式 (Data-Intensive)**: 基于海量数据和机器学习的数据密集型科学。
第四范式的核心特征是：**规律不是人类推导出来的，而是从数据中"涌现"出来的**。
这对传统的科研流程产生了颠覆性影响。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AlphaFold 的影响
AlphaFold 是 DeepMind 开发的蛋白质结构预测模型。
- **2020**: AlphaFold 2 在 CASP14（蛋白质结构预测竞赛）中取得碾压性胜利。
- **2021**: 发布 AlphaFold DB，包含近乎所有已知蛋白质的结构预测。
- **2024**: AlphaFold 3 进一步预测蛋白质与 DNA、RNA、药物分子的相互作用。
这改变了结构生物学的游戏规则：
- **过去**: 实验室竞争"谁能先解出某个蛋白的结构"。
- **现在**: 结构预测成为"免费午餐"，竞争转向下游应用（药物设计、机制研究）。
对于非 CS 领域的研究者，这意味着：**不会用 AI 工具，可能就失去了入场券**。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI 辅助选题与文献的工具
- **OpenReviewer / paperreview.ai**: 审稿模拟器。上传你的摘要或论文草稿，AI 会模拟审稿人提出尖锐问题，帮你提前发现逻辑漏洞。
- **Consensus**: 只基于同行评审论文回答问题的搜索引擎。避免被网络噪音干扰。
- **Elicit**: 自动从海量论文中提取关键信息（方法、结论、样本数）并生成表格。
- **Connected Papers**: 可视化论文引用网络，帮你快速定位经典论文和最新进展。
这些工具的共同特点是：**降低信息过载，提升决策质量**。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Pipeline as Code 与 容器化
- **Pipeline as Code**: 将数据处理流程编写成脚本（而非手工操作），确保每次运行结果一致。代表工具：Snakemake, Nextflow, Make。
- **容器化 (Containerization)**: 将代码、依赖库、甚至操作系统打包成一个"镜像"(Image)，确保在任何机器上都能获得相同的运行环境。代表工具：Docker, Singularity。
这两者是解决"可复现性危机 (Reproducibility Crisis)"的核心手段。
据估计，发表论文中有 50%+ 的实验结果无法被独立复现。Pipeline as Code + 容器化 是解决这一问题的工程化方案。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Git-based Writing (基于 Git 的写作)
传统的论文写作方式（Word + 邮件来回传）存在很多问题：版本混乱、合并困难、历史丢失。
**Git-based Writing** 将软件工程的最佳实践引入学术写作：
1. **版本控制**: 每次修改都有记录，可追溯、可回滚。
2. **分支协作**: 多人同时写不同章节，互不干扰，最后合并。
3. **自动化发布**: 论文提交后自动编译成 PDF、自动发布到预印本网站。
代表工具：**Manubot**, **Overleaf + Git**, **Paperpile**。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### RAG (Retrieval-Augmented Generation)
RAG 是一种让大语言模型"接地气"的技术：
1. **传统 LLM**: 只能依赖训练数据，容易产生幻觉，无法获取最新信息。
2. **RAG**: 在生成答案前，先从外部知识库检索相关文档，然后基于检索结果生成答案。
优势：
- **实时性**: 知识库可以随时更新。
- **可控性**: 答案有据可查（可以追溯到具体文档）。
- **隐私性**: 知识库可以完全本地化，不上传云端。
这是目前企业和研究机构最常用的知识管理方案。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 开源精神与教育
**开源 (Open Source)** 的核心不是免费，而是**共建共享**。
在教育领域应用开源精神意味着：
1. **资源共享**: 把自己的课件、代码、工具公开，降低他人的入门门槛。
2. **协作改进**: 他人可以在你的基础上改进，然后再回馈给社区。
3. **声誉积累**: 通过贡献建立专业声誉（类似学术界的引用）。
GitHub 等平台让这种协作变得可追踪、可量化。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI 时代的教学转型
传统的编程教学强调"语法细节"和"从零开始"。
但在 AI 时代，更重要的能力是：
1. **提问能力 (Prompting)**: 把模糊需求转化为精确指令。
2. **审辨能力 (Critical Thinking)**: 识别 AI 输出中的错误和偏见。
3. **系统思维 (Systems Thinking)**: 理解输入-处理-输出的基本逻辑。
这些能力是"与 AI 协作"的基础，比死记语法更重要。
禁止学生用 AI 就像禁止学生用计算器——既不现实，也不明智。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 学习的阶段性
根据 Dreyfus 技能习得模型，技能学习分为五个阶段：
1. **新手 (Novice)**: 需要规则和指导。
2. **高级新手 (Advanced Beginner)**: 开始识别情境。
3. **胜任者 (Competent)**: 能制定计划并执行。
4. **精通者 (Proficient)**: 整体把握，直觉判断。
5. **专家 (Expert)**: 无需规则，与技能融为一体。
本课程的目标是帮大家从"新手"跨入"高级新手"——能识别基本模式，能与专业人员沟通，能在 AI 辅助下完成简单任务。
这已经是巨大的进步。

</div>

---

## **5. 课程资源库 (The Library)**

为了支持大家持续学习，我们整理了以下资源：

1.  **Awesome-AI-Education**: 精选的全球 AI 教育项目列表。
2.  **Prompt 模板库**: 针对教学和科研场景 (出题、批改、解释、实验、写作等) 的高阶 Prompt。
3.  **高效开发工具 (Tools)**: 常用的 AI 辅助工具 (ComfyUI, Dify, 以及常用的 Python 代码块)。

*(链接将发送至群公告)*

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 持续学习资源包
为了避免课程结束后的"拔剑四顾心茫然"，我们准备了三个层级的资源：
1.  **宏观视野**: Awesome-AI-Education (知道别人在做什么)。
2.  **微观实操**: Prompt 模板库 (拿来即用)。
3.  **开发工具**: ComfyUI/Dify 工具包 (进阶开发)。
这些资源将托管在 GitHub 上，保持长期维护更新。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要"共建"而不是"购买"？
市面上有很多现成的教育 AI 平台，为什么要自己做？
1. **定制化**: 外购平台无法深度适配本校的课程体系和教学风格。
2. **数据主权**: 学生数据和课程内容应该由学校自己掌控。
3. **能力建设**: 共建过程本身就是最好的学习——"Learning by Doing"。
4. **成本优势**: 长期来看，自建比订阅更经济。
这也是"Course as Software"理念的终极体现：把整个学校的课程体系当作一个软件系统来运营。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 两句名言的深意
- **叶芝 (Yeats)** 的话强调教育的本质不是"知识传递"，而是"激发潜能"。这与我们课程的设计理念一致：不是让老师们成为程序员，而是让大家**敢于尝试**、**敢于创造**。
- **纳德拉 (Nadella)** 的话指出了时代趋势：编程（计算思维）正在成为像读写一样的基本素养。这不意味着人人都要写代码，而是人人都要理解 **"软件是怎么影响世界的"**。
这两句话，一句指向教育的本质，一句指向时代的趋势，形成完美的收束。

</div>

---

## **最后的致谢**

感谢大家的开放心态，感谢大家的无数次 Debug。
未来的软件工程，不再属于少数精英工程师，而属于每一个拥有**创造力**和**解决问题意愿**的人。

**Keep Coding. Keep Creating.**
**去改变我们的世界吧！**

*(未完待续)*

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 课程总结
本节课（第32节）作为全课程的收官，完成了以下任务：
1. **理论升维**: 用"第四范式"定位软件在科研中的新角色。
2. **危机意识**: 用 AlphaFold 案例警示"不进则退"的现实。
3. **方法论落地**: 给出科研全流程的 AI 工具链。
4. **社区构建**: 宣布课程群升级为长期社区。
5. **行动号召**: 发起 NCU 智慧课程平台共建计划。
6. **情感收束**: 用名言和致谢完成仪式感的结尾。
课程结束了，但学习和创造才刚刚开始。

</div>