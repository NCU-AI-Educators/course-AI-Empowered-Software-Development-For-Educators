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
![bg blur:2px brightness:60%](../../../lectures/images/2025-11-27-12-35-23.png)

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
## 第16节课: 综合项目——电影市场洞察报告

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 导入 (Introduction)
明确本节课为综合项目课，设定角色和任务。

</div>

---

## **项目背景：寻找“财富密码”**

<div class="columns ratio-6-4" style="font-size:0.9em">
<div>

你手里有一份 `movies.xlsx`，包含 **电影名**、**类型**、**成本(Cost)**、**票房(Revenue)** 和 **评分(Rating)**。

**你的任务**：
1.  **计算回报率**: 投资回报率 (ROI) = (票房 - 成本) / 成本。
2.  **类型分析**: 哪个类型的平均回报率最高？
3.  **口碑验证**: 评分 > 8.0 的电影，票房真的高吗？
4.  **导出名单**: 筛选出“高分高票房”的必看清单。

**数据现状**:
- 包含 **500+部** 电影数据。
- 包含 **缺失值** (部分电影未公开成本)。

</div>
<div>

![电影海报墙 vs 复杂的K线图和数据报表 width:500px](../../../lectures/images/2025-11-27-12-40-50.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 问题 (Problem)
设定具体的业务问题，驱动后续的分析步骤。

</div>

---

## **项目路线图**

<div class="columns">
<div>

我们将分四步完成这个项目：

1.  **Step 1: 读取与体检** (复习 Lesson 13)
    - 读取数据，检查缺失情况。
2.  **Step 2: 数据清洗与计算** (复习 Lesson 15)
    - 处理缺失成本，计算 ROI。
3.  **Step 3: 统计分析** (复习 Lesson 15)
    - 按类型统计平均 ROI。
4.  **Step 4: 导出报告** (复习 Lesson 14)
    - 筛选“双高”电影，保存为Excel。

</div>
<div>

![配图占位符](../../../lectures/images/2025-11-27-12-42-47.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 路线图 (Roadmap)
清晰展示项目流程。

</div>

---

## **Step 1: 读取与体检**

<div class="columns ratio-4-6">
<div>

**任务**：
1.  读取 `movies.xlsx`。
2.  查看前5行。
3.  查看数据基本信息 (`info`)。

**思考**：
- `成本` (Cost) 有没有缺失值？

</div>
<div>

**AI指令**：

> 请帮我生成Python代码，读取 'movies.xlsx' 文件。
> 然后打印前5行，并打印数据的基本信息 (info)。

**AI 生成的核心代码**
```python
df = pd.read_excel('movies.xlsx')
print(df.info())
```

**预期输出**:
```text
RangeIndex: 603 entries...
成本: 517 non-null... (有86部缺失!)
```

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 实施 (Step 1)
执行读取和检查。

</div>

---

## **Step 2: 数据清洗与计算**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

**任务**：
1.  **处理缺失**: 删除 `成本` 缺失的行 (无法计算ROI)。
2.  **计算ROI**: 创建新列 `ROI`。
    `ROI = (票房 - 成本) / 成本`
3.  打印前5行检查。

</div>
<div>

**AI指令**：

> 请帮我生成Python代码，接上面的代码。
> 1. 请删除 `成本` 列为空的行。
> 2. 请创建一个新列 `ROI`，计算公式为：(`票房` - `成本`) / `成本`。
> 3. 打印前5行。

**AI 生成的核心代码**
```python
df = df.dropna(subset=['成本'])
df['ROI'] = (df['票房'] - df['成本']) / df['成本']
```

**预期输出**:
```text
   ... 成本   票房  ROI
0  ... 237    760.5    2.21
```

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 实施 (Step 2)
执行清洗和计算。

</div>

---

## **Step 3: 统计分析 (类型对比)**

<div class="columns ratio-4-6"  style="font-size:0.8em">
<div>

**任务**：
1.  按 `类型` (Genre) 分组。
2.  统计 `ROI` 的平均值。
3.  找出回报率最高的类型。

</div>
<div>

**AI指令**：

> 请帮我生成Python代码，接上面的代码。
> 请帮我按 `类型` 分组，计算 `ROI` 的平均值。
> 并按平均值降序排列，打印结果。

**AI 生成的核心代码**
```python
# 按类型分组，算均值，再排序
result = df.groupby('类型')['ROI'].mean().sort_values(ascending=False)
print(result)
```

**预期输出**:
```text
类型
恐怖       15.3  (恐怖片回报率最高)
音乐       6.4
...
```

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 8分钟
### 环节: 实施 (Step 3)
执行分组统计分析。

</div>

---

## **Step 4: 导出必看清单**

<div class="columns ratio-4-6">
<div>

**任务**：
1.  筛选出 **评分 > 8.0** 且 **ROI > 2** 的电影。
2.  将结果保存为 `must_watch.xlsx`。

</div>
<div>

**AI指令**：

> 请帮我生成Python代码，筛选出 `评分` 大于 8.0 且 `ROI` 大于 2 的电影。
> 将这些电影的数据保存为 `must_watch.xlsx`。
> 记得不要保存索引。

**AI 生成的核心代码**
```python
# 多条件筛选 + 导出
must_watch = df[(df['评分'] > 8.0) & (df['ROI'] > 2)]
must_watch.to_excel('must_watch.xlsx', index=False)
```

**验证**:
打开Excel，看看有哪些神作上榜了？

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 实施 (Step 4)
执行导出。

</div>

---

## **避坑指南与答疑**

<div class="columns">
<div>

### **常见报错**
1.  **KeyError**: 列名拼错了（比如把 `成本` 写成 `Cost`）。
2.  **ZeroDivisionError**: 如果有成本为0的电影，计算ROI会报错。
3.  **PermissionDenied**: Excel文件正打开着。

</div>
<div>

### **Q & A**
- **Q**: 能不能分析导演？
- **A**: 当然！把 `groupby('Genre')` 改成 `groupby('Director')` 就行。
- **Q**: 怎么画出票房走势图？
- **A**: 下个模块（数据可视化）我们专门讲！

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 总结 (Summary)
总结常见问题。

</div>

---

## **模块四结业：从“小白”到“分析师”**

<div class="columns align-middle">
<div>

### **你的成就**
- ✅ **工具**: 熟练使用 Pandas。
- ✅ **流程**: 掌握了 读取 -> 清洗 -> 计算 -> 统计 -> 导出 的全流程。
- ✅ **思维**: 建立了“数据驱动”的分析思维。

### **下一步：模块五**
**数据可视化**
让数据讲故事，让图表会说话。

</div>
<div>

![一张精美的数据可视化图表（柱状图+折线图） width:450px](../../../lectures/images/2025-11-27-15-28-45.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 结业 (Conclusion)
庆祝结业，展望未来。

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
}

p {
  font-size: 24px;
  color: #555;
  line-height: 1.5;
}
</style>

<p>

*小提示：你已经是合格的“AI数据分析师”了！<br>尝试运用“读取-清洗-分析-导出”的标准流程，指挥你的AI助手挖掘原始数据背后的秘密。*
</p>

<br><br>

<div class="tip" style="bottom: 40px; left: 80px; right: 80px; text-align: left; font-size: 0.6em;">

💡 **挑战任务 (Challenge)**:
我们还提供了一份**原始的、未裁剪的**数据集 `movie_metadata.csv` (5000+部电影)。
请尝试用它重复上述分析流程：
1. 用 `pd.read_csv()` 读取。
2. 列名会不一样：成本是 `budget`，票房是 `gross`，类型是 `genres`。
3. 记得先清洗数据！
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 拓展 (Extension)
利用完整数据集提供分层教学，满足学有余力的学员需求。

</div>

---

## **课后练习：探索原始电影数据集 (基础)**

我们为你准备了一份包含 **5000+部** 电影的完整数据集 `movie_metadata.csv` (原始数据)。
请尝试完成以下挑战，看看你能发现什么？

#### **挑战一：谁是票房之王？**
> *“请帮我生成Python代码，统计哪位 **导演 (director_name)** 的总票房 (**gross**) 最高？请按导演分组，对票房求和，并找出第一名。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：这需要用到 `groupby` 操作。注意原始数据的列名是小写的 `director_name` 和 `gross`。记得先清洗数据 (`dropna`) 哦！

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 难度: 基础
### 知识点: groupby, sum, sort_values
### 目标: 巩固分组统计的基本操作。

</div>

---

## **课后练习：探索原始电影数据集 (进阶)**

#### **挑战二：电影越来越长了吗？**
> *“请帮我生成Python代码，统计不同 **年份 (title_year)** 的 **平均时长 (duration)**，看看有什么趋势？可以按年份排序，对比一下早期和近期的电影。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：`duration` (时长) 是原始数据独有的字段。你需要按 `title_year` 分组，计算 `duration` 的均值。画个图可能更直观（虽然我们还没学画图，但可以试着让AI画一下）？

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 难度: 进阶
### 知识点: groupby, mean, 趋势分析
### 目标: 引导学员思考数据背后的趋势，预热可视化概念。

</div>

---

## **课后练习：探索原始电影数据集 (挑战)**

#### **挑战三：寻找“遗珠”**
> *“请帮我生成Python代码，筛选出 **成本 (budget) < 1000万** 但 **评分 (imdb_score) > 8.5** 的电影。这些通常是典型的小成本佳作。”*

<div class="insight" style="font-size: 0.6em; margin-top: 20px;">

**思考**：这是一个多条件筛选问题。注意原始数据的成本单位是“元”，不是百万。你需要组合两个条件：`budget < 10000000` 和 `imdb_score > 8.5`。

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 难度: 挑战
### 知识点: 多条件筛选, 逻辑运算符
### 目标: 综合运用筛选技能，发现数据中的"遗珠"。

</div>