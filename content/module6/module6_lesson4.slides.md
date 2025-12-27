---
marp: true
theme: default
paginate: true
size: 16:9
math: katex
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

<!--
(2分钟) 各位老师好！欢迎来到模块六的最后一课，也是我们的**Capstone Project (顶点项目)**。
这次我们要举办一场**“产品孵化营”**。
回想一下，在之前的模块中，我们写了很多有用的脚本：点名器、文件整理助手、数据分析代码。
但它们现在就像躺在抽屉里的零件，只有你懂怎么用，既不方便看也不好分享。
今天，我们要把这些“半成品”拿出来，利用本模块掌握的 Web 技术，给它们穿上现代化的外衣，将它们从**“个人工具 (Script)”** 升级为 **“公共产品 (Product)”**。
-->

---

## **1. 赛道选择：让旧代码重生**

<div class="columns" style="font-size: 0.9em;">
<div>

### **Track A: 智慧教室助手 (Based on Mod 1)**
*   **原型**: **随机点名器** (Module 1).
*   **升级目标**: **扫码互动系统**。
    *   **签到**: 手机扫码自动登记 (防作弊)。
    *   **抢答**: 课件嵌入二维码，学生扫码答题，大屏实时显分。
*   **价值**: 从“被动点名”转变为“主动参与”。

</div>
<div>

### **Track B: 格式转换工厂 (Based on Mod 3)**
*   **原型**: **批量文件整理助手** (Module 3).
*   **升级目标**: **万能文档转换器**。上传 Doc/PPT/PDF，一键转为 **Markdown**。
*   **理由**: Markdown 是 AI (LLM) 最喜欢的格式，为 Module 7 打基础。

### **Track C: 数据视界 (Based on Mod 4/5)**
*   **原型**: **电影市场/旅游市场洞察报告** (Module 4/5).
*   **升级目标**: **交互式 BI 看板**，动态ECharts展示。

</div>
</div>

<!--
(3分钟) 现在，请大家打开自己的代码仓库，进行一次**“代码考古”**。
我们为大家准备了三个升级赛道，请根据兴趣任选其一：
**Track A (互动流)**: 升级你的点名器。把它变成手机扫码的“抢答神器”，不仅能自动评分，还能防止学生代签打卡。
**Track B (工具流)**: 升级文件助手。把它变成一个“万能转换工厂”，特别是把文档转成 Markdown，这是为下个模块的大模型准备的“口粮”。
**Track C (数据流)**: 升级数据报表。把那些静态的 PNG 图片，变成老板最爱的、可以点击交互的 Web 数据看板。
请在 1 分钟内做出选择。
-->

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

<!--
(2分钟) 选择 **Track A** 的老师，你们将打造一款**“教学神器”**。
市面上虽有“学习通”等工具，但功能不好与我们的课件集成，而且容易通过远程代签作弊。
我们今天要开发的，是一个**零依赖、纯本地**的智慧助手。
利用 **局域网 (LAN)** 的特性，我们可以通过校验 IP 来防止代签（因为学生都在同一个教室 WiFi 下）。
更重要的是，这让学生看到了——**老师自己就能开发出如此复杂的互动工具**，这本身就是最好的编程教育。
-->

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

<!--
(2分钟) 选择 **Track B** 的老师，你们是未来的 **“AI 军火商”**。
为什么这么说？因为 AI 大模型无法直接理解 Word 或 PDF 的复杂排版，它最喜欢的是纯净的 Markdown。
你们开发的这个工具，本质上是在构建一条 **ETL 数据流水线**。
它将人类可读的文档，清洗为机器可读的语料。这是未来 Module 7 构建私有知识库的必经之路。
-->

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

<!--
(2分钟) 选择 **Track C** 的老师，你们的挑战是 **“交互 (Interaction)”**。
静态的图片（死图）已经无法满足现代管理者的需求，他们需要的是**数据驾驶舱**。
你们的任务是把 Pandas 算出的数据，通过 API 喂给前端的 **ECharts** 图表库。
这不仅是画图，更是让数据**“活”**起来：支持缩放、筛选、悬停查看。这是商业智能 (BI) 的核心体验。
-->

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

<!--
(2分钟) 在 这次的黑客松热身活动 开始前，我送大家三个 AI 时代的开发锦囊。
第一，**借脑 (PM思维)**：如果不知道该做什么，把模糊的想法扔给 AI，让它帮你拆解需求。
第二，**借力 (技术官思维)**：遇到 `sqlite3`、`ECharts` 这种没学过的库，如果想了解一下这些新知识的话，不要去翻厚厚的文档。让 AI 给你写一个最小可运行的 Demo，然后讲解给你听。
第三，**借眼 (调试者思维)**：报错是最好的老师。直接把红色的错误日志扔给 AI，它比任何专家修得都快。
-->

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

<!--
(15分钟后10分钟) 时间到！Hackathon 结束。
现在是产品发布会环节。请邀请你的同桌作为**第一位用户**，扫码体验你的产品。
在这个环节，请大家哪怕是“鸡蛋里挑骨头”，也要帮对方找出一个 Bug 或体验痛点。
因为在软件工程中，**沉默是最大的伤害，反馈 (Feedback) 才是进化的阶梯**。
-->

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

<!--
(2分钟) 恭喜大家完成了模块六的挑战！
我们让一个个孤立的 Python 脚本，进化到了可以联网互动的 Web 应用。我们的代码不再是冰冷的黑框框，而是有温度、可分享的产品。
但是，现在的应用虽然好用，却还不够“智能”。
下个模块，我们将给这个躯壳装上**“最强大脑”**。
我们将学习如何在本地部署大模型，让你的应用真正拥有 AI 的灵魂。我们模块七见！
-->