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
![bg blur:3px brightness:60%](../../../lectures/images/2025-10-26-17-28-32.png)

<style scoped>
h1{
  color: #F5F5F5; /* 设置文字颜色为白色 */
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8); /* 添加一个柔和的深色阴影 */
}
h2 {
  color: #E0E0E0; /* 设置文字颜色为白色 */
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8); /* 添加一个柔和的深色阴影 */
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
  border-left: 5px solid #4CAF50; /* 用一条强调色作为装饰 */
}
</style>

<div class="course-title">AI赋能软件开发</div>

# 模块一: AI编程新纪元 (思想破冰)
## 第3节课: 你的第一个AI应用：可视化随机点名器

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 从“体验者”到“创造者”
欢迎来到第三节课！在上一课中，我们已经成功搭建了与AI协作所需的环境。这节课，我们将利用这个环境，完成从“体验”到“创造”的关键一步。

我们将要创造的“随机点名器”，是一个看似简单却五脏俱全的完整软件应用。它包含了数据（学生名单）、交互（按钮）、逻辑（随机选取）和视觉呈现（滚动动画）。

通过这个项目，你将第一次完整地体验到作为一名“产品设计师”或“项目总监”，如何将一个想法变为现实的全过程。

</div>

---

## **本节课目标：创造你的第一个实用教学工具**

<div class="columns ratio-6-4">
<div>

在本节课中，我们将完成一次角色的重要升级：

从上一节课单纯体验AI的“即兴魔法”，**转变为第一次作为“产品总监”，指挥AI为你从零到一创造一个真正实用、可视化的教学应用**。

你将扮演“**产品总监**”的角色，你的任务是提出清晰的需求，AI则会作为你的“全栈开发团队”，负责实现一切。

</div>
<div>

![占位图：从观众到指挥家的角色转变](../../../lectures/images/2025-10-26-17-32-39.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 理解“产品总监”的角色
在软件开发行业中，“产品总监”或“产品经理”是一个至关重要的角色。他们负责：
- **发现问题**: 洞察用户的痛点和需求。
- **定义产品**: 设计产品的功能和形态，决定“做什么”和“不做什么”。
- **沟通协调**: 将产品的需求清晰地传达给开发团队。

在AI辅助编程的新范式下，你学习的核心正是“产品总监”的思维方式。AI负责技术实现，而你负责定义产品的灵魂。今天的练习，就是一次产品总监的“迷你实战演练”。

</div>

---

## **真实场景：让课堂点名变得有趣！**

<div class="columns ratio-6-4">
<div>

想象一下，传统的点名方式可能是……

- 拿着纸质名单，逐个念名字（耗时、单调）
- 随机叫学号（缺乏仪式感）

**我们的愿景**：创造一个充满动感和趣味的“随机点名器”，在屏幕上快速滚动学生的名字，最后随机定格。让每一次点名，都像一次激动人心的抽奖！

</div>
<div>

![占位图：从单调列表到趣味抽奖的对比](../../../lectures/images/2025-10-26-17-39-12.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么从“痛点”和“愿景”开始？
所有成功的软件产品，都源于对一个“痛点”的深刻理解，并为之提供一个有吸引力的“愿景”。
- **痛点 (Pain Point)**: 用户在特定场景下感到的不便、不满或低效。在这里，痛点是“传统点名方式单调、缺乏仪式感”。
- **愿景 (Vision)**: 对解决了痛点之后美好状态的描绘。在这里，愿景是“像激动人心的抽奖一样的点名体验”。

在启动任何一个项目前，先花时间清晰地定义“痛点”和“愿景”，是产品设计的第一步，也是最重要的一步。

</div>

---

## **解构魔法：先搭“骨架”（数据与交互）**

在告诉AI“做什么”之前，我们先像产品经理一样，把“大想法”拆解成“小零件”。

**我们的愿景：** 一个充满动感和趣味的随机点名器。

**首先，思考它的基本框架：**

1.  **“原料”是什么？** -> 点名器需要“认识”所有学生。
    -   **特性1 (数据)**：程序必须能**读取一份学生名单**。

2.  **“开关”在哪里？** -> 我们需要一种方式来命令它“开始”和“停止”。
    -   **特性2 (交互)**：需要一个 **“开始/停止”按钮**。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 编程思维：分解问题
将一个大而复杂的问题，分解成一系列小而简单的、可以独立解决的子问题，是计算机科学和软件工程中最核心的思维方式之一，我们称之为“**分解 (Decomposition)**”。

在这里，我们将“制作一个随机点名器”这个大问题，分解成了几个更小的特性。

我们首先关注的是所有应用最基础的两个部分：
- **数据 (Data)**: 程序需要处理的信息。没有数据，程序就无事可做。在这里就是学生名单。
- **交互 (Interaction)**: 用户与程序沟通的方式。没有交互，用户就无法控制程序。在这里就是按钮。

先定义好这两部分，就等于为我们的应用搭建好了“骨架”。

</div>

---

## **解构魔法：再填充“功能”与“外观”**

有了骨架，我们再为它实现核心功能与视觉外观。

3.  **它“做什么”？（核心功能）** -> 核心功能是从名单里随机挑出一个。
    -   **特性3 (逻辑)**：当停止时，程序能**最终确定一个随机名字**。

4.  **如何让它“有趣”？（视觉外观）** -> 要有动态效果，而不是瞬间完成。
    -   **特性4 (视觉)**：在挑选过程中，名字要像老虎机一样**快速滚动**。
      

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 软件的不同层次：逻辑与表现
在搭建好“数据”和“交互”的骨架后，我们需要填充另外两个关键部分：
- **逻辑 (Logic)**: 也常被称为“业务逻辑”，是程序的核心算法和规则，它定义了程序“做什么”。在这里，核心逻辑就是“从列表中随机选择一个元素”。
- **表现 (Presentation/View)**: 指程序呈现给用户的视觉界面和体验。在这里，就是“快速滚动的动画效果”。

在现代软件开发中，将**逻辑**和**表现**分离是一种非常重要的设计原则。逻辑关注的是“正确性”，而表现关注的是“用户体验”。我们今天的小应用，就同时包含了这两个方面。

</div>

---

## **从要素到需求**

<div class="columns ratio-6-4">
<div>

看，通过这四步，我们就把一个模糊的想法，变成了一份清晰的功能清单。

这份清单组合起来，就形成了一份完美的“产品需求文档”，也就是我们接下来在“动手环节”要交给AI的、清晰无误的指令！

</div>
<div>

![占位图：从零件到蓝图的合成过程](../../../lectures/images/2025-10-26-17-41-11.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是“产品需求文档”(PRD)？
“产品需求文档 (Product Requirements Document)”是软件工程中用于沟通产品需求的标准文档。它详细描述了产品的功能、特性、行为和设计，是开发团队、测试团队和项目管理团队共同的工作依据。

我们刚才通过四步分析得到的功能清单，就是一份最简化的PRD。它的核心价值在于：
- **澄清思想**: 强迫我们把模糊的想法变得具体。
- **统一共识**: 确保“产品总监”（你）和“开发团队”（AI）对要做的东西有完全一致的理解。
- **规避风险**: 避免因为需求不明确而导致开发出错误的产品，浪费时间和资源。

学会撰写清晰的需求，是与AI高效协作的第一步。

</div>

---

## **动手环节：三步创造你的应用**

现在，让我们进入VS Code，打开下方的集成终端，启动 `qwen` 助手，然后一步步创造奇迹。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 准备就绪
现在，我们将进入本节课的动手实践环节。请按照以下步骤准备好你的环境：
1. 打开VS Code。
2. 通过顶部菜单 `终端(Terminal)` -> `新建终端(New Terminal)` 打开集成终端。
3. 在终端中输入 `qwen` 并按回车，启动AI助手。
4. 等待 `>` 提示符出现，表示AI助手已准备好接收你的指令。

</div>

---

<style scoped>
.tip {
  background-color: #f0f8ff;
  border-left: 5px solid #1e90ff;
  padding: 15px;
  margin-top: 20px;
}
</style>

### **第一步：创建你的班级花名册**

根据我们刚才分析的 **特性1 (数据)**，我们的应用需要一份“原料”——学生名单。所以，我们的第一步，就是指挥AI为我们准备这份数据。在 `qwen` 提示符后，输入指令：

> `请帮我创建一个名为 students.txt 的文件, 里面包含30个随机的中文名字, 每个名字占一行。`

**魔法时刻**: AI会向你确认“是否允许创建文件”，输入 `y` 并回车。你会立刻在VS Code左侧的文件列表中看到 `students.txt` 文件！

<div class="tip">

**小贴士 (Pro Tip):**
之后在你自己的课堂上，你可以直接从教务系统或Excel中，复制学生名单，然后粘贴到这个 `students.txt` 文件里，点名器就可以马上为你所用了！
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 理解数据与代码的分离
这一步我们创建了一个独立的 `students.txt` 文件，而不是将学生名单直接写入程序代码中。这是一种非常重要的编程实践，称为“**数据与代码分离**”。

**这样做的好处是**：
- **灵活性**：当你的学生名单变化时（例如下学期换了一个班），你只需要修改 `students.txt` 这个数据文件，而完全不需要触碰和改动程序的核心代码（`点名器.html`）。
- **可维护性**：程序逻辑和具体数据各司其职，使得代码更清晰，更容易管理和维护。

在未来，你会看到这种分离思想的广泛应用，比如网站的文字内容和网站的程序代码是分开的，游戏的关卡设计和游戏引擎是分开的。

</div>

---
### **第二步：构建并启动点名器**

数据“原料”已经备好。现在，我们要将分析出的另外三个特性——**特性2 (交互)**、**特性3 (逻辑)** 和 **特性4 (视觉外观)**——打包成一个完整的需求，一次性地交给AI，让它为我们构建应用本身。请注意，我们在最后增加了一条【输出指令】：

> `请帮我创建一个名为 "点名器.html" 的文件。这个程序需要读取同目录下的 students.txt 文件来获取所有学生名单。网页上要有一个“开始/停止”按钮。第一次点击按钮，网页会像老虎机一样快速随机滚动学生名字；再次点击，滚动停止，并最终显示一个随机选中的名字。`
>
> `【输出指令】: 创建完成后，请立刻在默认浏览器中打开这个 "点名器.html" 文件。`

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 剖析“点名器”的Prompt
这个Prompt是我们这节课“产品设计”的最终成果。让我们再次剖析它的构成，这对于你未来独立与AI协作至关重要：
- **定义数据源**: `需要读取同目录下的 students.txt 文件` -> 明确了程序的输入。
- **定义交互界面**: `网页上要有一个“开始/停止”按钮` -> 明确了用户如何与程序互动。
- **定义核心逻辑**: `再次点击，滚动停止，并最终显示一个随机选中的名字` -> 明确了程序的核心功能。
- **定义视觉表现**: `像老虎机一样快速随机滚动学生名字` -> 明确了用户体验和视觉要求。
- **定义后续动作**: `【输出指令】: 创建完成后，请立刻...打开这个...文件` -> 告诉AI完成任务后还需要做什么。

一个高质量的Prompt，就像一份给专业开发者的清晰需求文档，是项目成功的关键。

</div>

---
### **第三步：见证奇迹**

<div class="columns ratio-6-4">
<div>

同样，在 `qwen` 提示符后粘贴以上指令并回车，然后在AI请求权限时输入 `y` 批准。

接下来，你什么都不用做！

AI创建完文件后，会**自动调用你的默认浏览器，为你打开 `点名器.html`**。你的第一个AI教学应用，就这样在你眼前诞生并运行了！

</div>
<div>

![占位图：浏览器弹出，展示最终应用](../../../lectures/images/2025-10-26-17-43-05.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI的“行动能力”
这个环节最神奇的地方在于，AI不仅为你生成了代码，还**自动打开了浏览器**来运行它。

这表明我们使用的`qwen-code`助手不仅是一个“代码生成器”，更是一个“**AI智能代理 (AI Agent)**”。它具备执行shell命令的能力，可以代表你在电脑上执行某些操作，例如：
- 创建、删除、移动文件
- 启动程序
- 运行代码

这种“行动能力”是新一代AI工具的核心特征。它使得AI不再仅仅是一个被动的知识库，而是一个可以主动帮助你完成任务的“数字员工”。当然，所有这些操作都会在你的明确批准下进行，确保安全。

</div>

---

### **所有程序的“秘密配方”**

祝贺你，刚刚你不仅创造了一个应用，更在不经意间，实践了所有程序开发共同的“秘密配方”！

让我们回顾一下“随机点名器”的工作过程：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-58-01.png)

*图：程序的“输入-处理-输出”模型*

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 计算机科学的基石：输入-处理-输出 (IPO) 模型
**输入-处理-输出 (Input-Process-Output, IPO)** 模型是描述计算机程序如何工作的最基本、最核心的模型。无论程序多么复杂，其本质都可以被简化为这三个阶段：
- **输入 (Input)**: 程序从外部世界获取数据和指令。来源可以是：键盘输入、鼠标点击、文件、数据库、网络传感器等。在我们的案例中，输入是 `students.txt` 文件和用户的按钮点击。
- **处理 (Process)**: 程序根据预设的逻辑和算法，对输入数据进行操作、计算、转换。在我们的案例中，处理过程是读取文件内容、在内存中形成一个列表、然后从中随机选择一项。
- **输出 (Output)**: 程序将处理结果返回给外部世界。形式可以是：显示在屏幕上、写入文件、打印、播放声音、控制硬件等。在我们的案例中，输出是显示在屏幕上的那个最终选定的名字。

理解IPO模型，是你开始用“计算机的方式”思考问题的起点。

</div>

---

### **编程的核心思维：定义起点和终点**

发现了吗？任何程序，本质上都是一个“转换器”，它接收一些**输入**，通过一系列**处理**，最终产生一些**输出**。

这就是编程最核心的思维方式：
在动手开始写第一行代码之前，专业的开发者会先清晰地定义两件事：
1.  **起点 (输入):** 我要处理的“原料”是什么？（是`students.txt`文件）
2.  **终点 (输出):** 我最终要得到什么“成品”？（是一个在屏幕上显示的名字）

只有当起点和终点都无比清晰时，我们才开始思考中间的“**处理**”过程（例如，需要一个按钮、需要一个滚动动画等）。

这个 **“先定义起点和终点，再规划中间路径”** 的思维习惯，就是“编程思维”的精髓。掌握了它，你就能应对任何复杂的编程挑战。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么“先定义起点和终点”如此重要？
“先定义输入和输出，再设计处理过程”的思维方式，在软件工程中被称为“**面向接口编程**”或“**黑盒设计**”的简化体现。它之所以高效，是因为：
1.  **锚定目标**: 它强迫你从一开始就明确最终目标，避免在开发过程中迷失方向。如果不知道要去哪里，任何一条路都可能是错的。
2.  **简化问题**: 当输入和输出被清晰定义后，“处理”过程就被限定在一个“黑盒子”里。你需要解决的问题范围被大大缩小了，你只需要思考“如何将给定的输入转化为期望的输出”，而无需思考其他无关问题。
3.  **便于测试**: 清晰的输入和输出定义，使得测试变得非常容易。你可以准备一组输入，然后检查程序的输出是否符合预期。

养成这个习惯，不仅能让你在编程时思路更清晰，在日常工作和生活中处理复杂问题时，同样大有裨益。

</div>

---

## **开启对话：如果初版不完美怎么办？**

<div class="columns ratio-6-4">
<div>

AI生成的初版应用，是一个优秀的“草稿”，但它可能并不完美。这恰恰是“人机协作”的价值所在！

如果效果不符合预期，我们不需要修改代码，而是继续**与AI对话**，提出你的优化意见：

- **优化动画**：“动画太快了，眼睛看不清，请让名字闪动的速度慢一点。”
- **优化样式**：“选中的名字不够突出。请让最终选中的学生名字，用红色、更大的字号显示。”
- **增加内容**：“请在页面的最上方，增加一个标题‘课堂随机点名器’。”

**记住：AI编程是一个持续对话、不断优化的过程。**

</div>
<div>

![占位图：人与AI的对话反馈闭环](../../../lectures/images/2025-10-26-17-51-49.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 迭代开发：从“草稿”到“成品”
很少有软件产品能够一次性开发完美。无论是传统开发还是AI开发，**迭代 (Iteration)** 都是一个必不可少的过程。

**迭代的循环过程如下**：
1.  **构建 (Build)**: 基于初始需求，快速构建一个可用的最小版本（我们称之为“草稿”或“原型”）。
2.  **评估 (Evaluate)**: 使用和测试这个版本，找到它的不足之处。
3.  **反馈 (Feedback)**: 将不足之处整理成新的、具体的修改需求。
4.  **重复**: 将新的需求再次交给“开发团队”（AI），构建下一个版本。

在AI辅助编程中，这个迭代循环的速度被极大地加快了。因为从“反馈”到“构建新版本”的过程，可能只需要几秒钟。学会与AI进行多轮对话来优化你的应用，是本课程需要掌握的一项核心技能。

</div>

---

## **下一步挑战：从“好用”到“好玩”**

我们的点名器已经诞生，但它还能变得更好！你可以课后尝试向AI提出这些“进阶需求”：

- **挑战1 (增加幸运感)**：
  > “当我停止滚动，选中一个学生时，可不可以给他加上一些庆祝的动画特效，比如撒花或者闪光？”

- **挑战2 (避免重复)**：
  > “在一节课中，我不想重复点到同一个人。你能帮我实现这个功能吗？”

这些挑战将引导你探索更复杂的编程逻辑，也是我们后续课程会深入学习的方向。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 挑战解析：引入“状态”的概念
这两个挑战比我们课上做的要复杂，它们引入了更高级的编程概念。

- **挑战1 (庆祝特效)**: 这个需求会涉及到更复杂的CSS动画或JavaScript动态DOM操作。AI需要生成代码，在特定事件（选中名字）发生后，动态地创建或显示一些新的视觉元素（如撒花效果）。

- **挑战2 (避免重复)**: 这个需求从根本上改变了程序的逻辑。为了实现“不重复”，程序需要“**记住**”已经被点到过的学生。在编程中，我们把这种需要被程序记住并随时间变化的信息称为“**状态 (State)**”。

  为了管理这个“状态”，AI可能需要这样做：
  1.  在内存中创建一个“已点名列表”。
  2.  每次点名前，从“总名单”中剔除“已点名列表”中的学生。
  3.  点名结束后，将新选中的学生加入到“已点名列表”中。

“状态管理”是所有复杂应用都需要面对的核心问题，我们将在后续课程中花更多时间来学习它。

</div>

---

## **你已掌握AI应用开发的核心！**

通过今天的练习，你已经体验了AI时代全新的软件开发模式：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-51-22.png)

*图：AI时代全新的软件开发模式*

</div>

你不再是代码的实现者，而是**创意的掌舵人**和**产品的决策者**。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI时代的软件开发新范式
今天你亲身体验的软件开发流程，代表了AI时代的一个根本性转变。
- **从“以代码为中心”到“以意图为中心”**: 传统编程的核心是代码，你需要用精确的语法来表达逻辑。现在，核心是“意图(Intent)”，你只需要用自然语言清晰地表达你的目标，AI会负责将其转换为代码。
- **从“长时间开发周期”到“实时迭代”**: 传统模式下，一个小的修改也可能需要数小时或数天。在AI辅助下，你可以在几分钟甚至几秒钟内，通过一次对话就完成一次迭代。
- **开发技能的“民主化”**: 过去，只有少数经过专业训练的程序员才能创造软件。现在，任何能够清晰思考和表达的人，都有可能成为软件的创造者。

你今天掌握的，不仅仅是制作一个点名器的方法，而是未来十年最重要的创造力模式之一。

</div>

---

## **下一步预告**

<div class="columns ratio-6-4">
<div>

这节课，我们创造了一个完整的应用。
在下一节课，也是模块一的最后一节课中，我们将：

- **分享**彼此创造的点名器和心得。
- **探讨**AI编程带来的全新视角。
- **总结**第一个模块的收获，并展望后续的精彩旅程。

</div>
<div>

![占位图：学员分享与社群讨论](../../../lectures/images/2025-10-26-18-06-21.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 学习金字塔：分享是最好的学习
下一节课我们将进入“分享”和“探讨”环节。这并不仅仅是一个“汇报”，它其实是学习过程中最重要的一环。

根据“学习金字塔”理论，**“教授他人”或“立即应用”** 是知识留存率最高的方式。当你准备向他人分享你的作品和心得时，你会不自觉地对知识进行更深层次的复盘、整理和内化。

**课后建议**:
1.  一定要亲手完成本节课的动手环节。
2.  尝试完成“下一步挑战”中的至少一个。
3.  思考一下在本节课的体验中，哪个环节让你印象最深？是AI的强大能力？还是你自己作为“产品总监”的体验？

准备好你的想法，期待在下节课听到你的分享！

</div>