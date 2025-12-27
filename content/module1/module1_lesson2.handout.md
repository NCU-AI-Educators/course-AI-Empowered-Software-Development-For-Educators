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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 从“观众”到“实践者”
欢迎来到第二节课！上一课，我们见证了AI的强大能力。从这一课开始，你将亲自体验如何驾驭这种能力。

本节课的核心任务是**环境搭建**。这是所有编程学习的起点，就像画家需要准备画板和颜料，作家需要准备纸和笔一样。我们将一步步在你的电脑上安装和配置所有必要的工具，为你后续的“创造”之旅铺平道路。

请跟随指引，保持耐心，准备好迎接你的第一个AI编程伙伴！

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 理解我们的四步计划
这四个步骤是精心设计的，旨在让你平滑地进入AI编程的世界。

1.  **安装 VS Code**: VS Code 是一个代码编辑器，但它远不止于此。它是一个高度可扩展的平台，我们将在这里编写指令、查看代码、运行程序。把它想象成你的“数字工作台”。(顺便一提，本课程所有教学材料都是用VS Code开发的，它在AI赋能之下，早已不只是一个编程工具了)
2.  **解锁“魔法控制台”**: “控制台”或“终端”是与计算机进行文本交互的强大工具。我们将在VS Code的集成终端中工作，这意味着我们不需要离开编辑器窗口就能向计算机下达命令。
3.  **召唤AI助手**: 我们将安装一个命令行工具，这就是我们的AI编程助手。它能理解我们的自然语言指令，并帮助我们完成各种任务。
4.  **体验“瞬间创造”**: 这是对我们整个安装过程的“验收测试”。我们将通过一个真实的例子，验证我们的环境是否搭建成功，并让你第一次体验到指挥AI创造的乐趣。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 详解“冒险地图”上的六个站点

这张地图是我们本节课的行动指南。
1.  **VS Code**: 我们的主工作区。
2.  **内置控制台**: 我们下达指令的地方。
3.  **Node.js**: 我们的AI助手是一个基于JavaScript的程序，Node.js就是让它能够在你的电脑上运行起来的“基础环境”。没有它，AI助手就无法“生存”。
4.  **Qwen Code**: 我们将要安装的AI助手的名字。
5.  **第一次施法**: 一个快速的、成就感满满的实践，让你立刻看到成果。
6.  **让AI指导安装Python**: 这是一个“元学习”任务。Python是我们课程后半段进行数据分析等任务的核心语言。但这次，我们不直接告诉你如何安装，而是让你练习使用刚刚安装好的AI助手，来教你如何完成这个任务。这能让你体会到AI作为“老师”和“向导”的价值。

</div>

---

## **第一站：安装你的“魔法工作室” (VS Code)**

Visual Studio Code (简称 VS Code) 是我们未来的“魔法工作室”和“代码编辑器”。几乎所有后续的创造都将在这里发生。

**任务：像安装普通软件一样安装它。**

1.  打开浏览器，访问官网: **`code.visualstudio.com`**
2.  网站会自动识别你的系统，点击巨大的蓝色下载按钮即可。
3.  运行你下载的安装包，一路点击“下一步”完成安装。
4.  **(Windows用户特别注意)** 在安装过程中，请确保勾选了所有“添加到PATH”和“通过‘使用Code打开’操作添加到...”相关的选项。

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是VS Code？为什么要勾选那些选项？

**Visual Studio Code (VS Code)** 是由微软开发的一款免费、开源、功能强大的代码编辑器。它之所以成为全球最受欢迎的开发工具，是因为：
- **轻量且快速**: 启动和运行都很快。
- **高度可扩展**: 拥有庞大的插件生态系统，可以通过安装插件来支持任何编程语言和工作流。我们后面安装AI助手，就是利用了它的扩展能力。
- **集成度高**: 自带了终端、调试器、Git版本控制等功能，提供了一站式的工作体验。

**为什么要勾选“添加到PATH”？**
- “PATH”是操作系统的一个“环境变量”，它记录了一系列文件夹的路径。当你在终端里输入一个命令（比如 `code`）时，系统会去PATH记录的所有路径里查找是否存在一个叫 `code` 的程序。
- 勾选“添加到PATH”，就相当于把VS Code的安装位置告诉了系统。这样，你就可以在任何终端里通过输入 `code` 命令来快速启动它，非常方便。

**为什么要勾选“通过‘使用Code打开’操作添加到...”？**
- 这会在你的文件或文件夹上右键时，出现一个“使用Code打开”的选项。这让你可以在文件管理器中快速地用VS Code打开一个项目，同样是为了提升效率。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 深入理解“集成终端”

**终端（Terminal）**，也被称为命令行、控制台或Shell，是计算机的一种用户界面。与我们习惯的图形界面（点鼠标、拖窗口）不同，终端允许你通过输入文本命令来直接与操作系统交互。它非常强大和高效，是专业开发者的必备工具。

**“集成”终端的优势在哪里？**
- **上下文统一**: 当你在VS Code中打开一个项目文件夹时，内置终端的默认路径就是这个项目文件夹。这意味着你输入的命令会直接作用于你的项目，避免了在不同文件夹之间切换的麻烦。
- **工作流闭环**: 想象一个场景：AI帮你生成了一个Python文件，你可以立刻在下方的终端里输入 `python a.py` 来运行它，如果出错了，你可以立刻在上面的编辑器里修改代码，然后再次在终端里运行。整个“编码-运行-调试”的循环都在一个窗口内完成，极大地提升了效率。
- **多终端管理**: VS Code允许你轻松地打开、命名和切换多个终端实例，方便同时处理不同的任务。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是Node.js？我们为什么需要它？

**JavaScript** 是一门最初为网页浏览器设计的编程语言，用于实现网页的动态效果和交互。在很长一段时间里，它只能在浏览器这个“沙盒”里运行。

**Node.js** 的诞生改变了这一切。它是一个开源的、跨平台的 **JavaScript 运行时环境**。简单来说，Node.js把JavaScript从浏览器中“解放”了出来，让它可以在任何地方（比如你的个人电脑、服务器）运行。

**我们为什么需要它？**
我们课程中使用的AI编程助手 `qwen-code`，本身就是一个用JavaScript编写的命令行工具。因此，为了让这个工具能在我们的电脑上运行，我们就必须先安装它的“生存环境”——Node.js。

**LTS vs. Current**
- **LTS (Long-Term Support)**: 长期支持版。这是官方推荐的稳定版本，经过了充分的测试，适合绝大多数用户和生产环境。
- **Current**: 最新功能版。它包含最新的功能，但可能不稳定，更适合想要尝鲜新特性的开发者。
对于学习和日常使用，**永远优先选择LTS版本**。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 拆解安装命令与授权流程

**`npm install -g @qwen-code/qwen-code@latest`**

这行命令由几个部分组成：
- **`npm`**: Node Package Manager (Node包管理器)。安装Node.js时会附带安装这个工具。它是世界上最大的软件注册表，你可以用它来下载和管理各种JavaScript工具和库。
- **`install`**: `npm`的一个命令，意为“安装”。
- **`-g`**: `install`命令的一个标志（flag），是 `--global` 的缩写。它告诉`npm`将这个包安装在系统级别的全局位置，而不是某个具体项目的文件夹里。这样，你就可以在任何地方的终端中使用这个工具。
- **`@qwen-code/qwen-code@latest`**: 这是我们要安装的包的名称和版本。`@qwen-code/qwen-code`是包名，`@latest`表示安装最新的版本。

**授权流程**
- 第一次运行 `qwen` 命令时，它需要知道你是谁，以便将你的使用情况与你的账户关联起来。
- 它采用的是一种安全、标准的 **OAuth** 授权流程。通过让你在浏览器中登录你的官方账户（例如阿里云账户）来确认身份，而不是让你在终端里输入密码。
- 授权成功后，`qwen`工具会在你的电脑上保存一个令牌（token），所以之后再使用就不需要重复登录了。

</div>

---

## **恭喜！你的AI编程助手已就位！**

**现在，它正在等待你的第一个指令...**

<div class="align-middle-center">

![一个终端窗口的特写，清晰地显示光标在闪烁的 `>` 提示符后 width:250px](../../../lectures/images/2025-10-26-00-33-06.png)

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### `>` 提示符的含义

当你成功激活并进入 `qwen` 工具后，终端的提示符会从常规的 `$` 或 `C:\>` 变为 `>`。

这个 `>` 提示符是 `qwen-code` 工具特有的交互界面，它告诉你：**“现在你不是在和普通的电脑终端对话，你正在和Qwen Code AI助手直接对话。”**

从现在开始，你在这个 `>` 后面输入的任何内容，都将作为“指令”（Prompt）发送给AI进行处理，而不是作为普通的系统命令来执行。

要退出这个AI对话模式，回到普通的终端，你可以随时按下 `Ctrl + C`。

</div>

---

## **第五站：第一次施法——体验瞬间创造！**

现在，让我们指挥AI助手，亲自施展第一节课里的一个魔法！

我们将命令它，从零开始，创造一个充满艺术感的“关系宇宙”动态网页，并保存成文件然后**自动打开它**。

![第一节课中展示的“关系宇宙”动态效果图 width:700px](../../../lectures/images/2025-10-25-16-31-11.png)

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么选择这个案例作为第一次实践？

选择“关系宇宙”作为你的第一个创造物，是基于以下考虑：
- **效果惊艳**: 它的视觉效果非常酷炫，能让你在第一时间感受到AI编程的魅力，获得强烈的成就感。
- **自包含**: 它不依赖任何外部图片或数据文件，所有代码都可以封装在一个HTML文件里，非常适合作为入门体验。
- **指令清晰**: 它的需求可以用纯粹的自然语言清晰地描述，是练习“Prompt编写”的绝佳范例。
- **即时反馈**: 最终产物是一个网页，可以直接在浏览器中看到结果，反馈非常直观。

这个练习的目的是让你相信：**只要环境搭建正确，你现在就已经具备了创造出惊艳作品的能力。**

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 剖析这个“魔法咒语”（Prompt）

这个Prompt是一个高质量指令的典范，让我们来剖析它的结构：
- **`# 任务`**: 用一句话概括核心目标，让AI立刻抓住主旨。
- **`## 核心愿景`**: 用描述性的语言描绘最终想要达到的“感觉”和“氛围”，这有助于AI在细节上做出更具创造性的决策。
- **`## 功能与设计要点`**: 这是Prompt的核心，将模糊的愿景拆解为具体、可执行的功能点。
  - **结构化**: 使用多级列表，让需求一目了然。
  - **精确化**: 尽量使用精确的词语（如“辉光效果”、“平滑、舒缓地移动”、“优雅地避开”），并给出量化参考（“间距小于100-150像素”）。
- **`## 技术要求`**: 设置明确的约束条件。这里要求“独立文件”和“原生实现”，排除了AI“偷懒”使用第三方库的可能，确保了结果的可控性。
- **`## 输出指令`**: 明确告知AI在完成代码编写后，还需要执行哪些“动作”（保存文件、打开文件）。这展示了AI助手作为“自动化工具”的能力。

**学习编写这样的Prompt，是本课程最重要的核心技能之一。**

</div>

---

## **见证你的魔法**

**1. 批准AI的操作**
   - 在执行创建文件、打开网页等操作前，负责任的AI助手会请求你的许可。
   - 当它询问时，请输入 `y` 然后按回车来批准它的计划。

**2. 欣赏你的作品**
   - 命令执行完毕后，你会发现AI不仅在VS Code左侧的文件浏览器中为你创建了 `particles.html` 文件...
   - ...它还会**自动在你的默认浏览器中打开这个网页**，让你即刻欣赏你的第一个作品！

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 理解“计划-批准”工作流

AI助手在执行任何可能影响你电脑文件的操作（如创建、修改、删除文件，或执行命令）之前，都会先向你展示一个**行动计划（Plan）**，并等待你的批准。这是一个至关重要的**安全机制**。

**为什么这个机制很重要？**
- **控制权在你**: 它确保了最终的控制权永远在你手中。AI只是一个提建议和执行的助手，你才是决策者。
- **防止意外**: 即使你给出的指令有歧义，或者AI的理解出现了偏差，这个“计划审查”环节也能让你在潜在的破坏性操作发生前，及时发现并中止它（通过输入`n`）。

**如何与它互动？**
- 当看到 `Continue with the current plan? (y/n)` 的提示时：
  - **`y`**: Yes，同意。AI将开始执行计划中的步骤。
  - **`n`**: No，不同意。AI将中止操作，等待你的下一个指令。你可以修改你的Prompt后重新提交。

**养成审查计划的习惯，是与AI安全、高效协作的第一步。**

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 复盘你的第一次创造

这次成功的实践，不仅仅是生成了一个好看的网页，它验证了我们整个工作流的正确性：
1.  **环境就绪**: 你的VS Code, Node.js, Qwen Code都已正确安装和配置。
2.  **AI可用**: AI助手能够正确接收你的指令，联网访问大模型，并返回结果。
3.  **指令有效**: 你给出的Prompt足够清晰，AI能够理解并将其转化为代码。
4.  **执行通路**: AI拥有执行文件操作和shell命令的权限，并能在你的批准下完成任务。

这是你迈出的第一步，但也是最重要的一步。它证明了你与AI之间的“沟通渠道”已经完全打通。接下来的所有学习，都将是探索如何更高效、更具创造性地使用这条通路。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI的第二重身份：你的专属老师

一个强大的AI助手，不仅能帮你“做事”，更能教你“如何做事”。这是AI赋能学习最核心的体现。

**为什么我们要这样做？**
- **培养核心能力**: 在快速发展的技术世界里，具体的技术（如某个软件的安装步骤）会不断变化，但“如何快速找到解决方案”的能力是永恒的。学会向AI提问，就是掌握了这种核心能力。
- **个性化指导**: AI可以根据你的具体情况（如操作系统版本）给出最适合你的、最新的指导。这比看一篇通用的、可能已经过时的博客文章要高效得多。
- **7x24小时可用**: 你的AI老师永远在线，你可以随时向它请教任何问题。

从这个任务开始，请逐渐养成一个习惯：**遇到问题时，先试着问问AI。**

</div>

---

## **核心任务：如何优雅地向AI提问？**

一个好的问题，是得到好答案的关键。请在VS Code的 `qwen` 提示符 `>` 后面，参考以下模板，输入你的问题：

**提问模板：**
> 我是一个编程初学者，请给我一份在我的 **[这里换成你的操作系统，例如：Windows 11 或 macOS]** 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。

**示例：**
`> 我是一个编程初学者，请给我一份在我的 Windows 11 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。`

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 优质提问（Prompt）的构成要素

向AI提问以解决问题时，一个优质的Prompt通常包含以下几个要素，这个模板就是它们的体现：

1.  **角色 (Persona)**: `我是一个编程初学者...`
    - 告诉AI它应该扮演什么角色来回答你，或者你是什么样的角色。这会影响AI回答的口吻、详略程度和侧重点。例如，对初学者的回答会更详细、更通俗。

2.  **上下文 (Context)**: `...在我的 Windows 11 / macOS 电脑上...`
    - 提供与问题相关的、具体的背景信息。对于技术问题，操作系统、软件版本、错误信息等都是至关重要的上下文。上下文越充分，AI的答案越精准。

3.  **任务 (Task)**: `...给我一份...安装Python的详细步骤。`
    - 明确、具体地说明你希望AI做什么。

4.  **格式/要求 (Format/Constraints)**: `...请确保这份指南对新手来说非常容易理解。`
    - 对AI的输出格式、风格或内容提出具体要求。例如，你可以要求它“用表格形式展示”、“提供代码示例”、“分步说明”等。

掌握这四个要素，你就能向AI提出绝大多数高质量的问题。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么“Add to PATH”如此重要？

我们再次强调这个问题，因为它是在Windows上安装命令行工具时最常见的“坑”。

想象一下你的电脑是一个大城市，各种程序（如`python.exe`, `node.exe`）是城市里的居民，他们住在不同的地址（安装路径）。
**PATH环境变量**就像是这个城市的“114查号台”。只有在查号台注册过的居民，你才能通过直呼其名（如在终端输入`python`）找到他。没有注册的，你就必须提供他的完整家庭住址（如`C:\Users\...\AppData\Local\Programs\Python\Python312\python.exe`）才能找到他，这显然非常麻烦。

勾选 **`Add Python to PATH`**，就是在安装时，自动把Python的“家庭住址”注册到“114查号台”上。

**如果忘记勾选了怎么办？**
- 别担心，这不是世界末日。你可以卸载Python后重新安装一遍，记得这次一定要勾选。
- 或者，你也可以手动去修改系统的环境变量设置，把Python的路径添加进去。具体步骤可以问你的AI助手：“我在安装Python时忘记勾选Add to PATH了，如何手动修复？”

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 理解验证过程

这个最终检查是在验证两个核心问题：
1.  **Python是否安装成功并被系统识别？**
    - `python --version` 命令会查找并执行`python`程序。如果系统能在`PATH`环境变量中找到它，就会运行它并打印出版本号。如果找不到，你就会看到 `command not found` 或类似的错误。
2.  **Node.js和Qwen Code是否仍然正常？**
    - `qwen --version` 命令同样是在验证`qwen`这个程序是否能被系统找到并执行。

**为什么需要重启VS Code？**
VS Code在启动时，会加载当前的系统环境变量。如果你在VS Code运行期间安装了新软件并修改了`PATH`，已经打开的终端实例是不会自动感知到这个变化的。关闭并重新启动VS Code，可以确保它加载最新的环境变量，从而能正确地找到你新安装的`python`。

**如果`python --version`成功，但`qwen --version`失败了怎么办？**
这通常意味着Node.js的安装或其`PATH`配置出了问题。你需要回头检查Node.js的安装步骤。同样，你可以向AI提问来寻求帮助。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 你在本节课的收获

这节课看似一直在“安装”，但实际上你已经收获了未来编程之路上最重要的几块基石：

1.  **一个现代化的开发环境 (VS Code)**: 你拥有了一个专业、高效、统一的工作平台。
2.  **与终端的初步接触**: 你已经克服了对命令行的恐惧，并学会了在其中执行基本命令。
3.  **包管理器的概念 (npm)**: 你理解了可以通过`npm`这样的工具来获取和安装社区提供的海量软件库。
4.  **环境变量PATH的初步理解**: 你知道了为什么有时需要重启终端，以及`Add to PATH`的重要性。
5.  **最重要的：利用AI解决问题的能力**: 你实践了如何通过向AI提问来解决一个真实的、具体的技术问题。

这些基础知识和技能，远比安装软件本身更有价值。它们是你未来能够独立探索和解决未知问题的基础。

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 如何面对和解决错误？

在编程世界里，遇到错误是常态，解决错误是成长的阶梯。

**`command not found` (找不到命令)**
- **核心原因**: 操作系统在`PATH`环境变量记录的所有路径下，都找不到你想要执行的那个程序。
- **排查步骤**:
  1.  **重启终端/VS Code**: 这是最简单、最优先的尝试。
  2.  **检查安装选项**: 回忆安装时是否勾选了`Add to PATH`。如果没有，最简单的办法是卸载重装。
  3.  **寻求AI帮助**: 可以向AI提问“如何在[我的系统]下，手动将[Python/Node.js]添加到环境变量PATH中？”

**`npm install` 报错**
- **核心原因**: `npm`需要从国外的服务器下载文件，网络连接可能不稳定或被限制。
- **排查步骤**:
  1.  **更换网络**: 尝试切换到手机热点或其他网络环境再试一次。
  2.  **配置镜像源**: 这是一个更稳定但稍复杂的方法。`npm`允许你将其下载服务器更换为国内的镜像服务器（如淘宝镜像），可以大大提高下载速度和成功率。你可以向AI提问：“如何为npm配置淘宝镜像源？”
  3.  **权限问题**: 在macOS或Linux上，有时全局安装需要管理员权限。可以尝试在命令前加上`sudo`，即 `sudo npm install -g ...`，然后输入你的电脑密码。

**最重要的心态：不要害怕错误信息。仔细阅读它，试着理解它，或者把它完整地复制下来，去问AI或向同学、老师求助。**

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 展望下一课：从“对话”到“创造”

本节课我们打通了与AI“对话”的渠道。下一节课，我们将学习如何让“对话”变得更高效、更有创造力。

**Prompt工程 (Prompt Engineering)**
- 这不是一门严谨的科学，更像一门与AI沟通的“艺术”。我们将学习如何组织我们的语言，运用角色扮演、提供示例、设置约束等技巧，来引导AI产出更符合我们预期的结果。

**实践项目：随机点名器**
- 这个项目将综合运用我们所学的知识。我们会指挥AI：
  1.  用HTML和CSS构建一个漂亮的网页界面。
  2.  用JavaScript编写随机抽取的逻辑。
  3.  让界面能够读取一个学生名单。
  4.  在点击按钮时，在屏幕上快速滚动名字，并最终停在一个幸运儿身上。

这将是你第一个完整的、可以拿去在真实场景中使用的“软件作品”。请保持期待！

</div>