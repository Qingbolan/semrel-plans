# Naser Moghadasi & Ghaderi — Agentic Cost-Aware Query Planning with Knowledge Distillation for Big Data Analytics

本文提出一个“智能体式”查询规划系统：规则化 teacher 生成 6 种改写策略组合的 SQL 计划，UCB1 bandit 在内存/延迟约束下探索，随机森林预测延迟，最后把 teacher-bandit 的选择蒸馏到逻辑回归或直方图梯度提升 student。在 NYC Taxi 与 IMDB 上，完整系统中位延迟 251.8ms，对比 DuckDB 默认 340.2ms，约束满足率从 72.3% 升至 96.1%。论文仅 6 页，已全文阅读；实验细节（查询实例数、硬件、重复次数）原文未给出，且正文数字存在若干不一致（见 benchmark）。

[原文](https://arxiv.org/abs/2605.17831)

版本：arXiv:2605.17831v1（cs.LG，2026-05-18），6 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§I、§III-A，PDF pp.1–2 |
| method | §III-B、§III-C，PDF pp.2–3 |
| evaluation | §IV、Tables II–VI、Figs 2–4，PDF pp.3–5 |
| limitations | §V-B，PDF p.5 |
