# Giannakouris & Trummer — λ-Tune: Harnessing Large Language Models for Automated Database System Tuning

λ-Tune 让 LLM（GPT-4）根据压缩后的工作负载描述、硬件规格和目标数据库，一次生成完整的配置脚本（系统参数 + 建索引语句），再用带几何增长超时的多轮评测从少数候选中选出最优配置。在 PostgreSQL 与 MySQL 上的 TPC-H、JOB、TPC-DS 共 14 个场景中，其最佳配置相对全局最优的平均代价为 1.41，优于 DB-BERT（1.82）、GPTuner（1.91）、UDO（2.00）等。已阅读预印本全文 14 页。

[原文](https://doi.org/10.1145/3709652)

版本：目录指向 PACMMOD（SIGMOD 2025）正式版 DOI，ACM 页面未能直接下载 PDF；本次阅读作者版 arXiv:2411.03500v1（2024-11-05，标注“author's version… Version of Record published in SIGMOD 2025”），14 页。正式版可能有排版或细节修订。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，PDF pp.1–3 |
| method | §3–§5（Algorithms 1–4、Table 1、Theorems 4.3 与 5.2），PDF pp.3–9 |
| evaluation | §6、Tables 3–5、Figures 3–8，PDF pp.9–13 |
| limitations | 无独立局限一节；§6.3–6.4 与 §8，PDF pp.11–14 |
