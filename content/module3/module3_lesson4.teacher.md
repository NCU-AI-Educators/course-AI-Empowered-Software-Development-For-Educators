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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 开场：模块收官项目
本页作为课程开场，核心目标是宣告模块三最终项目的开始，并点明项目主题——一个极具现实意义和实用价值的“批量文件整理助手”，从而激发学员的参与感和成就动机。

**核心要点**:
1. **点明主题**: 清晰地揭示本节课是模块的“收官项目”。
2. **项目定调**: 将项目定位为一个实用的、解决真实痛点的工具，提升其在学员心中的价值。
3. **建立期待**: 预示着学员将要综合运用本模块所学，完成一次最终的、有价值的挑战。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 回顾技能：你已是“AI开发主管”
本页旨在通过快速回顾本模块的核心技能，来巩固学员的“AI开发主管”新身份，并为接下来的“最终试炼”设定一个充满信心和仪式感的基调。

**核心要点**:
1. **巩固身份**: 再次强调“AI开发主管”的角色，并将其与本模块的三大核心技能（封装、纠错、评审）强绑定。
2. **能力梳理**: 将三个核心技能包装成更高级的“领导力”概念（授权、品控、决策），提升学员的自我效能感。
3. **设定基调**: 将最终项目定位为对这些高级技能的“最终试炼”，激发学员迎接挑战的信心和荣誉感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 项目使命：解决真实世界的“烦恼”
本页旨在引入项目背景，通过连接一个教师群体普遍存在的真实痛点（教学文件命名不统一），来阐明新项目的现实意义和应用价值，从而激发学员的内在学习动机。

**核心要点**:
1. **痛点切入**: 从一个非常贴近教师日常工作的“文件命名”痛点切入，能迅速引发共鸣。
2. **价值主张**: 清晰地定义项目的目标是“一键为所有文件添加统一前缀”，这是一个非常有吸引力的价值主张。
3. **效果可视化**: 通过“Before/After”的视觉对比，直观地展示项目的最终效果，让学员产生“我也想要这个工具”的强烈愿望。

</div>

---

## **第一步(1/2)：蓝图设计——明确输入与输出(IPO)**

在思考“如何做”之前，我们必须先彻底搞清楚“做什么”。一个专业的开发者，会花费大量时间来明确定义程序的**输入(Input)**和**输出(Output)**。

这就像做菜，你必须先弄清要用哪些食材（输入），以及最终想做出什么菜（输出），然后才能设计菜谱（处理流程）。

<div class="align-center">

![height:300px](../../../lectures/images/2025-11-21-12-23-55.png)

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 蓝图设计(1/2)：明确输入与输出(IPO)
本页旨在将原有的“蓝图设计”环节一分为二，首先聚焦于最重要的IPO（输入-处理-输出）分析。通过Mermaid图，让学员直观地理解，在设计任何算法前，都必须先清晰地定义它的“输入”和“输出”，这是专业软件开发的基石。

**核心要点**:
1. **强调IPO优先**: 明确传递“先定义输入输出，再设计处理过程”的核心思想。
2. **可视化分析**: 使用Mermaid图代替纯文本，将IPO模型更直观地呈现出来。
3. **建立心智模型**: 强化“做菜”的比喻，帮助学员建立“输入-处理-输出”的心智模型。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 蓝图设计(2/2)：设计处理流程
本页是“蓝图设计”的第二部分，专注于将文字化的“处理流程”转化为可视化的“流程图”。这能帮助学员更深入地理解算法的逻辑、循环和分支，并为下一步编写精确的Prompt打下坚实基础。

**核心要点**:
1. **算法可视化**: 使用Mermaid流程图，将抽象的文字步骤转化为具体的逻辑流程图。
2. **深化逻辑理解**: 流程图能清晰地展示循环（回到“遍历”）和条件分支（“是文件吗？”），帮助学员理解程序的核心控制流。
3. **连接下一步**: 一个清晰的流程图，本身就是一份完美的“伪代码”，可以直接翻译为下一步的“终极指令”。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 技术探索：向AI顾问咨询“新工具”
本页旨在教授学员一项重要的元技能：当遇到未知领域时，如何向AI提问以寻找解决问题所需的合适工具。这体现了从“让AI直接给答案”到“让AI帮我找工具”的思维转变。

**核心要点**:
1. **示范“探索性Prompt”**: 这个Prompt不要求AI直接写代码，而是询问“需要用到哪些工具”，这是一种更高层次、更具探索性的提问方式。
2. **角色重塑**: 将AI定位为“全能技术顾问”，引导学员学会在遇到新问题时，首先向AI寻求方向性指导，而不是盲目搜索。
3. **引入新知识**: 通过提问，自然地引出本项目所需的核心工具——Python的`os`模块。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 知识讲解：`os`模块——与操作系统对话
本页旨在快速介绍`os`模块中本次项目所需的核心函数。教学重点不是让学员记住所有细节，而是让他们对这些“新工具”的存在和大致用途有一个清晰的印象，以便在下一步编写Prompt时能够“言之有物”。

**核心要点**:
1. **清单式教学**: 以“工具清单”的形式，清晰地列出每个函数的作用，便于快速查阅。
2. **聚焦核心**: 只列出与本项目直接相关的函数，避免信息过载。
3. **建立联系**: 每个函数都直接对应了“算法蓝图”中的某一个步骤（如`os.listdir`对应“遍历文件夹”），让知识学以致用。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 第三步(1/3): 提出“愿景驱动”的初始指令
本页旨在引入一个全新的、更平滑的Prompt设计流程，解决了“终极指令”对新手而言过于困难的痛点。核心是教给学员如何从一个简单的“愿景驱动”指令开始，与AI进行协作。

**核心要点**: 
1. **降低门槛**: 明确指出“一次性写出完美指令是困难的”，承认学员的潜在痛点，并提供解决方案。
2. **引入新流程**: 提出“与AI迭代出指令”的新工作流。
3. **示范“愿景驱动”Prompt**: 提供一个非常简单、开放式的初始Prompt范例，极大地降低了学员的心理负担和操作门槛。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 第三步(2/3): 引导AI思考“边界情况”
本页是“迭代式Prompt”流程的核心环节。它旨在教会学员如何通过“挑战边界”的追问，引导AI从一个简单的方案走向一个更健壮、更周全的方案。

**核心要点**: 
1. **角色扮演**: 引入“压力测试工程师”的新角色，让学员理解自己此时的职责是“找茬”，而不是“接受”。
2. **教授核心思维**: 明确提出“边界情况”这一专业软件开发的核心概念。
3. **示范追问Prompt**: 提供一个结构化的“追问Prompt”，其中包含了具体的、可举一反三的例子（子文件夹、隐藏文件、重复执行），极具实践指导价值。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 第三步(3/3): 请求AI整合生成“终极指令”
本页是本课程“Prompt工程”教学的升华。它直接响应了用户的核心建议，即“让AI帮助写出Prompt”，并将其包装成一种高级的“元能力”。

**核心要点**: 
1. **思维升维**: 引入“元能力”和“利用AI优化与AI的沟通”的概念，让学员感受到一种思维上的跃迁。
2. **角色扮演升级**: 让AI扮演“需求分析师”，来为“AI程序员”写指令，这个比喻生动地解释了这种“元操作”的本质。
3. **示范“元Prompt”**: 提供一个非常具体、强大、可操作性极强的“元Prompt”范例，它清晰地指示AI去“总结讨论”并“生成指令”。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 第四步：审查并执行AI生成的“终极指令”
本页将原有的“第三步”转变为新流程的“第四步”。其核心教学目标，从“如何从零编写复杂指令”，转变为“如何审查AI生成的指令，并用它来驱动最终的编码”，这极大地降低了学员的认知负荷。

**核心要点**: 
1. **角色转换**: 学员的角色从“指令的创作者”变成了“指令的审查者”，更贴合“开发主管”的身份。
2. **成果展示**: 将“终极指令”定位为前序步骤的产出物，让学员对“与AI协作设计Prompt”的流程有直观的成果感知。
3. **强调审查**: 引导学员在执行前，要对AI生成的指令进行最后一次审查，培养严谨的工作习惯。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 植入专业思想：沙盒与数据安全
本页在最终动手环节前，插入一个关于“专业素养”和“安全意识”的教学点。这对于一个要操作真实文件的脚本来说至关重要。

**核心要点**:
1. **风险预警**: 明确告知学员，操作文件的脚本具有“破坏性”，建立其风险意识。
2. **引入专业流程**: 引入“沙盒测试”、“试运行”、“数据备份”等专业概念，培养学员严谨、负责的工程思想。
3. **流程可视化**: 通过Mermaid流程图，清晰地展示从开发到生产的各个阶段，并明确标出本节课实践所处的环节。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 18分钟
### 动手环节：见证混乱变为有序
本页是本模块的最终动手实践环节，旨在引导学员完成项目的全部流程，从准备“实验材料”，到执行脚本，再到最终验证结果，亲眼见证“混乱变为有序”的奇迹，从而获得巨大的成就感。这是本节课耗时最长的部分，需要给予学员充分的探索和试错时间。

**核心要点**:
1. **专业思想植入**: 在动手前通过文字和流程图，强调“沙盒”、“试运行”、“数据备份”等概念，培养学员的专业素养和安全意识。
2. **学以致用**: 让学员综合运用本模块学到的所有技能（Prompt编写、代码审查、终端操作）来完成一个完整的项目。
3. **即时反馈**: 项目的最终结果（文件被自动重命名）是即时的、可见的、符合预期的，能给予学员最强烈的正向反馈。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 模块总结：合格的“AI开发主管”
本页旨在对整个模块三的学习成果进行系统性总结和价值升华。通过再次强调“AI开发主管”的角色，并将本模块的三个核心主题（函数、调试、审查）包装成更高阶的“领导力”，来极大地提升学员的成就感和价值认同。

**核心要点**:
1. **价值升华**: 将技术技能（函数、调试、审查）包装成管理能力（授权、品控、决策），让学员认识到自己学到的不仅是技术，更是思想。
2. **巩固身份**: 再次肯定学员“AI开发主管”和“领导者”的新身份，完成本模块的角色塑造闭环。
3. **系统总结**: 清晰地回顾本模块的三个核心部分，帮助学员建立对所学知识的整体性认知。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 里程碑：完成“魔法学徒”阶段
本页旨在通过更新“课程成长路径图”，清晰地标记出学员已完成的学习进度，为他们提供一个里程碑式的成就感，并为下一阶段的学习做铺垫。

**核心要点**:
1. **进度可视化**: 在成长路径图上用一个清晰的“✅”标记出已完成的“魔法学徒”阶段，让学员对自己的成长有直观、清晰的感知。
2. **给予成就感**: 明确宣告“我们已经成功完成了...全部修行！”，给予学员阶段性成功的正向反馈。
3. **承前启后**: 为模块三画上一个圆满的句号，并自然地将学员的视线引向下一阶段“作坊工匠”。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 承前启后：预告“AI数据分析师”
本页作为模块结尾，核心是承上启下。通过指出当前项目在“数据来源”上的局限性，制造出对处理真实世界复杂数据（Excel, CSV）的新需求，从而为下一模块“数据分析”建立强烈的学习动机。

**核心要点**:
1. **制造新痛点**: 指出当前项目处理的数据过于简单（硬编码、文件名），与真实世界的复杂数据形成对比，创造学习新知识的内在需求。
2. **引出新主题**: 通过设问，引出数据分析的核心任务（读取、筛选、清洗、统计）。
3. **建立新期待**: 预告下一模块全新的角色“AI数据分析师”和强大的新工具“Pandas”，最大限度地激发学员的学习期待。

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