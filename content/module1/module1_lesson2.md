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

---

## 本节课目标：搭建你的AI工作室

<div class="columns ratio-6-4">
<div>

本节课的目标，是搭建一个统一、高效的AI编程环境，完成从“观众”到“魔法师”的转变：

1.  **安装**你的“魔法工作室” (VS Code)。
2.  **解锁**内置的“魔法控制台”，体验无缝操作。
3.  **召唤**出你的专属AI编程助手。
4.  **指挥**它为你施展“瞬间创造”的魔法。

</div>
<div class="align-middle-center">

![一个从观众席走向舞台的魔法师隐喻图片 height:400px](../../../lectures/images/2025-10-26-00-21-55.png)

</div>
</div>

---

## 本节课的冒险地图

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

![一张充满奇幻风格的冒险地图，包含六个标记点 height:400px](../../../lectures/images/2025-10-26-14-54-59.png)

</div>
</div>

---

## 第一站：安装你的“魔法工作室” (VS Code)

Visual Studio Code (简称 VS Code) 是我们未来的“魔法工作室”和“代码编辑器”。几乎所有后续的创造都将在这里发生。

**任务：像安装普通软件一样安装它。**

1.  打开浏览器，访问官网: **`code.visualstudio.com`**
2.  网站会自动识别你的系统，点击巨大的蓝色下载按钮即可。
3.  运行你下载的安装包，一路点击“下一步”完成安装。
4.  **(Windows用户特别注意)** 在安装过程中，请确保勾选了所有“添加到PATH”和“通过‘使用Code打开’操作添加到...”相关的选项。

---

## 第二站：解锁内置的“魔法控制台”

现在，启动你刚刚安装的VS Code。这里就是我们的大本营。

**1. 如何进入？**
   - 在VS Code的顶部菜单栏，选择 `终端(Terminal)` -> `新建终端(New Terminal)`。
   - 屏幕下方会弹出一个面板，这就是我们的“内置魔法控制台”。

**2. 为什么用它？**
   - **无缝体验**：代码在上，命令在下，无需切换窗口。
   - **所见即所得**：AI在左侧生成文件，你立刻就能在右侧看到，并在下方终端里运行它。

**从现在开始，我们所有的“咒语”都在这里输入。**

---

## 第三站：为AI安装“生存环境” (Node.js)

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

![Node.js官网首页截图，并高亮LTS版本下载按钮 height:400px](../../../lectures/images/2025-10-26-00-30-17.png)

</div>
</div>

---

## 第四站：召唤你的AI编程助手 (Qwen Code)

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

![一个从电脑屏幕中浮现出的友好AI助手形象 height:400px](../../../lectures/images/2025-10-26-00-31-49.png)

</div>
</div>

---

## 恭喜！你的AI编程助手已就位！

**现在，它正在等待你的第一个指令...**

<div class="align-middle-center">

![一个终端窗口的特写，清晰地显示光标在闪烁的 `>` 提示符后 height:250px](../../../lectures/images/2025-10-26-00-33-06.png)

</div>

---

## 第五站：第一次施法——体验瞬间创造！

现在，让我们指挥AI助手，亲自施展第一节课里的一个魔法！

我们将命令它，从零开始，创造一个充满艺术感的“关系宇宙”动态网页，并保存成文件然后**自动打开它**。

![第一节课中展示的“关系宇宙”动态效果图 height:300px](../../../lectures/images/2025-10-25-16-31-11.png)

---

## 施法咒语 (The Prompt)

请**完整复制**下面的“魔法咒语”，它包含了“做什么”和“如何做”的完整指令。然后，粘贴到VS Code中 `qwen` 终端的 `>` 提示符后面，按回车。

```
# 任务：创建具备科技美感的交互式粒子背景

## 核心愿景
我需要一个独立的HTML文件，用于呈现一个充满未来感和科技感的动态粒子宇宙。它应该是一个视觉上引人入胜的全屏背景，能够优雅地响应用户的交互。

## 功能与设计要点
- **整体外观**:
    - **背景**: 纯黑色全屏画布，无边距或滚动条。
    - **粒子效果**: 粒子应为白色，并带有**辉光/发光效果** (glowing effect)，使其在黑色背景上显得明亮而柔和。
    - **动态感**: 粒子需要**平滑、舒缓地**在画布内随机移动，而不是快速、生硬地跳动。

- **核心交互逻辑**:
    - **粒子连接**: 当粒子彼此靠近时（例如，间距小于100-150像素），在它们之间绘制一条**半透明的、有渐变效果**的线条。距离越近，线条越亮；距离越远，线条越暗，直至消失。
    - **鼠标交互**: 当鼠标在画布上悬停时，周围的粒子应**优雅地避开**鼠标指针，形成一个可见的“力场”或排斥圈。这个交互应该是流畅的，而不是突然的。

## 技术要求
- **独立文件**: 所有代码（HTML, CSS, JavaScript）必须封装在**一个文件**中。
- **原生实现**: **禁止**使用任何外部JavaScript库或CSS框架（如jQuery, p5.js, three.js等），请使用原生的Canvas API。

## 输出指令
- 将最终的完整代码保存为一个名为 `particles.html` 的文件。
- 接着打开这个文件，让我能看到运行的效果。
```

---

## 见证你的魔法

**1. 批准AI的操作**
   - 在执行创建文件、打开网页等操作前，负责任的AI助手会请求你的许可。
   - 当它询问时，请输入 `y` 然后按回车来批准它的计划。

**2. 欣赏你的作品**
   - 命令执行完毕后，你会发现AI不仅在VS Code左侧的文件浏览器中为你创建了 `particles.html` 文件...
   - ...它还会**自动在你的默认浏览器中打开这个网页**，让你即刻欣赏你的第一个作品！

---

## 你，刚刚，创造了它！

<div class="columns ratio-6-4">
<div>

浏览器中出现的，就是你亲手指挥AI创造的第一个数字艺术品。

这证明了：
- 你的AI助手是一个能听懂指令、并能直接动手的强大伙伴。
- **你，即将掌握通过自然语言指挥AI完成创造的核心能力。**

</div>
<div class="align-middle-center">

![“关系宇宙”网页在浏览器中全屏运行的惊艳截图 height:400px](../../../lectures/images/2025-10-26-00-34-35.png)

</div>
</div>

---

## 第六站：让AI指导你安装Python

<div class="columns ratio-6-4">
<div>

刚才，我们体验了AI作为“创造者”的强大。接下来，我们将体验它作为“老师”的智慧。

**任务：** 我们不再提供Python的安装步骤，而是要让你面前的AI编程助手告诉你该怎么做。

</div>
<div class="align-middle-center">

![一个友好的机器人老师正在指向Python的Logo height:400px](../../../lectures/images/2025-10-26-00-36-17.png)

</div>
</div>

---

## 核心任务：如何优雅地向AI提问？

一个好的问题，是得到好答案的关键。请在VS Code的 `qwen` 提示符 `>` 后面，参考以下模板，输入你的问题：

**提问模板：**
> 我是一个编程初学者，请给我一份在我的 **[这里换成你的操作系统，例如：Windows 11 或 macOS]** 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。

**示例：**
`> 我是一个编程初学者，请给我一份在我的 Windows 11 电脑上安装Python的详细步骤。请确保这份指南对新手来说非常容易理解。`

---

## 核心任务：跟随AI向导，完成安装

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

![Python在Windows上安装过程的截图，并用红色方框高亮“Add Python to PATH”复选框 height:400px](../../../lectures/images/2025-10-26-00-37-38.png)

</div>
</div>

---

## 最终检查：验证你的工作室

当你跟随AI的指引完成所有操作后，我们需要进行最终检查。

**重要：请先关闭并重新启动VS Code。** (这样才能让它内置的终端识别到新安装的Python)

然后，在VS Code中重新打开一个集成终端，依次输入以下两个命令：

```bash
$ python --version
# 预期输出: Python 3.x.x (类似的版本号)

$ qwen --version
# 预期输出: @qwen-code/cli/1.x.x (类似的版本号)
```

---

## 恭喜！你的AI工作室已全面落成！

<div class="columns ratio-7-3">
<div>

如果你能成功看到两个版本号，那么恭喜你，你已经：
- ✅ 搭建了以VS Code为核心的“魔法工作室”。
- ✅ 掌握了在集成终端中召唤并指挥AI助手。
- ✅ 在AI老师的指导下，完成了所有核心工具的安装。

你已经真正踏上了“AI赋能编程”的道路！

</div>
<div class="align-middle-center">

![一个庆祝性的图片，上面有“工作室落成”的字样和Python、AI助手的Logo height:400px](../../../lectures/images/2025-10-26-00-38-58.png)

</div>
</div>

---

## 常见问题与定心丸

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

---

## 下一步预告

<div class="columns ratio-6-4">
<div>

工作室已经建成，下一节课，我们将正式开始“创造”。

- **学习目标**: 掌握与AI高效沟通的艺术——Prompt工程。
- **实践项目**: 指挥AI从零创造你的第一个**可视化教学应用**——一个可以直接在课堂上使用的、充满动感的“随机点名器”！

</div>
<div class="align-middle-center">

![一个动态随机点名器应用的GIF或静态截图 height:400px](../../../lectures/images/2025-10-26-01-01-15.png)

</div>
</div>