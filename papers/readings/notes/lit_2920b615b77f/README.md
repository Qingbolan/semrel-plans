# Zhang et al. — ACT-SQL: In-Context Learning for Text-to-SQL with Automatically-Generated Chain-of-Thought

ACT-SQL 是面向 text-to-SQL 的上下文学习方法：对训练样例中 SQL 用到的列、表，用句向量相似度找出问题中最相关的片段，自动生成类似 schema linking 的思维链示例，生成每条 SQL 只调用一次 LLM。在 Spider dev 上，GPT-4 + ACT-SQL 得 EX 82.9、TS 74.5，作者称在当时的上下文学习方法中最高；但在 Spider 鲁棒性变体和多轮数据集 SParC/CoSQL 上提升有限甚至下降。已阅读正文 §1–5、Limitations 和附录 A–B；附录 C 提示模板只抽查。

[原文](https://arxiv.org/abs/2310.17342)

版本：arXiv:2310.17342v1（2023-10-26），32 页（正文 9 页，其余为参考文献与附录提示）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头公式，PDF pp.1–3 |
| 方法 | §3.1–3.4、Figures 1–2，PDF pp.3–5 |
| 评测 | §4、Tables 1–10，PDF pp.5–9；附录 A Tables 11–12、附录 B Table 13，p.12 |
| 局限 | Limitations，PDF p.9；§4.4，p.8 |
