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
pre code {
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
![bg blur:3px brightness:60%](../../../lectures/images/2025-10-26-00-52-00.png)

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

# 模块一: AI编程新纪元 (思想破冰)
## 第2节课: 我的第一个AI编程助手

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场：承前启后
本页作为第二节课的开场，核心目标是“承前启后”，并为本节课的动手实践环节设定一个激动人心的基调。

**核心要点**：
1.  **回顾与衔接**: 通过提及上一课的“魔法”，快速唤醒学员的记忆，并将课程从“看”的阶段自然过渡到“做”的阶段。
2.  **设定本节课目标**: “我的第一个AI编程助手”这个标题直接点明了本节课的核心产出，让学员有明确的期待。
3.  **延续课程隐喻**: 继续使用“魔法工作室”、“召唤”等隐喻，保持课程叙事的一致性，将枯燥的环境安装过程包装成一次有趣的探险。

</div>

---

## **本节课目标：搭建你的AI工作室**

<div class="columns ratio-6-4">
<div>

本节课的目标，是搭建一个统一、高效的AI编程环境，完成从“观众”到“魔法师”的转变：

1.  **安装**你的“魔法工作室” (VS Code)。
2.  **解锁**内置的“魔法控制台”，体验无缝操作。
3.  **召唤**出你的专属AI编程助手。
4.  **指挥**它为你施展“瞬间创造”的魔法。

</div>
<div class="align-middle-center">

![一个从观众席走向舞台的魔法师隐喻图片 width:400px](../../../lectures/images/2025-10-26-00-21-55.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 目标拆解与动机激发
本页将本节课的宏大目标拆解为四个具体的、可执行的步骤，并用富有吸引力的动词（安装、解锁、召唤、指挥）来包装。

**核心要点**：
1.  **降低认知负荷**: 将复杂的环境搭建任务分解为四个清晰的步骤，让学员感觉目标明确、路径清晰。
2.  **激发内在动机**: “从观众到魔法师的转变”这一说法，旨在激发学员的身份认同感和成就动机。
3.  **建立预期**: 第四步“指挥它为你施展魔法”是一个强有力的“钩子”，它告诉学员，今天不仅仅是枯燥的安装，最后还有一个立竿见影的、充满成就感的实践环节，从而维持学员的注意力和期待感。

</div>

---

## **本节课的冒险地图**

<div class="columns ratio-6-4">
<div>

我们将按以下六步，完成这次探险：

1.  安装你的“魔法工作室” (VS Code)
2.  解锁内置的“魔法控制台”
3.  安装AI的“生存环境” (Node.js)
4.  召唤“AI编程助手” (Qwen Code)
5.  **第一次施法：体验瞬间创造！**
6.  核心任务：让AI指导你安装Python

</div>
<div class="align-middle-center">

![一张充满奇幻风格的冒险地图，包含六个标记点 width:400px](../../../lectures/images/2025-10-26-14-54-59.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供可视化路线图
这张“冒险地图”是本节课的详细议程。它比上一页的四步目标更具体，加入了Node.js和Python的安装环节。

**核心要点**：
1.  **可视化议程**: “冒险地图”的比喻和配图，将按部就班的安装流程变得生动有趣，符合课程的整体风格。
2.  **管理预期**: 清晰地列出所有六个步骤，让学员对本节课的工作量和流程有一个完整的预期。
3.  **引入“元学习”**: 第六步“让AI指导你安装Python”是一个关键的教学设计。它不仅仅是安装一个软件，更是让学员实践“如何利用AI来学习和解决问题”这一核心技能，是“授人以渔”的体现。

</div>

---

## **第一站：安装你的“魔法工作室” (VS Code)**

Visual Studio Code (简称 VS Code) 是我们未来的“魔法工作室”和“代码编辑器”。几乎所有后续的创造都将在这里发生。

**任务：像安装普通软件一样安装它。**

1.  打开浏览器，访问官网: **`code.visualstudio.com`**
2.  网站会自动识别你的系统，点击巨大的蓝色下载按钮即可。
3.  运行你下载的安装包，一路点击“下一步”完成安装。
4.  **(Windows用户特别注意)** 在安装过程中，请确保勾选了所有“添加到PATH”和“通过‘使用Code打开’操作添加到...”相关的选项。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 第一个动手任务：清晰、简单、有重点
这是学员的第一个动手任务，设计的核心是“零失败”和“防踩坑”。

**核心要点**：
1.  **简化指令**: 将任务类比为“安装普通软件”，降低学员的心理门槛。步骤清晰，指令明确（“巨大的蓝色下载按钮”）。
2.  **主动防错**: 明确指出Windows用户需要注意的关键选项（添加到PATH和右键菜单）。这是教学经验的体现，能主动避免后续90%的环境变量问题，极大提升课堂流畅度。
3.  **建立心智模型**: 将VS Code比喻为“魔法工作室”和“家”，强化其作为核心工作区的心智模型。

</div>

---

## **第二站：解锁内置的“魔法控制台”**

现在，启动你刚刚安装的VS Code。这里就是我们的大本营。

**1. 如何进入？**
   - 在VS Code的顶部菜单栏，选择 `终端(Terminal)` -> `新建终端(New Terminal)`。
   - 屏幕下方会弹出一个面板，这就是我们的“内置魔法控制台”。

**2. 为什么用它？**
   - **无缝体验**：代码在上，命令在下，无需切换窗口。
   - **所见即所得**：AI在左侧生成文件，你立刻就能在右侧看到，并在下方终端里运行它。

**从现在开始，我们所有的“咒语”都在这里输入。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引入核心工具：集成终端
本页的目的是引导学员熟悉VS Code的集成终端，并理解其优势。

**核心要点**：
1.  **清晰的操作路径**: `终端 -> 新建终端`，指令明确，易于跟随。
2.  **阐述“为什么”**: 明确解释使用集成终端的两个核心优势（“无缝体验”和“所见即所得”），而不是仅仅告知“如何做”。这有助于培养学员对“高效工作流”的认知。
3.  **建立操作习惯**: “从现在开始，我们所有的‘咒语’都在这里输入”这句话，是在为学员建立一个贯穿整个课程的核心操作习惯。

</div>

---

## **第三站：为AI安装“生存环境” (Node.js)**

<div class="columns ratio-6-4">
<div>

我们的AI编程助手是用特殊的“基因”(JavaScript)编写的，它需要一个量身打造的“生存环境”才能运行。Node.js就是这个“栖息地”。

**任务：像安装普通软件一样安装它。**

1.  打开浏览器，访问官网: **`nodejs.org`**
2.  在首页，选择并下载 **LTS (长期支持版)**。
3.  运行你下载的安装包，一路点击“下一步”完成安装。
4.  **重要**：安装完成后，**重启VS Code**，让新环境生效。

</div>
<div class="align-middle-center">

![Node.js官网首页截图，并高亮LTS版本下载按钮 width:400px](../../../lectures/images/2025-10-26-00-30-17.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引入依赖项：Node.js
本页引入了第一个外部依赖项Node.js。教学设计的重点是解释“为什么需要它”并给出明确的操作指引。

**核心要点**：
1.  **生动的类比**: 将Node.js类比为“生存环境”或“游戏运行库”，让零基础学员能直观地理解其作用，而不是陷入技术细节。
2.  **明确的选择**: 强调选择“LTS”版本，避免学员因选择错误版本而导致后续问题。这是一个重要的实践指导。
3.  **关键操作提醒**: 再次强调“重启VS Code”。这是环境安装中最常见的一个“坑”，主动、反复地提醒可以有效避免学员受挫。

</div>

---

## **第四站：召唤你的AI编程助手 (Qwen Code)**

<div class="columns ratio-6-4">
<div>

“生存环境”已就位，现在可以在VS Code的集成终端中召唤AI编程助手了！

**1. 安装指令**
   - 在VS Code下方的**集成终端**中，**完整地复制**以下命令，粘贴后按回车：
     ```bash
     npm install -g @qwen-code/qwen-code@latest
     ```

**2. 授权激活**
   - 安装成功后，在终端里输入 `qwen` 并按回车。
   - 浏览器会自动打开，提示你登录并授权。
   - 授权成功后，回到VS Code的终端...

</div>
<div class="align-middle-center">

![一个从电脑屏幕中浮现出的友好AI助手形象 width:400px](../../../lectures/images/2025-10-26-00-31-49.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 核心工具安装与激活
这是本节课最核心的安装步骤。设计的重点是指令的精确性和对过程的解释。

**核心要点**：
1.  **强调精确性**: 反复强调“完整地复制”，因为命令行对字符非常敏感，任何微小的错误都可能导致失败。
2.  **解释命令含义**: 简单解释 `npm install -g` 的含义（通过npm包管理器进行全局安装），对命令进行“祛魅”，让学员知道这行神秘代码大致在做什么。
3.  **分步指导**: 将过程清晰地分为“安装”和“授权激活”两步，并解释了授权的原因（验证身份），让整个流程逻辑清晰。

</div>

---

## **恭喜！你的AI编程助手已就位！**

**现在，它正在等待你的第一个指令...**

<div class="align-middle-center">

![一个终端窗口的特写，清晰地显示光标在闪烁的 `>` 提示符后 width:250px](../../../lectures/images/2025-10-26-00-33-06.png)

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 里程碑与正向反馈
这是一个简短但重要的过渡页，用于庆祝一个关键里程碑的达成。

**核心要点**：
1.  **明确的成功标志**: 将“看到 `>` 提示符”定义为成功的标志，给学员一个清晰的、可验证的检查点。
2.  **给予正向反馈**: “恭喜！”和“已就位！”等积极的措辞，给予学员及时的正向反馈，增强其成就感。
3.  **营造期待感**: “等待你的第一个指令...”这句话，自然地将学员的注意力引向下一个更激动人心的环节。

</div>

---

## **第五站：第一次施法——体验瞬间创造！**

现在，让我们指挥AI助手，亲自施展第一节课里的一个魔法！

我们将命令它，从零开始，创造一个充满艺术感的“关系宇宙”动态网页，并保存成文件然后**自动打开它**。

![第一节课中展示的“关系宇宙”动态效果图 width:700px](../../../lectures/images/2025-10-25-16-31-11.png)

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 实践环节：连接过去，创造未来
这是本节课的第一个“爽点”，其核心目标是让学员在完成枯燥的安装后，立刻获得一个巨大、炫酷、正向的反馈。

**核心要点**：
1.  **连接过去**: 复现第一节课的案例，能让学员产生“原来那个魔法我真的可以做到”的感受，形成完美的体验闭环。
2.  **明确任务**: 任务描述非常具体：“创造一个...动态网页”、“保存成文件”、“自动打开它”。这让学员对即将发生的事情有清晰的预期。
3.  **视觉吸引力**: “关系宇宙”这个案例本身具有很强的视觉吸引力，作为第一个实践项目，能给学员带来巨大的成就感。

</div>

---

<style scoped>
pre {
  font-size: 1rem;
}
</style>

## **施法咒语 (The Prompt)**

请**完整复制**下面的“魔法咒语”，它包含了“做什么”和“如何做”的完整指令。然后，粘贴到VS Code中 `qwen` 终端的 `>` 提示符后面，按回车。

<pre style="white-space: pre-wrap; margin: 0; padding: 1em; background-color: #f5f5f5; border-radius: 5px; overflow-wrap: break-word; overflow-x: auto; font-size: 14px"><code>
# 任务：创建具备科技美感的交互式粒子背景

## **核心愿景**
我需要一个独立的HTML文件，用于呈现一个充满未来感和科技感的动态粒子宇宙。它应该是一个视觉上引人入胜的全屏背景，能够优雅地响应用户的交互。

## **功能与设计要点**
- **整体外观**:
    - **背景**: 纯黑色全屏画布，无边距或滚动条。
    - **粒子效果**: 粒子应为白色，并带有**辉光/发光效果** (glowing effect)，使其在黑色背景上显得明亮而柔和。
    - **动态感**: 粒子需要**平滑、舒缓地**在画布内随机移动，而不是快速、生硬地跳动。

- **核心交互逻辑**:
    - **粒子连接**: 当粒子彼此靠近时（例如，间距小于100-150像素），在它们之间绘制一条**半透明的、有渐变效果**的线条。距离越近，线条越亮；距离越远，线条越暗，直至消失。
    - **鼠标交互**: 当鼠标在画布上悬停时，周围的粒子应**优雅地避开**鼠标指针，形成一个可见的“力场”或排斥圈。这个交互应该是流畅的，而不是突然的。

## **技术要求**
- **独立文件**: 所有代码（HTML, CSS, JavaScript）必须封装在**一个文件**中。
- **原生实现**: **禁止**使用任何外部JavaScript库或CSS框架（如jQuery, p5.js, three.js等），请使用原生的Canvas API。

## **输出指令**
- 将最终的完整代码保存为一个名为 `particles.html` 的文件。
- 接着打开这个文件，让我能看到运行的效果。
</code></pre>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 示范“高质量Prompt”
本页不仅是让学员复制粘贴，更是一次关于“如何编写高质量Prompt”的隐性教学。

**核心要点**：
1.  **提供范本**: 这个结构清晰、内容详尽的Prompt本身就是一个极佳的教学范例。
2.  **拆解Prompt结构**: 教师在逐字稿中，会引导学员快速浏览Prompt的结构（愿景、功能、技术、输出），让他们初步理解一个好Prompt的构成要素。
3.  **强化核心理念**: 再次强调“你负责设计，AI负责实现”的核心协作模式，并将Prompt比喻为“设计图纸”，加深学员的理解。
4.  **明确的行动指令**: “完整复制”、“粘贴到...后面，按回车”，指令简单直接，确保学员能成功操作。

</div>

---

## **见证你的魔法**

**1. 批准AI的操作**
   - 在执行创建文件、打开网页等操作前，负责任的AI助手会请求你的许可。
   - 当它询问时，请输入 `y` 然后按回车来批准它的计划。

**2. 欣赏你的作品**
   - 命令执行完毕后，你会发现AI不仅在VS Code左侧的文件浏览器中为你创建了 `particles.html` 文件...
   - ...它还会**自动在你的默认浏览器中打开这个网页**，让你即刻欣赏你的第一个作品！

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引导“人机交互”并验证结果
本页指导学员完成与AI的关键交互（批准计划），并引导他们验证操作结果。

**核心要点**：
1.  **解释“批准”行为**: 将AI的请求许可解释为“负责任的”、“好的安全习惯”，而不是一个麻烦。这在教学初期就为学员建立了正确的“人机协作安全观”。
2.  **指导验证**: 清晰地告诉学员需要观察两个地方的成功标志：VS Code左侧出现文件，以及浏览器自动打开。这让成功变得具体、可衡量。
3.  **营造高潮**: “见证奇迹的时刻”等措辞，将这个普通的技术步骤渲染得充满仪式感和成就感。

</div>

---

## **你，刚刚，创造了它！**

<div class="columns ratio-6-4">
<div>

浏览器中出现的，就是你亲手指挥AI创造的第一个数字艺术品。

这证明了：
- 你的AI助手是一个能听懂指令、并能直接动手的强大伙伴。
- **你，即将掌握通过自然语言指挥AI完成创造的核心能力。**

</div>
<div class="align-middle-center">

![“关系宇宙”网页在浏览器中全屏运行的惊艳截图 width:400px](../../../lectures/images/2025-10-26-00-34-35.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 强化成就与升华意义
本页是“第一次施法”环节的总结和升华，目标是最大化地强化学员的成就感和自信心。

**核心要点**：
1.  **归因于学员**: 强调“你，刚刚，创造了它”，将这份成就感完全归属于学员本人，而不是工具。
2.  **升华能力**: 将这次成功的实践，从“完成了一个小练习”拔高到“证明了你即将掌握核心能力”的层面，赋予其更深远的意义。
3.  **强化身份转变**: 再次强调“你已经是创造者了”，巩固学员的自我认同，为后续更难的学习任务注入强大的心理动力。

</div>

---

## **第六站：让AI指导你安装Python**

<div class="columns ratio-6-4">
<div>

刚才，我们体验了AI作为“创造者”的强大。接下来，我们将体验它作为“老师”的智慧。

**任务：** 我们不再提供Python的安装步骤，而是要让你面前的AI编程助手告诉你该怎么做。

</div>
<div class="align-middle-center">

![一个友好的机器人老师正在指向Python的Logo width:400px](../../../lectures/images/2025-10-26-00-36-17.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引入“元学习”任务
本页引入了一个新的学习维度：利用AI进行学习（元学习）。这是比利用AI进行创造更高阶的能力。

**核心要点**：
1.  **角色转换**: 明确提出AI的“老师”角色，拓展学员对AI应用的想象力，让他们意识到AI不仅是工具，更是学习伙伴。
2.  **从“喂饭”到“觅食”**: 教学方式从教师“给予”步骤，转变为学员“索取”步骤。这是一个关键的转变，旨在培养学员主动使用AI解决问题的能力和习惯。
3.  **任务明确**: 任务非常具体——“让AI告诉你该怎么做”，简单而清晰。

</div>

---

## **核心任务：如何优雅地向AI提问？**

一个好的问题，是得到好答案的关键。请在VS Code的 `qwen` 提示符 `>` 后面，参考以下模板，输入你的问题：

**提问模板：**
> 我是一个编程初学者，请给我一份在我的 **[这里换成你的操作系统，例如：Windows 11 或 macOS]** 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。

**示例：**
`> 我是一个编程初学者，请给我一份在我的 Windows 11 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。`

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教授“提问的艺术”
本页是“元学习”任务的具体方法论指导。它没有直接给答案，而是给出了一个“渔”——提问的模板。

**核心要点**：
1.  **提供模板**: 对于初学者，直接让他们开放式提问可能会导致低效。提供一个结构化的模板，可以极大地提升他们首次提问的成功率和答案质量。
2.  **拆解模板要素**: 逐字稿中拆解了模板的三个核心要素（角色、上下文、要求），这实际上是在教授Prompt Engineering的基本原则，让学员知其然，并知其所以然。
3.  **鼓励个性化**: 模板中留出了 `[你的操作系统]` 这个需要学员自己填充的部分，鼓励他们将模板应用于自己的实际情况。

</div>

---

## **核心任务：跟随AI向导，完成安装**

<div class="columns ratio-6-4">
<div>

现在，请仔细阅读AI给你的回复，并跟随它的指引一步步操作。

它会告诉你：
- 去哪个网站下载 (python.org)
- 下载哪个版本
- **安装时务必勾选 `Add Python to PATH`**

**“Add to PATH”** 这个选项非常重要，它的意思是“在你的电脑里注册Python”，这样你在任何地方呼唤 `python`，电脑都能找到它。

</div>
<div class="align-middle-center">

![Python在Windows上安装过程的截图，并用红色方框高亮“Add Python to PATH”复选框 width:400px](../../../lectures/images/2025-10-26-00-37-38.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 监督执行与再次强调
本页的目的是让学员在AI的指导下独立完成任务，同时教师再次强调最关键的步骤，作为“双重保险”。

**核心要点**：
1.  **信任AI**: 引导学员“仔细阅读AI给你的回复”，建立对AI指导能力的信任。
2.  **关键点二次确认**: 教师再次口头和视觉上（通过截图）强调 `Add Python to PATH` 的重要性。这种“AI说一遍，老师再说一遍”的重复，能最大程度地确保学员不会漏掉这个关键步骤。
3.  **提供支持**: “遇到问题随时提问”为学员提供了安全网，让他们可以放心地进行尝试。

</div>

---

## **最终检查：验证你的工作室**

当你跟随AI的指引完成所有操作后，我们需要进行最终检查。

**重要：请先关闭并重新启动VS Code。** (这样才能让它内置的终端识别到新安装的Python)

然后，在VS Code中重新打开一个集成终端，依次输入以下两个命令：

```bash
$ python --version
# 预期输出: Python 3.x.x (类似的版本号)

$ qwen --version
# 预期输出: @qwen-code/cli/1.x.x (类似的版本号)
```

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### “验收”环节：提供明确的成功标准
这是本节课的最后一步操作，目标是提供一个清晰、可量化的成功标准，来检验整个环境搭建的成果。

**核心要点**：
1.  **再次强调重启**: 第三次强调“重启VS Code”，因为这是从安装Python到验证Python能否被识别的关键一步。
2.  **明确的验证命令**: 提供了两个简单、明确的验证命令 `... --version`。
3.  **清晰的预期输出**: 给出了每个命令的预期输出格式，让学员可以轻松地判断自己是否成功。
4.  **区分终端模式**: 提醒学员这次是在普通终端而不是qwen终端里输入命令，这是一个重要的细节，避免学员混淆。

</div>

---

## **恭喜！你的AI工作室已全面落成！**

<div class="columns ratio-7-3">
<div>

如果你能成功看到两个版本号，那么恭喜你，你已经：
- ✅ 搭建了以VS Code为核心的“魔法工作室”。
- ✅ 掌握了在集成终端中召唤并指挥AI助手。
- ✅ 在AI老师的指导下，完成了所有核心工具的安装。

你已经真正踏上了“AI赋能编程”的道路！

</div>
<div class="align-middle-center">

![一个庆祝性的图片，上面有“工作室落成”的字样和Python、AI助手的Logo width:400px](../../../lectures/images/2025-10-26-00-38-58.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 总结与庆祝
本节课的收尾页，核心是总结学员的成就，并给予最热烈的祝贺，最大化他们的成就感。

**核心要点**：
1.  **总结成就**: 用三个“✅”清晰地总结了本节课的核心产出和学员掌握的技能，让他们对自己的收获一目了然。
2.  **正向激励**: “恭喜！”、“全面落成！”、“真正踏上...道路！”等强有力的正面词汇，给予学员积极的心理暗示。
3.  **视觉化庆祝**: 使用带有庆祝元素的图片，在视觉上强化这种积极的情绪。

</div>

---

## **常见问题与定心丸**

<style scoped>
section::before {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 56%;
  height: 100%;
  background-image: url(../../../lectures/images/2025-10-26-00-40-41.png);
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  opacity: 0.2;
}
</style>

**“咒语”无效？别担心，这是成为魔法师的必经之路！**

*   **问题1: 输入 `qwen` 或 `python` 后，提示 `command not found`？**
    *   **原因**: 主要是“环境变量PATH”没设置对。最常见的情况是：
        1.  安装程序后没有**重新打开**一个新的终端窗口。
        2.  安装Python时，忘记勾选 `Add Python to PATH`。
    *   **定心丸**: 这是最常见的问题。请先尝试重开终端。

*   **问题2: 安装过程（尤其是`npm install`那一步）报错？**
    *   **原因**: 通常是网络问题或电脑权限不足。
    *   **定心丸**: 这同样很常见。请把完整的错误信息截图发到群里！

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 故障排除与心理按摩
这是一个非常重要的“兜底”页面，目标是预判学员可能遇到的问题，并提前给予心理疏导和解决方案。

**核心要点**：
1.  **预判问题**: 列出了两个最可能发生的错误（`command not found` 和 `npm` 报错），显示了教师的经验，能让遇到问题的学员感觉“老师懂我”。
2.  **分析原因**: 简单分析了问题产生的最常见原因，授人以渔。
3.  **提供“定心丸”**: “别担心”、“必经之路”、“这很常见”等话语，是在为学员做“心理按摩”，极大地缓解了他们遇到错误时的焦虑和挫败感。
4.  **明确求助路径**: “把完整的错误信息截图发到群里”提供了一个清晰、可执行的求助方式。

</div>

---

## **下一步预告**

<div class="columns ratio-6-4">
<div>

工作室已经建成，下一节课，我们将正式开始“创造”。

- **学习目标**: 掌握与AI高效沟通的艺术——Prompt工程。
- **实践项目**: 指挥AI从零创造你的第一个**可视化教学应用**——一个可以直接在课堂上使用的、充满动感的“随机点名器”！

</div>
<div class="align-middle-center">

![一个动态随机点名器应用的GIF或静态截图 width:400px](../../../lectures/images/2025-10-26-01-01-15.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 课程预告与“钩子”
本节课的结尾，需要一个清晰的预告和有吸引力的“钩子”，来激发学员对下一节课的期待。

**核心要点**：
1.  **明确学习目标**: 清晰地指出下一课的理论学习目标是“Prompt工程”，让学员知道要学什么。
2.  **设置实践项目**: “随机点名器”是一个完美的项目：
    - **实用性强**: 每个老师都能用得上。
    - **趣味性高**: “充满动感”的描述和视觉展示很有吸引力。
    - **难度适中**: 适合作为第一个完整的、从零开始的项目。
3.  **保持期待**: 用一个吸引人的项目作为预告，是维持学员学习动力的有效手段。

</div>