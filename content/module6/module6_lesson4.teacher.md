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
  padding: 15px;
}
.insight {
  background-color: #eefcff; 
  border-left: 5px solid #17a2b8; 
  padding: 15px; 
}
.key-point {
  background-color: #fffbe6; 
  border-left: 5px solid #ffc107; 
  padding: 15px; 
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
.styled-div h3 {
  font-size: 1.2em; 
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
![bg blur:2px brightness:60%](../../../lectures/images/2025-12-13-17-30-42.png)

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

# 模块六: Python+Web开发入门
## 第24节课: 综合工作坊——打造你的 Web 应用作品集

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 导入 (Introduction)
**核心目标**: **价值重构 (Reframing)**。
将枯燥的“综合练习”重构为激动人心的“产品孵化”。引导学员意识到，他们今天不是在写作业，而是在打造自己的**作品集 (Portfolio)**。

</div>

---

## **1. 赛道选择：让旧代码重生**

<div class="columns" style="font-size: 0.9em;">
<div class="styled-div" style="font-size: 0.7em;">

### **Track A: 智慧教室助手 (Based on Mod 1)**
*   **原型**: **随机点名器** (Module 1).
*   **升级目标**: **扫码互动系统**。
    *   **签到**: 手机扫码自动登记 (防作弊)。
    *   **抢答**: 课件嵌入二维码，学生扫码答题，大屏实时显分。
*   **价值**: 从“被动点名”转变为“主动参与”。

</div>
<div class="styled-div" style="font-size: 0.7em;">

### **Track B: 格式转换工厂 (Based on Mod 3)**
*   **原型**: **批量文件整理助手** (Module 3).
*   **升级目标**: **万能文档转换器**。上传 Doc/PPT/PDF，一键转为 **Markdown**。
*   **理由**: Markdown 是 AI (LLM) 最喜欢的格式，为 Module 7 打基础。

### **Track C: 数据视界 (Based on Mod 4/5)**
*   **原型**: **电影市场/旅游市场洞察报告** (Module 4/5).
*   **升级目标**: **交互式 BI 看板**，动态ECharts展示。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 分组 (Grouping)
**教学策略**: **差异化教学 (Differentiated Instruction)**。
- Track A: 侧重 **并发与风控 (Concurrency & Control)**。
- Track B: 侧重 **I/O 流水线 (Data Pipeline)**。
- Track C: 侧重 **前端可视化 (Visualization)**。
给予学员自主选择权，能最大程度激发**内驱力**。

</div>

---

## **2.1 Track A: 智慧教室助手 (需求发布)**

<div class="columns">
<div>

### **你的客户 (一线教师) 说：**
> "现在的课堂太沉闷了，学生都在低头看手机。
> 我想用**魔法**打败魔法：
> 1.  我在课件封面放个**二维码**，他们必须扫码才能签到。
> 2.  讲完一个知识点，立马出个题，他们扫码抢答。
> 3.  系统**自动评分**，马上告诉我谁答对了，谁是第一名。"

</div>
<div>

### **作为开发者，你需要...**
*   **交互**: 课件嵌入动态二维码 (`/qrcode`).
*   **风控**: **IP 访问限制** (局域网内，不到场无法参与，且一个 IP 只能提交一次)。
*   **反馈**: 实时更新的排行榜 (Leaderboard)。
*   **部署**: **本地运行**，数据不出教室，绝对安全。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 需求洞察 (Insight)
**赋能感**: 强调工具的**自主可控性**。
**技术价值**: 引入“局域网安全”和“并发控制”的概念。

</div>

---

## **2.2 Track B: 在线效率工具箱 (需求发布)**

<div class="columns">
<div>

### **你的客户 (教务处) 说：**
> "我们有几百个 Word 格式的教案，想喂给 AI 做质量分析。
> 但 AI 读 Word 总是格式乱套，听说 **Markdown** 才是 AI 的母语。
> 我想要一个网页工具：
> 1.  把我们的 docx/pptx/pdf 拖进去。
> 2.  自动转换成整洁的 Markdown 文本。
> 3.  **打包下载**，方便我们后续生成题库或报告。"

</div>
<div>

### **作为开发者，你需要...**
*   **核心库**: `python-docx` (读文档), `PyPDF2` (读PDF), `markitdown` (微软开源库) 或 `markdownify`。
*   **流程**: 上传 -> 识别格式 -> 调用转换各种库 -> 拼接 Markdown -> 返回文件。
*   **价值**: 这是非结构化数据 (Doc) 走向 AI (Data) 的必经之路。

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 任务发布 (Task Definition)
**前瞻性设计**: 明确指出该任务的战略价值——为下一模块（大模型应用）做**数据准备**。
让学员意识到自己不仅仅是在写转换器，而是在为 AI 时代修路。

</div>

---

## **2.3 Track C: BI 数据驾驶舱 (需求发布)**

<div class="columns">
<div>

### **你的客户 (老板) 说：**
> "你发给我的 PNG 图片我也不能点，太死板了。
> 我看隔壁公司的**大屏**都是动态的：
> 1.  鼠标放上去能显示具体数字。
> 2.  可以筛选'只看这个月'的数据。

> 请把你之前的 Pandas 分析结果，放到网页上去！"

</div>
<div>

### **作为开发者，你需要...**
*   **技术栈**: Pandas (后端算) + **ECharts** (前端画)。
*   **API**: `GET /chart_data` 返回 JSON 格式的数据（即 ECharts 的 `option` 配置项）。
*   **挑战**: 如何把 DataFrame 转换成 ECharts 需要的 JSON 格式？(问 AI)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 任务发布 (Task Definition)
**脚手架 (Scaffolding)**: 针对 ECharts 配置极其复杂的痛点，明确给出解决策略——**利用 AI 生成配置 JSON**。
这是 "AI-Assisted Coding" 的最佳应用场景之一。

</div>

---

## **3. 锦囊：AI 时代的开发技巧**

<div class="columns" style="font-size: 0.85em;">
<div>

### **1. 需求模糊怎么办？**
*   不要自己猜。
*   **Prompt**: "作为产品经理，请根据客户的这段话（...），整理出详细的功能列表和 API 接口定义。"

### **2. 这里有新知识点！**
*   **Track A**: 怕学生作弊？Prompt: "如何在 FastAPI 中获取客户端 IP，并实现每个 IP 每道题只能提交一次..."
*   **Track B**: 怎么转 Markdown？Prompt: "用 Python 将 docx 内容读取并转换为 markdown 格式..."
*   **Track C**: ECharts？Prompt: "如何在 HTML 中引入 ECharts 并渲染柱状图..."

</div>
<div>

### **3. 遇到报错**
*   **不要慌**。
*   直接把报错信息扔给 AI。
*   Prompt: "我遇到了这个错误 [Error Log]，这是我的代码 [Code]，请分析原因并修复。"

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 方法论指导 (Methodology)
**元认知策略**: 讲授解决问题的“元方法”。
这里的重点不是教某个具体的库，而是教 **"How to learn"** 和 **"How to debug"** with AI。这是终身受用的技能。

</div>

---

## **4. 成果展示 (Showcase)**

<div class="columns">
<div>

### **交付标准**
1.  **Web 化**: 必须有网页界面，支持局域网访问。
2.  **可用性**: 核心功能跑通 (记录/整理/画图)。
3.  **用户价值**: 解决了我在“脚本时代”解决不了的问题 (如数据持久化、易用性、交互性)。

### **互评环节**
*   请同桌扫一扫你的二维码 (局域网访问)，或者直接操作你的电脑。
*   **Find a Bug**: 找出一个体验不好的地方。

</div>
<div>

![配图：展览会现场，各种屏幕展示着不同的应用，观众在参观](../../../lectures/images/2025-12-13-18-06-02.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 15分钟后10分钟
### 环节: 同伴互评 (Peer Assessment)
**社会化学习**: 通过“找茬”游戏，让学员在互评中学习他人的优点，同时反思自己的不足。
**真实感**: 模拟真实的用户验收测试 (UAT) 场景，建立“为了用户而开发”的意识。

</div>

---

## **模块六总结：从点到面**

<div class="columns">
<div>

### **能力跃迁**
*   **Module 1-5**: 只有你自己能用的**工具 (Tools)**。
*   **Module 6**: 连接世界的**产品 (Product)**。
这不仅是技术的提升，更是**个人价值**的放大。

### **下个篇章：模块七**
现在的应用虽然能跑，但还不够“聪明”。
下个模块，我们将挑战：
**在本地部署大模型，并把它接入你的 Web 应用！**

</div>
<div>

![配图：Module 6是最后一块拼好的边框，中间空缺着Module 7的核心大脑](../../../lectures/images/2025-12-13-18-05-12.png)

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 模块总结 (Module Summary)
**知识图谱**: 明确本模块在整个课程体系中的位置——**连接层 (Connectivity)**。它连接了底层的 Python 逻辑和未来的 AI 大脑。
**预告**: 抛出“智能化”的愿景，维持学员的学习热情。

</div>