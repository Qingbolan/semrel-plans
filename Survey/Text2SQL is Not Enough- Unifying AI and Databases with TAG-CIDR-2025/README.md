# Text2SQL is Not Enough: Unifying AI and Databases with TAG

很多真实的数据库自然语言问题既要精确计算，又要语言模型的语义推理或世界知识（如“硅谷地区的学校”“最讽刺的评论”）；Text2SQL 只能表达有关系等价物的问题，RAG 只能检索少量行再调用一次模型。Biswal、Patel 等人提出表增强生成（TAG）范式：查询合成 syn(R) → Q、查询执行 exec(Q) → T、答案生成 gen(R, T) → A，并把 Text2SQL 与 RAG 视为其特例。

作者把 BIRD 的 80 个问题改写为需要世界知识或推理的版本，构建首个 TAG 基准。在 60 个非聚合问题上，基线的精确匹配率都不超过 20%，而用 LOTUS 手写的 TAG 管道达到 55%，平均耗时 2.94 秒。手写管道使用了专家的 schema 知识，是上界式参照，不是自动系统。

[原文](https://vldb.org/cidrdb/papers/2025/p11-biswal.pdf)

版本：CIDR 2025（Amsterdam）正式论文，PDF 10 页。2026-10-14 阅读正文 §1–6、Tables 1–2 与附录 A–C；2026-11 复核全部数字；未复现实验。
