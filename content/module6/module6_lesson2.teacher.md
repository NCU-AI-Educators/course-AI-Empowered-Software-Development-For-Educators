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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 导入 (Introduction)
**复习**: 快速回顾 Lesson 1 的内容 (API)，引出 Lesson 2 的主题 (Frontend)。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 目标 (Objective)
**核心隐喻**: 贯穿全课的“餐厅隐喻”：Web页=前厅，API=后厨，JS=服务员。
这有助于非技术背景学员理解抽象的“前后端分离”。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 硬核知识 (Hard Core)
**关键点**: Fetch 是本节课唯一的新技术点。
用“人话”解释 Promise (.then)：不要讲异步原理，只讲“先去拿...拿到之后...再...”的顺序逻辑。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 场景引入 (Scenario)
**模糊需求**: 模拟现实中甲方/老板的常态。
教育学员：开发者的第一步往往不是 Coding，而是 Clarifying。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 需求分析 (Requirements)
**角色扮演**: 引入 PM 角色。强调“想清楚再写代码”。
Prompt 的核心在于 Context (餐厅老板) 和 Output (功能清单)。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 评审 (Review)
**Critical Thinking**: 不要盲信 AI。
引导学员检查 AI 生成的清单是否遗漏了关键的“等位”环节（呼应开头的痛点）。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 架构设计 (System Design)
**教学目标**: 培养学员的**顶层设计意识**。
**关键动作**:
1. **角色切换**: 从关注“用户要什么”(PM) 切换到关注“系统怎么做”(Architect)。
2. **抽象思维**: 引导学员将具体的业务功能（如“点菜”），映射为抽象的技术接口（如 `POST /order`）。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 设计评审 (Design Review)
**教学目标**: 培养学员的**审查能力 (Auditing Capability)**。
**关键动作**:
1. **验证标准**: 引导学员检查 AI 生成的接口是否符合 RESTful 规范。
2. **数据溯源**: 检查 API 返回的数据字段是否足以支撑前端页面的显示需求（如：页面要显示价格，API 就必须返回 price）。

</div>

---

## **3.5 第三步：编程实现 (Implementation)**

<div class="columns" style="font-size: 0.7em;">
<div class="styled-div" style="font-size: 0.8em;">

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 编程实现 (Implementation)
**教学目标**: 培养**计算思维中的“分解 (Decomposition)”能力**。
**策略**:
1. **认知负荷管理**: 将复杂的全栈开发拆解为两个独立的原子任务，避免学员产生畏难情绪。
2. **过程控制**: 强调“先后台，再前台”的工程顺序，确保地基稳固后再盖楼。

</div>

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
<div style="font-size: 0.7em;">

### **Prompt (设计驱动，出于练习目的)**
> "现在，请变身为**资深 UI 设计师**。
> 请美化 `index.html`，无需修改逻辑，只优化样式：
> 1. **风格**: 现代简约 (Modern Clean)，使用 Card 布局。
> 2. **配色**: 采用更有食欲的**暖色调** (Warm Palette)。
> 3. **交互**: 按钮和卡片增加**鼠标悬停上浮** (Hover Lift) 效果。
> 4. **适配**: 确保在手机上也能完美显示 (Responsive)。"

</div>
</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: UI美化 (Visual Design)
**教学目标**: 体验 AI 的**跨学科能力** (从逻辑构建切换到视觉设计)。
**关键策略**: **领域特定语言 (DSL) 提示法**。
通过对比“把网页做漂亮点”和使用专业术语（如 Responsive, Hover, Card）的效果差异，让学员领悟 Prompt Engineering 的核心原则：**高质量的输入决定高质量的输出**。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 集成验收 (Integration Review)
**教学目标**: 培养学员的**全链路排查能力**。
**关键策略**: **关键路径分析 (Critical Path Analysis)**。
不要只盯着报错看，而是引导学员在脑海中追踪一个点击事件的完整生命周期：`Button Click -> Fetch Request -> API Handler -> JSON Response -> DOM Update`。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 错误驱动学习 (Error-Driven Learning)
**教学策略**: **预设故障 (Planned Failure)**。
我们故意不提前配置 CORS，让学员先撞墙，亲眼看到报错。
这种“先报错，再修复”的体验，能让学员深刻理解**浏览器安全边界**的存在，比直接给出完美代码的教学效果好得多。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 逻辑进阶 (Logic Advancement)
**教学目标**: 培养学员区分 **"固定值"** 与 **"流动值"** 的计算思维。
**关键点**:
- **一次性计算**: `Finish Time` 在下单瞬间确定后就不再改变（比如 12:30 出餐）。
- **实时计算**: `Remaining Time` 必须每次根据最新的 `Now()` 重新计算。
引导学员理解：为什么我们需要在 API 接口里实时计算，而不是把“剩余 10 分钟”这个数字存进数据库（因为它下一秒就变了）。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 代码解析 (Code Walkthrough)
**教学目标**: 理解 **面向对象编程 (OOP)** 中的时间模型。
**关键概念**:
- **时刻 (Point in Time)**: `datetime` 对象。
- **时长 (Duration)**: `timedelta` 对象。
**难点突破**: 初学者常混淆两者。通过**“数轴隐喻”**（点与线段）帮助理解：
- 点 + 线段 = 新点
- 点 - 点 = 线段

</div>

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
<div style="font-size: 0.6em;">

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 测试 (Testing)
**教学目标**: 建立 **"工程化质量保障"** 的意识。
**关键概念**: **回归测试 (Regression Testing)**。
**教学策略**:
从“手动测试的不可持续性”切入。引导学员理解：随着系统变大，靠人点是不可能的。必须用代码去管理代码。这是从“业余编程”走向“专业工程”的分水岭。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 结果验证 (Verification)
**教学目标**: 建立对 **Headless Testing (无头测试)** 的感性认识。
**教学策略**:
通过对比“手动点鼠标”和“脚本跑测试”的速度差异（几分钟 vs 几毫秒），让学员直观感受自动化测试的压倒性优势，从而接受这种工程实践。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 深度思考 (Critical Thinking)
**教学目标**: 引导学员理解 **"无状态 (Stateless)"** 的架构权衡。
**认知冲突**: 通过“刷新即丢失”的现象，打破学员对“程序应该记住我”的直觉预期。
**承上启下**: 指出当前架构的局限性，自然引出下一节课的高阶主题（数据库与会话管理），激发学习欲望。

</div>

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 2分钟
### 环节: 范式升华 (Paradigm Shift)
**教学目标**: 引导学员完成**身份认同的转变**。
从关注语法的 "Code Monkey (码农)" 转变为驾驭 AI 的 **"Software Engineer (软件工程师)"**。
**核心理念**: **Coding is cheap, Architecture & Verification is expensive.** (代码变得廉价，而架构与验证变得昂贵)。

</div>

---

## **8.AI赋能的Web应用开发过程模型**

<div class="align-center">

![width:1000px](../../../lectures/images/2025-12-12-15-18-20.png)

</div>

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 模型总结 (Model Synthesis)
**核心隐喻**: **星系模型 (Galaxy Model)**。
**教学目标**: 形象化地总结“人机协作”的动态关系。
**关键点**:
1.  **能量中心**: AI 负责 Execution (写代码)，提供核心动力。
2.  **轨道控制**: 人类负责 Decision (定需求、定接口、定质量)。
3.  **并发优势**: 强调图中“生成期”的前后端并行，这是 AI 开发相对于传统开发最大的效率提升点。

</div>

---

## **9.课程小结**

<div class="columns" style="font-size: 0.85em;">
<div class="styled-div" style="font-size: 0.7em;">

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 课程结语 (Conclusion)
**教学目标**: **知识体系化 (Systematization)**。
将本节课零散的技术点（API, Fetch, CORS, Test）串联成一个完整的 **"全栈开发方法论"**。
**情感设计**: 通过预告“MUD 游戏 Web 化”，激发学员将所学技能应用于复杂趣味项目的渴望，保持学习动力。

</div>