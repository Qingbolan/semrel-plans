# usecase

原文给出的应用是数据库管理和知识图谱：先用 DrugProt NER 标注器在摘要中标出化学物和基因/蛋白提及，再运行关系抽取系统，输出 (PMID, 关系类型, CHEMICAL, GENE) 元组，合并到加权的二部有向图中；用户可按关系类型取子图，或按各 run 的测试集精确率过滤。示例：antagonist 子图有 95,812 个节点、274,401 条边，聚类系数 0.04、同配系数 −0.1，最大连通分量 92,267 个节点；讨论部分还从全 PubMed 图谱中抽出与生物材料相关的 part-of/inhibitor/activator 网络（Figure 19）。

阅读者分析：若项目把这一场景转成语义查询（例如"找出被某化学物抑制的所有基因"），应保留实体提及未归一化、边权来自测试集精确率而非单条边的正确率、只覆盖摘要等边界；这些是项目派生用法，原文未评测这种查询的准确率。

依据：[Miranda-Escalada et al., Database 2023, baad080，JATS 全文](https://doi.org/10.1093/database/baad080)，Results：DrugProt Large Scale Silver Standard Knowledge Graph；Discussion、Figure 19。
