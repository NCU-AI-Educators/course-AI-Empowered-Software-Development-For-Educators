## module1_lesson1: 我们的学习路径概览

这是一个从思想到工具，再到创造的完整旅程。

<div class="mermaid">

%%{init: {'theme': 'base'}}%%
graph LR
    subgraph 123["模块 1-3: 基础能力"]
        direction TB
        A[模块1: 思想破冰]
        B[模块2: 编程基础]
        C[模块3: 代码复用与调试]
        A --> B --> C
    end
    subgraph 456["模块 4-6: 核心应用"]
        direction TB
        D[模块4: 数据处理]
        E[模块5: 数据可视化]
        F[模块6: Web应用基础]
        D --> E --> F
    end
    subgraph 78["模块 7-8: 综合与创新"]
        direction TB
        G[模块7: 综合项目开发]
        H[模块8: 成果转化与教学]
        G --> H
    end 
    123 --> 456
    456 --> 78
    
    classDef nodeStyle fill:#fff,stroke:#bbb,stroke-width:1px,color:#333
    class A,B,C,D,E,F,G,H nodeStyle

    style 123 fill:#f5f5f5,stroke:#ddd
    style 456 fill:#f5f5f5,stroke:#ddd
    style 78 fill:#f5f5f5,stroke:#ddd

    linkStyle 5 stroke:#333,stroke-width:2px
    linkStyle 6 stroke:#333,stroke-width:2px

</div> 


### module1_lesson3:**所有程序的“秘密配方”**

祝贺你，刚刚你不仅创造了一个应用，更在不经意间，实践了所有程序开发共同的“秘密配方”！

让我们回顾一下“随机点名器”的工作过程：

<div class="mermaid">

graph LR
    subgraph "我们的点名器"
        direction LR
        A["<b style='font-size:16px'>学生名单.txt</b><br/>(输入/原料)"]
        B["<b style='font-size:18px'>点名器.html</b><br/>(处理/配方)"]
        C["<b style='font-size:16px'>最终显示的名字</b><br/>(输出/成品)"]
        A --> B --> C
    end
    
</div> 

## module1_lesson3: 你已掌握AI应用开发的核心！

通过今天的练习，你已经体验了AI时代全新的软件开发模式：

<div class="mermaid">

graph LR
    A(1. 提出创意与需求) --> B(2. AI生成应用原型);
    B --> C(3. 测试与评估);
    C --> D(4. 提出优化指令);
    D --> B;

</div>