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
![bg blur:5px brightness:60%](../../../lectures/images/2025-10-25-18-45-29.png)

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
## 第1节课: 导论 & 现场魔法秀

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 开场
第一页幻灯片的目标是营造一种沉浸感和期待感，而不是传统的“老师好，今天我们讲第一章”的枯燥开场。背景图的选择、标题的层级，都是为了从视觉上就告诉学员：这门课不一样。

**核心要点**：
1.  **建立身份**: 明确课程、模块和讲师信息。
2.  **设定基调**: “思想破冰”和“魔法秀”这两个词，直接定义了第一节课的核心任务——打破思维定式，展示AI编程的惊艳效果，激发学员的好奇心和学习兴趣。
3.  **降低焦虑**: 开宗明义，这不是一门传统的编程课，目的是让零基础的学员从一开始就放下对“编程”的恐惧。

</div>

---

## **欢迎！这不是一门传统的编程课**

<div class="columns ratio-6-4">
<div>

这是一个关于**思维转变**的旅程：

- 从 “我不会编程” 到 **“我能指挥AI编程”**
- 从 “技术恐惧” 到 **“技术赋能”**
- 从 “软件的被动使用者” 到 **“工具的主动创造者”**

</div>
<div class="align-top-center">

![width:450px](../../../lectures/images/2025-10-25-18-43-20.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 确立核心价值
这一页是本课程的“价值观宣言”。对于零基础的学员，最大的障碍是心理上的恐惧和自我设限。因此，在展示任何技术细节之前，必须先从思想上为他们“松绑”。

**核心要点**：
1.  **重新定义“会编程”**: 将学员的注意力从“写代码”这个行为，转移到“指挥AI”这个更高层次的、更侧重逻辑与沟通的思维活动上。这极大地降低了入门门槛。
2.  **强调“赋能”而非“学习”**: 课程的价值主张是“技术赋能”，是让你获得解决实际问题的能力，而不是仅仅学会一门技术。这更能激发作为教育工作者的学员的学习动机。
3.  **点燃“创造者”火焰**: “主动创造者”这个身份，远比“学习者”更具吸引力。它暗示着课程的产出是实实在在的、有用的个人作品，符合“作品导向”的教学哲学。

</div>

---

## **现场魔法秀：AI编程的五重“魔法”**

接下来，我们将现场见证AI如何仅凭几句“人话”，就为我们创造出五个风格迥异、逻辑复杂的应用。

1.  **第一重魔法**: 可交互的物理世界
2.  **第二重魔法**: 交互式3D数字模型
3.  **第三重魔法**: 创造性的抽象建模
4.  **第四重魔法**: 富有生命力的UI设计
5.  **第五重魔法**: 交互式的数据可视化

*（本节课，我们将欣赏AI的“表演”，课后你将有机会亲自尝试这些“魔法”）*

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 建立认知框架
这一页是“魔法秀”的目录，其核心教学目标是“建立认知框架”和“管理预期”。

**核心要点**：
1.  **结构化展示**: 将演示内容结构化为“五重魔法”，让学员对即将发生的事情有一个清晰的预期，而不是一头雾水地被动观看。
2.  **覆盖广度**: 五个例子的选择，特意覆盖了从理科（物理）、文科（地理、社会学）到艺术（UI设计）、商科（数据可视化）等不同领域，目的是让所有背景的老师都能看到与自己相关的可能性，产生代入感。
3.  **预期管理**: 最后一句斜体字非常关键。它告诉学员，今天你们的角色是“欣赏”，而不是“跟练”，避免他们因为看到复杂的效果而产生新的焦虑。同时，也埋下伏笔，“课后你将有机会亲自尝试”，维持了他们的期待感。

</div>

--- 

## **第一重魔法：可交互的物理世界**

**物理老师的需求**：我需要一个能向学生直观演示力学原理的3D沙盒。比如，一个建筑在定向爆破下的结构拆解过程，要求完全符合物理规律，并有爆炸、烟尘等视觉特效。

给AI的“实验设计方案” ：

<div class="columns" style="display: grid; grid-template-columns: 1fr; gap: 1rem; font-size: 16px;">
<pre style="white-space: pre-wrap; margin: 0; padding: 1em; background-color: #f5f5f5; border-radius: 5px; overflow-wrap: break-word; overflow-x: auto;"><code>使用 three.js, cannon-es.js 生成一个震撼的3D建筑拆除演示。
<br>
## **场景设置：**
- 地面是一个深灰色混凝土平面，尺寸80*80，
- 所有物体严格遵循现实物理规则，包括重力、摩擦力、碰撞检测和动量守恒
<br>
## **建筑结构：**
一座圆形高层建筑，周长对应20个方块
- 建筑总高度60个方块
- 每层采用砖砌结构，方块与砖结构建筑一致, 错开50%排列，增强结构稳定性
- 建筑外墙使用米色方块
- **重要：方块初始排列时必须确保紧密贴合，无间隙，可以通过轻微重叠或调整半径来实现**
- **重要：建筑初始化完成后，所有方块应该处于物理"睡眠"状态，确保建筑在爆炸前保持完美的静止状态，不会因重力而下沉或松散**
- 建筑砖块之间使用粘性材料填充（不可见），通过高摩擦力（0.8+）和低弹性（0.05以下）来模拟粘合效果
- 砖块在建筑倒塌瞬间不会散掉，而是建筑作为一个整体倒在地面的时候才因受力过大而散掉
<br>
## 定向爆破系统：
- 在建筑的第1层的最右侧方块附近安装爆炸装置（不可见）
- 提供操作按钮点击爆炸
- **爆炸时唤醒所有相关方块的物理状态**
- 爆炸点产生半径2的强力冲击波，冲击波影响到的方块, 受到2-5单位的冲击力
<br>
## **建筑稳定性要求：**
- **确保建筑在未爆炸时完全静止，无任何晃动或下沉**
- **物理世界初始化后给建筑几个物理步骤来自然稳定，或使用睡眠机制**
- **方块间的接触材料应具有高摩擦力和极低弹性，模拟砖块间的砂浆粘合**
<br>
## **震撼的倒塌效果：**
- 方块在爆炸冲击下不仅飞散，还会在空中翻滚和碰撞
- 烟尘会随着建筑倒塌逐渐扩散，营造真实的拆除现场氛围
<br>
## **增强的视觉效果：**
- 添加环境光照变化：爆炸瞬间亮度激增，然后被烟尘遮挡变暗
- 粒子系统包括：烟雾、灰尘
<br>
## **技术要求：**
- 粒子系统用于烟雾和灰尘效果
- 所有代码集成在单个HTML文件中，包含必要的CSS样式
- 添加简单的UI控制：重置按钮、相机角度切换, 爆炸按钮, 鼠标左键控制摄像机角度，右键控制摄像机位置，滚轮控制摄像机焦距
</code></pre>
</div>

---

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“精确描述”的力量
这个案例的重点不是物理模拟本身，而是展示Prompt的“精确性”和“结构性”。

**核心要点**：
1.  **领域相关性**: 这是一个典型的、与学科教学深度结合的需求。它告诉学员，AI编程不是玩具，而是可以用来创造专业教学工具的。
2.  **Prompt即设计**: 展示的“实验设计方案”实际上就是软件工程中的“需求规格说明书”。通过这个例子，让学员初步感知到，与AI协作的核心，是将模糊的想法转化为清晰、无歧义、结构化的指令。
3.  **高亮关键指令**: Prompt中用`**重要**`高亮的几个稳定性要求，是这个模拟能否成功的关键。这暗示了在与AI协作时，识别并强调核心约束条件的重要性。

</div>

---

## **结果：AI构建了“物理沙盒”**

AI收到这份详尽的“脚本”后，为我们生成了一个完整的、可交互的物理模拟世界。

![An animated GIF showing a 3D building demolition simulation height:400px](../../../lectures/images/2025-10-25-16-28-16.png)

**AI展示了它对复杂需求和专业领域知识（物理引擎）的惊人理解力。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 建立“结果-输入”的强关联
这一页的核心是验证。它用一个震撼的、符合预期的结果，来证明上一页那个详尽的Prompt是有效的、值得的。

**核心要点**：
1.  **即时反馈**: 强有力的视觉结果，能给初学者带来巨大的震撼和信心，让他们直观地感受到AI的能力上限非常高。
2.  **归因分析**: 明确地将成功的结果归因于“详尽的脚本”。这强化了上一页的核心观点：Prompt的质量决定了输出的质量。
3.  **引入专业概念**: 简单提及“物理引擎”和“3D渲染库”，是为了让学员意识到，AI能够驾驭和整合非常专业的第三方工具库来完成复杂任务。这拓展了他们对AI能力的想象空间。

</div>

---

<style scoped>
blockquote {
  font-size: 22px !important;
  background-color: #f3f3f3;
  border-left: 5px solid #ccc;
  padding: 1em;
  margin-left: 0;
  margin-right: 0;
}
</style>

## **第二重魔法：交互式3D数字模型**

**地理老师的需求**：我需要一个可以交互的3D地球，用来给学生们展示地理信息，并且希望它能自己旋转，背景里还有星星。

**给AI的指令**：
> 请创建一个独立的HTML文件，使用Three.js渲染一个3D地球。这个地球必须有逼真的彩色地球纹理，可以交互（通过鼠标旋转和缩放），并且背景中要带有星星。地球本身也需要缓慢地自转。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“整合外部数据”的能力
这个案例比上一个简单，但它引入了一个新的维度：整合外部资源（地球纹理图片）。

**核心要点**：
1.  **简洁Prompt**: 与上一个复杂的需求相比，这个案例的Prompt相对简洁。这可以让学员理解，Prompt的详略取决于需求的复杂度，并非越长越好。
2.  **数据与代码分离**: “逼真的彩色地球纹理”这个要求，暗示了程序需要加载一个外部的图片文件。这让学员初步接触到“代码”和“数据”相分离的概念，一个程序不仅包含逻辑，还常常需要消耗外部资源。
3.  **应用的广泛性**: 数字地球仪是一个非常通用且吸引人的例子，几乎所有老师都能想象出在自己的课堂上使用它的场景，进一步加强了课程的吸引力。

</div>

---

## **结果：AI生成了“数字地球仪”**

AI不仅理解了3D建模的需求，还正确地引入了“地球纹理”这一外部数据。

![A stunning, interactive 3D globe generated by AI height:360px](../../../lectures/images/2025-10-25-16-29-52.png)

**AI展示了它整合外部数据并创造交互式应用的能力。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 强化“能力维度”的认知
每个案例后的总结页，都在为一个核心目标服务：帮助学员构建对AI能力的系统认知。

**核心要点**：
1.  **总结提炼**: 将具体的案例（数字地球仪）提炼、拔高到一个抽象的能力维度（“整合外部数据并创造交互式应用”）。这种“具体-抽象”的教学方法，有助于学员形成结构化的知识体系。
2.  **建立信心**: 通过一次次成功的展示，不断强化“AI很强大”的印象，从而让学员对“我指挥AI也能做到”这件事产生更强的信心。

</div>

---

<style scoped>
blockquote {
  font-size: 22px !important;
  background-color: #f3f3f3;
  border-left: 5px solid #ccc;
  padding: 1em;
  margin-left: 0;
  margin-right: 0;
}
</style>

## **第三重魔法：创造性的抽象建模**

**社会学老师的需求**：我希望能有一种方式，可视化地展示人群中的社交网络，或者知识的传播路径，让学生直观地感受到“连接”的存在。

**给AI的指令**：
> 请创建一个独立的HTML文件，其中包含一个全屏的画布。画布上要有浮动的、发光的粒子动画，当粒子彼此靠近时，它们之间会用线条连接。粒子动画还需要对鼠标的移动做出反应。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“抽象概念可视化”的能力
这个案例的独特之处在于它的“开放性”和“艺术性”。它旨在打破学员“AI只能做理工科任务”的刻板印象。

**核心要点**：
1.  **文科应用场景**: “社交网络”、“知识传播”是典型的人文社科研究对象。这个案例能极大地激发文科背景教师的兴趣。
2.  **从“具体”到“抽象”**: 前两个例子都是模拟真实世界（建筑、地球），而这个例子是创造一个不存在的、用于隐喻的视觉模型。它展示了AI不仅能“再现”，还能“表现”。
3.  **描述性Prompt**: 这个Prompt没有给出精确的物理参数或数据来源，而是用感性的、描述性的语言（“浮动的、发光的粒子”）来定义需求。这告诉学员，与AI的沟通方式是多样的，既可以是精确的“说明书”，也可以是充满想象力的“诗篇”。

</div>

---

## **结果：AI生成了“关系宇宙”**

这个看似抽象的、充满艺术感的“粒子宇宙”，可以完美地用来隐喻各种“关系”的可视化。

![An interactive particle system with connecting lines height:400px](../../../lectures/images/2025-10-25-16-31-11.png)

**AI展示了它将抽象概念转化为可视化作品的创造力。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 激发学员的“创造性联想”
这一页的目的是让学员不仅仅是“看”，更是“想”。

**核心要点**：
1.  **开放性诠释**: 讲师在逐字稿中，主动给出了多种诠释方式（“同学关系网”、“信息传播路径”等），目的是引导学员进行发散思维，让他们思考：“这个东西，我能用到我的学科里做什么？”
2.  **强调“创造力”**: 将AI的能力从“执行”拔高到“创造”的层面。这会进一步激发学员的创作欲望，让他们感觉自己指挥的不是一个工具，而是一个有创造潜能的伙伴。

</div>

---

## **第四重魔法：富有生命力的UI设计**

**美术老师/设计师的需求**：我希望能为我的网页或课件添加一些生动、有趣的视觉元素，比如根据天气动态变化的小卡片，但我不想学复杂的动画软件。

**给AI的指令**：
> 创建一个包含CSS和JavaScript的单一HTML文件，用于生成一组动画天气卡片。每个卡片应通过独特的动画直观地表示一种天气状况：风（移动的云，摇曳的树），雨（下落的雨滴），晴（旋转的光芒），雪（飘落的雪花）。将所有卡片并排显示，背景为深色。所有代码都在一个文件中。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“前端开发与UI设计”能力
这个案例非常贴近老师们制作课件或网页的实际需求，具有很强的实用性。

**核心要点**：
1.  **低代码/无代码场景**: 这个需求的核心是“不想学复杂技术”。它完美地展示了AI如何成为一种“超级视觉外包”，让非技术人员也能创造出专业级的视觉效果。
2.  **组件化思维**: “一组动画天气卡片”这个概念，向学员初步渗透了“组件化”的开发思想。这些卡片就像一个个独立的积木，可以被轻松地应用到不同的网页或课件中。
3.  **CSS的艺术性**: 这个例子也展示了，有时候实现惊艳的视觉效果，并不需要动用大型的框架或库，纯粹的CSS和JS也能创造出“魔法”。

</div>

---

## **结果：AI生成了“天气心情卡片”**

AI利用纯粹的CSS动画，为我们创造了一组生动活泼的UI组件。

![Weather Animation Demo height:360px](../../../lectures/images/2025-10-25-16-31-57.png)

**AI展示了它在UI设计和前端开发中的创造力，能够将简单的想法转化为富有生命力的视觉元素。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 连接“已知”与“未知”
老师们可能不熟悉CSS，但都用过PPT里的动画。这个案例起到了一个桥梁作用。

**核心要点**：
1.  **降低认知负荷**: 将复杂的CSS动画，类比为PPT动画，让学员在自己熟悉的领域内去理解这个新事物，可以有效降低学习的焦虑感。
2.  **强调“组件”价值**: 再次强调这些卡片是可复用的“UI组件”，强化了其作为“素材”或“积木”的价值，让学员能立刻想到“这个东西我可以直接拿来用”。

</div>

---

## **第五重魔法：交互式的数据可视化**

**经济学老师的需求**：我需要为我的经济学或社会学课程制作一个数据可视化图表，用来展示一个国家或地区复杂的能源流动情况。图表需要清晰、美观，并且能够交互，让学生可以直观地看到数据的流向和比例。

**给AI的指令**：
> 创建一个独立的HTML文件，使用ECharts图表库来渲染一个桑基图。数据源使用一个复杂的、多层级的能源流向JSON数据集。图表需要适配深色主题，并且可以交互。

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 展示“专业数据处理与可视化”能力
这是五个案例中技术复杂度最高的，它展示了AI在专业数据科学领域的强大能力，是课程后半段（模块四、五）内容的“终极预告”。

**核心要点**：
1.  **引入专业工具库**: “ECharts”是一个业界知名的数据可视化库。这个例子告诉学员，AI不仅能写原生代码，还能熟练使用各种强大的第三方库。
2.  **数据处理能力**: 这个任务的隐藏难点是“数据处理”。AI需要理解桑基图所需的数据结构（包含节点和链接），并正确地格式化数据。这展示了AI作为“数据分析师”的潜力。
3.  **课程内容预告**: 这个案例直接对应了教学大纲中的模块五“AI数据分析师(下)”。通过这个惊艳的最终效果，可以极大地激发学员对后续课程的学习兴趣。

</div>

---

## **结果：AI绘制了“能量流动桑基图”**

AI不仅找到了合适的图表库和真实的数据集，还正确地处理了数据格式，最终生成了一个极具视觉冲击力的、复杂的数据可视化作品。

![Sankey Diagram Demo height:360px](../../../lectures/images/2025-10-25-16-32-25.png)

**AI展示了它在数据分析、数据处理和高级图表生成方面的专业能力。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 完成“信心闭环”
从第一个物理模拟到最后一个数据科学图表，五个案例难度和专业度层层递进，到这里完成了对学员的“信心构建”的闭环。

**核心要点**：
1.  **能力矩阵**: 五个案例共同构成了一个能力矩阵：物理模拟（专业领域）、3D建模（通用交互）、抽象可视化（文科艺术）、UI设计（前端开发）、数据科学（数据处理）。这全面地展示了AI的能力广度与深度。
2.  **从“魔法”到“工具”**: 在学员心中，AI的形象已经从一个看不懂的“魔法”，转变为一个虽然强大但可理解、可驾驭的“超级工具”。破冰任务完成。

</div>

---

## **“魔法”揭秘：什么是AI辅助编程？**

<div class="columns ratio-6-4">
<div>

刚才发生的一切，其核心是**人机协作**的新范式。

- **你的角色 (项目总监)**
  - 提出创意、定义问题
  - 清晰描述需求和逻辑
  - 评估最终结果

- **AI的角色 (高效程序员)**
  - 理解你的自然语言需求
  - 快速生成、实现代码
  - 执行重复性、模式化的任务

</div>
<div class="align-middle-center">

![width:500px](../../../lectures/images/2025-10-25-19-02-38.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 定义“人机关系”
这是本节课最重要的理论升华。在展示了足够多“是什么”之后，必须清晰地定义“如何做”以及“你是谁”。

**核心要点**：
1.  **角色重新定位**: “项目总监”这个比喻，极大地提升了学员的自我定位，让他们意识到自己是在从事一项创造性的、高层次的智力活动，而不是在学习一项“搬砖”的技能。
2.  **明确职责边界**: 清晰地划分了人和AI的职责。人的核心是“思考”（定义问题、描述逻辑），AI的核心是“执行”（生成代码）。这为后续所有课程的教学都奠定了理论基础。
3.  **建立伙伴关系**: 强调人与AI是“协作”的伙伴关系，而非“替代”关系，这有助于缓解部分学员可能存在的“被AI取代”的深层焦虑。

</div>

---

## **思维的转变：编程学习的颠覆**

<div class="columns ratio-6-4">
<div>

| | **传统编程** | **AI辅助编程** |
| :--- | :--- | :--- |
| **核心** | 学习并记忆**语法** | 分析并清晰**描述问题** |
| **角色** | 代码的**编写者** | 解决方案的**设计者** |
| **过程** | 从零开始，逐行构建 | 与AI协作，迭代优化 |
| **门槛** | 陡峭，需要大量时间 | 平缓，即时获得反馈 |

</div>
<div class="align-middle-center">

![width:500px](../../../lectures/images/2025-10-25-19-06-25.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 固化“新旧对比”的认知
通过一个清晰的表格，将新旧范式进行直接对比，能极大地强化认知，让学员深刻理解这场变革的本质。

**核心要点**：
1.  **从“记忆”到“描述”**: 这是核心能力的变化。它告诉学员，未来最重要的能力，不再是记住多少代码，而是能否将你的思想清晰、有条理地表达出来。这对教育工作者而言，是一个巨大的福音，因为“清晰表达”本就是我们的核心专业能力之一。
2.  **从“编写者”到“设计者”**: 这是身份的跃迁。再次强化了学员作为“创造者”的自我认同。
3.  **平缓的学习曲线**: “门槛平缓，即时反馈”是AI辅助编程能成功应用于零基础教学的关键。它解决了传统编程教学中“入门难，易放弃”的最大痛点。

</div>

---

## **这对你（教育工作者）意味着什么？**

<div class="columns ratio-6-4">
<div>

掌握AI编程，你将能够：

- **提升科研效率**: 自动化处理实验数据、文本语料、调查问卷...
- **孵化教学创新**: 为你的课堂量身打造专属的计算器、分析工具、演示软件...
- **赋能你的学生**: 将这种解决问题的新范式传授给学生，培养他们的创新能力。

</div>
<div class="align-middle-center">

![width:500px](../../../lectures/images/2025-10-25-19-08-36.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 连接“课程价值”与“个人需求”
这一页的目的是将课程的价值，与学员的三个核心身份（研究者、教学者、育人者）进行强绑定，让课程的价值变得具体、可感。

**核心要点**：
1.  **科研效率**: 这是很多高校教师的刚需，能迅速抓住他们的痛点。
2.  **教学创新**: 这是所有一线教师的追求，展示了将教学想法变为现实的可能性。
3.  **赋能学生**: 这是教育工作者的终极使命，将课程的价值提升到了“培养下一代”的高度，能引发学员更深层次的共鸣。

</div>

---

## **你的学科，你的魔法**

**这股力量，正在赋能所有学科：**

*   **对于文科教师**: 瞬间分析数百篇数字化文献，自动提取关键词或进行情感分析。
*   **对于理科教师**: 自动处理繁杂的实验数据，从海量数据中绘制图表。
*   **对于经管教师**: 编写一个网络爬虫，实时获取并分析市场数据。
*   **对于艺术教师**: 将一个抽象的设计理念，快速生成数十种视觉方案。

**无论你的领域是什么，AI都能成为你专属的超级研究助理。**

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 破除“学科壁垒”
这一页旨在进一步破除学员心中可能存在的“学科壁垒”，让每个人都找到自己的位置。

**核心要点**：
1.  **具体案例**: 为不同学科门类提供了非常具体、可操作的应用案例，而不是空泛的口号。
2.  **身份认同**: “超级研究助理”这个比喻，精准地切中了高校教师的需求，让他们能立刻感受到AI的实用价值。
3.  **激发想象**: “只受限于你的想象力”这句话，是在鼓励学员开始主动思考AI在自己领域内的应用，将他们从被动的知识接收者，转变为主动的需求发现者。

</div>

---

## **我们的学习路径概览**

这是一个从思想到工具，再到创造的完整旅程。

<div style="text-align: center;">

![学习路径图 width:1024px](../../../lectures/images/2025-10-26-17-01-49.png)

*图：课程学习路径概览*

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 提供“学习地图”
在课程的第一节课，给学员一张清晰的“学习地图”，对于稳定学习心态、建立长期目标至关重要。

**核心要点**：
1.  **可视化路径**: 用一张流程图来展示整个课程的结构，比纯文字更直观，更易于理解和记忆。
2.  **管理学习预期**: 地图清晰地标示了每个阶段的学习重点（编程基础 -> 数据分析 -> Web应用 -> 综合项目），让学员对未来的学习内容和难度有一个科学的预期。
3.  **建立全局观**: 这张图帮助学员从一开始就建立起对课程的全局观，让他们知道自己当前所学在整个知识体系中的位置，从而减少学习过程中的迷茫感。

</div>

---

## **课堂互动：你的“痛点”是什么？**

请花两分钟思考一下：

1.  在你的教学或科研中，是否存在大量**重复、耗时**的工作？
2.  你是否曾有一个想法，但因为**技术限制**而无法实现？

*欢迎在课程群或线上讨论区分享，这些都可能成为你未来AI赋能软件开发的灵感来源！*

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 连接“学习”与“应用”
这是一个非常重要的互动环节，它的目的是将课程学习的“外部动机”转化为“内部动机”。

**核心要点**：
1.  **问题导向学习 (PBL)**: 通过引导学员反思自己的“痛点”，将课程的学习目标与解决个人实际问题进行绑定。这是最有效的学习动机激发方式。
2.  **收集项目灵感**: 这个环节也是在为课程后期的“综合项目”收集素材和灵感。让学员从第一节课就开始构思自己的项目，可以极大地提升课程的参与度和最终的完成质量。
3.  **建立社群联结**: 鼓励学员在课程群里分享，可以促进学员之间的交流，为建立学习社群打下基础。

</div>

---

## **下一步预告**

<div class="columns ratio-6-4">
<div>

在下一节课中，我们将亲手搭建自己的AI编程环境。

- **目标**: 安装并配置好所有必需的工具。
- **内容**:
  - 安装 Python
  - 安装 VS Code 编辑器
  - 安装并授权 Qwen Code AI助手

为创造属于你自己的“魔法”做好准备！

</div>
<div class="align-middle-center">

![width:500px](../../../lectures/images/2025-10-25-19-11-00.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 清晰的“行为召唤”
课程的结尾需要一个清晰、具体、可执行的“下一步”，让学员明确知道下节课要做什么。

**核心要点**：
1.  **明确任务**: 清晰地列出了下节课的三个核心安装任务，让学员有备而来。
2.  **从“看”到“做”**: 明确地告知学员，课程将从“思想破冰”进入“动手实操”的阶段，完成了学习节奏的转换。
3.  **保持激励**: “为创造属于你自己的‘魔法’做好准备！”这句话，再次强化了课程的创造者导向，并保持了学员的学习热情和期待感。

</div>