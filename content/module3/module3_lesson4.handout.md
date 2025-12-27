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
  padding: 15px 15px 0.1px; 
}
.insight {
  background-color: #eefcff; 
  border-left: 5px solid #17a2b8; 
  padding: 15px 15px 0.1px; 
}
.key-point {
  background-color: #fffbe6; 
  border-left: 5px solid #ffc107; 
  padding: 15px 15px 0.1px; 
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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-21-00-14-43.png)

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

# 模块三: 代码复用与人机协作
## 第12节课: 模块收官项目：批量文件整理助手

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 自动化脚本 (Automation Script)
我们今天要编写的“批量文件整理助手”，在行业中通常被称为“**自动化脚本**”。

自动化脚本是一种旨在自动执行一系列重复性、常规性任务的程序。它的核心价值在于**将人力从枯燥、易错的重复劳动中解放出来，极大地提升工作效率**。

常见的自动化脚本应用场景包括：
- **文件管理**: 如我们今天要做的，批量重命名、移动、复制、删除文件。
- **数据处理**: 自动从Excel中读取数据，进行计算，并生成报告。
- **系统管理**: 定时备份数据库、检查服务器状态。
- **Web自动化**: 自动登录网站、填写表单、抓取信息。

学会编写自动化脚本，是程序员提升个人生产力的“必备魔法”。

</div>

---

## **回顾：你已是“AI开发主管”**

<div class="columns ratio-6-4">
<div style="font-size: 0.9em;">

在模块三的前三节课，我们作为“AI开发主管”，已经掌握了提升代码品质的核心方法，完成了从“能运行”到“高品质”的思维转变。

我们掌握了作为一名“**AI开发主管**”的全部核心技能：

- **封装与授权 (函数)**
  - 你能将混乱的逻辑打包成清晰的“功能积木”。
- **品控与纠错 (调试)**
  - 你能从容地将“事故报告”交给AI，并指导它修复问题。
- **评审与决策 (审查)**
  - 你能挑战AI，在多个方案中权衡利弊，做出最佳决策。

今天，我们将迎来对这些高级技能的**最终试炼**。

</div>
<div class="align-middle-center">

![一个充满自信的开发主管，站在白板前，指挥着一个AI机器人团队 width:400px](../../../lectures/images/2025-11-21-00-16-12.png)
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 技术主管 (Tech Lead) 的角色
本模块中我们扮演的“AI开发主管”，在软件行业中通常对应“**技术主管 (Tech Lead)**”或“**首席开发 (Lead Developer)**”的角色。

技术主管不仅是优秀的程序员，更是团队的技术核心和领导者。其职责超越了单纯的编码，主要包括：

1.  **技术决策 (Technical Decision-Making)**: 负责关键的技术选型、架构设计和代码质量标准制定。（对应我们的“评审与决策”）
2.  **任务分解与分配 (Task Breakdown & Delegation)**: 将复杂的业务需求分解为可执行的开发任务。（对应我们的“封装与授权”）
3.  **代码审查与质量保证 (Code Review & Quality Assurance)**: 确保团队产出的代码符合规范、健壮且易于维护。（对应我们的“品控与纠错”）
4.  **指导与赋能 (Mentorship & Empowerment)**: 帮助团队成员成长，提升整个团队的技术水平。

通过本模块的学习，你实践了作为一名技术主管所需的核心能力，完成了从“执行者”到“领导者”的关键转变。

</div>

---

## **项目使命：解决一个真实世界的“烦恼”**

<div class="columns ratio-6-4">
<div style="font-size: 0.8em;">

我们今天的项目，不再是构建虚拟世界，而是要解决一个老师们在日常工作中频繁遇到的真实烦恼：

**教学文件命名不统一**

想象一下你一个学期的教学资料文件夹，里面的文件名五花八门：
- `第1课.pptx`
- `学生名单-最新.xlsx`
- `课程总结.md`

当这些文件被传来传去，或从压缩包解压后，我们很难一眼看出它们属于哪个学期、哪门课程。

**我们的目标**：指挥AI编写一个“**批量文件重命名助手**”，一键为指定文件夹里的所有文件，都加上统一、清晰的前缀，例如 `2025秋-软件工程-`。

</div>
<div class="align-middle-center">

![一个文件列表，通过一个脚本，所有文件名前都加上了统一的前缀，例如“2025秋-软件工程-” width:400px](../../../lectures/images/2025-11-21-00-17-40.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 需求分析 (Requirements Analysis)
在任何软件项目开始之前，首要任务都是进行“**需求分析**”。需求分析的核心是回答以下问题：
1.  **要解决什么问题？(Problem)**：文件命名混乱，难以管理。
2.  **谁是用户？(User)**：教师、行政人员等需要管理大量文件的用户。
3.  **核心功能是什么？(Features)**：为指定文件夹下的所有文件批量添加前缀。
4.  **成功的标准是什么？(Acceptance Criteria)**：运行脚本后，目标文件夹内的所有文件（非文件夹）都被正确添加了前缀。

一个清晰的需求分析，是项目成功的基石。它为后续的设计、开发和测试提供了明确的方向和目标。我们现在做的，就是一次迷你的需求分析实践。

</div>

---

## **第一步(1/2)：蓝图设计——明确输入与输出(IPO)**

在思考“如何做”之前，我们必须先彻底搞清楚“做什么”。一个专业的开发者，会花费大量时间来明确定义程序的**输入(Input)**和**输出(Output)**。

这就像做菜，你必须先弄清要用哪些食材（输入），以及最终想做出什么菜（输出），然后才能设计菜谱（处理流程）。

<div class="align-center">

![height:300px](../../../lectures/images/2025-11-21-12-23-55.png)

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### IPO模型
**IPO (Input-Process-Output)** 模型是计算思维中最基本、最核心的思维框架之一。它描述了一个程序最基础的结构：
- **输入 (Input)**: 程序从外部世界获取数据。数据来源可以是用户键盘输入、文件、数据库、网络请求等。
- **处理 (Process)**: 程序对输入的数据进行一系列的计算、转换、操作。这是程序的核心逻辑所在。
- **输出 (Output)**: 程序将处理后的结果返回给外部世界。输出形式可以是显示在屏幕上、写入文件、存入数据库等。

在开始编写任何复杂程序前，先用IPO模型画出草图，清晰地定义程序的边界和核心功能，是一种能极大提升开发效率和成功率的专业习惯。

</div>

---

## **第一步(2/2)：蓝图设计——设计处理流程**

当我们清晰地定义了输入和输出后，就可以开始设计连接两者的“桥梁”——**处理流程 (Process)**。

<div class="columns">
<div style="font-size: 0.95em;">

**处理流程 (文字描述):**
1.  获取目标文件夹的路径和指定的前缀。
2.  遍历该文件夹中的**每一项**。
3.  构建该项的完整路径，并判断**如果**它是一个**文件**（而不是子文件夹）：
4.  构建出它的**新文件名** (前缀 + 原文件名)。
5.  构建出完整的新文件路径。
6.  将该文件从“旧的完整路径”**重命名**为“新的完整路径”。

</div>
<div class="align-center">

![width:165px](../../../lectures/images/2025-11-21-12-34-20.png)
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 伪代码与流程图
在编写实际代码之前，使用“**伪代码**”或“**流程图**”来规划算法，是两种非常常见的专业实践。
- **伪代码 (Pseudocode)**: 一种使用自然语言（夹杂少量代码格式）来描述算法逻辑的方法。它忽略了具体编程语言的语法细节，只关注算法的核心步骤和逻辑。我们左侧的“处理流程”就是一份伪代码。
- **流程图 (Flowchart)**: 一种使用标准化的图形符号来表示算法或流程的图表。它能非常直观地展示程序中的顺序、选择（分支）和重复（循环）结构。
  - **椭圆形/圆角矩形**: 代表流程的开始或结束。
  - **矩形**: 代表一个处理步骤。
  - **菱形**: 代表一个判断或决策点。

这两种工具都能帮助我们在动手编码前，理清思路，发现潜在的逻辑问题，并为后续与AI（或同事）的沟通提供一份清晰的设计文档。

</div>

---

## **第二步：向AI咨询，发现“新工具”**
<div style="font-size: 0.9em;">

我们的算法蓝图需要一些我们从未接触过的能力：如何“遍历文件夹”？如何“重命名文件”？

这时，我们不需要去Google搜索，而是直接向我们的“**全能技术顾问**”——AI——提问。

> **探索性Prompt:**
>
> “你好，我想用Python写一个批量重命名文件的脚本。请问我需要用到哪些工具（比如标准库或模块），来实现以下操作：
> 1.  列出某个文件夹里的所有文件名？
> 2.  将一个文件从旧名字重命名为新名字？”

**AI的回答**：它会告诉你，Python的内置`os`模块，就是处理这些操作系统相关任务的“瑞士军刀”。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### “学习如何学习”的元技能
在信息爆炸的时代，掌握“**学习如何学习 (Learning how to learn)**”的元技能，比单纯记忆知识点更重要。在编程领域，这意味着：
- **承认未知**: 承认自己不可能知道所有的库、函数和API。
- **定义问题**: 能够将一个大的目标，分解为需要特定工具才能解决的、更小的问题（例如，“批量重命名”被分解为“遍历文件夹”和“执行重命名”）。
- **有效提问**: 知道如何向搜索引擎或AI提出精准的问题，以寻找解决这些小问题的工具。

本页的“探索性Prompt”，就是一次“定义问题”和“有效提问”的实践。掌握了这种能力，你就能在AI的辅助下，不断地扩展自己的能力边界，进入任何新的编程领域。

</div>

---

## **新工具介绍：`os`模块**
<div style="font-size: 0.84em;">

`os`模块提供了我们完成任务所需的所有“工具”：

- **`os.listdir(path)`**
  - **作用**：列出指定`path`文件夹内的所有文件和文件夹名，返回一个**列表**。
- **`os.path.join(path, filename)`**
  - **作用**：智能地将文件夹路径和文件名拼接成一个完整的绝对路径。（比手动拼接更健壮！）
- **`os.path.isfile(full_path)`**
  - **作用**：判断一个给定的完整路径是否是一个**文件**，返回`True`或`False`。
- **`os.rename(source_path, destination_path)`**
  - **作用**：重命名或**移动**一个文件/文件夹。我们将用它来完成重命名。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 标准库 (Standard Library)
`os`模块是Python“**标准库**”的一部分。

“标准库”是指随着Python解释器一同安装的、一组经过验证的、高质量的模块和函数集合。这意味着，只要你安装了Python，就可以直接`import os`来使用它，而不需要像第三方库那样额外通过`pip install`等命令来安装。

Python拥有一个“**自带电池 (batteries included)**”的强大标准库，涵盖了从文件操作、网络通信、数据压缩到日期时间处理等各种常见任务。熟悉标准库，能让你在不引入任何外部依赖的情况下，完成大量实用工作。

`os.path`是`os`模块中的一个子模块，专门用于处理文件路径相关的操作。使用`os.path.join()`而不是手动拼接字符串，是一个非常重要的、体现专业性的编程习惯。

</div>

---

## **第三步(1/3): 从“愿景”到“指令”——提出初始想法**
<div class="columns" style="font-size: 0.9em;">
<div>

我们已经有了清晰的蓝图和工具，但要一次性写出完美的“终极指令”，对新手而言依然是巨大的挑战。

一个更轻松、更符合AI协作精神的工作流是：**与AI一起“迭代”出最终的指令**。

这个过程的第一步，不是追求完美，而是先向AI抛出一个简单的、**“愿景驱动”的初始指令**，告诉它我们大致想做什么。

这就像对一个团队成员说：“嘿，我们大概要做个批量重命名的东西”，而不是直接甩给他一份详细的规格书。

</div>
<div>

> **“愿景驱动”的初始Prompt:**
>
> “你好，我想用Python写一个脚本。
>
> **目标**：批量重命名某个文件夹里的所有文件，为它们统一添加一个前缀字符串。
>
> 你觉得这个任务可行吗？如果让你来做，大致的思路是怎样的？”

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 愿景驱动 vs. 设计驱动
在与AI协作编写代码时，我们可以大致采用两种Prompt模式：
- **愿景驱动 (Vision-Driven)**: 你只向AI描述你最终想要实现的“**愿景**”或“**目标**”，而不关心具体的实现步骤和技术细节。这种模式非常适合项目的初期探索和头脑风暴阶段。它的优点是简单快速，缺点是AI的输出不确定性高。
- **设计驱动 (Design-Driven)**: 你向AI提供一份详尽的“**设计规格**”，精确地告诉AI每一步应该做什么、使用什么工具。这种模式适合在思路清晰后，需要精确控制代码产出的阶段。它的优点是输出结果高度可控、可预测，缺点是需要前期投入更多思考。

一个专业的AI协作者，会根据项目阶段，灵活地在这两种模式之间切换。我们现在学习的，就是如何从“愿景驱动”平滑过渡到“设计驱动”。

</div>

---

## **第三步(2/3): 引导AI思考“边界情况”**
<div class="columns" style="font-size: 0.9em;">
<div>

在收到初始指令后，AI可能会给你一个简单的实现思路（比如直接使用`os.listdir`和`os.rename`）。

此时，我们的职责不是马上写代码，而是扮演“**压力测试工程师**”的角色，引导AI思考方案中潜在的“**边界情况**”和“**风险**”。

这是从普通使用者到专业开发者的关键一步。

</div>
<div style="font-size: 0.95em;">

> **“挑战边界”的追问Prompt:**
>
> “你的思路听起来不错。但在实际操作中，这个方案有没有什么需要特别注意的‘**边界情况**’或**可能出错**的地方？
>
> 比如：
> 1.  如果文件夹里除了文件，还有**子文件夹**怎么办？
> 2.  如果遇到像`.DS_Store`这样的**隐藏文件**怎么办？
> 3.  如果脚本不小心被**重复执行**了两次，文件名会不会被加上两次前缀？
>
> 请帮我分析这些风险，并提出你的优化建议。”

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 边界情况 (Edge Cases)
“**边界情况**”是软件测试中的一个核心概念，指的是那些发生在输入值范围的“边缘”或极端情况下的场景。

例如，对于我们的重命名脚本：
- **类型边界**: 文件夹内容物不是普通文件（而是子文件夹、快捷方式等）。
- **命名边界**: 文件名本身就很特殊（如隐藏文件`.DS_Store`，没有后缀名的文件，名字超长的文件）。
- **状态边界**: 系统处于某种特殊状态（文件夹为空，文件正在被其他程序占用，脚本被重复执行）。

新手程序员往往只关注“**正常路径 (Happy Path)**”（即一切顺利的情况），而专业的开发者会花费大量精力去思考和处理各种“边界情况”，因为绝大多数的Bug都隐藏在这些角落里。学会主动思考边界情况，是专业素养的体现。

</div>

---

## **第三步(3/3): 请求AI整合生成“终极指令”**
<div class="columns" style="font-size: 0.9em;">
<div>

经过几轮讨论，我们和AI已经对需求达成了共识，并考虑了各种细节。

现在，我们不必亲自费力去总结，可以把这个任务也交给AI！

我们可以“**升维思考**”，要求AI扮演“**需求分析师**”，将我们刚才的所有讨论，整理成一份高质量的、给“AI程序员”看的“终极指令”。

这是一种强大的“**元能力**”：**利用AI来优化我们与AI自身的沟通**。

</div>
<div style="font-size: 0.4em;">

> **“生成指令”的元Prompt:**
>
> “非常好！我们现在已经把各种情况都考虑清楚了。
>
> 现在，请你**扮演一名专业的‘需求分析师’**，将我们从开始到现在的所有讨论，包括：
> 1.  最初的**核心目标** (加前缀)
> 2.  后来补充的各种**边界情况处理** (跳过子文件夹、跳过隐藏文件、避免重复添加前缀)
> 3.  以及你建议使用的**技术工具** (`os`模块)
>
> 全部整理成一份**清晰、详尽、高质量、步骤化**的开发指令(Prompt)。
>
> 这份指令的目标读者是另一位‘AI程序员’，所以它必须足够精确，没有任何歧义。”

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 元认知与元Prompting (Meta-cognition & Meta-Prompting)
“**元认知 (Meta-cognition)**”指的是“关于认知的认知”，通俗讲就是“对自己思考过程的思考”。它包括对自身学习、记忆、解决问题等认知活动的监控和调节。

我们将这个概念迁移到与AI的互动中，就产生了“**元Prompting**”：**编写旨在生成或优化其他Prompt的Prompt**。

当你向AI发出“请帮我把这个问题描述得更清晰”或“请把我们的对话总结成一份开发需求文档”这类指令时，你就是在进行“元Prompting”。

这标志着你与AI的协作进入了一个新的层次：
- **基础协作**: 你思考，AI执行。
- **元协作**: 你与AI一起思考“如何更好地思考”，你引导AI帮助你优化你对AI下达的指令。

掌握元协作，是AI时代保持人类认知优势的关键。

</div>

---

## **第四步：审查并执行AI生成的“终极指令”**
<div class="styled-div" style="font-size: 0.55em;">

在我们发出了“生成指令”的元Prompt后，AI“需求分析师”就会为我们生成一份融合了我们所有讨论成果的“终极指令”。

这份指令现在成为了我们指导“AI程序员”工作的最终蓝图。我们的任务，是**最后审查一遍**，然后将其发送给AI（甚至可以是同一个AI），让它生成最终脚本。

> **AI生成的终极指令 (审查稿):**
>
> 请为我编写一个Python脚本，名为`batch_renamer.py`，用于给文件批量添加前缀。
>
> 1.  导入`os`模块。
> 2.  定义一个名为 `batch_rename_files` 的函数，它接收 `folder_path` 和 `prefix` 两个字符串作为参数。
> 3.  在函数内部，使用 `os.listdir()` 遍历指定 `folder_path` 下的所有项目。
> 4.  在循环中，构建每个项目的完整路径，并用 `os.path.isfile()` 判断它是否是一个文件。
> 5.  为增加代码健壮性，请只重命名文件，不要对子文件夹进行操作。同时，跳过以`.`开头的隐藏文件。
> 6.  在重命名之前，增加一个判断：如果文件名**已经**以指定`prefix`开头，就跳过这个文件，并打印一条提示信息，避免重复添加前缀。
> 7.  构建新的文件名（`prefix + original_filename`），并基于此构建完整的新文件路径。
> 8.  使用 `os.rename()` 将文件从旧路径重命名为新路径，并打印出重命名的过程，例如：“已重命名: a.txt -> 2025-final-a.txt”。
> 9.  在脚本的**最末尾**，定义两个变量：`TARGET_FOLDER = "./test_folder"` 和 `PREFIX = "2025秋-软件工程-"`。
> 10. 最后，调用 `batch_rename_files(TARGET_FOLDER, PREFIX)` 函数来执行脚本。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 指令审查 (Prompt Review)
在我们我们将一份最终的、复杂的指令交给AI执行之前，进行最后一次“**指令审查**”，是一个能极大提升协作效率和准确性的好习惯。

这与开发流程中的“**代码审查 (Code Review)**”异曲同工。它的目的是：
1.  **确认完整性**: 检查指令是否遗漏了我们在讨论中提到的任何关键需求或边界情况。
2.  **检查清晰度**: 确保指令的每一步描述都清晰、无歧义，不会让AI产生误解。
3.  **最终确认**: 作为项目的“决策者”，这是你为“即将执行的复杂操作”做的最后一次“Go/No-Go”决策。

经过审查的、高质量的指令，是获得高质量代码输出的最重要保障。

</div>

---

## **动手环节：批量重命名你的“课程文件”**
<div style="font-size: 0.9em;">

在开始动手之前，我们需要建立一个重要的专业认知：一个正规的软件项目，其开发、测试和生产环境是严格分离的。我们编写的任何工具，都必须先在一个安全的“沙盒”环境中进行充分测试，确保它完全符合预期后，才能应用到真实的、重要的数据上。

测试通过后，在我们将工具应用于真实的、海量的课程文件之前，通常还会有一个“**试运行**”阶段。在这个阶段，我们会选择一小部分不那么重要但真实的文件进行操作，并**提前做好数据备份**。这是为了防范那些在沙盒测试中未能发现的、意料之外的BUG，是保障数据安全的最后一道防线。

<div>

![](../../../lectures/images/2025-11-21-13-10-06.png)
</div>

我们今天的实践，主要就是模拟流程图中的“**沙盒测试**”这个过程。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 开发、测试与生产环境
在软件工程中，为了保证软件质量和系统稳定，通常会设置多个独立的环境：
- **开发环境 (Development)**: 开发者本地的开发机器。代码在这里被编写和初步调试。
- **测试环境 (Testing / Staging / QA)**: 一个专门用于测试的环境，其配置应尽可能地与生产环境相似。我们创建的`test_folder`就是一个最简化的测试环境。
- **生产环境 (Production)**: 软件最终部署和运行，为真实用户提供服务的环境。这是最关键的环境，任何操作都必须慎之又慎。

“**不要在生产环境做测试**”是所有程序员都必须遵守的铁律。我们今天的实践，就是在模拟这一专业流程，先在安全的“测试环境”中验证我们的工具。

</div>

---

### **第一步：创建“沙盒环境”与“测试数据”**
<div style="font-size: 0.9em;">

在你的项目根目录下，创建一个名为`test_folder`的文件夹，这就是我们的“沙盒”。然后，在AI助手中，使用以下指令，在沙盒中创建一些用于测试的空白文件：

> 请帮我在`./test_folder/`目录下，创建以下几个空白文件：`课程大纲.docx`, `第1课讲义.pptx`, `学生名单.xlsx`。

### **第二步：执行“重命名脚本”**
1.  向AI发送我们上一页的“**终极指令**”，让它生成`batch_renamer.py`脚本。
2.  **审查代码**：花一分钟时间，对照你的指令，检查AI生成的代码逻辑是否完全符合你的设计。
3.  在VS Code的终端中，运行这个脚本：`python batch_renamer.py`

### **第三步：验证“测试结果”**
- 查看你的`test_folder`“沙盒”。
- 所有测试文件的名字是否都成功地被加上了你设定的前缀？（例如：`2025秋-软件工程-课程大纲.docx`）

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 脚本的配置与执行
我们通过在脚本末尾定义`TARGET_FOLDER`和`PREFIX`变量的方式，来“配置”这个脚本的行为。这是一种简单直接的配置方法。

在更复杂的应用中，配置信息通常会通过更灵活的方式提供，例如：
- **命令行参数 (Command-line Arguments)**: 允许用户在运行脚本时，通过命令行直接传入参数，例如 `python renamer.py --folder /path/to/folder --prefix "MyPrefix-"`。这需要使用`argparse`等模块。
- **配置文件 (Configuration Files)**: 将配置信息写入一个单独的文件（如`.ini`, `.json`, `.yaml`），脚本启动时读取这个文件。这使得修改配置无需修改代码。
- **环境变量 (Environment Variables)**: 从操作系统环境变量中读取配置。

我们目前的硬编码方式虽然简单，但理解这些更高级的配置方式，是编写更通用、更专业工具的基础。

</div>

---

## **模块三总结：你已是合格的“AI开发主管”**

<div class="columns ratio-6-4">
<div style="font-size: 0.8em;">

**祝贺你，完成了模块三的终极试炼！**

让我们回顾一下在本模块，你作为“AI开发主管”所掌握的三大核心领导力：

- **封装与授权 (函数)**
  - 你学会了将复杂任务分解，并“授权”给一个个独立的函数去执行。
- **品控与纠错 (调试)**
  - 你学会了管理AI的“失误”，通过分析报告和清晰指令，引导其修复问题。
- **评审与决策 (审查)**
  - 你学会了评估AI的不同方案，并基于权衡做出最终的架构决策。

你已经不再是AI的简单使用者，而是能**驾驭AI**，主导项目从设计、实现、到质量把控全流程的**领导者**。

</div>
<div class="align-middle-center">

![一个自信的领导者，身后是代表函数、调试、审查的图标，他/她正在指挥一个AI团队 width:400px](../../../lectures/images/2025-11-21-01-03-59.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 从编码到工程的思维转变
模块三的核心，是引导你完成一次从“**编码思维**”到“**工程思维**”的转变。
- **编码思维**更关注“**如何用代码实现一个特定的功能**”。它的产出是“能跑的代码”。
- **工程思维**则更关注“**如何系统性地、高质量地构建和维护一个软件产品**”。它需要考虑代码的可读性、可维护性、健壮性、团队协作等一系列超越功能本身的因素。它的产出是“高质量的、可持续发展的代码”。

你所学习的函数封装、调试流程、代码审查，都是“工程思维”的重要组成部分。具备了工程思维，你才能真正地“驾驭”AI，构建出可靠、有价值的软件应用，而不仅仅是生成一些一次性的小玩具。

</div>

---

## **课程成长路径：从“魔法学徒”到“作坊工匠”**

<div class="columns align-middle">
<div>

![width:250px](../../../lectures/images/2025-11-03-12-09-12.png)

</div>

<div>

| 阶段 | 目标 | 对应模块 |
| :--- | :--- | :--- |
| **魔法学徒** | 掌握编程基础，学习封装复用 | 模块 1-3 ✅ |
| **作坊工匠** | 处理真实数据，构建交互工具 | 模块 4-6 |
| **初级建筑师** | 构建综合项目，转化教学设计 | 模块 7-8 |

**我们已经成功完成了“魔法学徒”阶段的全部修行！**
你不仅掌握了编程的基础规则，更学会了封装与复用代码的核心思想。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 学习阶段的划分
本课程的三个阶段划分，借鉴了“**认知学徒制 (Cognitive Apprenticeship)**”的理念，旨在模拟传统手工艺中“学徒-工匠-大师”的成长路径。
- **魔法学徒 (模块1-3)**: 核心是**模仿与内化**。你通过模仿老师和AI，学习编程的基本“招式”（语法）和“心法”（思想），并完成一些结构化的练习。
- **作坊工匠 (模块4-6)**: 核心是**实践与应用**。你开始使用更专业的工具（如Pandas），处理更真实、更复杂的“原材料”（数据），并能独立打造出有实用价值的“作品”（数据报告、Web应用）。
- **初级建筑师 (模块7-8)**: 核心是**综合与创新**。你将综合运用所有知识和技能，设计并建造一个完整的、解决特定领域问题的“建筑”（综合项目），并开始思考如何将自己的能力传授给他人（教学设计）。

</div>

---

## **下一步预告：模块四 - AI数据分析师(上)**

<div class="columns ratio-6-4">
<div style="font-size: 0.82em;">

到目前为止，我们所有的“数据”都来自于我们自己在代码中“**硬编码**”的`world`字典，或是简单的文件名。

但现实世界中，更有价值的数据，往往存在于**外部文件**中，例如：
- 一份包含全班学生成绩的 **Excel 表格**。
- 一份从网站下载的、包含数千行数据的 **CSV 文件**。

**我们如何指挥AI：**
- 读取并理解这些复杂的表格数据？
- 从海量数据中，筛选出我们关心的特定行和列？
- 对数据进行清洗、统计，并发现其中的规律？

在下一个模块，我们将开启全新的篇章，学习如何成为一名“**AI数据分析师**”，并认识一个数据科学领域最强大的工具——**Pandas**！

</div>
<div class="align-middle-center">

![一个数据分析师与AI机器人一起，看着屏幕上由Excel表格转换成的酷炫图表 width:400px](../../../lectures/images/2025-11-21-01-05-17.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据分析与Pandas简介
- **数据分析 (Data Analysis)**: 是一个对数据进行检查、清洗、转换和建模的过程，目的是发现有用信息、提出结论并支持决策。它是当今几乎所有行业（科研、商业、教育等）都需要的核心能力。
- **结构化数据 (Structured Data)**: 指高度组织化的、通常是表格形式的数据，其中数据被组织成行和列。Excel和CSV文件都是典型的结构化数据。
- **Pandas**: 是Python生态中最流行的数据分析和处理库。它提供了一种名为`DataFrame`的核心数据结构，可以让你像操作Excel表格一样，轻松、高效地对数据进行读取、筛选、分组、聚合等各种复杂操作。学习Pandas，是进入数据科学世界的“入场券”。

</div>

---

# 课后练习

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

h1 {
  font-size: 60px;
  margin-bottom: 20px;
}

p {
  font-size: 24px;
  color: #555;
  line-height: 1.5;
}
</style>

<p>

*小提示：你已经是合格的“AI开发主管”了！<br>尝试将下面的需求，像设计蓝图一样拆解成清晰的步骤，然后指挥你的AI助手来完成开发和调试。*
</p>

---

## ****课后练习：让你的“文件助手”更智能 (基础)****

我们已经完成了一个实用的批量重命名工具。但是，一个“智能”的助手，应该更懂得“偷懒”和“猜测”用户的意图。

请向你的AI助手提出新的需求，对`batch_renamer.py`进行迭代升级。

#### **挑战一：更灵活的路径处理**
> *“如果用户在运行时，不提供`folder_path`参数，我们的脚本应该默认处理运行脚本时所在的文件夹。请为`batch_rename_files`函数增加这个默认行为。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：这需要修改函数的哪个部分？`os.getcwd()` 也许能派上用场。

</div>

---

## ****课后练习：让你的“文件助手”更智能 (进阶)****

#### **挑战二：更友好的前缀参数**
> *“除了现有的`prefix`参数，我希望函数能支持更友好的`semester_name`（学期名称）和`course_name`（课程名称）参数。当这些参数被提供时，它们会自动组合成`prefix`，例如 `2025秋-软件工程-`。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：函数的定义（参数列表）需要做什么改变？函数内部如何根据不同的输入参数来决定最终的`prefix`？

</div>

---

## ****课后练习：让你的“文件助手”更智能 (挑战)****

<div style="font-size: 0.95em;">

#### **挑战三：智能的“学期名”生成**
> *“如果用户没有提供`semester_name`，我希望脚本能根据当前的系统日期，自动生成学期名称。规则如下：”*
> - *如果当前月份在9月到1月之间，学期为 `{当年}秋` (例如 2025年11月 -> `2025秋`)。*
> - *如果当前月份在3月到6月之间，学期为 `{上一年}春` (例如 2025年4月 -> `2024春`)。*
> - *如果当前月份在7月到8月之间，学期为 `{当年}夏` (例如 2025年7月 -> `2025夏`)。*
> - *如果当前是2月，则让用户从两个学期中选择一个（例如，提示用户输入‘1’代表‘2024秋’，输入‘2’代表‘2025春’）。*
</div>

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：你需要什么新“工具”来获取当前日期？（提示：向AI询问`datetime`模块）。这个逻辑用`if-elif-else`结构会非常清晰。对于2月份的选择，你该如何实现用户交互？（提示：`input()`函数）

</div>

---

## ****课后练习：让你的“文件助手”更智能 (终极挑战)****

#### **挑战四：智能的“课程名”猜测**
> *“如果用户没有提供`prefix`和`course_name`，我希望脚本能变得更‘聪明’一点。它应该分析当前的文件夹路径，并从中**模糊匹配**出可能的课程名称。例如，如果脚本在`/Users/teacher/Documents/MyCourses/Software_Engineering_2025/`路径下运行，它应该能猜出课程名是‘Software Engineering’。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：这是一个开放性挑战！你该如何向AI描述这个“模糊匹配”的需求？是基于文件夹名称的关键词？还是需要一个预设的课程列表？尝试设计你的方案并指挥AI实现。

</div>