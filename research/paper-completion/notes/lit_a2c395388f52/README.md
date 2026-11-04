# Mang, Xiang et al. — PLOP: Cost-Based Placement of Semantic Operators in Hybrid Query Plans

PLOP 是在 DuckDB 中实现的计划级优化器，决定语义算子在语义–关系混合计划中的位置，以最小化 LLM 调用数加 α 倍关系处理行数。它先上拉语义投影、把语义连接分解为叉积上的语义过滤，从而把问题化归为语义过滤器的放置；证明在函数缓存下全部上拉可使 LLM 调用最少；再用 DP 代价模型权衡关系代价。在 30 条自建混合查询上，PLOP-Cost 相对 DuckDB+Cache 的几何平均加速为 1.50×、成本降低 4.18×，平均 F1≈0.85；在 SemBench E-Commerce 14 条查询上质量为 0.840。已读全文（pp.1–12）。

[原文](https://arxiv.org/abs/2604.09944)

版本：arXiv:2604.09944v2（2026-04-24），13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，Listing 1、Figure 1，PDF pp.1–4 |
| method | §2、§4–5，Algorithms 1–2、Theorems 4.1–4.3，PDF pp.3–7 |
| evaluation | §6、Tables 1–3、Figures 5–9，PDF pp.7–11 |
| limitations | §3.2 问题简化、§5 固定选择率、§7 准确性讨论，PDF pp.3、7、11–12；无专门局限节 |
