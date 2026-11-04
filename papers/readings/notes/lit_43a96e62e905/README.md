# Jiang et al. — Active Retrieval Augmented Generation

本文提出“主动检索增强生成”的统一框架，即在生成过程中主动决定何时检索、检索什么，并实现 FLARE：先生成一个临时的下一句，若其中有低概率 token，就用该句（遮盖低置信词或改写为问题）作查询检索文档，再重新生成该句。基于 text-davinci-003，在 2WikiMultihopQA、StrategyQA、ASQA（含 ASQA-hint）、WikiAsp 四个长输出任务上，FLARE 均优于单次检索和多次被动检索基线；多跳 QA 上 EM 51.0，单次检索为 39.4。已阅读正文 §1–9 与附录 A–C；附录 D 提示只抽查。

[原文](https://arxiv.org/abs/2305.06983)

版本：arXiv:2305.06983v2（2023-10-22），24 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3（3.1 FLARE-instruct，3.2 FLARE-direct，3.3 实现），PDF pp.3–5；附录 A，p.14 |
| 评测 | §4–6、Tables 1–6、Figures 4–5，PDF pp.5–9；附录 B–C、Tables 7–9，pp.14–16 |
| 局限 | §9 Limitations，PDF p.9；附录 A Efficiency，p.14 |
