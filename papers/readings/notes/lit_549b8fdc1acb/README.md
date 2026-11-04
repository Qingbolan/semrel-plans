# Zhu et al. — AutoTQA: Towards Autonomous Tabular Question Answering through Multi-Agent Large Language Models

AutoTQA 是 PingCAP 与华东师大提出的多智能体表格问答框架：User、Planner、Engineer、Executor、Critic 五个 agent 通过对话协作，Executor 调用 LinguFlow 构建的 text-to-SQL 等工具，经 Trino 数据连接器跨 TiDB、BigQuery、API 等系统访问多表。GPT-4 版在 WikiTQ 上 75.3%，在 PingCAP 计费数据集（多表、约 300 GiB）上 85.0%。已读全文正文；论文无独立局限章节。

[原文](https://www.vldb.org/pvldb/vol17/p3920-zhu.pdf)

版本：PVLDB 17(12): 3920–3933，2024，doi:10.14778/3685800.3685816，14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1，PDF pp.1–3 |
| 方法 | §3–§4，PDF pp.3–8 |
| 评测 | §5、Tables 1–6、Figures 6–7，PDF pp.8–12 |
| 局限 | 无独立章节；§4.3、§5.3–5.5 中的说明，PDF pp.7–8、10–11 |
