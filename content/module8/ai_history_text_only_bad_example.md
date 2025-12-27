---
marp: true
theme: default
size: 16:9
---

<style>
/* 模拟拥挤的排版 */
.dense-columns {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 三列 */
  gap: 15px;
  font-size: 16px; /* 字体很小 */
  line-height: 1.4;
}
.dense-columns h3 {
  font-size: 18px;
  color: #333;
  border-bottom: 2px solid #666;
  margin-bottom: 10px;
  padding-bottom: 5px;
}
.dense-columns ul {
  padding-left: 20px;
  margin: 0;
}
.dense-columns li {
  margin-bottom: 4px;
}
</style>

# 境界一示例：人工智能发展简史 (文字密集型)

<div class="dense-columns">

<div>

### 第一阶段：符号与推理 (1943-1979)
*   **1943** M-P神经元：联结主义数学模型起点
*   **1948** 控制论：维纳提出反馈与交互
*   **1950** 图灵测试：定义机器智能的标准
*   **1956** 达特茅斯会议：AI 概念正式诞生
*   **1956** 逻辑理论家：首个证明定理的程序
*   **1958** LISP语言：符号处理的基石
*   **1958** 感知机：联结主义的第一次高潮
*   **1966** ALPAC报告：机器翻译失败，寒冬I
*   **1969** 明斯基批评：证明感知机局限性
*   **1972** MYCIN系统：专家系统兴起

</div>

<div>

### 第二阶段：知识与专家 (1980-2009)
*   **1980** XCON系统：专家系统商业化巅峰
*   **1986** 反向传播(BP)：复活联结主义
*   **1989** Q-Learning：强化学习形式化
*   **1997** 深蓝：符号主义战胜人类棋王
*   **1997** LSTM：解决序列长依赖问题
*   **1998** LeNet-5：CNN开启视觉识别时代
*   **2006** 深度置信网：Hinton开启深度学习
*   **2009** ImageNet：大数据时代的燃料

</div>

<div>

### 第三阶段：学习与涌现 (2010-2025)
*   **2012** AlexNet：深度学习全面爆发
*   **2013** DQN：感知与决策的初步融合
*   **2014** GAN：生成对抗网络诞生
*   **2015** ResNet：识别精度首次超越人类
*   **2016** AlphaGo：三派合一的里程碑
*   **2017** Transformer：注意力机制统治NLP
*   **2020** GPT-3：大模型涌现通用智能
*   **2022** ChatGPT：RLHF引入人类反馈
*   **2024** Sora：世界模型理解物理规律
*   **2025** 具身智能：AI进入物理世界

</div>

</div>

> **教学反思**：
> 典型的“仓库型”课件。虽然逻辑结构（分三列）有了，但信息密度过大，学生在课堂上根本来不及阅读，只能机械地拍照。缺乏视觉焦点和逻辑流动。