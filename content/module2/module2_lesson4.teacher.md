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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场：宣告项目课的开始
本页作为模块二的收官项目课，其核心目标是营造一种“毕业设计”的仪式感和兴奋感。

**核心要点**：
1.  **承上启下**: 快速回顾之前学过的“三原色”，强调本节课是知识的“融会贯通”，而非学习新知。
2.  **降低焦虑**: 明确告知“不学任何新语法”，可以有效降低学员对项目课的畏难情绪。
3.  **角色扮演**: 赋予学员“游戏设计师”的角色，激发他们的创造欲和主人翁意识。
4.  **设定目标**: “创造你自己的江湖传说”这个目标宏大而富有吸引力，能迅速点燃学员的热情。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 知识回顾与信心建立
本页的核心目标是在项目开始前，快速回顾本模块的核心知识，并建立学员的信心。

**核心要点**：
1.  **系统性回顾**: 将之前三节课的核心内容高度概括为“三原色”，并用关键词（地图、规则、心跳）进行总结，帮助学员快速回顾并形成知识体系。
2.  **“三原色”比喻**: 这个比喻非常强大，它暗示了学员手中工具的“基础性”和“无限可能性”，能极大地激发他们的创造欲。
3.  **强调“组合”**: 明确指出本节课的核心是“组合”而非“学习新知”，将学员的注意力引导到如何创造性地应用已有知识上。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 明确项目目标与角色转换
本页旨在清晰地定义本次项目课的核心任务，并再次进行角色转换，激发学员的创造性。

**核心要点**：
1.  **区分“引擎”与“游戏”**: 这个对比非常重要。它让学员理解到，一个可运行的程序框架（引擎）和一个有趣的产品（游戏）之间，还存在着“内容”和“设计”的鸿沟。
2.  **引入新角色**: “关卡设计师”和“剧情策划”这两个新角色，引导学员的思维从“如何实现功能”转向“如何让游戏更好玩”，从技术思维转向设计思维和产品思维。
3.  **赋予自主权**: “你的世界，你做主！”这句话，给予了学员极大的创造自由度和主人翁感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 统一技术基线
本页的目标是在开放式项目开始前，确保所有学员都有一个统一、可用的代码基础。

**核心要点**：
1.  **“地基”比喻**: 将基础代码比作“地基”，形象地说明了其重要性，也暗示了本节课的工作是在其上“添砖加瓦”，而非推倒重来。
2.  **清单式检查**: 清晰地列出了基础代码应具备的三个核心要素，方便学员自我检查。
3.  **提供支持**: 考虑到部分学员可能没有跟上，主动提出可以寻求帮助，获取基础代码，确保了所有学员都能参与到项目课中，体现了教学的包容性。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教授核心元技能：两种Prompt模式
本页是本次项目课的核心教学法，旨在让学员亲身体验并对比两种与AI协作的模式。

**核心要点**：
1.  **方法论构建**: 将实践过程提炼为“两阶段提示词实践法”，并赋予其“愿景驱动（先有）”和“设计驱动（再好）”的名称，易于理解和记忆。
2.  **对比学习**: 通过并列对比，清晰地展示了两种模式在“目标”、“方法”、“产出”和“价值”上的巨大差异。
3.  **强调“解释”环节**: 在第一阶段，特别强调了“追问AI解释代码”这一关键后续步骤。这是利用AI进行学习的核心技巧，能帮助学员快速地从“黑箱使用者”转变为“白箱理解者”。
4.  **锚定核心价值**: 在第二阶段，明确点出其核心价值是“驾驭”AI，与课程的终极目标相呼应。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开放式、选择性的项目实践
本页是项目实践的核心环节，其设计旨在给予学员充分的自主性和选择权。

**核心要点**：
1.  **“菜单”式选择**: 提供一个“挑战菜单”，而不是规定所有人都做同一个任务。这种选择性可以更好地匹配不同学员的兴趣和学习进度，提高参与感。
2.  **明确任务细节**: 每个挑战都清晰地描述了“效果”和“核心逻辑”，为学员提供了足够的脚手架，让他们不至于无从下手。
3.  **风险提示**: “开始之前记得先备份”这是一个非常重要、非常专业的实践提示。它教给学员版本控制的基本思想，并降低他们“怕改错”的恐惧心理。
4.  **难度分层**: 四个挑战在逻辑复杂度上是不同的（例如，`take`涉及两个列表的修改，而`salute`只是一个简单的`elif`），这实际上形成了一个隐性的难度分层，让不同水平的学员都能找到适合自己的挑战。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供范例，降低难度
本页作为一个“参考”或“脚手架”，其目标是在开放式探索中为可能遇到困难的学员提供支持。

**核心要点**：
1.  **具体范例**: 针对最复杂的`/take`指令，提供了一个完整的两阶段Prompt范例，这可以作为学员模仿的“模板”。
2.  **强化对比**: 将两种风格的Prompt并列放置，能让学员最直观地感受到从“模糊愿景”到“清晰设计”的思维转变过程。
3.  **重申目标**: 在每个Prompt下方，再次强调了该阶段的核心目标（“快速原型” vs “完全掌控”），巩固了之前建立的方法论。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 同行学习与反思分享
本页旨在通过一个“作品发布会”的形式，将个人的实践学习，转化为一个集体的、分享反思的学习体验。

**核心要点**：
1.  **成果展示**: 为学员提供一个展示自己劳动成果的舞台，能极大地满足其成就感。
2.  **引导深度反思**: 提供的分享要点，不是关注“代码写得好不好”，而是关注“两种模式的体验和感悟”、“对AI协作看法的改变”等更深层次的“元认知”问题。这引导学员从“做事”上升到“思考”。
3.  **同行学习 (Peer Learning)**: 其他学员通过聆听分享，可以了解到不同挑战的实现思路，以及同学对两种协作模式的真实感受，这比老师单方面的讲解更具说服力和启发性。
4.  **价值肯定**: “这将是你第一次，作为一名驾驭AI的架构师...”这句话，给予了分享者极高的价值肯定和荣誉感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 知识迁移与应用启发
本页的核心目标是引导学员将课堂上学到的编程知识，迁移到他们自己的实际工作场景中，实现“学以致用”。

**核心要点**：
1.  **价值外溢**: 将编程能力的价值，从“做好玩的游戏”，延伸到“解决真实工作烦恼”，极大地提升了课程的实用性和学员的学习动机。
2.  **场景启发**: 提供了三个非常具体、贴近教师日常工作的自动化场景（检查作业、查找文件、整理图片），作为“引子”，启发学员进行联想和思考。
3.  **强调核心技术**: 在每个场景描述中，都加粗了“为全班”、“从大量的”、“对一个文件夹里”等词语，这些都明确指向了“循环”这一核心技术。
4.  **提供具体点子**: “点子示例”提供了一个非常具体、可操作的想法，进一步降低了学员思考的门槛，让他们能更快地产生自己的创意。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 思想升华：揭示“组合”的力量
本页旨在项目课的结尾，进行一次思想上的升华，揭示编程的本质在于“组合”。

**核心要点**：
1.  **制造“Aha! 时刻”**: 通过“我们没有学习任何新的语法！”这个惊奇的发现，引导学员顿悟到，他们能力的提升并非来自新知识的堆砌，而是来自对旧知识的灵活运用。
2.  **揭示深刻哲理**: 将编程的秘密总结为“用有限的规则，创造无限的世界”，这是一个非常深刻且富有启发性的哲学观点，能极大地提升课程的格局。
3.  **强化核心比喻**: 再次使用“乐高积木”这个比喻，与“三原色”相呼应，将“组合创造复杂性”这一核心思想视觉化、形象化。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 模块总结与价值肯定
本页作为模块二的最后一页，其核心目标是系统性地总结本模块的学习成果，并给予学员强烈的价值肯定和成就感。

**核心要点**：
1.  **里程碑式总结**: 清晰地列出了本模块四节课的核心主题和价值（蓝图、规则、心跳、设计师），帮助学员回顾并巩固整个模块的知识体系。
2.  **呼应开篇**: “从‘魔法观众’到‘世界架构师’”这个标题，与模块开篇时“从‘产品总监’到‘首席架构师’”的角色转变相呼应，形成完美的闭环，展示了学员在本模块的成长。
3.  **视觉化成长**: “成长路径图”这张图片，直观地展示了学员一步步“登山”的过程，极具仪式感和成就感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 制造新的认知冲突，引出下一模块
本页的设计与之前课程的结尾页一脉相承，其核心目标是在一个模块成功结束后，立刻制造一个新的、更高级的“痛点”，从而为下一个模块的学习建立强烈的动机。

**核心要点**：
1.  **肯定现有成就**: “取得了显著的进展！”——先扬后抑，让学员在接受新问题时不会感到挫败。
2.  **预见未来问题**: 将问题从“当前”延伸到“未来”（增加10个、20个指令），让学员意识到当前架构的“可扩展性”问题。
3.  **生动比喻**: “臃肿和混乱”、“杂乱无章的巨大抽屉”等比喻，让学员能直观地感受到代码质量下降带来的痛苦。
4.  **代码示例**: 通过展示一个不断变长的`if-elif`链，将这种“混乱”具象化。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 预告下一模块，完成课程闭环
本页作为模块二的终点和模块三的起点，其核心目标是清晰地预告下一模块的内容，并展示它如何解决我们刚刚提出的“痛点”。

**核心要点**：
1.  **问题-解决方案结构**: 将“函数”作为解决“臃肿主循环”问题的终极方案来引入，逻辑清晰，动机充足。
2.  **核心比喻**: “打包”、“功能积木”是非常经典且有效的比喻，它让学员能直观地理解函数“代码复用”和“封装”的核心价值。
3.  **人机协作升级**: 明确指出模块三将学习“与AI结对调试”，这预示着人机协作的模式将进入一个更高级、更主动的阶段。
4.  **角色升级**: “从‘游戏设计师’，升级为更全能的‘AI开发主管’”——用一次激动人心的“角色升级”，为模块二画上圆满句号，并为模块三建立强烈的期待感。

</div>