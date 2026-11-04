# Dai et al. — UQE: A Query Engine for Unstructured Databases

本文提出 UQE：接受 UQL（在 SELECT、WHERE、GROUP BY 中允许自然语言描述的 SQL 方言），把 LLM 当作逐行语义判断器。系统用基于嵌入聚类的分层抽样对聚合做无偏估计，以在线主动学习替代"索引"进行检索，并用编译器式规划把子句排序、融合为最少的 LLM 调用。在 IMDB、ABCD、AirDialog、Clevr 上，条件计数的相对误差和语义检索 F1 都明显优于长上下文 LLM 与同预算 UDF 基线，每查询成本约 $0.01–0.20。已阅读正文 §1–7 与附录 B–C 的数据设置；附录 D 的全部查询文本未逐条核对。

[原文](https://arxiv.org/abs/2407.09522)

版本：arXiv:2407.09522v2（2024-11-17，NeurIPS 2024），32 页（正文 10 页）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2（术语与三类分析任务）、§3 UQL，PDF pp.1–4 |
| 方法 | §4.1 抽样"索引"（Prop 1、Algorithms 1–2）、§4.2 编译与内核，PDF pp.4–6 |
| 评测 | §6、Tables 1–5、Figures 4–5，PDF pp.7–10；附录 C.1–C.2、Table 6，PDF pp.17–18 |
| 局限 | §3 Assumptions、§4.1 Extension、§7 Conclusion，PDF pp.4–5、10 |
