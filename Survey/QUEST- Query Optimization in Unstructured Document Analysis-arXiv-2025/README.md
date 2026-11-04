# Sun, Deng, Chai et al.（北京理工 / U. Arizona / MIT）— QUEST: Query Optimization in Unstructured Document Analysis

在用 LLM 从文档中抽取属性再做 SQL 式分析的系统里，抽取是主要成本。QUEST 针对 SPJ 查询从两方面降本：用文档级 + 片段级两级索引和样本“证据”只把相关片段喂给 LLM，降低每次抽取的 token；在执行时逐文档决定过滤顺序（按选择率与该文档上的抽取代价），并把 join 转成 IN 过滤参与排序，减少抽取次数。

在 LCR、WikiText、SWDE 共 500 篇文档、50 条查询上，QUEST 的每文档 token 比 ZenDB/PZ/RAG/LOTUS 低（摘要称节省 30%–6 倍），F1 与 LOTUS 接近，在长文档 LCR 上 0.72 对 LOTUS 0.45。

[原文](https://arxiv.org/abs/2507.06515v2)

版本：arXiv 2507.06515v2（2025-07-11，cs.DB），14 页。2026-10-14 通读正文 §1–6、表 1–3、图 1–8，第 11 页表 2–3 已渲染核对；2026-11 按本地全文（research/2026-10-14/semantic/pdfs/quest.pdf）重新核对数字。未复现实验。
