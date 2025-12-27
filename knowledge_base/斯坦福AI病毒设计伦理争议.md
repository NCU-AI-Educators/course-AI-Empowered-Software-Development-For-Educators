

# **达尔文2.0还是潘多拉魔盒：斯坦福大学Evo模型与AI生成病毒新纪元的分析**

## 执行摘要

本报告对斯坦福大学（Stanford University）和弧菌研究所（Arc Institute）开发的生成式人工智能模型“Evo”进行了全面分析，并深入探讨了其在成功设计出新型、有活力的病毒（噬菌体）后引发的伦理与生物安全危机 ¹。“达尔文2.0”（Darwin 2.0）³ 的比喻恰当地指出了Evo作为生物学里程碑的地位，它为加速进化和设计新型疗法提供了革命性的潜力 ¹。然而，“潘多拉魔盒”（Pandora's Box）的比喻同样适用。该模型所展示的能力——特别是“重写”基因组以创造更高适应性病毒的能力 ⁷——代表了双重用途风险的质的飞跃，显著降低了制造新型或增强型病原体的门槛 ⁹。

这场危机的核心在于当前安全范式的明显失败：作为主要保障措施的“数据排除”已被证明是无效的。当开源的Evo 1模型发布后，研究人员在数周内就利用人类病毒数据对其进行了微调 ¹⁰。本报告的结论是，学术界将如此强大、具有双重用途的模型开源的规范是站不住脚的。本报告呼吁立即建立一个基于模型许可、访问控制和人工智能驱动的合成筛选的多层次治理框架。

---

## I. 一种新的生命架构：‘Evo’模型的技术基础

### **1.1. 定义基因组基础模型**

Evo不仅仅是“用于生物学的人工智能”，而是一个“基因组基础模型”（genomic foundation model）¹¹，这是一个全新的工具类别。它由斯坦福大学的Brian Hie和弧菌研究所共同领导的多机构团队开发 ⁴，是“进化设计实验室”（Laboratory of Evolutionary Design）的一部分 ⁵。

在架构上，Evo并未使用标准的Transformer架构。它建立在**StripedHyena**之上，这是一种深度信号处理架构，旨在提高处理长序列时的效率和质量 ¹³。这一架构选择是其实现长上下文能力的关键。

在训练数据和规模上，Evo的规模是巨大的。Evo 1在270万个原核生物和噬菌体基因组上进行了训练 ¹¹。Evo 2则在一个“高度策划的基因组图谱”（OpenGenome2）上进行训练，该图谱包含**9.3万亿个DNA碱基对**，涵盖了所有生命领域，包括人类、植物、细菌甚至已灭绝的物种 ⁴。

Evo 2在上下文窗口方面取得了前所未有的突破，达到了**100万个token（核苷酸）的上下文长度** ⁴，而Evo 1的上下文长度为13.1万个碱基对（kb）¹¹。这是一个关键的技术阈值。最小的“极简”细菌基因组长度约为58万个碱基对 ¹⁵。以前的模型受限于较小的上下文窗口，只能孤立地分析基因或基因簇 ¹¹。通过跨越100万个token的门槛，Evo 2成为第一个能够同时“看到”并推理一个简单生物体*整个基因组*的模型。由于基因组依赖于“涌现的复杂性”（emergent complexity）¹⁶ 和基因之间“长距离相互作用”（long-distance interactions）⁴，这种能力是从*基因预测*转向*基因组设计*的根本推动力。该模型因此能够理解一个基因的突变如何通过数千个碱基对之外的另一个基因的变化来补偿——这是基因组层面设计的基石 ¹⁶。

### **1.2. 从预测到生成：Evo经过验证的能力**

Evo模型的能力超越了简单的模式识别，进入了功能预测和生成领域。

零样本预测（Zero-Shot Prediction）：  
该模型仅从DNA序列中学习 ¹⁴。在没有针对特定任务进行微调的情况下，它就能准确预测遗传变异的功能影响。这是一种“零样本”能力 ¹³。

* **临床相关性：** 它被证明可以预测非编码致病性突变，以及“临床上显著的BRCA1变异” ¹⁴。这直接展示了其在人类健康领域的应用潜力 ⁴。  
* **生物学洞察：** 机械可解释性分析显示，Evo*自主学习*了复杂的生物学特征，如“外显子-内含子边界、转录因子结合位点”和“蛋白质结构元件” ¹⁴。这表明它正在建立对基因组规则的真正“理解”。

多模态生成（Multimodal Generation）：  
Evo从预测转向了生成 ⁴。它可以“编写”新的遗传密码 ⁴。至关重要的是，这种生成是“多模态的”，跨越了DNA、RNA和蛋白质 ¹¹。

* **关键案例：** 该模型被用于生成合成的**CRISPR-Cas复合物** ¹¹。这不仅仅是设计一个蛋白质；它是*协同设计*（codesign）一个蛋白质（Cas核酸酶）及其非编码RNA（crRNA/tracrRNA）组件 ¹¹。  
* **关键案例：** 它还生成了功能性的**转座系统**（IS200/IS605），这是复杂的蛋白质-DNA系统 ¹¹。  
* **重大意义：** 这被认为是“使用语言模型进行蛋白质-RNA和蛋白质-DNA协同设计的首个例子” ¹¹。

这种“多模态协同设计”能力本身代表了一个新的双重用途威胁载体。传统的生物安全分析（biosecurity analyses）⁹ 通常关注单一威胁：设计一种更强的毒素（蛋白质）或一个更具毒力的基因组（DNA）。然而，Evo所*证明*的 ¹¹ 设计*功能性、多组分系统*（蛋白质 \+ RNA/DNA）的能力，代表了一种更为复杂的威胁。这种“协同设计”能力是设计复杂生物武器的技术先决条件。恶意行为者可能利用这一点，不仅设计出致病载荷，还设计出其传递、调控和表达的*整个系统*——例如，一个新型载体及其类似基因驱动的传播系统。这种复杂的相互作用是“人类设计师难以预料的” ⁸。

#### **表1：基因组基础模型Evo 1与Evo 2对比分析**

| 特征 | Evo 1 | Evo 2 |
| :---- | :---- | :---- |
| **架构** | StripedHyena ¹³ | StripedHyena ¹⁴ |
| **参数规模** | 70亿 (7B) ¹¹ | 70亿 (7B) 和 400亿 (40B) ¹⁴ |
| **训练数据规模** | 270万个基因组 (约3000亿核苷酸) ¹¹ | 9.3万亿个DNA碱基对 ¹⁴ |
| **上下文窗口** | 13.1万个碱基对 (131 kb) ¹¹ | 100万个token (1 Mb) ⁴ |
| **关键验证能力** | 零样本基因重要性测试；CRISPR系统生成 ¹³ | BRCA1变异预测；兆碱基规模生成；16个活体噬菌体 ¹ |

这份对比清晰地展示了从Evo 1（2024年11月发布 ⁶）到Evo 2（2025年2月发布 ⁴）的快速、非线性的能力飞跃。这种规模和能力的急剧增长（例如，上下文窗口从131k跃升至1M）表明，这项技术正在加速发展，为治理讨论增添了极端的紧迫性。

---

## II. 2025年9月的“卢比孔河”：有活力噬菌体的生成式设计

2025年9月，一项研究的出现标志着一个转折点，将Evo的能力从理论变为现实，从而引发了这场“伦理风暴”（ethical firestorm）。

### **2.1. 从代码到衣壳：一项关键实验**

引发伦理风暴的事件源于一份于2025年9月17日左右发布在bioRxiv上的预印本论文 ²。该论文标题为“使用基因组语言模型生成式设计新型噬菌体”（Generative design of novel bacteriophages with genome language models）¹。截至分析时，该论文尚未经过同行评审 ²。

该实验的目标是测试一个“长期存在的挑战”（long-standing challenge）¹⁶：基因组语言模型是否能“在整个基因组规模上生成功能性序列” ¹。这是对AI生成基因组*体内*（in vivo）活力的首次测试，超越了早期Evo 2论文中的*计算机*（in silico）设计 ⁸。

**方法论：**

* **模板：** 团队使用了被充分研究过的裂解性噬菌体**ΦX174**作为“设计模板” ¹。  
* **选择ΦX174的理由：** 这一选择是出于安全和研究控制的双重考虑。首先，它是1977年首个被测序的DNA基因组，研究极其充分，这使得团队能够“观察到AI对噬菌体进行的突变有多新颖” ²。其次，至关重要的是，“噬菌体不感染人类”，这使得它“在实验室中可以安全地使用” ²。  
* **过程：** Evo 1和Evo 2模型使用了ΦX174特定的序列和提示进行了微调 ⁷。这是一个*引导式生成*任务，而不是从零开始创造随机病毒。AI产生了302个候选基因组 ⁷。这些基因组随后被（化学）合成 ¹⁶，并用于测试其对抗*大肠杆菌*（E. coli）的能力 ²。

### **2.2. 非自然选择：评估AI生成的病毒**

实验结果证实了Evo模型在基因组尺度上具有强大的设计能力。

**“命中率”：** 在302个AI生成的基因组中，**有16个具有活力**——这意味着它们成功地在*大肠杆菌*宿主中复制并杀死了细菌 ¹。这是“首次通过生成式设计获得有活力的噬菌体基因组” ¹。

这一5.3%（16/302）的“命中率” ⁷ 具有深远的影响。Brian Hie曾将传统的生物设计描述为“非常手工...非常随机...成功率非常低” ²¹。相比之下，对于*从头设计*（de novo）、*有活力*的*完整基因组*而言，5.3%的成功率是一个惊人的、工业规模的成功。这一“蓝图”（blueprint）¹ 将全基因组工程从一个高失败率、依赖人类手工的工艺，转变为一个可扩展的、高通量的“生成式”过程 ²⁰。这同等地加速了良性和恶意应用的发展。

**卓越的性能：** AI生成的噬菌体不仅功能正常；许多噬菌体甚至*优于*自然的ΦX174 ⁷。

* 它们在生长竞争中表现出“更高的适应性”（higher fitness）¹。  
* 它们展示了“更优的裂解动力学”（superior lysis kinetics）（即更快地杀死细胞）¹。  
* 在一项实验中，与AI设计的变体相比，天然的ΦX174“甚至没有进入”最具传染性噬菌体的前五名 ⁷。

**“实质性的进化新颖性”：** AI展示了真正的创造力。最重要的发现来自于对AI设计的一个名为Evo-Φ36的活体噬菌体的分析 ⁸。

* **“基因组重写”的发现：** 在这个噬菌体中，其J蛋白基因（负责DNA包装）被一个来自*远缘*噬菌体（G4）的基因所取代。人类主导的实验早已证明，这种替换会*摧毁*（cripples）噬菌体的功能。然而，AI **“重写了...基因组的其余部分，使这种替换得以奏效”** ⁸。

这一“基因组重写”（genomic rewiring）的能力是该实验揭示的最具爆炸性的发现，也是“潘多拉魔盒”比喻的核心所在。合成生物学的最大挑战是“涌现的复杂性”，即“单个突变就可能使整个基因组失去活力” ¹⁶。Evo的“重写”能力 ⁸ 表明它正开始掌握这种复杂性。它不仅仅是在进行点突变；它是在执行大规模的基因组手术，然后*智能地*在其他地方应用*补偿性突变*以维持其活力。

对于恶意行为者来说，最大的挑战不是设计毒素，而是创造一个稳定、有活力和可传播的病原体来*递送*它。Evo的“重写”能力正是解决这一难题的直接方案。理论上，它可以被用来获取一个无功能的或嵌合的病原体，并将其“重写”为有活力和传染性的——这是生物武器设计中的一个典型障碍 ⁹。

#### **表2：2025年9月噬菌体生成研究摘要**

| 阶段 | 方法论 | 关键发现 / 指标 |
| :---- | :---- | :---- |
| **1. 设计** | 在ΦX174模板上微调Evo 1和Evo ² ¹ | 生成了302个候选基因组 ⁷ |
| **2. 合成与验证** | 湿实验室DNA合成并在*大肠杆菌*上测试 ¹ | 16个活体噬菌体（5.3%的命中率）¹ |
| **3. 性能** | 生长竞争和裂解动力学分析 ¹ | AI噬菌体显示出“更高的适应性”和“更优的裂解能力” ¹ |
| **4. 新颖性** | 冷冻电镜和序列分析 ¹ | “实质性的进化新颖性”，包括成功“重写”一个本应致残的基因交换 ¹ |

---

## III. “达尔文2.0”论点：生物工程的范式转变

尽管存在风险，Evo模型及其应用也带来了巨大的、革命性的益处，这构成了“达尔文2.0”论点的基础。

### **3.1. 加速进化以造福人类**

“进化设计实验室”的既定使命是“确保生物学领域的人工智能革命以造福人类的方式发生” ⁵。其目标是“加速进化”（accelerate evolution）⁵，以“设计出能够应对不断变化的威胁的生物学” ⁵。

应用1：对抗抗生素耐药性。  
这是噬菌体实验的主要良性理由。实验结果表明，由16种AI生成的噬菌体组成的“鸡尾酒”疗法，能够“迅速克服三种大肠杆菌菌株的...耐药性” ¹。这为对抗“快速进化的细菌病原体” ¹ 提供了“设计多样化合成噬菌体”的“蓝图” ¹。Brian Hie证实，他的团队“现在正致力于寻找临床应用” ⁷。这直接解决了全球公共卫生领域的一大危机 ²⁴。  
应用2：生命科学的“里程碑”。  
该工具被誉为生命科学的“里程碑”（milestone）⁴。

* **加速研究：** 该工具允许实验室“通过虚拟查询运行数十种其他标准实验” ⁴，将研究时间线从“数年（或数千年）”缩短到“数分钟或数小时” ⁴。  
* **新型疗法：** 它可以“识别...可用于生物工程和医学的分子” ⁴，设计“更好的抗病毒抗体” ⁵，并创造“有助于治愈疾病的新基因序列” ⁴。  
* **环境解决方案：** 该模型可用于“重新编程微生物”，以执行诸如碳封存或“吞噬海洋中的微塑料”等任务 ⁶。

### **3.2. “机器正在重新思考生命”**

“达尔文2.0”这一关键短语 ³ 是由普林斯顿大学化学教授**Michael Hecht**提出的，他也从事*从头设计*蛋白质的工作 ²⁵。Hecht称这项工作“非常令人不安和震惊”（very unsettling and staggering）³。他表示：“机器正在重新思考什么是人类，什么是生命...它们正在设计，创造出新的生命形式” ³。

“达尔文2.0”并不仅仅是一个诗意的比喻，它在技术上精确地描述了一个新的进化范式：

* **达尔文1.0（自然）：** 通过*随机*突变和*自然*选择来运作 ⁴。它是一个“盲眼钟表匠”。  
* **达尔文1.5（人类科学家）：** 通过*手工*设计和*人工*选择来运作。它是“非常随机的”，并且“成功率很低” ²¹。  
* **达尔文2.0（Evo）：** 引入了*生成式*设计和*计算机*（in silico）选择。它允许科学家“更直接地转向具有有用功能的突变” ⁴。AI可以“以进化史上从未有过的方式编写基因” ⁴。

这代表了进化*能动性*（agency）和*速度*（speed）的根本性转变。“加速进化” ⁵ 的使命是字面意义上的。

---

## IV. “潘多拉魔盒”的现实：全球生物安全的红线事件

与“达尔文2.0”的愿景并存的，是Evo技术所开启的“潘多拉魔盒”的严峻现实。这场“伦理风暴”的核心是Evo代表的强大的、新颖的双重用途风险。

### **4.1. 生成式生物学中的双重用途困境**

这项技术“本质上”是双重用途的（dual-use）²⁸。*同一个*“能够设计用于递送基因疗法的良性病毒载体”的模型，也“可能被用来设计一种更具致病性的病毒” ⁹。*同一种*能够找到“治疗靶点”的适应性预测能力，也能够“催化有害合成微生物的开发” ⁹。

这不再是一个未来的、假设的风险。“生成式生物学”（Generative biology）²² 和“生物人工智能模型”（BAIMs）³¹ 已经“濒临”于“实质性地帮助新手开发...生物武器” ¹⁰。人们担忧的是，这些工具将有助于“开发更具危害性甚至全新的、能够引发流行病或大流行病的病原体” ¹⁰，或“提高病毒逃避现有免疫的能力” ²³。

### **4.2. “数据排除”的谬误：一个已被证实的严重漏洞**

本报告的核心论点在于：Evo实验不仅展示了强大的能力，也暴露了当前安全范式的灾难性失败。

**宣称的保障措施：** 斯坦福团队意识到了风险。他们*主动*实施了一项保障措施：从训练数据中“排除了已知会感染人类和其他某些生物的病毒基因组” ¹⁵。这是出于“担心”AI可能“设计出可能伤害人类的病毒” ²。

**开源的决定：** 与此同时，该团队致力于“开源、完全访问”（open-source, all-access）⁴。Evo 1的模型权重和代码被发布在HuggingFace上 ⁸。

“潘多拉魔盒”时刻（10漏洞）： 该保障措施失败了。一篇2024年的学术论文——其作者中甚至*包括了Evo 2技术论文的部分作者*——记录了这次失败 ¹⁰。

1. **Evo ¹**的创建者排除了“感染真核宿主（包括人类、植物和动物）的病毒基因组” ¹⁰。  
2. 然后他们“发布了模型权重” ¹⁰。  
3. **“在Evo发布后的数周内，其他科学家就利用感染人类的病毒数据，对发布的模型权重进行了微调（refined）”** ¹⁰。

这一事件是理解当前危机的关键。噬菌体实验 ¹ 是能力的*展示*。而模型的*发布* ¹⁰ 则是打开魔盒的*行为*。10的记录是生物安全研究界*自己*承认：主要的保障措施（数据排除）在学术界的开源规范面前是无效的。

这是一个灾难性的安全范式失败。“数据排除”防御措施成了一种“表演性”的安全措施。任何行为者都可以下载开源模型，并廉价地用他们选择的任何病原体数据对其进行微调。Evo 2的论文“几乎没有提供任何保证来确保这种情况不会再次发生” ¹⁰。“开源、完全访问的工具” ⁴ 根据定义，已成为一个“系统性威胁” ²²。

### **4.3. “不切实际”的辩护：一个有时间限制的论点**

面对争议，Brian Hie为这项工作进行了辩护。他认为，生物安全的“试金石”是它是否“降低了（设计生物武器的）获取门槛” ⁷。

**Hie的论点：** Hie声称该技术*没有*降低门槛，因为他的团队需要进行大量的“前期工作”（legwork required）⁷。他表示：“如果你想用AI设计生物武器，这比从自然界中获取要困难得多...这只是不切实际的。**至少目前是这样。**”（...it'd just be impractical. **For now, at least.**）⁷。

这种“不切实际”的辩护是自相矛盾的。Hie的实验室*公开宣称的使命*就是“用机器学习改进所有这些方面” ²¹，使生物设计*不再*“手工化” ²¹，而是变得*更*实用、*更*加速 ⁴。Hie的“达尔文2.0”使命的*成功*，正是使其“潘多拉魔盒”辩护失效的*机制*。他的工作*明确地*旨在使“不切实际”变得*切合实际*。

他辩护中“至少目前是这样” ⁷ 的限定词，是他声明中最令人警醒的部分。它承认了这一辩护具有一个“保质期”——而他自己的研究正在竞相加速这个“保质期”的到来。

---

## V. 治理的风暴：在新的生物安全格局中航行

Evo事件暴露了我们在面对*从头设计*（de novo）威胁时的治理真空。

### **5.1. 监管真空：针对新威胁的过时框架**

当前的治理体系，如国际基因合成联盟（IGSC）的规定 ²³，依赖于DNA合成订单与*已知*病原体数据库的比对筛选。

这一框架现在已经“过时了”（outdated）²³。AI生成的*从头*蛋白质或*从头*病毒 ³，“根据定义，不保证”与“现有的自然蛋白质同源” ²³。那16种有活力的AI噬菌体 ¹ 很可能不会触发IGSC式的筛查警报。

这是一个全球性的失败。研究发现，“94%的国家缺乏管理双重用途生物安全风险的系统” ²²。监管“远远落后”于技术发展 ³²，“政府不能坐等” ³²。

### **5.2. 可行的治理路径：多层次防御框架**

解决这个问题需要一个“多层次的防御” ¹⁰。

**第1层：模型层面治理（上游控制）**

* **问题：** 高能力、“双重用途基础模型” ¹⁴ 的开源 ¹⁰。  
* **建议：** **停止“前沿”基因组模型的开源实践。**  
* **政策：** 实施“模型许可”（Model Licensing）³³。超过特定能力（例如，超过100万上下文窗口、经过*体内*验证的生成能力）的模型的开发者，必须获得训练或发布的许可。模型“不应公开发布” ²⁹，而应通过“限制访问...通过API或其他安全方式” ²⁹ 提供。这允许进行监控、审计和防止“越狱”（jailbreak）³⁰ 攻击。

**第2层：合成层面治理（下游控制）**

* **问题：** 过时的数据库筛选 ²³。  
* **建议：** **强制推行人工智能驱动的*预测性*筛选。**  
* **政策：** DNA合成供应商不仅要检查提交的序列与已知病原体的*同源性*，还必须*使用*预测模型（如Evo自身的预测引擎）来评估其*从头*设计的功能和风险。这是为了“审查新合成的序列” ²³，以识别*新颖*的威胁。

**第3层：机构与社区治理（研究控制）**

* **问题：** 学术规范（例如，“不发表就出局”、开源）与生物安全发生直接冲突 ¹⁰。  
* **建议：** **对所有涉及生成式AI和生物学的交叉研究，强制执行“扩大的双重用途审查”** ³³。  
* **政策：** 资助机构（如FASEB ³⁵）和期刊（如ASM ³⁶）必须要求“透明披露”（transparent disclosure）³⁷ 所使用的所有AI工具。AI*不能*成为作者 ³⁶。研究人员*必须*“验证...AI生成的输出” ³⁹，并对其研究的完整性和*可预见的后果*负责。针对具有大流行潜力的研究的“默认禁止”（default-no）规则 ⁴⁰，必须扩展到*计算机*（in silico）设计阶段。

#### **表3：生成式生物学模型的双重用途风险与治理矩阵**

| 能力 | 良性应用 (达尔文2.0) | 恶意应用 (潘多拉魔盒) | 治理与缓解状态 |
| :---- | :---- | :---- | :---- |
| **1. 零样本功能预测** | 预测BRCA1变异 ¹⁴ | 预测“功能增益”突变 ⁹ | 开放获取 ¹⁴; **未受监管** |
| **2. 多模态协同设计 (蛋白质-RNA)** | 设计CRISPR系统 ¹¹ | 设计新颖的、多组分的毒素递送系统 (见1.2节分析) | 开放获取 ¹⁴; **未受监管** |
| **3. 全基因组生成** | 设计噬菌体鸡尾酒疗法 ¹ | 设计*从头*病原体或“重写”现有病原体 ⁸ | **缓解措施失败** |
| **4. 开源模型权重** | 促进学术合作 ⁴ | 在人类病原体上进行微调 ¹⁰ | 宣称的缓解措施 (数据排除) ¹⁵ -> 状态：失败/易受攻击 ¹⁰ |

结论：  
“达尔文2.0”还是“潘多拉魔盒”？答案是两者皆是。Evo模型代表了生物科学的革命性飞跃。但它在2025年9月的应用，以及其开源所暴露的系统性漏洞 ¹⁰，清楚地表明：潘多拉魔盒不仅已被打开，而且我们已经见证了其主要安全锁（数据排除）的失效。这场“伦理风暴”不仅是媒体的渲染，更是对一个迫切现实的合理回应：即技术的能力已经超越了我们的治理，而将“不切实际”的威胁7变为现实的倒计时已经开始。必须立即采取多层次、有约束力的治理行动。

## 引用的资料

1. Generative design of novel bacteriophages with genome language models - bioRxiv, 访问时间为 2025-11-13， [https://www.biorxiv.org/content/10.1101/2025.09.12.675911v1](https://www.biorxiv.org/content/10.1101/2025.09.12.675911v1)  
2. AI generated its first working genome: a tiny bacteria killer, 访问时间为 2025-11-13， [https://www.sciencenews.org/article/ai-genome-bacteria-phage](https://www.sciencenews.org/article/ai-genome-bacteria-phage)  
3. Inside the debate over a tech breakthrough raising questions about life itself, 访问时间为 2025-11-13， [https://www.washingtonpost.com/science/2025/11/11/ai-designed-viruses-bacteria-life/](https://www.washingtonpost.com/science/2025/11/11/ai-designed-viruses-bacteria-life/)  
4. Generative AI tool marks a milestone in biology | Stanford Report, 访问时间为 2025-11-13， [https://news.stanford.edu/stories/2025/02/generative-ai-tool-marks-a-milestone-in-biology-and-accelerates-the-future-of-life-sciences](https://news.stanford.edu/stories/2025/02/generative-ai-tool-marks-a-milestone-in-biology-and-accelerates-the-future-of-life-sciences)  
5. Evolutionary Design, 访问时间为 2025-11-13， [https://evodesign.org/](https://evodesign.org/)  
6. Welcome Evo, ChatGPT for the Genome - BioQuick News, 访问时间为 2025-11-13， [https://bioquicknews.com/welcome-evo-chatgpt-for-the-genome/](https://bioquicknews.com/welcome-evo-chatgpt-for-the-genome/)  
7. AI can now design more deadly virus genomes - The Register, 访问时间为 2025-11-13， [https://www.theregister.com/2025/09/18/researchers\_just\_created\_a\_working/](https://www.theregister.com/2025/09/18/researchers_just_created_a_working/)  
8. AI-Designed Phages - Asimov Press, 访问时间为 2025-11-13， [https://press.asimov.com/articles/ai-phages](https://press.asimov.com/articles/ai-phages)  
9. AI and biosecurity: The need for governance: Governments should evaluate advanced models and if needed impose safety measures - NIH, 访问时间为 2025-11-13， [https://pmc.ncbi.nlm.nih.gov/articles/PMC12158449/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12158449/)  
10. Opportunities to Strengthen U.S. Biosecurity from AI-Enabled Bioterrorism: What Policymakers Should Know - CSIS, 访问时间为 2025-11-13， [https://www.csis.org/analysis/opportunities-strengthen-us-biosecurity-ai-enabled-bioterrorism-what-policymakers-should](https://www.csis.org/analysis/opportunities-strengthen-us-biosecurity-ai-enabled-bioterrorism-what-policymakers-should)  
11. Sequence modeling and design from molecular to genome scale ..., 访问时间为 2025-11-13， [https://pmc.ncbi.nlm.nih.gov/articles/PMC12057570/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12057570/)  
12. Sequence modeling and design from molecular to genome scale with Evo - PubMed, 访问时间为 2025-11-13， [https://pubmed.ncbi.nlm.nih.gov/39541441/](https://pubmed.ncbi.nlm.nih.gov/39541441/)  
13. Evo: Long-context modeling from molecular to genome scale, 访问时间为 2025-11-13， [https://www.together.ai/blog/evo](https://www.together.ai/blog/evo)  
14. Brian Hie | Genome Modeling & Design Across All Domains of Life | Stanford HAI, 访问时间为 2025-11-13， [https://hai.stanford.edu/events/brian-hie-genome-modeling-design-across-all-domains-of-life](https://hai.stanford.edu/events/brian-hie-genome-modeling-design-across-all-domains-of-life)  
15. Welcome Evo, generative AI for the genome | Stanford University ..., 访问时间为 2025-11-13， [https://engineering.stanford.edu/news/welcome-evo-generative-ai-genome](https://engineering.stanford.edu/news/welcome-evo-generative-ai-genome)  
16. Generative design of novel bacteriophages with genome language models - bioRxiv, 访问时间为 2025-11-13， [https://www.biorxiv.org/content/10.1101/2025.09.12.675911v1.full-text](https://www.biorxiv.org/content/10.1101/2025.09.12.675911v1.full-text)  
17. Genome modeling and design across all domains of life with Evo 2 ..., 访问时间为 2025-11-13， [https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1)  
18. Synthetic biology breakthrough: Scientists use AI to create viable bacteriophages from scratch - International Hospital, 访问时间为 2025-11-13， [https://interhospi.com/synthetic-biology-breakthrough-scientists-use-ai-to-create-viable-bacteriophages-from-scratch/](https://interhospi.com/synthetic-biology-breakthrough-scientists-use-ai-to-create-viable-bacteriophages-from-scratch/)  
19. AI-designed viruses are here and already killing bacteria : r/EverythingScience - Reddit, 访问时间为 2025-11-13， [https://www.reddit.com/r/EverythingScience/comments/1njh8fy/aidesigned\_viruses\_are\_here\_and\_already\_killing/](https://www.reddit.com/r/EverythingScience/comments/1njh8fy/aidesigned_viruses_are_here_and_already_killing/)  
20. Stanford–Arc Team Reports AI-Made Viruses That Kill Bacteria - BiopharmaTrend, 访问时间为 2025-11-13， [https://www.biopharmatrend.com/news/stanfordarc-team-reports-ai-made-viruses-that-kill-bacteria-1383/](https://www.biopharmatrend.com/news/stanfordarc-team-reports-ai-made-viruses-that-kill-bacteria-1383/)  
21. The Poetry Fan Who Taught an LLM to Read and Write DNA | Quanta Magazine, 访问时间为 2025-11-13， [https://www.quantamagazine.org/the-poetry-fan-who-taught-an-llm-to-read-and-write-dna-20250205/](https://www.quantamagazine.org/the-poetry-fan-who-taught-an-llm-to-read-and-write-dna-20250205/)  
22. Generative biology: How can safeguards play catch up? | World Economic Forum, 访问时间为 2025-11-13， [https://www.weforum.org/stories/2025/10/generative-biology-immense-opportunity-how-security-play-catch-up/](https://www.weforum.org/stories/2025/10/generative-biology-immense-opportunity-how-security-play-catch-up/)  
23. Security challenges by AI-assisted protein design: The ability to design proteins in silico could pose a new threat for biosecurity and biosafety - PMC, 访问时间为 2025-11-13， [https://pmc.ncbi.nlm.nih.gov/articles/PMC11094011/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11094011/)  
24. Ethical argument for establishing good manufacturing practice for phage therapy in the UK, 访问时间为 2025-11-13， [https://jme.bmj.com/content/51/5/jme-2023-109423](https://jme.bmj.com/content/51/5/jme-2023-109423)  
25. Hecht Lab finds truncated de novo proteins that act as biological catalysts, 访问时间为 2025-11-13， [https://chemistry.princeton.edu/news/hecht-lab-finds-truncated-de-novo-proteins-that-act-as-catalysts/](https://chemistry.princeton.edu/news/hecht-lab-finds-truncated-de-novo-proteins-that-act-as-catalysts/)  
26. Network Models | Columbia University Department of Systems Biology, 访问时间为 2025-11-13， [https://systemsbiology.columbia.edu/tags/network-models](https://systemsbiology.columbia.edu/tags/network-models)  
27. A Strategy for Combinatorial Cavity Design in De Novo Proteins - PubMed, 访问时间为 2025-11-13， [https://pubmed.ncbi.nlm.nih.gov/31979320/](https://pubmed.ncbi.nlm.nih.gov/31979320/)  
28. Full article: Dual use concerns of generative AI and large language models, 访问时间为 2025-11-13， [https://www.tandfonline.com/doi/full/10.1080/23299460.2024.2304381](https://www.tandfonline.com/doi/full/10.1080/23299460.2024.2304381)  
29. Dual-use capabilities of concern of biological AI models - PMC - NIH, 访问时间为 2025-11-13， [https://pmc.ncbi.nlm.nih.gov/articles/PMC12061118/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12061118/)  
30. Generative AI for Biosciences: Emerging Threats and Roadmap to Biosecurity - arXiv, 访问时间为 2025-11-13， [https://arxiv.org/html/2510.15975v1](https://arxiv.org/html/2510.15975v1)  
31. NIST AI 800-1, Managing Misuse Risk for Dual-Use Foundation Models RFC - Johns Hopkins Center for Health Security, 访问时间为 2025-11-13， [https://centerforhealthsecurity.org/sites/default/files/2024-09/johns-hopkins-center-for-health-security-nist-ai-800-1-rfc-9924.pdf](https://centerforhealthsecurity.org/sites/default/files/2024-09/johns-hopkins-center-for-health-security-nist-ai-800-1-rfc-9924.pdf)  
32. Regulating Under Uncertainty: Governance Options for Generative AI - Cyber Policy Center, 访问时间为 2025-11-13， [https://cyber.fsi.stanford.edu/content/regulating-under-uncertainty-governance-options-generative-ai](https://cyber.fsi.stanford.edu/content/regulating-under-uncertainty-governance-options-generative-ai)  
33. Towards Responsible Governance of Biological Design Tools - arXiv, 访问时间为 2025-11-13， [https://arxiv.org/html/2311.15936](https://arxiv.org/html/2311.15936)  
34. Dual-use capabilities of concern of biological AI models - Research journals - PLOS, 访问时间为 2025-11-13， [https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012975](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012975)  
35. Recommendations for Generative AI in the Biological and Biomedical Sciences - FASEB, 访问时间为 2025-11-13， [https://www.faseb.org/getmedia/f1f19f8c-bca8-4f3d-98e8-a7b323e5274b/GenAI-Task-Force-Report-Accessibility-January-14-2025-25.pdf](https://www.faseb.org/getmedia/f1f19f8c-bca8-4f3d-98e8-a7b323e5274b/GenAI-Task-Force-Report-Accessibility-January-14-2025-25.pdf)  
36. Generative AI - ASM Journals - American Society for Microbiology, 访问时间为 2025-11-13， [https://journals.asm.org/generative-ai](https://journals.asm.org/generative-ai)  
37. RESPONSIBLE USE OF GENERATIVE AI IN RESEARCH Living guidelines on the, 访问时间为 2025-11-13， [https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc\_en?filename=ec\_rtd\_ai-guidelines.pdf](https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en?filename=ec_rtd_ai-guidelines.pdf)  
38. Protecting scientific integrity in an age of generative AI - PNAS, 访问时间为 2025-11-13， [https://www.pnas.org/doi/10.1073/pnas.2407886121](https://www.pnas.org/doi/10.1073/pnas.2407886121)  
39. Ten simple rules for optimal and careful use of generative AI in science - PMC, 访问时间为 2025-11-13， [https://pmc.ncbi.nlm.nih.gov/articles/PMC12561928/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12561928/)  
40. New report urges critical action to address growing biosecurity risks, 访问时间为 2025-11-13， [https://news.stanford.edu/stories/2025/10/securing-biology-biosecurity-risks-threats-report](https://news.stanford.edu/stories/2025/10/securing-biology-biosecurity-risks-threats-report)