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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 开场：函数——代码的“积木”
本页作为课程开场，核心目标是点明本节课的核心概念“函数”，并用“积木”这一核心比喻，建立学员对函数功能（封装与复用）的初步、直观印象。

**核心要点**:
1. **点明主题**: 清晰地揭示本节课的主角是“函数”。
2. **建立比喻**: 引入“积木”的核心比喻，将抽象的函数概念与具体、可感的对象联系起来。
3. **激发兴趣**: 预示着学员将要学习一种强大的代码组织工具。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 回顾痛点：臃肿的主循环
本页的核心目标是承上启下，通过回顾模块二结尾留下的“代码臃肿”这一痛点，并借助“杂乱的抽屉”比喻，来激发学员学习新知识（代码组织方法）的强烈动机。

**核心要点**:
1. **连接过去**: 从学员已有的体验（模块二的代码）出发，引出新的问题。
2. **痛点可视化**: 用“杂乱的抽屉”比喻，让“代码混乱”这一抽象问题变得具体可感。
3. **建立动机**: 清晰地提出“我们该如何整理？”这一问题，为引入“函数”这一解决方案做铺垫。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 设定目标：学会“打包”与“复用”
本页旨在明确本节课的核心学习目标。通过引入“封装”思想和“函数”概念，并使用“代码包裹”和“功能积木”等比喻，清晰地定义学员将要掌握的“封装逻辑”和“简化流程”两项新能力。

**核心要点**:
1. **引入核心思想**: 正式提出“封装”这一重要的编程思想。
2. **定义核心概念**: 将“函数”定义为实现封装的工具。
3. **明确能力产出**: 清晰地告知学员，学完本节课后，他们将能“封装逻辑”和“简化流程”。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 核心比喻：从“菜谱”到“微波炉”
本页通过“菜谱 vs 微波炉”这一生动、具体的比喻，让学员深刻理解函数是如何解决“代码重复”这一核心问题的。通过前后对比，直观展示函数在提升代码简洁性和复用性方面的巨大价值。

**核心要点**:
1. **问题具象化**: 将没有函数的重复代码比作“菜谱”，步骤繁琐。
2. **方案具象化**: 将使用函数封装的代码比作“微波炉”，功能强大且使用简单。
3. **引入关键概念**: 在比喻中自然地引入“调用(Call)”和“参数(Parameter)”的概念。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 函数解剖：定义与调用
本页旨在清晰地拆解函数的两大核心环节。通过将“定义”比作“创造工具”，将“调用”比作“使用工具”，来帮助学员建立心智模型，并结合代码实例，讲解`def`、函数名、参数等基本语法。

**核心要点**:
1. **环节拆分**: 明确区分“定义(Define)”和“调用(Call)”两个核心动作。
2. **建立心智模型**: 用“创造工具 vs 使用工具”的比喻来帮助理解。
3. **语法讲解**: 结合代码，点出`def`关键字、函数名、参数、函数体等关键语法元素的含义。
4. **固化思想**: 用“买一次微波炉，用无数次”的比喻，强化“一次定义，多次调用”的核心思想。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 案例演示：封装`/look`指令
本页通过一个具体的“重构”前后对比，让学员直观地看到函数封装给代码结构带来的巨大改善。核心是展示原本混乱的逻辑块如何被一行简洁的函数调用所替代。

**核心要点**:
1. **前后对比**: 采用“Before/After”的结构，视觉冲击力强，效果一目了然。
2. **展示收益**: 清晰地展示了重构后的代码变得更“干净”，实现细节被“藏”起来，主干逻辑更清晰。
3. **建立感性认识**: 让学员在亲眼所见中，体会到函数封装带来的“代码变整洁”的直观好处。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 价值升华：清晰的“指挥中心”
本页旨在从架构层面升华函数封装的价值。通过展示一个完全重构后的理想主循环，引入“指挥中心”的比喻，让学员理解代码分层和“分离关注点”的重要思想。

**核心要点**:
1. **架构视角**: 将学员的视角从“实现一个功能”提升到“设计一个系统”的高度。
2. **强化比喻**: 将主循环比作“指挥中心”，将函数调用比作“分发任务”，生动地解释了代码分层的概念。
3. **引入专业思想**: 首次引入“分离关注点”（Separation of Concerns）这一重要的软件设计原则，提升课程的理论深度。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 动手环节：指挥AI进行封装
本页是第一个动手实践环节，核心是引导学员通过编写一个结构化的Prompt，指挥AI完成一次完整的代码封装重构任务，将理论知识转化为实践能力。

**核心要点**:
1. **任务导向**: 给予学员一个明确、具体的重构任务。
2. **Prompt即教学**: 提供的Prompt范例本身就是一次高质量需求的教学，它将一个大任务分解为多个清晰的步骤。
3. **聚焦“参数”**: Prompt的第4点，引导学员开始思考函数与外部世界的数据交换，为后续理解“参数”这一核心概念埋下伏笔。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 4分钟
### 动手环节：审查AI的设计并理解“参数”
本页的核心是引导学员审查AI生成的代码，并聚焦于理解“参数”这一最核心、最难的概念。通过提供“审查清单”和提问模板，培养学员的代码阅读能力和利用AI进行深度学习的能力。

**核心要点**:
1. **角色转换**: 让学员扮演“架构师”的角色，从被动接受代码转变为主动审查代码。
2. **结构化审查**: 提供“审查清单”，将模糊的“审查”任务分解为具体的检查点，降低认知负荷。
3. **聚焦难点**: 明确指出“参数”是本节课的难点和核心，并提供向AI提问的范例，示范如何利用AI作为学习工具来攻克难点。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 核心概念：函数的“返回值”
本页旨在引入函数的第二个核心概念——返回值`return`。通过“黑箱”和“递回结果”的比喻，清晰地展示“传入参数 -> 处理 -> 传出结果 -> 外部接收”的完整数据流。

**核心要点**:
1. **提出问题**: 从“函数如何将内部结果递回给外部”这一问题出发，自然地引出`return`的必要性。
2. **可视化数据流**: “黑箱”图非常直观地展示了参数（输入）和返回值（输出）在函数边界内外的数据流动。
3. **闭环展示**: 代码示例清晰地展示了函数内部`return new_loc`和外部`player_location = handle_go(...)`的“传出-接收”完整闭环。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 4分钟
### 动手环节：使用`return`迭代重构
本页是第二个动手实践环节，目标是引导学员通过编写迭代指令，亲手实践如何使用`return`语句来重构函数，使其职责更纯粹。

**核心要点**:
1. **迭代式开发**: 教学员通过追加需求的方式，对现有代码进行优化，体验“迭代开发”的过程。
2. **Prompt即算法**: 提供的Prompt范例通过分步指令，实际上是在用自然语言描述一个算法，潜移默化地培养学员的算法思维。
3. **埋下伏笔**: 最后的“思考题”引导学员思考重构带来的“职责”变化，为下一页升华到“单一职责原则”做铺垫。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 理论升华：单一职责原则
本页旨在将`return`的实践升华到软件设计的理论高度。通过引入“单一职责原则”和“纯函数”的概念，并借助“瑞士军刀 vs 扳手”的比喻，让学员理解代码质量的核心标准。

**核心要点**:
1. **理论联系实践**: 将刚才的重构实践与经典的“单一职责原则”联系起来，让学员知其然并知其所以然。
2. **引入高级概念**: 引入“纯函数”、“副作用”、“高内聚、低耦合”等专业术语（点到为止），拓展学员的知识边界。
3. **生动比喻**: “瑞士军刀 vs 扳手”的比喻，让“功能混杂”与“功能单一”的优劣对比一目了然。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 总结：盘点本节课收获
本页旨在通过结构化的清单和可视化的“宝箱”，为学员系统性地总结本节课在思维、工具和能力上的核心收获，强化其获得感。

**核心要点**:
1. **结构化总结**: 从“思想”、“操作”、“能力”三个维度进行总结，层次清晰。
2. **关键词强化**: 再次强调“封装”、“重构”、“架构师”等本节课的核心关键词。
3. **正向反馈**: 使用“宝箱”图片和积极的措辞，给予学员强烈的正向激励和满足感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 承前启后：预告“与AI结对调试”
本页作为课程结尾，核心是承上启下。通过提出“如果积木出错了怎么办？”这一新的痛点，自然地引出下一节课“调试”的主题，并预告新的角色升级（项目经理），激发学员的学习期待。

**核心要点**:
1. **制造新痛点**: 提出一个学员在实践中必然会遇到的现实问题——“代码出错”，从而创造学习新知识的内在需求。
2. **引出新主题**: 清晰地预告下一节课的主题是“与AI结对调试”。
3. **建立新期待**: 预告学员将要解锁“项目经理”这一新角色，维持课程的趣味性和学员的进阶动机。

</div>