# Balaka et al. — Pneuma: Leveraging LLMs for Tabular Data Representation and Retrieval in an End-to-End System

Pneuma 是一个面向“表发现”的检索增强系统：用户用自然语言提问，系统从表集合中返回相关表的排序。离线阶段用 LLM 叙述列含义、再拼接 5 条抽样行形成内容摘要；在线阶段结合 BM25、向量检索和“LLM 判官”二分类重排。作者用自建的基准生成器在 5 个数据集上生成内容/上下文问题，并外加 BIRD；k=1 时 Pneuma 在所有报告场景中命中率最高。已阅读正文 §1–9；未逐项审计所有图中数值。

[原文](https://doi.org/10.1145/3725337)

版本：arXiv:2504.09207v1（2025-04-12），页眉为 PACMMOD Vol.3 No.3 (SIGMOD) Article 200，28 页；目录链接为 ACM DOI，实际保存的是作者在 arXiv 上的同名版本。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–5 |
| 方法 | §3–5，Fig. 2–4，PDF pp.5–10 |
| 评测 | §6–7，Table 1–2，Fig. 6–19，PDF pp.10–22 |
| 局限 | 无独立章节；§1、§5.2、§7.4.5，PDF pp.3、9–10、22 |
