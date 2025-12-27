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

![bg blur:1px brightness:60%](../../../lectures/images/2025-12-13-14-53-06.png)

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
## 第22节课: 不仅是网页——前端交互基础

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<!--
(1分钟) 各位老师好！在上节课，我们成功搭建了“后厨”（API），并且用 Swagger 这个“试菜台”验证了它能工作。
但是，我们不可能让学生或者用户去用 Swagger 点菜吧？那太不安全了。
我们需要一个真正的“前厅”，一个装修精美、操作简单的网页。
在模块一，我们用 AI 生成过漂亮的网页。今天，我们要更进一步：
我们要让这个网页“活”起来，让它能真正连接到我们的 Python 后厨，实现数据的实时交互。
-->

---

## **1. 本课学习目标**

<div class="columns">
<div>

1.  **前后端分离**: 理解现代 Web 开发的核心模式。
2.  **让网页说话**: 使用 JavaScript 的 `fetch` 指令呼叫后厨。
3.  **Prompt 进阶**: 指挥 AI 写出既好看又能用的前端代码。

### **核心隐喻**
*   **HTML/CSS**: 餐厅装修 (静态)。
*   **JavaScript (Fetch)**: 服务员 (动态跑腿)。
*   **API**: 后厨窗口。

</div>
<div class="align-middle-center">

![配图：一个餐厅前厅，服务员在餐桌和后厨之间跑来跑去](../../../lectures/images/2025-12-13-14-55-34.png)

</div>
</div>

<!--
(1分钟) 本节课有三个核心目标。
第一，理解**“前后端分离”**。这就是现代 Web 开发的“厨房法则”：前厅点餐，后厨做菜。
第二，掌握 **Fetch 指令**。这是我们的“传菜员”，负责在前后端之间传递数据。
第三，进阶 **Prompt 技巧**。我们将学习如何指挥 AI 写出既好看又能用的前端代码。
大家只要记住今天的核心隐喻：HTML/CSS 是装修，JS 是服务员，API 是后厨窗口。
-->

---

## **2. 认识能够“跑腿”的指令：Fetch**

<div class="columns ratio-4-6">
<div>

### **Fetch API**
浏览器内置的“传送门”。

**用法 (人话版)**:
1.  **去哪里**: `fetch('http://.../menu')`
2.  **拿什么**: `.then(拿到数据)`
3.  **做什么**: `.then(显示在屏幕上)`

</div>
<div>

```javascript
// JavaScript 代码片段
// 1. 呼叫后厨
fetch('http://127.0.0.1:8000/menu/红烧肉')
  // 2. 等待回话，并把回话转成文本(JSON)
  .then(response => response.json())
  // 3. 拿到结果，更新屏幕
  .then(data => {
      document.getElementById('price').innerText = data.price;
  });
```

</div>
</div>

<!--
(3分钟) 我们看一下这段前端的核心代码。这段 JS 代码其实就讲了一个故事：
第一步 `fetch`：服务员跑去后厨窗口（URL）。
第二步 `response.json`：服务员拿到厨师给的单子（JSON），看懂它。
第三步 `innerText`：服务员跑回餐桌，把价格写在客人的账单上（更新网页元素）。
这就是前后端交互的本质。我们不需要自己写这段代码，但我们要能看懂这个流程，才能指挥 AI 去写。
-->

---

## **3. 案例背景：数字化餐厅的挑战**

<div class="columns">
<div>

### **老板的模糊需求 (Fuzzy Problem)**
> "甚至连我自己都说不清楚想要什么……
> 我只知道现在客人一多，服务员就忙不过来，到处都在喊'服务员点菜'。
> 我想弄个像肯德基那样**扫码点餐**的东西，大家自己手机上点，厨房直接做，不用服务员跑来跑去。"

</div>
<div style="font-size: 0.9em;">

### **痛点分析**
1.  **人力瓶颈**: "人肉传输" (服务员) 效率低。
2.  **描述模糊**: 只有一个方向 ("扫码点餐")，没有细节 ("具体有哪些页面？")。

### **AI赋能的软件开发范式**
*   **全能助手**: AI的编程能力远超人类，可以瞬间写出数千行代码。
*   **双刃剑**: 但它稍不留神就会写出一堆“能跑但错误”的代码，甚至搞砸整个项目。
*   **你的任务**: 用专业的**Prompt**和**工程思维**去驾驭它，而不是被它带着跑。

</div>
</div>

<!--
(2分钟) 我们先来带入一个真实的业务场景。
假设你有个朋友是一家餐厅老板。他的痛点很明确：生意太好，服务员不够用。
他想做数字化转型，但作为一个非技术人员，他只能说出“我想要个扫码点餐”。
至于具体怎么扫？界面长啥样？数据怎么传？他一头雾水。
这就是现实世界中 99% 的需求状态——**模糊**。
今天我们的第一个任务，不是写代码，而是让 AI 当我们的**产品经理 (PM)**，帮我们把这个模糊的想法，变成清晰的需求文档。
-->

---

## **3.1 第一步：需求分析 (Requirements)**

<div class="columns">
<div>

### **策略：角色扮演 (PM)**
*   **目标**: 定义产品，而不是写代码。
*   **角色**: 赋予 AI **"产品经理"** 视角。
*   **关键点**:
    1.  **场景**: 描述真实用例 (扫码点餐)。
    2.  **流程**: 这里的核心是 "Wait Time" (痛点)。
    3.  **产出**: 要求 Output 是功能清单。

</div>
<div>

### **Prompt (Copy & Paste)**
> "我是一家数字化餐厅老板。
> 请帮我梳理**顾客扫码点餐系统**的核心功能和流程。
> **场景**：顾客用手机打开网页。
> **核心流程**：**浏览菜单 -> 选择菜品 -> 确认下单 -> 查看进度**。
> 请列出核心功能点和用户旅程。"

</div>
</div>

<!--
(2分钟) 好，现在我们进入第一步：需求分析。
虽然我们心里大概知道要做“扫码点餐”，但这个想法太粗糙了。
如果直接让 AI 写代码，它可能会问你：“要不要登录？要不要支付？菜单在哪？”把你问晕。
所以，我们先不写代码，先让 AI 帮我们“理思路”。
我们赋予它 **产品经理 (PM)** 的角色，告诉它我们的业务场景（手机网页、点餐、看进度），让它帮我们列出一份详细的功能清单。
这份清单，就是我们后续开发的航海图。
-->

---

## **3.2 需求评审：AI 的分析结果**

<div class="columns">
<div>

### **AI 生成的功能清单**
1.  **用户流程**:
    *   **Home页**: 展示所有菜品列表 (图片+价格)。
    *   **Action**: 点击“下单”按钮。
    *   **Feedback**: 弹窗提示“下单成功，预计等待X分钟”。
2.  **核心痛点解决**:
    *   **电子菜单**: 实时同步，不用跑去看墙上的价目表。
    *   **进度反馈**: 缓解等待焦虑。

</div>
<div>

### **分析 (Analysis)**
*   **完整性**: AI 是否覆盖了"点餐"和"等位"两个环节？
*   **可行性**: 作为一个 Demo，这些功能是写得出来的。
*   **下一步**: 有了这份清单，我们就可以找“架构师”做设计了。

</div>
</div>

<!--
(3分钟) 收到 AI 的分析报告后，作为产品负责人，我们需要进行**评审 (Review)**。
请大家重点关注 AI 是否捕捉到了核心痛点。
比如，它是否自动补全了“等待时间反馈”这个功能？这正是解决“顾客焦虑”的关键。
初学者常犯的错误是把应用做成简单的“信息展示”（如查价格），而忽略了“业务交互”（如下单、查进度）。
今天我们要实现的，就是一个包含**数据读取**、**数据提交**和**反馈闭环**的完整 MVP (最小可行性产品)。
-->

---

## **3.3 第二步：系统设计 (System Design)**

<div class="columns">
<div>

### **策略：设计优先 (Architect)**
*   **目标**: 确定 API 接口，这是前后端的契约。
*   **关键点**:
    1.  **输入**: 拿着上一步的 PM 需求。
    2.  **要求**: 明确要求定义 API (URL 和 Method)。
    3.  **视觉**: 顺便求一个 UI 草图描述。

</div>
<div>

### **Prompt (Copy & Paste)**
> "作为架构师，请基于上述需求设计系统架构：
> 1. **API 设计**: 需要哪些接口？(明确 URL 和 Method)。
> 2. **数据结构**: 菜单和订单长什么样？(JSON 格式)。
> 3. **UI 设计**: 简述界面布局。"

</div>
</div>

<!--
(2分钟) 拿到需求清单后，很多初学者的冲动是直接开始写代码。但这时我们要先扮演“架构师”角色。
我们需要先进行**系统设计**，核心是定义 **API 接口**。
API 在这里起到了**“法律契约”**的作用。
一旦我们确定了“查询菜单”的 URL 是什么，返回的 JSON 格式长什么样，前端和后端就可以**解耦**，开始并行开发了。
后端去思考数据库怎么查，前端去思考页面怎么画，只要大家都遵守这个契约，最后就能完美拼合。
-->

---

## **3.4 设计评审：前后端契约**

<div class="columns">
<div>

### **AI 生成的 API 列表**
*   `GET /menu` 
    *   返回: `[{"name": "红烧肉", "price": 12, "time": 10}, ...]`
*   `POST /order` 
    *   输入: `{"dish": "红烧肉"}`
    *   返回: `{"status": "success", "wait_time": 10}`
*   `GET /order/status` *(Advanced)*

</div>
<div>

### **分析 (Analysis)**
*   **RESTful**: AI 使用了标准的 GET (查) 和 POST (改)。
*   **字段**: 注意 `time` 字段，这是我们计算倒计时的关键。
*   **契约**: 只要后端按这个写，前端按这个调，大家就能对上号。

</div>
</div>

<!--
(2分钟) 我们来看看 AI 这位架构师交出的图纸。
请大家重点检查两个细节：
第一，**HTTP 动词**用对了吗？`GET` 用于获取菜单，`POST` 用于提交订单。这符合 RESTful 的行业标准。
第二，**数据完整性**。特别要注意返回的数据里有没有 `time`（制作时间）字段。如果这里漏了，我们后续的“倒计时”功能就成无米之炊了。
确认无误后，这份 API 列表就成为了我们接下来的“施工标准”。
-->

---

## **3.5 第三步：编程实现 (Implementation)**

<div class="columns" style="font-size: 0.7em;">
<div>

### **策略：分工协作 (Coding)**
我们把任务拆成两块：后端和前端。

### **Prompt 1: 后端 (Backend)**
> "请修改 `main.py` 以匹配 API 设计：
> 1. 数据：创建一个包含 `price` 和 `time` 的菜单字典。
> 2. 接口：实现 `GET /menu` 和 `POST /order`。
> 3. 逻辑：下单时记录当前时间。"

### **Prompt 2: 前端 (Frontend)**
> "请写一个 `index.html`：
> 1. `fetch('/menu')` 获取列表并渲染成卡片。
> 2. 点击按钮时 `fetch('/order')` 提交订单。
> 3. 样式：美观的卡片式布局。"

</div>
<div class="align-middle-center">

![配图：程序员指挥AI写代码，屏幕上同时显示Python和HTML代码块](../../../lectures/images/2025-12-13-15-05-40.png)

</div>
</div>

<!--
(3分钟) 设计图纸完成后，我们进入施工阶段。
为了保证质量，我们将采用**“分而治之 (Divide and Conquer)”**的策略。
如果我们试图让 AI 一口气“写个完整的点餐系统”，它很容易顾此失彼。
所以，我们要像技术总监一样进行调度：
第一步，指挥**后端工程师 (AI)** 修改 `main.py`，专注于把数据逻辑跑通。
第二步，指挥**前端工程师 (AI)** 编写 `index.html`，专注于界面交互。
请大家按照这个顺序，分别发送 Prompt。
-->

---

## **3.6 视觉进阶：让 AI 当设计师 (UI Design)**

<div class="columns">
<div>

### **策略：角色赋能 (Design)**
*   **痛点**: 后端开发者的审美通常...不太行。
*   **解法**: 赋予 AI **"资深 UI 设计师"** 的角色。
*   **能力**: AI 熟知色彩心理学、排版原则和现代 CSS 特效。
*   **技巧**: 不要只说“好看”，要用**专业术语** (圆角、阴影、响应式)。

</div>
<div style="font-size: 0.9em;">

### **Prompt (设计驱动，出于练习目的)**
> "现在，请变身为**资深 UI 设计师**。
> 请美化 `index.html`，无需修改逻辑，只优化样式：
> 1. **风格**: 现代简约 (Modern Clean)，使用 Card 布局。
> 2. **配色**: 采用更有食欲的**暖色调** (Warm Palette)。
> 3. **交互**: 按钮和卡片增加**鼠标悬停上浮** (Hover Lift) 效果。
> 4. **适配**: 确保在手机上也能完美显示 (Responsive)。"

</div>
</div>

<!--
(2分钟) 功能跑通了，接下来我们关注**用户体验**。
以前，后端开发出的网页往往被戏称为“工程师审美”，既丑又难用。
但现在，你可以瞬间变身为**设计总监**。
大家注意看这段 Prompt，我们不再描述逻辑，而是大量使用了设计圈的**行话**：比如“卡片式布局”、“暖色调”、“悬停效果”。
为什么要用这些词？因为在 AI 的世界里，你使用的语言越专业，它调用的能力就越高级。
-->

---

## **3.7 代码评审：前后端对接**

<div class="columns">
<div>

### **Python (Backend)**
```python
@app.get("/menu")
def get_menu():
    return menu_data  # 列表

@app.post("/order")
def create_order(item: Item):
    # 记录时间，模拟下单
    return {"status": "ok"}
```

</div>
<div>

### **JavaScript (Frontend)**
```javascript
// Render Menu
fetch('/menu')
  .then(res => res.json())
  .then(data => {
     // Loop through data
     // Create HTML Elements
  });
```

</div>
</div>

<!--
(5分钟) 代码生成完毕。现在我们要进行最关键的一步：**集成 (Integration)**。
请大家像侦探一样，重点检查两条“线索”：
第一，**连接点 (Connection)**：前端 fetch 的地址 (`/menu`) 和后端定义的路由 (`@app.get("/menu")`) 必须一个字符都不差。
第二，**数据流 (Data Flow)**：后端返回的字典键名（如 `price`），前端在解析时必须用一模一样的名字（`data.price`）。
只要这两个地方对不上，程序就会立刻罢工。
-->

---

## **4. 遇到拦路虎：跨域 (CORS)**

<div class="columns">
<div>

### **现象**
网页报错：`Access to fetch ... has been blocked by CORS policy`。

### **原因 (安全机制)**
浏览器默认**禁止**网页（前厅）随意访问不同源的服务器（后厨），怕有坏人下毒。

### **解法 (在 FastAPI 端)**
我们要给后厨发“通行证”。
告诉浏览器：这个网页是自己人，放行！

</div>
<div>

```python
# 在 main.py 中增加
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    # 允许所有来源的网页访问我
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)
```

</div>
</div>

<!--
(3分钟) 当大家点击按钮时，可能会发现没有任何反应。如果我们打开浏览器的开发者工具 (F12)，会看到红色的报错信息：`CORS error`。
请不要慌张，这是 Web 开发中一定会遇到的“拦路虎”。
这其实是浏览器的**安全机制**在起作用。浏览器有一个非常严格的安全铁律：只有当 协议、域名（或IP）、端口 三者完全一致时，才被认为是“一家人”（同源）。当我们直接双击打开 index.html 文件时，浏览器地址栏会显示 file:///Users/...），因为 file 协议和网页访问后端时的 http 协议不同，浏览器默认认为前端（网页index.html）和后端(http://127.0.0.1:8000)是“陌生人”，禁止互相传递数据。
解决办法是：我们需要在后端代码里签署一份**“通行协议” (Middleware)**，显式地告诉浏览器：“我允许这个网页来访问我。”
-->

---

## **5. 课堂练习：估算等餐时间 (Wait Time)**

<div class="columns">
<div style="font-size: 0.9em;">

### **Level 1: 静态估算 (Logic)**
*   **需求**: “红烧肉要20分钟，其他菜10分钟。”
*   **Prompt**: "实现 `/eta/{dish}`，如果菜名是'红烧肉'返回20分钟，否则10分钟。"

### **Level 2: 动态倒计时 (Timestamp)**
*   **痛点**: 只有“固定时间”不够，顾客想看倒计时。
*   **目标**: `Remaining = Order + Cooking - Now()`。
*   **Prompt**: "升级系统，记录下单时间。提供 `/order/{id}/status` 接口，返回剩余分钟数。"

</div>
<div>

### **Prompt (设计驱动，出于练习目的)**
> "请升级点餐系统，实现**真实的出餐倒计时**：
> 1. **数据**: 给菜单增加 `time` (红烧肉: 10分钟)。
> 2. **下单**: 记录下单时的系统时间戳。
> 3. **接口**: `GET /order/{id}/status`。
>    **逻辑**: 用 (下单时间+制作时间) 减去 (当前时间)。
>    如果时间没到，返回剩余分钟数；到了，返回'已出餐'。"

</div>
</div>

<!--
(2分钟) 基础功能完成后，我们要解决最具挑战性的痛点：**缓解等待焦虑**。
简单地告诉顾客“红烧肉要做20分钟”是不够的。因为10分钟后，他还需要等20分钟吗？不，应该是10分钟。
这就需要我们的系统具备**时间感**。
我们需要指挥 AI 做两件事：
第一，**记住**顾客下单的那一瞬间（记录时间戳）。
第二，**计算**计划出餐时间（一次性逻辑）。
第三，**计算**现在距离出餐还有多久（动态逻辑）。
这标志着我们的程序从简单的“搬运数据”进化到了“处理逻辑”。
-->

---

## **代码解析：时间戳逻辑 (Timestamp)**

<div class="columns">
<div>

### **Level 1 代码 (If-Else)**
```python
if dish_name == "红烧肉":
    return "20分钟"
```

### **Level 2 代码 (Timestamp)**
```python
# 下单时
order_time = datetime.now()

# 查进度时
cooking_time = timedelta(minutes=10)
finish_time = order_time + cooking_time
remaining = finish_time - datetime.now()
```

</div>
<div>

### **分析 (Analysis)**
*   **数学逻辑**: 时间计算 = 小学算术。
    *   `Finish` = `Now()` + `Cooking`
    *   `Left` = `Finish` - `Now()`
*   **Python 工具**:
    *   `datetime`: 获取现在的时刻。
    *   `timedelta`: 表达一段时间 (10分钟)。
*   **结论**: 只要逻辑通顺，AI 就能把公式翻译成代码。

</div>
</div>

<!--
(2分钟) 我们来看看 AI 写出的这段代码。它用到了两个很关键的词：`datetime` 和 `timedelta`。
大家可以把 `datetime` 想象成钟表上的一个**点**（时刻，如 10:30），而 `timedelta` 是一把**尺子**（时长，如 20分钟）。
Python 的强大之处在于，它允许你直接对这两个东西做加减法：**点 + 尺子 = 新的点**。
比如代码里的 `order_time + cooking_time`，Python 会自动帮你算出出餐的具体时刻。你完全不用操心“59分加1分等于00分”这种复杂的进位问题，AI 和 Python 帮你搞定了一切。
-->

---

## **6. 闭环：让 AI 自动测试 (Automated Testing)**

<div class="columns">
<div>

### **为什么要自动测试？**
*   **痛点**: 每次改了代码，都要去浏览器点点点，又累又枯燥。
*   **解法**: 让 AI 写一个 **“机器人”** (Python 脚本)，帮我们去自动访问接口。
*   **价值**:
    1.  **快**: 1秒钟测完所有接口。
    2.  **准**: 机器人不会眼花。

</div>
<div style="font-size: 0.9em;">

### **Prompt (Copy & Paste)**
> "请帮我写一个自动化测试脚本 `test_api.py`。
> **目标**: 测试点餐系统的所有接口。
> **工具**: 使用 `requests` 库。
> **测试流程**:
> 1. `GET /menu`: 确认能拿到菜单，且里面有 '红烧肉'。
> 2. `POST /order`: 下单 '红烧肉'，确认状态是成功。
> 3. `POST /order`: 下单 '乱七八糟'，确认状态是失败。"

</div>
</div>

<!--
(2分钟) 功能做完了，但还有一个隐患。
以后我们每次修改代码（比如加个新菜），难道都要手动去浏览器里点一遍按钮测试一下吗？这既浪费时间，又容易漏测。
在软件工程中，我们使用 **自动化测试 (Automated Testing)** 来解决这个问题。
我们可以让 AI 写一段专门的“质检代码”。它就像一个不知疲倦的**虚拟测试员**，能在1秒钟内把所有接口都测一遍。
一旦它发现问题，就会立刻报警。这就保证了我们无论怎么改代码，都不会破坏已有的功能。
-->

---

## **测试结果分析：解读 AI 的报告**

<div class="columns">
<div>

### **运行测试**
在终端输入：
`python test_api.py`

### **预期结果**
```text
[PASS] GET /menu: 菜单获取成功
[PASS] POST /order (红烧肉): 下单成功
[PASS] POST /order (乱七八糟): 成功拒绝异常点单
All tests passed! 
```
看到全是 **Green/Pass**，就说明你的系统非常健壮！

</div>
<div>

### **分析 (Analysis)**
*   **Requests 库**: 它是 Python 界的“浏览器”。我们用 Python 代码模拟了浏览器的行为。
*   **断言 (Assert)**: 机器人的“判断标准”。
    *   `assert response.status_code == 200`
    *   `assert "红烧肉" in response.text`

</div>
</div>

<!--
(2分钟) 现在，让我们运行这个脚本。大家看终端里的输出，是不是瞬间刷出了一排绿色的 `[PASS]`？
这说明我们的系统经受住了考验。
在这个脚本里，`requests` 库扮演了一个**没有显示器的浏览器 (Headless Browser)**，它在后台快速地向服务器发送请求。
而代码里的 `assert` 语句，就是我们设定的**质量门禁 (Quality Gate)**。比如“红烧肉的价格必须是20”，如果服务器返回了19，脚本就会立刻报错并拦截。
这一排绿色的 PASS，就是你能交付给用户的信心来源。
-->

---

## **6.5 深度思考：HTTP 协议的无状态特性 (Critical Thinking)**

<div class="columns">
<div style="font-size: 0.88em;">

### **现象观察 (Observation)**
在刚才的实验中，大家可能注意到了一个现象：
*   当用户刷新浏览器页面时，之前的下单记录**全部消失**了。
*   服务器无法区分“新用户”与“刚刚下过单的回头客”。

### **技术原理：无状态 (Stateless)**
*   这是 HTTP 协议的核心设计特征，而非 Bug。
*   **设计权衡**: 这种设计让服务器处理请求更轻量、易扩展，但也导致它无法默认维持会话上下文 (Session Context)。

</div>
<div>

### **课程设计意图 (Pedagogical Intent)**
为了降低本节课的认知负荷，我们暂时略过了**数据持久化**层。

真实的企业级应用，必须引入**状态管理 (State Management)** 机制（如数据库 Session 或 Token）来维持用户状态。

这正是我们 **下节课 (Lesson 23: MUD Game)** 将要探讨的核心挑战：如何在无状态的 Web 世界构建连续的交互体验。

</div>
</div>

<!--
(2分钟) 在课程最后，我要请大家做一个破坏性实验：刷新你的浏览器页面。
发现了什么？刚才下的单、预计的时间，全部归零了。
这是 Bug 吗？不，这是 Web 开发中最著名的特性：**HTTP 是无状态的 (Stateless)**。
就像自动售货机，你买完一瓶水走开，再回来买第二瓶，它并不认识你是刚才那个人。服务器对每一次请求都是“脸盲”的。
这种“健忘”让服务器能同时服务成千上万的人而不累垮，但也给我们带来了难题：如何让它记住“我是我”？
这正是我们在下一节课——把 MUD 游戏搬上网时，要解决的核心技术难题：**状态管理**。
-->

---

## **7.开发范式重构：从线性到螺旋**

<div class="columns" style="font-size: 0.9em;">
<div>

### **传统开发 (Waterfall)**
*   **流程**: 需求 -> 设计 -> 后端 -> 前端 -> 联调。
*   **痛点**: 线性、僵化。一旦需求变了，全流程都要返工。
*   **思维**: **“甲方验收”思维** (做好了交差)。

### **AI 赋能开发 (Agile + AI)**
*   **流程**: 需求 -> **AI (全栈生成)** -> 验证 -> 修正。
*   **特点**: **大迭代 + 小迭代**。AI 同时搞定前后端。
*   **思维**: **“过程控制”思维** (驾驭 AI，持续微调)。

</div>
<div>

### **为什么要先学后端？**
虽然 AI 能全自动生成，但如果不理解 **API** 和 **JSON**，我们就无法进行 **“质量品控”**。
*   **Lesson 21 (后端)**: 学习“发动机原理”。
*   **Lesson 22 (全栈)**: 学习“驾驶技术”。

### **角色切换**
与 AI 结对编程时，我们需要在不同角色间高频切换：
*   **PM**: 定义需求。
*   **架构师**: 控制接口规范。
*   **QA**: 验收测试。

</div>
</div>

<!--
(2分钟) 最后，我们来升华一下今天的体验。
大家发现没有？有了 AI，软件开发的模式变了。
以前，开发就像**接力赛**（瀑布模型），PM传给架构师，架构师传给后端，后端传给前端，任何一个环节掉链子，整个项目就停摆。
现在，开发更像是**指挥乐队**。你是那个乐队的灵魂——指挥家。
你指挥 AI 做需求分析，指挥 AI 做系统设计，指挥 AI (后端乐手) 写 API，指挥 AI (前端乐手) 画界面，指挥 AI (测试乐手) 找 Bug。
在这个模式下，你不再需要亲自去写文档、敲代码，但你必须懂得**看图纸**（架构设计）和**验房子**（质量验收）。
这就是 AI 时代的**“超级个体”**开发范式。
-->

---

## **8.AI赋能的Web应用开发过程模型**

<div class="align-center">

![width:1000px](../../../lectures/images/2025-12-12-15-18-20.png)

</div>

<!--
(1分钟) 这张图总结了我们今天的终极心法：**AI 赋能开发的“星系模型”**。
中间这颗恒星是 **AI 引擎**，它提供源源不断的算力和代码生成能力。
而我们人类，就像能切换轨道的行星，用提示词来切换轨道完成不同的任务：
1.  **定义期**: 作为 PM，我们把模糊的需求拆解清晰。
2.  **设计期**: 作为架构师，我们制定 **“契约” (API)**。这一步至关重要，因为有了契约，AI 就可以**左右互搏**，同时并行生成前端和后端代码，效率倍增。
3.  **验证期**: 作为 QA，我们进行验收。如果不对，带着报错日志进入下一轮**螺旋迭代**。
-->

---

## **9.课程小结**

<div class="columns" style="font-size: 0.85em;">
<div>

### **今日成就**
1.  **全栈闭环**: 完整体验了一次 **“从后端 API 到前端 Page”** 的开发全流程。
2.  **API 调用**: 用 `Fetch` 指令打通了前后端的任督二脉。
3.  **工程素养**: 掌握了 CORS 修复与自动化测试，像专业人士一样工作。

### **下节预告**
现在我们有了后端，有了前端，技术地基打好了。
下节课，我们将进入 **“案例拆解”** 环节。
来看看如何把我们在模块2写的 MUD 游戏，变成网游！

</div>
<div>

![配图：左边是单向箭头（线性），右边是螺旋上升箭头（AI迭代），展示开发模式的进化](../../../lectures/images/2025-12-13-15-08-45.png)

</div>
</div>

<!--
(1分钟) 各位老师，今天我们完成了一次跨越。
我们不再是在黑框框里写脚本，而是构建了一个完整的**互联网服务**。
回顾一下我们的武器库：**FastAPI** 是后厨，**Fetch** 是传菜员，**CORS** 是安检门，而 **自动化测试** 是我们的质量卫士。
掌握了这套组合拳，你们就已经具备了现代全栈开发的基础。
下节课，我们将迎来本次课程的高潮——**“MUD 游戏重制版”**。
我们要把模块2里那个只能自己玩的文字游戏，搬到互联网上，加入**状态管理**，让它变成一个真正的多人在线游戏。请大家做好准备！
-->