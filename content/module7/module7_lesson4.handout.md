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
.styled-div h3 {
  font-size: 1.2em; 
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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是“打磨” (Polishing)?
在软件开发中，完成核心功能只占 20% 的时间，剩下 80% 的时间通常花在处理各种异常情况、优化性能和美化界面上。
本节课我们聚焦于“健壮性打磨”：确保你的 AI 应用在面对各种意外输入时不会轻易崩溃。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是 Demo 翻车？
在技术圈，"Demo Effect" (演示效应) 是一个著名的墨菲定律：**平时跑得好好的代码，一上台演示就会挂**。
这通常是因为网络波动、API 突发故障或输入了边缘情况。
本节课的核心就是教大家如何防御这些意外。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 为什么 `print()` 是最好的调试工具？
虽然有很多高级调试器，但对于 AI 应用，简单的 `print()` 往往最有效。
因为 AI 的输出是不可预测的自然语言，把它打印出来亲眼看看，比任何断点调试都能更快发现“幻觉”或格式错误。

</div>

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

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 什么是鲁棒性 (Robustness)?
鲁棒性是指程序在遇到异常输入时，依然能正常运行的能力。
AI 的输出是不可控的（Probabilistic），它可能今天输出纯 JSON，明天就带个 Markdown 代码块。
所以我们的代码必须能处理这些“杂质”。
上面的 `parse_ai_json` 函数就是一个典型的“防御性编程”案例。

</div>

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
<div class="insight" style="font-size: 0.6em;">

**演示小贴士 (Pro Tip)**:
我们更看重**创意 (Prompt 的设计)**，而不是代码的复杂度。
如果程序跑得慢，可以一边跑一边解释你的 Prompt 思路，填补空白时间。

</div>
</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### Mock 数据 (假数据)
在开发中，我们会常用 Mock Data 来模拟服务器的返回。
这不仅用于测试，也是演示时的“救命稻草”。
当真实后端挂掉时，切换到 Mock 模式，至少能保证演示流程（点击->显示结果）是顺畅的。

</div>

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

<div class="tip" style="font-size: 0.6em;">

**下个模块: Demo Day**
这不是考试，而是我们的**产品发布会**。
不需要完美的 UI (黑框框也没关系)，只要能解决一个真实的痛点。
带着我们的 MVP，Demo Day 见！

</div>
</div>

<div class="styled-box explanation-box">
<strong class="box-title">[解释]</strong>

### 敏捷开发 (Agile Development)
黑客松其实模拟了一个完整的敏捷开发周期 (Sprint)。
从需求分析 (Ideation)，到原型开发 (Vision/Cloud)，再到测试加固 (Polish)，最后发布 (Demo Day)。
这正是硅谷创业公司的工作方式。

</div>