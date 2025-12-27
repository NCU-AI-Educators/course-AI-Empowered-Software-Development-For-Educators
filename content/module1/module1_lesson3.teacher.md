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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场：承前启后，设定目标
本页作为第三节课的开场，旨在快速回顾上节课的成果，并清晰地设定本节课更具创造性的目标。

**核心要点**：
1.  **回顾与衔接**: 确认学员已完成环境搭建，并将其从“魔法学徒”的角色自然地过渡到本节课的“产品总监”。
2.  **目标具体化**: “可视化随机点名器”是一个非常具体、贴近教学场景的目标，能让学员立刻理解本节课的产出和价值。
3.  **角色升级**: 强调从“体验”到“创造”的角色转变，提升学员的参与感和主人翁意识。

</div>

---

## **本节课目标：创造你的第一个实用教学工具**

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 确立核心隐喻与角色定位
本页的核心是强化“产品总监 vs AI开发团队”这一隐喻，为整个课程的“人机协作”模式奠定基调。

**核心要点**：
1.  **角色扮演**: 让学员代入“产品总监”的角色，可以有效地将他们的注意力从对“写代码”的恐惧，转移到他们相对熟悉的“提要求”、“沟通协调”等活动上。
2.  **能力拆分**: 清晰地界定人（提需求）和AI（实现）的职责，让学员明白自己应该聚焦于“想清楚”，而不是“做出来”。
3.  **降低心理门槛**: “全栈开发团队”的比喻，极大地增强了学员的信心，让他们感觉自己拥有了强大的技术后盾。

</div>

---

## **真实场景：让课堂点名变得有趣！**

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 建立需求背景与价值主张
本页旨在将项目与学员的真实工作场景深度绑定，并清晰地阐述产品的“价值主张”。

**核心要点**：
1.  **场景代入**: 通过描述“传统点名方式”的痛点，快速引发学员的共鸣。
2.  **价值主张**: “让课堂点名变得有趣！”和“激动人心的抽奖”，清晰地定义了产品要创造的核心价值——提升课堂的趣味性和仪式感。
3.  **视觉对比**: 图片直观地展示了从“无聊”到“有趣”的转变，强化了产品的吸引力。

</div>

---

## **解构魔法：先搭“骨架”（数据与交互）**

在告诉AI“做什么”之前，我们先像产品经理一样，把“大想法”拆解成“小零件”。

**我们的愿景：** 一个充满动感和趣味的随机点名器。

**首先，思考它的基本框架：**

1.  **“原料”是什么？** -> 点名器需要“认识”所有学生。
    -   **特性1 (数据)**：程序必须能**读取一份学生名单**。

2.  **“开关”在哪里？** -> 我们需要一种方式来命令它“开始”和“停止”。
    -   **特性2 (交互)**：需要一个 **“开始/停止”按钮**。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教授“需求分析”的核心方法
本页开始引导学员进行结构化的思考，将一个模糊的想法分解为具体、可实现的功能点。这是编程思维的核心训练。

**核心要点**：
1.  **引入“解构”思想**: 将“需求分析”包装成“解构魔法”，生动易懂。
2.  **建立基本模型**: 提出任何程序都包含的两个基本要素“数据（原料）”和“交互（开关）”，为学员提供一个分析问题的通用框架。
3.  **从具体到抽象**: 将“学生名单”抽象为“数据”，将“按钮”抽象为“交互”，培养学员的抽象思维能力。

</div>

---

## **解构魔法：再填充“功能”与“外观”**

有了骨架，我们再为它实现核心功能与视觉外观。

3.  **它“做什么”？（核心功能）** -> 核心功能是从名单里随机挑出一个。
    -   **特性3 (逻辑)**：当停止时，程序能**最终确定一个随机名字**。

4.  **如何让它“有趣”？（视觉外观）** -> 要有动态效果，而不是瞬间完成。
    -   **特性4 (视觉)**：在挑选过程中，名字要像老虎机一样**快速滚动**。
      

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引入“逻辑”与“视觉”的分离
本页继续进行需求解构，引入了“功能逻辑”和“视觉表现”这两个同样重要的维度。

**核心要点**：
1.  **功能与形式分离**: 清晰地区分了“它做什么（逻辑）”和“它看起来怎么样（视觉）”，这是一种非常重要的设计思想，有助于学员理解软件的不同层次。
2.  **连接愿景**: 将“快速滚动”这个视觉特性，与之前定义的“有趣”这个愿景联系起来，让学员理解每一个设计决策都应该服务于最初的目标。

</div>

---

## **从要素到需求**

<div class="columns ratio-6-4">
<div>

看，通过这四步，我们就把一个模糊的想法，变成了一份清晰的功能清单。

这份清单组合起来，就形成了一份完美的“产品需求文档”，也就是我们接下来在“动手环节”要交给AI的、清晰无误的指令！

</div>
<div>

![占位图：从零件到蓝图的合成过程](../../../lectures/images/2025-10-26-17-41-11.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 总结“需求分析”过程
本页是对前面几页“解构”过程的总结，旨在固化学员对“将想法转化为需求”这一过程的理解。

**核心要点**：
1.  **过程回顾**: 总结了从“模糊想法”到“清晰功能清单”的转化过程，强化了学员刚刚习得的思维方法。
2.  **引入专业术语**: 正式地将“功能清单”等同于“产品需求文档”，让学员认识到他们刚才所做的，就是一项专业的产品设计工作，增强其成就感。
3.  **建立因果关系**: 强调了“清晰的指令”是得到好结果的前提，为下一步的动手环节做好铺垫。

</div>

---

## **动手环节：三步创造你的应用**

现在，让我们进入VS Code，打开下方的集成终端，启动 `qwen` 助手，然后一步步创造奇迹。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 场景切换
一个简单的过渡页，清晰地告知学员从“理论学习”进入“动手实践”阶段，帮助他们调整状态。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 第一个具体的动手任务
这个任务的目标是让学员成功地生成应用所需的数据文件。

**核心要点**:
1.  **连接理论**: 明确指出这一步对应的是之前分析的“特性1 (数据)”，让学员理解每一步操作的目的性。
2.  **指令清晰**: 提供的指令简单、明确，成功率高。
3.  **即时反馈**: 结果（生成`students.txt`文件）是即时的、可见的，能迅速给予学员正向反馈。
4.  **引导实际应用**: “小贴士”部分非常关键，它将练习与学员的实际工作联系起来，展示了工具的真实可用性，极大地提升了学习动机。

</div>

---
### **第二步：构建并启动点名器**

数据“原料”已经备好。现在，我们要将分析出的另外三个特性——**特性2 (交互)**、**特性3 (逻辑)** 和 **特性4 (视觉外观)**——打包成一个完整的需求，一次性地交给AI，让它为我们构建应用本身。请注意，我们在最后增加了一条【输出指令】：

> `请帮我创建一个名为 "点名器.html" 的文件。这个程序需要读取同目录下的 students.txt 文件来获取所有学生名单。网页上要有一个“开始/停止”按钮。第一次点击按钮，网页会像老虎机一样快速随机滚动学生名字；再次点击，滚动停止，并最终显示一个随机选中的名字。`
>
> `【输出指令】: 创建完成后，请立刻在默认浏览器中打开这个 "点名器.html" 文件。`

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 核心指令的下达
这是本节课的核心环节，学员将之前分析的所有需求点综合成一个完整的Prompt，并交给AI执行。

**核心要点**:
1.  **综合应用**: 指导学员将之前分解的多个特性，重新组合成一个结构化的、完整的指令。这是一个“分解-整合”的完整思维闭环。
2.  **引入“行动指令”**: 明确指出`【输出指令】`的作用，让学员意识到可以命令AI执行“编码”之外的“行动”（如打开文件），拓展他们对AI能力的认知。
3.  **提供完整范本**: 提供可以直接复制的完整Prompt，确保学员在此关键步骤的成功率。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### “收获”与“验证”
本页的目的是引导学员验证AI的执行结果，并最大化他们的成就感。

**核心要点**:
1.  **营造高潮**: “见证奇迹”、“你什么都不用做”等语言，旨在营造一种轻松而又充满期待的氛围，让最终结果的出现充满仪式感。
2.  **结果验证**: 引导学员观察“浏览器自动打开”这一现象，并尝试与应用交互（“点击按钮试试”），完成对项目成果的最终验证。
3.  **强化“创造者”身份**: “在你眼前诞生并运行了”、“你的第一个AI教学应用”，这些话语都在不断强化和肯定学员作为“创造者”的身份和成就。

</div>

---

### **所有程序的“秘密配方”**

祝贺你，刚刚你不仅创造了一个应用，更在不经意间，实践了所有程序开发共同的“秘密配方”！

让我们回顾一下“随机点名器”的工作过程：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-58-01.png)

*图：程序的“输入-处理-输出”模型*

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 理论升华（一）：引入IPO模型
在学员获得巨大成就感的时刻，及时进行理论升华，能取得事半功倍的效果。本页将具体实践抽象为通用的“输入-处理-输出 (IPO)”模型。

**核心要点**:
1.  **时机恰当**: 在成功的实践后立刻进行理论总结，学员的学习意愿和接受度最高。
2.  **模型简化**: IPO模型是计算机科学的基础，这里用“秘密配方”的比喻和极简的图示，让零基础学员可以轻松理解。
3.  **案例关联**: 将IPO的每一个环节都与学员刚刚完成的“点名器”案例一一对应，让抽象理论变得具体可感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 理论升华（二）：教授核心编程思维
本页在IPO模型的基础上，提炼出更具操作性的方法论——“先定义起点和终点”。

**核心要点**:
1.  **方法论提炼**: 将IPO模型转化为一个可执行的思维步骤，即“先两头，再中间”，极具实践指导意义。
2.  **再次关联案例**: 再次使用点名器的例子来解释这个思维习惯，反复加深学员的理解。
3.  **价值拔高**: 将这个思维习惯定义为“编程思维的精髓”，并强调其比具体语法更重要，旨在引导学员关注更高层次的思维能力培养，而不是陷入代码细节。

</div>

---

## **开启对话：如果初版不完美怎么办？**

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教授“迭代优化”的方法
本页旨在管理学员对AI输出的预期，并教授他们如何通过对话来进行迭代优化。

**核心要点**:
1.  **预期管理**: 明确告诉学员AI的初版是“草稿”，不完美是正常的。这可以有效防止学员因AI输出不完美而感到的挫败感。
2.  **教授方法**: 提供了三个非常具体、清晰的优化指令范例，分别对应动画速度（逻辑）、样式（CSS）和内容（HTML），让学员知道可以从哪些方面提出修改意见。
3.  **强化核心理念**: “AI编程是一个持续对话、不断优化的过程”这句话是本页的核心，是对“人机协作”模式的进一步深化。

</div>

---

## **下一步挑战：从“好用”到“好玩”**

我们的点名器已经诞生，但它还能变得更好！你可以课后尝试向AI提出这些“进阶需求”：

- **挑战1 (增加幸运感)**：
  > “当我停止滚动，选中一个学生时，可不可以给他加上一些庆祝的动画特效，比如撒花或者闪光？”

- **挑战2 (避免重复)**：
  > “在一节课中，我不想重复点到同一个人。你能帮我实现这个功能吗？”

这些挑战将引导你探索更复杂的编程逻辑，也是我们后续课程会深入学习的方向。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供“延伸学习”路径
本页为学有余力的学员提供课后探索的方向，并巧妙地预告了后续课程的内容。

**核心要点**:
1.  **学习分层**: “挑战”任务为不同水平的学员提供了差异化的学习路径，满足了高阶学员的探索欲。
2.  **需求升级**: 两个挑战分别代表了“视觉效果”和“程序逻辑”的升级。特别是“避免重复”，它引入了“状态管理”这一更复杂的编程概念，是很好的进阶练习。
3.  **内容预告**: “也是我们后续课程会深入学习的方向”这句话，是在告诉学员，即使现在做不出来也没关系，课程后面会教，从而管理好学员的预期，避免挫败感。

</div>

---

## **你已掌握AI应用开发的核心！**

通过今天的练习，你已经体验了AI时代全新的软件开发模式：

<div style="text-align: center;">

![](../../../lectures/images/2025-10-26-16-51-22.png)

*图：AI时代全新的软件开发模式*

</div>

你不再是代码的实现者，而是**创意的掌舵人**和**产品的决策者**。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 总结与升华
本页是对本节课学习成果的最终总结与升华，旨在固化新的开发模式认知，并再次强化学员的价值感。

**核心要点**:
1.  **流程固化**: 通过可视化的流程图，将本节课的核心工作流（想法->解构->指令->迭代）清晰地固化下来，便于学员记忆和复用。
2.  **价值重申**: 再次强调学员的新角色——“创意的掌舵人”和“产品的决策者”，给予他们最高的价值肯定。
3.  **完成闭环**: 与课程开始时“产品总监”的角色设定遥相呼应，形成完美的教学闭环。

</div>

---

## **下一步预告**

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 承上启下，布置课后任务
本页作为课程的结尾，清晰地预告了下一节课的内容，并暗示了课后任务。

**核心要点**:
1.  **明确预告**: 清晰地列出了下一节课的三个核心活动（分享、探讨、总结），让学员有备而来。
2.  **鼓励分享**: “分享彼此创造的点名器”这个活动，会激励学员在课后去完成和优化自己的挑战任务，将学习从课内延伸到课外。
3.  **节奏转换**: 明确下一节课将从“动手”切换到“分享与讨论”，帮助学员调整学习预期。

</div>