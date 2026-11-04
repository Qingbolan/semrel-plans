# usecase

原文附录 B.1 给出一个完整标注示例（Doc#45，评论，在家上学话题，PDF p.44）：

- 原文先诉诸情感：“剥夺孩子的基础教育是一种虐待儿童……”，标为 pathos（appeal to emotion）。
- claim：“Home schooling should be illegal”，紧跟 rebuttal：“除非家长能证明提供与公立学校同等水平的教育”。
- premise：在复杂的全球技术社会中，所有人都需要对科学、技术与文化有基本理解。
- 第二个 claim：“我看不出任何孩子有在家上学的必要”，rebuttal：“除非孩子有特殊需要或学习困难”；另一个 premise 批评美国公立教育。
- 标注者还为每个成分写了一句概括（如 “Science and technology are not taught in HS”）。

结合 Figure 2（PDF p.3），预期用途是：对某个争议话题，按“支持/反对”列出各篇文档中的理由，让用户快速看到论证要点。

阅读者分析（项目派生，非原文评测）：若在本项目中把它当作“从评论中抽取 claim/premise”的语义抽取任务，应保留两步结构（先过滤说服性文档，再抽成分），并注意原文自动系统只在句子级预测，rebuttal/refutation 几乎识别不出来。

依据：[Computational Linguistics 43(1):125–179, 2017（ACL Anthology J17-1004），55 页](https://aclanthology.org/J17-1004)。
