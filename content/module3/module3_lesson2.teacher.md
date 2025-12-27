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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 开场：成为AI的“项目经理”
本页作为课程开场，核心目标是点明本节课的核心技能——调试(Debugging)，并通过引入“项目经理”这一新的角色定位，将一个看似枯燥的技术活动包装成一次有趣的能力升级，从而激发学员的学习兴趣。

**核心要点**:
1. **点明主题**: 清晰地揭示本节课的主题是“与AI结对调试”。
2. **角色升级**: 引入“项目经理”的新角色，让学员对即将学习的技能有更高的价值认同。
3. **建立期待**: 预示着学员将从“使用者”升级为“管理者”，激发其学习动机。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 回顾痛点：当“积木”本身就是坏的
本页的核心目标是承上启下，通过重现上一节课结尾留下的“积木出错”这一痛点，来正式引入“Bug”和“错误信息”这两个核心概念，并为后续的“心态转变”教学环节做好心理铺垫。

**核心要点**:
1. **连接过去**: 紧接上一课的结尾，让课程内容衔接更紧密。
2. **引入概念**: 正式定义“Bug”和“错误信息”，让学员对要解决的问题有清晰的认知。
3. **引导思考**: 通过设问“是恐惧，放弃，还是挑战？”，引导学员初步思考如何面对错误，为下一页的“心态转变”做准备。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 设定目标：成为AI的“项目经理”
本页旨在明确本节课的核心学习目标与新的角色定位。通过将“调试”这一技术活动，包装成“项目管理”和“品控”的高阶能力，清晰地定义学员将获得的“阅读事故报告”和“指导AI修复”这两项核心能力，从而提升学员的学习价值感。

**核心要点**:
1. **能力升级**: 将“调试”重新定义为一项“元技能”，强调其重要性。
2. **角色重塑**: 提出“项目经理”或“品控主管”的新角色，让学员的自我认同从“执行者”转向“管理者”。
3. **明确产出**: 将学习目标分解为“阅读报告”和“指导修复”两个具体、可操作的能力点。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 心态转变：错误不是“失败”，而是“线索”
本页是进行调试教学前最重要的一步心理建设。核心目标是通过强烈的“心态对比”和生动的“比喻”，帮助学员克服对错误的本能恐惧和挫败感，建立积极、健康的调试心态。

**核心要点**:
1. **共情与破除**: 首先描述学员可能有的负面“本能反应”，引发共鸣，然后明确指出这是“最大心理障碍”，必须破除。
2. **重塑认知**: 将错误信息比作“求助信”和“线索”，将负面的“失败”感，转变为积极的“解谜”感。
3. **价值判断**: 明确指出“错误信息是通往解决方案的唯一线索”，提升其在学员心中的价值。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 案发现场：Python的“事故报告” (Traceback)
本页旨在正式引入Traceback，让学员对错误信息有一个初步的、具象的认识。核心是通过比喻和视觉呈现，降低学员对这堆“天书”的天然畏惧感。

**核心要点**:
1. **正式引入**: 给出错误信息的专有名称“Traceback”。
2. **比喻祛魅**: 将Traceback比作“事故报告”或“法医报告”，延续“侦探解谜”的课程叙事，使其显得不那么可怕。
3. **直面恐惧**: 直接展示一个真实的、看起来很吓人的Traceback截图，让学员直面它，然后立刻告诉他们“这可以被读懂”，帮助他们建立掌控感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 如何阅读“事故报告”：三步破案法
本页是本节课最核心的技能教学点，旨在教授学员一套阅读和理解Traceback的标准化方法。通过“三步破案法”，将看似无序的错误信息结构化，使其变得可读、可解。

**核心要点**:
1. **方法论**: 提出简单、易记的“三步破案法”（看最后、向上看、再向上看），并分别对应“What, Where, How”三个关键问题。
2. **可视化教学**: 在真实的Traceback截图上，通过高亮不同区域，直观地展示三个步骤分别对应哪些信息。
3. **翻译解读**: 对每个步骤提取出的信息，都用通俗易懂的“大白话”进行解读，帮助学员跨越专业术语的障碍。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 人机协作：AI侦探工作流
本页旨在建立一套与AI协作解决Bug的标准化流程。核心是让学员明白，他们不需要自己成为“侦探”，而是要学会如何高效地“报案”，将专业的工作交给AI。

**核心要点**:
1. **流程标准化**: 提出“AI侦探工作流”这一概念，并将其分解为“收集证据、报案、下达指令”三个简单、可执行的步骤。
2. **强调纪律**: 明确要求“完整地”复制和“原封不动地”粘贴错误信息，将其作为一项必须遵守的纪律，这是确保AI获得足够上下文的关键。
3. **角色定位**: 再次强化“报案人”和“总指挥”的角色，让学员明确自己在流程中的位置和职责。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### “报案模板”：如何向AI高效求助
本页旨在为学员提供一个高质量、可复用的调试Prompt模板。核心是教会学员，一个好的求助Prompt应该包含哪些要素，从而极大地提升AI回答的准确性和有效性。

**核心要点**:
1. **提供模板**: 给予一个结构清晰、可直接套用的“报案模板”，降低学员的提问门槛。
2. **结构化输入**: 模板包含“目标（上下文）”、“错误信息（证据）”、“分析请求（诉求）”三部分，这本身就是对高质量Prompt构成要素的一次教学。
3. **引导式提问**: 模板中的“分析请求”部分，被分解为三个具体问题（什么意思、哪里出错、如何修复），这会引导AI提供结构更清晰、内容更丰富的回答。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 动手环节(1/3)：布置“案发现场”
本页的核心是引导学员亲手、故意地制造一个Bug。这种“主动犯错”的体验，旨在帮助学员克服对程序错误的天然恐惧感，并为接下来的“侦破”环节准备好清晰的“案发现场”和关键证据（Bug）。

**核心要点**:
1. **主动犯错**: 让学员“故意”制造一个错误，将消极的“犯错”行为，转变为一次积极、可控的“实验”。
2. **清晰指引**: 提供非常清晰、简单的“制造Bug”的步骤，确保所有学员都能成功复现“案发现场”。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 动手环节(2/3)：触发“案件”并报案
本页旨在引导学员完整地实践“AI侦探工作流”的前半部分：获取错误信息，并使用标准模板向AI求助。这是将理论流程转化为核心实践能力的关键一步。

**核心要点**:
1. **获取证据**: 引导学员通过实际操作，获得一份真实、完整的Traceback“事故报告”。
2. **流程演练**: 让学员亲手实践“复制错误 -> 套用模板 -> 发送求助”的标准化报案流程。
3. **强化纪律**: 再次强调“完整地”复制错误信息的重要性。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 4分钟
### 动手环节(3/3)：审查报告并“结案”
本页是动手环节的收尾，核心是引导学员学会批判性地阅读AI的分析，并在多种解决方案中做出选择，最终验证修复，完成从“发现问题”到“解决问题”的完整闭环。

**核心要点**:
1. **培养批判性思维**: 引导学员审查AI报告，并思考不同解决方案（修正数据 vs. 防御性代码）的优劣，培养其决策能力。
2. **完成闭环**: 强调“采纳并验证”是必不可少的最后一步，让学员获得“成功破案”的成就感。
3. **引导深度思考**: 最后的“思考题”引导学员进行方案的权衡，这是一个更高层次的工程思维训练。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 角色升级：AI的“项目经理”
本页的核心目标是**点明并升华“一人分饰多角”的理念**，将之前课程中不断切换的角色统一为AI时代开发者的核心能力，并最终将学员的身份固化在最高阶的“项目经理”上。

**核心要点**:
1. **统一困惑**: 主动点出学员在角色切换中的困惑，并将其重新定义为一种高级能力，完成“Aha!”时刻的塑造。
2. **职责定义**: 清晰地定义了“项目经理”作为最高阶角色的三项核心价值：发现问题、定义问题、验证修复。
3. **强化新范式**: 再次强调“你负责规划，AI负责执行”的人机协作新范式，巩固学员的管理者身份认同。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 总结：盘点本节课收获
本页旨在通过结构化的清单和可视化的“宝箱”，为学员系统性地总结本节课在心态、技能、流程和角色上的核心收获，强化其获得感。

**核心要点**:
1. **多维度总结**: 从“心态”、“技能”、“流程”、“角色”四个维度进行总结，层次清晰，让学员的收获感更立体。
2. **关键词强化**: 再次强调“错误即线索”、“Traceback”、“AI侦探工作流”、“项目经理”等本节课的核心关键词。
3. **正向反馈**: 使用“宝箱”图片和积极的措辞，给予学员强烈的正向激励和满足感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 承前启后：预告“AI代码审查”
本页作为课程结尾，核心是承上启下。通过提出一个更深层次的、关于代码“质量”的新痛点，自然地引出下一节课“代码审查”的主题，并预告新的活动形式，激发学员的学习期待。

**核心要点**:
1. **制造新痛点**: 提出一个更高级的问题：“能跑”不等于“好”，将学员的关注点从“功能实现”引向“质量提升”。
2. **引出新主题**: 清晰地预告下一节课的主题是“AI代码审查 (AI Code Review)”，这是一个更高级的“品控”活动。
3. **建立新期待**: 通过设问，引出“判断好坏”、“寻求多种方案”、“重构”等下一节课的精彩看点，维持学员的学习热情。

</div>