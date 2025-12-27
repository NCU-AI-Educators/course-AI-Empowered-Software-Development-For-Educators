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

![bg blur:3px brightness:60%](../../../lectures/images/2025-10-26-21-45-52.png)

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
## 第4节课: 首个AI应用发布会 & 创造者心得

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

---

## 本节课目标：庆祝我们的“首个产品发布会”！

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

---

## 环节一：应用博览会 (App Fair)

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

---

## 环节二：导演幕后访谈

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

---

## 环节三：进阶功能头脑风暴

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

---

### **挑战参考答案 (1/2): 视觉需求**

刚才我们一起探讨了实现思路，现在，让我们看看一份比较专业的“产品需求文档”（Prompt）会怎么写。

**对于“增加幸运感” (视觉需求):**
> 这是一个纯粹的视觉需求。我们可以这样对AI说：
>
> `“请优化我们之前的点名器。当名字滚动停止，最终选定一个名字后，请在那个名字周围增加一个持续1-2秒的、明亮的、金色的闪光或撒花庆祝动画效果。”`
>
> *（关键：清晰描述**触发时机**、**动画效果**和**持续时间**。）*

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

---

## 环节四：创意风暴 & 导师魔法秀

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

---

<style scoped>
section p,
section li {
  font-size: 0.8rem; /* 原本约 1.25rem */
}
</style>

### **创意构思：随机性的表现形式 (1/2)**

<div class="columns ratio-5-5">
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

![图片描述：蒲公英的种子在风中飞舞 width:500px](../../../lectures/images/2025-10-26-22-12-34.png)

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

---

## 跨越鸿沟：AI如何赋能我们成为创造者

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

---

## 人机协作：我们的核心价值在哪里？

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

---

## 模块一总结：我们收获了什么？

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

---

## 下一步预告：模块二 - 与AI对话 (编程基础)

<div class="columns ratio-6-4">
<div>

思想破冰之后，我们将开始了解编程的一些“核心规则”。

我们将学习如何下达更精确的指令，在指挥AI使用**变量、条件、循环**等核心概念的过程中，真正理解它们的作用和威力！

</div>
<div class="align-middle-center">

![图片描述：代表变量(x)、条件(if)、循环(loop)的编程积木 width:330px](../../../lectures/images/2025-10-26-23-02-43.png)

</div>
</div>

---

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
  margin-bottom: 20px; /* 控制标题和提示语的间距 */
}
p {
  font-size: 24px;
  color: #555;
  line-height: 1.5; /* 增加行高，让提示语更易读 */
}
</style>

# 课后练习

<p>

*小提示：别忘了，你的AI编程助手也是一位出色的学伴和老师！<br>当你对这些练习题有任何疑惑时，随时可以和它讨论，让它引导你完成思考。*

</p>

---

## **课后练习：“回响”——从“痛点”到“可编程时刻”**

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