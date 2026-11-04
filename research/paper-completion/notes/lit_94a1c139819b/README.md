# Lei, Chen et al. — Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows

Spider 2.0 是面向企业级数据工作流的 text-to-SQL 评测：632 个任务来自真实教程、论坛和 DBT 项目，数据库部署在 BigQuery、Snowflake、SQLite、DuckDB、PostgreSQL、ClickHouse 上，平均每库约 744 列，金标准 SQL 平均约 148 个 token。

完整版是代码智能体设定（需浏览代码库、文档并与数据库交互），另有只输出 SQL 的 Spider 2.0-lite（547 例）与 Spider 2.0-snow（547 例，全在 Snowflake）。最好的 Spider-Agent + o1-preview 在 Spider 2.0 上成功率仅 21.36%，传统 text-to-SQL 方法在 lite 上最高 EX 仅 5.68%（Tables 5–6）。已阅读正文 §1–5 及附录 A、C 部分；未逐一阅读全部案例图。

[原文](https://arxiv.org/abs/2411.07763)

版本：arXiv:2411.07763v2（2025-03-17，ICLR 2025 会议版排版），45 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1、Figs. 1–2，PDF pp.1–3 |
| 方法（基准构造） | §2.2–2.3、Tables 1–3，PDF pp.3–6；附录 A 评测脚本，pp.15–16 |
| 评测 | §3–4、Tables 4–11、Figs. 4–5，PDF pp.6–10；附录 Tables 20–21，pp.38–39；p.9 已渲染核对 |
| 局限 | 无独立局限节；§4 分析、附录 A 评测口径讨论，PDF pp.8–10、15 |
