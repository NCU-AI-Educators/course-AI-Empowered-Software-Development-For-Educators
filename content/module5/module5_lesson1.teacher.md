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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 导入 (Introduction)
**模块衔接**: 从“数据处理”平滑过渡到“数据展示”。
**价值主张**: 强调可视化对于“观点表达”和“辅助决策”的重要性。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 痛点 (Pain Point)
通过“3秒挑战”，让学员切身体会表格数据的局限性，从而产生对可视化的强烈需求。

</div>

---

## **愿景：从表格到“数据驾驶舱”**

<div class="align-top-center">

![数据驾驶舱示意图：深色背景，中央是中国地图热力图，四周环绕各种统计图表 width:800px](../../../lectures/images/2025-12-06-02-52-14.png)

</div>

<div class="insight" style="font-size:0.8em">

🌟 **目标**: 这就是我们作为“AI数据分析师”的终极形态 —— 将冰冷的数据，变成辅助决策的**智慧大脑**。
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 愿景 (Vision)
展示最终的高级形态（Dashboard），为枯燥的基础学习提供动力。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 对比 (Contrast)
通过Before/After的直接对比，强化可视化的价值。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 支架 (Scaffolding)
通过简单的环境搭建，降低学员的畏难情绪。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 常见错误 (Common Errors)
提前解决技术障碍，避免学员在实操时因乱码产生挫败感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 任务 (Task)
从简单任务入手，建立信心。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 代码解读 (Walkthrough)
重点解释 `kind` 和 `head()`，让学员理解代码与图表的对应关系。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 结果解读 (Interpretation)
引导学员学会“看图说话”，从简单的排名中提取有价值的业务信息（如地域分布规律）。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 进阶任务 (Advanced Task)
引入 `groupby`，这是数据分析中最重要的概念之一。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 视觉优化 (Visual Optimization)
教授横向柱状图的适用场景（长标签），培养学员对阅读体验的关注。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 结果验证 (Verification)
通过分析高价城市的分布规律，让学员理解数据背后的地理与经济逻辑。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 练习 (Practice)
发布练习任务，引导学员独立思考 AI 指令。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 代码解读 (Walkthrough)
讲解饼图特有的参数设置（如百分比显示）。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 结果解读 (Interpretation)
通过饼图直观展示“金字塔结构”，强化稀缺性概念。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 总结 (Summary)
回顾知识点，并抛出下节课的悬念，保持学员兴趣。

</div>