# Abacus: A Cost-Based Optimizer for Semantic Operator Systems

语义算子程序（LLM 驱动的 map、filter、join 等）中的每个算子都有成千上万种物理实现（换模型、Mixture-of-Agents 集成、缩减上下文、Critique-and-Refine 等）。已有优化器（LOTUS、DocETL）基本只优化质量，不能在费用或延迟约束下取舍。Abacus 在 Palimpzest 中实现：先用面向 Pareto 前沿的多臂老虎机（MAB）在少量验证样本上测算子的质量、费用和延迟，再用 Pareto-Cascades 动态规划在约束下选出整条计划。

以“最大化质量”为目标，在 BioDEX、CUAD、MMQA 上，Abacus 的质量比次优系统分别高 20.8%、39.4%、6.7%，平均便宜 10.8 倍、快 3.4 倍（摘要与 §1；与 Table 2 一致，但 §4.3 正文给出另一组数字，见“评测与边界”）。

[原文](https://arxiv.org/abs/2505.14661v3)

版本：Russo, Liu, Sudhir, Vitagliano, Cafarella, Kraska, Madden（MIT），PVLDB 19(5):1060–1073, 2026；核对所用全文为 arXiv 2505.14661v3（2026-02-03，带 PVLDB 版头，14 页）。已通读 §1–7、Tables 1–3、Figures 1–8，数字已对照全文核查；未复现实验。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2.2–2.3，PDF pp.1–5 |
| method | §3.1–3.3、Algorithms 1–5，pp.5–7；§4.1 实现规则，p.8 |
| evaluation | §4.2–4.6、Tables 2–3、Figures 6–8，pp.8–11 |
| limitations | §5（算子依赖、顺序 MAB 采样），p.12 |
