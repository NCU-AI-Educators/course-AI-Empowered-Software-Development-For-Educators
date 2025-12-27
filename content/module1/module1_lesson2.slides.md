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

<!--
（音乐渐弱）
各位老师，大家好！欢迎回到我们的第二节课。
上一节课，我们进行了一场思想上的破冰，见证了AI编程的“魔法”。今天，我们将不再是观众，而是要亲自走向舞台，动手搭建我们自己的“魔法工作室”，并召唤出属于你的第一个AI编程助手。
-->

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

<!--
具体来说，我们今天的目标非常明确，浓缩为这四步。
首先，安装我们的“魔法工作室”——VS Code，这是我们未来所有创造的基地。
然后，解锁工作室里内置的“魔法控制台”，也就是终端，这是我们发号施令的地方。
接着，召唤出我们的专属AI编程助手。
最后，也是最激动人心的，我们将亲自指挥它，施展一次“瞬间创造”的魔法，完成从观众到魔法师的身份转变。
-->

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

<!--
为了让大家更清晰，我把今天的任务绘制成了一张‘冒险地图’。
它比上一页更详细，总共六个站点。前两步我们已经知道了。
第三步，我们需要为AI安装一个‘生存环境’，叫做Node.js。
第四步是召唤AI助手。
第五步是我们的第一次‘施法’，体验创造的乐趣。
最后，也是一个非常重要的核心任务，我们将不再依赖我给出的步骤，而是要学会让AI来指导我们安装课程所需的另一个核心软件——Python。
请大家跟紧节奏，我们一站一站地闯关。
-->

---

## **第一站：安装你的“魔法工作室” (VS Code)**

Visual Studio Code (简称 VS Code) 是我们未来的“魔法工作室”和“代码编辑器”。几乎所有后续的创造都将在这里发生。

**任务：像安装普通软件一样安装它。**

1.  打开浏览器，访问官网: **`code.visualstudio.com`**
2.  网站会自动识别你的系统，点击巨大的蓝色下载按钮即可。
3.  运行你下载的安装包，一路点击“下一步”完成安装。
4.  **(Windows用户特别注意)** 在安装过程中，请确保勾选了所有“添加到PATH”和“通过‘使用Code打开’操作添加到...”相关的选项。

<!--
好了，冒险开始！第一站，安装VS Code。
它将是我们未来8周课程的“家”，我们所有工作都会在这里进行。
请大家打开浏览器，在地址栏输入 `code.visualstudio.com`。
这个网站很智能，会自动识别你的电脑是Windows还是Mac，你只需要点击那个最显眼的蓝色下载按钮。
下载完成后，就双击运行它。安装过程和安装普通软件没什么区别，一路点击“下一步”或“同意”就可以。
这里要特别提醒一下Windows的老师们，在安装过程中，会有一个让你勾选的界面，请务必把所有和“PATH”以及“右键菜单”相关的选项都勾选上。这会为我们未来省去很多麻烦。
-->

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

<!--
好，安装完成后，请大家打开VS Code。
我们的第二站，就是要解锁工作室里的“魔法控制台”，它的官方名字叫“终端”。
请看顶部菜单栏，找到“终端(Terminal)”，然后点击“新建终端(New Terminal)”。
（稍作停顿，给学员操作时间）
大家会看到，屏幕下方弹出了一个面板，这里就是我们未来输入各种命令和“咒语”的地方。
为什么我们要用这个内置的终端，而不是用系统自带的呢？因为它提供了一种无缝的体验。你可以想象，未来我们在这里，上面写代码，下面输命令，左边看文件，所有操作都在一个窗口里完成，非常高效。
-->

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

<!--
第三站，我们需要为即将到来的AI助手安装一个“生存环境”。
我们的AI助手是用一种叫做JavaScript的语言编写的，而Node.js就是能让JavaScript在你的电脑上（而不仅仅是在浏览器里）运行起来的环境。
大家可以把它理解成一个游戏运行库，比如玩游戏需要安装DirectX一样。
请大家访问 `nodejs.org`。在首页，你会看到两个大大的绿色按钮。请务必选择左边的 **LTS** 版本。LTS代表“长期支持版”，它是最稳定、最推荐的版本。
下载后，同样是一路“下一步”完成安装。
最后，有一个非常重要的操作：安装完成后，请**完全关闭并重新启动VS Code**。这一步是为了让VS Code能识别到我们刚刚安装好的Node.js环境。
-->

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

<!--
好了，AI的生存环境已经就位。现在，万事俱备，只欠东风。我们可以正式召唤AI助手了。
请大家回到VS Code下方的终端。
然后，**完整地、一字不差地**复制我屏幕上的这行命令，粘贴到终端里，然后按下回车键。
（等待学员操作，观察是否有报错）
这行命令会通过Node.js的包管理器npm，从网上下载并安装qwen-code这个工具。`-g`的意思是全局安装，这样我们在任何地方都能使用它。
安装成功后，我们来激活它。在终端里输入 `qwen` 这四个字母，然后按回车。
这时，你的浏览器会自动弹出一个网页，提示你登录并授权。这是为了验证你的身份，让AI知道你是谁。请大家完成登录授权。
授权成功后，再回到VS Code的终端，你会发现，它已经准备好，在等待你的指令了。
-->

---

## **恭喜！你的AI编程助手已就位！**

**现在，它正在等待你的第一个指令...**

<div class="align-middle-center">

![一个终端窗口的特写，清晰地显示光标在闪烁的 `>` 提示符后 width:250px](../../../lectures/images/2025-10-26-00-33-06.png)

</div>

<!--
如果大家在终端里看到了这个大于号 `>` 提示符，并且光标在不停地闪烁，那么我非常高兴地宣布：你的AI编程助手已经成功就位！
它就像一个蓄势待发的精灵，已经准备好接收你的第一个指令了。
-->

---

## **第五站：第一次施法——体验瞬间创造！**

现在，让我们指挥AI助手，亲自施展第一节课里的一个魔法！

我们将命令它，从零开始，创造一个充满艺术感的“关系宇宙”动态网页，并保存成文件然后**自动打开它**。

![第一节课中展示的“关系宇宙”动态效果图 width:700px](../../../lectures/images/2025-10-25-16-31-11.png)

<!--
激动人心的时刻到了！第五站，第一次施法！
为了检验我们的工作室和AI助手是否一切正常，也为了让大家立刻体验到创造的乐趣，我们将亲自复现第一节课里那个充满艺术感的“关系宇宙”动态网页。
我们将命令AI，从一个空文件夹开始，为我们生成一个完整的HTML文件，并且在完成后自动用浏览器打开它。
-->

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

<!--
这就是我们的“施法咒语”，也就是我们给AI的指令——Prompt。
请大家**完整地**把它复制下来，然后粘贴到 `>` 提示符的后面，按下回车。
在AI开始工作之前，我们快速看一下这个Prompt。它写得非常详细，就像一份设计图纸。它定义了核心愿景、功能要点、技术要求，甚至最后明确指令AI要保存文件并打开它。
这就是我们未来与AI协作的核心模式：你负责思考和设计，AI负责实现。你的设计图纸越清晰，AI造出的房子就越符合你的预期。
好了，请大家按下回车，施展魔法吧！
-->

---

## **见证你的魔法**

**1. 批准AI的操作**
   - 在执行创建文件、打开网页等操作前，负责任的AI助手会请求你的许可。
   - 当它询问时，请输入 `y` 然后按回车来批准它的计划。

**2. 欣赏你的作品**
   - 命令执行完毕后，你会发现AI不仅在VS Code左侧的文件浏览器中为你创建了 `particles.html` 文件...
   - ...它还会**自动在你的默认浏览器中打开这个网页**，让你即刻欣赏你的第一个作品！

<!--
按下回车后，AI会开始思考，并很快给你一份它的行动计划。
你会看到它说：我准备创建一个叫 `particles.html` 的文件，然后用默认程序打开它。你同意吗？
这是一个非常好的安全习惯，一个负责任的AI在对你的电脑进行任何修改前，都会征求你的许可。
我们输入字母 `y`，然后按回车，批准它的操作。
（等待执行）
见证奇迹的时刻到了！你的浏览器是不是自动弹出来了？并且左边的文件列表里，是不是多了一个 `particles.html` 文件？
这就是你的第一个作品！
-->

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

<!--
请大家尽情欣赏浏览器里这个漂亮的动态网页。
这不是我给你的，也不是从网上下载的。这就是你，刚刚，亲手指挥AI，从零创造出来的第一个数字艺术品。
这个成功的体验证明了两件事：
第一，你的AI助手已经就位，它是一个能听懂复杂指令，并能直接动手的强大伙伴。
第二，也是最重要的，你已经掌握了，或者说即将掌握通过自然语言指挥AI完成创造的核心能力。
你不再是观众，你已经是创造者了。
-->

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

<!--
好的，庆祝过后，我们的冒险继续。第六站，也是我们今天最后一个核心任务。
刚才，我们体验了AI作为“创造者”和“执行者”的强大。接下来，我们要解锁它的另一个重要角色——作为“老师”和“向导”的智慧。
我们课程的后半部分需要用到Python这门编程语言。但这一次，我不会在屏幕上给出安装步骤。我希望大家学会利用你面前的AI编程助手，让它来告诉你该怎么做。
-->

---

## **核心任务：如何优雅地向AI提问？**

一个好的问题，是得到好答案的关键。请在VS Code的 `qwen` 提示符 `>` 后面，参考以下模板，输入你的问题：

**提问模板：**
> 我是一个编程初学者，请给我一份在我的 **[这里换成你的操作系统，例如：Windows 11 或 macOS]** 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。

**示例：**
`> 我是一个编程初学者，请给我一份在我的 Windows 11 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。`

<!--
那么，如何向AI提一个好问题呢？这本身就是一门艺术。一个好的问题，是得到好答案的关键。
请大家参考我屏幕上的这个提问模板。在向AI提问时，我们要提供几个关键信息：
首先，告诉它你的“角色”和“水平”——“我是一个编程初学者”。这能让AI调整它的语言，用更通俗易懂的方式来回答。
其次，提供你的“上下文环境”——“在我的Windows 11或macOS电脑上”。这能让AI给出针对性的、可操作的步骤。
最后，明确你对答案的“要求”——“请确保这份指南对新手来说非常容易理解”。
现在，请大家根据自己的电脑系统，修改并输入你的问题吧。
-->

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

<!--
好的，现在AI已经给了你一份为你量身定制的安装指南。
请大家仔细阅读它的回复，并跟随它的指引，一步一步地去操作。
你会发现，它给出的步骤非常清晰。它会告诉你去哪个官网下载，下载哪个版本。
并且，一个好的AI向导，一定也会像我一样，反复提醒你那个最重要的选项——在安装时，务必勾选 `Add Python to PATH`！
这个选项的意思，就是为Python在你电脑里“注册一个合法的身份”，让系统在任何地方都能找到它。
请大家开始操作，如果遇到任何问题，随时在群里提问。
-->

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

<!--
当你认为已经跟随AI的指引完成所有安装后，我们来进行最后一步的“总体验收”。
非常重要的一步：请再次**关闭并重新启动VS Code**。因为我们刚刚又安装了新的程序Python，需要重启来让终端环境刷新。
重启后，在VS Code里重新打开一个终端。注意，这次我们是在普通的终端（提示符是`$`或`C:\>`）里输入命令，而不是在`qwen`的`>`提示符里。
请依次输入这两个命令：`python --version` 和 `qwen --version`。
`--version`是查询版本号的意思。如果这两个命令都能成功地打印出类似我屏幕上的版本号信息，那就说明你的环境完全没问题了。
-->

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

<!--
如果你能成功地看到两个版本号，那么，我非常高兴地宣布：恭喜你！你的个人AI工作室，已经全面落成！
回顾一下，今天我们搭建了以VS Code为核心的工作室，掌握了召唤和指挥AI助手的方法，并且还在AI老师的指导下，安装了Python。
你已经完成了从零到一的全部准备工作，真正踏上了“AI赋能编程”的道路！为你自己鼓掌！
-->

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

<!--
当然，成为魔法师的路上总会有些小波折。在安装过程中遇到问题是非常正常的，请大家千万不要有挫败感。
最常见的问题就是，输入 `qwen` 或 `python` 后，电脑提示 `command not found`（找不到命令）。这99%的原因都是“环境变量PATH”没有设置对。要么是安装后没有重启终端，要么是安装Python时忘了勾选那个重要的选项。
另一个常见问题是 `npm install` 那一步报错，这通常是由于网络不稳定或者学校网络有防火墙限制。
这些都是小问题。我把它们称为“定心丸”，意思是告诉你，遇到这些问题很正常，你不是一个人。请不要慌张，把完整的错误信息截图发到我们的课程群里，我和助教随时会帮助大家解决。
-->

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

<!--
好了，今天的冒险就到这里。我们的工作室已经全面落成。
下一节课，我们将正式开始用它来创造。我们会深入学习与AI高效沟通的艺术——也就是如何写好Prompt。
同时，我们会做一个非常有趣、也非常实用的实践项目：指挥AI，从零开始，为我们创造一个可以直接在课堂上使用的、充满动感的“随机点名器”！
感谢大家的参与，我们下节课见！
-->