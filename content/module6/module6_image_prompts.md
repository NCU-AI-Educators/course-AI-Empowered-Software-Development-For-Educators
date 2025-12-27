# Module 6 配图生成提示词指南 (AI Image Generation Prompts)

本文档整理了 **Module 6: Python + Web 开发入门** 四节课讲义中所有图片占位符 (`placeholder_*.png`) 的 AI 生成提示词。

这些提示词专为 **Nano Banana Pro** 或类似的高级生图模型设计。

**特别说明：风格策略 (Style Strategy)**
*   **封面 (Covers)**: 采用 **电影感 (Cinematic)** 风格。建立沉浸感，强调“未来已来”的宏大叙事。
*   **内容图 (Infographics)**: 采用 **2.5D 等距/扁平 (Isometric/Flat)** 风格。强调清晰度，降低认知负荷。

---

## **课程封面 (Lesson Covers - Cinematic Style)**

以下提示词用于生成每节课的 **16:9 电影感封面图**。

### **Lesson 21: Web 应用架构 (The Backend Core)**
*   **Filename**: `L21_cover.png`
*   **Prompt**:
    > **Subject**: The Monumental Backend Architecture.
    > **Description**: An **extreme low-angle shot** looking up at towering, skyscraper-sized server monoliths in a vast, dark digital void. They stretch infinitely upwards into a canopy of fiber-optic stars. In the center, a blindingly bright vertical beam of pure energy (The API) connects the abyss to the sky. A tiny human silhouette stands at the bottom for scale, looking up at the majesty of the system.
    > **Style**: **Epic Cinematic**, Megastructure, Nolan-esque scale (Interstellar vibe), God rays, Volumetric lighting, IMAX composition, 8k resolution.

### **Lesson 22: 前端交互 (The Frontend Touch)**
*   **Filename**: `L22_cover.png`
*   **Prompt**:
    > **Subject**: Magic of Frontend Interaction.
    > **Description**: Extreme close-up (Macro shot). A human fingertip is about to touch a floating, transparent glass interface. The point of contact generates a ripple of colorful digital particles and code fragments, spreading outwards like water.
    > **Style**: **Cinematic**, Bright and airy, Apple-style commercial aesthetic, Depth of field (Bokeh), Ray tracing, Soft lighting, 8k resolution.

### **Lesson 23: MUD 游戏重制 (Code of Jianghu)**
*   **Filename**: `L23_cover.png`
*   **Prompt**:
    > **Subject**: The Awakening of a Wuxia Legend from Code.
    > **Description**: A cinematic fusion of retro-tech and oriental fantasy. An old CRT monitor displays green command-line text: ">> Enter Jianghu". Bursting OUT of the screen is a magnificent **Chinese Swordsman** (Wuxia hero) in flowing white robes, wielding a sword. His movement creates a trail that transitions from digital binary code into **traditional Chinese ink-wash (Shuimo)** strokes. Background blends a digital matrix with misty Chinese mountains.
    > **Style**: **Cinematic**, Oriental Fantasy, Wuxia aesthetics, Crouching Tiger Hidden Dragon vibe, Ink particle effects, Ethereal lighting, 8k resolution.

### **Lesson 24: 综合工作坊 (The Architect's Workshop)**
*   **Filename**: `L24_cover.png`
*   **Prompt**:
    > **Subject**: Building the Digital Future.
    > **Description**: A hero shot of a high-tech workshop. A complex, glowing holographic structure (a web application blueprint) is floating above a workbench. Mechanical arms and laser beams are assembling it. It looks like a polished gem or a complex clockwork mechanism made of light.
    > **Style**: **Cinematic**, Iron Man lab aesthetic, Blue and Orange color grading, Intricate details, 8k resolution.

---

## **Lesson 21: Web 应用架构 (module6_lesson1.master.md)**

### 1. 孤岛效应 (Slide: 课程回顾)
*   **Filename**: `placeholder_island_effect.png`
*   **Prompt**:
    > **Subject**: The "Island Effect" in software.
    > **Description**: A lonely programmer sitting on a small floating digital island with a laptop, surrounded by code blocks. In the distance, other people on separate islands look at him but cannot reach the tools. There is no bridge between them. Visualizes the isolation of local scripts.
    > **Mood**: Melancholic but clean tech style.

### 2. 脚本到应用的进化 (Slide: 进阶之路)
*   **Filename**: `placeholder_review_to_web.png`
*   **Prompt**:
    > **Subject**: Transformation from Script to Web App.
    > **Description**: A transformation pipeline. On the left, simple Python file icons (snake logo) entering a glowing digital tunnel. On the right, they emerge as modern, colorful Web Application windows floating in the cloud, accessible by phones and laptops.
    > **Style**: 3D Isometric process flow.

### 3. 单机 vs 服务 (Slide: 本课学习目标)
*   **Filename**: `placeholder_script_to_web.png`
*   **Prompt**:
    > **Subject**: Comparison of Local Script vs Web Service.
    > **Description**: Split screen. Left side: A command line interface (CLI) on a single monitor (Local). Right side: A cloud server radiating signal to multiple devices (Phones, Tablets, Laptops) showing a GUI (Web Service).
    > **Style**: Flat vector comparison infographic.

### 4. 聚焦后端 (Slide: 本课任务)
*   **Filename**: `placeholder_focus_backend.png`
*   **Prompt**:
    > **Subject**: Focus on Backend Architecture.
    > **Description**: A simplified layered architecture diagram (Frontend -> API -> Backend -> Database). The "Backend/API" layer is glowing and highlighted in bright color, while other layers are semi-transparent/faded. A magnifying glass focuses on the Python/API gear.
    > **Style**: Blueprint style, schematic.

### 5. 现代Web架构 (Slide: 全局视野)
*   **Filename**: `placeholder_app_architecture.png`
*   **Prompt**:
    > **Subject**: Modern Web App Architecture.
    > **Description**: A clean diagram showing "Client-Server" separation. Left: Devices (Mobile, Laptop). Right: Server Rack/Cloud. Middle: A bridge labeled "API". Clear data flow arrows back and forth.
    > **Style**: Modern flat infographic, corporate tech style.

### 6. 餐厅隐喻 (Slide: 解构交互)
*   **Filename**: `placeholder_restaurant_metaphor.png`
*   **Prompt**:
    > **Subject**: Restaurant Metaphor for Client-Server.
    > **Description**: A lively cross-section of a restaurant.
    > 1. **Dining Area (Client)**: Customers sitting at tables reading menus.
    > 2. **Waiter (HTTP/API)**: A waiter carrying a note (Request) to the kitchen or a dish (Response) to the table.
    > 3. **Kitchen (Server)**: Chefs cooking with ingredients (Data).
    > **Style**: 2.5D Isometric illustration, detailed and cute.

### 7. AI生成架构图 (Slide: 架构图Prompt演示)
*   **Filename**: `placeholder_architecture_diagram.png`
*   **Prompt**:
    > **Subject**: Client-Server Diagram (AI Generated Style).
    > **Description**: A laptop with a browser window on the left, labeled 'Client'. A stylized server rack or cloud icon on the right, labeled 'Server'. Two arrows connecting them: Top arrow points right labeled 'Request', bottom arrow points left labeled 'Response'.
    > **Style**: Tech-education, soft blue and friendly colors, white background, high quality vector art.

### 8. HTTP 状态码 (Slide: 深入餐厅运作)
*   **Filename**: `placeholder_http_codes.png`
*   **Prompt**:
    > **Subject**: HTTP Status Codes as Waiter Signals.
    > **Description**: Three waiters standing in a row.
    > - Waiter 1 (Green Uniform): Smiling, holding a "200 OK" sign and a covered dish.
    > - Waiter 2 (Yellow Uniform): Looking confused, holding a "404 Not Found" sign and an empty tray.
    > - Waiter 3 (Red Uniform): Looking panicked, with smoke coming from the tray, holding a "500 Error" sign.
    > **Style**: Cartoon character illustration.

### 9. FastAPI 工具 (Slide: 搭建后厨)
*   **Filename**: `placeholder_fastapi_rocket.png`
*   **Prompt**:
    > **Subject**: FastAPI Concept.
    > **Description**: A sleek, futuristic rocket ship launching upwards. The rocket has the FastAPI logo colors (Teal/Green). It creates a trail of binary code. Symbolizes speed and modern performance.
    > **Style**: Minimalist vector logo art.

### 10. 路由与端点 (Slide: 关键概念)
*   **Filename**: `placeholder_routes.png`
*   **Prompt**:
    > **Subject**: API Routes as Hotel Doors.
    > **Description**: A perspective view of a clean hotel corridor.
    > - Door 1 label: "/menu" (Menu icon).
    > - Door 2 label: "/order" (Cart icon).
    > - Door 3 label: "/login" (Key icon).
    > A digital path glowing on the floor leading to Door 1.
    > **Style**: 3D rendering, clean and bright.

### 11. 浏览器 Hello World (Slide: 顾客进店)
*   **Filename**: `placeholder_browser_hello.png`
*   **Prompt**:
    > **Subject**: Browser displaying JSON.
    > **Description**: A stylized mockup of a web browser window (Chrome style). The address bar says "http://127.0.0.1:8000". The white page content shows a simple JSON text: `{"message": "Hello, Web!"}` in a clean monospace font.
    > **Style**: Flat UI mockup.

### 12. 服务器调试 (Slide: 厨房救火)
*   **Filename**: `placeholder_debugging_server.png`
*   **Prompt**:
    > **Subject**: Debugging a Server.
    > **Description**: A cartoon doctor or engineer examining a server rack. The server has a "bandage" on a specific port (Port 8000). The engineer is holding a stethoscope connected to the server. Represents fixing connection issues.
    > **Style**: Friendly cartoon illustration.

### 13. 静态 vs 动态 (Slide: 应用需求)
*   **Filename**: `placeholder_static_vs_dynamic.png`
*   **Prompt**:
    > **Subject**: Static vs Dynamic Content.
    > **Description**: Split comparison.
    > - **Left (Static)**: A wooden signpost or stone tablet, unchangeable, dusty.
    > - **Right (Dynamic)**: A holographic digital billboard that changes content (scrolling text), glowing and interactive.
    > **Style**: Fantasy vs Sci-fi contrast.

### 14. Swagger UI (Slide: 试菜台)
*   **Filename**: `placeholder_swagger_ui.png`
*   **Prompt**:
    > **Subject**: Swagger UI Representation.
    > **Description**: A stylized UI mockup of the Swagger interface. Shows blue and green horizontal bars (GET/POST endpoints). A mouse cursor is clicking a "Try it out" button.
    > **Style**: Simplified UI wireframe, clean and professional.

### 15. 课程思维导图 (Slide: 课程小结)
*   **Filename**: `placeholder_summary_mindmap.png`
*   **Prompt**:
    > **Subject**: Lesson Summary Mindmap.
    > **Description**: A central node labeled "Web API". Branches extending to: "FastAPI" (Server), "Browser" (Client), "JSON" (Language), "HTTP" (Protocol). Icons at end of each branch.
    > **Style**: Clean, organized mind map graphic.

---

## **Lesson 22: 前端交互基础 (module6_lesson2.master.md)**

### 1. 前厅服务员 (Slide: 学习目标)
*   **Filename**: `placeholder_waiting_staff.png`
*   **Prompt**:
    > **Subject**: Front-of-House Waiter (Frontend).
    > **Description**: A dynamic scene in a restaurant dining area. A waiter (representing JavaScript) is swiftly moving between customer tables (HTML Elements) and the kitchen pass-through window (API). Speed lines indicate motion.
    > **Style**: 2.5D Isometric, lively atmosphere.

### 2. 全栈编程 (Slide: 编程实现)
*   **Filename**: `placeholder_fullstack_coding.png`
*   **Prompt**:
    > **Subject**: Full-Stack Coding Environment.
    > **Description**: A computer monitor split vertically.
    > - **Left side**: Dark mode editor with Python code (Backend logic).
    > - **Right side**: Light mode editor with HTML/CSS code (Frontend structure).
    > A pair of hands typing on a keyboard in the foreground. Glowing syntax highlighting.
    > **Style**: Cyberpunk/Tech coding aesthetic.

### 3. 开发范式螺旋 (Slide: 课程小结)
*   **Filename**: `placeholder_paradigm_shift.png`
*   **Prompt**:
    > **Subject**: Development Paradigm Shift: Linear to Spiral.
    > **Description**:
    > - **Left**: A grey, rigid downward ladder or waterfall (Waterfall model), looking heavy and slow.
    > - **Right**: A dynamic, upward-spiraling DNA-like structure or tornado (Spiral/Agile model), glowing with golden/blue energy.
    > Represents the evolution from rigid linearity to rapid iteration.
    > **Style**: Abstract conceptual art, infographic style.

---

## **Lesson 23: MUD 游戏 Web 化 (module6_lesson3.master.md)**

### 1. MUD 进化 (Slide: 对比)
*   **Filename**: `placeholder_mud_evolution.png`
*   **Prompt**:
    > **Subject**: Evolution of Text Game to Graphic Game.
    > **Description**: Split comparison.
    > - **Left (Before)**: An old CRT monitor showing green command-line text "You are in a dark room. > go north".
    > - **Right (After)**: A modern tablet displaying a colorful RPG interface with room illustrations and interactive "North" buttons.
    > An arrow points from left to right indicating upgrade.
    > **Style**: Retro vs Modern contrast.

### 2. 需求文档 (Slide: 效果演示)
*   **Filename**: `placeholder_requirements_doc.png`
*   **Prompt**:
    > **Subject**: Digital Requirements Document.
    > **Description**: A floating, holographic document sheet. It is neatly organized with headers like "User Stories", "Data Models", and checklists. It glows slightly, indicating it's "Docs as Code".
    > **Style**: Futuristic UI element, clean and high-tech.

### 3. API 架构图 (Slide: 效果演示)
*   **Filename**: `placeholder_api_architecture.png`
*   **Prompt**:
    > **Subject**: MUD Game API Architecture.
    > **Description**: A schematic data flow diagram.
    > - **User** (Stick figure) clicks "Move" button.
    > - **Signal** travels to **API Gateway** (FastAPI).
    > - **Logic** processes the move in a **Game Loop**.
    > - **Data** updates in a central **Memory Block** (World/Players).
    > - **Response** (JSON) travels back to User.
    > **Style**: Clean, schematic, educational infographic.

### 4. 代码目录结构 (Slide: 效果演示)
*   **Filename**: `placeholder_code_structure.png`
*   **Prompt**:
    > **Subject**: Project Directory Structure.
    > **Description**: A 3D isometric visualization of a project folder tree.
    > - Root folder: "mud_game".
    > - Sub-folder "backend" containing "main.py".
    > - Sub-folder "frontend" containing "index.html".
    > - File "docs" containing specs.
    > Visualized as building blocks or floating glass panes.
    > **Style**: 3D Isometric UI.

### 5. 联网对战 (Slide: 效果演示)
*   **Filename**: `placeholder_multiplayer_demo.png`
*   **Prompt**:
    > **Subject**: Multiplayer Web Interaction.
    > **Description**: Two distinct device screens (Laptop and Phone) side-by-side.
    > - Laptop screen shows "Player A" in the "Inn".
    > - Phone screen shows "Player B" in the same "Inn".
    > - A chat bubble on the Laptop says "Hello!", and it instantly appears on the Phone screen.
    > - Connection lines link both to a central cloud server.
    > **Style**: Product mockup collage.

### 6. 扫码体验 (Slide: 课堂实战)
*   **Filename**: `placeholder_qr_scan.png`
*   **Prompt**:
    > **Subject**: QR Code Scanning for Web Access.
    > **Description**: Close-up of a hand holding a smartphone. The phone camera is scanning a QR code displayed on a laptop screen in the background. On the phone screen, a magical portal or the game interface is starting to open/load.
    > **Style**: Modern lifestyle tech illustration.

### 7. 解耦系统 (Slide: 课程小结)
*   **Filename**: `placeholder_decoupled_system.png`
*   **Prompt**:
    > **Subject**: Decoupled System as Clockwork.
    > **Description**: Inside a sophisticated Swiss watch.
    > - **Golden Gears**: Represent the Backend logic.
    > - **Silver Gears**: Represent the Frontend display.
    > - They are distinct but mesh perfectly at a specific point (The API Interface).
    > Symbolizes precision and separation of concerns.
    > **Style**: Steampunk or Macro photography style, metallic textures.

---

## **Lesson 24: 综合工作坊 (module6_lesson4.master.md)**

### 1. 成果展示会 (Slide: 成果展示)
*   **Filename**: `placeholder_showcase.png`
*   **Prompt**:
    > **Subject**: Tech Project Showcase.
    > **Description**: A vibrant tech exhibition scene. Several booths or tables with monitors displaying different types of Web Apps (Charts, Text Tools, Games). Diverse people are mingling, pointing at screens, and discussing. Atmosphere of creativity and collaboration.
    > **Style**: Colorful vector illustration, joyful.

### 2. 课程拼图 (Slide: Module 6 总结)
*   **Filename**: `placeholder_module_summary.png`
*   **Prompt**:
    > **Subject**: Course Curriculum Puzzle.
    > **Description**: A large jigsaw puzzle being assembled.
    > - Piece 1 (Bottom Left): "Python Scripts" (Muscle/Bone).
    > - Piece 2 (Bottom Right): "Web Apps" (Skin/Senses) - *This piece is glowing, just placed*.
    > - Piece 3 (Top Center, Missing/Faded): "AI Model" (Brain).
    > Visualizes the progression from body to brain.
    > **Style**: 3D conceptual art.
