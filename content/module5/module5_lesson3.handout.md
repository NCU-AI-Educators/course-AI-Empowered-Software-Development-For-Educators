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
![bg blur:3px brightness:60%](../../../lectures/images/2025-12-06-03-05-06.png)

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
## 第19节课: 高阶可视化——不仅要准，还要美

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Seaborn vs Matplotlib
如果说 Matplotlib 是手动挡汽车（功能强大但操作复杂），那么 Seaborn 就是自动挡跑车（操作简单且颜值高）。
Seaborn 是建立在 Matplotlib 之上的，它简化了许多常见统计图形的绘制过程，并自带了非常美观的配色方案。

</div>

---

## **本课学习目标**

<div class="columns">
<div>

学完这节课，你将能够：

1.  **审美升级**: 从“统计图表”进阶到“信息图表”。
2.  **工具升级**: 掌握 **Seaborn** 的高级绘图功能。
3.  **技能**:
    - 绘制 **小提琴图 (Violin Plot)** 展示分布。
    - 绘制 **成对关系图 (PairPlot)** 展示多维关系。
    - 体验用**一行代码**完成数据全景扫描的快感。

</div>
<div class="align-middle-center">

![配图占位符](../../../lectures/images/2025-12-06-03-06-41.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 声明式绘图 (Declarative Visualization)
Seaborn 的设计哲学是“声明式”的。
你只需要告诉它“我想画Level和Sold_Price的关系”，而不需要像在Matplotlib中那样详细规定“画一条线，起点在哪终点在哪”。这让我们能更专注于分析逻辑。

</div>

---

## **1. 任务一：美学升级——Seaborn 小提琴图**

<div class="columns ratio-4-6">
<div>

### **痛点：箱线图样式单调**
我们想对比 5A/4A 景区的价格分布。
- **箱线图 (Boxplot)**: 只能看中位数，看不到分布形状。
- **小提琴图 (Violin Plot)**: = 箱线图 + 直方图。既能看“胖瘦”（分布），又能看“高低”（价格）。

### **工具：Seaborn**
Python 可视化界的**美学典范**。

</div>
<div>

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 设置一个好看的主题
sns.set_theme(style="whitegrid")

# 依然要配置中文
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 核密度估计 (KDE)
小提琴图优美的轮廓线其实是数据的 **核密度估计 (Kernel Density Estimation)** 曲线。
简单来说，它就像把直方图的锯齿抹平了，变成了一条光滑的曲线，能更优雅地展示数据在不同数值上的密集程度。

</div>

---

## **AI 指令：绘制小提琴图**

<div class="columns ratio-4-6"  style="font-size:0.9em">
<div>

### **AI 指令 (Prompt)**

> "请使用 seaborn 库画一个**小提琴图 (Violin Plot)**。
> - **X轴**: `Level` (景区等级)，顺序为 ['5A', '4A', '3A']。
> - **Y轴**: `Sold_Price` (门票价格)。
> - **过滤**: 去掉价格 > 1000 的极端值、价格 < 10 的杂项。
> - **配色**: 使用 'muted' 调色板。"

</div>
<div>

### **代码解析**
```python
# 1. 过滤异常值 (保留 10-1000 元之间的数据)
df_clean = df[(df['Sold_Price'] < 1000) & 
              (df['Sold_Price'] > 10)]

# 2. 画图
sns.violinplot(data=df_clean, 
               x='Level', y='Sold_Price', 
               order=['5A', '4A', '3A'], 
               palette='muted')

plt.title('不同等级景区价格“体型”对比')
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 调色板 (Palette)
Seaborn 提供了非常丰富的内置调色板。
- `muted`: 柔和色调。
- `bright`: 明亮色调。
- `pastel`: 粉笔色调（适合打印）。
- `coolwarm`: 冷暖渐变（适合热力图）。
选择合适的配色是提升图表专业度的第一步。

</div>

---

## **任务一结果：不同等级的价格“体型”**

<div class="columns ratio-6-4" style="font-size:0.9em">
<div>

### **图表解读**
1.  **5A (头重脚轻)**: 蓝色小提琴有一个长长的“脖子”伸向高价区。说明 5A 景区**整体上限极高**。
2.  **4A (一枝独秀)**: 橙色小提琴虽然重心较低，但有一根极细的“尖刺”伸向了比 5A 更高的价格区。这说明个别 4A 景区（可能是高端小众景点）的价格甚至超过了 5A。
3.  **3A (大肚便便)**: 绿色小提琴的“肚子”贴在底部（低价区）。说明绝大多数 3A 景区都是**平价甚至免费**的。

### **洞察**
*   **等级溢价**: 5A 的“长脖子”证明了品牌溢价的存在。
*   **市场分层**: 3A 主打亲民，5A 主打高端，市场定位泾渭分明。
*   **隐形冠军**: 4A 中的“尖刺”提示我们，某些细分领域的精品项目（如高端民宿）定价能力超越了 5A。

</div>
<div class="align-middle-center">

![不同等级景区价格小提琴图](data/3-1_violin.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 概率密度 (Probability Density)
小提琴图的宽度代表了**概率密度**。
“肚子”越宽，说明数据落在该价格区间的概率越大（即景点数量越多）。
“脖子”越长，说明数据的**长尾分布 (Long Tail)** 越明显，即存在少量的极端高价。

</div>

---

## **2. 任务二：全局概览——成对关系图 (PairPlot)**

<div class="columns">
<div>

### **场景：数据全景扫描**
我们想看：**“价格、评分、等级这三个变量之间，到底有什么错综复杂的关系？”**

如果用散点图，我们要画：
*   价格 vs 评分
*   价格 vs 等级
*   评分 vs 等级 ...

**PairPlot** 可以**一行代码画出所有关系**。

</div>
<div class="align-middle-center">

![PairPlot示意图：一个密密麻麻的图表矩阵](../../../lectures/images/2025-12-06-03-09-17.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 矩阵散点图 (Scatter Matrix)
PairPlot 本质上是一个 n*n 的矩阵。
- **对角线上**: 是单变量的分布图（自己和自己比，如直方图）。
- **非对角线上**: 是双变量的散点图（两两相比）。
这种图表能极快地暴露数据集中潜藏的相关性或聚类模式。

</div>

---

## **AI 指令：绘制成对关系图 (进阶)**

<div class="columns">
<div>

**请向 AI 发送以下指令**：

> "我想对数据进行全景扫描。
> 请使用 `sns.pairplot` 画出 **成对关系图**。
> - **分析变量**：`Sold_Price` (价格) 和 `Rating_Clean` (评分)。
> - **分类变量**：`Level` (用 `hue` 参数根据等级上不同的颜色)。
> - **数据源**：使用 `df_clean`，并**进一步过滤掉评分=0**的数据。"

</div>
<div>

### **代码实现**
```python
# 1. 准备数据：过滤掉评分=0的记录
df_pair = df_clean[df_clean['Rating_Clean'] > 0]

# 2. 绘制成对关系图
# hue='Level': 按照等级着色 (5A=蓝, 4A=橙...)
sns.pairplot(df_pair, 
             vars=['Sold_Price', 'Rating_Clean'], 
             hue='Level',
             height=3)
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 维度增加 (Adding Dimensions)
普通的散点图只能展示 X 和 Y 两个维度。
通过 `hue`（颜色）、`size`（点的大小）、`style`（点的形状），我们可以将 3维甚至 4维、5维 的信息压缩到一张二维平面图中。
在本例中，我们同时看到了：价格(X)、评分(Y)、等级(Color) 三个维度的信息。

</div>

---

## **任务二结果：多维关系的“全景图”**

<div class="columns" style="font-size:0.8em">
<div class="styled-div" style="font-size:0.55em">

### **图表解读**
1.  **对角线 (单变量分布)**: 
    - **左上角 (价格)**: 绝大多数景点都很便宜（右偏分布）。
    - **右下角 (评分)**: 绝大多数景点都是高分（左偏分布）。
2.  **非对角线 (双变量关系 - 分段看)**:
1.  **低价区 (<200)**: **良莠不齐**。既有满分评价，也有低分巨坑（散点上下分布极广）。
2.  **中价区 (200-800)**: **品质收敛**。低分点消失了！说明多花钱确实能买到“下限保障”（避雷）。
3.  **高价区 (>800)**: **边际效应递减**。价格虽高，但评分并没有继续上升，反而因为期望过高而难以打出满分。

### **洞察**
*   **非线性关系**: 价格和评分不是简单的正比关系，而是呈现出复杂的**倒U型**或**收敛**趋势。
*   **消费决策**: 预算有限选低价（需慧眼识珠），追求稳妥选中价（花钱买下限）。

</div>
<div>

![PairPlot结果](data/3-2_pairplot.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 矩阵图的阅读逻辑 (Reading Logic)
PairPlot 将多维数据展开为一个 **N x N 矩阵**，阅读时需区分两个区域：
1.  **非对角线 (Off-diagonal)**: **看关系 (Relationship)**。
    - **坐标**: (1,2) 和 (2,1)。
    - **图表**: **散点图**。展示两个不同变量（如 价格 vs 评分）是如何相互影响的。
2.  **主对角线 (Diagonal)**: **看分布 (Distribution)**。
    - **图表**: **密度图 (KDE)**。你可以把它看作是数据的“山峰”。
    - **坐标轴**:
      - **横轴 (X-axis)**: 变量的值（如：价格 100元）。
      - **纵轴 (Y-axis)**: **密度 (Density)**。简单理解就是“浓度”。
        - **高度**: 代表样本的**密集程度**。峰值越高，说明聚集在这里的景点越多。
        - **面积**: 曲线下的总面积代表**样本总数** (100%)。
    - **怎么看**:
      - **(1,1) 价格分布**: 山峰集中在**横轴左侧**（低价区）。解读：**绝大多数景点都很便宜**。
      - **(2,2) 评分分布**: 山峰集中在**横轴右侧**（高分区）。解读：**绝大多数景点评分都很高**。

</div>

---

## **3. 任务三：量化关系——相关系数热力图**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **任务**
PairPlot 让我们看到了关系，那能不能**量化**这种关系？
请计算变量之间的 **相关系数 (Correlation)** 并可视化。

### **AI 指令**
> "请计算 `Sold_Price` 和 `Rating_Clean` 的相关系数。
> 并用 `sns.heatmap` 画出**相关系数矩阵的热力图**。
> 显示数值 (`annot=True`)。"

</div>
<div>

### **参考示范**
```python
# 1. 计算相关系数矩阵
corr_matrix = df_clean[['Sold_Price', 'Rating_Clean']].corr()

# 2. 画热力图
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('价格与评分的相关性')
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 皮尔逊相关系数 (Pearson Correlation)
`.corr()` 默认计算的是皮尔逊系数，它衡量的是**线性相关性**。
**重要假设**: 皮尔逊系数假设变量之间存在线性关系。如果关系是非线性的（如抛物线），系数可能为0，但实际上两者紧密相关。
**安斯库姆四重奏 (Anscombe's Quartet)**: 正如我们在 **Lesson 2** 中所见，四组数据可能拥有相同的统计特性（如相关系数），但图形分布截然不同。这再次提醒我们：**不要盲目迷信数字**，必须结合可视化（如 PairPlot）来交叉验证。

</div>

---

## **任务三结果：量化关系的“体检单”**

<div class="columns" style="font-size:0.8em">
<div>

### **图表解读**
*   **0.11 (弱相关)**: 价格和评分的相关系数仅为 **0.11**。
*   **接近 0**: 说明两者几乎**线性无关**。
*   **颜色**: 呈现**冷色调**（蓝色），直观地反映了相关性极低（远离 1.0 的红色热区）。

### **洞察**
*   **高价 $\neq$ 高分**: 数据的弱相关性表明，昂贵的门票并不意味着游客会有更高的满意度（性价比才是关键）。
*   **多因素驱动**: 游客的满意度可能更多取决于服务、景观、拥挤度等其他因素，而非单纯的价格。

</div>
<div class="align-middle-center">

![热力图结果](data/3-3_heatmap.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 相关性 != 因果性 (Correlation != Causation)
即使系数很高（比如 0.9），也不能说明“价格导致了评分高”。
更何况这里系数很低 (0.11)，说明两者在统计学上几乎是独立的。
这提醒我们在做决策时，不能单一归因。

</div>

---

## **4. 任务四：综合案例——江西省全景报告**

<div class="columns" style="font-size:0.9em">
<div>

### **从“单点”到“全景”**
前面我们学习了各种图表（柱状图、散点图、小提琴图）。
现在，让我们把这些“积木”组合起来，为一个省份（以 **江西省** 为例）制作一份全方位的“体检报告”。

### **分析目标 (3D View)**
1.  **资源 (Quantity)**: A 级景区结构是怎样的？
2.  **消费 (Cost)**: 门票价格分布如何？
3.  **口碑 (Value)**: 性价比如何？

**成果**: 一张包含 4 个子图的 **高清全景报告**。

</div>
<div class="align-middle-center">

![配图：一张包含饼图、分布图、散点图的组合分析报告示意图](../../../lectures/images/2025-12-06-03-12-38.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 综合项目 (Capstone Project)
在布鲁姆教育目标分类法 (Bloom's Taxonomy) 中，**“创造 (Create)”** 是最高阶的认知目标。
本环节的设计意图，就是希望读者能从“理解”和“应用”碎片化知识，跃升到“综合”运用多种技能来解决复杂问题。
它不引入新知识，而是强调知识的**整合 (Integration)** 和**迁移 (Transfer)**。

</div>

---

## **版面规划与 AI 指令**

<div class="columns" style="font-size:0.85em">
<div>

### **版面设计 (2x2 布局)**
*   **左上**: **饼图** (景区等级占比)
*   **右上**: **小提琴图** (价格分布形状)
*   **左下**: **散点图** (价格 vs 评分)
*   **右下**: **热力图** (相关性强度)

### **关键 AI 指令**
> "请帮我筛选出 `df` 中属于 '江西省' 的数据。
> **过滤掉价格<10及评分=0的异常值**。
> 画一个 2x2 的组合图：
> 饼图、小提琴图、散点图、热力图。
> 设置总标题为 '江西省旅游竞争力全景分析'。"

</div>
<div>

### **代码实现**
```python
# 1. 数据准备 (江西11地市)
jiangxi_cities = ['南昌', '九江', '景德镇', '上饶', '赣州', 
                  '宜春', '吉安', '抚州', '萍乡', '新余', '鹰潭']
# 筛选并清洗数据
df_jx = df[df['City'].isin(jiangxi_cities) &
           (df['Sold_Price'] > 10) &
           (df['Rating_Clean'] > 0)]

# 2. 创建画布
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 3. 绘制子图
# 左上：饼图
df_jx['Level'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=axes[0,0])
axes[0,0].set_ylabel('')
# 右上：小提琴图
sns.violinplot(data=df_jx, x='Level', y='Sold_Price', 
               order=['5A','4A','3A','2A','1A'], ax=axes[0,1])
# 左下：散点图
sns.scatterplot(data=df_jx, x='Sold_Price', y='Rating_Clean', 
                hue='Level', ax=axes[1,0])
# 右下：热力图
sns.heatmap(df_jx[['Sold_Price', 'Rating_Clean']].corr(), 
            annot=True, cmap='coolwarm', ax=axes[1,1])

# 4. 调整布局
plt.suptitle('江西省旅游竞争力全景分析', fontsize=20)
plt.tight_layout()
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 仪表板设计 (Dashboard Design)
将多个图表组合在一起不仅仅是技术实现，更是一种设计艺术。
**信息层级 (Information Hierarchy)**: 
- 左上角通常是最重要的位置（饼图：总体结构）。
- 右上展示细节（小提琴图：分布特征）。
- 左下展示深度关系（散点图：相关性）。
- 右下角展示量化指标（热力图：相关系数）。
这种布局符合用户的 **“F型”阅读习惯 (F-Shaped Pattern)**：
用户浏览页面时，视线通常先水平扫视顶部（第一行），然后视线略微下移进行第二次较短的水平扫视，最后垂直扫描左侧内容。因此，**左上角**和**顶部**是视觉关注度最高的区域，适合放置核心结论或总体概览。

</div>

---

## **任务四结果：江西省全景报告**

<div class="columns ratio-4-6" style="font-size:0.65em">
<div class="styled-div" style="font-size:0.8em">

### **图表解读**
1.  **资源 (左上)**: **4A级景区**占据半壁江山 (46.7%)，是江西旅游的中坚力量。5A级 (6.7%) 稀缺且珍贵。
2.  **消费 (右上)**: 价格分布极不均匀。**2A级**价格跨度最大（有平价也有高价），而**5A级**价格相对集中。
3.  **口碑 (左下)**: **性价比之王**出现在低价区。高分景点（>4.5分）大多集中在 200元以下。
4.  **关系 (右下)**: 相关系数 **0.12**，再次验证了“高价不等于高分”的普遍规律。

### **洞察**
*   **江西旅游画像**: 一个以 **4A级景区** 为主导，**性价比极高** 的旅游目的地。
*   **建议**: 重点挖掘 4A 级景区中的“隐形冠军”（低价高分），避开高价低分的“坑”。

</div>
<div class="align-middle-center">

![江西省全景报告](data/3-4_jiangxi.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据讲故事 (Data Storytelling)
数据分析的终局不是“图表”，而是“故事”。
这张全景图其实在讲述一个关于江西旅游的故事：
“虽然我没有那么多顶级的5A（饼图），但我有海量的4A（饼图），而且价格丰俭由人（小提琴图），只要你肯淘，就能在低价区找到高分宝藏（散点图）。”
**您**在制作报告时，也要学会像这样把碎片化的图表串联成一条逻辑线索。
### 为什么要做全景分析？
单一图表只能看到大象的一条腿。
只有把不同维度的图表组合在一起，才能拼凑出大象的全貌。
这就是**Dashboard (仪表盘)** 的雏形，也是商业分析报告的标准形式。

</div>

---

## **5. 课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **高级绘图**: Seaborn 的小提琴图与成对关系图。
2.  **多维分析**: 从单变量到多变量的关系探索。
3.  **综合应用**: 如何将多个图表组合成一份全景报告。

</div>
<div>

### **下节课预告 (实战工作坊)**
掌握了分析工具后，最重要的是将其**迁移**到您关注的领域。
下节课，我们将进行**实战演练**。
邀请您选择一个感兴趣的省份，从数据探查到可视化，亲手制作一份**完整的数据洞察报告**。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据素养 (Data Literacy)
Gartner 将数据素养定义为：阅读、书写和交流数据的能力。
通过本模块的学习，**您**已经从一个单纯的“数据消费者”（看报表）进化为“数据生产者”（做报表）。
这种能力的跃迁，将极大地扩展**您**在数字化时代的教学和科研边界。

</div>