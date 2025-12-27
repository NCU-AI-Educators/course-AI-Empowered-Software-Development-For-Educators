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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-13-18-53-14.png)

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
## 第6节课：赋予世界规则——指令解析与条件判断

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场：承前启后，引入新主题
本页作为第6节课的开篇，核心目标是快速回顾上一节课的成果和局限，并清晰地引出本节课的核心主题——“规则”与“判断”。

**核心要点**：
1.  **回顾与衔接**: 用“静态蓝图”和“固定剧本”来回顾上一节课的成果与痛点，自然地引出本节课的学习动机——让世界“活”起来。
2.  **引入核心概念**: “规则”、“判断”、“选择”，这些关键词清晰地预告了本节课将要学习的核心内容——条件判断。
3.  **设定目标**: “让程序听懂我们的指令”是一个非常具体且有吸引力的目标，能迅速抓住学员的注意力。

</div>

---

## **回顾：一个“固定剧本”的世界**

<div class="columns ratio-6-4">
<div style="font-size: 0.85em;">

在上一节课，我们取得了巨大的进步！

我们成功地用“字典”绘制了一幅宏大的“世界蓝图”，并让玩家“降生”在了世界上。

但是，我们的程序就像一个“**固定剧本**”。
- **情节是固定不变的**：程序从第一行开始，沿着唯一的路径执行到最后一行，然后就结束了。
- **无法响应玩家**：它不能暂停下来等待我们的指令，更不能根据我们的想法产生任何分支或改变。

这种**单向、不可交互的执行流程**，是它无法成为真正“游戏”的根本原因。

**我们如何让程序“暂停”下来，聆听我们的指令，并据此走向不同的未来呢？**

</div>
<div>

![一个机器人只能沿着一条直线路径行走，无法拐弯 width:400px](../../../lectures/images/2025-11-14-00-07-39.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 强化痛点，建立学习动机
本页完全复用了上一节课结尾的“痛点”幻灯片，其目的是在本节课的一开始，就立刻重新聚焦于问题，强化上一节课留下的“认知不满足感”，从而为本节课的新知识建立最强大、最直接的学习动机。

**核心要点**：
1.  **重复与强调**: 通过重复，将“固定剧本”、“单向、不可交互”这个核心痛点深深植入学员的认知。
2.  **聚焦问题**: 在引入任何解决方案之前，先让学员再次清晰地认识到当前程序最致命的缺陷。
3.  **提出引导性问题**: “我们如何让程序‘暂停’下来...”这个问题，直接指向了本节课需要解决的两个关键技术点：获取用户输入 (`input`) 和根据输入做判断 (`if-else`)。

</div>

---

## **本节课目标：指挥AI构建“规则”与“选择”**

为了让世界“活”起来，我们必须为它建立“**规则**”，让它能根据情况做出“**选择**”。

本节课，我们将学习“指挥AI的三大核心指令”中的第二个：

### **条件判断 (If-Else)**
- **作用**：在程序中建立“**决策点**”，赋予程序“**选择**”的能力。
- **你的新能力**：
  1. **定义“规则”**：学会用“如果玩家输入的是`/go`指令，就...”的结构，向AI清晰地描述游戏规则。
  2. **审查“逻辑”**：审查AI代码中的“决策逻辑”是否符合你的游戏设计。

**最终，你将能指挥AI，为你的武侠世界创造出第一个“指令解析器”！**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 清晰化本节课的学习目标与产出
本页的核心目标是清晰地告诉学员“我们这节课要学什么”以及“学完能做什么”。

**核心要点**：
1.  **呼应模块框架**: “指挥AI的三大核心指令中的第二个”这句话，将本节课内容置于整个模块的宏大框架之下，让学员有清晰的全局感。
2.  **明确核心概念**: 明确指出本节课的核心是“条件判断 (If-Else)”。
3.  **能力化目标**: 将学习目标描述为两项可习得的“新能力”（定义规则、审查逻辑），而不是干巴巴的知识点。这更能激发学员的学习热情。
4.  **具象化产出**: “指令解析器”是一个非常具体、可检查的产出物。它让学员从一开始就知道本节课的最终目标是什么，有助于他们集中注意力。

</div>

---

## **情景带入：我们身边的“游戏规则”**

其实，“如果...就...”的决策规则，早已贯穿我们玩过的所有游戏中。

- **角色扮演游戏**
  - **如果** `玩家选择的职业是“法师”`，**就** `初始智力+10`。
  - **如果** `玩家的等级低于10级`，**就** `无法进入“高级地下城”`。

- **策略游戏**
  - **如果** `我方单位是“骑兵”且攻击目标是“弓箭手”`，**就** `伤害加成50%`。
  - **如果** `地图上的资源“木材”少于100`，**就** `高亮显示所有树木`。

这些游戏规则，正是我们为“游戏世界”这个**问题**所建立的**抽象规则**。编程的核心，就是将我们为现实世界中各类问题所建立的规则，用代码精确地实现出来。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 从生活经验出发，建立直观理解
本页的目标是在引入任何技术概念之前，通过学员熟悉的游戏场景，为“条件判断”这个抽象概念建立一个直观、感性的认识。

**核心要点**：
1.  **关联已有经验**: 从学员大概率玩过的游戏类型（RPG、策略游戏）入手，能迅速引发共鸣。
2.  **具体化案例**: 提供了四个非常具体、易于理解的游戏规则案例，将抽象的`If-Then`逻辑与生动的游戏体验联系起来。
3.  **理论升华**: 在案例之后，及时进行总结，将“游戏规则”提升到“为问题建立抽象规则”的高度，并点明“编程的核心是实现规则”，赋予了编程这项活动更深刻的意义。

</div>

---

## **概念拆解：程序的“判断题”**

计算机是如何做出“判断”的呢？在执行 `if` 语句前，它会先求解一个答案只有 **“真” (True)** 或 **“假” (False)** 的“判断题”。

<div class="columns" style="font-size: 0.9em;">
<div>

**例1：判断玩家指令 (文本比较)**
`command == "/quit"`
这句代码是在**提问**：
> “变量 `command` 里的文本，**是不是等于** `"/quit"` 这个词？”

- 若 `command` 是 `"/quit"`，答案为 **`True`**。
- 若 `command` 是 `"/look"`，答案为 **`False`**。

</div>
<div>

**例2：判断玩家等级 (数值比较)**
`player_level >= 10`
这句代码也是在**提问**：
> “变量 `player_level` 里的数字，**是不是大于或等于** `10`？”

- 若 `player_level` 是 `15`，答案为 **`True`**。
- 若 `player_level` 是 `5`，答案为 **`False`**。

</div>
</div>

<div class='insight' style="margin-top: 1rem;font-size: 0.6em;">

💡 **核心定义**：`==`(等于)、`!=`(不等于)、`>`(大于)、`<`(小于)、`>=`(大于等于) 这些符号，是程序用来进行“是/非”判断的工具，它们统称为“**比较运算符**”。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 拆解核心概念：条件表达式
本页的核心目标是将`if`语句的“条件”部分拆解出来，让学员理解其本质是一个结果为“真”或“假”的表达式。

**核心要点**：
1.  **“判断题”比喻**: 这个比喻非常生动，它将一个技术概念（条件表达式）转化为一个学生非常熟悉的生活概念，极大地降低了理解门槛。
2.  **区分比较与赋值**: 明确强调`==`（比较）和`=`（赋值）的区别，这是初学者最容易犯错的地方之一，需要反复强调。
3.  **覆盖两种核心场景**: 案例覆盖了最常见的两种比较：字符串比较（判断指令）和数字比较（判断等级），具有代表性。
4.  **引入术语**: 在学员理解了概念后，在`insight`框中及时引入“比较运算符”这个正式术语，帮助学员建立专业词汇。

</div>

---

## **核心概念1：布尔值——只有“真”或“假”的世界**

在Python中，`True` 和 `False` 这两个特殊的“答案”，是一种全新的数据类型，叫做“**布尔值 (Boolean)**”。

布尔值是程序世界的逻辑基石，它代表了所有“判断题”的最终结果。

你可以亲自在命令行中运行 `python` 后，将以下代码复制到Python的`>>>`提示符后按回车验证一下：

<div class="columns">
<div>

**代码示例**
```python
# 我们可以直接打印出一个“判断题”的答案
command = "/quit"

print("指令是不是'/quit'?", command == "/quit")

print("指令是不是'/look'?", command == "/look")

print("玩家等级是不是大于10?", 15 > 10)
```

</div>
<div>

**输出结果**
```text
指令是不是'/quit'? True
指令是不是'/look'? False
玩家等级是不是大于10? True
```

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 正式引入“布尔值”
本页的目标是正式地、清晰地引入“布尔值”这一核心数据类型。

**核心要点**：
1.  **正式定义**: 明确指出`True`和`False`是一种名为“布尔值 (Boolean)”的新数据类型。
2.  **强调其重要性**: 用“逻辑基石”来形容布尔值的重要性。
3.  **提供即时反馈的实践**: “在Python交互环境中验证”是一种极佳的实践方式。它非常轻量，不需要创建文件，学员可以立刻看到代码`15 > 10`的计算结果就是`True`，这种即时反馈能极大地巩固他们对概念的理解。

</div>

---

## **核心概念2：布尔的本质——逻辑开关**

“真”与“假”是抽象的逻辑概念。在程序中，它们就像一个最简单的“**逻辑开关**”。

一个开关，只有“**开**”和“**关**”两种状态，绝不可能存在第三种。

- **`True`** 就等同于“**开**”：条件满足，执行这条路。
- **`False`** 就等同于“**关**”：条件不满足，不走这条路，去别处看看。

<div class="align-middle-center">

![一个清晰的拨动式电灯开关，左边是关，右边是开 width:300px](../../../lectures/images/2025-11-13-18-58-04.png)

</div>

我们写的 `if score >= 60:`，本质上就是在检查“及格”这个逻辑开关是否被打开。理解了这一点，`if`语句就变得非常简单。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 建立强大的心智模型
本页的核心目标是为学员建立一个关于“布尔值”和“条件判断”的、强大而简单的心智模型 (Mental Model)。

**核心要点**：
1.  **核心比喻**: “逻辑开关”是一个极佳的比喻。它简单、直观、人人都能理解，并且能非常准确地映射`if`语句的行为（二选一，路径选择）。
2.  **强化二元性**: “绝不可能存在第三种”这句话，强化了布尔逻辑的二元性，帮助学员建立非黑即白的程序思维。
3.  **连接概念与语法**: 最后一句“我们写的 `if score >= 60:`...”将抽象的“逻辑开关”比喻与具体的代码语法连接了起来，让学员能立刻应用这个心智模型去理解代码。

</div>

---

## **核心语法1：用 `If-Else` 搭建第一个“T字路口”**

理解了布尔值和开关，`If-Else` 的工作原理就变得非常简单：**它就是在检查一个“开关”是开着还是关着。** 请将代码复制到Python的>>>提示符后运行，理解一下程序逻辑：

<div class="columns">
<div class="styled-div" style="font-size:0.8em">

**设计逻辑**

> **如果** `玩家输入的指令` 是 `"/quit"`，
> **就** `退出游戏`；
> **否则**，
> **就** `继续游戏`。

**程序中的逻辑**
```python
command = "/go east"

# 计算机算出 command == "/quit" 是 False (开关是关的)
if command == "/quit": 
    # 因为开关是关的，所以这部分代码被跳过
    print("你退出了江湖...")
else: 
    # 程序走到这里，执行这个代码块
    print("游戏继续...")
```

</div>
<div class="align-middle-center" style="flex-direction: column;">

![width:240px](../../../lectures/images/2025-11-13-20-20-13.png)
**决策的可视化流程图**

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 讲解基础的If-Else语法
本页的目标是清晰地讲解最基础的`if-else`二元选择结构。

**核心要点**：
1.  **应用心智模型**: 开头第一句话就立刻应用了上一页建立的“逻辑开关”心智模型来解释`if-else`，加强了知识的连贯性。
2.  **三位一体的解释**: 通过“设计逻辑（伪代码）”、“程序逻辑（真实代码+注释）”和“可视化流程图”这三种方式，从不同维度解释同一个概念，确保所有学员都能理解。
3.  **强调缩进**: Python中的缩进是语法的一部分，非常重要。代码示例中清晰的缩进，以及注释中“缩进的代码块”的说法，都在潜移默化地强调这一点。

</div>

---

## **核心语法2：用 `elif` 搭建“立交桥”**

如果我们的指令不止两种呢？比如，我们需要处理 `/go`, `/look`, `/get` 等多种指令。

这时，我们就需要使用 `elif` (else if的缩写) 来搭建更复杂的“**立交桥**”，进行多轮判断。

<div class="columns">
<div>

**更复杂的指令解析**
（ 请继续复制代码，观察执行结果）
```python
command = "/look"

if command == "/go": # 第1个判断
    print("处理移动逻辑...")
elif command == "/look": # 如果第1个判断为假，则进行第2个判断
    print("处理观察逻辑...")
elif command == "/get": # 如果前2个判断都为假，则进行第3个判断
    print("处理拾取逻辑...")
else: # 如果以上所有判断都为假
    print("无效的指令！")
```

</div>
<div class="align-middle-center" style="flex-direction: column;">

![width:300px](../../../lectures/images/2025-11-13-20-22-16.png)
**“立交桥”的可视化流程图**

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 讲解多路选择结构
本页的目标是在`if-else`的基础上，引入`elif`，讲解多路选择的实现方式。

**核心要点**：
1.  **“立交桥”比喻**: 这是一个从“T字路口”自然延伸而来的比喻，生动地描述了多路选择的复杂性。
2.  **强调执行顺序**: 通过逐字稿的讲解，清晰地传达了`if-elif-else`结构的一个核心特点：条件是**从上到下依次检查**的，并且**一旦满足一个，其余的就不再检查**。
3.  **流程图辅助**: 对于这种稍复杂的逻辑，流程图的价值变得更大，它能非常直观地展示程序的执行路径。

</div>

---

## **核心语法3：用 `and` / `or` 组合判断**

有时，一个简单的“判断题”不足以描述我们的规则。我们需要组合多个条件。

- **`and` (并且)**：要求**所有**子问题都为 `True`，最终答案才是 `True`。
  - `(玩家等级 > 10) and (拥有“公会徽章”)` -> 两个都得满足。

- **`or` (或者)**：只要**任何一个**子问题为 `True`，最终答案就是 `True`。
  - `(职业 == "法师") or (智力 > 15)` -> 满足一个就行。

`and` 和 `or` 就像连词，让我们可以提出更复杂的“判断题”。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引入逻辑运算符
本页的目标是介绍`and`和`or`这两个核心的逻辑运算符，让学员学会构建复合条件。

**核心要点**：
1.  **从需求出发**: 从“一个简单的判断题不足以...”这个需求出发，自然地引出需要组合多个条件。
2.  **清晰的定义**: 对`and`（并且）和`or`（或者）的定义清晰、准确，并用一句话总结了它们的核心要求（“所有都为True” vs “任何一个为True”）。
3.  **场景化举例**: 提供的两个游戏场景例子（进副本、学技能）非常贴切，能帮助学员在具体情境中理解`and`和`or`的用途。

</div>

---

## **模式转换：从“学习语法”到“指挥AI”**

我们已经掌握了 `if-else` 的核心逻辑。从现在开始，我们不再逐行编写代码，而是转换角色，作为“游戏设计师”**通过自然语言指挥AI完成整个程序**。

接下来，我们将通过两步指令，让AI为我们构建出完整的游戏循环和指令解析器。

<div class='insight' style="margin-top: 1rem;font-size: 0.6em;">

💡 **请注意：**

1.  **关注“指令”，而非“代码”**：你的核心任务是思考并写下清晰的、给AI的**指令**（Prompt）。
2.  **AI的代码可能包含“超前”内容**：为了让程序完整运行，AI可能会使用我们尚未学过的知识（例如 `startswith()` 方法）。
3.  **学会“忽略”**：你**完全可以忽略**那些看不懂的代码！只需关注AI生成的代码中，和你刚刚学过的 `if-else` 相关的部分即可。
4.  **保持“好奇”**：如果你对“超前”的代码感兴趣，这正是绝佳的预习机会！大胆地复制那段代码，向AI提问：“请用初学者能听懂的语言，解释这段代码是什么意思？”

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 动手环节前的“心理建设”
本页是一个非常重要的“过渡”和“心理建设”幻灯片，它在理论学习和动手实践之间搭建了一座桥梁。

**核心要点**：
1.  **明确角色转换**: 清晰地告诉学员，接下来的学习模式将从“学习语法”切换到“指挥AI”，这符合我们课程的核心理念。
2.  **管理学习预期**: “AI的代码可能包含‘超前’内容”这一点至关重要。它提前为学员打了“预防针”，避免了他们在看到不认识的代码时产生焦虑或挫败感。
3.  **教授学习方法**: “学会‘忽略’”和“保持‘好奇’”这两点，是在教授一种高效的、以我为主的AI辅助学习方法。它鼓励学员聚焦于当前的学习目标，同时利用AI进行自主探索，而不是被AI的输出牵着鼻子走。

</div>

---

## **第一步：让世界“聆听”一次指令**

我们向AI发出第一个指令。这个指令的目标是：让游戏能**执行一次完整的交互**：显示场景、获取指令、并根据最简单的 `/quit` 指令做出反应。

> **我们的指令 (Prompt):**
>
> 请在现有代码基础上进行修改。我需要程序能实现一次完整的单次交互：
> 1.  首先根据 `player_location` 变量，打印出当前地点的描述。
> 2.  然后使用 `input()` 函数来获取玩家的输入，并将输入的内容存入一个名为 `command` 的变量中。
> 3.  最后，使用 `if` 语句判断：如果玩家输入的 `command` 等于 `"/quit"`，就打印 "你退出了江湖..."。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 两步式动手任务 (第一步)
将一个大的动手任务分解为两个小步骤，是降低学员认知负荷、保证其获得持续正反馈的有效方法。

**核心要点**：
1.  **小步快跑**: 第一步的目标非常小、非常聚焦——只处理`/quit`这一个指令。这确保了学员能快速地获得一个成功的、可运行的中间产物，从而建立信心。
2.  **结构化Prompt**: 再次为学员提供了高质量的、结构化的Prompt范例，让他们在模仿中不断内化这种“将需求分解为步骤”的思维模式。
3.  **引入新函数**: 这个指令自然地引入了一个新的、至关重要的函数`input()`，让学员在任务驱动中学习新知识。

</div>

---

## **AI的实现与我们的关注点**

<div style="font-size:0.85em;">

AI根据我们的指令，生成了如下的单次交互脚本（注意：AI生成有一定随机性，内容可能稍有不同）。

```python
# ... (之前的世界定义代码) ...

# 根据 player_location 变量的值，从 world 字典中获取玩家所在地的描述，并打印出来
print("\n=== 武侠世界 ===")
print(world[player_location]['description'])

# 获取玩家输入
command = input("\n请输入指令（输入/quit退出）：")

# 判断玩家输入
if command == "/quit":
    print("你退出了江湖...")  
```

<div class='insight' style="font-size: 0.6em;">

✅ **我们的关注点：**

我们看到，程序现在是一个简单的、从上到下执行一次的脚本。`if command == "/quit":` 这一行精确地实现了我们“判断退出指令”的设计意图。这就足够了！

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 验证第一步成果并聚焦核心
本页的目标是展示第一步任务的成功结果，并引导学员将注意力聚焦到与本节课核心知识点最相关的代码上。

**核心要点**：
1.  **提供标准答案**: 展示AI生成的标准代码，让学员可以对比自己的结果，进行验证。
2.  **引导关注点**: `insight`框中的“我们的关注点”部分，明确地告诉学员，在AI生成的一堆代码中，你现阶段只需要看懂`if command == "/quit":`这一行就足够了。这极大地降低了学员的学习焦虑，让他们能聚焦于核心。
3.  **建立正反馈**: “这就足够了！”、“我们成功了！”等语言，为学员完成第一步任务提供了强烈的正向反馈和成就感。

</div>

---

## **第二步：实现完整的指令解析**

<div style="font-size:0.85em;">

很好，我们的程序已经能响应最基础的 `/quit` 指令了。接下来，我们向AI发出第二个指令，要求它在 `if` 语句后面，用 `elif` 和 `else` 补完所有我们设计好的游戏规则，构建一个完整的指令解析器。

> **我们的指令 (Prompt):**
>
> 非常棒！现在请在 `if` 语句后面继续添加 `elif` 和 `else` 分支，来实现对其他指令的解析：
> 1.  如果玩家输入 `"/look"`，就重新打印当前地点的描述。
> 2.  如果玩家输入的是以 `"/go"` 开头的指令（例如 `"/go east"`），就解析出后面的方向。然后检查这个方向是否是当前地点的一个有效出口。
>     - 如果是有效出口，就更新 `player_location` 变量为新的地点ID，并打印一句提示，比如“你来到了[新地点名称]...”。
>     - 如果不是有效出口，就打印“你不能往那个方向走。”
> 3.  对于所有其他无法识别的指令，用 `else` 分支打印“无效的指令！”。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 两步式动手任务 (第二步)
本页是动手任务的第二部分，其目标是在第一步的基础上，构建一个功能完整的、多路选择的指令解析器。

**核心要点**：
1.  **渐进式复杂性**: 任务的复杂性是逐渐增加的。这个Prompt比第一个要复杂得多，特别是`/go`指令的处理，它包含了一个“嵌套”的条件判断（先判断是不是`/go`，再判断出口是否有效）。
2.  **训练逻辑分解**: 这个Prompt本身就是一个极佳的逻辑分解范例。它教给学员如何将一个复杂的需求（处理玩家移动），分解为一系列更小的、可执行的逻辑步骤。
3.  **覆盖所有情况**: `else`分支的引入，是在训练学员一种重要的编程思维——**完备性**，即要考虑到所有可能的情况，包括非法的、预料之外的输入。

</div>

---

## **AI的最终代码与审查**

AI迅速迭代生成了包含完整逻辑的、有详细注释的最终代码，质量很高。

<style scoped>
.small-code pre, .small-code code {
  font-size: 0.72em;
  line-height: 0.9;
}
</style>

<div class="small-code">

```python
# ... (前面是没有变化的代码) ...
# 判断玩家输入
if command == "/quit":
    print("你退出了江湖...")
elif command == "/look":
    # 重新打印当前地点的描述
    print(world[player_location]['description'])
elif command.startswith("/go "):
    # 解析方向参数
    direction = command.split(" ", 1)[1]  # 获取/go后面的部分，例如"east"
    
    # 检查这个方向是否是当前地点的一个有效出口
    if direction in world[player_location]['exits']:
        # 更新 player_location 变量为新的地点ID
        new_location = world[player_location]['exits'][direction]
        player_location = new_location
        
        # 打印提示
        print(f"你来到了{new_location}...")
    else:
        # 不是有效出口，打印错误信息
        print("你不能往那个方向走。")
else:
    # 对于所有其他无法识别的指令，打印无效指令提示
    print("无效的指令！")

```

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示最终成果并引导测试
本页展示了整个动手任务的最终代码成果，并引导学员进行测试。

**核心要点**：
1.  **展示完整方案**: 提供了包含所有逻辑的最终代码，作为学员参考和学习的“标杆”。
2.  **引导多场景测试**: 逐字稿中引导学员测试多种情况（look, go-valid, go-invalid, other），这本身就是在教授“软件测试”的基本思想——覆盖不同的执行路径。
3.  **建立成就感**: 当学员发现程序的行为和预期完全一致时，他们会获得巨大的成就感，从而极大地激发他们继续学习的动力。

</div>

---

## **作为“设计师”的最终审查**

<div class="columns">
<div style="font-size:0.82em">

现在，请扮演“游戏设计师”的角色，对AI生成的最终代码进行**逻辑审查**。

你不需要理解每一行代码的技术细节，但你需要通过输入和输出的内容确认：

-   [✅] `"/quit"` 的逻辑对吗？
-   [✅] `"/look"` 的逻辑对吗？
-   [✅] `"/go"` 的逻辑是否完整？
    -   有没有处理无效方向（比如 `/go north`）？
    -   有没有处理错误指令（比如 `/go` 后面没跟方向）？
-   [✅] 对所有其他指令，是不是提示了“无效指令”？

</div>
<div class="align-middle-center" style="flex-direction: column;">

![AI负责实现，你负责设计和验收 width:400px](../../../lectures/images/2025-11-13-19-01-58.png)

**你的核心价值：代码评审与逻辑验收。** AI负责实现代码，你负责确保代码的逻辑符合你的设计蓝图。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 强化“设计师”角色与核心价值
本页旨在通过一个正式的“审查”环节，强化学员作为“设计师”的角色定位，并再次明确其核心价值。

**核心要点**：
1.  **角色扮演**: “请扮演‘游戏设计师’的角色”这句话，再次将学员代入到我们设定的角色中。
2.  **清单式审查**: 提供一个清晰的Checklist，将模糊的“审查”任务，分解为一系列具体的、可操作的检查项。
3.  **价值锚定**: 右栏的文字和图片，再次强调并总结了本阶段学员的核心价值——“代码评审与逻辑验收”，将实践活动与我们之前定义的“人机协作新模式”理论联系起来。

</div>

---

## **价值升华：你是“游戏规则”的唯一制定者**

<div class="columns">

<div class="styled-div" style="font-size: 0.65em">

我们来回顾一下这节课的人机协作流程：
1.  **你 (设计师)**：提出 `/look` 和 `/go` 的核心玩法规则。
2.  **AI (程序员)**：根据你的规则，生成了包含 `if/elif/else` 的代码。
3.  **你 (审查者)**：检查AI的代码逻辑，确保它符合你的预期，没有产生类似“原地踏步”的Bug。

AI能不知疲倦地编写代码，但它没有灵魂，没有世界观。它不知道“光明顶”和“武当山”哪个更应该是正派，也不知道你的游戏中，“/look”一下是否应该消耗体力。

**这些，只有你——游戏世界的设计师和规则的唯一制定者——才能决定。**

</div>
<div class="align-middle-center" style="flex-direction: column;">

![一个艺术家正在为一个巨大的机器人心脏绘制蓝图 width:300px](../../../lectures/images/2025-11-13-19-05-15.png)

<div class='insight' style="font-size: 0.6em;margin-top: 0.2rem;">

💡 **AI负责实现，你负责想象。** 你的核心价值，在于为代码注入灵魂——**创造**规则、构建体验、讲述故事。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 课程核心思想的再次升华
本页是本节课的“顶点”，旨在将学员的认知从“学会了if-else”提升到“理解了我在AI时代的价值”。

**核心要点**：
1.  **流程回顾**: 清晰地回顾了本节课的“设计-编码-审查”三步人机协作流程。
2.  **点明AI的局限性**: “没有灵魂，没有世界观”这句话，一针见血地指出了当前AI的根本局限，从而反衬出人类的独特价值。
3.  **锚定人类的创造性价值**: 用非常感性的语言（“注入灵魂”、“创造规则”、“构建体验”、“讲述故事”），将人类的价值定位在“创造性”和“设计感”上，给予学员极大的价值肯定。
4.  **视觉与文字的统一**: “为机器人心脏绘制蓝图”的图片，与“为代码注入灵魂”的文字形成了完美的隐喻统一，极具感染力。

</div>

---

## **本节课总结：我们获得了什么？**

<div class="columns ratio-6-4">

<div class="styled-div" style="font-size: 0.65em">

在本节课，我们为游戏世界装上了“规则引擎”，你作为“游戏设计师”的核心能力也得到了升级：

- **获得了“规划”能力**
  - 你学会了如何将现实世界的游戏规则，翻译成程序可以理解的 `If-Else` 决策路径。
- **获得了“审查”能力**
  - 你掌握了审查AI代码“设计蓝图”中**核心交互逻辑**的方法，确保AI的决策符合你的设计意图。

你不再只是一个被动的旁观者，而是能主动为你的世界**制定规则、定义交互**的创造者——哪怕目前，这还只是“一瞬间”的交互。

</div>

<div class="align-middle-center">

![width:400px](../../../lectures/images/2025-11-13-19-06-50.png)

</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 总结本节课的核心能力收获
本页旨在用简洁的语言，为学员总结本节课获得的核心技能，强化其获得感。

**核心要点**：
1.  **能力化总结**: 再次将学习成果总结为“规划能力”和“审查能力”这两项可迁移的技能，而不是知识点。
2.  **关键词强化**: “规则引擎”、“决策路径”、“核心交互逻辑”等关键词，回顾并强化了本节课的核心概念。
3.  **肯定并埋下伏笔**: “你不再只是一个被动的旁观者...”这句话给予了学员极大的肯定和价值感。而最后“哪怕目前，这还只是‘一瞬间’的交互”这句话，则巧妙地指出了当前方案的局限性，为下一节课的内容埋下了伏笔。

</div>

---

## **下一步预告：从“时间切片”到“时间流逝”**

<div class="columns ratio-6-4">

<div style="font-size: 0.9em;">

我们已经能让世界响应我们的指令了！这是一个巨大的进步！

但是，我们的程序依然只能表现世界运转的**一个极短的“时间切片”**。它接收一次指令，执行一次判断，然后整个世界的“时间”就停止了。

**如何让时间真正“流动”起来？**

我们如何为这个世界装上“心跳”，让它不再是执行一次就结束的“切片”，而是能持续运转、让玩家沉浸其中探索的“时间流”？

为了让世界拥有“心跳”，下一节课，我们将学习指挥AI的三大核心指令中的最后一个——**循环**！

</div>

<div class="align-middle-center">

![width:400px](../../../lectures/images/2025-11-13-19-09-28.png)

</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 制造悬念，预告下一课
本页作为本节课的结尾，其核心目标是制造一个新的、更强的“痛点”，并清晰地预告下一节课的主题，激发学员持续学习的欲望。

**核心要点**：
1.  **肯定现有成果**: “我们已经能让世界响应我们的指令了！这是一个巨大的进步！”——先扬后抑，让学员在获得满足感的同时，更容易接受新的挑战。
2.  **制造新的“痛点”**: “时间切片” vs “时间流”的比喻非常生动，它让学员能直观地感受到当前程序“无法持续运行”的致命缺陷。
3.  **引入终极悬念**: “为世界装上‘心跳’”这个比喻，将“循环”这个技术概念包装得极具吸引力和重要性。
4.  **呼应模块目标**: “三大核心指令中的最后一个”这句话，让学员意识到下一节课将是本模块理论学习的高潮和收官，从而产生更高的期待。

</div>