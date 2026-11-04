# Heuillet & Peddiraju — CIPHER: A Decoupled Exploration-Selection Framework for Test-Time Scaling of Data Science Agents

本文（AWS，NeurIPS 2026 AABA4ET workshop）提出数据科学 agent CIPHER 及其"解耦探索-选择"（DES）测试时扩展框架：先生成 N 个候选分析计划，选 M<N 个并行执行，再由聚合器汇总。作者在 Infi-DA-Bench（257 个封闭题）和 InsightBench（100 个开放题）上用 Claude 4.5 Haiku 与 DeepSeek-V3.2 两套模型扫描 48 种设计。结论：生成方式（双提示 Ensemble，+3.36pp）和聚合器容量（+0.46pp）有效，选择策略与随机选择无可分辨差别；参考配置与专用基线 DataWise、Agent-Poirot 相差约 1.2pp 以内。已读正文与附录 A–F。

[原文](https://arxiv.org/abs/2607.14386)

版本：arXiv:2607.14386v2（2026-10-26），17 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，附录 B，PDF pp.1–2、8–9 |
| method | §2–3、Algorithm 1、附录 C，PDF pp.2–4、10–11 |
| evaluation | §4、Tables 1–3，附录 D（Tables 5–9），PDF pp.4–5、11–17 |
| limitations | 附录 F，PDF p.14 |
