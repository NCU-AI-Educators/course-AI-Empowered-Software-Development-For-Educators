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

![bg blur:3px brightness:60%](../../../lectures/images/2025-10-27-10-51-00.png)

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
## **第5节课：变量与蓝图——绘制你的第一幅江湖地图**

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

---

## **回顾与展望：从“产品总监”到“首席架构师”**

在模块一，我们扮演了“**产品总监**”的角色，仅仅通过描述我们的愿景（**问题域**），我们的AI“开发团队”就为我们交付了一个可以反复使用的、功能完整的“随机点名器”应用。

**但我们必须认识到我们的能力存在不足：**
AI交付给我们的是一个神奇的“**黑箱**”。我们知道它能用，但我们并不知道它**如何**工作。
- 我们无法**评估**它内部的实现质量是高是低。
- 当它出现微妙的Bug时，我们无法**精准地**指导AI去修复。
- 我们无法**举一反三**，将它的核心原理应用到下一个完全不同的项目中。

为了真正地**驾驭AI**，我们必须完成一次关键的角色切换：从“产品总监”，化身为能读懂“设计蓝图”的“**首席架构师**”。我们必须深入到**求解域**——程序——的内部，去理解其运作的规则与机制。

---

## **模块二目标：掌握构建复杂世界的“三原色”**

在本模块，我们将以“**构建一个迷你武侠世界**”为主线任务，学习“指挥AI的三大核心指令”：
1.  **变量 & 数据结构**: 学习如何用结构化的方式，描绘出世界的“**地图与状态**”。
2.  **条件 (Conditions)**: 学习如何定义游戏规则，让世界充满“**选择与奇遇**”。
3.  **循环 (Loops)**: 学习如何构建游戏引擎，成为驱动世界运转的“**心跳**”。

---

## **本节课目标：绘制你的第一幅江湖地图**

本节课，我们将从零开始，像一位真正的“世界架构师”一样，构筑我们“文本武侠MUD”的雏形。你将：

1.  **学习**：如何使用最核心的编程工具——**变量**和**字典**——来描述一个想象中的世界。
2.  **产出**：为你自己的“武侠MUD”项目，创造出第一版的“**世界地图**”代码。

---

## **最原始的办法：用`print`“写小说”**

在学习任何编程概念前，让我们先用最原始的办法——`print()`函数，像写小说一样来描述我们的世界。

```python
# 目标：描述玩家在“扬州广场”的所见所闻
print("你来到了一个叫做“扬州广场”的地方。")
print("你环顾四周，发现这里人来人往，非常热闹。东边是一家茶馆，西边是一家兵器铺。")

# 接着，我们想描述玩家移动到了“茶馆”
print("你来到了一个叫做“茶馆”的地方。")
print("你走了进去，发现里面坐满了茶客，一位说书人正在讲着三国的故事。")
```

**思考：这种“写小说”式代码，会带来什么问题？**

<div class="tip" style="font-size: 0.8em; margin-top: 1rem;">
  <strong>小贴士 (Pro Tip):</strong><br>
  我们练习时可以新建一个文件，复制这段代码进去，保存为 <code>.py</code> 文件并让AI帮我们运行它。<br>
  现在，请先跟随我们的思路，理解这段代码的“好”与“坏”。
</div>

---

## **“写小说”式代码的“痛点”**

<div class="columns ratio-6-4">
<div>

刚才的代码暴露了两个核心痛点：

1.  **维护的噩梦**
    - 如果“扬州广场”这个名字要改成“中央广场”，你需要修改多少处代码？
    - 如果游戏有100个地点，这将是一场灾难。

2.  **无法“指代”**
    - 我们没有办法在程序的其他地方，通过一个简单的名字来“指代”‘扬州广场’这个地点。
    - 我们只能一遍遍地重复它的名字，代码之间毫无关联。

</div>

<div class="align-middle-center">

![一个程序员面对一团乱麻的代码，显得很苦恼 width:400px](../../../lectures/images/2025-11-01-17-00-00.png)

</div>
</div>

--- 

## **编程的进化：为数据“命名”**

为了解决“指代不明”的危机，程序员发明了编程中第一个，也是最重要的概念：**变量 (Variable)**。

<div class="columns" style="margin-top: 2rem;">
<div>

### 变量，就是给数据贴上一个有意义的“标签”或“名字”。

它就像一个贴了标签的“**数据盒**”，我们可以把数据（比如`"扬州广场"`）放进去，之后就可以通过这个“名字”（比如`location_name`）来指代盒里的数据。

</div>
<div class="align-middle-center">

![一个数据盒，上面贴着标签“location_name”，盒子里面装着文本“扬州广场” width:450px](../../../lectures/images/2025-11-01-16-01-01.png)

</div>
</div>

---

## **变量的威力：数据与逻辑分离**

<div class="columns ratio-6-4">
<div>

**进化版代码：**
```python
# 我们为“扬州广场”这个数据，起了个名字叫 location_name
location_name = "扬州广场"

# 描述文本现在也通过拼接变量来生成，而不是写死
location_description = "你正站在" + location_name + "，这里人来人往..."

# 我们可以多次使用这个“名字”
print("欢迎来到 " + location_name)
print(location_description)

# 如果现在需要改名，只需要修改一处！
location_name = "中央广场"
print("地点已更名为: " + location_name)
```

</div>

<div>

### 革命性飞跃：

通过“命名”，我们成功地将 **易变的“数据”** 和 **不变的“逻辑”** 分离开。

现在，代码变得清晰、可读，且易于维护。

</div>

</div>
<div class="tip">

**小贴士 (Pro Tip):**
你可能注意到了代码中的 `+` 号。当它被用在文本（我们称之为“字符串”）之间时，它的作用就像“胶水”，会把几段文本**拼接**成一个更长的文本。
</div>

---
## **动手环节(1/3)：实践“数据与逻辑分离”**

现在，你已经理解了“变量”的威力。让我们亲手实践刚刚学到的“数据与逻辑分离”思想。

**任务**：指挥AI，使用一个变量来动态构建另一个变量。

**向你的 `qwen` 助手发出以下指令：**

> `请写一段Python脚本，来实践“数据与逻辑分离”思想：
> 1. 创建一个名为 location_name 的变量，并赋值为文本 “扬州广场”。
> 2. 创建第二个变量 location_description，**它的值必须通过拼接第一个变量 location_name 和一段描述性文字（例如“，这里人来人往...”）来动态生成**。
> 3. 最后，使用 print() 函数，将 location_description 的内容打印出来，以验证我们的成果。`

运行脚本，并观察结果！我们不仅为数据命了名，更重要的是，我们用一个变量（名字）去动态地构建了另一个变量（描述）。这就是“数据与逻辑分离”的第一次胜利！

---

## **架构师的思考：我们为何这样提问？**

<div class="columns">
<div>

你可能会想：为什么刚才的提示词要写得那么像“代码”？

这正是本阶段训练的核心！我们刻意地用“编程思维”来写提示词，目的不是为了迁就AI，而是为了**训练我们自己的大脑**，学会将一个模糊的目标，拆解成清晰、无歧义的逻辑步骤。

这是**驾驭AI**的必经之路。当我们熟练掌握了这种结构化思维后，我们就能用更宏观、更具设计感的语言来描述我们的愿景，而AI将能更好地领会并实现这些技术细节。

</div>
<div class="align-middle-center">

![一个大脑中包含着清晰的逻辑齿轮的图片 width:400px](../../../lectures/images/2025-11-01-17-01-01.png)

</div>
</div>

---

## **成功的喜悦与新的挑战**

我们成功了！使用变量，我们可以清晰地描述一个地点。但，如果想让世界更丰富，增加第二个地点“茶馆”呢？

我们就必须继续定义一堆散乱的变量：

```python
# 第一个地点
loc1_name = "扬州广场"
loc1_desc = "你正站在扬州城的中央广场..."

# 第二个地点
loc2_name = "茶馆"
loc2_desc = "你走进了一家茶馆，茶香四溢。"

# ... 如果有100个地点？
```

**思考：这种做法，会带来什么新的“危机”呢？**

---

## **隐藏的危机：散乱的变量**

<div class="columns ratio-6-4">
<div>

刚才的做法暴露了两个核心危机：

1.  **关系混乱**
    - 程序并不知道 `loc1_name` 和 `loc1_desc` 都属于“扬州广场”这个**实体**。它们只是两张散乱的笔记，毫无关联。

2.  **扩展噩梦**
    - 每增加一个地点，就需要新定义一堆变量。当世界变得庞大时，这将是一场灾难，代码会变得难以维护。

</div>
<div class="align-middle-center">

![两组分离的、代表变量的方框，一组是loc1_name和loc1_desc，另一组是loc2_name和loc2_desc，它们之间没有连接，显得很混乱 width:450px](../../../lectures/images/2025-11-01-17-02-02.png)

</div>
</div>

---

## **升级思维：从“变量”到“模型”**

刚才的“危机”告诉我们，当世界变得复杂时，用一堆散乱的变量来描述是行不通的。我们需要再次升级思维，从“**定义变量**”，升级到“**构建模型**”。

<div class="columns" style="margin-top: 15px; gap: 2.5rem;">
  <div style="text-align: center;">
    <p style="font-size: 2.5em; margin-bottom: 0;">🧱</p>
    <h3 style="margin-top: 0.5rem; margin-bottom: 0.5rem;">第一步：提取实体 (Entity)</h3>
    <p style="font-size: 0.9em;">你的世界里有哪些独立、重要的“<strong>事物</strong>”？</p>
    <p style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; font-size: 0.9em;">地点、玩家、NPC</p>
  </div>
  <div style="text-align: center;">
    <p style="font-size: 2.5em; margin-bottom: 0;">🏷️</p>
    <h3 style="margin-top: 0.5rem; margin-bottom: 0.5rem;">第二步：归纳属性 (Attribute)</h3>
    <p style="font-size: 0.9em;">每个“实体”有哪些关键的“<strong>特征</strong>”？</p>
    <p style="background-color: #f5f5f5; padding: 10px; border-radius: 5px; font-size: 0.9em;">名称、描述、出口</p>
  </div>
</div>

<div class="insight">

  💡 **核心洞察**：我们刚才的痛点，本质上就是没有一种好的方式，能把“地点”这个实体的所有“属性”**打包**在一起！
</div>

---

## **架构师的方案：用“字典”为实体建模**

为了解决这个“打包”难题，程序员发明了一种完美的数据结构：**字典 (Dictionary)**。

它就像一个贴了“**标签**”的储物柜，允许我们将一个“实体”的所有“属性”都打包在一起。

<div class="columns">
<div>

**进化版方案：**
```python
# 用一个“字典”，为“扬州广场”这个实体建模
# “标签”就是属性名，“值”就是属性内容
guangchang = {
    "name": "扬州广场",
    "description": "你正站在扬州城的中央广场...",
    "exits": {"east": "chaguan"}
}

# 现在，一个变量就代表一个完整的实体！
# 我们可以清晰地获取它的任何属性
print(guangchang["description"])
```

</div>
<div>

![一个储物柜，上面贴着“扬州广场”的标签，每个抽屉上分别贴着“名称”、“描述”、“出口”的标签 width:500px](../../../lectures/images/2025-11-01-15-03-03.png)

</div>
</div>

<div class="insight" style="margin-top: 0px;">

💡**核心洞察**：字典的“**键-值对**”结构，是实现“**实体-属性**”建模的关键。它将程序从“一堆散乱的笔记”升级为了“**一张张结构清晰的实体蓝图**”。
</div>


---

## **变量的本质：为“现实世界”创建“数字分身”**

我们刚才做的，就是把现实世界中的“事物”和它们的“属性”，在程序世界里用**变量**这个工具“建模”出来。

每一个变量，都是现实世界某个事物或属性的一个“**数字分身 (Digital Avatar)**”。

<div class="columns" style="margin-top: 1rem; font-size: 0.9em;">
<div style="border-right: 2px solid #eee; padding-right: 1.5rem;">

**现实世界 (你的游戏设定)**
- **实体**: 地点, 玩家, 物品
- **属性**: 
  - 描述, 出口
  - **当前位置**, 背包
  - 名称, 攻击力

</div>
<div>

**程序世界 (代码)**
```python
# 为现实世界中的“属性”创建分身
location_description = "..."
player_location = "guangchang"
sword_attack = 10
```

</div>
</div>

<div class='insight' style="margin-top: 1rem;font-size: 0.85em;">

💡**核心洞察**：`player_location` 这个变量，并不是`"guangchang"`这个文本本身，而是“玩家当前位置”这个 **属性** 在程序里的“分身”。这个分身可以随时被赋予不同的值（比如移动到`'chaguan'`）。
</div>

---

## **世界蓝图：玩家与数据类型**

我们的世界地图有了，但还需要一个主角！现在，让我们为玩家创建一个“**角色卡**”（`player`字典），并在其中认识一下构建世界所必需的几种“**数据原料**”。

<div style="margin-top: 1rem;font-size: 0.8em;">

```python
player = {
    "name": "令狐冲",
    "level": 1,
    "health": 100,
    "inventory": ["新手布衣", "一把生锈的剑"],
    "current_location": "guangchang"
}
```
</div>

<div class="columns" style="grid-template-columns: 1fr 1fr 1fr 1fr; gap: 0.5rem; margin-top: 1rem; font-size: 0.7em; text-align: center;">
  <div style="background-color: #f8f9fa; padding: 0.8em; border-radius: 5px;">
    <h4>📝 文本 (String)</h4>
    <hr>
    <p style="text-align: left;"><strong>用途</strong>: 描述文字信息。<br><strong>写法</strong>: 用引号包裹。<br><strong>示例</strong>: <code>"令狐冲"</code></p>
  </div>
  <div style="background-color: #f8f9fa; padding: 0.8em; border-radius: 5px;">
    <h4>🔢 数字 (Number)</h4>
    <hr>
    <p style="text-align: left;"><strong>用途</strong>: 表示可计算的数值。<br><strong>写法</strong>: 直接写。<br><strong>示例</strong>: <code>1</code>, <code>100</code></p>
  </div>
  <div style="background-color: #f8f9fa; padding: 0.8em; border-radius: 5px;">
    <h4>📜 列表 (List)</h4>
    <hr>
    <p style="text-align: left;"><strong>用途</strong>: 有序存放多个物品。<br><strong>写法</strong>: 用<code>[]</code>包裹。<br><strong>示例</strong>: <code>["..."]</code></p>
  </div>
  <div style="background-color: #f8f9fa; padding: 0.8em; border-radius: 5px;">
    <h4>🗄️ 字典 (Dictionary)</h4>
    <hr>
    <p style="text-align: left;"><strong>用途</strong>: 打包实体的所有属性。<br><strong>写法</strong>: 用<code>{}</code>包裹。<br><strong>示例</strong>: 整个 <code>player</code></p>
  </div>
</div>

---

## **类型为何重要？`100 + 50` 与 `"100" + "50"`**

为什么要严格区分“物品”的类型？因为对于**完全相同**的操作符（比如 `+`），不同类型的“物品”会有**完全不同**的反应。

<div class="columns">
<div style="font-size: 0.8em; ">

### 🔢 当 `+` 遇到 **数字**
它执行的是“**数学加法**”。
```python
# 玩家喝了一瓶治疗药水
player_health = 100
potion_effect = 50

# 结果是 150 (玩家成功回血)
player_health = player_health + potion_effect
```
<div style="text-align: center; font-size: 0.8em; margin-top: 20px;">
  <span style="border: 2px solid #ccc; padding: 10px; border-radius: 5px;">100</span>
  <span style="margin: 0 15px;">+</span>
  <span style="border: 2px solid #ccc; padding: 10px; border-radius: 5px;">50</span>
  <span style="margin: 0 15px;">=</span>
  <span style="border: 2px solid #4CAF50; padding: 10px; border-radius: 5px; color: #4CAF50; font-weight: bold;">150</span>
</div>

</div>
<div style="font-size: 0.8em; ">

### 📝 当 `+` 遇到 **文本**
它执行的是“**文本拼接**”。
```python
# 系统想显示玩家的等级
level_text = "等级: "
player_level = "1" # 注意，这里的1是文本

# 结果是 "等级: 1"
level_display = level_text + player_level
```
<div style="text-align: center; font-size: 0.8em; margin-top: 20px;">
  <span style="border: 2px solid #ccc; padding: 10px; border-radius: 5px;">"等级: "</span>
  <span style="margin: 0 15px;">+</span>
  <span style="border: 2px solid #ccc; padding: 10px; border-radius: 5px;">"1"</span>
  <span style="margin: 0 15px;">=</span>
  <span style="border: 2px solid #1e90ff; padding: 10px; border-radius: 5px; color: #1e90ff; font-weight: bold;">"等级: 1"</span>
</div>

</div>
</div>

<div class ="key-point" style="font-size: 1em; margin-top: 20px;">

  ⚠️ **核心要点**：搞混数据类型，可能会让你的程序做出完全不符合预期的事（比如想加血，结果却把`100`和`50`拼成了字符串`"10050"`！）。
</div>

---

## **变量的动态性：记录玩家移动的“足迹”**

变量不仅能在开始时“装入”数据，还能在程序运行中，不断地用新结果“**覆盖**”旧结果，以此来“**记录和更新**”游戏世界的状态。

它就像一个动态的“**地图标记**”，时刻记录着玩家的足迹。

<div class="columns" style="margin-top: 1.5rem;">
<div>

**案例：玩家在世界中移动**
```python
# 玩家的初始位置
player_location = "guangchang"
print(f"你来到了【{player_location}】")

# 玩家决定向东走...
# (在下一课，我们将学习如何根据玩家指令来触发这个改变)
new_location = "chaguan"

# 玩家的位置变化了！“地图标记”被新结果“覆盖”
player_location = new_location
print(f"你移动到了【{player_location}】")
```

</div>
<div class="align-middle-center">
<div class="insight" style="font-size: 0.8em;">

💡 **核心洞察**

`player_location` 这个变量，并不是`"guangchang"`这个文本本身，而是“玩家当前位置”这个**属性**在程序里的“分身”。

这个分身可以随时被赋予不同的值（比如移动到`'chaguan'`），这种可以被 **重复赋值（覆盖）** 的能力，是实现所有动态交互的基石。

</div>
</div>
</div>

---

## **变量的艺术：如何起一个好名字？**

为变量起一个好名字，是写出清晰代码的关键。一个好的名字能让代码不言自明。

**核心原则：**
- **清晰、准确、有意义**。用 `player_health` 代替 `ph` 或 `shuju1`。
- **使用小写字母和下划线**。这是Python的推荐风格，例如 `player_location`。

AI助理通常是这方面的专家，因为它学习了海量优秀代码。我们的目标是能读懂并写出同样清晰的命名，以便与AI高效协作。

---

## **你的新角色：AI助理的“世界架构师”**

让我们用一个更贴切的比喻，来理解**你、AI、电脑**三者的关系：

<div class="columns" style="grid-template-columns: 1fr 1fr 1fr; text-align: center; gap: 2rem;">
  <div style="border: 2px solid #ccc; border-radius: 10px; padding: 0em;">
    <p style="font-size: 3em;">🧑‍🎨</p>
    <h3>你 (世界架构师)</h3>
    <p>提出核心创意与世界观</p>
  </div>
  <div style="border: 2px solid #ccc; border-radius: 10px; padding: 0em;">
    <p style="font-size: 3em;">🤖</p>
    <h3>AI (全能程序员)</h3>
    <p>理解你的“设计蓝图”并生成代码</p>
  </div>
  <div style="border: 2px solid #ccc; border-radius: 10px; padding: 0em;">
    <p style="font-size: 3em;">💻</p>
    <h3>电脑 (忠实执行者)</h3>
    <p>严格按照生成的代码呈现世界</p>
  </div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 20px;font-size: 0.9em;">
  <div style="background-color: #ffebe6; border-left: 5px solid #ff5722; padding: 15px;">
    <p><strong>核心问题</strong>：AI没玩过你的游戏，它完全依赖你的口头描述。如果它误解了你的意图，<strong>它生成的代码就是错的！</strong></p>
  </div>
  <div style="background-color: #e6f4ea; border-left: 5px solid #4CAF50; padding: 15px;">
    <p><strong>你的核心价值</strong>：作为唯一的“世界架构师”，在“运行”前审查AI生成的 <strong>代码</strong>  ，凭借你的领域知识发现并修正AI的错误。</p>
  </div>
</div>



---

## **动手环节(2/3)：指挥并“面试”你的AI助理**

<div class="columns">
<div>

现在，让我们带着“世界架构师”和“面试官”的视角，来完成本节课的实践。

**你的任务：**
指挥AI为你绘制“武侠MUD”的第一版世界地图，并准备“面试”它，让它解释自己的设计。

**(小提示：你可以让AI把地点换成你喜欢的任何武侠场景，比如“光明顶”、“武当山”！)**

</div>
<div>

**第一步：下达“世界蓝图”指令**
<div style="background-color: #f5f5f5; border-radius: 5px; padding: 1em; font-size: 0.65em;">

> `作为一名世界架构师，请为我的文本武侠游戏设计Python脚本的“世界地图”部分。要求如下：
> 1. 创建一个名为 world 的字典变量，作为整个世界的容器。
> 2. 在 world 字典中，请设计至少3个地点，每个地点都作为 world 的一个子字典。请用有意义的英文ID作为键（例如 'square', 'teahouse', 'weapon_shop'）。
> 3. 每个地点字典内，必须包含 'description'（一段生动的武侠风格描述）和 'exits'（一个指向其他地点ID的出口字典）这两个键。
> 4. 创建一个名为 player_location 的字符串变量，并将其初始值设置为你的出生点（例如 'square'）。
> 5. 最后，请根据 player_location 变量的值，从 world 字典中获取玩家所在地的描述，并打印出来，作为游戏的开场白。`

</div>

</div>
</div>

--- 

## **动手环节(3/3)：开启“代码评审会”**

<div class="columns">
<div>

**第二步：审查并“面试”AI**

AI生成代码后，不要只看结果。请带着“架构师”的视角，向它追问。

<div class="tip">

  <strong>小贴士 (Pro Tip):</strong>
你可能会想：“我没有编程经验，如何评审代码？”—— 这正是AI辅助学习的魅力所在！我们无需预先成为专家。**我们可以让AI向我们解释它生成的**代码 **，并讲解任何我们不理解的技术细节。** 这能极速提升我们对代码的评审能力。

</div>
</div>
<div>

**现在，让我们来“面试”它：**
<div style="background-color: #f5f5f5; border-radius: 5px; padding: 1em; font-size: 0.85em;">

> `很好，现在请向我汇报你的设计思路：
> 1. 为什么你选择用一个“字典的字典”结构来表示我的世界？这样做有什么好处？
> 2. 'exits' 字典的设计，对于我们未来实现“go”指令有什么帮助？
> 3. player_location 这个变量，和 world 字典之间，是如何配合工作的？`

</div>
</div>

---

## **知识升华：编程思想的第一次实践**

祝贺你！今天，我们不仅学会了使用变量，更重要的是，我们亲身实践了“**用程序去建模一个真实世界**”的核心编程思想。

**编程的本质是：**
1.  首先针对现实世界的问题，通过建立问题域的**抽象模型**（我们今天做的`world`和`player`字典是核心内容之一），从而准确**定义问题**。（我们可以和AI一起分析讨论后确定）
2.  之后**设计算法**对问题进行求解（通常可以由AI帮我们完成，但初学时可以和AI讨论算法的设计）。
3.  接着将算法映射为程序语言编写的**代码** （通常可以由AI帮我们完成）。
4.  最终利用程序的**自动化处理能力**，解决问题。

你今天绘制的“世界蓝图”，就是这所有伟大创造的第一步！

---

## **本节总结：我们获得了什么？**

<div class="columns">
<div>

### ✅ 我们获得的能力

#### 🗺️ 映射与建模
我们学会了如何将现实事物（地点、出口）映射为程序中的变量和字典，为世界建立了“数字分身”。


#### 📺 展示与输出
我们学会了使用`print`函数，将模型中的细节（如地点描述）和状态变化（如玩家位置）展示出来。

</div>
<div class="align-middle-center">

![一个装满金币和技能图标的宝箱 width:400px](../../../lectures/images/2025-11-01-18-00-00.png)

</div>
</div>

---

## **新的“痛点”：一个“不变”的世界**

<div class="columns">
<div>

我们深刻地认识到，这种“固定剧本”式的程序，就像一本只能从头读到尾的小说。

- **情节是固定不变的**：程序一旦开始运行，就只能沿着唯一的路径走到终点。
- **无法响应变化**：它不能根据任何新情况（如玩家的指令）产生分支或改变。

这种**单向、不可变的执行流程**，是它无法成为真正“游戏”的根本原因。

</div>
<div class="align-middle-center">

![一个机器人只能沿着一条直线路径行走，无法拐弯 width:400px](../../../lectures/images/2025-11-01-18-01-01.png)

</div>
</div>

---

## **下一步预告：从“单行道”到“交互路口”**

<div class="columns">
<div>

我们今天的脚本，是一条**单行道**。程序一旦启动，就只能沿着预设好的唯一路径，从头走到尾，终点永远不变。

它没有路口，不会拐弯，更不懂得选择。一个只会走直线的程序，无法应对现实世界中无处不在的“十字路口”。

**如何让程序学会“选择”？**
我们如何赋予它在十字路口“左顾右盼”并做出**判断**的能力，从而走向不同的未来？

为了赋予程序**决策的智慧**，下一节课，我们将学习编程三大核心中的第二个——**条件判断**！

</div>
<div>

![width:400px](../../../lectures/images/2025-10-26-23-02-43.png)

</div>
</div>