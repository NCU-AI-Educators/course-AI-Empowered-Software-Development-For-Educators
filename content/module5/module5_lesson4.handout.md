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
.tip {
  background-color: #f0f8ff;
  border-left: 5px solid #1e90ff;
  padding: 15px 15px 0.1px; 
}
.insight {
  background-color: #eefcff; 
  border-left: 5px solid #17a2b8; 
  padding: 15px 15px 0.1px; 
}
.key-point {
  background-color: #fffbe6; 
  border-left: 5px solid #ffc107; 
  padding: 15px 15px 0.1px; 
}
.tip p, .tip li,
.insight p, .insight li,
.key-point p, .key-point li {
  font-size: inherit !important;
}
.styled-div p, 
.styled-div li, 
.styled-div ol, 
.styled-div ul, 
.styled-div blockquote {
  font-size: inherit !important;
}
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
![bg blur:3px brightness:60%](../../../lectures/images/2025-12-06-03-13-45.png)

<style scoped>
h1{
  color: #F5F5F5;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}
h2 {
  color: #E0E0E0;
  text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
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
}
</style>

<div class="course-title">AI赋能软件开发</div>

# 模块五: AI数据分析师(下)
## 第20节课: 实战工作坊——我的第一份数据报告

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 基于项目的学习 (PBL)
本节课采用 **Project-Based Learning (PBL)** 模式。
PBL 强调通过解决真实世界的问题来学习。与传统的“听讲-练习”模式不同，PBL 要求我们在复杂的、非结构化的问题情境中，综合运用多种知识和技能，最终产出具体的作品。

</div>

---

## **工作坊任务：你的专属分析报告**

<div class="columns ratio-6-4">
<div>

### **任务目标**
基于 `china_tourism.csv` 数据集，选择一个**非江西省**的目标省份（如四川、浙江、云南等），独立制作一份**全景分析报告**。

### **核心要素 (建议)**
1.  **资源分布**: 景区等级比例 (饼图)。
2.  **消费水平**: 门票价格分布 (小提琴图)。
3.  **性价比**: 价格与评分的关系 (散点图)。
4.  **相关性**: 价格与评分的量化关系 (热力图)。

</div>
<div class="align-middle-center">

![数据分析师正在工作的场景插图](../../../lectures/images/2025-12-06-03-16-27.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 迁移能力 (Transfer of Learning)
本任务的核心是考察**迁移能力**。
我们需要将针对“江西”的代码逻辑，应用到新的对象（其他省份）上。这要求我们不仅是复制粘贴代码，而是理解代码中的变量（如`jiangxi_cities`）与数据逻辑之间的关系。

</div>

---

## **Step 1: 选题与探查**

你需要知道你的目标省份有哪些城市在数据里。

**AI 指令建议**:
> "请帮我列出 `df['City']` 中包含的所有城市名称，并打印出来，方便我筛选属于 **[你的目标省份]** 的城市。"

**AI 优先策略**:
不要自己去百度城市列表，也不要手动翻 Excel。
**直接问 AI**。它知道中国所有的行政区划。

<div class="tip" style="font-size:0.6em">

💡 **AI 提示词**: 
"我有一个包含 `City` 列的 dataframe `df`。请帮我找出 `df['City']` 中所有属于 **[四川省]** 的城市，并生成一个列表 `my_cities`。"
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### AI 的知识库 (Knowledge Base)
AI 不仅是一个编程助手，更是一个百科全书。
在本例中，数据集中没有“省份”信息，如果用传统编程方法，我们需要手动建立“城市-省份”映射字典，非常繁琐。
但 AI 知道“成都属于四川”，利用这一特性，我们可以直接让 AI 帮我们完成**语义层面的筛选**，这是传统代码难以做到的。

</div>

---

## **Step 2: 综合实战 (Comprehensive Practice)**

### **任务：编制“全景报告”**
请综合应用本模块所学技能（**数据思维、视觉表达、AI 协作**），为你感兴趣的省份制作一份全景分析报告。

### **任务要求**
1.  **独立思考**: 没有现成的指令模板，请根据**分析目标**，自行设计 Prompt。
2.  **自主设计**: 请自行规划从“数据筛选”到“全景绘图”的完整分析流程。
    *   *提示：如果卡住了，可以参考课程提供的 Jupyter Notebook (`module5_all.ipynb`)。*
3.  **验证**: 检查代码是否运行报错，图表是否美观。

<div class="insight" style="font-size:0.6em">

🚀 **挑战**: 尝试修改图表的配色 (`palette`)，打造你的专属风格。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 综合应用 (Synthesis)
这是布鲁姆认知分类中的高阶能力。
本任务要求**您**同时调用三种核心能力：
1.  **数据思维**: 决定“筛选什么数据”（如过滤异常值）。
2.  **视觉表达**: 决定“用什么图表”（如小提琴图看分布）。
3.  **AI 协作**: 决定“怎么指挥AI”（编写 Prompt）。
这种**多维能力的实时整合**，才是解决复杂问题的关键。

</div>

---

## **Step 3: 成果展示与互评**

**展示环节**:
邀请 2-3 位学员上台展示分析报告。

**互评维度**:
1.  **完整性**: 是否包含了资源、消费、性价比、相关性等核心维度？
2.  **准确性**: 数据筛选逻辑是否严谨？图表是否准确反映了数据特征？
3.  **美观性**: 是否尝试了不同的配色或布局？图表是否清晰易读？
4.  **洞察力**: 能否基于图表讲出一个关于该省份的“数据故事”？

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 同行评审 (Peer Review)
在软件工程中，代码评审 (Code Review) 是保证质量的核心环节。
在数据分析中，**同行评审**同样重要。
- **纠偏**: 别人可能会发现你忽略的逻辑漏洞（如：是否剔除了异常值？）。
- **启发**: 别人的配色方案或分析视角（如：“火辣”的四川）可能会给你新的灵感。
学会 **“批判性地看”** 和 **“建设性地评”**，是**您**进阶的必修课。

</div>

---

## **模块结业：你已经是一名数据分析师了！**

<div class="columns ratio-6-4" style="font-size:0.9em">
<div>

### 回顾旅程
1.  **数据思维**: 学会了用数据（而非直觉）去验证假设。
2.  **工具升级**: 掌握了 Matplotlib 和 Seaborn，能画出专业级的统计图表。
3.  **AI 协作**: 习惯了“你出思路，AI 写代码”的高效工作流。
4.  **价值交付**: 从零开始，打造了一份真实的旅行分析报告。

### 下一站
**模块六 (Web开发)**:
我们将把这个分析脚本，变成一个**人人可用的网页 App**！

</div>

<div class="align-middle-center">

![](../../../lectures/images/2025-12-06-03-20-14.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据素养 (Data Literacy)
Gartner 将数据素养定义为：阅读、书写和交流数据的能力。
通过本模块的学习，**您**已经从一个单纯的“数据消费者”（看报表）进化为“数据生产者”（做报表）。
这种能力的跃迁，将极大地扩展**您**在数字化时代的教学和科研边界。

</div>

---

## **课后拓展 (Homework): 新的数据洞察报告**

<div class="columns ratio-4-6" style="font-size:0.9em">
<div>

### **进阶任务**
不要局限于旅游数据。
请尝试寻找一份**全新的数据集** 或者身边的数据，运用本模块所学技能，制作一份分析报告。

### **数据资源推荐**
*   **Kaggle**: 全球最大的数据科学社区。
*   **天池 (Aliyun)**: 中国的数据竞赛平台。
*   **和鲸社区 (Heywhale)**: 丰富的数据集和项目案例。

</div>
<div>

### **提交形式**
*   一份 Jupyter Notebook (`.ipynb`) 文件。
*   包含：数据读取、清洗、至少3种不同类型的图表、以及你的分析结论。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 开放数据运动 (Open Data Movement)
数据民主化是 AI 时代的重要趋势。
**Kaggle**: 成立于 2010 年，是全球最大的数据科学社区。它不仅提供数据集，还提供免费的 GPU 算力 (Kernels)。
鼓励**您**去探索这些平台，是因为真实世界的数据往往比课堂案例更复杂、更脏、也更有趣。处理这些“野生数据”的经验，是您成为高阶分析师的必经之路。

</div>