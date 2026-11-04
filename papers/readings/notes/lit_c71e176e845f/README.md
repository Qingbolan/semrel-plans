# Lian et al. — ChatBI: Towards Natural Language to Complex Business Intelligence SQL

ChatBI 是北京邮电大学与百度提出的 NL2BI 系统，面向多轮对话、上百列宽视图和同环比等复杂 BI 查询。系统由三部分组成：小模型多轮对话匹配、把 schema linking 转为单视图选择、"LLM 输出 JSON → 规则模板生成 SQL"的分阶段流程（含虚拟列）。在百度内部构造的 153 条中文 BI 查询上，ChatBI 的有用执行准确率（UEX）为 SRD 74.43%、MRD 67.32%，高于 DIN-SQL 和 MAC-SQL。已通读全文。

[原文](https://arxiv.org/abs/2405.00527)

版本：arXiv:2405.00527v1（2024-05-01），12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1 C1–C3、§2，PDF pp.1–4 |
| 方法 | §3–5、Algorithm 1、Figs.3–6，PDF pp.4–8 |
| 评测 | §6.1–6.3、Tables 2、4–6，PDF pp.7–11 |
| 局限 | §6.4 Discussion，PDF p.11 |
