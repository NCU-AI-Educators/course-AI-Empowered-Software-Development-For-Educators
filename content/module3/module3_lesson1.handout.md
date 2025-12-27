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
pre, code {                                                                                          
  white-space: pre-wrap !important;                                                                  
  word-wrap: break-word !important;                                                                  
                                                                             
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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-21-14-57-02.png)

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
## 第9节课: 核心概念：函数——代码的“积木”

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 模块化与代码复用
本节课的核心“函数”，是实现“**模块化编程 (Modular Programming)**”的基础。模块化思想旨在将一个大型、复杂的软件系统，拆分成一个个独立的、功能明确的、可交互的“模块”。这样做的好处是：
1.  **降低复杂度**: 每个模块只关注自己的功能，使得我们可以独立地思考和解决问题，而不用一次性面对整个系统的复杂性。
2.  **提升复用性**: 一个设计良好的模块（如一个计算特定税率的函数），可以在多个不同的项目中被重复使用，避免重复“造轮子”。
3.  **便于协作**: 在团队开发中，不同的开发者可以分工负责不同的模块，并行开发，提高效率。

**函数，就是我们在Python中能创建的最小、最基础的“模块”。**

</div>

---

## **回顾：新的“痛点”——臃肿的主循环**

<div class="columns ratio-6-4">
<div style="font-size: 0.8em;">

在模块二的结尾，我们构建了一个可以持续运行的武侠世界，取得了巨大进展！

但是，作为一个追求卓越的“架构师”，我们发现了一个新的痛点：我们的“游戏主循环”开始变得**臃肿和混乱**了。

所有的游戏逻辑——处理`/go`、`/look`、`/take`、`/drop`——都堆积在 `while` 循环内部，形成了一个巨大的 `if-elif-else` 长链。

```python
while True:
    # ...
    if command.startswith("/go "):
        # 处理go的一大段代码
    elif command.startswith("/take "):
        # 处理take的一大段代码
    # ... 更多更多的elif
```

这就像一个**杂乱无章的巨大抽屉**，所有东西都堆在一起，找起来费劲，改起来也容易出错。

</div>
<div class="align-middle-center" style="flex-direction: column;">

![一个人面对着一团乱麻般的代码，显得很苦恼 width:350px](../../../lectures/images/2025-11-21-13-50-46.png)

<p style="margin-top: 1rem; font-size: 0.9em;">我们该如何为这个混乱的“抽屉”进行整理和归类呢？</p>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 代码异味与技术债
软件工程中，我们把这种预示着深层问题的代码特征，称为“**代码异味 (Code Smell)**”。我们遇到的“臃肿的主循环”，就是一种典型的代码异味，叫做“**过长方法 (Long Method)**”。它违反了“单一职责”的原则，让一段代码承担了过多的功能。

如果放任“代码异味”不管，项目就会积累下“**技术债 (Technical Debt)**”。就像现实中的债务一样，现在为了图快而写的“烂代码”，将来需要花费更多的时间和精力去维护和修改。我们这节课学习函数，就是一次主动的“**重构 (Refactoring)**”，一次对代码质量的投资，是在“偿还”技术债。

</div>

---

## **本节课目标：学会“打包”与“复用”**

为了解决“代码臃肿”的问题，我们需要学习一种全新的、极其重要的编程思想：**封装 (Encapsulation)**。

本节课，我们将学习实现“封装”的核心工具：

### **函数 (Function)**
- **它是什么**：一个被命名的、可重复使用的“**代码包裹**”或“**功能积木**”。
- **你的新能力**：
  1. **封装逻辑**：学会将一段具体的业务逻辑（如处理`/go`指令的所有代码）“打包”成一个独立的函数。
  2. **简化流程**：通过“调用”函数，让你的主循环变得像“总指挥”一样清晰、简洁。

**最终，你将能指挥AI，将你的游戏引擎重构为一个由多个“功能积木”搭建而成的、结构清晰的系统。**

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 抽象与封装
- **抽象 (Abstraction)**: 编程中的“抽象”指的是忽略一个主题中与当前目标无关的复杂细节，只关注与目标相关的核心概念。例如，当我们开车时，我们只关心方向盘、油门、刹车（抽象接口），而不需要关心发动机内部的活塞运动和燃料燃烧（实现细节）。

- **封装 (Encapsulation)**: “封装”是实现“抽象”的一种技术手段。它将数据（属性）和操作数据的方法（函数）捆绑在一起，并对外部世界隐藏其内部的实现细节。一个函数就是最基本的封装形式：调用者只需要知道函数名和参数（接口），而不需要关心函数内部是如何实现的（实现细节）。

本节课，我们学习用函数去“封装”逻辑，本质上就是在进行一次“抽象”的实践。

</div>

---

## **核心比喻：从“菜谱”到“微波炉”**

<div class="columns" style="font-size: 0.85em;">
<div>

### **没有函数之前**
我们的代码就像一本详细的“**菜谱**”。每次想“加热食物”，都必须从头到尾把所有步骤（拿出盘子、放入食物、设置时间、开始加热...）念一遍。

```python
# 第一次加热
print("拿出盘子")
print("放入剩菜")
print("设置1分钟")
print("开始加热")

# 第二次加热
print("拿出盘子")
print("放入牛奶")
print("设置30秒")
print("开始加热")
```
**问题**：重复、繁琐、容易出错。

</div>
<div style="font-size: 0.95em;">

### **有了函数之后**
函数就像一台“**微波炉**”。我们把所有加热步骤都“封装”在了微波炉内部。

现在，我们只需要“**调用**”它，并告诉它要加热的“**参数**”（食物和时间），它就能自动完成所有内部步骤。

```python
def heat_food(food, time):
    print("拿出盘子")
    print(f"放入{food}")
    print(f"设置{time}")
    print("开始加热")

# 调用函数
heat_food("剩菜", "1分钟")
heat_food("牛奶", "30秒")
```
**优势**：简洁、易用、一次定义、随处复用。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### DRY原则
这个比喻完美地诠释了软件开发中一个极其重要的原则：**DRY (Don't Repeat Yourself)**，即“不要重复你自己”。

DRY原则的核心思想是，系统中的每一处知识都必须具有单一、无歧义、权威的表示。换句话说，任何一段逻辑、一个配置、一个算法，都应该只在一个地方定义。如果你发现自己在复制粘贴代码，那几乎总是违反了DRY原则的信号。

**违反DRY的危害**:
- **维护困难**: 如果一段逻辑被复制了10次，当需求变更时，你就必须找到并修改所有这10个地方，很容易出错或遗漏。
- **代码臃肿**: 大量的重复代码会迅速增加代码库的体积。
- **逻辑不一致**: 在修改多个副本时，很容易因为疏忽导致某些副本没有被更新，从而产生逻辑不一致的Bug。

函数是实践DRY原则最基本、最强大的工具。

</div>

---

## **函数的“解剖学”：定义与调用**

一个函数主要由两部分组成：**定义** 和 **调用**。

<div class="columns" style="font-size: 0.8em;">
<div>

### **1. 定义函数 (Define)**
这是在“**创造工具**”。我们使用 `def` 关键字，为一段代码赋予一个名字，并规定它需要哪些“原料”（参数）。

```python
# def 关键字，表示“我要定义一个函数”
# handle_look 是我们为这个功能起的名字
# () 里是“参数列表”，是它工作需要的“原料”
def handle_look(world, player_location):
    
    # 缩进的代码块，是这个函数的“功能主体”
    print("--- 观察四周 ---")
    print(world[player_location]['description'])
    # ... (更多处理逻辑)
```

</div>
<div>

### **2. 调用函数 (Call)**
这是在“**使用工具**”。我们通过写下函数的名字，并提供它需要的具体“原料”（参数），来执行它内部封装的所有代码。

```python
# 在主循环中
# ...
elif command == "/look":
    # 调用我们定义的函数
    # 并把当前的世界地图和玩家位置作为“原料”传给它
    handle_look(world, player_location)
```

</div>
</div>

<div class='insight' style="margin-top: 1rem;font-size: 0.6em;">

💡 **核心思想**：**定义**只发生一次，就像你只买一台微波炉。而**调用**可以发生无数次，就像你可以随时用这台微波炉加热任何东西。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 函数签名、参数与作用域
- **函数签名 (Function Signature)**: 通常指函数的名称和它的参数列表（参数的类型、顺序和数量）。函数签名是函数的唯一标识。在很多静态类型语言中，函数签名还包括返回值的类型。

- **形参与实参 (Parameter vs. Argument)**:
  - **形式参数 (Parameter)**: 定义函数时，写在函数名后括号里的变量，如 `world`, `player_location`。它们是函数内部的“占位符”，规定了该函数需要接收什么样的数据。
  - **实际参数 (Argument)**: 调用函数时，传递给函数的具体值或变量。它们是填充“占位符”的真实“原料”。

- **作用域 (Scope)**: 指的是一个变量能够被访问的区域。
  - **全局作用域 (Global Scope)**: 在程序的任何地方都能被访问的变量（如我们定义在最外层的`world`字典）。
  - **局部作用域 (Local Scope)**: 在函数内部定义的变量，只在该函数内部有效，函数执行结束后就会被销毁。函数的参数也属于局部作用域。这就像微波炉内部的转盘，只有微波炉自己知道它的存在。这种机制避免了不同函数间的变量名冲突，是封装思想的重要体现。

</div>

---

## **重构第一步：将`/look`指令封装成函数**

让我们从最简单的`/look`指令开始，亲手实践一次“封装”的过程。

<div class="columns">
<div>

#### **重构前 (Before)**
主循环的`elif`分支中，堆砌着所有处理观察的逻辑。

```python
# 主循环
while True:
    # ...
    elif command == "/look":
        # 所有细节都堆在这里
        print(world[player_location]['description'])
        if 'items' in world[player_location]:
            for item in world[player_location]['items']:
                print(f"你看到了: {item}")
        # ... 更多代码
```

</div>
<div>

#### **重构后 (After)**
主循环变得非常“干净”，只负责调用函数。所有实现细节都被“藏”在了函数内部。

```python
# 1. 在主循环外部，定义函数
def show_room_details(world, player_location):
    print(world[player_location]['description'])
    if 'items' in world[player_location]:
        for item in world[player_location]['items']:
            print(f"你看到了: {item}")
    # ... 更多代码

# 2. 在主循环内部，调用函数
while True:
    # ...
    elif command == "/look":
        show_room_details(world, player_location)
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 重构 (Refactoring)
本页我们进行的“封装”操作，是“**重构**”的一种。

**重构**是一个严格定义的过程，指的是**在不改变代码外在行为的前提下，对其内部结构进行修改，以提高其可读性、可维护性和代码质量。**

重构的关键在于“**不改变外在行为**”。也就是说，对于用户（或程序的其他部分）来说，重构前和重构后，程序的功能是完全一样的。`/look`指令在重构前后，打印出的内容没有任何变化。但对于开发者来说，代码的内部结构却变得更清晰、更易于管理了。

重构是软件开发中一项至关重要的日常活动。优秀的程序员会像整理房间一样，持续不断地对代码进行小范围的重构，以防止“技术债”的累积。我们刚才做的，就是一次最基本、也最常见的重构手法：**提取函数 (Extract Method/Function)**。

</div>

---

## **重构的价值：清晰的“指挥中心”**

<div style="font-size: 0.75em;">

经过函数封装的重构后，我们的游戏主循环，从一个混乱的“大车间”，变成了一个清晰的“**指挥中心**”。

```python
# 重构后的主循环
while True:
    command = input("> ")

    if command == "/quit":
        handle_quit() # 调用“处理退出”的函数
    
    elif command.startswith("/go"):
        handle_go(command, world, player_location) # 调用“处理移动”的函数

    elif command.startswith("/take"):
        handle_take(command, world, player_location) # 调用“处理拾取”的函数

    elif command == "/look":
        handle_look(world, player_location) # 调用“处理观察”的函数
        
    else:
        handle_unknown_command() # 调用“处理未知指令”的函数
```

**架构师的视角**：现在，主循环只负责“**分发任务**”，而不关心任务的“**具体实现**”。这使得代码的逻辑层次变得极为清晰，极大地提升了可读性和可维护性。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 分离关注点 (Separation of Concerns, SoC)
这是软件设计中最核心、最古老的原则之一。它主张将一个复杂的系统划分为不同的部分，每个部分只处理一个**关注点**。

一个“关注点”是指影响代码的一组信息。在我们的例子中：
- 主循环的“关注点”是：**接收用户输入，并将指令路由或分发给正确的处理器**。
- `handle_go`函数的“关注点”是：**处理与“移动”相关的所有逻辑**。
- `handle_look`函数的“关注点”是：**处理与“观察”相关的所有逻辑**。

通过函数封装，我们成功地将“指令分发”和“具体指令处理”这两个不同的“关注点”分离开来。

**SoC的好处**:
- **可理解性**: 每个部分都更简单，更容易被理解。
- **可维护性**: 修改一个关注点（如修改移动逻辑），不会意外地影响到另一个关注点（如观察逻辑）。
- **可复用性**: 单一的、功能内聚的模块更容易被复用。

</div>

---

## **动手环节(1/2)：指挥AI进行“封装”**

<div style="font-size: 0.85em;">

现在，让我们指挥AI，将我们臃肿的主循环，重构为由函数驱动的清晰结构。

**你的任务：**
指导AI将处理`/look`和`/go`指令的逻辑，分别封装到独立的函数中。

> **我们的指令 (Prompt):**
>
> 请帮我重构现有的武侠游戏脚本，以提升代码的结构和可读性。具体要求如下：
> 1.  创建一个名为 `handle_look` 的函数。将主循环中处理 `/look` 指令的所有逻辑代码，都移动到这个函数内部。
> 2.  创建一个名为 `handle_go` 的函数。将主循环中处理 `/go` 指令的所有逻辑代码，都移动到这个函数内部。
> 3.  修改主循环的 `if-elif` 结构：在对应的指令判断分支下，改为“调用”你刚刚创建的相应函数。
> 4.  请仔细思考这两个函数需要哪些“外部信息”（例如`world`地图、`player_location`等）才能正常工作，并为它们设计合理的“参数”。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Prompt的层次
这个Prompt范例，展示了一种“**设计驱动**”的提问方式。与之前模块我们可能使用的“**愿景驱动**”的Prompt（例如：“帮我把代码变得更整洁”）相比，它的特点是：
- **指令性强**: 使用“创建”、“移动”、“修改”等动词，明确告知AI要执行的操作。
- **步骤清晰**: 将一个大的重构任务，分解为多个可执行的小步骤。
- **包含设计约束**: 不仅告诉AI“做什么”，还告诉它“怎么做”（例如，要创建指定名字的函数，要思考参数）。

这种提问方式，能让你对AI的产出有更强的控制力，使得AI生成的代码更符合你的预期。作为“AI开发主管”，你需要熟练掌握这种编写清晰、结构化需求的能力。

</div>

---

<style scoped>
.styled-box {
  font-size: 0.4em;
}
</style>

## **动手环节(2/2)：审查AI的“设计”**

<div style="font-size: 0.7em;">

AI会根据你的指令，生成重构后的代码。现在，你的任务是作为“架构师”，审查它的设计。

**审查清单：**
1.  **函数定义是否正确？**
    - AI是否使用了 `def` 关键字？
    - 函数名 (`handle_look`, `handle_go`) 是否清晰？
2.  **逻辑是否被正确移动？**
    - 原本在`elif`块中的代码，是否被完整地移动到了函数内部，并保持了正确的缩进？
3.  **函数调用是否正确？**
    - 主循环中是否正确地调用了这两个函数？
4.  **参数设计是否合理？ (最关键)**
    - AI为这两个函数设计了哪些参数？
    - 你能理解为什么需要这些参数吗？（例如，`handle_go`为什么不仅需要`world`和`player_location`，还需要`command`本身？）

<div class='key-point' style="margin-top: 1rem;font-size: 0.6em;">

  ⚠️ **核心挑战**：理解“参数”是函数最核心、也最难理解的概念。它是外部世界与函数内部世界沟通的“唯一桥梁”。大胆地向AI提问：“请解释一下，你为什么为`handle_go`函数设计了这三个参数？它们分别起什么作用？”
</div>

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 值传递 vs. 引用传递
关于参数传递，编程语言主要有两种方式：
- **值传递 (Pass by Value)**: 函数接收的是实参的一个“副本”。在函数内部修改参数，**不会**影响到函数外部的原始变量。这就像你把一份文档复印给了同事，他在复印件上修改，不会影响你的原件。
- **引用传递 (Pass by Reference)**: 函数接收的是实参的“内存地址”，即变量的“引用”。在函数内部修改参数，**会**影响到函数外部的原始变量。这就像你把一个在线文档的链接分享给了同事，他通过链接直接修改了云端的同一份文档。

Python的参数传递机制比较特殊，官方称之为“**按对象引用传递 (Pass by Object Reference)**”。可以简化理解为：
- 对于**不可变类型**（如数字、字符串、元组），其行为类似于“值传递”。
- 对于**可变类型**（如列表、字典），其行为类似于“引用传递”。

在我们的例子中，`world`（字典）和`inventory`（列表）都是可变类型。因此，当我们将它们作为参数传递给函数时，函数内部对它们的修改（如`items.remove()`）会直接影响到原始的`world`和`inventory`。理解这一点，对于编写正确的Python代码至关重要。

</div>

---

## **函数的“返回值”：从函数内部“递出”结果**

<div style="font-size: 0.75em;">

我们的函数现在像一个“黑箱”，能接收外部的“原料”（参数），然后在内部处理。

但如果函数内部产生了新的结果（例如，玩家移动后，`player_location`更新了），它该如何将这个新结果“**递回**”给外部世界呢？

答案是：**`return` 语句**。
</div>

<div class="columns">
<div>

```python
# handle_go 函数内部
def handle_go(command, world, current_loc):
    # ... (一堆处理逻辑)
    
    if direction_is_valid:
        new_loc = ... # 计算出新的地点
        print("你移动到了...")
        return new_loc # 将新地点作为“结果”返回
    else:
        print("无法移动...")
        return current_loc # 移动失败，将旧地点原样返回

# 主循环中
while True:
    # ...
    elif command.startswith("/go"):
        # “接收”函数返回的结果，并用它更新主循环中的状态
        player_location = handle_go(...)
```

</div>
<div class="align-middle-center">

![一个黑箱，一个箭头指向它（参数），另一个箭头从它指向外部（返回值） width:400px](../../../lectures/images/2025-11-21-14-01-26.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 函数的输入与输出
至此，我们学习了函数与外部世界交互的两种通道：
- **输入**: 通过**参数 (Parameters/Arguments)** 接收数据。
- **输出**: 通过**返回值 (Return Value)** 传递结果。

一个设计良好的函数，应该像一个纯粹的“数据处理器”。它接收输入，进行处理，然后返回输出，而不应该偷偷地去修改函数外部的状态（这被称为“副作用”）。

在Python中：
- 函数可以没有参数。
- 函数可以没有`return`语句。如果一个函数执行完毕时没有遇到`return`，它会自动返回一个特殊的值`None`。
- `return`语句一旦被执行，函数会立刻终止，并返回指定的值。
- 函数可以返回任何类型的数据，包括数字、字符串、列表、字典，甚至另一个函数。

</div>

---

## **迭代指令：用`return`重构`handle_go`**

现在，让我们用更专业的“返回值”方式，来重构我们的`handle_go`函数。

> **我们的迭代指令 (Prompt):**
>
> 请再次重构我的`handle_go`函数，让它的职责更纯粹。
> 1.  在`handle_go`函数中，当移动成功时，不要直接修改全局的`player_location`变量。相反，函数应该使用`return`语句，返回计算出的`new_location`。
> 2.  如果移动失败，函数应该`return`旧的、未发生改变的`player_location`。
> 3.  修改主循环中调用`handle_go`函数的代码：它现在需要“接收”`handle_go`函数的返回值，并用这个返回值来更新主循环中的`player_location`变量。

**思考：** 为什么要这么做？这种修改，让`handle_go`函数的“职责”发生了什么变化？

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 全局变量 vs. 局部变量
- **全局变量 (Global Variable)**: 在程序顶层（任何函数之外）定义的变量。理论上，它可以在程序的任何地方被读取和修改。我们之前的`player_location`就是一个全局变量。
- **局部变量 (Local Variable)**: 在函数内部定义的变量（包括参数）。它只在函数内部有效。

**为什么应尽量避免在函数内部修改全局变量？**
1.  **降低可读性**: 如果一个函数悄悄地修改了外部的全局变量（这种行为被称为“**副作用 (Side Effect)**”），代码的逻辑会变得非常隐晦和难以追踪。你必须阅读函数的每一行代码，才能知道它对外部世界造成了什么影响。
2.  **增加耦合度**: 函数与它所修改的全局变量产生了紧密的“**耦合**”。这使得函数无法被独立地测试和复用。你不能把它拿到另一个没有定义那个全局变量的项目中使用。
3.  **易于出错**: 在大型项目中，多个函数可能会在不经意间修改同一个全局变量，导致难以预料的、灾难性的Bug。

通过使用“参数”传入数据，并通过“返回值”传出结果，可以最大限度地减少函数对全局变量的依赖，使其成为一个独立的、可预测的“纯函数”。

</div>

---

<style scoped>
.styled-box {
  font-size: 0.4em;
}
</style>

## **架构师的思考：单一职责原则**

<div class="columns ratio-6-4">
<div class="styled-div" style="font-size: 0.5em;">

刚才的重构，体现了软件设计中一条极其重要的原则：**单一职责原则 (Single Responsibility Principle)**。

#### **重构前**
`handle_go` 函数做了**两件**事：
1.  计算新位置。
2.  修改外部世界的状态（直接修改了`player_location`）。

#### **重构后**
`handle_go` 函数现在只做**一件**事：
1.  根据输入，计算并返回一个结果。

它变成了一个“**纯函数**”，一个纯粹的“计算工具”。它不再关心外部世界的状态，也不再有“副作用”。

这种“高内聚、低耦合”的设计，使得函数更容易被理解、测试和复用。这是衡量代码质量的核心标准。

</div>
<div class="align-middle-center">

![一个瑞士军刀（功能混杂）和一个扳手（功能单一）的对比 width:350px](../../../lectures/images/2025-11-21-14-11-47.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 软件设计原则
- **单一职责原则 (Single Responsibility Principle, SRP)**: 一个模块（如一个函数或一个类）应该只对一类用户或一个功能负责。通俗地说，它应该只有一个“引起变化的原因”。在我们的例子中，`handle_go`函数现在只因“计算移动逻辑”的改变而改变，而不再因“外部状态管理方式”的改变而改变。

- **纯函数 (Pure Function)**: 一个函数如果满足以下两个条件，就被认为是纯函数：
  1.  **相同的输入永远产生相同的输出**。
  2.  **没有可观察到的副作用**（不修改外部变量、不进行I/O操作如打印等）。
  我们重构后的`handle_go`（如果我们忽略其中的`print`语句）就非常接近一个纯函数。纯函数具有极强的可预测性、可测试性和可组合性，是函数式编程范式的核心。

- **高内聚，低耦合 (High Cohesion, Low Coupling)**: 这是衡量软件设计质量的通用标准。
  - **高内聚**: 指一个模块内部的各个元素（代码、数据）彼此紧密相关，共同完成一个单一的功能。我们的新`handle_go`函数内聚性很高。
  - **低耦合**: 指模块与模块之间的依赖关系很弱。通过使用参数和返回值，我们大大降低了`handle_go`函数与主循环之间的耦合度。

</div>

---

## **本节总结：我们获得了什么？**

<div class="columns ratio-6-4">
<div style="font-size: 0.82em;">

在本节课，我们掌握了整理代码、提升架构的终极武器——**函数**。

- **一个核心思想：封装**
  - 我们学会了将混乱的逻辑“打包”成独立的、可复用的“功能积木”。

- **两种核心操作：定义与调用**
  - 掌握了 `def` (创造工具) 和 `call` (使用工具) 的基本模式。

- **一种架构能力：重构**
  - 你第一次作为“架构师”，通过函数封装，将一个混乱的程序**重构**成了一个结构清晰、职责分明的系统。你的代码质量和你的思维层次，都得到了质的飞跃。

</div>
<div class="align-middle-center">

![一个宝箱，里面装着函数的图标、积木和一个大脑的图标 width:400px](../../../lectures/images/2025-11-21-14-14-40.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 知识体系复盘
本节课，你学习了“**函数式分解 (Functional Decomposition)**”这一核心编程范式。这意味着你开始学习将一个大的问题，分解为一个个更小的、可以被函数解决的子问题。

你接触到的软件工程概念包括：
- **思想**: 封装 (Encapsulation), 抽象 (Abstraction), 分离关注点 (SoC), 单一职责原则 (SRP)。
- **原则**: DRY (Don't Repeat Yourself)。
- **实践**: 重构 (Refactoring), 提取函数 (Extract Function)。
- **术语**: 代码异味 (Code Smell), 技术债 (Technical Debt), 副作用 (Side Effect), 纯函数 (Pure Function), 高内聚低耦合。

虽然你不需要立刻记住所有这些术语，但理解它们背后的思想，将为你成为一名优秀的AI赋能开发者奠定坚实的理论基础。

</div>

---

## **下一步预告：当“积木”出错了怎么办？**

<div class="columns ratio-6-4">
<div style="font-size: 0.9em;">

我们已经学会了如何创造和使用“功能积木”。

但是，如果我们的积木本身就有问题呢？如果AI给我们的函数，在某些情况下会“崩溃”怎么办？

- 当程序因为一个错误而意外终止时，我们该如何看懂那些天书般的“**错误信息**”？
- 我们该如何向AI准确地描述问题，并**引导它自我修复**，而不是我们自己去修改代码？

下一节课，我们将学习一项至关重要的人机协作技能：**与AI结对调试 (Pair Debugging)**，让你从“代码的使用者”，真正升级为AI的“**项目经理**”。

</div>
<div class="align-middle-center">

![一个程序员和一个AI机器人坐在一起，指着屏幕上的一个红色Bug图标进行讨论 width:400px](../../../lectures/images/2025-11-21-14-18-21.png)
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 软件开发生命周期：测试与调试
一个完整的软件开发过程，不仅仅是“写代码”。一个简化的生命周期包括：
1.  **需求分析**: 我们想做什么？
2.  **设计**: 我们该怎么做？（我们画的蓝图、对函数的规划都属于设计）
3.  **实现 (Implementation)**: 编写代码。
4.  **测试 (Testing)**: 验证代码是否按预期工作。
5.  **调试 (Debugging)**: 当测试发现问题时，定位并修复错误的过程。
6.  **维护 (Maintenance)**: 在软件发布后，持续修复问题和增加新功能。

我们下一节课要学习的“调试”，是软件质量保障环节中不可或缺的一环。学会调试，意味着你开始具备独立完成一个小型软件开发全周期的能力。

</div>