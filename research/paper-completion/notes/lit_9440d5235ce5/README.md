# Chai, Li, Deng, Zhong, Yuan, Wang, Cao — Doctopus: Budget-aware Structural Table Extraction from Unstructured Documents

Doctopus 在用户给定的 LLM token 预算下，从非结构化文档集合中抽取一张“每文档一行、每属性一列”的表：先切块建 PQ 向量索引并用参考句增强属性查询，只把相关块交给 LLM；再把每个候选策略（OpenIE6、Evaporate 代码生成、DebertaV3、不同块组合的 GPT-4o）的质量估计为“包含概率 × 抽取概率”；最后用分组背包动态规划为每个（文档，属性）选择策略。

论文在自建的 4 个数据集（共 3,200 份文档，人工核验约 1,000 小时）上报告：同成本下准确率提升 11%，同准确率下成本降低 2.7 倍。已阅读正文全部；NP-hard 证明与候选剪枝在技术报告中，未阅读。

[原文](https://www.vldb.org/pvldb/vol18/p3695-chai.pdf)

版本：PVLDB Vol.18 No.11，pp.3695–3707（2025），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，pp.1–4 |
| method | §3–§6，Algs.1–2、Fig.2，pp.4–8 |
| evaluation | §7，Figs.3–11，pp.8–12 |
| limitations | §9 结论段，p.12；§7.1 Remark，p.10 |
