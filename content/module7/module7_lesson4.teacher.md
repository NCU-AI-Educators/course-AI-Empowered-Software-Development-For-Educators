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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 导入 (Introduction)
**收口思维**: 从“狂想”回归“工程落地”。
强调“最后一公里”的重要性，为整节课的“稳定性”主题定调。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 目标设定 (Goal Setting)
**预期管理**: 明确本节课不是用来开发新功能的，而是用来“体检”的。
**关键词**: 稳定性 (Stability)、鲁棒性 (Robustness)。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 调试方法论 (Methodology)
**二分法**: 将问题拆解为“眼睛坏了”、“脑子坏了”或“网断了”。
**痛点直击**: 直接指出初学者最容易遇到的“JSON 解析错误”，引起共鸣。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 5分钟
### 环节: 代码实战 (Coding)
**鲁棒性编程**: 教会学员不要相信外部输入（哪怕是 AI 的输入）。
**正则表达式**: 展示正则在“数据清洗”中的威力，这是非 CS 教师很少接触但非常有用的工具。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 3分钟
### 环节: 工程管理 (Engineering Management)
**墨菲定律**: “凡是可能出错的事，必定会出错。”
**Plan B**: 强调演示环境的不确定性，教会学员准备 Plan B 是专业性的体现。

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

<div class="styled-box design-box">
<strong class="box-title">[教学设计]</strong>

### 教学时间: 1分钟
### 环节: 总结 (Conclusion)
**里程碑回顾**: 串联整个模块的知识点，赋予学员成就感。
**展望**: 为下一个模块 (Demo Day) 预热。

</div>