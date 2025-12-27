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

<!--
各位老师好！欢迎来到我们模块三的第二节课。
在上一节课，我们学会了如何扮演“架构师”，用函数将代码封装成积木。今天，我们将再次迎来角色升级，学习一项在AI时代至关重要的人机协作技能——与AI结对调试。
我们将学习如何看懂程序出错时的“天书”，并从容地指挥AI去修复问题，从而真正成为AI开发团队的“项目经理”。
-->

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

<!--
让我们回顾一下上节课留下的那个悬念。
我们已经学会了如何创造和使用“功能积木”，也就是函数。
但是，一个非常严峻、也非常现实的问题摆在我们面前：如果AI给我们的，或者我们自己写的这个“积木”，它本身就是坏的、有缺陷的，该怎么办？
在编程的世界里，这种缺陷我们称之为“Bug”。当Bug发生时，程序往往会崩溃，并且在屏幕上打印出一堆像天书一样的“错误信息”。
我相信，这是所有编程初学者最恐惧的时刻。面对这些看不懂的红色文字，我们该怎么办？是感到挫败和恐惧，甚至放弃？还是，我们可以把它看作一次有趣的解谜挑战？
这节课，我们就来学习如何征服它。
-->

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

<!--
所以，我们这节课的目标，就是学习一项在AI时代至关重要的“元技能”——调试。
但请注意，我们的目标不是让大家成为传统的、需要逐行检查代码的“调试工程师”。我们的目标是再次升级，成为AI的“项目经理”或“品控主管”。
你将获得两项核心能力：
第一，学会阅读程序的“事故报告”。也就是那些错误信息。我们将学习如何像一个侦探一样，从里面提取出“哪里出错了”和“为什么出错”的关键线索。
第二，也是最重要的，学会指导你的“AI程序员”去修复问题。我们将学习如何把错误信息，翻译成清晰的指令，引导AI自己去定位和修复它写的Bug。
最终，你将不再畏惧任何错误，而是能从容地指挥AI解决任何问题。
-->

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

<!--
在学习具体技术之前，我们必须先完成一次最重要的、也是最困难的转变——心态的转变。
当看到程序报错时，我们很多人的本能反应是负面的：“天啊，我做错了什么？”“我把一切都搞砸了！”“我是不是不适合学编程？”……这种自我怀疑和挫败感，是成为优秀开发者的最大心理障碍。
从今天起，我希望大家能进行一次彻底的心态转变。你要告诉自己：程序报错，不是在“评判”我，不是在说我有多笨。它是在向我“求助”！程序在用它唯一会的、一种很笨拙的方式，告诉我：“主人，我在某个地方遇到了麻烦，我不知道该怎么办了，请帮帮我！”
所以，从现在开始，请把错误信息，看作是程序寄给你的“求助信”，是通往解决方案的、唯一的、宝贵的“线索”！
-->

---

## **案发现场：Python的“事故报告” (Traceback)**

当程序崩溃时，Python会打印一份详细的“事故报告”，我们称之为 **Traceback**。它看起来很吓人，但其实充满了破案的关键线索。

<div style="font-size: 0.7em; background-color: #1e1e1e; color: #d4d4d4; padding: 15px; border-radius: 5px; border: 1px solid #333;">
<pre><code>Traceback (most recent call last):
  File "C:/Users/Hawk/game.py", line 52, in &lt;module&gt;
    player_location = handle_go(command, world, player_location)
  File "C:/Users/Hawk/game.py", line 28, in handle_go
    new_location_data = world[new_location_id]
KeyError: 'market'</code></pre>
</div>

这就像一份**法医报告**，虽然专业，但只要掌握了阅读方法，就能快速定位“案发过程”和“致命伤”。

<!--
心态调整好了，我们现在就直面这个“案发现场”。
当Python程序崩溃时，它打印出来的这份详细的“事故报告”，有一个专业名称，叫做“Traceback”，翻译过来就是“回溯”或“追溯”。
我知道，它看起来很吓人，一堆英文，还有行号。但请相信我，它其实充满了破案的关键线索。
你可以把它想象成一份“法医报告”。虽然里面有很多专业术语，但只要我们掌握了阅读方法，就能从里面快速定位“案发过程”和“致命伤”。
-->

---

## **如何阅读“事故报告”：三步破案法**

面对一长串的Traceback，不要慌张。我们只需要像侦探一样，关注三个核心线索：

<div class="columns">
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

<!--
那么，这份“法医报告”到底该怎么读呢？非常简单，我们只需要用“三步破案法”。
第一步，**看最后一行**。这是最关键的，它告诉我们最终的“死因”是什么。这里是`KeyError: 'market'`。`KeyError`的意思是“钥匙错误”，说明我们想用一个叫`'market'`的钥匙，去查阅一个字典，但那个字典里没有这个钥匙。
第二步，**向上看一行**。这里定位了精准的“案发现场”。它告诉我们，事故发生在`game.py`文件的第28行，位于`handle_go`函数内部，出问题的就是这行代码`new_location_data = world[new_location_id]`。
第三步，**再向上看**。这里是追溯整个“调用链”，告诉我们这起“命案”是如何一步步发生的。报告显示，程序是从主程序的第52行，调用了`handle_go`函数，然后才在函数内部出了问题。
通过这三步，What, Where, How，整个案件的来龙去脉就一清二楚了。
-->

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

<!--
好，现在我们已经能读懂“法医报告”了。但记住，我们的角色是“项目经理”，不是“福尔摩斯”。我们不需要自己去破案。
我们要做的，是建立一套高效的、与我们的“AI侦探”协作的工作流程。
这个工作流非常简单，只有三步，但必须严格遵守：
第一步，保护现场，收集证据。也就是把终端里从`Traceback`开始到最后一行错误的所有内容，**完整地**复制下来。不要自己解读，不要只复制最后一行，要全部复制。
第二步，向“AI侦探”报案。把刚才复制的完整信息，**原封不动地**粘贴给你的AI助手。
第三步，清晰下达指令。使用我们接下来要讲的“报案模板”，告诉AI你需要它做什么。
记住这个流程，你就能调动AI的全部能力来为你服务。
-->

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

<!--
这是我们“AI侦探工作流”的第三步，也是最能体现你“项目经理”能力的一步：如何清晰地下达指令。
一个好的指令，也就是一个好的Prompt，应该包含三个部分。我们已经为大家准备好了一个万能的“报案模板”。
第一部分，“这是我的目标”。用一两句话告诉AI，你本来想做什么。这为AI提供了业务层面的上下文。
第二部分，“这是完整的错误信息”。把你刚才复制的Traceback原封不动地粘贴在这里。这是技术层面的核心证据。(如果你已经粘贴了错误信息，可以改成“前面是完整的错误信息”)
第三部分，“请帮我分析”。向AI提出具体、结构化的问题。不要只问“怎么办？”，而是引导它思考：这个错误在我的场景里是什么意思？根源可能在哪里？请给我具体的修复建议。
这个模板，能引导AI给出高质量、结构化的回答，而不是泛泛而谈。
-->

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
<div class="tip">

💡 **目的**：主动、可控地犯一次错，可以彻底消除对“不小心犯错”的恐惧。我们是在为“AI侦探”准备一个练手的靶子。
</div>
</div>

<!--
好了，理论和工具我们都掌握了。现在，进入动手实践环节！
我们将亲手制造一起“悬案”，然后指挥我们的“AI侦探”来侦破它。
第一步，布置“案发现场”。请大家打开上一节课我们重构好的游戏脚本，或者我们为大家准备的这节课初始版本。找到`world`字典里，‘guangchang’（扬州广场）的出口定义。我们故意把其中一个出口，比如东边的出口，从一个存在的地方，改成一个不存在的地点ID，比如`'market'`（市场）。我们的游戏世界里，并没有定义`market`这个地点。
大家可能会问，为什么要故意犯错？因为主动、可控地犯一次错，可以彻底消除我们对“不小心犯错”的恐惧。我们不是在搞破坏，我们是在为我们的“AI侦探”，精心准备一个练手的靶子。
-->

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

<!--
“案发现场”已经布置好了。现在，我们来触发它。
请大家运行你的游戏脚本。然后，输入指令`/go east`，尝试从扬州广场往东走，去那个我们刚刚捏造出来的、不存在的`market`。
你会观察到，程序“砰”的一声崩溃了，并且在终端里打印出了一长串红色的Traceback信息。这就是我们期待的、最关键的破案证据！
接下来，就进入我们的“AI侦探工作流”的报案环节。
第一，完整地复制所有错误信息。第二，打开你的AI助手。第三，套用我们刚才的“报案模板”，把你的目标（比如“我想让玩家能正常移动”）、以及完整的错误信息，都粘贴进去，然后发送给AI。
现在，就看我们的AI侦探如何表演了。
-->

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

<!--
好了，AI侦探已经给出了它的分析报告。现在，我们进入最后一步：审查报告，并“结案”。
请大家仔细阅读AI的解释。它有没有像我们刚才分析的那样，告诉你`KeyError`是什么意思？有没有指出问题的根源在于`'market'`这个地点不存在？
然后，重点看它给出的解决方案。它很可能会给出两种方案。方案A是“修正数据”，也就是让你去改`world`字典，把错误的数据改对。方案B是“增加防御性代码”，也就是在移动之前，先检查一下目标地点存不存在，如果不存在就不移动。
现在，请大家作为“品控主管”，思考一下，这两种方案，你觉得哪一种更好？为什么？
选择你认为更合适的方案，让AI帮你修改代码。然后，重新运行程序，再次尝试`/go east`，确认程序不会再崩溃了。这个确认修复的过程，我们就称之为“结案”。
-->

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

<!--
祝贺大家！通过刚才完整的“报案-破案-结案”过程，你们已经完成了又一次重要的角色升级。

你可能已经注意到，在这几节课里，我们不断地在切换角色：从设计功能的“架构师”，到寻找线索的“侦探”，现在又成为了“项目经理”。
但这并非混乱，这恰恰是AI时代开发的核心！在传统公司里，这些是不同的岗位，但在AI赋能的新模式下，我们一个人就能扮演所有角色。
今天，你通过定义问题、委派任务、验证修复，就在扮演这个团队中最高级的“项目经理”角色。我们的核心价值，不是深入细节修修补补，而是管理整个流程、把控最终质量。
在这个新的人机协作模式中，你负责出思想、定方向，而AI，则负责具体的执行。
-->

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

<!--
好了，我们来盘点一下本节课的收获。
今天，我们一起直面了编程中最令人畏惧，但也最有价值的部分——错误。
我们收获了一种全新的心态：错误即线索，不再恐惧，而是当作一次解谜游戏。
我们掌握了一项新技能：阅读Traceback，学会了三步破案法。
我们建立了一个新流程：AI侦探工作流，学会了如何高效地向AI“报案”。
最重要的是，我们解锁了一个新角色：项目经理。我们学会了如何报告问题和验证修复，将自己从一个程序的执行者，提升为了AI的管理者。
这些收获，都已放入你们的宝箱，请收好！
-->

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

<!--
我们已经学会了如何修复那些让程序“崩溃”的功能性Bug。
但是，作为一名追求卓越的“项目经理”，我们很快会遇到一个更隐蔽、也更高级的问题：
如果一段代码，它能正常运行，不报错，但就是写得非常糟糕，比如逻辑混乱、难以阅读、难以修改，我们该怎么办？
我们如何判断代码的“好”与“坏”？我们如何让AI给我们提供多种不同的、更优雅的解决方案？我们又如何指挥AI，把一段仅仅“能跑”的代码，重构成一段“优雅”的代码？
这就是我们下一节课要探讨的主题，一项更高级的“品控”技能——AI代码审查。我们下节课见！
-->