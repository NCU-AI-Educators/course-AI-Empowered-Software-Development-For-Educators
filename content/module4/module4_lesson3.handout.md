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
![bg blur:3px brightness:60%](../../../lectures/images/2025-11-27-12-15-09.png)

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
## 第15节课: 数据清洗与统计——做一名严谨的“影评人”

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### GIGO原则与数据质量管理
**GIGO (Garbage In, Garbage Out)** 是计算机科学和数据分析领域的基本原则,最早由IBM工程师George Fuechsel在1960年代提出。这个原则强调:**输出质量完全取决于输入质量**。

**数据质量的维度**: 在数据管理领域,数据质量通常从以下维度评估:
- **完整性 (Completeness)**: 数据是否有缺失值
- **准确性 (Accuracy)**: 数据是否反映真实情况
- **一致性 (Consistency)**: 同一数据在不同地方是否一致
- **唯一性 (Uniqueness)**: 是否存在重复记录
- **及时性 (Timeliness)**: 数据是否是最新的

**数据清洗的现实意义**: 研究表明,数据科学家将80%的时间花在数据准备和清洗上。这不是效率低下,而是必要投资。正如建筑需要坚实的地基,数据分析需要高质量的数据。

本节课通过电影数据这个贴近生活的场景,帮助您掌握数据清洗的核心技能,这些技能可以直接应用到您的教学和科研数据处理中。

</div>

---

## **问题导入：棘手的电影数据**

<div class="columns ratio-6-4">
<div style="font-size:0.95em">

为了研究电影市场，你下载了一份 `movies.xlsx`。打开一看，数据**充满瑕疵**：

1.  **重复收录**: 《阿凡达》出现了两次（可能是重映版）。
2.  **数据缺失**: 很多老电影没有 **票房 (Revenue)** 数据。
3.  **数据异常**: 评分应该是0-10分，有的电影竟然是空值。

**思考**:
如果不清洗直接算“平均票房”，结果会准吗？
（重复的《阿凡达》会让总票房虚高，缺失的数据会报错...）

</div>
<div>

![一张乱七八糟的Excel表，有空行，有重复行，有红色标记的异常值 width:450px](../../../lectures/images/2025-11-27-12-29-00.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 脏数据的类型与危害
本页展示了三种最常见的**数据质量问题 (Data Quality Issues)**，它们是数据分析中的“隐形杀手”：

1.  **重复数据 (Duplicate Data)**：
    - **成因**：系统错误、多次导入、版本混淆。
    - **危害**：导致统计结果虚高（如票房翻倍），误导决策。

2.  **缺失数据 (Missing Data)**：
    - **成因**：信息未收集、传感器故障、用户拒绝填写。
    - **危害**：导致计算错误（NaN传播），或样本偏差（Sample Bias）。

3.  **异常数据 (Outliers/Anomalies)**：
    - **成因**：输入错误（如年龄200岁）、单位混淆、欺诈行为。
    - **危害**：严重拉偏均值（Mean），影响模型准确性。

**数据完整性 (Data Integrity)**：在数据库理论中，这些问题破坏了数据的完整性。如果不先解决它们，后续的所有分析都建立在沙堆之上。这正是为什么我们需要在分析前进行严格的“数据体检”。

</div>

---

## **本课学习目标**

<div class="columns">
<div>

学完这节课，你将能够：

1.  **掌握** 使用 `drop_duplicates()` 去除重复电影。
2.  **掌握** 使用 `dropna()` 或 `fillna()` 处理票房/评分缺失。
3.  **掌握** 使用 `describe()` 快速查看电影评分分布。
4.  **掌握** 使用 `groupby()` 按“类型”统计平均票房。

</div>
<div class="align-top-left">

![配图占位符](../../../lectures/images/2025-11-27-12-20-28.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 技能构建：从清洗到洞察
本课的学习目标设计遵循了数据分析的自然工作流，涵盖了两个关键阶段：

1.  **数据清洗阶段 (Data Cleaning)**：
    - 目标1 & 2 (`drop_duplicates`, `dropna`) 关注的是**数据质量**。这是“防御性”的技能，旨在消除错误。

2.  **探索性分析阶段 (EDA)**：
    - 目标3 & 4 (`describe`, `groupby`) 关注的是**数据洞察**。这是“进攻性”的技能，旨在发现规律。

**工具的选用**：
    - `describe()` 是**单变量分析 (Univariate Analysis)** 的利器，用于了解单个维度的分布。
    - `groupby()` 是**多变量分析 (Multivariate Analysis)** 的基础，用于研究变量间的关系（如：类型 vs 票房）。

掌握这套组合拳，您就具备了处理大多数基础数据分析任务的能力。

</div>

---

## **示范效果：清洗前 vs 清洗后**

<div class="columns">
<div>

**清洗前 (Dirty)**
| 电影 | 类型 | 票房(百万美元) |
| :--- | :--- | :--- |
| 阿凡达 | 科幻 | 760.5 |
| 阿凡达 | 科幻 | 760.5 |
| 罗马假日 | 爱情 | (空) |

*平均票房: 7.6亿 (虚高)*
*(注：Pandas计算均值时会自动忽略空值，即除以2而不是3)*

</div>
<div>

**清洗后 (Clean)**
| 电影 | 类型 | 票房(百万美元) |
| :--- | :--- | :--- |
| 阿凡达 | 科幻 | 760.5 |
| 罗马假日 | 爱情 | 0 |

*平均票房: 3.8亿 (可计算)*
*(注：填0是权宜之计，虽能计算但会拉低均值)*

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 统计偏差 (Statistical Bias)
本页通过一个微型案例，直观展示了**统计偏差**是如何产生的。

- **虚高 (Overestimation)**：重复数据导致总和与均值偏高。在商业分析中，这可能导致对市场规模的误判。
- **偏差 (Skewness)**：缺失值的处理方式也会引入偏差。
  - 如果直接忽略缺失值（Pandas默认行为），可能导致样本代表性不足。
  - 如果填充 0，虽然保留了样本，但会拉低均值。

**权衡的艺术 (Trade-off)**：数据清洗往往没有绝对的“正确答案”，而是一种权衡。
- 填 0 适合“确实没有收入”的场景。
- 如果是“数据丢失但实际有收入”，填 0 就会引入错误。此时用**均值填充 (Mean Imputation)** 或**中位数填充 (Median Imputation)** 可能更合理。

作为数据分析师，您需要根据业务背景选择最合适的处理策略，并清楚地知道每种策略可能带来的偏差。

</div>

---

## **Step 1: 去除重复 (Remove Duplicates)**

<div class="columns">
<div>

### **现象**
《阿凡达》出现了两次。这会让我们统计的“总票房”虚高。

### **指令**
> "请帮我生成Python代码，删除重复的电影。"

### **代码**
```python
# drop_duplicates() 一键去重
# keep='first': 保留第一次出现的，删除后面重复的
df = df.drop_duplicates()
```

</div>
<div>

<div class="tip" style="font-size:0.6em">

**检查重复**:
在去重前，你可以先问AI：“帮我检查一下有多少重复行？”
`df.duplicated().sum()`
</div>

<br>

<div class="insight" style="font-size:0.6em">

💡 **原理**:
Pandas 会检查每一行数据。如果发现两行完全一样，就会把多余的删掉，只留下一行。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 重复数据的成因与处理
**重复数据 (Duplicate Data)** 是最常见的数据质量问题之一。
- **成因**: 通常源于数据采集过程中的错误（如爬虫重复抓取）、系统合并时的冲突，或者人为的重复录入。
- **处理**: `drop_duplicates()` 是最标准的处理方式。默认情况下，它会保留第一个出现的记录 (`keep='first'`)。
- **验证**: 专业的做法是先 check (`df.duplicated().sum()`)，再 drop，最后再 check，形成闭环。

</div>

---

## **Step 2: 处理缺失 (Handle Missing Values)**

<div class="columns">
<div style="font-size:0.8em;">

### **现象**
有的电影没有评分，有的没有票房。

### **决策矩阵**
| 情况 | 策略 | 代码 |
| :--- | :--- | :--- |
| **关键信息缺失**<br>(如: 评分) | **删除** (Drop) | `df.dropna(subset=['评分'])` |
| **非关键/可填**<br>(如: 票房) | **填充** (Fill) | `df.fillna({'票房': 0})` |

</div>
<div>

### **代码示例**
```python
# 策略1: 没评分的电影，直接删掉
df = df.dropna(subset=['评分'])

# 策略2: 没票房的电影，填个0
df = df.fillna({'票房': 0})
```

<div class="insight" style="font-size:0.6em">

🔍 **交互实验**:
尝试输入 `df.info()` 查看非空值数量，运行上述代码后，再次 `df.info()`，观察变化。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 缺失值处理策略：删除 vs 填充
在处理缺失值 (Missing Values) 时，我们面临一个经典的决策：**删除 (Deletion)** 还是 **填充 (Imputation)**？

1.  **删除法 (`dropna`)**：
    - **适用场景**：缺失比例很小（如 <5%），或者缺失的是关键标签。
    - **优点**：简单，不引入人为假设。
    - **缺点**：减少了样本量。

2.  **填充法 (`fillna`)**：
    - **适用场景**：缺失比例较大，或者数据量本身很少。
    - **策略**：
        - **常数填充**：填 0 或 "Unknown"。
        - **统计量填充**：填均值、中位数。

**Pandas的设计**：`subset` 参数允许精细化控制，体现了数据处理的严谨性。

</div>

---

## **描述性统计 (Describe)**

清洗干净后，我们想快速了解电影市场的全貌。

<div class="columns">
<div>

### **指令**
> "请帮我生成Python代码，对数据进行描述性统计分析。"

### **AI生成的代码**
```python
# describe() 自动计算所有数字列的统计量
print(df.describe())
```

</div>
<div>

### **输出解读**
- **count**: 有多少部电影？
- **mean**: 平均分是多少？
- **max**: 最高分是多少？
- **50%**: 中位数是多少？

</div>
</div>

<div class="insight" style="font-size:0.6em">

🔍 **交互实验**:
尝试输入 `df.describe()`。
看看平均分(mean)是多少？
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 描述性统计与五数概括
`describe()` 函数是快速了解数据分布的神器，它默认提供了一组被称为**五数概括 (Five-Number Summary)** 的统计量（加上计数、均值和标准差）：

1.  **中心趋势 (Central Tendency)**：
    - **Mean (均值)**：数据的平均水平，但容易受极端值（如一部票房极高的电影）影响。
    - **50% (中位数)**：将数据从小到大排列，位于中间的数。中位数比均值更稳健（Robust）。

2.  **离散程度 (Dispersion)**：
    - **Std (标准差)**：数据分布的“胖瘦”。标准差越大，说明电影评分参差不齐；标准差越小，说明大家评分都很接近。
    - **Min/Max**：数据的范围。

**数据分析的直觉**：通过比较 Mean 和 50% (Median)，您可以快速判断数据分布的形态。
- 如果 Mean > Median，说明数据是**右偏 (Right-skewed)** 的（例如收入数据，少数富人拉高了平均值）。
- 如果 Mean ≈ Median，说明数据近似**正态分布 (Normal Distribution)**。

</div>

---

## **进阶统计：相关性分析 (Correlation)**

除了看单个指标，我们还想知道：**票房高的电影，评分也高吗？**

<div class="columns">
<div>

### **指令**
> "请帮我生成Python代码，计算 **票房** 和 **评分** 的相关系数。"

### **代码**
```python
# corr(): 计算相关系数
# 范围: -1 到 1
relation = df[['票房', '评分']].corr()
print(relation)
```

</div>
<div>

### **结果解读**
| 系数 (r) | 含义 | 例子 |
| :--- | :--- | :--- |
| **0.8 ~ 1.0** | **强相关** | 身高 vs 鞋码 |
| **0.3 ~ 0.5** | **弱相关** | 评分 vs 票房 |
| **0** | **不相关** | 身份证号 vs 智商 |
| **-1** | **负相关** | 运动量 vs 体重 |

<div class="insight" style="font-size:0.6em">

💡 <b>商业洞察</b>:
如果算出 r=0.3，说明“叫好”不一定“叫座”。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 皮尔逊相关系数 (Pearson Correlation Coefficient)
`df.corr()` 默认计算的是皮尔逊相关系数，用于衡量两个变量之间的**线性相关程度**。

**误区警示**:
**相关性不等于因果性 (Correlation does not imply Causation)**。
即使发现“冰淇淋销量”和“溺水人数”强相关（r=0.8），也不能说吃冰淇淋导致溺水。实际上，它们都受第三个变量“夏天的高温”影响。

在电影分析中，高票房和高评分可能都受“名导/名演”这个因素影响，但它们之间不一定有直接因果。

</div>

---

## **分组统计 (Group By)**

如果我们想对比不同类型的电影呢？这就需要用到 **分组**。

<div class="columns ratio-4-6" style="font-size:0.9em">
<div>

### **场景**
我想知道“科幻片”和“爱情片”谁的平均分更高？**而且要看样本量够不够。**

### **指令**
> "请帮我生成Python代码，按 **'类型'** 分组，计算 **'评分'** 的平均值和数量。"

</div>
<div>

### **代码逻辑**
```python
# agg(['mean', 'count']): 同时算均值和数量
result = df.groupby('类型')['评分'].agg(['mean', 'count'])
print(result)
```

**输出**:
```text
      mean  count
类型             
爱情    6.4     12
科幻    6.3    150
```

</div>
</div>

<div class="insight" style="font-size:0.6em">

💡 <b>统计陷阱</b>:
如果“爱情片”平均分8.0，但count只有1部；而“科幻片”平均分7.5，有100部。
你觉得谁更可靠？显然是科幻片。<b>忽略样本量单纯比较平均值，往往会得出误导性的结论。</b>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Split-Apply-Combine 分析范式
`groupby()` 操作背后蕴含着数据分析中最著名的范式之一：**Split-Apply-Combine (拆分-应用-合并)**。

1.  **Split (拆分)**：根据“类型”将大数据集拆分为多个小数据集。
2.  **Apply (应用)**：在每个小数据集上独立应用函数。这里我们用了 `agg(['mean', 'count'])`，这是**多重聚合**。
3.  **Combine (合并)**：将计算结果重新组合成一个新的 DataFrame。

**统计显著性的直觉**：
在教学中引入 `count` 是为了培养**统计直觉**。在小样本上计算出的均值波动极大（方差大），不可信。这是数据分析师必须具备的批判性思维。

</div>

---

## **动手练习：清洗与透视**

<div class="columns ratio-4-6">
<div>

**任务**：
1.  **准备**: 创建包含重复和缺失值的 `movies.xlsx`。
2.  **清洗**: 删除重复行，删除无评分行。
3.  **统计**: 查看评分的描述性统计 (`describe`)。
4.  **进阶**: 计算票房与评分的相关性 (`corr`)。
5.  **透视**: 按 `类型` 统计平均评分和数量 (`groupby`)。

</div>
<div>

**请向AI发送以下指令**：

> 请帮我生成Python代码，完成以下任务：
> 1. 读取 `movies.xlsx`，删除重复行和无评分的行。
> 2. 打印评分的描述性统计信息。
> 3. 计算并打印票房和评分的相关系数。
> 4. 按 `类型` 分组，计算平均评分和电影数量。

**预期结果**:
你将看到数据的“体检报告”、相关系数（是不是0.3左右？）和不同类型的评分对比。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 综合练习的设计意图
本练习是本节课的**高潮 (Climax)**，旨在通过一个完整的微型项目，帮助您整合碎片化的技能。

**脚手架 (Scaffolding) 的撤除**：
- 在之前的练习中，我们可能只关注某一个指令。
- 在这个练习中，您需要独立完成从“读取”到“清洗”再到“分析”的全过程。
- 这种设计模拟了真实的工作环境，培养您的**流程化思维 (Process Thinking)**。

**自我验证 (Self-Verification)**：
- 练习要求您先查看 `describe`，再查看 `corr`，最后 `groupby`。
- `corr` 提供了变量间的关系视角。
- `groupby` 提供了分类视角。
- 如果局部均值远高于全局均值，且样本量足够大，您就发现了一个显著的特征（Insight）。

通过这个练习，您不仅学会了写代码，更学会了如何像分析师一样**用数据讲故事**。

</div>

---

## **课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **清洗**: `drop_duplicates` (去重), `dropna` (去空)。
2.  **全貌**: `describe` (统计概况)。
3.  **透视**: `groupby` (分组统计)。
4.  **原则**: **Garbage In, Garbage Out** (先清洗，后统计)。

</div>
<div>

### **下节课预告**
我们已经掌握了单项技能。
下节课，我们将迎来 **模块四的终极挑战**：

**项目：电影市场洞察报告**
我们将综合运用所有技能，处理一份包含数百部电影的真实数据，分析票房与口碑的关系，寻找电影市场的“财富密码”。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 课程回顾与项目预告
本节课我们完成了从“数据获取”到“数据清洗”再到“基础统计”的跨越。

**知识图谱的构建**：
- **清洗** (`drop_duplicates`, `dropna`) 是地基，保证数据质量。
- **统计** (`describe`, `groupby`) 是支柱，支撑数据洞察。

**PBL (Project-Based Learning) 预告**：
下节课我们将进入模块四的**Capstone Project (顶点项目)**。
- 我们将不再处理玩具数据，而是面对一份真实的、复杂的电影市场数据。
- 您将需要综合运用 Lesson 1-3 学到的所有技能（读取、检查、清洗、筛选、排序、统计）。
- 这种**综合性项目**是检验学习成果的最佳方式，也是您建立自信的关键时刻。

请保持期待，下节课我们将一起挖掘电影市场的“财富密码”！

</div>