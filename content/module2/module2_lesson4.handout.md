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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-13-23-34-34.png)

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

# 模块二：与AI对话——学习编程的核心规则
## 第8节课: 模块收官项目：创造你自己的江湖传说

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 项目课的意义
项目课（Project-based Learning）是检验和巩固知识的最佳方式。与之前单点知识的学习不同，项目课要求你：
1.  **综合运用**: 将多个独立的知识点（变量、条件、循环）组合起来，解决一个更复杂、更完整的问题。
2.  **主动设计**: 从“学习者”转变为“创造者”，你需要自己做出设计决策（例如，你想为游戏增加什么功能）。
3.  **问题解决**: 在实践中，你几乎一定会遇到预料之外的问题和Bug，这个过程将极大地锻炼你分析和解决问题的能力。

本节课的目标，就是让你在AI的辅助下，完整地体验一次“从想法到实现”的迷你开发周期。

</div>

---

## **回顾：我们已集齐创世的“三原色”**

<div class="columns ratio-6-4">
<div style="font-size: 0.85em;">

在今天的前面几节课，我们已经掌握了构建任何复杂程序的“创世之力”：

- **变量 (Variables)**
  - 赋予世界“**地图**”与“**状态**”。

- **条件 (Conditions)**
  - 赋予世界“**规则**”与“**选择**”。

- **循环 (Loops)**
  - 赋予世界“**心跳**”与“**时间**”。

这节课，我们不学任何新语法。我们的任务，是像一位真正的“游戏设计师”，将这三种最基本的能力**组合**起来，为我们的武侠世界增添独一无二的细节与创意。

</div>
<div class="align-middle-center">

![一个调色盘，红黄蓝三原色混合在一起，创造出五彩斑斓的色彩 width:400px](../../../lectures/images/2025-11-14-00-04-38.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 结构化程序设计
“变量、条件、循环”这三个概念，是“结构化程序设计”理论的基石。该理论指出，任何复杂的算法逻辑，都可以由三种基本控制结构组合而成：
1.  **顺序 (Sequence)**: 代码从上到下依次执行。
2.  **选择 (Selection)**: 即条件判断（`if-else`），根据条件选择不同的执行路径。
3.  **重复 (Repetition)**: 即循环（`for`, `while`），重复执行某段代码。

这意味着，你现在掌握的工具虽然简单，但理论上已经足以构建出任何复杂的程序。本节课的挑战，就是对你“组合”这些基本结构，解决实际问题的能力的第一次综合考验。

</div>

---

## **项目使命：从“引擎”到“游戏”**

<div class="columns ratio-6-4">
<div>

在前三节课，我们已经成功构建了一个“**迷你游戏引擎**”。它拥有了地图、状态、规则和心跳，已经是一个“可运行”的框架。

但是，这个世界还很原始，还不能称之为一个“游戏”。

这节课，我们的使命就是扮演“**关卡设计师**”和“**剧情策划**”的角色，为这个框架填充血肉，注入灵魂，把它从一个“引擎”变成一个真正“好玩”的“游戏”。

**你的世界，你做主！**

</div>
<div class="align-middle-center">

![一个游戏设计师正在绘制地图、设计角色和剧情 width:400px](../../../lectures/images/2025-11-13-23-41-19.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 游戏开发中的角色分工
在专业的游戏开发团队中，通常有明确的角色分工：
- **游戏引擎程序员 (Engine Programmer)**: 负责开发和维护游戏的基础框架，如图形渲染、物理模拟、内存管理等。我们前几节课构建的循环和指令解析器，就属于最基础的引擎功能。
- **游戏玩法程序员 (Gameplay Programmer)**: 负责实现游戏的核心玩法和逻辑，例如角色的技能、战斗系统、任务流程等。
- **关卡设计师 (Level Designer)**: 负责设计游戏中的具体关卡，包括地图布局、敌人配置、谜题设计等。
- **剧情策划 (Narrative Designer/Writer)**: 负责编写游戏的故事情节、角色对话、世界观设定等。

在本节课，你将一人分饰多角，同时扮演“玩法程序员”、“关卡设计师”和“剧情策划”，来丰富你的游戏世界。

</div>

---

## **本次创意工坊的“技术起点”**

<div class="columns ratio-6-4">
<div style="font-size: 0.88em;">

在开始挥洒创意之前，让我们先明确我们这节课工作的“地基”。

我们每个人的手中，都应该已经拥有一个来自上一节课的、初级的“**迷你游戏引擎**”。它应该具备：

- 一个用`字典`和`列表`构建的 `world` 世界蓝图。
- 一个 `while True` 的游戏主循环，让世界持续运转。
- 一个能响应 `/go`、`/look`（可显示物品）和 `/quit` 指令的 `if-elif-else` 解析器。

这节课，我们就是在这个坚实的地基上，添砖加瓦，描绘属于我们自己的多彩世界！

</div>
<div class="align-middle-center">

![乐高积木，简单的几块积木，拼搭出极其复杂的城堡或飞船 width:400px](../../../lectures/images/2025-11-13-23-42-57.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 基线代码 (Baseline Code)
在软件开发中，“基线”或“基线代码”指的是一个项目的某个稳定、可运行的版本，它通常作为新功能开发或下一个迭代周期的起点。

我们上一节课完成的“迷你游戏引擎”，就是我们本次项目课的“基线代码”。它包含了我们这个模块所学的所有核心知识点：
- **数据结构**: `world` 字典，`items` 列表。
- **控制流**: `while True` 循环，`if-elif-else` 条件判断。
- **输入/输出**: `input()` 和 `print()`。

从这个基线出发，你可以专注于添加新的“功能”，而不需要从零开始重写基础框架。这是迭代开发模式的典型实践。

</div>

---

## **核心方法论：两阶段提示词实践法**

这节课，我们采用一种全新的训练方法，来体验AI辅助开发的两种不同模式。对于你选择的任何一个挑战，都需要分两步完成。

<div class="columns" style="font-size: 0.75em;">
<div class="styled-div" style="font-size: 0.8em;">

### **第一阶段：“愿景驱动”** (先有)
1.  **目标**：快速验证想法，获得即时反馈。
2.  **方法**：用**纯自然语言**向AI描述你的**最终目的**。
    > **Prompt示例**：
    > 你好，我想让我的游戏能拾取物品，比如输入‘/take sword’，地上的剑就到我包里了。
3.  **产出**：一个能运行的脚本，但你可能不完全理解其内部逻辑。
4.  **关键后续**：拿到代码后，立刻追问AI：
    > 请一步步向我解释你刚刚生成的代码，特别是处理‘/take’指令的部分，它的逻辑是什么？

</div>
<div class="styled-div" style="font-size: 0.8em;">

### **第二阶段：“设计驱动”** (再好)
1.  **目标**：掌握逻辑，精准控制，产出高质量代码。
2.  **方法**：**另起一个会话**，像架构师一样，给出**清晰、分步**的指令。
    > **Prompt示例**：
    > 请帮我实现`/take`指令：1. 为玩家创建名为`inventory`的空列表... 2. 检查指令是否为两部分... 3. 检查物品是否存在... 4. 写入到新的脚本...
3.  **产出**：一个你完全理解的、逻辑严谨的脚本。
4.  **核心价值**：通过这个过程，你将真正**驾驭**AI，而不仅仅是**使用**它。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 两种协作模式的深度解析
这两种模式代表了与AI协作的两种不同层次和场景：

- **“愿景驱动” (Vision-Driven / Declarative)**:
  - **特点**: 你只声明“**做什么 (What)**”，而将“**如何做 (How)**”的细节完全交给AI。
  - **优点**: 速度极快，非常适合早期创意探索、快速原型验证、或处理你不关心实现细节的一次性任务。
  - **缺点**: 产出代码的质量和逻辑可能不可控，你对代码的理解是“被动”的。

- **“设计驱动” (Design-Driven / Imperative)**:
  - **特点**: 你不仅定义“做什么”，更重要的是定义了“**如何做**”的详细步骤和逻辑。
  - **优点**: 你对代码有完全的掌控力，产出的代码逻辑严谨、符合你的设计，并且你对代码的理解是“主动”的。
  - **缺点**: 需要你对问题有更深入的思考和分解，前期花费的时间更多。

一个成熟的AI协作者，应该能根据任务的性质，在这两种模式之间灵活切换。

</div>

---

## **挑战菜单：选择你的任务！**

<div class="styled-div" style="font-size: 0.6em;">

现在，进入开放式的“**创意工坊**”。请在你已有的代码基础上，**任选以下列表中的一项**，并使用我们刚刚学习的“**两阶段提示词实践法**”来完成它。（**开始之前记得先备份当前版本,方便失败时复制备份的内容到实验用的脚本文件中**）

### **创意功能列表 (任选一项)**

1.  **实现 `/take [物品名]` 指令**
    - 效果：让玩家可以从当前地点拾取物品，并放入背包。
    - 核心逻辑：物品从`world`中的`items`列表，移动到玩家的`inventory`列表。
2.  **实现 `/inventory` 或 `/i` 指令**
    - 效果：让玩家可以查看自己背包`inventory`里的所有物品。
    - 核心逻辑：使用`for`循环遍历`inventory`列表并打印。
3.  **实现 `/drop [物品名]` 指令**
    - 效果：让玩家可以从背包中丢弃物品，物品会出现在当前地点。
    - 核心逻辑：`/take`指令的逆向操作。
4.  **实现“斜杠指令” (例如 `/salute`)**
    - 效果：输入`/salute`或`/meditate`等指令，打印一段有趣的描述性文字。
    - 核心逻辑：增加几个简单的`elif`分支，匹配特定指令并打印固定文本。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 各挑战的核心技术点
- **`/take`**: 这是最有挑战性的任务。它需要你处理：
  - 字符串解析：从 `"/take sword"` 中分离出 `"sword"`。
  - 条件判断：检查物品是否存在于房间的 `items` 列表中。
  - 列表操作：从 `items` 列表中移除（`remove()`），并添加到 `inventory` 列表中（`append()`）。
- **`/inventory`**: 这个任务相对简单，核心是：
  - 条件判断：检查 `inventory` 列表是否为空。
  - `for` 循环：遍历 `inventory` 列表并打印每一项。
- **`/drop`**: 这是 `/take` 的逆向逻辑，技术点类似，是很好的巩固练习。
- **斜杠指令**: 这是最简单的任务，只需要增加 `elif command == "/salute":` 这样的分支即可。非常适合用来快速体验“两阶段法”的流程。

</div>

---

## **实践参考：`take`指令的两阶段实现**

如果你在实践中遇到困难，可以参考`take`指令的两阶段实现过程，它清晰地展示了两种Prompt风格的差异。

<div class="columns">
<div>

#### **第一阶段：“愿景驱动” Prompt**
> “我想在我的文本游戏中加入一个拾取物品的功能。比如，如果地上有‘一把生锈的剑’，我输入‘/take 一把生锈的剑’，这把剑就应该从地上消失，然后出现在我的背包里。如果地上没有这个东西，就告诉我‘这里没有这个东西’。”

**➡️ 目标：快速获得一个能用的原型。**

</div>
<div class="styled-div" style="font-size: 0.6em;">

#### **第二阶段：“设计驱动” Prompt**
> “请帮我实现`/take`指令，逻辑如下：
> 1. 在`while`循环前，创建一个名为`inventory`的空列表。
> 2. 在主循环中，为以`'/take '`开头的指令增加`elif`分支。
> 3. 在分支中，先分离出玩家想拾取的物品名。
> 4. 检查该物品是否存在于当前房间的`items`列表中。
> 5. 如果存在，就从`items`列表移除，并添加到`inventory`列表，然后打印成功信息。
> 6. 如果不存在，就打印‘这里没有这个东西。’”

**➡️ 目标：产出逻辑严谨、自己完全掌控的代码。**

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Prompt 风格分析
- **“愿景驱动” Prompt**:
  - **特点**: 充满了具体的“**示例**”（如果地上有...，我输入...，它就应该...）。这种“**示例驱动 (Example-driven)**”的提问方式，对于大型语言模型非常有效，因为它能帮助AI快速理解你的意图。
  - **风险**: AI可能会为了实现你的示例，而做出一些“黑箱”式的实现，或者引入一些你未预料到的复杂逻辑。

- **“设计驱动” Prompt**:
  - **特点**: 是一种“**算法描述**”。你实际上是在用自然语言，为AI编写一份“伪代码”或“操作手册”。
  - **优势**: 你对最终的代码结构有完全的预期和控制。AI在这里扮演的是一个“翻译官”的角色，将你的逻辑翻译成Python语法。这使得最终的代码更容易被你理解和维护。

</div>

--- 

## **“我的江湖”作品发布会**

<div class="columns ratio-6-4">
<div style="font-size: 0.85em;">

在大家实现自己的创意后，我们将举办一个“**我的江湖”作品发布会**。

我们将邀请几位老师，自愿上台（共享屏幕），向大家展示你用“两阶段法”完成的作品：

- 你选择了哪个挑战？最终实现了什么效果？
- 对比两个阶段的Prompt，你有什么不同的体验和感悟？
- **“愿景驱动”的Prompt**为你带来了什么便利或困惑？
- **“设计驱动”的Prompt**有什么优势和缺点？
- 这个过程，如何改变了你对“与AI协作”的看法？

**这将是你第一次，作为一名驾驭AI的架构师，分享你的思考与洞见！**

</div>
<div class="align-middle-center">

![一个开发者在台上兴奋地展示自己的游戏作品 width:400px](../../../lectures/images/2025-11-13-23-53-42.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 元认知与学习共同体
- **元认知 (Metacognition)**: 指的是“关于认知的认知”，即对自己思考过程的思考。本次发布会引导你反思“两种Prompt模式的差异”，就是在进行一次关于“如何更好地与AI协作”的元认知活动。培养元认知能力，是成为高效学习者的关键。

- **学习共同体 (Learning Community)**: 通过分享和讨论，学员之间不再是孤立的学习者，而是形成了一个共同探索、互相启发的“学习共同体”。在这种氛围中，知识的流动是多向的，每个人既是学习者，也是贡献者。这能极大地提升整体的学习效果和课堂的凝聚力。

</div>

---

## **头脑风暴：你的“自动化”时刻**

<div class="columns ratio-6-4">
<div style="font-size: 0.8em;">

在你成功地为游戏世界注入“心跳”之后，你已经真正掌握了“自动化”的魔法。现在，让我们将这份能力照进现实。

**在你的教学或科研中，有没有哪一件让你感到烦恼的、需要手动重复的任务，是可以用我们学到的“循环”和“条件”来解决的？**

- 是不是需要**为全班**学生的作业（文件名），逐一检查是否符合“学号-姓名”的格式？
- 是不是需要**从大量的**文件存档，找出所有提到自己名字的文件？
- 是不是需要**对一个文件夹里**的所有图片，凡是大于10MB的，就把它移动到“高清图片”文件夹？

**把你的想法分享出来，它可能就是你的下一个AI应用！**

</div>
<div class="align-middle-center" style="flex-direction: column;">

![一个人坐在书桌前，头脑中迸发出许多关于自动化的创意火花 width:300px](../../../lectures/images/2025-11-13-23-55-37.png)

<div class="tip" style="margin-top: 20px; font-size: 0.6em;">
<strong>点子示例</strong><br>
指挥AI写一个脚本，遍历一个文件夹里的所有文件名，如果文件名不包含“最终版”三个字，就把它移动到`待检查`文件夹。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 脚本自动化 (Scripting Automation)
我们这节课构建的，本质上是一个“**脚本 (Script)**”。脚本通常指用来“自动化”一系列任务的、相对简短的程序。
脚本自动化在日常工作和科研中应用极其广泛，它可以：
- **文件/文件夹管理**: 批量重命名、移动、复制、删除文件。
- **文本处理**: 从大量的文本文件中提取信息、替换内容、格式化报告。
- **数据处理**: 自动化地从Excel或CSV文件中读取数据，进行计算和分析。
- **Web自动化**: 控制浏览器自动访问网页、填写表单、抓取数据（这需要更高级的库）。

你今天学到的“循环”和“条件”，是实现所有这些自动化任务的逻辑核心。识别出你工作中的“重复性”和“规则性”任务，是开启自动化之路的第一步。

</div>

---

## **Aha! 时刻：编程的秘密**

<div class="columns ratio-6-4">
<div>

大家发现了吗？

我们这节课**没有学习任何新的语法**！

我们只是将已知的“三原色”——变量、条件、循环——以一种有意义的方式**组合**了起来。

这就是编程最深刻，也最美妙的秘密：

> **用有限的、简单的规则，去创造和应对无限复杂的世界。**

掌握了“组合”的技巧，你就掌握了编程的精髓。

</div>
<div class="align-middle-center">

![乐高积木，简单的几块积木，拼搭出极其复杂的城堡或飞船 width:400px](../../../lectures/images/2025-11-13-23-57-23.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 计算思维：组合与抽象
本页揭示了“计算思维 (Computational Thinking)”中的两个核心概念：
- **组合 (Composition)**: 将简单、已有的部分（如变量、条件、循环）组合起来，构建出更复杂的系统。这是解决复杂问题的基本策略。我们这节课将多个`elif`分支组合成一个指令解析器，就是“组合”的体现。

- **抽象 (Abstraction)**: 忽略细节，关注本质。在下一个模块，我们将学习“函数”，它是编程中最重要的抽象工具。我们可以将一个复杂的“组合”（例如处理`/take`指令的所有逻辑）打包成一个简单的函数，以后我们只需要“调用”这个函数名，而无需关心其内部的复杂组合。

“组合”让我们能从小到大构建复杂系统，“抽象”则让我们能管理这种复杂性，而不被细节淹没。这两者是软件工程中相辅相成的核心思想。

</div>

---

## **模块二总结：从“魔法观众”到“世界架构师”**

<div class="columns ratio-6-4">
<div style="font-size: 0.85em;">

**祝贺你，完成了模块二的全部旅程！**

让我们回顾一下这条充满挑战与惊喜的成长之路：

- **第5节 (变量)**
  - 我们学会了用“**蓝图**”来描绘世界，让程序拥有了记忆。
- **第6节 (条件)**
  - 我们学会了为世界添加“**规则**”，赋予了程序决策的能力。
- **第7节 (循环)**
  - 我们为世界注入了“**心跳**”，让程序拥有了持续运转的动力。
- **第8节 (项目)**
  - 我们最终将所有能力融会贯通，成为了能主导游戏世界、充满创意的“**设计师**”。

</div>
<div class="align-middle-center">

![一条从山脚到山顶的成长路径图，沿途有变量、条件、循环、项目四个里程碑 width:400px](../../../lectures/images/2025-11-14-00-00-32.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 模块二知识体系复盘
本模块，你已经掌握了编程最核心的“控制流”和“数据结构”基础。
- **数据结构 (Data Structures)**:
  - 你学会了如何使用**变量**存储单个数据。
  - 你学会了如何使用**列表**存储有序的集合。
  - 你学会了如何使用**字典**存储键值对，为复杂实体建模。
- **控制流 (Control Flow)**:
  - 你掌握了**顺序结构**（代码默认执行方式）。
  - 你掌握了**选择结构**（`if-elif-else`），让程序学会做决策。
  - 你掌握了**循环结构**（`for`和`while`），让程序学会重复执行任务。

这些知识共同构成了你理解和编写任何程序逻辑的基础。你已经不再是一个门外汉，而是真正踏入了编程世界的大门。

</div>

---

## **新的“痛点”：臃肿的主循环**

<div class="columns ratio-6-4">
<div style="font-size: 0.8em;">

我们构建的武侠世界取得了显著的进展！

但是，作为一个追求卓越的“架构师”，你很快会发现一个新的痛点：我们的“游戏主循环”开始变得**臃肿和混乱**了。

想象一下，如果我们未来要增加10个、20个指令，我们的主循环代码会变成什么样？
```python
while True:
    # ...
    if command.startswith("/go "):
        # 处理go的一大段代码
    elif command.startswith("/take "):
        # 处理take的一大段代码
    elif command.startswith("/drop "):
        # 处理drop的一大段代码
    elif command.startswith("/talk "):
        # 处理talk的一大段代码
    # ... 更多更多的elif
```

</div>
<div class="align-middle-center" style="flex-direction: column;">

![一个人面对着一团乱麻般的代码，显得很苦恼 width:350px](../../../lectures/images/2025-11-14-00-01-32.png)

<p style="margin-top: 1rem; font-size: 0.9em;">这就像一个<strong>杂乱无章的巨大抽屉</strong>，所有东西都堆在一起，找起来费劲，改起来也容易出错。</p>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 代码质量与“代码味道”
我们遇到的新痛点，是软件工程中一个关于“**代码质量 (Code Quality)**”的核心问题。高质量的代码不仅功能正确，还应该具备：
- **可读性 (Readability)**: 容易被人类理解。
- **可维护性 (Maintainability)**: 容易被修改和扩展。

当代码变得“臃肿”和“混乱”时，它的可读性和可维护性就急剧下降。在软件工程中，我们把这种预示着深层问题的代码特征，称为“**代码味道 (Code Smell)**”。
- **过长的函数/方法**: 我们的`while`循环体现在就有点过长了。
- **巨大的`if-elif-else`链**: 这是另一种常见的“代码味道”，它违反了“单一职责原则”。

闻到“代码味道”，并用“重构”的手段去消除它，是优秀程序员必备的素养。

</div>

---

## **下一步预告：模块三 - 代码复用与人机协作**

<div class="columns ratio-6-4">
<div style="font-size: 0.9em;">

为了解决“功能代码”级别的重复和混乱问题，并进一步提升我们与AI的协作效率，在下一个模块，我们将学习：

- **函数 (Functions)**
  - 学会如何将一段代码“**打包**”成一个可以随时调用、重复使用的“**功能积木**”。

- **与AI结对调试 (Pair Debugging)**
  - 当我们的“积木”出现问题时，如何引导AI**自我检查**、**修复代码**，让你真正成为AI的“项目经理”。

**我们即将从“游戏设计师”，升级为更全能的“AI开发主管”！**

</div>
<div class="align-middle-center">

![一些代码块被打包成一个个独立的积木，然后被一只手轻松地取用和组合 width:400px](../../../lectures/images/2025-11-14-00-02-49.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 模块三核心概念展望
- **函数 (Function)**: 函数是组织好的、可重复使用的，用来实现单一，或相关联功能的代码段。它是现代编程语言中进行“**抽象**”和“**模块化**”的最基本单位。通过将代码封装进函数，我们可以：
  - **提高代码复用性**: 同一段逻辑无需重复编写。
  - **提高代码可读性**: 主循环将由一系列高层次的函数调用组成，逻辑一目了然。
  - **降低维护成本**: 修改一个功能的逻辑，只需在其对应的函数内部进行，不会影响到其他部分。

- **调试 (Debugging)**: 寻找并修复代码中错误的过程。与AI结对调试，指的是利用AI的分析能力，来帮助我们定位和修复Bug。这是一种能极大提升开发效率的新型工作范式。

</div>