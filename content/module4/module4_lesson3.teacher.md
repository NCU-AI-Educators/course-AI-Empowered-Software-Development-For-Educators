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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 导入 (Introduction)
引入GIGO原则，结合电影数据场景，强调数据清洗的重要性。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 问题 (Problem)
通过“脏数据”的具象化场景，展示不清洗数据的后果。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 目标 (Objective)
明确学习成果。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 示范 (Demo)
直观展示清洗对结果的巨大影响。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
讲解去重操作。增加 `duplicated().sum()` 的扩展知识。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
讲解缺失值处理的决策逻辑：Drop vs Fill。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 知识讲解 (Concept)
介绍 `describe()` 函数，重点解读统计指标的含义。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 进阶 (Advanced)
引入相关性分析，提升分析深度。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 6分钟
### 环节: 知识讲解 (Concept)
介绍 `groupby()` 和 `agg()` 函数。重点讲解“样本量”对统计结果可信度的影响。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 12分钟
### 环节: 练习 (Practice)
综合练习：清洗、统计、相关性、分组。包含巡堂指导和结果点评。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 总结 (Summary)
总结本课，预告下节课的Capstone Project。预留答疑时间。

</div>