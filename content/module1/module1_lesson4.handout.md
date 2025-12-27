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
![bg blur:3px brightness:60%](../../../lectures/images/2025-10-26-21-45-52.png)

<style scoped>
h1 {
  color: #F5F5F5;
  /* 设置文字颜色为白色 */
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  /* 添加一个柔和的深色阴影 */
}

h2 {
  color: #E0E0E0;
  /* 设置文字颜色为白色 */
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
  /* 添加一个柔和的深色阴影 */
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
  border-left: 5px solid #4CAF50;
  /* 用一条强调色作为装饰 */
}

</style>

<div class="course-title">AI赋能软件开发</div>

# 模块一: AI编程新纪元 (思想破冰)
## 第4节课: 首个AI应用发布会 & 创造者心得

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 学习的闭环：回顾、分享与内化
欢迎来到模块一的最后一课。在软件开发和项目管理中，一个项目结束后，团队通常会举行一个“复盘会议”，来回顾过程、总结经验、庆祝成功。这节课，就是我们第一个项目的“复盘大会”。

学习不仅仅是吸收新知识，更重要的是对所学知识进行**回顾(Review)**、**分享(Share)**和**内化(Internalize)**。通过向他人展示你的作品，倾听他人的经验，和反思自己的心路历程，你能将知识和技能更深刻地烙印在自己的脑海里。今天，让我们一起完成这个学习的闭环。

</div>

---

## **本节课目标：庆祝我们的“首个产品发布会”！**

<div class="columns ratio-6-4">
<div>

**欢迎来到模块一的总结分享会，暨我们的“首个产品发布会”！**

这堂课很特别，我们的核心任务不是编写新代码，而是完成三项更有意义的活动：

1.  **庆祝 (Celebrate)**：像发布新产品一样，展示和体验彼此的“可视化随机点名器”。
2.  **分享 (Share)**：交流在创造过程中的“Wow!”、“Aha!”和“Uh-oh...”时刻。
3.  **反思 (Reflect)**：探讨这次经历如何颠覆了我们对“编程”和“创造”的看法。

</div>
<div class="align-middle-center">

![图片描述：人们在产品发布会上庆祝的场景 width:440px](../../../lectures/images/2025-10-26-21-51-15.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 本节课的三个核心环节
- **庆祝 (Celebrate)**: 学习需要正反馈。公开展示和庆祝你的第一个“作品”，是获取成就感、建立自信心的最佳方式。同时，通过观摩他人的作品，你也能获得新的灵感。

- **分享 (Share)**: 分享是知识网络化的过程。当你分享你的经验时，你是在巩固自己的理解；当你倾听他人分享时，你是在吸收他人的智慧。特别是对“Aha!”（领悟）和“Uh-oh...”（困难）时刻的分享，能极大地加速整个学习共同体的成长。

- **反思 (Reflect)**: 这是学习的最高层次。它要求我们从具体的“术”（如何做一个点名器），上升到抽象的“道”（AI编程的本质是什么，它如何改变我们的工作）。具备反思能力，才能将一次学习的经验，迁移到未来的无数次创造中。

</div>

---

## **环节一：应用博览会 (App Fair)**

<div class="columns ratio-6-4">
<div>

**第一步：画廊漫步 (5分钟)**

欢迎来到我们的“首个AI应用发布会”！首先，请大家将自己的点名器运行起来，截一张最酷的图，发布到我们的班级群/讨论区中！

同时，请像逛画展一样，去欣赏、点赞、评论其他同学的作品。

**第二步：明星产品路演**

接下来，我们将从“画廊”中，邀请几位同学自愿上台（共享屏幕），向大家展示你的“可视化随机点名器”并分享心情！

</div>
<div class="align-middle-center">

![图片描述：线上画廊，展示着许多点名器应用的截图 width:440px](../../../lectures/images/2025-10-26-21-57-17.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Showcase: 开发者社区的传统
“Showcase”（展示）或“Demo Day”（演示日）是开发者社区和创业孵化器中的一个悠久传统。开发者们会定期向社区展示他们近期完成的作品，交流想法，并获取反馈。

**“画廊漫步”的价值**：
- **快速概览**: 让我们能在短时间内看到班级同学创意的多样性。
- **建立安全感**: 对于不善言辞或对作品不够自信的同学，发一张截图是分享成果的、心理负担最小的方式。

**“路演”的价值**：
- **深度交流**: 现场演示能更直观地展示应用的交互和效果。
- **锻炼表达**: “向他人介绍自己的作品”本身就是产品经理和创造者的一项核心能力。

</div>

---

## **环节二：导演幕后访谈**

<div class="columns ratio-6-4">
<div>

每一个作品背后，都有一位出色的“导演”。现在，让我们一起聊聊幕后的故事。

**请分享你的：**

1.  **“Wow!” 时刻** 🤩
    - *看到什么时最惊喜？*
2.  **“Aha!” 时刻** 🤔
    - *领悟到了什么妙招？*
3.  **“Uh-oh...” 时刻** 😅
    - *遇到了什么小麻烦？*

</div>
<div class="align-middle-center">

![图片描述：访谈或Q&A的图标 width:440px](../../../lectures/images/2025-10-26-22-08-08.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 复盘：将经验转化为能力
如果说动手实践是将知识转化为技能，那么复盘就是将技能转化为可以迁移的能力。这个“Wow/Aha/Uh-oh”框架，是个人和团队进行复盘的经典工具。
- **“Wow!” 时刻 (Peak Moments & Strengths)**: 关注和分享这些高峰体验，可以帮助我们识别哪些方法是有效的，哪些是能带来巨大价值的。这有助于我们固化成功的模式。
- **“Aha!” 时刻 (Insights & Learnings)**: 这是学习发生的关键信号。分享这些“顿悟”的瞬间，可以让整个团队的认知水平得到提升。别人的“Aha”时刻，可能正是你卡住的关键。
- **“Uh-oh...” 时刻 (Challenges & Opportunities)**: 诚实地面对遇到的困难，是成长的第一步。通过讨论这些“小麻烦”，我们可以共同寻找解决方案，并识别出未来需要改进和深入学习的方向。这也是发现学习需求和课程改进点的宝贵来源。

</div>

---

## **环节三：进阶功能头脑风暴**

<div class="columns ratio-6-4">
<div>

在上一节课的结尾，我们留下了两个有趣的进阶挑战。今天我们不检验结果，我们来一起**思考实现思路**。

**挑战1 (增加幸运感)**：
> “如果要给选中的学生加上‘撒花’特效，我们应该怎么用自然语言，向AI描述这个视觉需求？”

**挑战2 (避免重复)**：
> “那么，‘避免重复点名’这个功能，大家觉得它实现的难点在哪里？它要求程序必须具备一种什么样的新能力？”

</div>
<div class="align-middle-center">

![图片描述：一个亮起的灯泡，代表“创意”和“头脑风暴” width:440px](../../../lectures/images/2025-10-26-22-10-24.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 定义需求的两种类型：视觉型 vs. 逻辑型
通过这两个挑战的对比，我们可以看到在向AI提需求时，通常会遇到两种不同类型的需求：
- **视觉型需求 (Presentation Requirement)**: 这类需求主要关注“看起来怎么样”。
  - **定义要点**: 通常需要用丰富的、描述性的语言来定义效果。关键在于描述清楚 **“何时 (When)”** 触发、**“什么样 (What)”** 的效果、**“如何 (How)”** 表现（如动画速度、颜色、持续时间等）。
  - **例子**: “撒花特效”、“金色的闪光”、“更柔和的动画”。

- **逻辑型需求 (Logic/Functional Requirement)**: 这类需求主要关注“如何工作”，即内在的规则和步骤。
  - **定义要点**: 通常需要像写流程一样，用清晰的、有时序的、无歧义的步骤来描述。关键在于定义好 **“第一步做什么”、“第二步做什么”、“如果遇到...情况该怎么办”**。
  - **例子**: “避免重复点名”就需要定义一系列的检查、判断、更新步骤。

学会在Prompt中清晰地区分和定义这两种需求，是成为AI编程高手的关键一步。

</div>

---

### **挑战参考答案 (1/2): 视觉需求**

刚才我们一起探讨了实现思路，现在，让我们看看一份比较专业的“产品需求文档”（Prompt）会怎么写。

**对于“增加幸运感” (视觉需求):**
> 这是一个纯粹的视觉需求。我们可以这样对AI说：
>
> `“请优化我们之前的点名器。当名字滚动停止，最终选定一个名字后，请在那个名字周围增加一个持续1-2秒的、明亮的、金色的闪光或撒花庆祝动画效果。”`
>
> *（关键：清晰描述**触发时机**、**动画效果**和**持续时间**。）*

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 精确描述视觉需求的技巧
一个好的视觉需求Prompt，通常遵循一个简单的结构：**“在[时机]，发生[效果]，持续[多久]”**。
- **时机 (Trigger)**: `当名字滚动停止，最终选定一个名字后...` 这告诉AI在什么时候执行这个动画，是程序逻辑与视觉效果的连接点。
- **效果 (Effect)**: `...明亮的、金色的闪光或撒花庆祝动画效果。` 这是对视觉效果本身的具体描述。描述得越生动、越具体（例如使用“金色”、“明亮”等词），AI的发挥空间就越精确。
- **参数 (Parameters)**: `...持续1-2秒...` 这为动画提供了量化指标，使其行为更可控。

在描述视觉需求时，多运用感官和场景化的词汇，可以帮助AI更好地捕捉你想要营造的“氛围感”。

</div>

---

### **挑战参考答案 (2/2): 逻辑需求**

**对于“避免重复” (逻辑需求):**
> 这是一个逻辑需求，更复杂。我们需要引导AI“记住”已经点过的名字。可以这样分步说：
>
> `“首先，请在程序里创建一个空的列表，用来存放‘已被点过’的名字。`
>
> `第二，当我们随机挑选名字时，如果发现这个名字已经存在于‘已被点过’的列表中，就请重新挑选，直到找到一个不在列表中的名字为止。`
>
> `第三，当一个新名字被选中并显示后，请立刻将这个名字加入到‘已被点过’的列表中。”`
>
> *（关键：我们将一个复杂任务，拆解成了清晰的、有时序的**逻辑步骤**。这正是模块二要深入学习的思维方式！）*

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 算法思维：用步骤描述逻辑
这个“避免重复”的例子，完美地诠释了什么是“**算法思维 (Algorithmic Thinking)**”——即能够将一个任务（无论多复杂），分解为一系列有限的、明确的、可执行的步骤。

我们给AI的这个三步指令，就是一个简单的算法。让我们再深入看一下：
- **`“首先，...创建一个空的列表...”`**: 这是**初始化**步骤。程序需要一个地方来“记忆”，我们称之为“状态（State）”。这个列表就是用来保存我们程序的状态的。
- **`“第二，...如果发现...就请重新挑选...”`**: 这是**条件判断 (Condition)** 和 **循环 (Loop)**。程序需要根据一个条件（名字是否在列表中）来决定下一步的行动（重新挑选）。
- **`“第三，...将这个名字加入到列表中。”`**: 这是**状态更新 (State Update)**。程序在完成一次操作后，需要更新自己的“记忆”。

初始化、条件判断、循环、状态更新，这些正是我们将在模块二中深入学习的编程核心概念。通过这个例子，你已经对它们有了直观的感受。

</div>

---

## **环节四：创意风暴 & 导师魔法秀**

<div class="columns ratio-6-4">
<div>

大家都成功地让名字“动”了起来，创造了属于自己的动态点名器，非常好！

我们刚才在“应用博览会”上，可能已经看到了几种不同的视觉效果。其实，随机过程的乐趣，其表现形式远不止我们已经看到的这些。

让我们打开思路，看一些其他的可能性...

</div>
<div class="align-middle-center">

![图片描述：代表“创意风暴”的龙卷风或旋涡 width:300px](../../../lectures/images/2025-10-26-23-06-37.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 从功能到体验：分离逻辑与表现
这个环节的核心思想，是再次强调我们在上节课提到的“**逻辑与表现分离**”的设计原则。
- **核心逻辑**: 从一个列表中随机选择一个项目。这个逻辑是稳定的，不变的。
- **视觉表现**: 如何将这个“随机选择”的过程展示给用户。这个表现层是千变万化的。

一个优秀的“产品总监”或“创造者”，不仅要能设计出核心逻辑，更要懂得如何通过富有创意的视觉表现来提升产品的用户体验，让一个“好用”的工具，同时变得“好玩”和“有趣”。接下来的几页，就是一些关于“视觉表现”的创意启发。

</div>

---

<style scoped>
section p,
section li {
  font-size: 0.8rem;
  /* 原本约 1.25rem */
}

</style>

### **创意构思：随机性的表现形式 (1/2)**

<div class="columns" style="display: grid; grid-template-columns: 1fr; gap: 1rem; font-size: 16px;">
<div>

- **自然与有机类 (雅致、静谧)**
  - **蒲公英飞絮**: 带名字的种子在空中飞舞，最终一粒缓缓飘落。
  - **瓶中萤火虫**: 满瓶飞舞的萤火虫，最终只留一只在瓶中发光。
  - **星空与流星**: 流星划过天际，精准落在某颗“学生”星星上。
- **科技与未来类 (酷炫、硬核)**
  - **代码/矩阵雨**: 学生名字组成代码雨下落，最终一个高亮。
  - **DNA序列解码**: 名字作为基因序列在DNA双螺旋上滚动，最终解码出一段。
  - **星际跃迁**: 飞船在名字星球间穿梭，最终停靠在一个星系前。

</div>
<div class="align-middle-center">

![图片描述：蒲公英的种子在风中飞舞 width:440px](../../../lectures/images/2025-10-26-22-12-34.png)

</div>
</div>

---

### **创意构思：随机性的表现形式 (2/2)**

<div class="columns ratio-6-4">
<div>

- **游戏与趣味类 (活泼、有趣)**
  - **扭蛋机/盲盒**: 摇晃机器，掉出一个扭蛋，打开显示名字。
  - **街机角色选择**: 选择框在角色矩阵上疯狂跳动，最终定格。
  - **刮刮乐**: 刮开涂层，显示下面的名字。
- **艺术与抽象类 (高级、有设计感)**
  - **水墨散开**: 墨滴在宣纸上散开，名字若隐若现，最终形成书法。
  - **照片马赛克**: 无数模糊色块洗牌变换，最终拼成一幅艺术图。

</div>
<div class="align-middle-center">

![图片描述：一个日式扭蛋机 width:440px](../../../lectures/images/2025-10-26-22-20-35.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 主题化设计：为你的应用注入灵魂
这些创意构思不仅仅是“换皮肤”，它们体现了一种“**主题化设计 (Thematic Design)**”的思路。为你的应用设定一个主题，可以让它的体验更统一、更沉浸、更有情感共鸣。

在向AI描述这些复杂创意时，可以运用“**类比（Analogy）**”和“**场景化描述（Scenario Description）**”的技巧。
- **类比**: 直接告诉AI，你想要的效果“**像...一样**”。例如：“我想要一个像‘黑客帝国’里那样的代码雨效果”。
- **场景化描述**: 为AI描绘一整个场景。例如：“想象一个宁静的夜晚，天空中布满了星星，每一颗星星代表一个学生的名字。当点名开始时，一道流星会划过天际...”

通过这种富有想象力的沟通方式，你可以引导AI进行更具创造性的工作。

</div>

---

### **导师魔法秀：Pro版点名器演示**

<div class="columns ratio-6-4">
<div>

为了给大家一个更直观的感受，我将其中一种创意（例如“星空流星”）和我们提到的进阶功能（例如“避免重复”）结合起来，实现了一个Pro版的点名器。

我们一起来看一下，一个经过精心设计和功能迭代的应用，能达到什么样的效果……

**(此处为教师演示环节)**
</div>
<div class="align-middle-center">

![图片描述：舞台幕布拉开，聚光灯打下，代表“好戏上演” width:440px](../../../lectures/images/2025-10-26-23-08-50.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 迭代的力量：从“原型”到“产品”
这个“Pro版”点名器与我们上节课做的“初版”点名器之间的差距，就体现了“**迭代开发 (Iterative Development)**”的力量。
- **初版 (Prototype)**: 目标是快速验证核心功能是否可行。它可能很简单，甚至有些粗糙，但它能工作。
- **迭代版 (Polished Version)**: 在初版的基础上，通过多轮的“**反馈-修改**”循环，不断地增加新功能、优化用户体验、美化视觉设计，最终从一个“可用的原型”演变为一个“好用的产品”。

导师的这个演示，旨在告诉你，你上节课创造的，是一个非常有价值的“原型”。以此为起点，通过与AI的持续对话，你完全有能力将其打磨成一个令人惊艳的“产品”。

</div>

---

## **跨越鸿沟：AI如何赋能我们成为创造者**

<div class="columns ratio-7-3">
<div>

过去，编程的“鸿沟”——海量语法、抽象逻辑、繁琐环境——将许多有创意的想法挡在门外。

现在，AI为我们架起了桥梁。它成为我们的“首席翻译官”，负责将我们的**想法和意图**，转化为机器能懂的**代码**。

**这是一种能力的“平权”**：我们不再需要成为程序员，也能指挥机器去建造。我们的核心任务，是学会分析并拆解问题，然后清晰地向AI传达我们的设计。

</div>
<div class="align-middle-center">

![图片描述：一座宏伟的桥梁跨越幽深的峡谷 width:330px](../../../lectures/images/2025-10-26-22-25-00.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 范式转移：从“学习语法”到“表达意图”
我们正在经历一场从“**以语法为中心 (Syntax-centric)**”到“**以意图为中心 (Intent-centric)**”的编程范式转移。
- **旧范式**: 创造者必须学习机器的语言（编程语法），将自己的想法翻译给机器。这个翻译过程是主要瓶颈。
- **新范式**: 创造者用自己最擅长的自然语言来表达自己的“意图 (Intent)”，AI负责将这个意图翻译给机器。瓶颈从“懂不懂语法”转移到了“能不能清晰地表达意图”。

这带来的最大变化，就是“**创造力的民主化**”。过去，只有掌握了特定编程语言的“祭司”（程序员），才能与机器沟通。现在，任何能够清晰思考和表达的人，都获得了与机器沟通、指挥其创造的能力。这是一个全新的、充满机遇的时代。

</div>

---

## **人机协作：我们的核心价值在哪里？**

<div class="columns ratio-6-4">
<div>

AI是强大的工具，但它无法替代你，因为它缺少：

- **领域专业知识**
- **批判性思维与共情**
- **创新与愿景**

> AI是强大的画笔，而你，是挥舞画笔的艺术家。

</div>
<div class="align-top-left">

![图片描述：人类与AI机器人握手协作 width:400px](../../../lectures/images/2025-10-26-22-27-58.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 人类在AI时代的独特价值
在与AI协作时，你的价值不在于执行，而在于以下三个层面：
1.  **领域专业知识 (Domain Expertise)**: AI虽然拥有海量的通用知识，但它缺乏你在特定学科领域（如特定时期的历史、某种细胞的生物学特性、某个经济学流派的观点）深耕多年所形成的深刻洞察和隐性知识。你的专业知识是为AI设定正确方向和约束的“罗盘”。
2.  **批判性思维与共情 (Critical Thinking & Empathy)**: AI可以生成内容，但它没有价值观，无法判断“好”与“坏”。它会一本正经地胡说八道。你需要运用你的批判性思维来审视和验证AI的输出。同时，你也需要运用你的共情能力，来判断你创造出的东西，是否真正符合你的学生或用户的需求和情感。
3.  **创新与愿景 (Innovation & Vision)**: AI无法凭空产生目的和意义。它不会主动去发现一个值得解决的问题，更不会为一个领域提出一个高瞻远瞩的发展愿景。定义问题、树立愿景、提出那个“从0到1”的原创想法，是人类创造者永恒的核心价值。

</div>

---

## **模块一总结：我们收获了什么？**

<div class="columns ratio-6-4">
<div>

✅ **一种新思维**
   - 理解了人机协作的编程新范式。

✅ **一套工具箱**
   - 成功搭建了AI编程工作环境。

✅ **一个核心技能**
   - 亲身体验了完整的应用开发循环。

✅ **一份巨大的成就感**
   - 创造了属于自己的第一个可视化AI应用。

</div>
<div class="align-middle-center">

![图片描述：一个装满金币和技能图标的宝箱 width:440px](../../../lectures/images/2025-10-26-22-37-23.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 你的收获清单
让我们来详细解读一下你在本模块的四项核心收获：
- **一种新思维**: 你不再认为编程是少数人的专利，而是理解了“编程即对话”的新范式。你认识到，你的核心任务是清晰地表达意图，而不是记忆语法。
- **一套工具箱**: 你拥有了一个现代化的、功能强大的AI编程环境（VS Code + AI助手 + Python）。这个“工作室”是你未来所有创造的起点。
- **一个核心技能**: 你实践了“想法 -> 解构 -> 指令 -> 迭代”这一核心的应用开发流程。这个技能可以被复用到你未来的任何一个项目中。
- **一份巨大的成就感**: 这种“我能行”的感受，是打破“技术恐惧”、开启后续学习之路最宝贵的燃料。请一定珍视和记住这份感觉。

</div>

---

## **下一步预告：模块二 - 与AI对话 (编程基础)**

<div class="columns ratio-6-4">
<div>

思想破冰之后，我们将开始了解编程的一些“核心规则”。

我们将学习如何下达更精确的指令，在指挥AI使用**变量、条件、循环**等核心概念的过程中，真正理解它们的作用和威力！

</div>
<div class="align-middle-center">

![图片描述：代表变量(x)、条件(if)、循环(loop)的编程积木 width:330px](../../../lectures/images/2025-10-26-23-02-43.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 展望模块二：掌握编程的“语法”
如果说模块一我们学习的是如何与AI“对话”，那么模块二我们将学习如何让我们的“对话”更精确、更高效。我们将接触到编程世界最核心的三个概念：
- **变量 (Variables)**: 让程序能够“记忆”和“存储”信息。就像我们在“避免重复点名”挑战中需要的那个“已点名列表”。
- **条件 (Conditions)**: 让程序能够“判断”和“决策”。例如，“**如果**学生是男生，就显示蓝色；**否则**显示红色”。
- **循环 (Loops)**: 让程序能够“重复”执行任务。例如，“对名单上的**每一个**学生，都检查他是否交了作业”。

掌握了这三个“核心规则”，你就掌握了向AI下达几乎所有精确指令的能力，也就真正敲开了创造复杂应用的大门。

</div>

---

# 课后练习

<style scoped>
section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

h1 {
  font-size: 60px;
  margin-bottom: 20px;
  /* 控制标题和提示语的间距 */
}

p {
  font-size: 18px;
  color: #555;
  line-height: 1.5;
  /* 增加行高，让提示语更易读 */
}

</style>

<p>

*小提示：别忘了，你的AI编程助手也是一位出色的学伴和老师！<br>当你对这些练习题有任何疑惑时，随时可以和它讨论，让它引导你完成思考。*

</p>

---

## ****课后练习：“回响”——从“痛点”到“可编程时刻”****

还记得第一节课我们讨论的“痛点”吗？那时，我们只是感性地描述了我们遇到的麻烦。

现在，我们已经掌握了“输入-处理-输出”这个强大的思维工具。请你**重新审视当初的那个“痛点”**，或者发现一个新的，并尝试用我们新学到的思维框架来“解构”它：

- **输入 (Input):** 要处理的“原料”是什么？
- **处理 (Process):** 核心的转换步骤是什么？
- **输出 (Output):** 最终想得到的“成品”是什么？

这个从“感性诉苦”到“理性分析”的转变，标志着你已经从一个“问题拥有者”，**蜕变为一个“解决方案的设计者”**。

请带着你的这份“IPO分析报告”，满怀信心地进入模块二的学习！

---

### **课后练习：可选挑战 (1/2)**

如果你对我们课堂上讨论的两个进阶挑战意犹未尽，可以尝试完成下面这个“思考题”。这会极大地锻炼你“拆解复杂逻辑”的能力。

#### **挑战一：增加“幸运感”**
> *请用IPO模型分析，为点名器增加“撒花特效”需要改变什么？*
> - **输入 (Input):** 和原来相比，输入有变化吗？（提示：没有）
> - **输出 (Output):** 最终的“成品”增加了什么？（提示：视觉上增加了动画）
> - **处理 (Process):** “配方”需要增加哪个步骤？请用自然语言描述这个新增的步骤。（提示：参考我们课上展示的“参考答案”Prompt）

---

### **课后练习：可选挑战 (2/2)**

#### **挑战二：实现“避免重复”**
> *这是真正的挑战！请用IPO模型分析，并思考“处理”过程的巨大变化。*
> - **输入 (Input):** 为了“记住”点过的名字，我们的程序是否需要一个新的“输入”？（提示：是的，一个用于记录的、会动态变化的列表）
> - **输出 (Output):** 输出有变化吗？（提示：没有，依然是一个名字）
> - **处理 (Process):** 这是最复杂的部分。请尝试用我们课上学到的“分步拆解”方法，描述一下新的“处理”流程是怎样的？

完成这个思考题后，你对模块二要学习的“变量”和“逻辑”，会有更深刻的渴望！