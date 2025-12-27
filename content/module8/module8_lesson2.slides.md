---
marp: true
theme: default
paginate: true
size: 16:9
math: katex
---

<style>
/* --- Master Template Styles --- */
.rows { display: grid; grid-template-rows: repeat(2, minmax(0, 1fr)); gap: 1rem; }
.columns { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }
ul, ol { padding-inline-start: 25px; }
.tip { background-color: #f0f8ff; border-left: 5px solid #1e90ff; padding: 15px; }
.insight { background-color: #eefcff; border-left: 5px solid #17a2b8; padding: 15px; }
.quote { background-color: #fffaf0; border-left: 5px solid #ffcc00; padding: 20px; font-style: italic; }
</style>

![bg blur:3px brightness:60%](../../../lectures/images/2025-12-06-02-47-49.png)

<style scoped>
h1, h2 { color: #F5F5F5; text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8); }
.course-title {
  position: absolute; top: 60px; left: 80px;
  background-color: rgba(0, 0, 0, 0.4); color: #fff;
  padding: 8px 15px; border-radius: 5px;
  font-size: 22px; font-weight: bold; border-left: 5px solid #4CAF50;
}
</style>

<div class="course-title">AI赋能软件开发</div>

# 模块八: 总结与展望
## 第30节: 作品分享会 (上) —— 创意与实战 (Project Showcase I)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<!--
(1分钟) 欢迎来到我们的“Demo Day”第一场！
在硅谷，Demo Day 是创业者向世界展示梦想的时刻。
今天，这里就是我们的硅谷。
我们不看 PPT 做得漂不漂亮，我们看**代码能不能跑**，**问题解决得有没有效**。
Every line of code matters. Let's rock!
-->

---

## **Demo Day 规则 (Rules)**

<div class="columns">
<div>

### **展示流程 (10 min/Group)**
1.  **Pitch (2 min)**:
    *   **痛点**: 解决了什么具体教学/工作问题？
    *   **方案**: 你的核心思路 (One-liner)。
2.  **Live Demo (5 min)**:
    *   **必须演示**: 现场运行程序/网页。
    *   *禁止只放视频或截图 (除非网络不可抗力)*。
3.  **Q&A (3 min)**:
    *   接受师生提问与代码审查 (Code Review)。

</div>
<div>

### **评价维度 (Rubric)**
*   **创新性 (Innovation)**: 20%
    *   *想法是否独特？Prompt 是否巧妙？*
*   **完整性 (Completeness)**: 40%
    *   *代码能否跑通？主要功能是否实现？*
*   **实用性 (Utility)**: 40%
    *   *真的能解决问题吗？明天能用在课堂上吗？*

</div>
</div>

---

## **Group 1: 学科工具组**

*(请第一组上台，并在副屏准备好代码环境)*

<div class="tip">

**观察引导**:
请关注该组是如何将**学科知识** (Domain Knowledge) 转化为**Prompt** 的。
他们是否解决了“AI 幻觉”的问题？

</div>

*   **项目名称**: ____________________
*   **开发者**: ____________________
*   **核心技术栈**: (例如: Python + DeepSeek API)

---

## **Group 2: 效率工具组**

*(请第二组上台)*

<div class="tip">

**观察引导**:
请关注该组的**自动化流程** (Automation)。
他们使用了什么循环结构？如何处理异常情况 (Error Handling)？

</div>

*   **项目名称**: ____________________
*   **开发者**: ____________________
*   **核心技术栈**: (例如: Pandas + Excel Automation)

---

## **Group 3: 创意交互组**

*(请第三组上台)*

<div class="tip">

**观察引导**:
请关注该组的**用户体验** (User Experience)。
如果是 Web 应用，界面是否友好？交互逻辑是否清晰？

</div>

*   **项目名称**: ____________________
*   **开发者**: ____________________
*   **核心技术栈**: (例如: Streamlit / FastAPI)

---

## **中场点评 (Halftime Review)**

<div class="insight">

**讲师点评**:
我们看到了几个共同的亮点：
1.  **敢于动手**: 不再畏惧 Error，而是把 Error 当作导航。
2.  **人机协作**: 懂得了“让 AI 做 AI 擅长的 (生成代码)，人做人擅长的 (设计逻辑)”。

**改进建议**:
*   **硬编码 (Hard Coding)**: 有些同学把文件路径写死在代码里了 (`C:/Users/Administrator/...`)，换个电脑就跑不起来。记得要用**相对路径**。
*   **Prompt 优化**: 有些生成的回答太长，可以在 Prompt 里限制字数或格式。

</div>

---

## **下节预告**

精彩还在继续！
下节课，我们将迎来第二批项目展示，并将进行**深度复盘研讨**。
我们将一起探讨：作为非计算机专业的老师，如何在这条路上走得更远？

**请下半场的选手做好准备！**