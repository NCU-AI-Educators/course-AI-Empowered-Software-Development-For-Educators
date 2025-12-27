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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-21-14-20-34.png)

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
## 第10节课: 与AI结对调试——成为AI的“项目经理”

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 调试在软件开发中的位置
**调试 (Debugging)** 是识别、定位和修复软件中错误（即“Bug”）的过程。它是软件开发生命周期（Software Development Life Cycle, SDLC）中不可或缺的一环。

一个典型的编程流程是“编码 -> 测试 -> 调试”的循环。程序员编写代码实现功能，测试人员（或程序员自己）验证功能是否符合预期。一旦发现不符合预期的行为（Bug），调试就开始了。

在AI辅助开发的时代，这个流程并未改变，只是每个环节的角色发生了变化。AI可以极大地加速“编码”和“调试”环节，但“测试”（发现问题）和“定义问题”（向AI准确描述问题）的责任，更多地落在了人类开发者身上。本节课学习的，正是如何高效地与AI协同完成“调试”这个关键环节。

</div>

---

## **回顾：当“积木”本身就是坏的**

<div class="columns ratio-6-4">
<div style="font-size: 0.9em;">

在上一节课，我们学会了用“函数”来封装代码，将程序重构得清晰、优雅。

我们学会了创造和使用“功能积木”。

但是，一个严峻的问题摆在我们面前：

**如果AI给我们的“积木”（函数），本身就是坏的、有缺陷的，该怎么办？**

当程序因为一个未知的错误（我们称之为“**Bug**”）而崩溃时，屏幕上会打印出一堆天书般的“**错误信息**”。

我们该如何面对它？是恐惧，放弃，还是将它看作一次解谜的挑战？

</div>
<div class="align-middle-center">

![一个完好的积木和一个破碎的积木并列，形成对比 width:400px](../../../lectures/images/2025-11-21-14-32-37.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Bug, Error, Failure
在软件工程中，这三个词有细微但重要的区别：
- **错误 (Error)**: 指的是程序员在编码过程中犯下的一个具体错误。例如，在字典中写错了一个键名，或者在计算时用错了公式。这是导致问题的“**因**”。
- **缺陷 (Defect / Bug)**: 指的是由于“错误”而存在于软件内部的、潜在的、未被发现的问题。它就像一个埋在代码里的“地雷”。
- **失效 (Failure)**: 指的是当程序运行时，这个“缺陷”被触发，导致程序产生了不符合预期的行为（例如程序崩溃、计算结果错误等）。这是用户能观察到的“**果**”。

我们的任务，就是根据“失效”的现象（如程序崩溃），去反向追踪，定位并修复那个最初的“错误”。这个过程，就是调试。

</div>

---

## **本节课目标：成为AI的“项目经理”**

本节课，我们将学习一项在AI时代至关重要的“元技能”：**调试 (Debugging)**。

但我们不是要成为传统的“调试工程师”，而是要升级为AI的“**项目经理**”或“**品控主管**”。

### **你的新能力：**
1.  **阅读“事故报告”**
    - 学会从Python的错误信息（Traceback）中，像侦探一样提取出“**哪里出错了**”和“**为什么出错**”的关键线索。
2.  **指导“AI程序员”修复**
    - 学会如何将错误信息转化为清晰的指令，**引导AI定位并修复它自己写的Bug**。

**最终，你将不再畏惧任何错误信息，而是能从容地指挥AI解决问题。**

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 根本原因分析 (Root Cause Analysis)
调试的核心，不仅仅是“修复Bug”，更是进行“**根本原因分析 (RCA)**”。

一个Bug的表象（失效）和其根本原因（错误）可能相距甚远。例如：
- **表象 (Symptom)**: 程序在运行时，因为`KeyError`而崩溃。
- **直接原因 (Direct Cause)**: 试图访问一个不存在的字典键。
- **根本原因 (Root Cause)**: 可能是数据输入时就错了，也可能是之前的逻辑计算错了，还可能是两个模块的接口定义不一致。

一个优秀的开发者或项目经理，不会满足于仅仅修复直接原因（例如，用一个`if`语句简单地跳过错误），而是会刨根问底，找到并修复根本原因，以防止同类问题再次发生。我们向AI提问时，也应该引导它进行更深层次的根本原因分析。

</div>

---

## **心态转变：错误不是“失败”，而是“线索”**

<div class="columns ratio-6-4">
<div style="font-size: 0.9em;">

在面对程序错误时，人类的本能反应是：
- “我做错了什么？”
- “我把一切都搞砸了！”
- “我不适合学编程...”

**这是成为优秀开发者的最大心理障碍。**

我们需要一次彻底的**心态转变**：
> 程序错误，不是对你个人能力的“**评判**”，而是程序写给你的一封“**求助信**”。它在用自己唯一的方式，笨拙地告诉你：“我在某某地方遇到了麻烦，请帮帮我！”

**错误信息，不是“失败”的标志，而是通往解决方案的“线索”。**

</div>
<div class="align-middle-center">

![一个沮丧的人和一个充满好奇心的侦探，对比两种心态 width:400px](../../../lectures/images/2025-11-21-14-34-27.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 成长型心态与编程
本页倡导的，是心理学家卡罗尔·德韦克提出的“**成长型心态 (Growth Mindset)**”。
- **固定型心态 (Fixed Mindset)**: 认为人的智力、能力是固定不变的。遇到错误时，会认为“我不擅长这个”，并倾向于放弃。
- **成长型心态 (Growth Mindset)**: 认为人的能力可以通过努力和学习来提升。遇到错误时，会将其视为一次学习和成长的机会。

编程，特别是调试，是锻炼“成长型心态”的最佳实践之一。因为在编程世界里，犯错是常态，从错误中学习是进步的唯一途径。每一次成功调试，都是一次“我的能力得到了提升”的直接反馈，能极大地强化成长型心态。将调试看作解谜游戏，而非对个人能力的审判，是保持学习热情和韧性的关键。

</div>

---

## **案发现场：Python的“事故报告” (Traceback)**

当程序崩溃时，Python会打印一份详细的“事故报告”，我们称之为 **Traceback**。它看起来很吓人，但其实充满了破案的关键线索。

<div style="font-size: 0.6em; background-color: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 5px; border: 1px solid #333;">
<pre><code>Traceback (most recent call last):
  File "C:/Users/Hawk/game.py", line 52, in &lt;module&gt;
    player_location = handle_go(command, world, player_location)
  File "C:/Users/Hawk/game.py", line 28, in handle_go
    new_location_data = world[new_location_id]
KeyError: 'market'</code></pre>
</div>

这就像一份**法医报告**，虽然专业，但只要掌握了阅读方法，就能快速定位“案发过程”和“致命伤”。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 调用栈 (Call Stack)
要理解Traceback，首先要理解“**调用栈**”的概念。

程序在调用函数时，会像堆盘子一样，把函数调用信息一层层地往上堆。例如，主模块调用了`handle_go`函数，这个“调用栈”看起来就是：
```
| handle_go |  <-- 栈顶 (当前正在执行)
|-----------|
|   主模块   |  <-- 栈底
+-----------+
```
当`handle_go`函数内部发生崩溃时，Python会把整个“调用栈”的情况，**按照代码的执行顺序（从最初的调用开始）**，原封不动地打印出来，形成我们看到的Traceback。

这份报告的**打印顺序**是“**从栈底到栈顶**”的：
- Traceback的**最上方**，是程序执行的**起点**（栈底）。
- Traceback的**最下方**，是导致崩溃的**终点**（栈顶）。

因此，我们推荐的**阅读方法**正好相反，采用“**从下往上**”的侦探式读法，因为最关键的线索（“致命伤”和“案发现场”）都在报告的最底部。

Traceback的最后一行，即`KeyError: 'market'`，就是导致程序崩溃的那个异常（Exception）。

</div>

---

## **如何阅读“事故报告”：三步破案法**

面对一长串的Traceback，不要慌张。我们只需要像侦探一样，关注三个核心线索：

<div class="columns styled-div" style="font-size: 0.7em;">
<div>

<div style="font-size: 0.7em; background-color: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 5px; border: 1px solid #333;">
<pre><code>Traceback (most recent call last):
  File "C:/Users/Hawk/game.py", line 52, in &lt;module&gt;
    player_location = handle_go(command, world, player_location)
  File "C:/Users/Hawk/game.py", line 28, in handle_go
    <span style="background-color: rgba(255, 255, 0, 0.2);">new_location_data = world[new_location_id]</span>
<span style="background-color: rgba(255, 0, 0, 0.3);">KeyError: 'market'</span></code></pre>
</div>

1.  **看最后一行：确定“死因” (What)**
    - `KeyError: 'market'`
    - **解读**：最致命的伤口是`KeyError`，说明我们试图用一个不存在的“钥匙” (`'market'`)去查阅一个字典。

</div>
<div style="font-size: 0.85em;">

2.  **向上看一行：定位“案发现场” (Where)**
    - `File "game.py", line 28, in handle_go`
    - `new_location_data = world[new_location_id]`
    - **解读**：事故直接发生在`game.py`文件的第28行，位于`handle_go`函数内部。

3.  **再向上看：追溯“调用链” (How)**
    - `File "game.py", line 52, in <module>`
    - `player_location = handle_go(...)`
    - **解读**：程序是从第52行调用`handle_go`函数时，才引发了这起“命案”的。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 常见Python异常类型
Traceback的最后一行被称为“**异常 (Exception)**”。学会识别常见的异常类型，能帮助你更快地定位问题。
- **`KeyError`**: 试图访问字典中不存在的键。
- **`IndexError`**: 试图访问列表中不存在的索引（例如，列表长度为3，你却试图访问第5个元素）。
- **`NameError`**: 使用了一个未被定义的变量名。
- **`TypeError`**: 对一个变量执行了它不支持的操作（例如，尝试将一个数字和一个字符串相加）。
- **`ValueError`**: 传递给函数的参数类型正确，但值不合适（例如，`int('abc')`）。
- **`AttributeError`**: 试图访问一个对象不存在的属性或方法（例如，一个列表变量没有`.keys()`方法）。
- **`FileNotFoundError`**: 试图打开一个不存在的文件。

当你遇到不认识的异常类型时，直接将它复制粘贴问AI，是最高效的学习方法。

</div>

---

## **人机协作新模式：AI侦探工作流**

<div class="columns ratio-6-4">
<div style="font-size: 0.85em;">

我们不需要自己成为“福尔摩斯”。我们只需要扮演好“**报案人**”和“**总指挥**”的角色。

面对任何错误，都严格遵守以下“**AI侦探工作流**”：

1.  **保护现场，收集证据**
    - **完整地**复制从`Traceback`开始到最后一行错误信息的所有内容。不要遗漏，也不要自己解读。

2.  **向“AI侦探”报案**
    - 将完整的错误信息，**原封不动地**粘贴给你的AI助手。

3.  **清晰下达指令**
    - 使用我们为你准备的“报案模板”，清晰地提出你的诉求。

</div>
<div class="align-middle-center">

![一个侦探拿着放大镜，旁边是一个AI机器人助手正在分析线索 width:400px](../../../lectures/images/2025-11-21-14-36-39.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 上下文的重要性
为什么“完整地”和“原封不动地”复制Traceback如此重要？因为Traceback为AI提供了解决问题所需的**完整上下文**。

- **`KeyError: 'market'`** 告诉AI问题是“键错误”。
- **`new_location_data = world[new_location_id]`** 告诉AI这个键错误发生在哪段代码。
- **`handle_go`** 告诉AI这段代码属于哪个函数。
- **`player_location = handle_go(...)`** 告诉AI这个函数是在哪里被调用的。

缺少任何一环，AI都可能无法准确地定位问题。例如，如果你只告诉AI“我遇到了一个KeyError”，它可能会给出一个非常笼统的、与你游戏逻辑无关的回答。只有提供了完整的Traceback，AI才能像一个真正的“侦探”一样，掌握全部线索，从而给出精准的分析和解决方案。

</div>

---

## **“报案模板”：如何向AI高效求助**
<div style="font-size: 0.82em;">

向AI求助时，提供**上下文**和**清晰的问题**至关重要。你可以套用以下模板：

> **报案模板 (Prompt Template):**
>
> 你好，我的Python程序崩溃了。
>
> **这是我的目标：**
> （简单描述你本来想做什么，例如：“我正在写一个文本游戏，想实现玩家从A点移动到B点的功能。”）
>
> **这是完整的错误信息：**
> ```
> (在此处粘贴你复制的完整Traceback)
> ```
>
> **请帮我分析：**
> 1.  这个错误`KeyError: 'market'`在我的游戏场景里，具体代表什么意思？
> 2.  根据错误信息，问题的根源最可能出在哪段代码？
> 3.  请给我一个修复这个问题的具体代码建议。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 专业的Bug报告
这个“报案模板”实际上是一个简化版的、专业的“**Bug报告**”。在真实的软件开发团队中，测试人员或用户提交的Bug报告通常包含以下要素：
- **标题 (Title)**: 简明扼要地描述问题。
- **复现步骤 (Steps to Reproduce)**: 清晰地描述如何一步步地触发这个Bug。我们的“目标”描述和代码上下文起到了类似的作用。
- **预期行为 (Expected Behavior)**: 描述在这些步骤下，程序本应该如何表现。
- **实际行为 (Actual Behavior)**: 描述程序实际上是如何表现的（例如，程序崩溃，并附上完整的错误信息）。
- **环境 (Environment)**: 描述问题发生时的环境（如操作系统、软件版本等）。

学会编写包含清晰上下文、预期和实际结果的Prompt，不仅能让你更高效地与AI协作，也能让你在未来与人类同事协作时，成为一个更受欢迎的、更专业的团队成员。

</div>

---

## **动手环节(1/3)：布置“案发现场”**
<div style="font-size: 0.88em;">

现在，让我们亲手制造一起“悬案”，并指挥我们的“AI侦探”来侦破它。

### **第一步：布置“案发现场” (制造Bug)**
1.  打开我们上一节课的游戏脚本。
2.  在`world`字典中，找到一个地点的`exits`出口定义。
3.  **故意**将其中一个出口的目的地，改成一个**不存在**的地点ID。
    ```python
    'guangchang': {
        'description': '这里是扬州广场...',
        # 将'chaguan'改成一个不存在的'market'
        'exits': {'east': 'market'}, 
        'items': [...]
    },
    # (我们的world里并没有'market'这个地点)
    ```
<div class="tip" style="font-size: 0.6em;">

💡 **目的**：主动、可控地犯一次错，可以彻底消除对“不小心犯错”的恐惧。我们是在为“AI侦探”准备一个练手的靶子。
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 调试的“消防演习”
我们“故意”制造一个Bug，这个行为在教学和训练中具有深刻的意义。我们可以把它理解为一次调试的“**消防演习 (Fire Drill)**”。

进行消防演习的目的，不是因为真的发生了火灾，而是在一个安全、可控的环境下，预演和练习标准的应急处理流程（例如，如何找到并跑到安全出口）。这样，当真正的火灾发生时，我们才不会惊慌失措。

同理，我们在这里故意制造一个可预期的、简单的Bug，就是为了进行一次“调试演习”。通过这次演习，我们熟悉了“警报”（Traceback）响起时的标准应对流程（观察信息、复制信息、向AI求助）。

当未来我们真的在自己的项目中遇到意料之外的“火情”（真正的Bug）时，我们就能凭借这次演练的经验，从容不迫地应对，而不是手足无措。

</div>

---

## **动手环节(2/3)：触发“案件”并报案**

“案发现场”已经布置完毕，现在我们来触发它，并正式向“AI侦探”报案。

### **第二步：触发“案件”**
1.  运行你的游戏脚本。
2.  输入指令，尝试从“扬州广场”向东走 (`/go east`)。
3.  **观察**：程序崩溃，并打印出一长串`Traceback`信息。这是破案的关键证据！

### **第三步：向“AI侦探”报案**
1.  **完整地**复制终端里所有的`Traceback`错误信息。
2.  启动AI助手。
3.  套用我们刚才学习的“**报案模板**”，将你的目标和完整的错误信息粘贴进去，然后发送。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 复现Bug的重要性
我们刚才做的“触发案件”的步骤，在专业术语中叫做“**复现Bug (Reproduce a Bug)**”。

能够稳定地复现一个Bug，是成功修复它的前提。如果一个Bug只是偶尔出现，无法找到必现的触发路径，那么定位和修复它将变得极其困难。

一个好的Bug报告，其核心价值就在于提供了一套清晰、可靠的“复现步骤”。它能让接手这个问题的开发者（无论是人类还是AI）在自己的环境中，百分之百地重现问题发生时的场景，从而为分析和调试提供了坚实的基础。

</div>

---

## **动手环节(3/3)：“结案”并思考**
<div style="font-size: 0.95em;">

AI侦探已经提交了它的分析报告，现在轮到我们扮演“品控主管”的角色，来审查并做出决策。

### **第四步：审查“AI侦探”的报告**
1.  **阅读AI的解释**：它是否清晰地告诉你`KeyError`意味着你尝试访问一个不存在的字典键？它是否指出了问题在于`'market'`这个ID在`world`字典里找不到？
2.  **审查AI的解决方案**：AI可能会提出几种修复方案：
    - **方案A (修正数据)**：建议你将`'market'`改回一个存在的地点，或者在`world`里新增一个`'market'`地点。
    - **方案B (增加防御性代码)**：建议在尝试访问`world[new_location_id]`之前，先用`if new_location_id in world:`来检查一下该地点是否存在。
3.  **采纳并验证**：选择你认为更合适的方案，指挥AI（或自己动手）修改代码，然后重新运行，确认Bug已被修复。这个过程，我们称之为“**结案**”。

**思考：** 方案A和方案B，哪一种更好？为什么？
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 防御性编程 (Defensive Programming)
AI给出的方案B，体现了一种重要的编程思想——“**防御性编程**”。

它的核心思想是：**不信任任何来自外部的数据**。函数的编写者应该假定所有传入的参数都可能是无效的、错误的，并编写代码来处理这些异常情况，以保证程序在任何情况下都不会崩溃。

- **方案A (修正数据)**: 治标不治本。它只修复了当前这一个数据错误。如果未来因为其他原因，又出现了一个指向不存在地点的出口，程序依然会崩溃。
- **方案B (增加防御性代码)**: 从根本上解决了问题。它为`handle_go`函数增加了一层“装甲”，使得无论数据如何错误，该函数本身都足够健壮（Robust），不会再因为同样的原因而崩溃。

在大多数情况下，**增加防御性代码（方案B）是比仅仅修正当前数据（方案A）更优秀、更专业的解决方案**。它提升了代码的“**健壮性 (Robustness)**”。

</div>

---

## **你的新角色：AI的“项目经理”**

<div class="columns ratio-6-4">
<div style="font-size: 0.78em;">

祝贺你！通过刚才的“破案”过程，你已经完成了又一次重要的**角色升级**。

你不再是那个面对错误手足无措的“学徒”，而是升级成为了AI开发团队的“**项目经理 (Project Manager)**”或“**品控主管 (QA Lead)**”。

**你的核心价值在于：**
- **发现并报告问题**：在程序运行中发现不符合预期的行为（Bug）。
- **定义问题**：将模糊的“程序出错了”，转化为包含清晰上下文和错误信息的“**Bug报告**”。
- **验证修复**：在AI“程序员”提交修复后，负责测试和验证问题是否已真正解决。

你负责**把控质量、管理流程**，而AI负责**具体执行**。

</div>
<div class="align-middle-center">

![一个项目经理在白板前，向一个AI机器人团队分配任务和审查进度 width:400px](../../../lectures/images/2025-11-21-14-38-04.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI时代的全能开发者：一人身兼多职
你可能已经注意到，在这门课程中，我们不断地为你赋予新的角色：从最初的“魔法师”，到后来的“架构师”，再到本节课的“项目经理”和“品控主管”。你可能会感到困惑：我到底是谁？

这正是本课程希望传达的核心思想。在传统的大型软件开发团队中，项目经理（PM）、架构师、程序员、测试工程师（QA）等角色的确是由不同的人承担的。

但是，**AI赋能的软件开发，催生了一种全新的、更高效的“一人团队”模式**。特别是对于我们教学和科研中所需的不那么复杂的软件项目，你和你的AI助手，完全可以共同承担以上所有角色：
- 当你思考如何用函数组织代码时，你就是**架构师**。
- 当你发现并报告Bug时，你就是**品控主管 (QA)**。
- 而当你定义问题、向AI委派修复任务、并最终验证结果时，你就在扮演**项目经理**的角色。

所以，角色的切换并非混乱，**这正是AI时代开发者的核心能力：根据任务的不同，灵活地切换自己的角色，并主导整个人机协作的流程**。“项目经理”是我们现阶段最重要的角色，因为它代表了最高层级的管理和规划能力。

</div>

---

## **本节总结：我们获得了什么？**

<div class="columns ratio-6-4">
<div style="font-size: 0.78em;">

在本节课，我们直面了编程中最令人畏惧、却也最有价值的部分——**错误**。

- **一种新心态：错误即线索**
  - 我们克服了对错误信息的恐惧，学会了将其视为解决问题的宝贵线索。

- **一项新技能：阅读Traceback**
  - 掌握了从Python“事故报告”中提取“死因”、“地点”、“过程”的三步破案法。

- **一个新流程：AI侦探工作流**
  - 建立了一套标准的、高效的、与AI协作解决Bug的流程。

- **一个新角色：项目经理**
  - 你学会了如何“报告问题”和“验证修复”，将自己从“执行者”提升为了“**管理者**”。

</div>
<div class="align-middle-center">

![一个宝箱，里面装着侦探帽、放大镜和一个项目管理看板的图标 width:400px](../../../lectures/images/2025-11-21-14-39-21.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 调试的价值
调试不仅仅是修复错误，它还有更深远的价值：
1.  **加深对代码的理解**: 调试过程会迫使你去阅读和理解那些你平时可能一扫而过的代码，让你真正搞懂程序的运行机制。
2.  **提升代码质量**: 在修复Bug的过程中，你往往会发现代码中其他潜在的问题或可以改进的地方，从而进行重构，提升整体代码质量。
3.  **锻炼逻辑思维**: 调试是一个纯粹的逻辑推理过程，需要你根据已有的线索（Traceback、程序行为）进行假设、验证、排除，是锻炼分析和解决问题能力的最佳方式。

可以说，一个程序员的成长，很大程度上是由他调试过的Bug的数量和难度决定的。

</div>

---

## **下一步预告：当代码“能跑”，但“不好”**

<div class="columns ratio-6-4">
<div style="font-size: 0.88em;">

我们已经学会了如何修复那些让程序“崩溃”的**功能性Bug**。

但是，还存在另一种更隐蔽的问题：

**如果一段代码能够正常运行，没有报错，但它写得非常糟糕——难以阅读、难以修改、效率低下——我们该怎么办？**

- 我们如何判断一段代码的“好”与“坏”？
- 我们如何让AI为同一个问题，提供多种不同的解决方案，并向我们解释其优劣？
- 我们如何指挥AI，将一段“能跑”的代码，**重构**为一段“优雅”的代码？

下一节课，我们将学习一项更高级的“品控”技能：**AI代码审查 (AI Code Review)**。

</div>
<div class="align-middle-center">

![两段功能相同但风格迥异的代码并列，一段混乱，一段整洁 width:400px](../../../lectures/images/2025-11-21-14-40-44.png)
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 功能性需求 vs. 非功能性需求
软件开发中的需求，通常分为两类：
- **功能性需求 (Functional Requirements)**: 定义了系统“**做什么**”。例如，“程序在输入`/go east`后，玩家应该移动到东边的房间”。我们之前修复的Bug，就属于功能性需求未被满足的情况。
- **非功能性需求 (Non-functional Requirements)**: 定义了系统“**应该如何是**”。它描述的是系统的质量属性，而不是具体功能。例如：
  - **可读性 (Readability)**: 代码应该易于理解。
  - **可维护性 (Maintainability)**: 代码应该易于修改和扩展。
  - **性能 (Performance)**: 程序响应应该足够快。
  - **健壮性 (Robustness)**: 程序在遇到异常输入时，不应该崩溃。

下一节课我们要学习的“代码审查”，其核心就是检查代码在满足“功能性需求”的同时，是否也满足了重要的“非功能性需求”。

</div>