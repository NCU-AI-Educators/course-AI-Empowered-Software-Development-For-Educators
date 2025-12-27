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
![bg blur:3px brightness:60%](../../../lectures/images/2025-12-06-02-54-56.png)

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
## 第18节课: 可视化分析——数据背后的洞察

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 探索性数据分析 (EDA)
**历史背景**: 1977年，统计学大师 **John Tukey** 出版了经典著作《Exploratory Data Analysis》，正式确立了 EDA 的地位。他主张在进行复杂的统计建模之前，先用图表和简单的统计量来“倾听”数据。

**描述性 vs. 探索性**:
- **描述性分析 (Descriptive)**: 关注“过去发生了什么”。例如：上学期全班平均分是多少？（Fact-based）
- **探索性分析 (Exploratory)**: 关注“为什么发生”以及“变量间有什么关系”。例如：家庭作业完成率和考试成绩有相关性吗？（Insight-based）

从单纯的“现象描述”走向深层的“机制揭示”，是数据分析师进阶的关键一步。

</div>

---

## **引入：验证经验假设**

<div class="columns ratio-6-4">
<div>

**思考**：
在我们的潜意识里，是不是觉得“价格与质量成正比”？
**门票越贵的景区，评分就应该越高吗？**

*   ❌ **直觉**：这只是一个**假设 (Hypothesis)**。
*   ✅ **数据**：分析师不信直觉，只信**证据**。

**侦探工具**：散点图 (Scatter Plot)。

</div>
<div class="align-middle-center">

![配图：一个侦探拿着放大镜在看数据点](../../../lectures/images/2025-12-06-03-03-49.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 假设驱动分析 (Hypothesis-Driven Analysis)
这是科学方法 (Scientific Method) 在数据分析中的应用。

**流程**:
1.  **观察 (Observation)**: 门票贵的景点好像服务更好。
2.  **假设 (Hypothesis)**: 价格与评分呈正相关。
3.  **验证 (Verification)**: 绘制散点图，计算相关系数。
4.  **结论 (Conclusion)**: 证实或证伪。

**教学启示**: 这种思维方式与**探究式教学 (Inquiry-Based Learning)** 不谋而合。在教学中，**您**也可以鼓励学生先提出假设（“我认为...”），再寻找证据，而不是直接告诉他们答案。

</div>

---

## **本课学习目标**

<div class="columns">
<div>

学完这节课，你将能够：

1.  **思维**: 从“看结果”进阶到“找关系”。
2.  **工具**: 掌握 **散点图 (Scatter)** 和 **直方图 (Hist)** 的绘制。
3.  **实战**: 验证“价格越高，体验越好”的假设是否成立。
4.  **技能**: 使用多条件筛选 (`df[(A) & (B)]`) 寻找高性价比数据。

</div>
<div class="align-middle-center">

![配图占位符](../../../lectures/images/2025-12-06-02-59-49.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 变量关系
数据分析的核心往往在于探究两个或多个变量如何相互影响。
- **单变量分析**: 只看一个列（如：价格分布）。
- **双变量分析**: 看两列的关系（如：价格 vs 评分）。
本节课我们将带领**您**从单变量迈向双变量分析，这是理解复杂系统的必经之路。

</div>

---

## **任务一：价格 vs 评分 (散点图实战)**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **场景**
我们要在一张图上把所有 **3000多个** 收费景点都画出来。
看看它们是排成一条线（有关系），还是散落一地（没关系）。

### **AI 指令 (Prompt)**
> "请帮我画一个**散点图 (Scatter Plot)**：
> - **X轴**: `Sold_Price` (价格)
> - **Y轴**: `Rating_Clean` (评分)
> - 设置点的**透明度 (alpha)** 为 0.5，以免点太密集看不清。"

</div>
<div>

### **代码解析**
```python
# kind='scatter'
# alpha=0.5 让重叠的点颜色变深
df.plot(kind='scatter', x='Sold_Price', y='Rating_Clean', 
        alpha=0.5, color='purple')

plt.title('价格 vs 评分：寻找高性价比景点')
plt.xlabel('门票价格')
plt.ylabel('用户评分')
plt.grid(True) # 加网格更好看
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 相关性 (Correlation)
在统计学中，我们常用 **Pearson 相关系数 (r)** 来量化两个连续变量之间的线性关系。
- **r = 1**: 完美正相关 (Perfect Positive)
- **r = -1**: 完美负相关 (Perfect Negative)
- **r = 0**: 无线性相关 (No Correlation)

**安斯库姆四重奏 (Anscombe's Quartet)**: 统计学家 Francis Anscombe 构造了四组数据，它们的均值、方差、相关系数完全相同，但**散点图**形状截然不同。这有力地证明了：**“看图”比“看统计量”更重要**。散点图能揭示出统计量无法描述的非线性关系和异常值。

</div>

---

## **侦探时刻：你看到了什么？**

<div class="columns" style="font-size:0.8em">
<div>

### **图表解读**
*   **直觉预期**: 点应该均匀分布，或者排成一条线。
*   **实际看到的**: 
    1.  **图形畸形**: 大部分点都挤在左边一条狭长的区域里。
    2.  **右侧空旷**: 极少数几个点跑到了最右边（价格极高）。
    3.  **底部堆积**: 有很多评分为 0 的点。

### **初步判断**
这张图 **“生病了”**！
异常值（天价）和无效值（0分）严重干扰了我们的视线，导致我们看不清大部分正常景点的分布规律。

</div>
<div>

![散点图示意图：显示出受异常值影响严重的畸形图表](data/2-1.png)

<div class='insight' style="margin-top: 1rem;font-size: 0.6em;">

💡 **洞察**: 在得出结论之前，我们必须先**清洗数据**。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 读图能力：趋势与离散
绘制图表只是手段，读懂图表才是目的。

**趋势 (Trend)**: 数据的整体走向（向上、向下、平坦）。这对应统计学中的**期望值 (Expectation)**。
**离散 (Dispersion)**: 数据点围绕趋势线的松散程度。这对应统计学中的**方差 (Variance)**。

**教学类比**: 
- **趋势**: 就像**学生的学习曲线**，随着时间推移，成绩总体是上升的。
- **离散**: 就像**班级的两极分化**，如果点很散，说明学生水平参差不齐；如果点很聚拢，说明大家水平相当。

</div>

---

## **优化迭代：清洗后再看真相**

<div class="columns ratio-4-6">
<div>

### **清洗策略**
为了分析 **“付费景点的性价比”**，我们需要做三件事：
1.  **去天价**: 过滤价格 > 1000 的高端套餐。
2.  **去杂项**: 过滤价格 < 10 的电子导览/代金券。
3.  **去零分**: 过滤评分 = 0 的景点（暂无评分）。

</div>
<div>

### **代码实现**
```python
# 多条件筛选：保留 有评分、收费合理(10-1000元)的景点
df_filtered = df[
    (df['Rating_Clean'] > 0) & 
    (df['Sold_Price'] > 10) & 
    (df['Sold_Price'] < 1000)
]

df_filtered.plot(kind='scatter', 
                 x='Sold_Price', y='Rating_Clean', 
                 alpha=0.5, color='purple')
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据清洗 (Data Cleaning)
**GIGO 原则**: "Garbage In, Garbage Out" (垃圾进，垃圾出)。这是计算机科学中最著名的格言之一。

**清洗的维度**:
1.  **有效性 (Validity)**: 去除不符合业务规则的数据（如：价格 < 0，评分 > 5.0）。
2.  **准确性 (Accuracy)**: 修正错误数据。
3.  **完整性 (Completeness)**: 处理缺失值 (Missing Values)。
4.  **一致性 (Consistency)**: 统一单位和格式。

在本例中，我们去除“电子导览”和“天价套餐”，属于**业务逻辑清洗**，目的是为了让分析对象（门票）更加纯粹。

</div>

---

## **现在的真相：复杂的关系**

<div class="columns">
<div>

### **市场规律解读**
清洗后的图揭示了更有趣的市场规律：

1.  **低价区 (0-200元)**：**良莠不齐**。既有高分宝藏，也有低分雷区。选低价需“慧眼”。
2.  **中高价区 (200-800元)**：**品质收敛**。低分点消失，分数集中在高分段。**花钱能买到“下限保障”**。
3.  **高价区 (>800元)**：**边际效应**。价格再高，评分未线性上升，反而因用户高期待而略有回落。

</div>
<div class="align-middle-center">

![运行结果截图占位符](data/2-2.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 非线性关系与边际效用递减
现实世界中的变量关系往往不是简单的线性关系 (Linear Relationship)。

**边际效用递减 (Diminishing Marginal Utility)**: 经济学原理。随着投入增加，产出的增量逐渐减少。
- **商业**: 价格从 100 涨到 200，体验可能翻倍；但从 1000 涨到 2000，体验可能只提升 10%。
- **教育**: 学生从 0 分考到 60 分相对容易；但从 90 分考到 100 分，需要付出巨大的努力。

理解这种非线性关系，有助于**您**在资源有限的情况下，找到**投入产出比 (ROI)** 最高的那个点。

</div>

---

## **任务二：寻找“高性价比标杆” (多条件筛选)**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **场景**
既然图上有“宝藏区”（左上角），怎么把它们的名字找出来？

### **AI 指令 (Prompt)**
> "请帮我筛选出那些 **'高分低价'** 的景点。
> 条件是：
> 1. `Rating_Clean` 大于等于 4.8
> 2. `Sold_Price` 在 **50 到 200** 之间 (大众消费主力区)
> 
> 请列出这些景点的名字、城市和价格，按**评分从高到低**排序。"

</div>
<div>

### **代码解析**
```python
# 两个条件中间用 & 连接
# 每个条件必须加括号 ()，这是语法硬性规定
bargain_spots = df[ 
    (df['Rating_Clean'] >= 4.8) & 
    (df['Sold_Price'] >= 50) &
    (df['Sold_Price'] <= 200)
]

# 排序并显示
print(bargain_spots.sort_values('Rating_Clean', ascending=False) \
      [['名字', 'City', 'Sold_Price', 'Rating_Clean']].head(10))
```
<div class='tip' style="margin-top: 1rem;font-size: 0.6em;">

💡 **思考**: 有些景点虽然是 5.0 分，但可能非常小众（评分人数少），存在偶然性。在进阶分析中，通常需要引入 **“评论数”** 作为置信度门槛。
</div>

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 布尔逻辑与集合 (Boolean Logic & Sets)
代码中的 `&` 符号代表**逻辑与 (AND)**，在集合论中对应**交集 (Intersection)**。
这意味着筛选出的结果必须**同时**位于“高分集合”和“低价集合”的重叠区域。
理解这一点，有助于**您**构建更复杂的查询条件（如 `(A | B) & C`）。

</div>

---

## **任务二结果：高性价比宝藏榜**

<div class="columns">
<div>

### **榜单解读**
*   **特征分析**: 相比于低价区（<50元）多为公园/博物馆，这个区间（50-200元）涌现了大量 **“高成本体验型”旅游项目**，如**漂流、索道、海洋世界、溶洞**。
*   **价值发现**: 这些项目运营成本较高，能在这个价格段拿到高分，说明 **“物超所值”**。

### **⚠️ 避坑指南**
*   **样本量陷阱**: 某些 5.0 分景点可能只有寥寥几人评价（小众景点）。
*   **进阶技巧**: 在真实业务中，通常会要求 **“评论数 > 50”** 才纳入榜单，以确保评分的可靠性。

</div>
<div>

| 景点名称 | 城市 | 价格 |
| :--- | :--- | :--- |
| 九泷十八滩漂流 | 韶关 | 138 |
| 云丘山玉皇顶索道 | 临汾 | 70 |
| 阳泉海洋世界 | 阳泉 | 78 |
| 抚顺苏子河漂流 | 抚顺 | 73 |
| 石龙大峡谷 | 梧州 | 50 |
| 武进太湖湾景区 | 常州 | 60 |

*(注：均为评分>4.8的真实数据)*

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 幸存者偏差与置信度 (Survivorship Bias & Confidence)
**幸存者偏差**: 二战期间，统计学家 Abraham Wald 发现返航飞机的弹孔多集中在机翼，军方建议加固机翼。Wald 却建议加固**没有弹孔**的引擎——因为引擎中弹的飞机根本没能飞回来（没能成为“幸存者”）。

**数据应用**: 
- **评分陷阱**: 那些 5.0 分的景点，可能只是因为只有 1 个人评分（幸存者）。
- **置信度 (Confidence)**: 在统计学中，样本量越大，统计结果越可信。

**教学反馈**: 这就像**您**在课堂上，总是听到那几个活跃学生的意见（幸存者），而忽略了沉默的大多数。为了获得可信的反馈，**您**需要关注样本量，或者主动去收集那些“沉默者”的声音。

</div>

---

## **任务三：评分是否存在偏态分布？(直方图)**

<div class="columns ratio-4-6">
<div>

### **场景**
你可能会发现，怎么筛出来全是 4.8 分以上的？是不是大家的评分都很高？
我想看看**大部分景点的评分**到底在哪个区间？

### **工具：直方图 (Histogram)**
它可以告诉我们数据的**分布形状**。

</div>
<div>

### **AI 指令 (Prompt)**
> "请帮我画一个**直方图 (Histogram)**，看看 `Rating_Clean` 这一列的分布情况。
> 将数据分成 20 个区间 (bins=20)。"

### **代码解析**
```python
# kind='hist'
# 过滤掉0分（无评分）的数据
df[df['Rating_Clean'] > 0]['Rating_Clean'].plot(
    kind='hist', bins=20, 
    color='teal', edgecolor='black'
)

plt.title('全国景点评分分布图')
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 直方图 vs. 柱状图 (Histogram vs. Bar Chart)
这是初学者最容易混淆的两个概念。

| 特征 | 柱状图 (Bar Chart) | 直方图 (Histogram) |
| :--- | :--- | :--- |
| **数据类型** | 离散数据 (Categorical) | 连续数据 (Continuous) |
| **X轴含义** | 类别 (如城市、班级) | 数值区间 (如分数段、价格区间) |
| **柱子间距** | 有间距 (表示独立) | 无间距 (表示连续) |
| **形状含义** | 比较大小 | **分布形态** (Distribution) |

**教学类比**: 
- **柱状图**: 统计 **“各班级的人数”** 。
- **直方图**: 统计 **“全校学生的成绩分布”** （多少人考了60-70分，多少人考了70-80分）。

</div>

---

## **侦探分析：直方图解读**

<div class="columns">
<div>

### **观察**
*   图像严重**左偏**（高高的柱子集中在右侧）。
*   绝大多数评分都在 **4.0 - 5.0** 之间。
*   3.0 分以下的景点极少。

### **结论**
*   **评分虚高**: 确实存在，这被称为 **“评分通胀”**。
*   **决策调整**: 在选景点时，**4.0 分可能只是及格线**，4.5 分以上才算优秀。

</div>
<div class="align-middle-center">

![直方图示意图：柱子主要集中在4.0到5.0之间](data/2-3.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 偏态分布 (Skewness)
分布的形状蕴含着丰富的信息。

- **正态分布 (Normal Distribution)**: 钟形曲线，左右对称。大多数自然现象（如身高、智商）服从正态分布。
- **左偏/负偏 (Negative Skew)**: 尾巴拖在左边，大部分数据集中在右边（高分段）。
  - *含义*: **“天花板效应”**。如本例中的评分，或者一份过于简单的试卷。
- **右偏/正偏 (Positive Skew)**: 尾巴拖在右边，大部分数据集中在左边（低分段）。
  - *含义*: **“地板效应”**。如收入分布（少数富人拉高了平均值），或者一份极难的试卷。

识别偏态有助于**您**判断数据的**集中趋势**，此时**中位数 (Median)** 往往比**平均值 (Mean)** 更能代表大多数人的水平。

</div>

---

## **任务四：深入对比：5A真的比4A贵吗？**

<div class="columns ratio-4-6" style="font-size:0.8em">
<div>

### **任务**
我们想对比 **不同等级** 景区的价格分布。
看看 5A 景区是不是整体都比 4A 贵？

### **AI 指令**
> "请帮我画一个**箱线图 (Boxplot)**。
> - **X轴**: `Level` (景区等级)。
> - **Y轴**: `Sold_Price` (门票价格)。
> - **过滤**: 价格 大于 10 且 小于 300 的数据（去掉极端值）。"

</div>
<div>

### **参考示范**
```python
# 箱线图 (kind='box')
# by='Level': 按等级分组画箱子
# column='Sold_Price': 画价格的箱子
# 过滤掉极端高价(>300)和免费(0)的数据，只看收费景点的分布
df_paid = df[(df['Sold_Price'] < 300) & (df['Sold_Price'] > 10)]

df_paid.boxplot(
    by='Level', 
    column='Sold_Price', 
    figsize=(8, 6)
)

plt.title('不同等级景区价格对比')
plt.suptitle('') # 去掉默认生成的标题
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 箱线图 (Boxplot)
这是统计学大师 **John Tukey** 发明的另一种伟大图表，用于显示数据的**分散情况**。它基于 **“五数概括法” (Five-Number Summary)**：

1.  **最小值 (Minimum)**: 下边缘。
2.  **下四分位数 (Q1)**: 箱底。25% 的数据小于此值。
3.  **中位数 (Median)**: 箱中线。50% 的数据小于此值。
4.  **上四分位数 (Q3)**: 箱顶。75% 的数据小于此值。
5.  **最大值 (Maximum)**: 上边缘。

**异常值 (Outliers)**: 超出上下边缘的点通常被视为异常值（Tukey 定义为超过 1.5倍 IQR 的距离）。
箱线图是比较不同组别（如不同班级、不同等级景区）数据分布差异的最佳工具。

</div>

---

## **结论：等级即溢价**

<div class="columns" style="font-size:0.9em">
<div>

### **图表解读**
*   **阶梯式上升**: 从 1A 到 5A，箱子的位置（绿色中位数线）明显呈**台阶式上升**。
*   **5A的溢价**: 5A 景区的箱体明显高于其他等级，说明其起步价和均价都显著更高。

### **洞察**
虽然“评分”和“价格”没明显关系，但 **“官方等级”和“价格”呈现显著的正相关**。
*   **金字招牌**: “5A”是高价门票的关键原因。
*   **定价策略**: 等级越高，市场接受的溢价越高。

</div>
<div class="align-middle-center">

![箱线图示意图：显示出随等级升高价格明显上升的趋势](data/2-4.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 价格锚定与品牌溢价
**价格锚定 (Price Anchoring)**: 5A 级景区的高票价往往成为消费者心中的"价值锚点",让消费者潜意识认为"贵就是好"。
**品牌溢价 (Brand Premium)**: 5A 是国家背书的金字招牌。这张图证明了品牌不仅能带来流量,更能带来实实在在的溢价能力(定价权)。

</div>

---

## **任务五：景区等级越高体验越好吗？**

<div class="columns ratio-4-6">
<div>

### **场景**
5A 景区确实贵，但贵得有道理吗？
我们锁定 **200-800元** 的“中高消费”区间，看看在这个价位段，5A 的体验（评分）是否真的碾压 4A？

</div>
<div>

### **代码实现**
```python
# 1. 筛选中高价位数据
df_mid_high = df[(df['Sold_Price'] >= 200) & 
                 (df['Sold_Price'] <= 800) &
                 (df['Rating_Clean'] > 0)]

# 2. 绘制箱线图：等级 vs 评分
df_mid_high.boxplot(
    by='Level', 
    column='Rating_Clean', 
    figsize=(8, 6)
)
plt.show()
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 控制变量法 (Control Variable Method)
为了公平比较不同等级的体验差异,我们必须剔除"价格"这个干扰因素。
这种 **"控制其他变量不变,只改变一个变量(等级)"** 的方法,是科学实验和因果推断的核心思想。
如果不控制价格直接比较,5A的高分可能仅仅是因为它更贵(投入成本更高),而不是因为它的管理水平更高。

</div>

---

## **任务五结果：破解等级迷思**

<div class="columns" style="font-size:0.8em">
<div>

### **图表深度解读**
1.  **评分趋同**: 在 200-800 元区间，2A/3A/4A 的中位数与 5A **差异极小**。只要钱花到位了，体验通常都不差。
2.  **5A的价值**: 5A 的箱体极扁（方差小），说明**品质极度稳定**。选 5A 不一定最惊喜，但绝对**不踩雷**。
3.  **低A的机会**: 2A/3A/4A 虽然波动大，但上限高。同等高价下，它们往往是**特色鲜明的小众精品**。

### **决策建议**
*   **求稳（带长辈/客户）**: 选 **5A**。
*   **求新（个人/情侣）**: 选 **高价位的 3A/4A**。

</div>
<div class="align-middle-center">

![中高价位等级评分对比箱线图](data/2-5.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 方差与风险回报
**方差 (Variance)**: 箱线图的箱体高度代表了数据的离散程度(方差)。5A箱体扁,说明方差小,体验一致性高(风险低);2A/3A箱体长,说明方差大,体验波动大(风险高)。
**风险回报 (Risk-Return)**: 选择2A/3A就像投资高风险股票,可能获得超额回报(惊喜),也可能血本无归(踩雷);选择5A就像买国债,回报稳定但缺乏惊喜。

</div>

---

## **6. 课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **找关系**: `scatter` (散点图) -> 验证假设。
2.  **看分布**: `hist` (直方图) -> 发现虚高。
3.  **做对比**: `boxplot` (箱线图) -> 价格分层。
4.  **核心思维**: 数据分析 = 提出假设 + 画图验证。

</div>
<div>

### **下节课预告**
现在的图表只能看“两个变量”。
下节课，我们将进阶为 **“高级分析师”**。
引入 **Seaborn**，用 **小提琴图** 和 **成对关系图**，一眼看清数据中错综复杂的**多维关系**！

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 探索性数据分析 (EDA)
本节课我们进行的活动，在专业上称为 EDA (Exploratory Data Analysis)。
它不是为了生成最终报告，而是为了让分析师自己理解数据。
EDA 的核心动作就是：画图 -> 发现异常 -> 提出假设 -> 再画图验证。

</div>