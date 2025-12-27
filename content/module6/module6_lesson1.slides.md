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

<!--
(2分钟) 各位老师好！欢迎来到模块六。
回顾前五个模块，我们已经拥有了强大的“单兵作战”能力：
我们能用 Python 处理 Excel，能画漂亮的图表，甚至能写 MUD 游戏。
**但是，大家有没有发现一个痛点？**
我们的程序只能在自己的电脑上的终端里跑。
如果想把成果分享给学生、同事，他们得安装 Python，得配环境，非常麻烦。
**这一章，我们要打破这个限制。**
我们要学习如何把 Python 脚本变成 **Web 应用**。
只要给对方一个网址，他就能在浏览器里使用我们的 AI 工具。这就是“应用开发”的魅力。
-->

---

## **1. 课程回顾：从个人工具到孤岛困境**

<div class="columns" style="font-size: 0.9em;">
<div>

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

<!--
(2分钟) 在开始写代码前，让我们先停下来看看走过的路。
在模块一，大家体验过 AI 秒生成网页的震撼。但那些网页数据是固定的，没有后台。
在模块二到五，大家学会了用 Python 思考。有的老师甚至用 Python 的图形库做出了 MUD 游戏的界面，非常了不起。
但大家有没有发现，这些成果很难走出你的电脑？
你做的“旅游数据分析工具”，你的朋友能直接用手机打开吗？不能。他得先装 Python。
这就是“孤岛效应”。
-->

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

<!--
(2分钟) 怎么解决孤岛问题？答案就是 Web 化。
这就是我们今天要解决的最后“一公里”问题。
我们要把模块一学的“脸”（Web）和后面学的“身体”（Python）结合起来，把它变成一个真正的互联网应用。
给它一个网址，世界上的任何人都能使用你的工具，不需要他们懂怎么安装 Python。
-->

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

<!--
(1分钟) 今天的目标非常具体：我们要做一个可以在浏览器里访问的“服务接口”。
虽然它现在还很简单，只显示一行字，但它背后的原理，和淘宝、微信是完全一样的。
我们将学会两个核心概念：**请求 (Request)** 和 **响应 (Response)**。
-->

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

<!--
(1分钟) 一个完整的应用既要有头（前端）也要有身体（后端）。
这节课，我們先集中精力把“身体”造好。
因为对于 Web 应用来说，后端是灵魂。只要你的 API 做好了，无论前端是网页、手机 App 还是微信小程序，都可以直接对接使用。
所以，这节课我们的目标非常明确：**用 Python 代码提供一个可以被外界调用的接口**。
-->

---

## **5. 全局视野：互联网应用是如何运作的？**

<div class="columns" style="font-size: 0.9em;">
<div>

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

<!--
(2分钟) 在动手写代码之前，我们先从架构师角度看看蓝图。
我们后面要做的这个“学科知识机器人”，在工业界通常采用“前后端分离”的架构。
简单来说，把事情分成两半：
一部分是**前端**，就是用户看得到的界面，负责“好不好看”和“交互体验”。
另一部分是**后端**，就是用户看不到的服务器，负责“能不能用”和“逻辑计算”。
为什么要分开？因为实现方法不同，所以以前软件开发有前端工程师和后端工程师之分。
而将它们连起来的，就是我们今天要学的核心——**API**。
-->

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

<!--
(2分钟) 既然我们要把前端和后端分开，那它们之间怎么说话呢？
我们还是用那个经典的**“餐厅隐喻”**。
**前端就是顾客**，只管点菜和用餐，不需要知道菜是怎么炒的。
**后端就是后厨**，闷头做菜，很少直接面对顾客。
它们之间的桥梁就是 **API（菜单）**。顾客只能点菜单上有的菜。
而穿梭在两者之间传递盘子（数据）的，就是 **HTTP 协议（服务员）**。
理解了这个模型，你就理解了互联网应用架构的本质。
-->

---

## **5.2 互联网应用的架构图**

<div class="columns ratio 6-4" style="font-size: 0.73em;">
<div>

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

<!--
(2分钟) 我们常说“一图胜千言”。
以前，我要到处找素材用 PPT 画这个图。
现在，我只要把心里的画面描述给 AI，它几十秒就能生成一张专业级的图表。
大家看这个 Prompt：我不仅描述了内容（电脑、云），还定义了风格（扁平、科技感）。
这就是 提示词工程 在教学备课中的实战应用。
-->

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

<!--
(3分钟) 在餐厅里，我们有用餐礼仪。
最常用的两个动作是：
**GET** 就像是“看菜单”，你只是想获取信息，不会改变后厨的状态。比如你在浏览器输入网址，就是在发 GET 请求。
**POST** 就像是“下单”，你要把你的需求（数据）递给后厨。比如你登录或者提交表单，就是在发 POST 请求。

而服务器的反馈也有“行话”，叫状态码。
绿色 200 代表一切正常；
黄色 404 代表你点了一道菜单上没有的菜（找不到页面）；
红色 500 代表后厨着火了（代码写崩了）。
记住这三个数，你就能听懂服务器在说什么。以后大家打不开网页时，可以看看页面显示的是404还是500,就知道到底是服务器出问题了，还是资源被删掉了，或者是网络连不上了。
-->

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

<!--
(2分钟) 我们选用 Python 界最火的 Web 框架 —— **FastAPI**。
为什么选它？因为对初学者最友好。你只需要写一个普通的 Python 函数，加一行装饰器，它就变成了一个 API。
我们需要安装两个库：`fastapi` 负责逻辑，`uvicorn` 负责运行。（uvicorn 名字是 Python库 uvloop 和 一些 Python Web Server 产品常用的 –corn 后缀的组合，官方常用 Unicorn——独角兽的表情符号指代它）
-->

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

<!--
(3分钟) 我们先来做第一件事：让服务器跑起来。
大家把右边的 Prompt 复制给 AI。要求很明确：我要一个 Hello World，端口 8000。
端口就像是“门牌号”，必须指定好，不然我们等会找不到它。
-->

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

<!--
(3分钟) 代码生出来了，不管你看不看得懂，先通过特征识别来 Check 一下。
第一，找 `app =`，这是 App 的本体。
第二，找那个奇怪的 `@` 符号。在 Python 里这叫“装饰器”。
你不需要懂装饰器的原理，你只需要知道：**看到 @app.get 或者  @app.post，就是给这段代码挂了一个门牌号。**
第三，检查最后一行 run 的参数。如果 host 不是 0.0.0.0，记得让 AI 改过来，不然等会我们做手机访问实验时会连不通。
这就是“AI 时代的编程”：重阅读，轻拼写。
-->

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

<!--
(2分钟) 这里有两个黑话需大家记一下：**路由 (Route)** 和 **端点 (Endpoint)**。
想象顾客访问我们的服务时要经过一条长长的走廊。
**路由**就是门牌号（比如 `/menu`）。
**端点**就是门后边的那个房间（处理逻辑）。
FastAPI 的工作就是：顾客出示门牌号，就带他去哪个房间。
如果顾客出示了错误的门牌号，就不提供服务，而是提示著名的 **404 Not Found**。
-->

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

<!--
(2分钟) 等下大家在浏览器里看到结果时，会发现一串带大括号 `{}` 的英文。
这个格式叫 **JSON**。
你把它当成互联网的“普通话”就行。
好消息是，作为 Python 学习者，你已经学会它了。
仔细看，它是不是跟 Python 的**字典 (Dictionary)** 长得一模一样？
没错，你只要在代码里写一个字典，FastAPI 就会自动把它打包成 JSON 发出去。
所以，**写字典 = 写接口数据**。就这么简单。
-->

---

## **7. 顾客进店：浏览器访问**

<div class="columns ratio-6-4" style="font-size: 0.7em;">
<div>

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

<!--
(3分钟) 代码写好了，点击运行。
注意看终端，如果出现 `Uvicorn running on...`，说明服务器启动成功了！
现在，切换到浏览器，输入 `http://127.0.0.1:8000`。
看！屏幕上出现了我们 Python 代码里写的那句话。
恭喜你，你通过浏览器，成功访问了自己电脑上的程序！这就是一次完整的 Web 交互。
**这里要特别强调一下**：
我们刚才打开的这个浏览器窗口，其实就是**前端**。
虽然它现在看起来很简陋，没有漂亮的界面，但它确实完成了“顾客”的任务——向我们的后厨（服务器）点了菜，并把菜（JSON数据）展示给了我们看。
这就是最本质的前后端交互。
-->

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

<!--
(3分钟) 第一次跑服务，翻车是很正常的。
如果终端报红字说 "Address already in use"，说明 8000 号房间有人了。最简单的办法：改个房号，比如 8001。
如果你在浏览器里打不开页面，先别急着改代码，切回 VS Code 看看终端，你的“餐厅”到底开门了没有？有没有报错退出？
养成看终端日志的习惯，是成为开发者的基本素养。
-->

---

## **9. 应用需求：从静态到动态**

<div class="columns" style="font-size: 0.8em;">
<div>

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

<!--
(2分钟) 刚才的 Hello World 只是热身。
真实世界的应用，很少是完全静态的。
比如在餐厅，顾客翻菜单，点不同的菜，看到的价格是不一样的。
我们不可能提前把所有可能的对话都存好。
我们需要一种机制，让浏览器能把**“想查什么菜”**告诉服务器。
-->

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

<!--
(2分钟) 我们在网址里挖一个**“填空”**（比如 `/menu/{这里填菜名}`）。
你在浏览器里填什么，服务器就能收到什么。这就叫**“通过 URL 传参”**。
大家注意看这个 Prompt，它不再是像聊天一样随便说说，而是非常有条理。
我们明确了三件事：
1.  **数据**：不仅告诉 AI 要有菜单，还给了具体的菜名和价格做例子。
2.  **接口**：明确规定了网址长什么样，特别是那个 `{dish_name}`，告诉 AI 这里是变量。
3.  **逻辑**：告诉 AI 拿到菜名后该干嘛（查价格）。
写 Prompt 就像给程序员写需求文档，你写得越清楚，它生成的代码就越准。
-->

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

<!--
(3分钟) 我们来当一次“代码侦探”，看看 AI 写的这段代码是怎么工作的。
首先，它定义了一个**菜单**（字典），里面有麻婆豆腐和宫保鸡丁。
然后，关键来了：大家看那个 `dish_name`。它就像一个**接力棒**。
1.  你在浏览器网址里填“麻婆豆腐”，这个词就被 `dish_name` 接住了。
2.  然后它被传进函数里。
3.  最后，程序拿着它去菜单（字典）里查，找到了 12 块钱，并返给你。
如果有捣乱的顾客填了“满汉全席”，代码里的 `else` 就会生效，告诉他“卖光了”。。
-->

---

## **10. 试菜台：Swagger UI**

<div class="columns ratio-6-4" style="font-size: 0.75em;">
<div>

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

<!--
(2分钟) 在结束这节课之前，我要教大家一个专业工具。
总是手动修改浏览器地址栏太麻烦了，而且容易输错。
请大家在浏览器地址后面加上 `/docs`。
哇！一个可视化的测试页面出来了。这就是 **Swagger UI**。（Swagger就是“很拽”的意思）
以后我们写了新接口，直接来这里点一下 `Try it out` 就能测试，不需要一遍遍敲网址。
这也是专业后端开发者的标准工作方式之一（也有更高级的工具可以用，目前我们先忽略）。
-->

---

## **11.课程小结**

<div class="columns ratio-6-4" style="font-size: 0.75em;">
<div>

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

<!--
(1分钟) 总结一下。今天我们迈出了 Web 开发的第一步。
我们理解了餐厅模型，学会了用 FastAPI 开一家“数字餐厅”。
但是，这家餐厅现在只有后厨，没有前厅，没法对外营业。
下节课，我们将学习 **Web 前端**，给我们的 Python 后厨装上一间漂亮的“门面”（网页），让它变成一个真正的、用户友好的 Web 应用！
-->