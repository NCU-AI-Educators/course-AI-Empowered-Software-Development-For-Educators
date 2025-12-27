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

![bg blur:3px brightness:60%](image/module7_lesson4.master/1766171844943.png)

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

# 模块七: AI 应用黑客松
## 第28节: 赛前打磨——调试与优化 (Debugging & Polish)

<div style="position: absolute; bottom: 40px; left: 80px; color: rgba(255, 255, 255, 0.8); font-size: 18px; font-family: sans-serif;">
南昌大学计算机系 黎鹰
</div>

<!--
- **类型**: 逐字稿
- **内容**: |
  (1分钟) 各位老师好！这节课是黑客松 Demo Day 前的最后一次“技术交流”。
  大家的“脚手架”代码应该已经跑起来了。
  但要把这些做成一个能演示的产品，我们还得跨过最后一公里：**稳定性**。
  比如：AI 突然说胡话怎么办？演示时断网怎么办？
  本节课我们了解一下如何加固代码。
-->

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 1分钟
  ### 环节: 导入 (Introduction)
  **收口思维**: 从“狂想”回归“工程落地”。
  强调“最后一公里”的重要性，为整节课的“稳定性”主题定调。
-->

<!--
- **类型**: 解释
- **内容**: |
  ### 什么是“打磨” (Polishing)?
  在软件开发中，完成核心功能只占 20% 的时间，剩下 80% 的时间通常花在处理各种异常情况、优化性能和美化界面上。
  本节课我们聚焦于“健壮性打磨”：确保你的 AI 应用在面对各种意外输入时不会轻易崩溃。
-->

---

## **本节目标: 防止 Demo 翻车**

<div class="columns">
<div>

1.  **调试心法**: 如何在 Starter Kit 中定位问题？(是 Prompt 坏了还是代码坏了？)
2.  **结构化输出 (JSON)**: 强迫 AI 像程序员一样说话，修复“幻觉”格式。
3.  **兜底策略 (Plan B)**: 演示时的救命锦囊。

</div>
<div>

![1766171922579](image/module7_lesson4.master/1766171922579.png)

</div>
</div>

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 1分钟
  ### 环节: 目标设定 (Goal Setting)
  **预期管理**: 明确本节课不是用来开发新功能的，而是用来“体检”的。
  **关键词**: 稳定性 (Stability)、鲁棒性 (Robustness)。
-->

<!--
- **类型**: 逐字稿
- **内容**: |
  (1分钟) 我们这节课有三个任务。
  第一，教大家怎么修 Bug。特别是当 AI 不听话的时候，怎么定位问题。
  第二，教大家怎么“驯服” AI。让它乖乖吐出我们想要的格式，而不是一大堆废话。
  第三，为了防止翻车，我们要做一个赛前检查清单。
-->

<!--
- **类型**: 解释
- **内容**: |
  ### 什么是 Demo 翻车？
  在技术圈，"Demo Effect" (演示效应) 是一个著名的墨菲定律：**平时跑得好好的代码，一上台演示就会挂**。
  这通常是因为网络波动、API 突发故障或输入了边缘情况。
  本节课的核心就是教大家如何防御这些意外。
-->

---

## **1. 调试心法：定位错误的二分法**

<div class="columns">
<div style="font-size: 0.9em;">

当你的 Starter Kit 报错时，问题通常出在三个地方：

1.  **输入层 (VLM/OCR)**: 
    *   *征兆*: `result` 为空，或者认错了图。
    *   *对策*: `print(vision_result)`，看看眼睛是不是瞎了。
2.  **逻辑层 (LLM)**: 
    *   *征兆*: `JSONDecodeError`，AI 回复了一大堆废话。
    *   *对策*: 优化 Prompt。
3.  **连接层 (API)**: 
    *   *征兆*: `TimeOut`, `AuthenticationError`。
    *   *对策*: 检查 Key，检查余额。

</div>
<div>

<div class="error-box">

**最常见的坑: JSON 解析失败**
AI 说: "好的，这是结果: `{"score": 90}`"
代码崩溃: 因为它包含了多余的中文 "好的..."
**解法**: 见下一页。

</div>

![1766172334190](image/module7_lesson4.master/1766172334190.png)

</div>
</div>

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 3分钟
  ### 环节: 调试方法论 (Methodology)
  **二分法**: 将问题拆解为“眼睛坏了”、“脑子坏了”或“网断了”。
  **痛点直击**: 直接指出初学者最容易遇到的“JSON 解析错误”，引起共鸣。
-->

<!--
- **类型**: 逐字稿
- **内容**: |
  (3分钟) 当你的程序跑不通时，不要慌。我们用“二分法”来排查。
  首先 `print` 一下 input。如果 Vision 没识别出字，那是眼睛的问题。
  如果 Vision 识别对了，但 DeepSeek 回复报错，那是脑子的问题。
  通常大家遇到最多的坑，就是 AI 太客气了。
  我们要的是 JSON 数据，它非要加一句“好的，这是您的结果”。
  这多余的一句话，就会让我们的程序崩溃。
-->

<!--
- **类型**: 解释
- **内容**: |
  ### 为什么 `print()` 是最好的调试工具？
  虽然有很多高级调试器，但对于 AI 应用，简单的 `print()` 往往最有效。
  因为 AI 的输出是不可预测的自然语言，把它打印出来亲眼看看，比任何断点调试都能更快发现“幻觉”或格式错误。
-->

---

## **2. 进阶技巧：驯服 AI 的嘴 (JSON Mode)**

<div class="columns ratio-4-6">
<div>

**目标**: 让 AI 只输出 JSON，不要废话。

**Prompt 技巧**:
> "你是一个数据接口。只输出 JSON 对象。不要输出 Markdown 代码块。不要输出'好的'。"

**代码技巧 (鲁棒性)**:
哪怕 AI 输出了废话，我们也要能提取出来。

</div>
<div>

```python
import json
import re

def parse_ai_json(response_text):
    try:
        # 1. 尝试直接解析
        return json.loads(response_text)
    except:
        print("⚠️ AI 包含杂质，正在清洗...")
        # 2. 使用正则提取第一个 {...}
        match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return {"error": "无法解析AI回复"}

# 实战测试
raw = "当然可以！\n ```json\n{\"score\": 95}\n```"
data = parse_ai_json(raw)
print(data['score']) # 输出 95, 救回来了！
```

</div>
</div>

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 5分钟
  ### 环节: 代码实战 (Coding)
  **鲁棒性编程**: 教会学员不要相信外部输入（哪怕是 AI 的输入）。
  **正则表达式**: 展示正则在“数据清洗”中的威力，这是非 CS 教师很少接触但非常有用的工具。
-->

<!--
- **类型**: 解释
- **内容**: |
  ### 什么是鲁棒性 (Robustness)?
  鲁棒性是指程序在遇到异常输入时，依然能正常运行的能力。
  AI 的输出是不可控的（Probabilistic），它可能今天输出纯 JSON，明天就带个 Markdown 代码块。
  所以我们的代码必须能处理这些“杂质”。
  上面的 `parse_ai_json` 函数就是一个典型的“防御性编程”案例。
-->

<!--
- **类型**: 逐字稿
- **内容**: |
  (5分钟) 怎么解决 AI “太客气”的问题？
  一靠“严”，在 Prompt 里严厉地告诉它：不要废话！
  二靠“洗”，在代码里加一个清洗函数。
  大家看这段代码，它用了一个正则表达式。
  不管 AI 说什么，我只在里面找 `{...}` 这一对大括号。
  只要把这一块抠出来，剩下的废话全丢掉。这叫“鲁棒性”。
-->

---

## **3. 赛前检查清单 (Checklist)**

<div class="columns">
<div style="font-size: 0.9em;">

### **硬件与环境**
- [ ] 笔记本电量充足，投屏转接头带了吗？
- [ ] **本地模型** (`models` 文件夹) 完整吗？(不要现场下载！)
- [ ] 演示用的图片/文本准备好了吗？

### **成本与风控**
- [ ] **API 余额**: 检查 DeepSeek/SiliconFlow 后台，确保还有余额。
- [ ] **Plan B**: 如果现场断网，代码里有没有写死一个 `return {...}` 的假数据？
    *   *提示*: 演示时，如果真挂了，直接切到 Plan B，不要在台上修 Bug。

</div>
<div >
<div style="margin-top:1.0em">

![1766172407632](image/module7_lesson4.master/1766172407632.png)

</div>
<div class="insight" style="font-size: 0.9em;">

**演示小贴士 (Pro Tip)**:
我们更看重**创意 (Prompt 的设计)**，而不是代码的复杂度。
如果程序跑得慢，可以一边跑一边解释你的 Prompt 思路，填补空白时间。

</div>
</div>
</div>

<!--
- **类型**: 样式替换
- **版本**: [handout, teacher]
- **查找**: |
    <div class="insight" style="font-size: 0.9em;">
- **替换**: |
    <div class="insight" style="font-size: 0.6em;">
-->

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 3分钟
  ### 环节: 工程管理 (Engineering Management)
  **墨菲定律**: “凡是可能出错的事，必定会出错。”
  **Plan B**: 强调演示环境的不确定性，教会学员准备 Plan B 是专业性的体现。
-->

<!--
- **类型**: 逐字稿
- **内容**: |
  (3分钟) 最后，为了下周的 Demo Day，大家一定要过一遍这个清单。
  特别是 Plan B。
  现场网络可能会很差，DeepSeek 的 API 可能会挂。
  万一挂了怎么办？你就在代码里写死一个假数据返回。
  演示的时候，大家看的是你的 Idea，只要界面能动，大家是可以理解的。
  千万不要在台上尴尬地修 Bug。
-->

<!--
- **类型**: 解释
- **内容**: |
  ### Mock 数据 (假数据)
  在开发中，我们会常用 Mock Data 来模拟服务器的返回。
  这不仅用于测试，也是演示时的“救命稻草”。
  当真实后端挂掉时，切换到 Mock 模式，至少能保证演示流程（点击->显示结果）是顺畅的。
-->

---

## **4. 模块总结与 Demo Day 动员**

<div class="rows">
<div class="columns">
<div>

我们经历了四个阶段：
1.  **Vision (L25)**: 给了 AI 眼睛。
2.  **Cloud (L26)**: 给了 AI 大脑 (且学会了省钱)。
3.  **Ideation (L27)**: 诞生了伟大的点子。
4.  **Polish (L28)**: 打造了坚固的铠甲。

</div>
<div style="margin-top:1.0em">


![1766172125516](image/module7_lesson4.master/1766172125516.png)

</div>
</div>

<div class="tip">

**下个模块: Demo Day**
这不是考试，而是我们的**产品发布会**。
不需要完美的 UI (黑框框也没关系)，只要能解决一个真实的痛点。
带着我们的 MVP，Demo Day 见！

</div>
</div>

<!--
- **类型**: 样式替换
- **版本**: [handout, teacher]
- **查找**: |
    <div class="tip">
- **替换**: |
    <div class="tip" style="font-size: 0.6em;">
-->

<!--
- **类型**: 教学设计
- **内容**: |
  ### 教学时间: 1分钟
  ### 环节: 总结 (Conclusion)
  **里程碑回顾**: 串联整个模块的知识点，赋予学员成就感。
  **展望**: 为下一个模块 (Demo Day) 预热。
-->

<!--
- **类型**: 逐字稿
- **内容**: |
  (1分钟) 课程到今天已经接近尾声，回顾过去七周，我们走过了一段精彩的旅程。
  从一开始大家只会复制粘贴提示词，到现在我们可以用 AI 去看、去听、去思考。
  你们已经不仅是老师，你们是懂 AI 的产品经理。
  下周的 Demo Day，非常期待看到大家的作品。
  不管它多简陋，它都是我们用AI赋能教育的证明。
  我们下周见！
-->

<!--
- **类型**: 解释
- **内容**: |
  ### 敏捷开发 (Agile Development)
  黑客松其实模拟了一个完整的敏捷开发周期 (Sprint)。
  从需求分析 (Ideation)，到原型开发 (Vision/Cloud)，再到测试加固 (Polish)，最后发布 (Demo Day)。
  这正是硅谷创业公司的工作方式。
-->