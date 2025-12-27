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

![bg blur:3px brightness:60%](../../../lectures/images/2025-10-26-17-28-32.png)

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
## 第3节课: 你的第一个AI应用：可视化随机点名器

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

---

## 本节课目标：创造你的第一个实用教学工具

<div class="columns ratio-6-4">
<div>

在本节课中，我们将完成一次角色的重要升级：

从上一节课单纯体验AI的“即兴魔法”，**转变为第一次作为“产品总监”，指挥AI为你从零到一创造一个真正实用、可视化的教学应用**。

你将扮演“**产品总监**”的角色，你的任务是提出清晰的需求，AI则会作为你的“全栈开发团队”，负责实现一切。

</div>
<div>

![占位图：从观众到指挥家的角色转变](../../../lectures/images/2025-10-26-17-32-39.png)

</div>
</div>

---

## 真实场景：让课堂点名变得有趣！

<div class="columns ratio-6-4">
<div>

想象一下，传统的点名方式可能是……

- 拿着纸质名单，逐个念名字（耗时、单调）
- 随机叫学号（缺乏仪式感）

**我们的愿景**：创造一个充满动感和趣味的“随机点名器”，在屏幕上快速滚动学生的名字，最后随机定格。让每一次点名，都像一次激动人心的抽奖！

</div>
<div>

![占位图：从单调列表到趣味抽奖的对比](../../../lectures/images/2025-10-26-17-39-12.png)

</div>
</div>

---

## 解构魔法：先搭“骨架”（数据与交互）

在告诉AI“做什么”之前，我们先像产品经理一样，把“大想法”拆解成“小零件”。

**我们的愿景：** 一个充满动感和趣味的随机点名器。

**首先，思考它的基本框架：**

1.  **“原料”是什么？** -> 点名器需要“认识”所有学生。
    -   **特性1 (数据)**：程序必须能**读取一份学生名单**。

2.  **“开关”在哪里？** -> 我们需要一种方式来命令它“开始”和“停止”。
    -   **特性2 (交互)**：需要一个 **“开始/停止”按钮**。

---

## 解构魔法：再填充“功能”与“外观”

有了骨架，我们再为它实现核心功能与视觉外观。

3.  **它“做什么”？（核心功能）** -> 核心功能是从名单里随机挑出一个。
    -   **特性3 (逻辑)**：当停止时，程序能**最终确定一个随机名字**。

4.  **如何让它“有趣”？（视觉外观）** -> 要有动态效果，而不是瞬间完成。
    -   **特性4 (视觉)**：在挑选过程中，名字要像老虎机一样**快速滚动**。

---

## 从要素到需求

<div class="columns ratio-6-4">
<div>

看，通过这四步，我们就把一个模糊的想法，变成了一份清晰的功能清单。

这份清单组合起来，就形成了一份完美的“产品需求文档”，也就是我们接下来在“动手环节”要交给AI的、清晰无误的指令！

</div>
<div>

![占位图：从零件到蓝图的合成过程](../../../lectures/images/2025-10-26-17-41-11.png)

</div>
</div>

---

## 动手环节：三步创造你的应用

现在，让我们进入VS Code，打开下方的集成终端，启动 `qwen` 助手，然后一步步创造奇迹。

---

<style scoped>
.tip {
  background-color: #f0f8ff;
  border-left: 5px solid #1e90ff;
  padding: 15px;
  margin-top: 20px;
}
</style>

### **第一步：创建你的班级花名册**

根据我们刚才分析的 **特性1 (数据)**，我们的应用需要一份“原料”——学生名单。所以，我们的第一步，就是指挥AI为我们准备这份数据。在 `qwen` 提示符后，输入指令：

> `请帮我创建一个名为 students.txt 的文件, 里面包含30个随机的中文名字, 每个名字占一行。`

**魔法时刻**: AI会向你确认“是否允许创建文件”，输入 `y` 并回车。你会立刻在VS Code左侧的文件列表中看到 `students.txt` 文件！

<div class="tip">

**小贴士 (Pro Tip):**
之后在你自己的课堂上，你可以直接从教务系统或Excel中，复制学生名单，然后粘贴到这个 `students.txt` 文件里，点名器就可以马上为你所用了！
</div>

---
### **第二步：构建并启动点名器**

数据“原料”已经备好。现在，我们要将分析出的另外三个特性——**特性2 (交互)**、**特性3 (逻辑)** 和 **特性4 (视觉外观)**——打包成一个完整的需求，一次性地交给AI，让它为我们构建应用本身。请注意，我们在最后增加了一条【输出指令】：

> `请帮我创建一个名为 "点名器.html" 的文件。这个程序需要读取同目录下的 students.txt 文件来获取所有学生名单。网页上要有一个“开始/停止”按钮。第一次点击按钮，网页会像老虎机一样快速随机滚动学生名字；再次点击，滚动停止，并最终显示一个随机选中的名字。`
>
> `【输出指令】: 创建完成后，请立刻在默认浏览器中打开这个 "点名器.html" 文件。`

---
### **第三步：见证奇迹**

<div class="columns ratio-6-4">
<div>

同样，在 `qwen` 提示符后粘贴以上指令并回车，然后在AI请求权限时输入 `y` 批准。

接下来，你什么都不用做！

AI创建完文件后，会**自动调用你的默认浏览器，为你打开 `点名器.html`**。你的第一个AI教学应用，就这样在你眼前诞生并运行了！

</div>
<div>

![占位图：浏览器弹出，展示最终应用](../../../lectures/images/2025-10-26-17-43-05.png)

</div>
</div>

---

### **所有程序的“秘密配方”**

祝贺你，刚刚你不仅创造了一个应用，更在不经意间，实践了所有程序开发共同的“秘密配方”！

让我们回顾一下“随机点名器”的工作过程：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-58-01.png)

*图：程序的“输入-处理-输出”模型*

</div>

---

### **编程的核心思维：定义起点和终点**

发现了吗？任何程序，本质上都是一个“转换器”，它接收一些**输入**，通过一系列**处理**，最终产生一些**输出**。

这就是编程最核心的思维方式：
在动手开始写第一行代码之前，专业的开发者会先清晰地定义两件事：
1.  **起点 (输入):** 我要处理的“原料”是什么？（是`students.txt`文件）
2.  **终点 (输出):** 我最终要得到什么“成品”？（是一个在屏幕上显示的名字）

只有当起点和终点都无比清晰时，我们才开始思考中间的“**处理**”过程（例如，需要一个按钮、需要一个滚动动画等）。

这个 **“先定义起点和终点，再规划中间路径”** 的思维习惯，就是“编程思维”的精髓。掌握了它，你就能应对任何复杂的编程挑战。

---

## 开启对话：如果初版不完美怎么办？

<div class="columns ratio-6-4">
<div>

AI生成的初版应用，是一个优秀的“草稿”，但它可能并不完美。这恰恰是“人机协作”的价值所在！

如果效果不符合预期，我们不需要修改代码，而是继续**与AI对话**，提出你的优化意见：

- **优化动画**：“动画太快了，眼睛看不清，请让名字闪动的速度慢一点。”
- **优化样式**：“选中的名字不够突出。请让最终选中的学生名字，用红色、更大的字号显示。”
- **增加内容**：“请在页面的最上方，增加一个标题‘课堂随机点名器’。”

**记住：AI编程是一个持续对话、不断优化的过程。**

</div>
<div>

![占位图：人与AI的对话反馈闭环](../../../lectures/images/2025-10-26-17-51-49.png)

</div>
</div>

---

## 下一步挑战：从“好用”到“好玩”

我们的点名器已经诞生，但它还能变得更好！你可以课后尝试向AI提出这些“进阶需求”：

- **挑战1 (增加幸运感)**：
  > “当我停止滚动，选中一个学生时，可不可以给他加上一些庆祝的动画特效，比如撒花或者闪光？”

- **挑战2 (避免重复)**：
  > “在一节课中，我不想重复点到同一个人。你能帮我实现这个功能吗？”

这些挑战将引导你探索更复杂的编程逻辑，也是我们后续课程会深入学习的方向。

---

## 你已掌握AI应用开发的核心！

通过今天的练习，你已经体验了AI时代全新的软件开发模式：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-51-22.png)

*图：AI时代全新的软件开发模式*

</div>

你不再是代码的实现者，而是**创意的掌舵人**和**产品的决策者**。

---

## 下一步预告

<div class="columns ratio-6-4">
<div>

这节课，我们创造了一个完整的应用。
在下一节课，也是模块一的最后一节课中，我们将：

- **分享**彼此创造的点名器和心得。
- **探讨**AI编程带来的全新视角。
- **总结**第一个模块的收获，并展望后续的精彩旅程。

</div>
<div>

![占位图：学员分享与社群讨论](../../../lectures/images/2025-10-26-18-06-21.png)

</div>
</div>
