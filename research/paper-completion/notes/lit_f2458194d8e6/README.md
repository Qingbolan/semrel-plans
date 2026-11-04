# Gao, Luo — Automatic Database Description Generation for Text-to-SQL

阿里巴巴的短技术报告，在缺少表/列注释时为 Text-to-SQL 自动生成数据库描述：先由整库 schema 识别领域，逐表理解，再按 Code/Enum/DateTime/Text/度量对列分类并对比同类列，生成不超过 20 词的列描述，最后自底向上生成不超过 100 词的表描述。在 BIRD dev（不使用 evidence）上，三个开源 SQL 生成模型的执行准确率平均提高约 0.93 个百分点，人工描述平均提高约 2.33 个百分点。全文已读。

[原文](https://arxiv.org/abs/2502.20657)

版本：arXiv:2502.20657v1（2025-02-28，技术报告），5 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，PDF pp.1–2 |
| method | §2.1–2.5、Fig.1，PDF pp.2–3 |
| evaluation | §3、Table 1、Fig.2，PDF pp.3–5 |
| limitations | §3–4（无独立局限节），PDF pp.4 |
