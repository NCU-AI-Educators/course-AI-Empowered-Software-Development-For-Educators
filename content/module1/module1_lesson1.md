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
</style>

# 模块一: AI编程新纪元 (思想破冰)
## 第1节课: 导论 & 现场魔法秀

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

---

## 欢迎！这不是一门传统的编程课

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

---

## 现场魔法秀：AI编程的五重“魔法”

接下来，我们将现场见证AI如何仅凭几句“人话”，就为我们创造出五个风格迥异、逻辑复杂的应用。

1.  **第一重魔法**: 可交互的物理世界
2.  **第二重魔法**: 交互式3D数字模型
3.  **第三重魔法**: 创造性的抽象建模
4.  **第四重魔法**: 富有生命力的UI设计
5.  **第五重魔法**: 交互式的数据可视化

*（本节课，我们将欣赏AI的“表演”，课后你将有机会亲自尝试这些“魔法”）*

--- 

## 第一重魔法：可交互的物理世界

**物理老师的需求**：我需要一个能向学生直观演示力学原理的3D沙盒。比如，一个建筑在定向爆破下的结构拆解过程，要求完全符合物理规律，并有爆炸、烟尘等视觉特效。

给AI的“实验设计方案” ：
<div style="display: flex; gap: 20px; font-size: 16px; line-height: 1.4;">
<pre style="flex: 1; white-space: pre-wrap; word-wrap: break-word; margin: 0; padding: 1em; background-color: #f5f5f5; border-radius: 5px;"><code>使用 three.js, cannon-es.js 生成一个震撼的3D建筑拆除演示。

&#35;&#35; 场景设置：
&#45; 地面是一个深灰色混凝土平面，尺寸80*80，
&#45; 所有物体严格遵循现实物理规则，包括重力、摩擦力、碰撞检测和动量守恒

&#35;&#35; 建筑结构：
&#45; 一座圆形高层建筑，周长对应20个方块
&#45; 建筑总高度60个方块
&#45; 每层采用砖砌结构，方块与砖结构建筑一致, 错开50%排列，增强结构稳定性
&#45; 建筑外墙使用米色方块
&#45; &#42;&#42;重要：方块初始排列时必须确保紧密贴合，无间隙，可以通过轻微重叠或调整半径来实现&#42;&#42;
&#45; &#42;&#42;重要：建筑初始化完成后，所有方块应该处于物理"睡眠"状态，确保建筑在爆炸前保持完美的静止状态，不会因重力而下沉或松散&#42;&#42;
&#45; 建筑砖块之间使用粘性材料填充（不可见），通过高摩擦力（0.8+）和低弹性（0.05以下）来模拟粘合效果
&#45; 砖块在建筑倒塌瞬间不会散掉，而是建筑作为一个整体倒在地面的时候才因受力过大而散掉
</code></pre>
<pre style="flex: 1; white-space: pre-wrap; word-wrap: break-word; margin: 0; padding: 1em; background-color: #f5f5f5; border-radius: 5px;"><code>&#35;&#35; 定向爆破系统：
&#45; 在建筑的第1层的最右侧方块附近安装爆炸装置（不可见）
&#45; 提供操作按钮点击爆炸
&#45; &#42;&#42;爆炸时唤醒所有相关方块的物理状态&#42;&#42;
&#45; 爆炸点产生半径2的强力冲击波，冲击波影响到的方块, 受到2-5单位的冲击力

&#35;&#35; 建筑稳定性要求：
&#45; &#42;&#42;确保建筑在未爆炸时完全静止，无任何晃动或下沉&#42;&#42;
&#45; &#42;&#42;物理世界初始化后给建筑几个物理步骤来自然稳定，或使用睡眠机制&#42;&#42;
&#45; &#42;&#42;方块间的接触材料应具有高摩擦力和极低弹性，模拟砖块间的砂浆粘合&#42;&#42;

&#35;&#35; 震撼的倒塌效果：
&#45; 方块在爆炸冲击下不仅飞散，还会在空中翻滚和碰撞
&#45; 烟尘会随着建筑倒塌逐渐扩散，营造真实的拆除现场氛围

&#35;&#35; 增强的视觉效果：
&#45; 添加环境光照变化：爆炸瞬间亮度激增，然后被烟尘遮挡变暗
&#45; 粒子系统包括：烟雾、灰尘

&#35;&#35; 技术要求：
&#45; 粒子系统用于烟雾和灰尘效果
&#45; 所有代码集成在单个HTML文件中，包含必要的CSS样式
&#45; 添加简单的UI控制：重置按钮、相机角度切换, 爆炸按钮, 鼠标左键控制摄像机角度，
  右键控制摄像机位置，滚轮控制摄像机焦距
</code></pre>
</div>

---

## 结果：AI构建了“物理沙盒”

AI收到这份详尽的“脚本”后，为我们生成了一个完整的、可交互的物理模拟世界。

![An animated GIF showing a 3D building demolition simulation height:400px](../../../lectures/images/2025-10-25-16-28-16.png)

**AI展示了它对复杂需求和专业领域知识（物理引擎）的惊人理解力。**

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

## 第二重魔法：交互式3D数字模型

**地理老师的需求**：我需要一个可以交互的3D地球，用来给学生们展示地理信息，并且希望它能自己旋转，背景里还有星星。

**给AI的指令**：
> 请创建一个独立的HTML文件，使用Three.js渲染一个3D地球。这个地球必须有逼真的彩色地球纹理，可以交互（通过鼠标旋转和缩放），并且背景中要带有星星。地球本身也需要缓慢地自转。

---

## 结果：AI生成了“数字地球仪”

AI不仅理解了3D建模的需求，还正确地引入了“地球纹理”这一外部数据。

![A stunning, interactive 3D globe generated by AI height:400px](../../../lectures/images/2025-10-25-16-29-52.png)

**AI展示了它整合外部数据并创造交互式应用的能力。**

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

## 第三重魔法：创造性的抽象建模

**社会学老师的需求**：我希望能有一种方式，可视化地展示人群中的社交网络，或者知识的传播路径，让学生直观地感受到“连接”的存在。

**给AI的指令**：
> 请创建一个独立的HTML文件，其中包含一个全屏的画布。画布上要有浮动的、发光的粒子动画，当粒子彼此靠近时，它们之间会用线条连接。粒子动画还需要对鼠标的移动做出反应。

---

## 结果：AI生成了“关系宇宙”

这个看似抽象的、充满艺术感的“粒子宇宙”，可以完美地用来隐喻各种“关系”的可视化。

![An interactive particle system with connecting lines height:400px](../../../lectures/images/2025-10-25-16-31-11.png)

**AI展示了它将抽象概念转化为可视化作品的创造力。**

---

## 第四重魔法：富有生命力的UI设计

**美术老师/设计师的需求**：我希望能为我的网页或课件添加一些生动、有趣的视觉元素，比如根据天气动态变化的小卡片，但我不想学复杂的动画软件。

**给AI的指令**：
> 创建一个包含CSS和JavaScript的单一HTML文件，用于生成一组动画天气卡片。每个卡片应通过独特的动画直观地表示一种天气状况：风（移动的云，摇曳的树），雨（下落的雨滴），晴（旋转的光芒），雪（飘落的雪花）。将所有卡片并排显示，背景为深色。所有代码都在一个文件中。

---

## 结果：AI生成了“天气心情卡片”

AI利用纯粹的CSS动画，为我们创造了一组生动活泼的UI组件。

![Weather Animation Demo height:400px](../../../lectures/images/2025-10-25-16-31-57.png)

**AI展示了它在UI设计和前端开发中的创造力，能够将简单的想法转化为富有生命力的视觉元素。**

---

## 第五重魔法：交互式的数据可视化

**经济学老师的需求**：我需要为我的经济学或社会学课程制作一个数据可视化图表，用来展示一个国家或地区复杂的能源流动情况。图表需要清晰、美观，并且能够交互，让学生可以直观地看到数据的流向和比例。

**给AI的指令**：
> 创建一个独立的HTML文件，使用ECharts图表库来渲染一个桑基图。数据源使用一个复杂的、多层级的能源流向JSON数据集。图表需要适配深色主题，并且可以交互。

---

## 结果：AI绘制了“能量流动桑基图”

AI不仅找到了合适的图表库和真实的数据集，还正确地处理了数据格式，最终生成了一个极具视觉冲击力的、复杂的数据可视化作品。

![Sankey Diagram Demo height:400px](../../../lectures/images/2025-10-25-16-32-25.png)

**AI展示了它在数据分析、数据处理和高级图表生成方面的专业能力。**

---

## “魔法”揭秘：什么是AI辅助编程？

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

---

## 思维的转变：编程学习的颠覆

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

---

## 这对你（教育工作者）意味着什么？

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

---

## 你的学科，你的魔法

**这股力量，正在赋能所有学科：**

*   **对于文科教师**: 瞬间分析数百篇数字化文献，自动提取关键词或进行情感分析。
*   **对于理科教师**: 自动处理繁杂的实验数据，从海量数据中绘制图表。
*   **对于经管教师**: 编写一个网络爬虫，实时获取并分析市场数据。
*   **对于艺术教师**: 将一个抽象的设计理念，快速生成数十种视觉方案。

**无论你的领域是什么，AI都能成为你专属的超级研究助理。**

---

## 我们的学习路径概览

这是一个从思想到工具，再到创造的完整旅程。

<div style="text-align: center;">

![学习路径图 width:1024px](../../../lectures/images/2025-10-26-17-01-49.png)

*图：课程学习路径概览*

</div> 





---

## 课堂互动：你的“痛点”是什么？

请花两分钟思考一下：

1.  在你的教学或科研中，是否存在大量**重复、耗时**的工作？
2.  你是否曾有一个想法，但因为**技术限制**而无法实现？

*欢迎在课程群或线上讨论区分享，这些都可能成为你未来AI赋能软件开发的灵感来源！*

---

## 下一步预告

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