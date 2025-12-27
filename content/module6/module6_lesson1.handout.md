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
![bg blur:1px brightness:60%](../../../lectures/images/2025-12-13-11-49-16.png)

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
## 第21节课: Web应用架构——从 Web API 开始

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要学 Web 开发？
以前我们写的代码叫“脚本”，就像是在自己家做饭，想吃什么得自己动手，别人想吃还得来你家厨房。
现在我们要做的叫“Web 应用”，就像是**开了一家外卖店**。
- **顾客 (用户)** 不需要进厨房，只需要在手机上点单 (浏览器访问)。
- **后厨 (服务器)** 负责把菜做好送出去。
这种模式最大的好处就是：**用户不需要安装任何东西**，只要有浏览器就能用你的工具。

</div>

---

## **1. 课程回顾：从个人工具到孤岛困境**

<div class="columns" style="font-size: 0.9em;">
<div class="styled-div" style="font-size: 0.6em;">

### **前五个模块虽然强大...**
*   **Module 1**: 指挥 AI 生成了酷炫的网页（但没有后台逻辑）。
*   **Module 2/3**: 掌握了 Python 基础，甚至有高手用 `pygame` 做了 MUD 游戏界面。
*   **Module 4/5**: 学会了数据分析，做出了专业的全景数据报告。

### **痛点：孤岛效应**
*   **只能自己用**: 你的程序离不开这台电脑。
*   **分享难**: 别人想用，得先装 Python。
*   **交互弱**: 命令行界面 (CLI) 对普通人不友好。

</div>
<div class="align-middle-center">

![配图：一个人守着电脑孤独编程，旁边的人想看却看不了](../../../lectures/images/2025-12-13-11-53-25.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### “在我的电脑上能跑” (It works on my machine)
这是程序员最常说的一句“借口”。
因为每个人的电脑环境（Windows/Mac、Python版本、安装的库）都不一样，所以代码发给别人经常跑不起来。
Web 应用彻底解决了这个问题：计算都在**服务器**上完成，用户只需要一个显示器（浏览器）。这大大降低了软件的推广门槛。

</div>

---

## **2. 进阶之路：Web 化解决方案**

<div class="columns">
<div>

### **Module 6 的解法：Web 化**

<br>
<div style="text-align: center; margin: 20px 0;">

把 Python 的**逻辑** (模块 2-5) 
装进 
Web 的**外壳** (模块 1) 
= **Web 应用**

</div>
<br>

*   **随时访问**: 有浏览器就能用。
*   **美观**: 和现代 App 一样的体验。
*   **协作**: 把你的工具变成云端服务。

</div>
<div class="align-middle-center">

![配图：左边是各种Python脚本图标，右边是浏览器里的App图标，中间有一个箭头](../../../lectures/images/2025-12-13-11-57-07.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 网站 vs Web 应用
- **网站 (Web Site)**: 像**报纸**。主要是给你“看”的，比如学校官网、新闻网。内容一般不变。
- **Web 应用 (Web App)**: 像**工具**。主要是给你“用”的，比如 12306 买票、在线修图、Google 文档。它会根据你的操作进行计算。
我们这节课要做的，就是后者——能干活的网页工具。

</div>

---

## **3. 本课学习目标**

<div class="columns">
<div>

1.  **架构认知**: 理解 **现代Web应用架构**，知道浏览器和服务器是怎么配合的。
2.  **后端入门**: 使用 **FastAPI** 编写你的第一个 API 接口。
3.  **服务思维**: 从“写代码给机器跑”转变为“写服务给人用”。

</div>
<div class="align-middle-center">

![配图：从单机脚本到Web服务的对比图](../../../lectures/images/2025-12-13-13-12-12.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 请求与响应 (Request & Response)
这是互联网世界最基本的对话方式，就像**一问一答**。
- **Request (问)**: 浏览器说“我要看菜单”。
- **Response (答)**: 服务器说“这是菜单...”。
不管多复杂的网站，哪怕是双十一秒杀，本质上也是由无数个这样的“一问一答”组成的。

</div>

---

## **4. 本课任务：专注于后端 (The Backend)**

<div class="columns ratio-6-4">
<div>

### **为什么从后端开始？**
*   **灵魂**: 没有 高级功能的支持（后端），界面（前端）只能是个小工具。
*   **服务化**: 一旦后端写好，它可以同时服务网页、手机、甚至微信机器人。

### **核心产出**
我们今天要实现 **API 服务**：
1.  **提供服务**: 告诉外界“我能做什么” (菜单)。
2.  **接收指令**: 听懂外界的“请求” (点单)。
3.  **返回结果**: 把 服务 的结果送回去 (上菜)。

</div>
<div class="align-middle-center">

![配图：聚焦在Backend部分的架构图，高亮显示API层 width:550px](../../../lectures/images/2025-12-13-13-17-51.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### API (应用程序接口)
别被这个缩写吓到。把它想象成银行的**业务窗口**。
- 你不需要知道柜员身后的金库怎么开，也不需要知道他们怎么记账。
- 你只需要在窗口递进去一张身份证（**输入**），说“我要取钱”。
- 柜员就会把钱递给你（**输出**）。
这个窗口，就是 API。它让外部人员（用户）可以安全、方便地使用内部资源（核心代码）。

</div>

---

## **5. 全局视野：互联网应用是如何运作的？**

<div class="columns" style="font-size: 0.9em;">
<div class="styled-div" style="font-size: 0.6em;">

### **问题域：我想做什么？**
*   **目标**: 做一个“学科知识机器人”。
*   **用户**: 学生（通过网页/手机）。
*   **核心**: 你的 Python 知识库代码 (Module 7)。

### **求解域：怎么做？(架构设计)**
主流方案：**前后端分离架构**。
*   **前端 (Frontend)**: 负责**好不好看**。
    *   网页、App、小程序。
*   **后端 (Backend)**: 负责**能不能用**。
    *   AI 推理、数据处理、业务逻辑。
*   **API**: 连接两者的桥梁。

</div>
<div class="align-middle-center">

![配图：以学科知识机器人为例的前后端分离架构图，左边是手机/电脑，右边是服务器，中间是API](../../../lectures/images/2025-12-13-13-24-09.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要“前后端分离”？
想象一下装修房子。
- **硬装 (后端)**: 就像水电管线、承重墙。这部分要稳固，轻易不改动。
- **软装 (前端)**: 就像壁纸、窗帘、家具。这部分要漂亮，经常换风格。
把它们分开，你就可以在不砸墙（不改后端代码）的情况下，随意换窗帘（改网页界面）。这就是“分离”的好处：**各司其职，互不干扰**。

</div>

---

## **5.1 解构交互：餐厅隐喻 (The Metaphor)**

<div class="columns" style="font-size: 0.9em;">
<div>

### **如何实现“对话”？**
顾客（前端）和后厨（后端）互不相见，怎么配合？

### **角色映射**
1.  **顾客 (Client/Frontend)**: 负责提要求 (点餐)。
    *   *浏览器、手机App*
2.  **后厨 (Server/Backend)**: 负责干活 (做菜)。
    *   *你的 Python 代码*
3.  **菜单 (API)**: 唯一的沟通标准。
    *   *URL 接口列表*
4.  **服务员 (HTTP 协议)**: 负责跑腿传话。

</div>
<div class="align-middle-center">

![配图：生动的餐厅场景插画，标注Client, Server, API](../../../lectures/images/2025-12-13-13-28-18.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 教学隐喻的作用
对于“客户端/服务器架构”这种抽象概念，新手很难直接建立心智模型。
“餐厅隐喻”完美对应了各个部分：
- **服务器**: 提供资源（做菜）。
- **客户端**: 发起请求（点菜）。
- **协议**: 沟通规则（服务员听得懂的语言）。
这个比喻我们会在后面反复使用。

</div>

---

## **5.2 互联网应用的架构图**

<div class="columns ratio 6-4" style="font-size: 0.73em;">
<div class="styled-div" style="font-size: 0.8em;">

### **为什么需要架构图？**
在向他人（或学生）解释技术原理时，一张清晰的架构图比一千句话更有效。
**AI 也是画图高手**。我们不需要自己画，只需要**描述**。

### **AI 绘图提示词 (Prompt)**
> 主题：客户端-服务器架构图（AI 生成风格）。
描述：左侧是一台带有浏览器窗口的笔记本电脑，标有“客户端”。右侧是一个风格化的服务器机架或云图标，标有“服务器”。两支箭头连接着它们：上面的箭头指向右侧，标有“请求”；下面的箭头指向左侧，标有“响应”。
风格：科技教育风格，柔和的蓝色和友好的配色，白色背景，高质量矢量图。

</div>
<div class="align-middle-center">

![配图：在此处插入我们将要生成的架构图](../../../lectures/images/2025-12-13-13-32-16.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 知识可视化
作为老师，我们不仅要学会写代码，还要学会**教代码**。
利用 AI 将抽象的思维模型（如架构图）转化为直观的视觉图表，是培养**工程表达能力**的关键环节。

</div>

---

## **5.3 深入餐厅运作：HTTP 协议**

<div class="columns ratio 6-4" style="font-size: 0.86em;">
<div>

### 服务员的“行话”
你的浏览器和服务端之间的对话，必须遵守规则。
1.  **GET (看菜单)**: 我想要获取信息。
    *   `GET /menu`
2.  **POST (下单)**: 我要提交数据（给后厨）。
    *   `POST /order`

### 状态码 (厨房的反馈)
*   **200 OK**: 菜做好了 (成功)。
*   **404 Not Found**: 没这道菜 (端点不存在/网址错了)。
*   **500 Server Error**: 厨师炸厨房了 (代码报错)。

</div>
<div class="align-middle-center">

![配图：服务员拿着不同颜色的牌子(200绿, 404黄, 500红)示意图](../../../lectures/images/2025-12-13-13-37-17.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是协议 (Protocol)？
协议就是**沟通的规矩**。
就像打电话：
- 我说“喂”，你知道要回答“你好”。
- 我说“再见”，你知道要挂电话。
**HTTP 协议**就是浏览器和服务器之间的通话规矩。
- **GET**: 意思是“给我看看”。
- **POST**: 意思是“请帮我处理这个”。

</div>

---

## **6. 搭建后厨：认识 FastAPI**

<div class="columns ratio-6-4" style="font-size: 0.95em;">
<div>

### **Why FastAPI?**
*   **快 (Fast)**: 运行速度极快（基于 Starlette）。
*   **易 (Easy)**: 代码简洁，像写普通 Python 函数一样。
*   **现代 (Modern)**: 自动生成交互式文档 (Swagger UI)。

### **安装**
```bash
pip install fastapi uvicorn
```
*   `fastapi`: 它是主厨，负责炒菜。
*   `uvicorn`: 它是餐厅经理，负责开门迎客（运行服务器）。

</div>
<div class="align-middle-center">

![配图：FastAPI的Logo和一个飞快的火箭](../../../lectures/images/2025-12-13-13-40-11.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么选 FastAPI？
在 Python 世界里，有很多做 Web 的工具（比如 Django, Flask）。
FastAPI 是最新的、最快的，也是目前**最适合与 AI 结合**的。
它最大的优点是：**你只需要写 Python 函数，它自动帮你变成网页接口。**
这大大降低了我们的学习成本。

</div>

---

## **6.1 从 "Hello World" 开始**

<div class="columns">
<div>

### **策略：角色扮演**
*   **角色**: 赋予 AI **"后端开发专家"** 的身份。
*   **痛点**: 我们不想写原本的 Python 代码。
*   **目标**: 明确**输入** (访问首页) 和 **输出** (Hello World)。
*   **约束**: 指定端口 `8000` 和 `0.0.0.0` (允许局域网)。

</div>
<div>

### **Prompt (Copy & Paste)**
> "**你是一位 Python 后端开发专家。**
> 我需要创建一个极简的 Web 服务 (API)。
> **需求**：
> 1. 用户访问主页 (`/`) 时，返回一条欢迎信息 `Hello, World!`。
> 2. 服务要在本地 8000 端口运行，允许局域网访问。
> 请使用最流行的 **FastAPI** 框架实现，并给出运行命令。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 角色扮演 Prompt
这是一个让 AI 写出好代码的技巧。
当你告诉 AI “你是一位专家”时，它会不仅仅给你代码，还会给你**最规范的写法**。
这就像你请教问题时，问小学生和问大学教授，得到的答案质量是完全不同的。

</div>

---

## **6.2 代码解析：AI 到底写了什么？**

<div class="columns">
<div>

### **AI 生成的代码**
```python
from fastapi import FastAPI
import uvicorn

# 1. 开店执照
app = FastAPI()

# 2. 迎宾牌 (路由)
@app.get("/")
def root():
    # 以 JSON 格式返回结果
    return {"message": "Hello, World!"}

# 3. 开门营业
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

</div>
<div>

### **分析 (Analysis)**
*   **`@app.get("/")`**: 这叫**装饰器**。不用懂原理，只要知道它把 **URL** 和 **函数** 绑在了一起。
*   **`host="0.0.0.0"`**: **关键点！** 这意味着“敞开大门”，允许你的手机访问电脑。如果是 `127.0.0.1`，就只能在你的电脑上使用了。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 装饰器 (Decorator)
代码里那个 `@` 符号。
不用去管复杂的定义。你可以把它想象成**便利贴**或**标签**。
- `def root()` 是一个普通的 Python 函数。
- 加上 `@app.get("/")`，就是给这个函数贴了个标签：“如果你访问首页 (/)，就会运行我。”
这就是 FastAPI 的魔法：用标签把网址和代码连起来。

</div>

---

## **6.3 关键概念：路由与端点 (Route & Endpoint)**

<div class="columns ratio-6-4" style="font-size: 0.95em;">
<div>

### **路由 (Route)**
*   **什么是路由？**: 就像酒店的**门牌号**。
*   **代码对应**: `@app.get("/...")` 里的那个字符串。
    *   `/` 是前台。
    *   `/menu` 是菜单墙。
    *   `/order` 是点餐台。

### **端点 (Endpoint)**
*   **什么是端点？**: 门牌号后面对应的**房间**（即处理函数）。
*   **代码对应**: `def root():` 下面的那段代码。

</div>
<div class="align-middle-center">

![配图：一个酒店走廊，门上挂着不同的牌子(/menu, /order)，门后是不同的房间](../../../lectures/images/2025-12-13-13-43-42.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 路由 (Routing)
简单说就是**指路牌**。
- 顾客问：“我想看菜单，走哪边？”
- 路由说：“往 `/menu` 走。”
FastAPI 的工作就是当这个指路人，把顾客带到正确的房间（函数）里去。

</div>

---

## **6.4 核心概念：什么是 JSON？**

<div class="columns">
<div>

### **它是谁？**
*   **全称**: JavaScript Object Notation.
*   **地位**: 互联网世界的 **"通用语"**。
*   **作用**: 让 Python (后端) 和 浏览器 (前端) 能听懂彼此说话。

</div>
<div>

### **秒懂指南 (Cheat Sheet)**
你不需要专门学 JSON，因为：
1.  还记得 **Python 字典** 吗？ `{"key": "value"}`
2.  **JSON 长得和 Python 字典几乎一模一样！**

**结论**: 只要你在 Python 里返回一个字典，FastAPI 会自动把它翻译成 JSON 发给顾客。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### JSON：机器人的世界语
互联网上有各种各样的语言：Python, Java, JavaScript...
它们之间怎么交流？就需要一种大家都能看懂的格式，这就是 **JSON**。
它非常简单，就是一堆“键值对”（Key-Value），长得非常像 Python 的字典。
所以，你不需要额外学新语法，会写字典就会写 JSON。

</div>

---

## **7. 顾客进店：浏览器访问**

<div class="columns ratio-6-4" style="font-size: 0.7em;">
<div class="styled-div" style="font-size: 0.8em;">

### **启动服务器**
在 VS Code 终端运行代码。你会看到：
`Uvicorn running on http://0.0.0.0:8000`

### **访问**
打开浏览器 (Chrome)，输入地址：
`http://127.0.0.1:8000`

### **特别说明：浏览器的角色**
*   **浏览器 = 通用客户端 (Frontend)**。
*   它就是我们架构图里说的“前端”。
*   虽然它现在只显示一行简陋的字，但它确实在行使“顾客”的权利：**向服务器要数据**。

### **结果**
屏幕上出现了一行字：`{"message":"Hello, World!"}`

</div>
<div class="align-middle-center">

![配图：浏览器中显示Hello World JSON结果的截图](../../../lectures/images/2025-12-13-13-49-22.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 浏览器就是你的“测试员”
你不需要写任何代码，就能测试你的 API。
因为浏览器天生就是一个发 **GET 请求** 的工具。
当你在地址栏输入网址并回车，本质上就是对服务器说：“Hello，请把首页的内容发给我 (GET /)。”
屏幕上显示的那串 JSON，就是服务器给你的回信。

</div>

---

## **8. 厨房救火：常见报错与修复**

<div class="columns" style="font-size: 0.95em;">
<div>

### **常见问题 1: 端口被占用**
*   **报错**: `Address already in use`
*   **原因**: 上一个程序没关，或者开了两个终端。
*   **解法**: 关掉所有终端，或者把代码里的 `8000` 改成 `8001`。

### **常见问题 2: 访问报错**
*   **现象**: 浏览器显示 "无法访问此网站"。
*   **原因**: 代码没运行，或者 `host` 写错了。
*   **解法**: 检查终端里是否有 `Uvicorn running` 的绿字。

</div>
<div class="align-middle-center">

![配图：一个医生给服务器看病的卡通图](../../../lectures/images/2025-12-13-14-00-14.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 端口 (Port)
如果 IP 地址是“大楼地址”，那么 Port 就是“房间号”。
一个房间同时只能进一个人。如果你的上一个程序还没关，新程序就进不去这个 8000 号房间。
**解决方法**：要么把里面的人赶出来（关掉旧程序），要么换个房间（改成 8001）。

</div>

---

## **9. 应用需求：从静态到动态**

<div class="columns" style="font-size: 0.8em;">
<div class="styled-div" style="font-size: 0.7em;">

### **业务场景**
*   **静态 (Static)**: `Hello World` 是固定的，每个人看到的都一样。
*   **动态 (Dynamic)**: 真实的业务（如查价格）是因人而异的。
    *   顾客查 "红烧肉" -> 返回 20 元
    *   顾客查 "宫保鸡丁" -> 返回 15 元

### **技术映射**
我们不需要为每个菜写一个网页。
我们需要的是**一套逻辑**：
`输入(菜名) -> 查找(字典) -> 输出(价格)`

这就是编程中最核心的能力：**抽象 (Abstraction)**。

</div>
<div class="align-middle-center">

![配图：左边是静止的招牌，右边是滚动的电子屏，暗示动态变化](../../../lectures/images/2025-12-13-14-02-26.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 网址传参 (URL Parameters)
这就像**完形填空**。
我们写一个模板：`这个菜是 {dish_name}`。
- 用户访问 `/menu/红烧肉` -> `dish_name` = 红烧肉
- 用户访问 `/menu/土豆丝` -> `dish_name` = 土豆丝
这样我们写一次代码，就能应对几千种不同的菜。这就是编程里的“偷懒”智慧——**复用**。

</div>

---

## **9.1 Prompt 设计 (Dynamic Params)**

<div class="columns">
<div>

### **策略：参数化 (Parameterization)**
*   **场景**: 餐厅不能只有一道菜，也不能为每一道菜写一个函数。
*   **关键点**:
    1.  **Data**: 先定义一份数据源 (Menu)。
    2.  **Variable**: 定义一个“变量” (Dish Name)。
    3.  **Logic**: 根据变量去数据源里查价格。

</div>
<div>

### **Prompt (Copy & Paste)**
> "请给 API 加一个**查询价格**的功能。
> 1. 数据：创建一个包含 '麻婆豆腐': 12, '宫保鸡丁': 15 的菜单字典。
> 2. 接口：`GET /menu/{dish_name}`。
> 3. 逻辑：接收菜名，返回对应的价格。如果没这道菜，返回错误信息。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要在 Prompt 里写大括号 {}？
在 Prompt 中写 `/menu/{dish_name}`，是利用了 FastAPI 的**路径参数**语法。
大模型（如 ChatGPT）读过很多代码，它看到这个花括号，就会明白：“哦，这里需要定义一个变量”。
这就好比你跟建筑师说“这里留个窗户”，他就会在图纸上画个框，而不是砌死。

</div>

---

## **9.2 代码解析：接口参数 (API Params)**

<div class="columns">
<div>

### **AI 生成的代码**
```python
# 1. 字典 (数据源)
menu = {"麻婆豆腐": 12, "宫保鸡丁": 15}

# 2. 接口参数 {dish_name}
@app.get("/menu/{dish_name}")
def get_price(dish_name: str):
    # 3. 查字典
    if dish_name in menu:
        return {"price": menu[dish_name]}
    else:
        return {"error": "Sold out"}
```

</div>
<div>

### **分析 (Analysis)**
*   **`{dish_name}`**: 这是 URL 里的**挖孔**。用户在浏览器输入什么，这里就会接收到什么。
*   **动态性**: 一个函数，服务千万道菜。这就是编程的魅力——**复用**。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 字典查表 (Dictionary Lookup)
代码中的 `menu[dish_name]` 就是在**查字典**。
- `menu` 是一本字典书。
- `dish_name` 是你要查的单词。
- 我们把查到的结果（12元），起个名字叫 `price`，然后递给顾客。
这是计算机处理数据最快、最常用的方式之一。

</div>

---

## **10. 试菜台：Swagger UI**

<div class="columns ratio-6-4" style="font-size: 0.75em;">
<div class="styled-div" style="font-size: 0.7em;">

### **浏览器地址栏的局限**
浏览器地址栏只能做最简单的查询 (GET)。
如果你想做**更专业的测试**（比如填参数、或者下节课要学的 POST 操作），地址栏就不够用了。

### **神奇的 `/docs`**
FastAPI 自动为你生成了**交互式文档 (Swagger UI)**。

**操作**:
1. 访问 `http://127.0.0.1:8000/docs`
2. 只要点点按钮，就能测试刚刚写的 `/menu/{dish_name}` 接口。

### **特别说明：这不是给用户用的**
*   **Swagger UI**: 是给**厨师（开发者）**用的**试菜台**。
*   **Frontend (Lesson 22)**: 才是给**顾客（用户）**用的**餐桌**。

</div>
<div class="align-middle-center">

![配图：Swagger UI界面截图](../../../lectures/images/2025-12-13-14-07-04.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 自动生成的说明书
以前写代码，写完还得专门写个 Word 文档告诉别人怎么用。
FastAPI 最牛的地方在于，你代码写完，**使用说明书 (API文档)** 自动就生成好了。

**冷知识：为什么叫 Swagger？**
"Swagger" 在英语里是“昂首阔步、神气活现”的意思。创始人 Tony Tam 起这个名字，就是为了表达他对这个工具充满自信——**“它自带气场 (It's got swagger)”**。

</div>

---

## **11.课程小结**

<div class="columns ratio-6-4" style="font-size: 0.75em;">
<div class="styled-div" style="font-size: 0.7em;">

### **关键点**
1.  **架构思维**: 浏览器 (Browser) 是顾客，API (Server) 是后厨。
2.  **Prompt 工程**: 描述清楚“端点(Endpoint)”和“返回内容”，AI 就能写出 API。
3.  **验收能力**: 能够读懂 `@app.get` 并确认 AI 是否正确实现了路由。
4.  **交互**: 通过 URL 网址传递接口参数。
5.  **数据通识**: Web 世界的通用语——**JSON**。

### **下节预告**
现在我们有了 **“后厨”** (API)，但只有一个简陋的测试界面(Swagger)。
为了让普通用户（比如你的学生）也能用，我们需要一张 **“脸”**。
下节课，我们将学习 **Web 前端开发**。
我们不再满足于 AI 生成的静态网页，而是要让网页**活起来**，真正去连接我们的 Python 后端！做一个**供多人使用的Web应用**！

</div>
<div class="align-middle-center">

![配图：一张简单的思维导图，连接浏览器、API和Python代码](../../../lectures/images/2025-12-13-14-10-47.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 三大支柱
今天的课看似复杂，其实就讲了三件事：
1.  **架构**: 分工合作（前台接待 vs 后厨做菜）。
2.  **工具**: 快速搭建（FastAPI）。
3.  **语言**: 通用交流（HTTP 和 JSON）。
掌握了这三点，你就拿到了互联网开发的入场券。

</div>