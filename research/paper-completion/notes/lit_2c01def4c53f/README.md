# Wang et al. — MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL

MAC-SQL 把 Text-to-SQL 拆给三个 LLM 智能体：Selector 在大库上裁剪出子 schema，Decomposer 用少样本思维链把问题拆成子问题并逐步生成 SQL，Refiner 执行 SQL 并依据报错修正。以 GPT-4 为骨干在 BIRD 隐藏测试集上执行准确率 59.59（写作时 SOTA）；另用其智能体数据微调 Code Llama 7B 得到 SQL-Llama。已阅读正文 §1–7、Limitations 及附录 A–C（实现细节、提示、错误类型）。

[原文](https://arxiv.org/abs/2312.11242)

版本：arXiv:2312.11242v6（2025-03-18），18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。Table 1 已渲染核对。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2，pp.1–3 |
| 方法 | §3（Algorithm 1、Figures 2–4）、§4，pp.2–5；附录 A–B，pp.11–17 |
| 评测 | §5、Tables 1–4、Figure 5，pp.5–8；附录 C、Figure 6，p.18 |
| 局限 | Limitations，p.9；附录 A.3，p.11 |
