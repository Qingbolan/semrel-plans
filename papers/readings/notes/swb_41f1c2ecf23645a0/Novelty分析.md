# novelty

原文声明的贡献：(1) 5,000 篇摘要的 DrugProt 金标准，含 24,526 条关系和 127,336 个实体，作者称其为最大的带文本跨度的化学物–蛋白交互人工语料；(2) 首个生物医学 NLP 大规模赛道，检验系统在约 236 万摘要上的可扩展性；(3) 融合参赛预测生成的银标准知识图谱（53,993,602 节点、19,367,406 条边、146,864,121 条预测），每条预测附带该 run 在测试集上的 micro 精确率，可用于过滤或加权；(4) CodaLab 持续评测与公开评测库；(5) 用金标准训练的 NER 标注器（CEM 精确匹配 F1 92.38、GPRO 90.34）及全 PubMed（2021-12）的关系标注。

阅读者评估：这是数据与评测基础设施论文，不提出新模型。节点数恰好等于 33,578,479 GPRO + 20,415,123 CEM 提及数，说明图谱节点是"提及"而非归一化后的实体；原文也把实体归一化列为后续工作，因此该图谱不能直接当作去重的化学物–基因概念图。大规模赛道只比较 F1，不比较同等硬件下的耗时，原文讨论部分也承认这一点。

依据：[Miranda-Escalada et al., Database 2023, baad080，JATS 全文](https://doi.org/10.1093/database/baad080)，Abstract、Introduction、Results：Large Scale corpus 与 Silver Standard Knowledge Graph、Table 3、Discussion。
