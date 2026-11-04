# Holzenberger, Blair-Stanek & Van Durme — A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering

本文提出 SARA（StAtutory Reasoning Assessment）：从美国《国内税收法典》（IRC）选取并简化 9 个条文，人工编写 276 个蕴含案例（176 训练、100 测试）和 100 个应纳税额数值题（80/20），并配套 147M token 税法语料、税法词向量和 Legal BERT。手写 Prolog 求解器在全部案例上达到 100%，而 BERT 与前馈基线在测试集上与多数类/常数基线相当（蕴含约 47–55%），且去掉法条后性能几乎不变。已通读正文 §1–7 并渲染核对 Table 5。

[原文](https://ceur-ws.org/Vol-2645/paper5.pdf)

版本：Proceedings of the 2020 Natural Legal Language Processing (NLLP) Workshop（KDD 2020 同期），CEUR-WS Vol-2645 paper5，8 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题（problem） | 摘要、§1、§2.1，PDF pp.1–2 |
| 方法（method） | §2 数据构造、§3 Prolog 求解器、§4 法律语料与模型、§5.1–5.2，PDF pp.2–5 |
| 评测（evaluation） | §5.3、Table 5（已渲染核对），PDF p.5 |
| 局限（limitations） | §2.1 简化说明、§2.2 任务边界、§3.2 Prolog 三项局限、§7，PDF pp.2–4、6 |
