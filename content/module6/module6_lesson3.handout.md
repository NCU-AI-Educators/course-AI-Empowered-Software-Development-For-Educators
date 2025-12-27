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
![bg blur:2px brightness:60%](../../../lectures/images/2025-12-13-16-38-09.png)

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
## 第23节课: 案例拆解——从脚本到应用 (MUD游戏Web化)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 重构 (Refactoring)
重构是软件工程的核心活动之一。它指的是**在不改变软件外部行为（功能）的前提下，改善其内部结构**。

今天我们做的略有不同，我们在重构内部架构（从单机到 Web）的同时，也升级了外部表现（从文字到 GUI）。这是理解“软件演化”的最佳实践。

</div>

---

## **1. 对比：进化前 vs 进化后**

<div class="columns" style="font-size: 0.92em;">
<div class="styled-div" style="font-size: 0.7em;">

### **Before: 命令行脚本 (CLI)**
*   **界面**: 黑底白字，枯燥。
*   **操作**: 必须敲键盘 (`/go north`)。
*   **局限**: 只能在自己的终端里跑，没法手机玩。
*   **运行模式**: `While True` 死循环。

### **After: Web 应用 (Web App)**
*   **界面**: 图文并茂，直观。
*   **操作**: 点击按钮 (👆北)。
*   **优势**: 发个链接给朋友，手机也能玩。
*   **运行模式**: **事件驱动 (Request/Response)**。

</div>
<div class="align-middle-center">

![配图：左边是黑框框截图，中间箭头，右边是带有按钮和图片的网页截图](../../../lectures/images/2025-12-13-16-42-59.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 事件驱动架构 (Event-Driven Architecture)
在 Web 开发中，程序不再是“从头跑到尾”。

- **Server (后端)**: 处于 **Passive (被动)** 状态。它启动后就进入“监听模式”，等待 HTTP 请求。
- **Client (前端)**: 处于 **Active (主动)** 状态。用户的点击行为触发请求，推动业务逻辑向前走。

理解这种 **“请求-响应”** 的心跳节奏，是理解 Web 开发的关键。

</div>

---

## **2.1 第一步：产品定义 (Define)**

<div class="columns" style="font-size: 0.9em;">
<div>

### **角色：产品经理 (PM)**
*   **任务**: 梳理 MUD 游戏的核心玩法，输出结构化的需求文档。
*   **Prompt**:
    > "你是一位资深游戏策划。
    > 请把命令行 MUD 游戏重构为 Web 版。
    > **核心玩法**: 
    > 1. 探索: 进房间看描述。
    > 2. 社交: 看其他玩家。
    > 3. 移动: 点击按钮移动。
    > 请输出 **User Stories (需求故事)**。"

</div>
<div>

### **PM 产出 (Requirements)**
1.  **US-01 漫游**: 玩家能看到当前房间描述。
2.  **US-02 邂逅**: 玩家能看到同房间的人。
3.  **US-03 行动**: 玩家能通过点击按钮改变位置。
4.  **US-04 身份**: 玩家需要有唯一名字。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 用户故事 (User Story)
敏捷开发中的标准需求格式：`As a <User>, I want to <Action>, so that <Value>`.

它的价值在于**Context (语境)**。
单纯说“我要个按钮”是苍白的；但说“我要个按钮来移动”，开发人员（AI）就知道这个按钮背后需要连接移动逻辑。

</div>

---

## **2.2 交付物解析：需求与数据**

<div class="columns">
<div>

### **技术拆解**
*   **User Story (用户故事)**: 是敏捷开发的核心。它不谈技术细节，只谈“谁(Who) 要做什么(What) 达到什么目的(Why)”。
*   **数据模型映射**:
    *   US-01 -> `World Map` (固定字典)
    *   US-02/04 -> `Player Session` (动态字典)

</div>
<div>

### **AI 生成的数据结构**
```python
# World Map (Static)
world = {
    "广场": {"desc": "...", "exits": {...}},
    "客栈": {"desc": "...", "exits": {...}}
}

# Player Session (Dynamic)
players = {
    "GuoJing": {"loc": "广场"},
    "HuangRong": {"loc": "客栈"}
}
```

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 领域模型：现实的投影
编程的本质是**对现实世界的模拟**。

- 现实中的“广场”，在 Python 里就是一个 `Dict`。
- 现实中的“移动”，就是修改 `players` 字典里 `GuoJing` 的 `loc` 字段。

当你能熟练地把现实事物映射为数据结构时，你就掌握了后端开发的精髓。

</div>

---

## **2.3 效果演示：需求文档概览**

<div style="font-size: 0.72em;">

# 需求规格说明书 (PRD) - MUD Game Web 2.0

## 1. 核心用户故事 (User Stories)

| ID | 角色 (As a...) | 需求 (I want to...) | 价值 (So that...) |
| :--- | :--- | :--- | :--- |
| **US-01** | **探索者** | 查看当前房间的文字描述 | 获得沉浸式体验 (Immersion) |
| **US-02** | **社交者** | 看见同一房间内的其他玩家 | 产生多人在线的连接感 |
| **US-03** | **玩家** | 点击按钮(东/南/西/北)移动 | 降低操作门槛(无需打字) |
| **US-04** | **访客** | 拥有唯一的江湖名号 | 在游戏世界中建立身份标识 |

## 2. 非功能需求 (NFR)
*   **接入效率**: 无需安装 App，手机扫码即玩。
*   **响应速度**: 移动反馈需要在 200ms 内完成。
*   **兼容性**: 适配 iOS/Android 手机浏览器视图。

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 文档驱动开发 (Document-Driven)
在 AI 时代，文档的重要性不降反升。

因为文档成为了人与 AI 协作的**中间介质**。
- 人类负责 Review 文档（人类检查逻辑对不对）。
- AI 负责 Implement 文档（人类检查代码对不对）。
一份高质量的文档，是生成高质量代码的前提。

</div>

---

## **3.1 第二步：架构设计 (Design)**

<div class="columns">
<div>

### **角色：架构师 (Architect)**
*   **任务**: 将模糊的需求转化为精确的 **API 契约 (Contract)**。
*   **Prompt**:
    > "作为架构师，请基于上述需求设计 API 接口：
    > 1. **User Action**: 登录、移动、查看状态。
    > 2. **Response**: 必须是 JSON 格式。
    > 请输出 **API 列表** 和 **返回示例**。"

</div>
<div>

### **Arch 产出 (API Schema)**
1.  `POST /login`: 注册及心跳。
2.  `POST /move`: 改变 `players` 字典中的位置。
3.  `GET /state`: 获取当前 `world` 描述和 `players` 列表。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 系统边界 (System Boundaries)
架构设计的核心就是**划界**。

API (Application Programming Interface) 就是这道界线上的**窗口**。
通过 API，我们将复杂的后端逻辑**封装 (Encapsulate)** 起来，只暴露简单的调用方式给前端。这是降低系统复杂度的不二法门。

</div>

---

## **3.2 交付物解析：API 契约**

<div class="columns">
<div>

### **技术拆解**
*   **为什么不需要数据库？**
    *   为了教学简化，我们用 **内存变量** (`world`, `players`) 模拟数据库。
    *   **优点**: 零依赖，代码短。
    *   **缺点**: 重启后数据丢失 (这是 MVP 版本的权衡)。
*   **RESTful 风格**:
    *   **GET** 获取状态 (幂等)。
    *   **POST** 改变状态 (副作用)。

</div>
<div>

### **JSON 契约示例**
```json
// GET /state?uid=GuoJing
{
    "code": 200,
    "data": {
        "description": "这里是...",
        "exits": ["north", "west"],
        "others": ["HuangRong"]
    }
}
```
*这个 JSON 就是前后端开发的“法律依据”。*

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 内存存储 vs 持久化
- **内存 (RAM)**: 像黑板。读写极快，但擦了（重启）就没了。
- **硬盘 (DB)**: 像笔记本。读写慢，但能永久保存。

在 MVP 阶段，我们为了追求速度，有意牺牲了持久性。这是一种**有意识的技术负债**。

</div>

---

## **3.3 效果演示：API 架构图**

![](../../../lectures/images/2025-12-13-22-06-06.png)

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 数据流图 (Data Flow Diagram)
对于初学者，代码是平面的，很难看清逻辑。
图表则是立体的。通过追踪数据的流动方向，我们能瞬间理解系统的运作机理。

</div>

---

## **4.1 第三步：编程实现 (Generate)**

<div class="columns">
<div>

### **角色：AI 工程师 (AI Worker)**
*   **任务**: 根据 API 契约，并行开发前后端代码。
*   **Prompt (Backend)**:
    > "你是一位 Python 专家。
    > 请基于设计好的 API，用 FastAPI 实现后端逻辑。
    > **数据**: 使用全局字典 `world` 和 `players`。
    > **逻辑**: `move` 接口要检查 `exits` 是否存在，合法才移动。"

</div>
<div class="styled-div" style="font-size: 0.6em;">

### **Prompt (Frontend)**
> "你是一位前端专家。
> 请编写单文件 `index.html`。
> 1. **登录页**: 输入名字，调用 `/login`。
> 2. **主界面**: 
>    *   显示房间描述 (大字)。
>    *   显示 'North/South/...' 按钮组。
>    *   显示 '这里还有: [玩家列表]'。
>    *   **Fetch API**: 与后端进行数据交互。
> 3. **交互**: 点击按钮调用 `/move`，然后刷新 `/state`。"

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 提示词链 (Prompt Chaining)
解决复杂任务时，不要试图用一句话搞定。

将任务拆解为 **Define -> Design -> Code** 的链条。
上一步的输出（文档），直接作为下一步的输入（Prompt）。这样可以最大程度减少 AI 的幻觉，保证逻辑的连贯性。

</div>

---

## **4.2 交付物解析：前后端代码**

<div class="columns">
<div>

### **后端 (FastAPI)**
*   **核心**: `main.py`
*   **特点**:
    *   `@app.post("/login")`: 处理玩家登录。
    *   `@app.post("/move")`: 处理玩家移动。
    *   `@app.get("/state")`: 获取当前房间状态。
    *   **CORS**: 允许前端跨域访问。

</div>
<div>

### **前端 (HTML/JS)**
*   **核心**: `index.html`
*   **特点**:
    *   **Fetch API**: 与后端进行数据交互。
    *   **DOM 操作**: 动态更新页面内容。
    *   **事件监听**: 响应按钮点击。
    *   **单页应用 (SPA)** 雏形。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### SPA (Single Page Application)
我们生成的这个网页是一个典型的 **SPA (单页应用)**。

- **传统网页**: 点击链接 -> 屏幕白一下 -> 加载新页面 (多页)。
- **SPA**: 点击按钮 -> 偷偷找服务器要数据 -> **局部刷新**页面文字 (单页)。

这种技术让网页拥有了像原生 App 一样丝滑的体验。

</div>

---

## **4.3 效果演示：代码结构与关键片段**

<div class="align-center">

![width:800px](../../../lectures/images/2025-12-13-16-57-37.png)

</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 工程化思维 (Engineering Mindset)
新手写代码往往是“一锅乱炖”（所有代码在一个文件里）。
专家写代码讲究“各归其位”。
- **模块化**: 把大问题拆成小文件。
- **结构化**: 用文件夹管理不同类型的文件。
这是管理复杂系统的必经之路。

</div>

---

## **5.1 第四步：产品验证 (Verify - QA)**

<div class="columns">
<div>

### **角色：测试经理 (QA)**
*   **任务**: 模拟真实用户使用，确保功能符合 US (用户故事)。
*   **测试策略**:
    1.  **单人流程**: 进得去、走得动。
    2.  **多人流程**: 开两个浏览器，互相能看见。

</div>
<div>

### **QA 产出 (Test Report)**
*   [x] 登录功能正常。
*   [x] 移动功能正常。
*   [ ] **Bug**: 两个人名字一样会冲突！ -> *Next Iteration*。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 极限编程 (XP) 精神
敏捷开发中的极限编程提倡 **"Test Everything"**。

当你发现一个 Bug 时，第一反应不应该是修代码，而是**写一个测试用例**复现它。
这样，这个 Bug 就永远不会再出现（因为有测试守门）。

</div>

---

## **5.2 交付物解析：多维度验证**

<div class="columns">
<div>

### **1. 浏览器 Network 面板**
*   按 F12 -> Network。
*   看 `fetch` 请求：
    *   **Status 200** = 成功。
    *   **Status 4xx/5xx** = 失败。
*   *这是 QA 的显微镜。*

</div>
<div>

### **2. 后端日志 (Console)**
```text
INFO:     127.0.0.1:51686 - "GET /state?uid=GuoJing HTTP/1.1" 200 OK
INFO:     127.0.0.1:51688 - "POST /move?uid=HuangRong" 200 OK
```
*   实时监控谁在做什么操作。
*   如果报错，这里会打印 Python Traceback。

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 可观测性 (Observability)
现代软件系统非常复杂，我们无法直接看到内部状态。
因此，我们需要通过系统的**外部输出**（日志、监控指标、Trace）来推断内部状态。这就是可观测性。
对于 Web 开发，HTTP 状态码（200, 404, 500）就是最基础的可观测指标。

</div>

---

## **5.3 效果演示：联网对战**

![](../../../lectures/images/2025-12-13-17-01-16.png)

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 状态同步 (State Synchronization)
这是网络游戏最难的地方。
我们需要保证所有玩家看到的“世界”是一致的。
在本例中，我们通过**轮询 (Polling)**（前端每隔几秒问一次服务器）来实现简易同步。虽然效率不高，但逻辑清晰，非常适合教学。

</div>

---

## **5.4 课堂体验：扫码加入 (Classroom Activity)**

<div class="columns" style="font-size: 0.8em;">
<div class="styled-div" style="font-size: 0.7em;">

### **零安装体验 (Zero Footprint)**
*   老师在讲台运行 `python main.py` 并打开网页。
*   **登录界面**会自动显示一个 **QR Code**。
*   其他人拿出手机，打开微信/相机 **扫一扫**。
*   **无需安装App**，直接进入名为“MUD江湖”的网页游戏。
*   大家可以在里面用 **喊话功能** 互相聊天！

### **此时此刻的架构**
*   **Server**: 老师的电脑 (运行 FastAPI)。
*   **Client**: 全班几十台手机 (运行浏览器)。
*   **Network**: 教室局域网 (Wi-Fi)。
*   **Interaction**: 实时高频并发。

</div>
<div class="align-middle-center">

![配图：手机扫描电脑屏幕上的二维码，进入游戏的场景](../../../lectures/images/2025-12-13-17-05-45.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 局域网访问原理 (LAN Access)
为什么你的手机能访问电脑上的网页？

因为你的 FastAPI 服务监听了 `0.0.0.0` (所有地址)，这意味着它向整个局域网敞开了大门。
只要手机和电脑在同一个 Wi-Fi 下（IP 网段相同），手机就能通过 `http://电脑IP:8000` 找到并访问你的服务。这打破了“只能在自己电脑上看”的限制。

</div>

---

## **6. 文档驱动的开发范式 (Documentation-Driven Development)**

<div class="columns">
<div class="styled-div" style="font-size: 0.5em;">

### **Step 1: 先写文档 (Docs First)**
*   不要上来就写代码。
*   先用 Prompt 让 AI 生成 `requirements.md` (需求) 和 `api_spec.json` (契约)。
*   **文档即源码**：文档变了，代码必须重成。

### **Step 2: 人工评审 (Review)**
*   **必须步骤**！
*   检查 AI 生成的文档逻辑漏洞。
*   Review 文档比 Review 代码快 10 倍。

### **Step 3: 生成代码 (Generate)**
*   把改好的文档喂回给 AI。
*   Prompt: "请严格按照 `api_spec.json` 实现后端代码..."

</div>
<div>

### **Project Structure (文档中心)**
```text
my_web_tool/
├── docs/            <-- 核心资产
│   ├── requirements.md
│   ├── api_spec.json
│   └── architecture.md
├── backend/         <-- 衍生品
│   ├── main.py      (AI 生成)
│   └── logic.py
├── frontend/        <-- 衍生品
│   └── index.html   (AI 生成)
└── requirements.txt
```
*   **理念**: **Docs is the Truth**. Code is just an artifact.

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么要先写文档？
因为自然语言（文档）是人类最擅长的，而编程语言（代码）是 AI 最擅长的。

通过“写文档 -> AI 生成代码”的流程，我们最大化了双方的优势：
- 人类负责**定义与决策**（在文档层面）。
- AI 负责**实现与细节**（在代码层面）。

</div>

---

## **课程小结**

<div class="columns" style="font-size: 0.8em;">
<div>

### **本次成就**
1.  **解耦**: 终于把“业务逻辑”和“界面显示”分开了。
2.  **服务化**: 你的游戏现在是一个 API 服务，理论上可以对接任何设备。
3.  **全栈**: 你刚刚完成了一次包含了 Backend (FastAPI) 和 Frontend (HTML/JS) 的全栈开发！

### **Thinking...**
但是，**如果服务器断电重启，玩家数据会怎样？**
*(数据瞬间蒸发！这就需要**数据库**来实现**持久化**。)*

</div>
<div class="align-middle-center">

![配图：一个复杂的钟表内部结构，象征解耦后的精密系统](../../../lectures/images/2025-12-13-17-18-16.png)

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 应用架构的三驾马车 (Three-Tier Architecture)
一个成熟的软件系统通常包含三层：
1.  **表现层 (Presentation)**: 浏览器/HTML (已掌握)。
2.  **业务逻辑层 (Logic)**: Python/FastAPI (已掌握)。
3.  **数据持久层 (Data)**: Database (**缺席**)。

我们今天其实是用“内存变量”临时客串了第三层。真正的企业级开发，必须引入数据库来确保数据安全和持久保存。

</div>