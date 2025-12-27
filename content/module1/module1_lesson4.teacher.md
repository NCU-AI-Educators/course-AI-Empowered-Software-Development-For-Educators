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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场：奠定“庆祝”与“反思”的基调
本页作为模块一的收官课程，核心目标是从“教与学”的模式，平滑过渡到“分享与庆祝”的模式。

**核心要点**：
1.  **明确课程性质**: 开宗明义，告知学员本节课的性质是“分享”和“总结”，而不是学习新技能，帮助学员放松心态，调整预期。
2.  **强化身份认同**: “首个AI应用发布会”和“创造者心得”这两个标题，旨在强化和肯定学员在上节课中获得的“创造者”身份，给予他们强烈的价值感和仪式感。
3.  **营造氛围**: 背景图片和标题都旨在营造一种轻松、愉悦、充满成就感的社区氛围。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 清晰地构建课堂议程
本页用三个关键词“庆祝”、“分享”、“反思”，清晰地定义了本节课的三个主要环节。

**核心要点**：
1.  **结构化**: 将一整节课的内容结构化为三个清晰的环节，让学员对课程流程一目了然，有稳定的预期。
2.  **正向引导**: “庆祝”、“分享”、“反思”这三个词本身都是非常积极和富有建设性的，能引导课堂走向一个开放、包容、正向的氛围。
3.  **情绪递进**: 三个环节的设计遵循了情绪递进的规律：从庆祝具体的作品，到分享个人的体验，再到反思抽象的观念，逐层深入。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 设计低门槛的参与式活动
“应用博览会”旨在用一种游戏化的、低压力的方式，鼓励所有学员展示自己的成果。

**核心要点**：
1.  **分层参与**: “画廊漫步”（发截图）是一个几乎没有门槛的参与方式，确保了100%的学员都能参与进来，获得展示机会。“明星产品路演”则为学有余力或表达欲强的学员提供了展示的舞台。这种分层设计能调动所有人的积极性。
2.  **社区互动**: “点赞、评论”的设计，是在主动营造积极、互助的社区学习氛围。
3.  **时间控制**: 明确“5分钟”的时间限制，有助于教师控制课堂节奏，确保活动高效进行。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供结构化的反思框架
本页旨在引导学员进行有结构的、有深度的过程反思，而不是泛泛而谈。

**核心要点**：
1.  **情感化框架**: “Wow!”、“Aha!”、“Uh-oh...”这个框架非常直观，且富含情感色彩。它鼓励学员分享个人化的、真实的感受，而不是做正式的“学习汇报”。
2.  **全面覆盖**: 这个框架覆盖了学习过程中的三个关键体验：正向的情感体验（Wow），认知上的突破（Aha），以及遇到的障碍（Uh-oh）。这使得反思更为全面。
3.  **引导积极归因**: 通过首先分享积极的“Wow”和“Aha”时刻，可以将整个访谈的基调定在积极和成长上，使得分享“Uh-oh”时刻也变成了一种对“如何克服困难”的探讨，而不是单纯的抱怨。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 引导高阶思维：从“做什么”到“如何定义”
本环节旨在拔高学员的思维层次，从“实现一个功能”提升到“如何清晰地定义一个复杂功能”，为下一模块的学习做铺垫。

**核心要点**：
1.  **聚焦“思路”而非“结果”**: 明确说明“不检验结果，只思考思路”，降低学员的压力，将他们的注意力引导到更高阶的“需求定义”和“问题分解”能力上。
2.  **区分需求类型**: 通过两个挑战的对比，引导学员自然地辨析“视觉需求”和“逻辑需求”的异同，前者更侧重“描述”，后者更侧重“步骤”。
3.  **启发式提问**: 教师的提问是开放式的（“怎么用自然语言描述？”、“难点在哪里？”），旨在激发学员的思考和讨论，而不是灌输标准答案。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供Prompt范例（视觉类）
在学员讨论结束后，提供一个高质量的Prompt范例，可以帮助他们固化认知，并学习到专业的需求描述方法。

**核心要点**：
1.  **展示“专业范本”**: 给出一个结构清晰、要素齐全的Prompt，作为学员未来模仿的标杆。
2.  **提炼关键要素**: 明确总结出定义一个视觉需求的关键三要素（“触发时机”、“动画效果”、“持续时间”），为学员提供一个可复用的“清单”，便于他们未来检查自己的Prompt是否完备。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供Prompt范例（逻辑类）
这个范例旨在向学员展示如何定义一个复杂的、包含状态管理的逻辑需求。

**核心要点**：
1.  **展示“算法思维”**: 这个分步的Prompt，本质上就是用自然语言在描述一个“算法”。它向学员展示了“编程思维”的核心——将一个任务分解为一系列精确的、有时序的步骤。
2.  **引入“状态”概念**: 通过“创建列表”、“检查列表”、“加入列表”这三个步骤，非常直观地向学员引入了程序需要“记忆”和“状态管理”的概念。
3.  **承前启后**: 明确指出“这正是模块二要深入学习的思维方式”，为下一个模块的学习建立了强烈的动机和清晰的衔接。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 激发创意，拓展边界
在学员已有的成功基础上，本环节旨在通过“创意风暴”来进一步激发他们的想象力，并为接下来的“导师演示”做铺垫。

**核心要点**：
1.  **肯定现有成果**: 首先肯定学员已有的“老虎机”式实现，给予价值感。
2.  **引入新维度**: 提出“随机性的表现形式”这一新维度，引导学员从“实现功能”的思维，转向“创意表达”的思维。
3.  **开放式提问**: “看一些其他的可能性...”是一个开放式的邀请，旨在激发学员的好奇心。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 拓展创意思维的边界
这两页幻灯片通过密集的、可视化的创意轰炸，旨在快速拓展学员对“可能性”的认知。

**核心要点**：
1.  **分类展示**: 将创意分为“自然”、“科技”、“游戏”、“艺术”四大类，有助于学员结构化地吸收信息，并能快速找到自己感兴趣的方向。
2.  **视觉辅助**: 每个类别都配有高质量的图片，视觉化地传达了创意的核心意象，比纯文字描述更具冲击力和启发性。
3.  **激发行动**: 目的不是让学员觉得“这太难了”，而是让他们感到“哇，这个好酷，我也想试试！”，激发他们课后继续探索和实践的欲望。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“天花板”，激发“愿景”
在进行了充分的创意激发后，“导师魔法秀”环节旨在通过一个高质量的成品，向学员展示本阶段能力的“天花板”，给他们树立一个可以追求的愿景。

**核心要点**：
1.  **成果展示**: 一个惊艳的、超出预期的Demo，是激发学员学习热情的最强催化剂。
2.  **连接理论**: 导师应在演示时，口头说明这个Pro版是如何结合了“创意构思”（如星空主题）和“进阶功能”（如避免重复）的，将演示与之前的教学内容联系起来。
3.  **榜样作用**: 导师亲自演示，其本身就是一种“以身作则”，表明导师也在使用同样的方法与AI协作，这能极大地增强学员对课程方法论的信任感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 模块核心思想升华
在所有活动和演示结束后，本页旨在对整个“思想破冰”模块的核心思想进行终极升华和总结。

**核心要点**：
1.  **“鸿沟”隐喻**: 用“鸿沟”和“桥梁”这个强大的隐喻，来形象化地总结AI编程带来的革命性变化，易于理解和记忆。
2.  **重新定义核心能力**: 再次强调，新的核心能力是“分析问题”和“清晰传达”，而不是“记忆语法”，巩固学员的信心。
3.  **价值拔高**: “能力的平权”这个说法，将AI编程的意义从“一个好用的工具”提升到了“赋予普通人创造能力”的更高层面，能引发学员更深层次的共鸣和认同。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 解答深层焦虑，确立人类价值
本页旨在正面回应学员心中可能存在的“被AI取代”的深层焦虑，清晰地定义在人机协作中，人类不可替代的价值。

**核心要点**：
1.  **直面问题**: 主动提出“我们的价值在哪里”这个问题，表明教师理解并重视学员的顾虑。
2.  **价值锚定**: 将人类的价值锚定在“领域知识”、“批判性思维/共情”和“创新/愿景”这三个AI难以企及的高层次能力上。这对于作为教育工作者的学员来说，极具说服力。
3.  **精妙比喻**: “AI是画笔，你是艺术家”这个比喻，形象、优雅且极具力量感，是本页乃至本模块的点睛之笔，能极大地提升学员的自我价值认同。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 系统性地总结模块收获
在模块的最后，用一页清晰的幻灯片，系统性地为学员总结本模块的收获，能极大地提升他们的获得感和满足感。

**核心要点**：
1.  **多维度总结**: 总结的维度覆盖了“思维”、“工具”、“技能”、“情感”四个层面，让学员感觉到收获是全方位的、立体的。
2.  **清晰的可视化**: “✅”清单加上“宝箱”的配图，在视觉上就传递出一种“收获满满”的感觉，非常直观。
3.  **正向强化**: 再次肯定学员的成就，给予积极的正向反馈，为模块画上一个圆满的句号。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 承前启后，建立学习动机
作为最后一页，它的核心任务是“承前启后”——总结过去，并为下一阶段的学习建立强烈的动机。

**核心要点**：
1.  **明确主题**: 清晰地预告了模块二的主题是“与AI对话”，以及核心内容是“编程基础（变量、条件、循环）”。
2.  **建立学习动机**: 它没有简单地罗列知识点，而是强调了学习这些知识点的“目的”——“下达更精确的指令”、“理解它们的作用和威力”。这让学员明白，学习这些规则是为了让自己变得更强大。
3.  **教学法重申**: 再次强调了本课程的教学方法——“在指挥AI使用的过程中理解”，而不是死记硬背，给学员吃下一颗定心丸，让他们对看起来很技术的模块二也不会感到恐惧。

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