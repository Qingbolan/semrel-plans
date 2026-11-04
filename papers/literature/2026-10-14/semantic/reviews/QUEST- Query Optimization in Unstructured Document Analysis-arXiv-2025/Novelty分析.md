# Novelty分析

QUEST把优化决定下沉到document instance：便宜且能提前拒绝记录的属性先抽取；join产生的候选key也参与过滤顺序。与只缩小模型或只做检索不同，它同时优化每次调用的token和需要调用的次数（§2–4）。

需要保留的条件：两级检索与证据聚类可能遗漏信息；selectivity由样本估计；论文的join支配结论依赖建模假设。多表选择只在当前left-deep扩展中做适应性决策，不是任意图的全局最优枚举。

§2.4提到跨查询缓存和并发“可支持”，同时明确多查询优化和benchmark超出本文范围。因此不能标成已验证multi-query batching系统。

来源：[QUEST: Query Optimization in Unstructured Document Analysis](https://arxiv.org/abs/2507.06515v2)。
