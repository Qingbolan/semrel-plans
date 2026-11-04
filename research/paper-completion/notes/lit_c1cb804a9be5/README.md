# Singh et al. — Panda: Performance Debugging for Databases using LLM Agents

Panda 是 AWS 提出的数据库性能排障助手框架：把用户的自然语言排障问题，与检索到的排障文档、历史工单、遥测特征和 SQL/schema 上下文拼接后交给 GPT-3.5，并加入问题过滤、答案校验、来源引用、影响估计和用户反馈。论文只做了 50 条人工设计问题、3 名不同水平 DBE 的成对偏好研究，Panda 在信任和有用性上明显优于直接问 GPT-4（高级 DBE 在 50 题中有 47 题认为 Panda 更可信、47 题认为更有用，Table 1）。全文 6 页均已阅读，含四张表；未复现实验。

[原文](https://www.vldb.org/cidrdb/papers/2024/p6-singh.pdf)

版本：CIDR 2024 论文 PDF（p6-singh），6 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1、Figure 1，PDF pp.1–3 |
| 方法 | §2（2.1–2.5）、Figure 2，PDF pp.2–4 |
| 评测 | §3、Tables 1–4，PDF pp.3–5 |
| 局限 | §3 末段、§4 Research Directions，PDF pp.5–6 |

PDF 仍保留 ACM 模板占位符（“Conference acronym ’XX … 2018”、页眉“Trovato and Tobin”），引用时应以 CIDR 2024 为准（阅读者分析）。
