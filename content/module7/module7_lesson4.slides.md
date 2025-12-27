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
(1分钟) 各位老师好！这节课是黑客松 Demo Day 前的最后一次“技术交流”。
大家的“脚手架”代码应该已经跑起来了。
但要把这些做成一个能演示的产品，我们还得跨过最后一公里：**稳定性**。
比如：AI 突然说胡话怎么办？演示时断网怎么办？
本节课我们了解一下如何加固代码。
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
(1分钟) 我们这节课有三个任务。
第一，教大家怎么修 Bug。特别是当 AI 不听话的时候，怎么定位问题。
第二，教大家怎么“驯服” AI。让它乖乖吐出我们想要的格式，而不是一大堆废话。
第三，为了防止翻车，我们要做一个赛前检查清单。
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
(3分钟) 当你的程序跑不通时，不要慌。我们用“二分法”来排查。
首先 `print` 一下 input。如果 Vision 没识别出字，那是眼睛的问题。
如果 Vision 识别对了，但 DeepSeek 回复报错，那是脑子的问题。
通常大家遇到最多的坑，就是 AI 太客气了。
我们要的是 JSON 数据，它非要加一句“好的，这是您的结果”。
这多余的一句话，就会让我们的程序崩溃。
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
(3分钟) 最后，为了下周的 Demo Day，大家一定要过一遍这个清单。
特别是 Plan B。
现场网络可能会很差，DeepSeek 的 API 可能会挂。
万一挂了怎么办？你就在代码里写死一个假数据返回。
演示的时候，大家看的是你的 Idea，只要界面能动，大家是可以理解的。
千万不要在台上尴尬地修 Bug。
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
(1分钟) 课程到今天已经接近尾声，回顾过去七周，我们走过了一段精彩的旅程。
从一开始大家只会复制粘贴提示词，到现在我们可以用 AI 去看、去听、去思考。
你们已经不仅是老师，你们是懂 AI 的产品经理。
下周的 Demo Day，非常期待看到大家的作品。
不管它多简陋，它都是我们用AI赋能教育的证明。
我们下周见！
-->