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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 导入 (Introduction)
**痛点痛击**: 从“单机脚本”难以分享的痛点切入，引出“Web应用”的必要性。
确立本模块的目标：从 Script（脚本）进阶到 App（应用）。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 痛点唤醒 (Pain Point)
**对比法**: 列举前几个模块的优秀成果 vs 无法分享的尴尬。
激发学员解决这个问题的强烈欲望。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 方案提出 (Solution)
**概念重构**: 将 Web 定义为 "Python 逻辑的外壳"。
这降低了学员对 Web 开发的陌生感——它只是你已有知识的一层包装。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 目标 (Objective)
强调“原理相通”，降低学员对 Web 开发的畏难情绪。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 聚焦 (Focus)
明确本节课的学习边界：暂时忽略前端页面，只关注后端的 API 实现。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 架构观念 (Architecture)
**Top-Down 教学**: 先给大图景（前后端分离），解释为什么要解耦（分工），通过“知识机器人”这个具体案例落地。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 类比 (Metaphor)
承接上一页的架构图，用隐喻来解释架构中各组件的**交互方式**。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 可视化 (Visualization)
**AI 赋能**: 展示如何让 AI 帮我们生成教学素材。你不再需要到处找图，而是描述你想要的图。
**互动**: 鼓励学员把这段 Prompt 复制给 AI (如 DALL-E, Midjourney) 试试看。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 深入原理 (Deep Dive)
补充 HTTP 基础，避免学员只会写代码但看不懂报错。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 工具介绍 (Tools)
介绍 FastAPI 的核心优势，并解释 `fastapi` 和 `uvicorn` 的关系。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 动手实验 (Lab)
**Scaffolding**: 对于非 CS 背景的老师，"端口 (Port)" 是个抽象概念。
这里用“门牌号”做类比，并强调 host="0.0.0.0" 的重要性（为了局域网访问）。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 原理 (Principle)
深入讲解 Python 的运行机制和网络端口概念，这是新手最容易卡壳的地方。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 概念强化 (Concept)
**关键点**: 区分 Route (路径) 和 Endpoint (处理函数)。
**隐喻**: 路径=门牌号，Endpoint=房间。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 概念 (Concept)
**降低认知门槛**: 强调 JSON 约等于 PyDict，消除对新术语的恐惧。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 验证 (Verification)
**关键点拨**: 明确指出“浏览器即前端”，消除学员对“前端必须是App”的刻板印象。
让学员亲手体验“代码-服务器-浏览器”的闭环，建立成就感。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 调试 (Debugging)
预判新手必踩的坑（端口占用）。
**教学策略**: 推荐使用“换房间策略”（改端口号）而非“清理房间策略”（杀进程），前者对初学者更安全且容易操作。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 进阶 (Advance)
**从常量到变量**: 这是一个认知的飞跃。
- **静态**: 像复读机，永远只说一句话。
- **动态**: 像对话，根据你问什么（输入），回答什么（输出）。
引入“填空”逻辑，是让程序变“聪明”的第一步。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 提示词工程 (Prompt Engineering)
**结构化提示词 (Structured Prompting)**:
通过 **Context (数据)** + **Instruction (接口)** + **Constraint (逻辑)** 的结构，引导 LLM 生成高质量代码。
这是从“闲聊”到“生产力”的关键转变。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 代码走查 (Code Walkthrough)
**核心目标**: 理解 **数据流 (Data Flow)**。
引导学员用手指在屏幕上划线，追踪变量 `dish_name` 的流动路径：URL -> 函数参数 -> 字典Key。
这是理解后端逻辑的关键。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 工具 (Tooling)
**前置教学**: 提前引入 Swagger UI，培养专业开发习惯，也为下节课的复杂操作打基础。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 总结 (Summary)
**回顾**: 强调后端 (API) 是核心逻辑。
**预告**: 抛出“只有后端不好用”的痛点，引出下节课的**前端 (Frontend)** 内容，建立知识的连续性。

</div>