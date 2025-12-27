---
marp: true
theme: default
paginate: true
size: 16:9
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
</style>

![bg blur:3px brightness:60%](../../../lectures/images/2025-10-30-10-00-00.png)

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

---

## **回顾：我们已集齐创世的“三原色”**

<div class="columns">
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

![一个调色盘，红黄蓝三原色混合在一起，创造出五彩斑斓的色彩 width:400px](../../../lectures/images/2025-10-29-10-15-15.png)

</div>
</div>

---

## **项目使命：从“引擎”到“游戏”**

<div class="columns">
<div>

在前三节课，我们已经成功构建了一个“**迷你游戏引擎**”。它拥有了地图、状态、规则和心跳，已经是一个“可运行”的框架。

但是，这个世界还很原始，还不能称之为一个“游戏”。

这节课，我们的使命就是扮演“**关卡设计师**”和“**剧情策划**”的角色，为这个框架填充血肉，注入灵魂，把它从一个“引擎”变成一个真正“好玩”的“游戏”。

**你的世界，你做主！**

</div>
<div class="align-middle-center">

![一个游戏设计师正在绘制地图、设计角色和剧情 width:400px](../../../lectures/images/2025-10-30-10-01-01.png)

</div>
</div>

---

## **本次创意工坊的“技术起点”**

<div class="columns">
<div style="font-size: 0.88em;">

在开始挥洒创意之前，让我们先明确我们这节课工作的“地基”。

我们每个人的手中，都应该已经拥有一个来自上一节课的、初级的“**迷你游戏引擎**”。它应该具备：

- 一个用`字典`和`列表`构建的 `world` 世界蓝图。
- 一个 `while True` 的游戏主循环，让世界持续运转。
- 一个能响应 `/go`、`/look`（可显示物品）和 `/quit` 指令的 `if-elif-else` 解析器。

这节课，我们就是在这个坚实的地基上，添砖加瓦，描绘属于我们自己的多彩世界！

</div>
<div class="align-middle-center">

![乐高积木，简单的几块积木，拼搭出极其复杂的城堡或飞船 width:400px](../../../lectures/images/2025-10-30-10-08-08.png)

</div>
</div>

---

## **核心方法论：两阶段提示词实践法**

这节课，我们采用一种全新的训练方法，来体验AI辅助开发的两种不同模式。对于你选择的任何一个挑战，都需要分两步完成。

<div class="columns" style="font-size: 0.75em;">
<div>

### **第一阶段：“愿景驱动”** (先有)
1.  **目标**：快速验证想法，获得即时反馈。
2.  **方法**：用**纯自然语言**向AI描述你的**最终目的**。
    > **Prompt示例**：
    > 你好，我想让我的游戏能拾取物品，比如输入‘/take sword’，地上的剑就到我包里了。
3.  **产出**：一个能运行的脚本，但你可能不完全理解其内部逻辑。
4.  **关键后续**：拿到代码后，立刻追问AI：
    > 请一步步向我解释你刚刚生成的代码，特别是处理‘/take’指令的部分，它的逻辑是什么？

</div>
<div>

### **第二阶段：“设计驱动”** (再好)
1.  **目标**：掌握逻辑，精准控制，产出高质量代码。
2.  **方法**：**另起一个会话**，像架构师一样，给出**清晰、分步**的指令。
    > **Prompt示例**：
    > 请帮我实现`/take`指令：1. 为玩家创建名为`inventory`的空列表... 2. 检查指令是否为两部分... 3. 检查物品是否存在... 4. 写入到新的脚本...
3.  **产出**：一个你完全理解的、逻辑严谨的脚本。
4.  **核心价值**：通过这个过程，你将真正**驾驭**AI，而不仅仅是**使用**它。

</div>
</div>

---

## **挑战菜单：选择你的任务！**

<div style="font-size: 0.75em">

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

---

## **实践参考：`take`指令的两阶段实现**

如果你在实践中遇到困难，可以参考`take`指令的两阶段实现过程，它清晰地展示了两种Prompt风格的差异。

<div class="columns">
<div>

#### **第一阶段：“愿景驱动” Prompt**
> “我想在我的文本游戏中加入一个拾取物品的功能。比如，如果地上有‘一把生锈的剑’，我输入‘/take 一把生锈的剑’，这把剑就应该从地上消失，然后出现在我的背包里。如果地上没有这个东西，就告诉我‘这里没有这个东西’。”

**➡️ 目标：快速获得一个能用的原型。**

</div>
<div style="font-size: 0.7em;">

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

--- 

## **“我的江湖”作品发布会**

<div class="columns">
<div style="font-size: 0.85em;">

在大家实现自己的创意后，我们将举办一个“**我的江湖”作品发布会**。

我们将邀请几位同学，自愿上台（共享屏幕），向大家展示你用“两阶段法”完成的作品：

- 你选择了哪个挑战？最终实现了什么效果？
- 对比两个阶段的Prompt，你有什么不同的体验和感悟？
- **“愿景驱动”的Prompt**为你带来了什么便利或困惑？
- **“设计驱动”的Prompt**有什么优势和缺点？
- 这个过程，如何改变了你对“与AI协作”的看法？

**这将是你第一次，作为一名驾驭AI的架构师，分享你的思考与洞见！**

</div>
<div class="align-middle-center">

![一个开发者在台上兴奋地展示自己的游戏作品 width:400px](../../../lectures/images/2025-10-30-10-07-07.png)

</div>
</div>

---

## **头脑风暴：你的“自动化”时刻**

<div class="columns">
<div style="font-size: 0.8em;">

在你成功地为游戏世界注入“心跳”之后，你已经真正掌握了“自动化”的魔法。现在，让我们将这份能力照进现实。

**在你的教学或科研中，有没有哪一件让你感到烦恼的、需要手动重复的任务，是可以用我们学到的“循环”和“条件”来解决的？**

- 是不是需要**为全班**学生的作业（文件名），逐一检查是否符合“学号-姓名”的格式？
- 是不是需要**从大量的**文件存档，找出所有提到自己名字的文件？
- 是不是需要**对一个文件夹里**的所有图片，凡是大于10MB的，就把它移动到“高清图片”文件夹？

**把你的想法分享出来，它可能就是你的下一个AI应用！**

</div>
<div class="align-top-center" style="flex-direction: column;">

![一个人坐在书桌前，头脑中迸发出许多关于自动化的创意火花 width:400px](../../../lectures/images/2025-10-29-10-13-13.png)

<div class="tip" style="margin-top: 20px; font-size: 0.9em;">
<strong>点子示例</strong><br>
指挥AI写一个脚本，遍历一个文件夹里的所有文件名，如果文件名不包含“最终版”三个字，就把它移动到`待检查`文件夹。
</div>

</div>
</div>

---

## **Aha! 时刻：编程的秘密**

<div class="columns">
<div>

大家发现了吗？

我们这节课**没有学习任何新的语法**！

我们只是将已知的“三原色”——变量、条件、循环——以一种有意义的方式**组合**了起来。

这就是编程最深刻，也最美妙的秘密：

> **用有限的、简单的规则，去创造和应对无限复杂的世界。**

掌握了“组合”的技巧，你就掌握了编程的精髓。

</div>
<div class="align-middle-center">

![乐高积木，简单的几块积木，拼搭出极其复杂的城堡或飞船 width:400px](../../../lectures/images/2025-10-30-10-08-08.png)

</div>
</div>

---

## **模块二总结：从“魔法观众”到“世界架构师”**

<div class="columns">
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

![一条从山脚到山顶的成长路径图，沿途有变量、条件、循环、项目四个里程碑 width:400px](../../../lectures/images/2025-10-30-10-10-10.png)

</div>
</div>

---

## **新的“痛点”：臃肿的主循环**

<div class="columns">
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
<div class="align-top-center" style="flex-direction: column;">

![一个人面对着一团乱麻般的代码，显得很苦恼 width:400px](../../../lectures/images/2025-10-30-10-11-11.png)

<p style="margin-top: 1rem; font-size: 0.9em;">这就像一个<strong>杂乱无章的巨大抽屉</strong>，所有东西都堆在一起，找起来费劲，改起来也容易出错。</p>

</div>
</div>

---

## **下一步预告：模块三 - 代码复用与人机协作**

<div class="columns">
<div style="font-size: 0.9em;">

为了解决“功能代码”级别的重复和混乱问题，并进一步提升我们与AI的协作效率，在下一个模块，我们将学习：

- **函数 (Functions)**
  - 学会如何将一段代码“**打包**”成一个可以随时调用、重复使用的“**功能积木**”。

- **与AI结对调试 (Pair Debugging)**
  - 当我们的“积木”出现问题时，如何引导AI**自我检查**、**修复代码**，让你真正成为AI的“项目经理”。

**我们即将从“游戏设计师”，升级为更全能的“AI开发主管”！**

</div>
<div class="align-middle-center">

![一些代码块被打包成一个个独立的积木，然后被一只手轻松地取用和组合 width:400px](../../../lectures/images/2025-10-30-10-12-12.png)

</div>
</div>
