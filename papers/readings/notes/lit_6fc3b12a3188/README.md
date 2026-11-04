# Trummer — Implementing Semantic Join Operators Efficiently

本文研究用自然语言描述连接条件的语义 θ-join，提出把两表各一批行放进同一个提示、让 LLM 直接输出匹配下标对的块嵌套循环连接，并给出按 token 计费的代价模型、已知选择率下的最优批大小公式，以及未知选择率时按溢出逐步放大估计的自适应连接。GPT-4 实验覆盖 3 个小规模场景，块连接比逐对比较的元组连接费用低若干数量级；Emails 场景中自适应连接的 F1 高于元组连接和 LOTUS。已阅读全文（正文 §1–9），Figure 6/7 与 Table 2 经渲染 p.11 核对。

[原文](https://arxiv.org/abs/2510.08489)

版本：arXiv:2510.08489v1（2025-10-09），13 页（ACM 模板，会议信息为占位符，未标注正式发表处）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–3 |
| method | §3–6，Algorithms 1–3、Figures 1–4，PDF pp.3–9 |
| evaluation | §7、Table 2、Figures 5–7，PDF pp.9–12；p.11 已渲染核对 |
| limitations | 无独立局限章节；§7.3 与 §8 中的讨论，PDF pp.11–12 |
