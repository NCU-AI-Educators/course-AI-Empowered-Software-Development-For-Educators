---
marp: true
theme: A4
paginate: true
--- 
<style>
/* --- 布局辅助样式 --- */
.rows {
  display: grid;
  grid-template-rows: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
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
![bg blur:3px brightness:60%](../../../lectures/images/2025-12-06-02-47-49.png)

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
## 第17节课: 可视化入门——让数据“被看见”

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么需要可视化？(The "Why" of Visualization)
**双重编码理论 (Dual Coding Theory)**: 心理学家 Allan Paivio 提出，人脑有两套独立的认知系统：一套处理语言（Verbal），一套处理图像（Visual）。同时调动这两套系统，能显著提升记忆和理解效果。

**图片优势效应 (Picture Superiority Effect)**: 研究表明，人类大脑处理视觉信息的速度比处理文本快 60,000 倍。
1.  **发现模式 (Pattern Recognition)**: 帮助**您**快速从海量数据中识别趋势、异常和相关性。
2.  **讲述故事 (Storytelling)**: 用直观的图形更有力地传达**您**的观点。
3.  **辅助决策 (Decision Support)**: 将复杂信息简化，降低决策时的**认知负荷 (Cognitive Load)**。

本节课我们将使用 Python 中最基础的绘图库 **Matplotlib**。它是 Python 可视化的基石，虽然代码略显繁琐，但理解它有助于您掌握绘图的底层逻辑。

</div>

---

## **问题导入：海量数据的认知挑战**

<div class="columns ratio-6-4">
<div>

**场景**：制定全家暑期出游计划。
面对网上铺天盖地的营销软文，我们决定**回归数据**，从 **30,000+** 条真实景点数据中寻找答案。

**痛点**：
面对如此海量的数据，试图通过**人眼**在密密麻麻的表格中寻找规律（比如：哪个城市5A景区最多？），几乎是一个**不可能完成的任务**。

*   ❌ **效率极低**：需要逐行阅读，耗时费力。
*   ❌ **难以比较**：无法直观感知数据之间的数量差异。

</div>
<div class="align-middle-center">

![左边是密密麻麻的Excel表格，右边是一张清晰的柱状图显示Top10城市 width:400px](../../../lectures/images/2025-12-06-02-49-55.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 认知负荷与可视化 (Cognitive Load & Visualization)
**工作记忆 (Working Memory)**: 认知心理学认为，人脑的工作记忆容量非常有限（通常为 7±2 个单位）。当**您**面对成千上万行的表格时，试图在脑中构建整体图像会瞬间耗尽认知资源，导致“认知超载”。

**前注意属性 (Preattentive Attributes)**: 可视化利用了人脑强大的视觉皮层，将“阅读数字”转化为“模式识别”。例如，人眼能瞬间识别出**长度**（柱子高低）、**颜色**（深浅）、**位置**（散点分布）。
这种转化绕过了工作记忆的瓶颈，实现了 **“瞬间认知”**。对于教育工作者来说，这意味着**您**可以用一张图表，在几秒钟内让听众（学生、家长、领导）理解复杂的教学数据。

</div>

---

## **愿景：从表格到“数据驾驶舱”**

<div class="align-top-center">

![数据驾驶舱示意图：深色背景，中央是中国地图热力图，四周环绕各种统计图表 width:800px](../../../lectures/images/2025-12-06-02-52-14.png)

</div>

<div class="insight" style="font-size:0.8em">

🌟 **目标**: 这就是我们作为“AI数据分析师”的终极形态 —— 将冰冷的数据，变成辅助决策的**智慧大脑**。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 商业智能 (BI) 仪表盘
图中展示的通常被称为 **BI Dashboard (商业智能仪表盘)**。它将企业的关键绩效指标 (KPI) 以图形化的方式集中展示。
虽然我们本节课只学习画单张图表，但这种“将多个图表组合起来讲述一个完整故事”的思维，是数据分析的高级境界。

</div>

---

## **1. 引入：海量数据的认知挑战**

<div class="columns">

<div>

### ❌ 这种数据怎么看？
*(密密麻麻的 3000 行 Excel)*
- 北京, 故宫, 5A...
- 上海, 迪士尼, 5A...
- 三亚, 天涯海角, 4A...

**分析目标**: 找出全国 **5A景区最多** 的城市。

</div>

<div>

### ✅ 一图胜千言
*(一张清晰的横向柱状图)*
- 北京: ██████████
- 重庆: ████████
- 西安: ██████

**结论**: 可视化不是为了绘图，是为了**瞬间认知**。

</div>

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 前注意属性 (Preattentive Attributes)
右图之所以能被“瞬间认知”，是因为它利用了人眼的**前注意属性**。
这是 Colin Ware 在《Information Visualization: Perception for Design》中提出的核心概念。

**四大核心属性**:
1.  **形式 (Form)**: 长度、宽度、方向、形状。
2.  **颜色 (Color)**: 色相、饱和度。
3.  **位置 (Position)**: 二维空间位置。
4.  **运动 (Motion)**: 闪烁、移动。

**教学应用**: 当**您**制作教学PPT或展示科研成果时，应有意识地利用这些属性（如用**红色**高亮关键数据，用**长条**表示显著差异）来引导观众的视线，降低他们的理解成本。

</div>

---

## **2. 环境搭建与数据加载**

我们将使用一份包含 **3万条** 真实记录的 **中国旅游景点数据集**。

<div class="columns">
<div>

### **任务**
我们不需要死记硬背 `read_csv` 的语法。
直接告诉 AI 你的文件在哪里，让它帮你写代码。

### **AI 指令 (Prompt)**
> "我有一份数据文件，路径是 `data/china_tourism.csv`。
> 请帮我用 pandas 读取它，并打印前 5 行看看数据长什么样。
> 同时，请导入画图需要的 matplotlib 库。"

</div>
<div>

### **AI 生成的代码**
```python
import pandas as pd
import matplotlib.pyplot as plt 

# 读取数据
df = pd.read_csv('data/china_tourism.csv')

# 检查前5行
print(df.head())
```

**预期输出**:
```text
  City          名字  Level ...
0 北京    故宫博物院     5A ...
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Pandas与Matplotlib：数据科学的双璧
- **Pandas**: 名字来源于 "Panel Data"（面板数据）。它是 Python 数据分析的**瑞士军刀**，提供了类似于 Excel 的数据结构 (DataFrame) 和操作接口。
- **Matplotlib**: 名字来源于 "MATLAB Plotting Library"。它的设计初衷是在 Python 中复刻 MATLAB 强大的绘图功能。

**架构关系**:
Matplotlib 是底层绘图引擎，功能强大但 API 繁琐（需要写很多行代码来配置坐标轴、图例等）。
Pandas 在 Matplotlib 之上封装了一层高级接口 (`df.plot()`)，让**您**可以直接针对 DataFrame 绘图，大大简化了代码量。
这体现了软件工程中的**分层设计 (Layered Architecture)** 思想：底层负责灵活强大，上层负责简单易用。

</div>

---

## **⚠️ 技术贴士：中文显示的本地化配置**

<div class="columns">
<div>

**解决方案**: 这是通用的 **“标准配置”**，**无需理解原理**，建议将此段配置保存，**每次画图前复制粘贴**即可。

</div>
<div>

```python
# --- 解决中文乱码的标准配置 ---

# 设置中文字体 (自动适配 Windows/Mac)
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS'] 

# 解决负号显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False 
```

</div>
</div>
<div class='tip' style="margin-top: 1rem;font-size: 0.6em;">

💡 **常见问题**: Python 绘图库默认不支持中文，直接画图会显示为方块 (□□□)。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么会有中文乱码？(The Encoding Problem)
这是一个经典的**国际化 (i18n)** 问题。

**字体文件 (Font File)**: 计算机绘图需要字体文件（如 `.ttf`）来描述每个字符的形状（字形，Glyph）。
**Matplotlib 的默认设置**: 它默认使用的字体（如 `DejaVu Sans`）只包含 ASCII 字符（英文、数字、标点），**不包含**庞大的中文字符集（CJK）。

**方块 (Tofu)**: 当程序试图绘制“北京”两个字时，它在默认字体中找不到对应的字形描述，就会显示为一个“缺失符号”（通常是方块，俗称 Tofu）。

**解决方案**: 代码 `plt.rcParams['font.sans-serif'] = ['SimHei']` 的作用就是修改全局配置，告诉 Matplotlib：“请去加载 `SimHei`（黑体）这个字体文件”，从而正确渲染中文。

</div>

---

## **3. 任务一：旅游资源分布分析 (计数与柱状图)**

<div class="columns ratio-4-6">
<div>

### **场景**
暑假想带孩子去一个景点**最密集**的地方，优化交通时间成本。

### **数据逻辑**
我们要做的动作叫 **“计数” (Counting)**。
即：统计 `City` 列中，每个城市出现了多少次。

</div>
<div>

### **AI 指令 (Prompt)**

> "请帮我统计 `City` 这一列中，各个城市出现的次数。
> 然后取前 10 名，画一个**柱状图 (Bar Chart)**。
> 标题设为 '热门旅游城市 Top 10'，颜色设为天蓝色。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 原始数据 vs. 聚合数据 (Raw vs. Aggregated Data)
这是数据分析中一对核心概念，理解它们的区别至关重要。

- **原始数据 (Raw Data)**: 未经处理的记录。每一行代表一个具体的实体（如一个景点、一次交易）。
  - **类比**: **您**收上来的几百份**学生试卷**，每一份都是独立的。
- **聚合数据 (Aggregated Data)**: 经过统计汇总后的数据。每一行代表一个类别（如一个城市、一个班级）。
  - **类比**: **您** 统计出的 **“各分数段人数表”** 或 **“班级平均分表”**。

**思维跃迁**: 画图（尤其是统计图表）通常都是基于**聚合数据**进行的。从关注“个例”（Raw）转向关注“整体分布”（Aggregated），是**您**成为数据分析师的关键思维跃迁。

</div>

---

## **代码解析：`.value_counts()`**

<div class="columns">
<div>

```python
# 1. 统计 + 排序 + 取前10
# value_counts() 自动按数量降序排列
top_cities = df['City'].value_counts().head(10)

# 2. 画图 (kind='bar')
# figsize=(10, 6) 控制图片大小
# rot=0 让x轴标签横向显示，提升阅读体验
top_cities.plot(kind='bar', figsize=(10, 6), 
                color='skyblue', rot=0)

plt.title('热门旅游城市 Top 10')
plt.xlabel('城市')
plt.ylabel('景点数量')
plt.show()
```

</div>
<div>

### **关键点**
*   **`value_counts()`**: 数据分析高频函数，专门用于统计分类数据的频次。
*   **`kind='bar'`**: 指定绘制“柱状图”。
*   **`plt.show()`**: 显示图表。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Pandas 绘图接口设计
Pandas 采用了**面向对象**的封装方式，将绘图功能集成在 DataFrame 对象上。

- **`df.plot()`**: 这是入口函数。
- **`kind` 参数**: 这是一个**多态 (Polymorphism)** 设计。通过改变这个参数，同一个函数可以表现出完全不同的行为（画出不同类型的图）。
  - `kind='bar'`: 垂直柱状图 (Vertical Bar Plot)
  - `kind='barh'`: 水平柱状图 (Horizontal Bar Plot)
  - `kind='line'`: 折线图 (Line Plot)

**`rot=0`**: 这是一个细节优化。默认情况下，Pandas 为了防止标签重叠，会将 x 轴标签旋转 90 度。但这对于中文阅读非常不友好。将其设为 0，强制标签水平放置，体现了**用户体验 (UX)** 优先的设计思维。

</div>

---

## **3. 旅游资源分布分析结果**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **图表解读**
*   **Top 1**: 日喀则以绝对优势位居榜首，拉萨紧随其后。
*   **趋势**: 热门城市多集中在**西藏、云南**等自然风光与民族文化浓郁的地区。
*   **意外发现**: 驻马店等非传统热门城市上榜，说明 A 级景区数量多并不完全等同于游客热度高。

### **价值**
这张图瞬间帮我们从 3000 多条数据中锁定 **“资源最丰富”** 的地区，为目的地选择提供了第一手依据。

</div>
<div class="align-middle-center">

![热门旅游城市 Top 10](data/1-3.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 帕累托法则 (Pareto Principle)
这张图表揭示了旅游资源分布的极度不均衡性，这符合著名的**帕累托法则**，也称为**二八定律 (80/20 Rule)**。

**历史背景**: 1906年，意大利经济学家 **Vilfredo Pareto** 发现，意大利 80% 的土地由 20% 的人口所有。后来这一规律被推广到各个领域。

**数据洞察**: 在本案例中，少数几个头部城市（如日喀则、拉萨、丽江）占据了绝大多数的 5A/4A 景区资源。
**应用**: 理解这种“幂律分布” (Power Law Distribution) 是进行商业分析（如识别核心客户）或政策制定（如资源倾斜）的基础。

</div>

---

## **4. 核心任务二：旅游成本分析 (分组与聚合)**

<div class="columns ratio-4-6">
<div>

### **场景**
预算有限，希望识别门票价格较高的城市，进行规避。
**哪个城市的平均门票价格最高？**

### **数据逻辑：分组聚合**
1.  **拆分**: 将数据按“城市”分组。
2.  **计算**: 计算每组的“平均价格”。
3.  **排序**: 按价格从高到低排列。

</div>
<div>

### **AI 指令 (Prompt)**

> "我有一列 `City` (城市) 和一列 `Sold_Price` (价格)。
> 请帮我按城市分组 (`groupby`)，计算每个城市的**平均价格**。
> 然后**从高到低排序**，取前 10 名。
> 最后画一个**横向柱状图 (barh)**，方便阅读城市名。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### “拆分-应用-合并” (Split-Apply-Combine)
这是数据科学大师 **Hadley Wickham** (R语言 ggplot2 作者) 提出的著名策略，是处理分组运算的标准范式。

**过程详解**:
1.  **Split (拆分)**: 将数据集按某个键（如 `City`）切分成多个小块。
    - *类比*: 将全校试卷按 **“班级”** 分堆。
2.  **Apply (应用)**: 对每个小块独立应用一个函数（如 `mean()`）。
    - *类比*: 计算每一堆试卷的 **“平均分”**。
3.  **Combine (合并)**: 将计算结果重新组合成一个新的数据结构。
    - *类比*: 填入一张新的 **“年级成绩表”**。

Pandas 的 `groupby` 函数完美实现了这一策略，让**您**能用一行代码完成这个复杂的“分治”过程。

</div>

---

## **代码解析：`.groupby()`**

```python
# 1. 分组 -> 计算平均值 -> 排序 -> 取前10
# groupby('City'): 按城市分组
# ['Sold_Price'].mean(): 计算价格平均值
expensive_cities = df.groupby('City')['Sold_Price'].mean() \
                     .sort_values(ascending=False).head(10)

# 2. 画横向柱状图 (kind='barh')
# alpha=0.8 设置透明度，视觉效果更柔和
expensive_cities.plot(kind='barh', figsize=(10, 6), color='salmon', alpha=0.8)

plt.title('平均门票价格最贵的城市 Top 10')
plt.xlabel('平均价格 (元)')
plt.show()
```

<div class='insight' style="margin-top: 1rem;font-size: 0.6em;">

💡 **技巧**: 当标签（城市名）较长时，使用**横向柱状图 (`barh`)** 阅读体验更好。
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么用 barh？(Visual Ergonomics)
这是一个**视觉人体工程学**的问题。

**阅读习惯**: 人眼的自然阅读顺序是从左到右、从上到下。
**标签可读性**: 
- **垂直柱状图 (Bar)**: x轴标签空间有限。当标签很长（如“阿坝藏族羌族自治州”）时，必须旋转或换行，导致阅读困难。
- **水平柱状图 (Barh)**: y轴标签有充足的横向空间，可以完整展示长文本，且符合从左到右的阅读流。

**最佳实践**: 当分类标签超过 5-7 个字符，或者类别数量较多（>10）时，优先选择 **横向柱状图**。

</div>

---

## **4. 旅游成本分析结果**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **图表解读**
*   **Top 3**: **甘孜**以接近 300 元的均价遥遥领先，**三沙**、**林芝**紧随其后。
*   **规律**: “最贵”的城市主要集中在**西部高原**（甘孜、林芝、怒江、迪庆）和**稀缺海岛**（三沙）。
*   **商业乐园**: 广州、珠海的上榜，主要是由长隆等大型商业主题乐园的高票价拉动的。

### **洞察**
“贵”通常意味着**稀缺**（高原/海岛）或**高投入**（大型乐园）。

</div>
<div class="align-middle-center">

![平均门票价格最贵的城市 Top 10](data/1-4.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 稀缺性溢价 (Scarcity Premium)
价格不仅仅是成本的反映，更是 **供需关系**的体现。

**经济学原理**: 
- **供给侧**: 甘孜、三沙拥有不可复制的自然资源（高原、纯净海岛），供给极度有限。
- **需求侧**: 随着消费升级，人们对独特体验的追求增加。

这种供需失衡导致了 **“稀缺性溢价”**。对于数据分析师来说，看到高价异常值时，不要急着认为是数据错误，先思考一下背后是否存在这种“稀缺性”逻辑。
这提醒**您**：数据分析不能脱离 **领域知识 (Domain Knowledge)**，否则容易得出肤浅甚至错误的结论。

</div>

---

## **5. 任务三：不同等级景区数量对比**

<div class="columns ratio-4-6">
<div>

### **任务**
我们只看了城市和价格，还没看过 **景区等级** (`Level`)。
1.  统计全国 **5A、4A、3A** 景区各有多少个？
2.  画一个 **饼图 (Pie Chart)** 来展示比例。

</div>

<div>

### **AI 指令**
> "请帮我统计 `Level` 列中每个等级的数量。
> 然后画一个**饼图 (Pie Chart)**。
> 标题设为 '中国A级景区等级分布'。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 饼图的争议与适用性 (The Pie Chart Controversy)
数据可视化界对饼图褒贬不一。Edward Tufte 等大师认为饼图难以精确比较面积。
**适用场景**: 当**您**关注的是“部分与整体的关系” (Part-to-Whole)，且类别较少（<5个）时，饼图依然是最直观的选择。
**最佳实践**: 如果类别过多，饼图会变得难以阅读（“碎盘子”效应），此时应优先选择**条形图**。

</div>

---

## **代码解析：饼图绘制**

<div class="columns">
<div>

```python
# 1. 统计
level_counts = df['Level'].value_counts()

# 2. 画饼图 (kind='pie')
# autopct='%1.1f%%' 显示百分比
level_counts.plot(kind='pie', figsize=(6, 6), 
                  autopct='%1.1f%%', title='等级分布')
plt.ylabel('') # 去掉Y轴标签更美观
plt.show()
```

</div>
<div>

### **关键点**
*   **`kind='pie'`**: 指定绘制饼图。
*   **`autopct`**: 自动计算并显示百分比，`%1.1f%%` 表示保留一位小数。
*   **`plt.ylabel('')`**: 饼图默认会显示Y轴标签，通常为了美观会将其隐藏。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 格式化字符串 (Format String)
`autopct='%1.1f%%'` 中的 `%1.1f` 是 Python 经典的 C 风格格式化符号 (C-style Formatting)，虽然现在推荐用 f-string，但在 Matplotlib 等老牌库中依然广泛使用。
- `%`: 占位符开始。
- `1.1`: 总宽度至少1位，保留1位小数。
- `f`: 浮点数 (float)。
- `%%`: 转义字符，输出一个字面量的百分号。

**绘图美学 (Aesthetics)**:
`plt.ylabel('')` 的作用是移除 Y 轴标签。虽然在数学上饼图没有 Y 轴，但 Pandas 绘图函数默认会把列名作为 Y 轴标签打印在图表左侧。这在饼图中显得多余且破坏美感，因此我们习惯性地将其隐藏。这体现了 **“少即是多” (Less is More)** 的设计原则。

</div>

---

## **5. 景区等级分布分析结果**

<div class="columns">
<div>

### **图表解读**
*   **占比最大**: **3A景区**占据了半壁江山（约56.8%），是A级景区的主力军。
*   **中坚力量**: **4A景区**占比约为25%，提供了丰富的高质量旅游选择。
*   **金字塔尖**: **5A景区**最为稀缺，仅占约2.4%，代表了国内顶级旅游资源。

### **洞察**
中国旅游景区等级分布呈现出典型的**钻石型结构**，中间等级（3A）数量最多。

</div>
<div class="align-middle-center">

![等级分布饼图](data/1-5.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 结构化分析 (Structural Analysis)
通过饼图，**您**不仅看到了“各有多少”，更看到了数据的 **“结构” (Structure)**。
这种 **中间大、两头小**的结构（3A最多，5A和1A较少）在社会科学中非常常见，类似于**正态分布 (Normal Distribution)** 的钟形曲线。

**产业洞察**:
- **5A (塔尖)**: 稀缺资源，主打品牌溢价。
- **3A/4A (塔身)**: 中坚力量，主打性价比和大众市场。

这种从图形到结构的思维跃迁，是数据分析师的核心素养。

</div>

---

## **6. 课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **中文配置**: 复制粘贴 `plt.rcParams`。
2.  **数量排名**: 使用 **柱状图** (bar) 展示 Top 10。
3.  **分类比较**: 使用 **条形图** (barh) 展示长标签数据。
4.  **占比分析**: 使用 **饼图** (pie) 展示整体结构。

</div>
<div>

### **下节课预告**
我们现在只能看到“哪里多”、“哪里贵”。
但 **“贵真的代表好吗？”**
下节课，我们将化身侦探，用 **散点图**、**直方图** 和 **箱线图**，去挖掘数据背后更深层的秘密关系与分布规律！

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 图表选择指南 (Chart Selection Guide)
这是数据可视化的核心方法论，通常被称为 **"Visual Vocabulary" (视觉词汇)**。

1.  **比较 (Comparison)**: 
    - 项目少: **柱状图 (Bar)**
    - 项目多/标签长: **条形图 (Barh)**
2.  **构成 (Composition)**: 
    - 静态占比: **饼图 (Pie)**
    - 随时间变化: 堆叠柱状图 (Stacked Bar)
3.  **分布 (Distribution)**: **直方图 (Histogram)**, **箱线图 (Boxplot)** (下节课重点)
4.  **关系 (Relationship)**: **散点图 (Scatter)** (下节课重点)

掌握这个分类体系，**您**就能应对 80% 的日常分析需求。

</div>