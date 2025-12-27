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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 导入 (Introduction)
本页作为模块四的开篇，旨在建立学员对“数据分析”的期待。
**核心要点**:
1. **场景切换**: 明确告知学员，我们从“逻辑编程”转向了“数据处理”。
2. **价值主张**: 强调本模块与教师日常工作（科研、教学管理）的高度相关性。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 问题 (Problem)
通过"电竞教练"的角色扮演，引入数据处理的场景。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 痛点 (Pain Point)
强调手动处理的低效，为引入Pandas做铺垫。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 目标 (Objective)
清晰列出本节课的学习成果。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 导入 (Introduction)
建立宏观框架 (Big Picture)，明确本模块在整个流程中的定位。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 示范 (Demo)
展示最终效果，建立信心。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
使用类比法讲解核心概念。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 知识讲解 (Concept)
简明扼要地介绍环境配置。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
重点讲解读取操作和路径问题。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 避坑 (Pitfalls)
预判新手常见错误，降低挫败感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
介绍常用的数据检查方法。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 扩展 (Extension)
补充CSV知识。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 8分钟
### 环节: 练习 (Practice)
综合练习：读取与检查。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 总结 (Summary)
总结本课，预告下节课。

</div>