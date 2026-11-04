# Kim — When Plans Change Answers: Formalizing Cost–Accuracy Optimization for Semantic Queries

这是一篇理论/形式化论文：在语义查询引擎中，谓词由模型判定，不同物理计划会返回不同答案。作者以校准置信度为起点，按每个决策对输出的贡献（最简单情形为 fan-out）加权，在无标注情况下预测计划的输出级召回/精确率，并把输出级目标反向推成每个元组的“误差价格”；在此基础上给出计划等价层级、复杂度结果和逐元组拉格朗日分解。实验仅为合成工作负载上的模拟，作者明确说明真实引擎评测留待未来。已通读 §1–§11 正文（参考文献未逐条核对）。

[原文](https://arxiv.org/abs/2610.08089)

版本：arXiv:2610.08089v2（2026-10-08），31 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Table 1，PDF pp.1–4 |
| method | §2–§8，PDF pp.4–20 |
| evaluation | §9（E1–E6）、Tables 5–9、Figures 5–8，PDF pp.20–25 |
| limitations | §9 Limitations、§11 Open Problems，PDF pp.25、28 |
