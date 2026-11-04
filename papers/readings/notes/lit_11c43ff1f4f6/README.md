# Naeem et al. — RetClean: Retrieval-Based Data Cleaning Using LLMs and Data Lakes

本文是 VLDB 2024 演示论文，介绍 RetClean：用 LLM 填补关系表中的缺失值，支持纯云端 LLM、数据湖检索增强（RAG）+云端 LLM、数据湖检索+本地小模型三种场景，并给出值来源（lineage）。初步结果仅为 4 个数据集、共 318 个元组的准确率表（Table 1）：在领域私有的 QCRI Personnel 上，云端 GPT-3.5 单独填补仅 5%，加数据湖检索后升至 94%（本地 RoBERTa 为 88%）。

注意 v2 标题为 “Using LLMs and Data Lakes”，与批次标题中的 “Foundation Models” 不同，系同一 arXiv 条目的版本改名（阅读者分析）。全文 4 页已全部阅读。

[原文](https://arxiv.org/abs/2303.16909)

版本：arXiv:2303.16909v2（2024-12-17，PVLDB 17(12) 演示论文版本），4 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF p.1 |
| 方法 | §2、§4.1–4.4，PDF pp.2–4 |
| 评测 | §3、§4.5、Table 1，PDF pp.2–4 |
| 局限 | 无独立局限章节；§1 场景动机与 §4.5 结果讨论，PDF pp.1、4 |
