# Zhou, Sun, Li — DB-GPT: Large Language Model Meets Database

这是清华数据库组的愿景论文（vision paper）：提出用 LLM 优化数据库任务的框架 DB-GPT，分为三条路线——自动生成输入提示、面向数据库任务的微调、数据库专用 LLM 的设计与预训练，每条路线给出挑战和设想。初步实践只验证了第一条路线：在 12 条查询的改写和 IMDB 索引调优上与 PostgreSQL 比较，作者报告改写效果比 PostgreSQL 改写器好 9.8% 和 22.4%。已通读全文 10 页正文；Fig. 4 的柱状图未逐值核对。注意：本文与 eosphoros-ai 的同名开源项目 “DB-GPT” 不是同一工作（阅读者分析）。

[原文](https://link.springer.com/article/10.1007/s41019-023-00235-6)

版本：Data Science and Engineering，DOI 10.1007/s41019-023-00235-6（PDF 未印卷期；OpenAlex 记为 9(1):102–111，2024；CC BY 4.0），出版社排版 PDF，由作者组主页 dbgroup.cs.tsinghua.edu.cn 获取（Springer 直链被浏览器验证拦截），10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1（C1–C3 三类挑战），pp.1–2 |
| 方法 | §2.1–2.4（Challenge/Vision 1–8），Table 1、Fig. 2–3，pp.3–7 |
| 评测 | §3（3.1 实现、3.2 查询改写与索引调优），Fig. 4，pp.7–8 |
| 局限 | §3 中两段 Limitations 与总结段，p.8 |
