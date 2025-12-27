---
marp: true
theme: A4
paginate: true
--- 
<style>
/*--- 布局辅助样式--- */
.columns {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.columns pre code {
  white-space: pre-wrap !important;
  overflow-wrap: break-word !important;
}
/*--- 列表缩进样式修正--- */
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
![bg blur:1px brightness:60%](../../../lectures/images/2025-11-27-11-46-55.png)

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
## 第14节课: 数据筛选与选择——寻找“强势英雄”

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 导入 (Introduction)
承接上节课，引出本节课主题"筛选"。

</div>

---

## **问题导入：寻找“强势英雄”**

<div class="columns">
<div>

作为“电竞教练”，你需要指导学生们选择本赛季的“强势英雄”。选拔标准如下：

1.  **职业要求**: 必须是 **法师 (Mage)**。
2.  **硬指标**: 胜率 (Win Rate) 必须 **大于 52%**。
3.  **信息精简**: 推荐名单上只保留 **英雄 (Hero)** 和 **胜率 (Win Rate)**，其他信息不需要。

**思考**:
如果用Excel筛选，你需要点几下？如果用Python呢？

</div>
<div>

![一个漏斗图，上面是杂乱的英雄头像，下面漏出来的是几位强力法师 width:480px](../../../lectures/images/2025-11-27-11-56-35.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 问题 (Problem)
设定具体的筛选场景，激发解决问题的欲望。

</div>

---

## **本课学习目标**

<div class="columns">
<div>

学完这节课，你将能够：

1.  **理解** “按行筛选” (Filter Rows) 和 “按列选择” (Select Columns) 的区别。
2.  **掌握** 使用简单条件（如 `> 0.52`）进行筛选。
3.  **掌握** 使用组合条件（如 `AND`, `OR`）进行复杂筛选。
4.  **掌握** 将筛选结果导出为新的Excel文件。

</div>
<div>

![配图占位符 width:480px](../../../lectures/images/2025-11-27-11-59-49.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 目标 (Objective)
明确学习成果。

</div>

---

## **示范效果：一键生成推荐榜单**

<div class="columns ratio-6-4">
<div>

**输入指令**
> "请帮我生成Python代码，筛选出所有 胜率 > 0.52 的 法师，只保留 英雄 和 胜率 两列，并保存为 'top_mages.xlsx'。"

**AI 生成的核心代码**
```python
# 筛选 + 选择
df[
    (df['职业'] == '法师') & 
    (df['胜率'] > 0.52)
][['英雄', '胜率']]
```
*(注：看不懂代码没关系，具体语法稍后会详细拆解)*
</div>
<div>

![width:300px](../../../lectures/images/2025-11-27-12-03-31.png)

**输出结果 (top_mages.xlsx)**
| 英雄 | 胜率 |
| :--- | :--- |
| 武则天 | 0.541 |
| ... | ... |

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 示范 (Demo)
展示自然语言交互的强大效率。

</div>

---

## **按行筛选 (Filter Rows)**

筛选，就像是用一个**筛子**，把符合条件的行留下来。

<div class="columns">
<div>

### **简单条件**
> "请帮我生成Python代码，筛选出 胜率 > 0.52 的数据。"

```python
# df['列名'] > 值
top_heroes = df[df['胜率'] > 0.52]
```

<div class="tip" style="font-size:0.6em">

💡 **语法拆解**:
1. **里层** `df['胜率'] > 0.52`: 生成一张“True/False”的判断表。
2. **外层** `df[...]`: 根据这张表，把为 True 的行挑出来。
</div>

</div>
<div>

### **组合条件 (逻辑)**
> "请帮我生成Python代码，筛选出 职业是法师 **并且** 胜率 > 0.52 的数据。"

```python
# & 表示“并且” (AND)
# | 表示“或者” (OR)
target = df[
    (df['职业'] == '法师') & 
    (df['胜率'] > 0.52)
]
```

</div>
</div>

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
讲解行筛选的核心语法：布尔索引。
**重点**:
1. 形象比喻：筛子。
2. 语法拆解：内层判断 vs 外层选择。
3. 逻辑运算：`&` (AND) 和 `|` (OR) 的用法及括号的重要性。

</div>

---

## **深度解析：判定表 (Decision Table)**

<div class="columns" style="font-size: 0.77em">
<div>

### **什么是判定表？**
它是结构化程序设计中，用来清晰描述**复杂逻辑条件**的工具。
在Pandas筛选中，每一行数据都要经过这张表的“面试”。

### **筛选逻辑图解**
| 英雄 | 职业==法师? | 胜率>0.52? | **结果 (Mask)** |
| :--- | :---: | :---: | :---: |
| 妲己 | ✅ True | ❌ False | **False** (淘汰) |
| 鲁班 | ❌ False | ❌ False | **False** (淘汰) |
| 武则天 | ✅ True | ✅ True | **True** (保留) |

</div>
<div>

### **Pandas 的执行过程**

1.  **生成判定表 (Mask)**:
    `mask = (df['职业']=='法师') & (df['胜率']>0.52)`
    这行代码本质上就是生成了左边那列 **结果 (Mask)**。

2.  **执行筛选**:
    `df[mask]`
    Pandas 拿着这张“录取名单”，只把标记为 **True** 的行挑出来。

<div class="insight" style="font-size:0.6em">

💡 **核心思维**:
写筛选代码，本质上就是设计这张**判定表**。
你只需要定义好“录取标准”（条件），Pandas 会自动完成成千上万次“面试”。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 深度解析 (Deep Dive)
### 目的:
利用“判定表”这一经典结构化设计工具，可视化布尔索引的内部逻辑，帮助学员建立清晰的逻辑模型。

</div>

---

## **Prompt技巧与实验**

<div class="columns">
<div>

### **💡 Prompt技巧**
对于复杂条件，用自然语言把逻辑说清楚最重要。
比如：“**筛选出 职业 是'法师' 并且 胜率 大于 0.52 的数据**”。

### **🔍 交互实验**
<div class="insight" style="font-size:0.6em">

请继续在上节课已经运行的Python交互模式中尝试输入：
`df[df['胜率'] > 0.52]`
看看输出了什么？是不是只有胜率高的英雄？
</div>

</div>
<div>

![](../../../lectures/images/2025-11-27-12-12-01.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
讲解行筛选的逻辑。

</div>

---

## **避坑指南：逻辑运算的“陷阱”**

<div class="columns" style="font-size:0.8em">
<div>

### **❌ 常见错误**
1.  **混用符号**: 在组合条件时要用 `&`/`|`，不能用 `and`/`or`。
2.  **忘记括号**: 组合条件时，**每个条件必须加括号**！

```python
# 错误写法 ❌
df[df['职业'] == '法师' and df['胜率'] > 0.5]
df[df['职业'] == '法师' & df['胜率'] > 0.5] 
```

<div class="tip" style="font-size:0.65em">

💡 **为什么要用 `&` 而不是 `and`？**
简单来说：`and` 只能判断两个"整体"的真假，而 `&` 可以对表格的"每一行"分别判断。Pandas 筛选需要后者。

**记住口诀**：筛选数据用 `&`，加上括号不会错！

</div>

</div>
<div>

### **✅ 正确写法**

```python
# 正确写法 (注意括号和符号)
df[
    (df['职业'] == '法师') & 
    (df['胜率'] > 0.5)
]
```

<div class="tip" style="font-size:0.65em">

💡 **AI 提示**:
如果你记不住这些规则，直接告诉AI：“**帮我筛选...**”，它会自动写出正确的符号和括号。出于学习目的，可以进一步向AI请教这些规则的含义。

</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 避坑 (Pitfalls)
强调Pandas特殊的逻辑运算符规则。

</div>

---

## **按列选择 (Select Columns)**

有时候表格太宽了（比如还有出场率、Ban率、金币...），我们只想看关键信息。

<div class="columns" style="font-size:0.6em">
<div class="styled-div" style="font-size:0.9em">

### **指令**
> "请帮我生成Python代码，只保留 **英雄** 和 **胜率** 这两列。"

### **AI生成的代码**
```python
# 双重中括号 [[...]]
subset = df[['英雄', '胜率']]
```

<div class="tip" style="font-size:0.8em">

💡 **为什么是双重中括号 `[[...]]`？**
- **外层 `[]`**: 告诉 Pandas "我要选列"
- **内层 `['英雄', '胜率']`**: 这是一个**列表**，装着你要的列名

**类比**：就像去超市，外层是购物篮，内层是购物清单。

</div>

</div>
<div>

### **效果对比**

**原表**:
| 英雄 | 职业 | 胜率 | Ban率 | ... |
| :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... |

**选择后**:
| 英雄 | 胜率 |
| :--- | :--- |
| ... | ... |

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 知识讲解 (Concept)
讲解列选择。

</div>

---

## **数据排序 (Sort)**
 
 筛选出英雄后，我们想知道：**谁的胜率最高？** 这就需要排序。
 
 <div class="columns">
 <div>
 
 ### **指令**
 > "请帮我生成Python代码，按 **胜率** 从高到低排序。"
 
 ### **AI生成的代码**
 ```python
 # sort_values: 排序
 # ascending=False: 降序 (从大到小)
 sorted_df = df.sort_values(
     by='胜率', 
     ascending=False
 )
 ```
 
 </div>
 <div>

<div class="insight" style="font-size:0.6em">
 
 🔍 **交互实验**:
 尝试输入 `df.sort_values(by='胜率', ascending=False).head()`。
 看看排在第一名的是谁？是不是武则天？
 </div>

<div class="tip" style="font-size:0.6em">
 
 💡 **小技巧**:
 默认是 `ascending=True` (升序，从小到大)。
 如果要找“倒数第一”，就不用加 `ascending=False`。
 
</div>
 
</div>
</div>
 

 
 
 <div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 知识讲解 (Concept)
新增排序知识点，完善数据分析链路。

</div>

 
---
 
 ## **保存成果 (Export)**

筛选出了结果，我们需要把它保存下来。

<div class="columns">
<div>

### **指令**
> "请帮我生成Python代码，把结果保存为 'top_mages.xlsx'。"

### **AI生成的代码**
```python
# to_excel 是 read_excel 的反向操作
# index=False 表示不保存行号(0, 1, 2...)
subset.to_excel('top_mages.xlsx', index=False)
```

</div>
<div>

<div class="insight" style="font-size:0.6em">

🔍 **交互实验**:
尝试输入 `subset.to_excel('test.xlsx')`。
然后去文件夹看看，是不是多了一个文件？
</div>

<div class="tip" style="font-size:0.6em">

💡 **小技巧**: `index=False`
通常我们不需要Pandas自动生成的那个 0, 1, 2 的索引列。告诉AI“**不要保存索引**”，可以让生成的Excel表格更干净。
</div>

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 知识讲解 (Concept)
讲解导出操作。

</div>

---

---

## **动手练习：筛选金牌英雄**

<div class="columns styled-div" style="font-size:0.55em">
<div>

**任务**：
1.  **筛选**: 找出 **职业** 为 "法师" **且** **胜率** > 0.52 的英雄。
2.  **排序**: 按 **胜率** 从高到低排序。
3.  **选择**: 只保留 `英雄` 和 `胜率` 两列。
4.  **导出**: 保存为 `top_mages.xlsx` (不带索引)。
5.  **验证**: 打开Excel检查。

</div>
<div>

**请向AI发送以下指令**：

> 请帮我生成Python代码，完成以下任务：
> 1. 筛选出 `职业` 是 '法师' 且 `胜率` > 0.52 的数据。
> 2. 按 `胜率` 降序排列。
> 3. 只保留 `英雄` 和 `胜率` 两列。
> 4. 将结果保存为 `top_mages.xlsx`，不要保存索引。

**预期结果**:
文件夹中生成了 `top_mages.xlsx`，打开后只有两列数据，且第一行是胜率最高的英雄。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 8分钟
### 环节: 练习 (Practice)
综合练习：筛选、排序与导出。

</div>

---

## **课程小结**

<div class="columns">
<div>

### **我们学到了什么？**
1.  **按行筛选**: 用条件（如 `胜率 > 0.52`）挑出记录。
2.  **数据排序**: 用 `sort_values` 找第一名。
3.  **按列筛选**: 用列名列表（如 `['英雄', '胜率']`）挑出特征。
4.  **保存**: 用 `to_excel()` 把成果存盘。

</div>
<div>

### **下节课预告**
游戏的数据是完美的，但现实世界的数据往往是“脏”的。
- 问卷里有人漏填了？
- 数据里有重复提交？

下节课：**数据清洗**。
我们将化身为**严谨的影评人**，面对一份“充满瑕疵”的**电影榜单数据**，学习如何做数据的“保洁员”。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 总结 (Summary)
总结本课，预告下节课。

</div>