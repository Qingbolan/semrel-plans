# Zimmerer et al. — SemCEB: A Cardinality Estimation Benchmark for Semantic Operators

本文提出 SemCEB，号称首个面向语义算子（语义过滤与语义连接）基数估计的基准：基于 Amazon Reviews 2023“Arts, Crafts and Sewing”类的多模态两表数据（45k 商品、936k 评论），102 条手写查询（62 过滤、40 连接），按准确率（q-error）、成本、延迟和内存评估估计器。初步评测显示均匀采样稳健但昂贵且不可扩展；改编的 Semantic Histograms 只能覆盖 31 条单列过滤，q-error 明显更差但约 6 s 即可估计。已阅读全文（7 页，正文 6 页），并渲染核对 p.6 的 Figure 5–6。

[原文](https://arxiv.org/abs/2606.23081)

版本：arXiv:2606.23081v1（2026-06-22），VLDB 2026 Workshop NOVAS，7 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1（含 Figure 1 动机实验与“经典方法为何不足”），PDF pp.1–2 |
| method | §3 基准框架、§3.1 数据集（嵌入、语义倾斜）、§3.2 查询与 Table 1，PDF pp.3–5 |
| evaluation | §4 指标、基线、结果，Figure 4–6，PDF pp.5–6；Figure 5–6 已渲染核对 |
| limitations | §5，PDF p.6；§3 关于单算子查询形状与模型相关真值的说明，p.3 |
