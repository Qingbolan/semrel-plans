# Zhao, Agrawal, El Abbadi — Hybrid Querying Over Relational Databases and Large Language Models

本文提出 SWAN，一个“超出数据库”（beyond-database）问题的混合查询基准：从 BIRD 的 4 个库中删除列或表，使 120 道问题（每库 30 道）无法仅靠库内数据回答，金标准为原 BIRD 金 SQL 在原库上的执行结果。论文给出两种基线：HQDL（模式扩展后由 LLM 逐行补全缺失数据再执行普通 SQL）与基于 BlendSQL 的混合查询 UDF。GPT-4 Turbo 5-shot 的 HQDL 最高执行准确率 40.0%、数据事实性 F1 48.2%。已阅读全文 8 页。

[原文](https://arxiv.org/abs/2408.00884)

版本：arXiv:2408.00884v2（2024-11-15），8 页，PDF 仍为 ACM 模板占位页眉（“Conference acronym 'XX”），不是 CIDR 2025 出版排版；批次 venue 记为 CIDR 2025。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、Figure 1，PDF pp.1–2；§2，p.2 |
| method | §3 SWAN 构建（Table 1），pp.2–3；§4.1 HQDL、§4.2 混合查询 UDF，pp.3–4 |
| evaluation | §5、Table 2–5，PDF pp.5–7 |
| limitations | §4.3 优化机会，pp.4–5；§6 结论与未来工作，p.7 |
