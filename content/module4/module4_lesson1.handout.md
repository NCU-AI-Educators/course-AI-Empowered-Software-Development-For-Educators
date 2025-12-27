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
![bg blur:1px brightness:60%](../../../lectures/images/2025-11-27-11-25-06.png)

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

# 模块四: AI数据分析师(上)
## 第13节课: Pandas入门与数据读取——唤醒沉睡的数据

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据科学与数据分析的兴起
在当今的数字化时代,数据已成为最宝贵的资源之一。从科研到商业,从教育到医疗,几乎每个领域都在经历"数据驱动"的转型。**数据科学 (Data Science)** 作为一门交叉学科,融合了统计学、计算机科学和领域知识,旨在从数据中提取有价值的洞察。

**数据分析 (Data Analysis)** 是数据科学的核心环节,通常包括以下步骤:
1. **数据获取 (Data Acquisition)**: 从各种来源(数据库、文件、API等)收集数据。
2. **数据清洗 (Data Cleaning)**: 处理缺失值、异常值、重复数据等质量问题。
3. **数据转换 (Data Transformation)**: 对数据进行格式转换、特征工程等操作。
4. **数据分析 (Data Analysis)**: 使用统计方法和算法发现模式、趋势和关联。
5. **数据可视化 (Data Visualization)**: 通过图表直观地呈现分析结果。
6. **结果解释 (Interpretation)**: 将分析结果转化为可操作的洞察和建议。

本模块将聚焦于前4个步骤,使用Python生态系统中最强大的数据分析库——**Pandas**,帮助您建立数据分析的基础能力。

</div>

---

## **问题导入：如果你是学生们的“电竞教练”...**

<div class="columns ratio-6-4">
<div>

为了拉近与学生的距离，我们决定客串一把 **“电竞教练”**。我们手里有一份包含 **100+位英雄** 详细数据的Excel表格。

**你的任务**：帮学生们用**数据**科学上分，而不是盲目操作。
1. 找出当前版本 **胜率 (Win Rate)** 最高的英雄。
2. 统计 **法师 (Mage)** 和 **射手 (Archer)** 谁的平均胜率更高？
3. 分析 **Ban率 (Ban Rate)** 高的英雄，胜率是否也一定高？

</div>
<div>

![王者荣耀英雄海报拼图 vs 电脑屏幕上整齐的数据流 width:400px](../../../lectures/images/2025-11-27-11-28-34.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据驱动决策 (Data-Driven Decision Making)
本页通过"电竞教练"这一场景,向您介绍一个重要的现代决策理念:**数据驱动决策 (DDDM)**。

传统的决策往往依赖于经验、直觉或权威意见。而数据驱动决策则强调:
- **客观性**: 基于事实和数据,而非主观臆断。
- **可验证性**: 决策的依据可以被量化和验证。
- **可重复性**: 相同的数据和方法应该得出一致的结论。

在游戏领域,这种方法被称为"**元游戏分析 (Meta-game Analysis)**"。职业电竞团队会雇佣专门的数据分析师,通过分析海量对局数据来发现:
- 哪些英雄在当前版本强势(高胜率)?
- 哪些英雄组合有协同效应(Synergy)?
- 哪些策略在特定地图或阵容下更有效?

这种分析方法同样适用于您的教育工作。您可以通过分析学生的成绩数据、问卷数据等,发现教学中的问题,优化教学策略。本课程选择游戏数据作为切入点,正是因为它能帮助您在轻松的情境中理解数据分析的价值和方法,进而迁移到更严肃的教育科研场景中。

</div>

---

## **痛点：如果用Excel手动做...**

<div class="columns ratio-6-4">
<div>

**面对100+行数据，手动筛选统计：**

*   😵‍💫 **眼睛看花**：一行行找数据，容易遗漏。
*   🖱️ **鼠标点断**：反复筛选、复制、粘贴，操作繁琐。
*   ❌ **容易出错**：看错行、算错数是常有的事。

**结论**：我们需要更高效的工具！

</div>
<div>

![一个疲惫的人对着满屏Excel表格抓狂 width:400px](../../../lectures/images/2025-11-27-11-32-09.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 电子表格的局限性
**Microsoft Excel** 是世界上使用最广泛的数据处理工具之一,它为非技术用户提供了直观的界面来处理表格数据。然而,Excel在处理大规模数据分析时存在明显的局限性:

1. **可扩展性差 (Poor Scalability)**:
   - Excel的行数限制约为100万行,对于大数据集无能为力。
   - 随着数据量增加,Excel会变得极其缓慢,甚至崩溃。

2. **重复性工作 (Repetitive Tasks)**:
   - 每次数据更新,都需要手动重复相同的筛选、排序、计算操作。
   - 无法有效地"记录"和"复现"分析流程。

3. **容易出错 (Error-Prone)**:
   - 手动操作容易产生人为错误(如选错单元格、公式拖拽错误)。
   - 缺乏版本控制,难以追溯错误的来源。

4. **缺乏可重复性 (Lack of Reproducibility)**:
   - 科研中的"可重复性"是黄金标准。Excel的点击式操作难以被精确记录和复现。
   - 审稿人或同行无法验证您的分析步骤。

**编程式数据分析**(如使用Pandas)则完美地解决了这些问题:
- 代码可以处理任意规模的数据。
- 分析流程被完整地记录在脚本中,可以一键重复执行。
- 代码可以被版本控制(如Git),便于协作和审查。
- 分析过程透明、可验证、可复现。

这也是为什么现代科研越来越强调"**可重复性研究 (Reproducible Research)**",并推荐使用编程语言进行数据分析的原因。

</div>

---

## **本课学习目标**

<div class="columns">
<div>

学完这节课，你将能够：

1.  **理解** Pandas 和 DataFrame 的核心概念。
2.  **掌握** 使用 `pd.read_excel()` 读取数据的方法。
3.  **掌握** 使用 `df.head()` 和 `df.info()` 快速检查数据全貌。
4.  **完成** “王者荣耀英雄数据唤醒”的第一个微项目。

</div>
<div>

![配图占位符](../../../lectures/images/2025-11-27-11-34-15.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 学习目标的设计原则
本页的学习目标设计遵循了**布鲁姆认知层次理论 (Bloom's Taxonomy)** 的修订版框架。该理论将学习目标分为六个认知层次,从低到高依次为:记忆 (Remember)、理解 (Understand)、应用 (Apply)、分析 (Analyze)、评价 (Evaluate)、创造 (Create)。

本课的学习目标精心设计为:
1. **理解层次**: "理解 Pandas 和 DataFrame 的核心概念" - 要求您能够用自己的话解释这些概念,而非死记硬背。
2. **应用层次**: "掌握使用 `pd.read_excel()` 读取数据" 和 "掌握使用 `df.head()` 和 `df.info()` 检查数据" - 要求您能够在实际场景中运用这些方法。
3. **创造层次**: "完成'王者荣耀英雄数据唤醒'微项目" - 要求您综合运用所学知识,独立完成一个完整的任务。

这种**渐进式目标设计 (Progressive Learning Objectives)** 确保您不仅掌握知识,更能将知识转化为实际能力。同时,目标的具体性和可测量性也符合**SMART原则** (Specific, Measurable, Achievable, Relevant, Time-bound),使您能够清晰地评估自己的学习成果。

</div>

---

## **全貌：数据分析五步法**

<div class="columns">
<div>

我们即将开启的旅程，遵循一套标准的数据分析流程：

1.  📥 **获取数据 (Get)**: 读取Excel/CSV/数据库 (`read_excel`)
2.  🧹 **清洗加工 (Clean)**: 去重、补全、筛选 (`dropna`, `filter`)
3.  📊 **统计分析 (Analyze)**: 计算均值、分组对比 (`groupby`, `mean`)
4.  📈 **可视化 (Visualize)**: 画图表，发现趋势 (**模块五**)
5.  💡 **洞察决策 (Insight)**: 得出结论，指导行动

**模块四重点攻克前三步！**

</div>
<div>

![数据分析流程图：从原始数据到清洗，再到分析和图表，最后得出灯泡图标的洞察 width:550px](../../../lectures/images/2025-11-27-11-40-48.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据分析的标准方法论
本页介绍的"数据分析五步法"是对业界广泛采用的**CRISP-DM (Cross-Industry Standard Process for Data Mining)** 方法论的简化和教学化改编。CRISP-DM是由IBM等公司在1990年代末提出的跨行业数据挖掘标准流程,包含六个阶段:业务理解、数据理解、数据准备、建模、评估和部署。

我们的五步法将其简化为更适合初学者的版本:
1. **获取数据 (Data Acquisition)**: 对应CRISP-DM的"数据理解"阶段,涉及数据源识别、数据加载和初步探索。
2. **清洗加工 (Data Cleaning)**: 对应"数据准备"阶段,包括处理缺失值、异常值检测、数据类型转换等。这一步通常占据数据科学家80%的工作时间。
3. **统计分析 (Statistical Analysis)**: 对应"建模"阶段的基础部分,使用描述性统计和分组分析发现数据中的模式。
4. **可视化 (Visualization)**: 是"评估"阶段的重要工具,通过图表使抽象的数字变得直观可理解。
5. **洞察决策 (Insight & Decision)**: 对应"部署"阶段,将分析结果转化为可操作的业务建议。

这种**流程化思维 (Process-Oriented Thinking)** 是数据科学的核心素养之一,它确保分析工作的系统性和可重复性。

</div>

---

## **示范效果：AI生成的“英雄体检报告”**

<div class="columns">
<div>

### **1. 提出需求**
拿到一份陌生的Excel，我们通常想知道：
*   有多少行数据？
*   有哪些列？
*   数据有没有缺失？

### **2. 指挥 AI**
> "请帮我生成Python代码，读取 `honor_of_kings.xlsx`，并打印数据的基本信息 (info)。"

</div>
<div>

### **3. AI 生成的代码与结果**
```python
import pandas as pd
df = pd.read_excel('honor_of_kings.xlsx')
df.info()
```

**输出结果**:
```text
RangeIndex: 108 entries... (108行)
Data columns (total 4 columns): (4列)
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   英雄       108 non-null    object 
 1   胜率       108 non-null    float64
 ...
```
*一眼看清：108位英雄，数据完整！*

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 探索性数据分析 (Exploratory Data Analysis, EDA)
本页展示的"数据体检"过程是**探索性数据分析 (EDA)** 的第一步。EDA是由著名统计学家约翰·图基 (John Tukey) 在1970年代提出的概念,强调在进行正式的统计建模之前,应该先通过可视化和描述性统计来"认识"数据。

**数据画像 (Data Profiling)** 是EDA的核心技术之一,通常包括:
1. **结构检查**: 行数、列数、列名、数据类型 - 这正是 `df.info()` 提供的信息。
2. **完整性检查**: 缺失值比例、空值分布 - `info()` 中的 "Non-Null Count" 列。
3. **分布检查**: 数值范围、均值、中位数、标准差 - 通过 `df.describe()` 获取。
4. **唯一性检查**: 重复值、唯一值数量 - 通过 `df.nunique()` 获取。

在专业的数据科学项目中,EDA通常占据项目时间的20-30%。正如数据科学家常说的:"**垃圾进,垃圾出 (Garbage In, Garbage Out)**"。只有充分理解数据的质量和特征,才能进行有效的分析和建模。本课通过 `info()` 和 `head()` 方法,帮助您建立这种"先体检,再治疗"的专业习惯。

</div>

---

## **核心概念：认识 Pandas 与 DataFrame**

<div class="columns ratio-6-4">
<div style="font-size:0.9em">

### **Pandas 是什么？**
它是Python的一个**第三方库**，专门用于数据分析。
你可以把它想象成一个**没有图形界面的、超级强大的Excel**。

### **DataFrame (数据框)**
这是Pandas的核心对象。
- **它就是一张表**: 有行(Index)，有列(Columns)。
- **它活在内存里**: 处理速度极快。

</div>
<div class="align-middle">

![一张Excel表格飞入电脑内存，变成一个带有行列号的矩阵结构 width:400px](../../../lectures/images/2025-11-27-11-43-58.png)

</div>
</div>

<div class="insight" style="font-size:0.6em">

💡 **类比**: 
- **Excel文件**: 像是仓库里的**账本**（在硬盘上，翻阅慢）。
- **DataFrame**: 像是铺在桌子上的**账页**（在内存里，随时可写画）。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Pandas的诞生与DataFrame的设计哲学
**Pandas** 由Wes McKinney于2008年在对冲基金AQR Capital Management工作时创建,最初是为了解决金融数据分析中的痛点。2009年开源后,迅速成为Python数据科学生态系统的基石。其名称来源于"Panel Data"(面板数据)和"Python Data Analysis"的组合。

**DataFrame** 的设计灵感来自R语言的同名数据结构,但在Python中进行了优化和扩展。它的核心特性包括:
1. **二维表格结构**: 类似于关系数据库中的表,具有行索引(Index)和列标签(Columns)。
2. **异构数据支持**: 不同列可以存储不同类型的数据(整数、浮点数、字符串、日期等)。
3. **标签化索引**: 支持通过标签而非位置访问数据,提高代码可读性。
4. **内存计算**: 数据完全加载到RAM中,利用NumPy的向量化运算,速度比Excel快数百倍。

**内存计算 vs 磁盘计算**的性能差异是巨大的。当前DDR5 RAM访问速度可达50GB/s,而较好的SSD硬盘的理想读取速度约为7GB/s左右,差距达6倍,实际硬盘随机读取速度要小得多，通常RAM和SSD的读取速度差距在100倍以上。这就是为什么DataFrame能够在毫秒级完成Excel需要数秒甚至数分钟的操作。当然,这也意味着DataFrame受限于内存大小,对于超大数据集(数十GB以上),需要使用Dask、Spark等分布式计算框架。

</div>

---

## **准备工作 (安装与导入)**

<div class="columns">
<div>

### **1. 安装 (Install)**
就像给手机装APP。
在终端运行：
```bash
pip install pandas openpyxl
```
*`openpyxl` 是读取Excel的助手。*

</div>
<div>

### **2. 导入 (Import)**
在使用前，要告诉Python。
在代码开头：
```python
import pandas as pd
```
*`as pd` 是给它起个别名，方便后面偷懒少打字。*

</div>
</div>

<div class="tip" style="font-size:0.6em">

💡 **检查**: 
如果不确定是否安装成功，可以在终端输入 `pip show pandas`。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Python包管理与依赖关系
**pip (Pip Installs Packages)** 是Python的标准包管理器,类似于Linux的apt-get或macOS的Homebrew。它从**PyPI (Python Package Index)** 这个中央仓库下载和安装第三方库。

**依赖关系 (Dependencies)** 是软件工程中的重要概念。Pandas本身依赖于多个底层库:
- **NumPy**: 提供高性能的多维数组和数学运算,是Pandas的计算引擎。
- **python-dateutil**: 处理日期和时间数据。
- **pytz**: 处理时区信息。

**openpyxl** 是一个专门用于读写Excel 2010+ (.xlsx)文件的库。Pandas本身不直接处理Excel文件格式,而是通过"引擎"(engine)的方式委托给专门的库。对于旧版Excel (.xls),则需要xlrd库。

**命名空间约定 (Namespace Convention)**: `import pandas as pd` 中的 `as pd` 是Python社区的约定俗成。这种约定包括:
- `import numpy as np`
- `import matplotlib.pyplot as plt`
- `import seaborn as sns`

遵循这些约定能让您的代码更易于他人理解,也便于在Stack Overflow等社区寻求帮助时,让他人快速理解您的代码。这体现了软件工程中的**可读性原则 (Readability Principle)**: "代码被阅读的次数远多于被编写的次数"。

</div>

---

## **读取数据 (Read)**

<div class="columns">
<div class="styled-div" style="font-size:0.6em">

### **核心函数**
- 读取Excel: `pd.read_excel('文件名.xlsx')`
- 读取CSV: `pd.read_csv('文件名.csv')`

### **指挥AI的指令**
> "请帮我生成Python代码，读取当前目录下的 'honor_of_kings.xlsx' 文件，并保存到变量 df 中。"

</div>
<div>

### **代码示例**
```python
import pandas as pd

# 读取数据
df = pd.read_excel('honor_of_kings.xlsx')

# 打印成功提示
print("数据读取成功！")
```

</div>
</div>

<div class="insight" style="font-size:0.6em">

🔍 **交互实验**:
请打开终端输入 `python` 进入交互模式，逐行输入上面的代码。
当看到 `数据读取成功！` 时，你就成功迈出了第一步！
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 文件I/O与路径解析
**I/O (Input/Output)** 是计算机科学的基础概念,指数据在程序与外部存储设备之间的传输。文件读取是最常见的输入操作之一。

**工作目录 (Working Directory)** 是程序执行时的"当前位置"。当你使用相对路径(如 `'honor_of_kings.xlsx'`)时,Python会在工作目录中查找文件。可以通过以下方式查看和修改工作目录:
```python
import os
print(os.getcwd())  # 查看当前工作目录
os.chdir('/path/to/dir')  # 修改工作目录
```

**相对路径 vs 绝对路径**:
- **相对路径**: `'data/file.xlsx'` 或 `'../file.xlsx'` - 相对于当前工作目录。
- **绝对路径**: `'/Users/username/Documents/file.xlsx'` (macOS/Linux) 或 `'C:\\Users\\username\\file.xlsx'` (Windows) - 从根目录开始的完整路径。

**最佳实践**:
1. **项目结构化**: 将数据文件放在项目的 `data/` 子目录中,代码放在 `src/` 或项目根目录。
2. **使用pathlib**: Python 3.4+推荐使用 `pathlib.Path` 处理路径,它能自动处理不同操作系统的路径分隔符差异。
3. **配置文件**: 对于复杂项目,将文件路径写入配置文件(如 `config.yaml`),避免硬编码。

`pd.read_excel()` 函数还支持许多高级参数,如 `sheet_name`(指定工作表)、`usecols`(选择特定列)、`skiprows`(跳过行)等,这些在处理复杂Excel文件时非常有用。

</div>

---

## **避坑指南：新手最容易遇到的两个报错**

<div class="columns">
<div>

### **1. 找不到文件 (FileNotFoundError)**
*   **现象**: `No such file or directory: 'xxx.xlsx'`
*   **原因**: 代码在A文件夹，文件在B文件夹。
*   **对策**: 把文件拖到代码所在的**同一个文件夹**里。

</div>
<div>

### **2. 中文乱码 (EncodingError)**
*   **现象**: 读CSV时，中文变成 ``。
*   **原因**: 编码格式不对 (GBK vs UTF-8)。
*   **对策**: 对AI说 "请尝试用 **gbk** 编码读取"。

</div>
</div>

<div class="tip" style="font-size:0.6em">

💡 **AI调试法**:
遇到报错不要慌，直接把**报错信息**复制给AI，问它："我遇到了这个报错，该怎么修？"
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 字符编码与异常处理
**字符编码 (Character Encoding)** 是计算机如何将字符映射为字节序列的规则。这是一个历史遗留问题,也是跨文化软件开发的核心挑战之一。

**常见编码格式**:
- **ASCII**: 最早的编码标准,只支持128个字符(主要是英文)。
- **GBK/GB2312**: 中国国家标准,支持简体中文,每个汉字占2字节。
- **UTF-8**: Unicode的一种实现,支持全球所有语言,是现代Web的标准编码。中文字符通常占3字节。
- **UTF-16**: Windows系统内部使用的编码,每个字符至少2字节。

**乱码产生的原因**: 当文件以GBK编码保存,但程序以UTF-8解码时,字节序列被错误解释,导致乱码。这类似于用英文字典去查中文字,自然无法正确理解。

**异常处理 (Exception Handling)** 是编程的重要技能。Python的异常机制提供了结构化的错误处理:
```python
try:
    df = pd.read_csv('file.csv')
except FileNotFoundError:
    print("文件不存在,请检查路径")
except UnicodeDecodeError:
    df = pd.read_csv('file.csv', encoding='gbk')
```

**调试策略**: 本页提倡的"AI调试法"体现了现代软件开发的新范式。传统的调试依赖于阅读文档和搜索Stack Overflow,而AI助手能够快速诊断问题并提供针对性的解决方案,大大降低了学习曲线。

</div>

---

## **检查数据 (Inspect)**

数据读进来了，我们得看一眼它长什么样，是不是我们想要的。

<div class="columns"  style="font-size:0.95em">
<div>

### **1. 看头 (Head)**
`df.head()`
默认显示前5行。就像看书先看目录和前几页。

### **2. 看尾 (Tail)**
`df.tail()`
显示最后5行。

</div>
<div>

### **3. 看信息 (Info)**
`df.info()`
显示数据的“体检报告”：
- 有多少行？
- 每一列是什么类型？(数字/文本)
- 有没有空值？

</div>
</div>

<div class="insight" style="font-size:0.6em">

🔍 **交互实验**:
继续在Python交互模式中输入 `df.head()` 、`df.tail()`和 `df.info()`。
观察输出结果，是不是和PPT上说的一样？
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据类型系统与数据验证
**数据类型 (Data Types)** 是编程语言和数据库系统的基础。Pandas的类型系统建立在NumPy之上,主要包括:
- **int64**: 64位整数,范围约为 -9×10¹⁸ 到 9×10¹⁸
- **float64**: 64位浮点数,用于存储小数
- **object**: Python对象,通常用于字符串,但也可以是任意Python对象
- **bool**: 布尔值 (True/False)
- **datetime64**: 日期时间类型
- **category**: 分类类型,用于存储有限集合的值,节省内存

**dtype推断 (Type Inference)**: Pandas在读取数据时会自动推断每列的数据类型。例如,如果一列全是数字,会被推断为int64或float64;如果包含文本,则为object。这个过程类似于TypeScript（另一种常用于Web应用开发的语言）的类型推断。

**数据验证的重要性**: `df.info()` 提供的信息对于数据质量检查至关重要:
1. **Non-Null Count**: 如果某列的非空值数量少于总行数,说明存在缺失值,需要决定是删除、填充还是保留。
2. **Dtype**: 类型错误会导致后续计算失败。例如,数字被误识别为字符串时,无法进行数学运算。
3. **Memory Usage**: 大数据集需要关注内存占用,必要时进行类型优化(如将int64降级为int32)。

**head() 和 tail() 的设计哲学**: 这两个方法体现了"采样检查"的思想。在大数据场景下,查看全部数据既不现实也无必要。通过查看头尾,您可以快速发现数据排序、格式等问题,这是数据科学家的基本功。

</div>

---

## **扩展知识：CSV文件**

除了Excel，我们还经常遇到 **CSV** 格式。
它本质是纯文本，通常用逗号分隔 (有时也用Tab或空格)。

<div class="columns">
<div>

### **Excel vs CSV**
- **Excel**: 格式丰富，体积大，需要专用软件。
- **CSV**: 纯文本，体积小，通用性强。

</div>
<div>

### **读取方法**
```python
# 读取Excel
df = pd.read_excel('data.xlsx')

# 读取CSV
df = pd.read_csv('data.csv')
```
*AI会自动帮你选择正确的函数。*

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### CSV格式与数据互操作性
**CSV (Comma-Separated Values)** 是一种简单的数据交换格式,由RFC 4180标准定义。其历史可以追溯到1970年代的大型机时代,至今仍是最广泛使用的数据格式之一。

**CSV的优势**:
1. **人类可读**: 纯文本格式,可以用任何文本编辑器打开查看。
2. **平台无关**: 不依赖特定软件,Windows、macOS、Linux都能处理。
3. **体积小**: 没有格式信息和元数据,文件体积通常是Excel的1/10。
4. **版本控制友好**: 文本格式可以被Git等版本控制系统有效追踪差异。

**CSV的局限性**:
1. **无类型信息**: 所有数据都是文本,需要程序自行推断类型。
2. **无格式**: 不支持字体、颜色、公式等Excel特性。
3. **单表格**: 一个CSV文件只能包含一个表格,而Excel可以有多个工作表。
4. **分隔符歧义**: 不同地区可能使用不同分隔符(逗号、分号、制表符),导致兼容性问题。

**开放数据运动 (Open Data Movement)**: 许多政府和科研机构选择CSV作为开放数据的标准格式,因为它符合"数据应该是机器可读且格式开放"的原则。例如,世界银行、联合国、各国统计局发布的数据集大多采用CSV格式。这也是为什么数据科学家必须熟练掌握CSV处理的原因。

</div>

---

## **动手练习：唤醒与体检**

<div class="columns ratio-4-6">
<div>

**任务**：
1.  **读取**: 读取 `honor_of_kings.xlsx`。
2.  **检查**: 查看前5行 (`head`) 和基本信息 (`info`)。
3.  **思考**:
    - 共有多少位英雄？
    - 胜率是数字还是文本？

</div>
<div>

**请向AI发送以下指令**：

> 我在当前目录下有一个 `honor_of_kings.xlsx` 文件。
> 请帮我写一段Python代码：
> 1. 读取这个Excel文件到变量 df。
> 2. 打印前5行数据。
> 3. 打印数据的基本信息 (info)。

**预期输出**:
```text
   英雄       职业    胜率 ...
0  鲁班七号   射手    0.512 ...
RangeIndex: 108 entries...
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 主动学习与认知负荷管理
本页的练习设计体现了**主动学习 (Active Learning)** 的教育理念。研究表明,学习者通过"做"来学习的效果远超过被动听讲。这个练习让您亲手完成完整的数据读取和检查流程,将知识转化为技能。

**认知负荷理论 (Cognitive Load Theory)** 由John Sweller提出,认为学习效果受工作记忆容量限制。本练习的设计遵循了降低认知负荷的原则:
1. **任务分解**: 将复杂任务分解为三个清晰的子任务(读取、查看、思考)。
2. **提供模板**: 给出具体的AI指令模板,降低"如何提问"的认知负荷。
3. **预期输出**: 展示期望结果,帮助您自我验证。

**脚手架教学 (Scaffolding)**: 本练习提供了详细的指导(AI指令模板),这是一种"脚手架"。随着您能力提升,后续课程会逐步减少这种支持,最终让您能够独立完成任务。这符合维果茨基的**最近发展区 (Zone of Proximal Development)** 理论。

**反思性问题**: "共有多少位英雄?胜率是数字还是文本?"这些问题不仅检验操作是否成功,更重要的是引导您**观察和思考**输出结果,培养数据敏感性。这是从"会操作"到"会分析"的关键一步。

</div>

---

## **课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **Pandas** 是Python的数据分析神器。
2.  **DataFrame** 是内存里的超级表格。
3.  **读取**: `read_excel` / `read_csv`。
4.  **检查**: `head()` 看前几行，`info()` 看体检报告。

</div>
<div>

### **下节课预告**
现在我们已经把100多位英雄装进了电脑。
但是，我只想要**胜率大于52%**的**法师**，怎么办？

下节课：**数据筛选**。
我们将学习如何做数据的“淘金者”，精准找到你想要的那个“强势英雄”！

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 知识巩固与学习动机维持
**课程总结**是教学设计中的关键环节,它不仅仅是简单的内容回顾,更是**知识巩固 (Knowledge Consolidation)** 的重要手段。根据**间隔效应 (Spacing Effect)** 理论,在学习后立即复习能显著提高长期记忆效果。

本页总结采用了**要点提炼 (Key Points Extraction)** 的方法,将本课的核心内容浓缩为四个要点:
1. **概念层**: Pandas和DataFrame的定位
2. **操作层**: 读取和检查的具体方法

这种结构化总结帮助您建立**知识框架 (Knowledge Framework)**,便于后续学习时将新知识挂载到已有框架上。

**预告设计的心理学**:
下节课预告采用了**问题驱动 (Problem-Driven)** 的设计:"我只想要胜率大于52%的法师,怎么办?"这个具体问题:
1. **制造认知缺口**: 您会意识到当前技能还不足以解决这个问题,从而产生学习需求。
2. **维持学习动机**: 通过"淘金者"这样的隐喻,让下节课的内容显得有趣和有价值。
3. **建立连贯性**: 明确告知下节课与本节课的逻辑关系,帮助您理解课程的整体架构。

这种**悬念式预告 (Cliffhanger Preview)** 借鉴了影视剧的叙事技巧,能有效提高您对后续课程的期待和参与度,是维持长期学习动机的有效策略。

</div>