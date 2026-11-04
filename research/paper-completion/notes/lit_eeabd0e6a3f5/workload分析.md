# 工作负载

DBMS：MySQL 5.7（582 个 knob）与 PostgreSQL 12.0（202 个 knob）（§6.1，PDF p.9）。

| 数据集 | 测试 | 训练 | 历史问题 \|Q\| | 手册 \|M\| | 测试 knob 覆盖 | 类型 |
|---|---|---|---|---|---|---|
| MySQL SO | 174 | 620 | 1,632 | 3,506 | 30% | NL |
| MySQL Forum | 49 | 620 | 1,632 | 3,506 | 17% | NL |
| PG SO | 57 | 114 | 402 | 756 | 38% | NL |
| MySQL Run | 100 | 620 | 1,632 | 3,506 | 15% | Runnable |

（Table 1，PDF p.10）NL 数据来自 StackOverflow 和 MySQL 社区，每个数据集按 7:2:1 切分为历史问题、训练和测试；MySQL SO 与 Forum 的历史问题合并。标签由正则从采纳答案或评论中抽取，作者称抽样人工核验准确，但未给核验数量。

MySQL Run 测试集为 70 个可复现环境的真实问题加 30 个人工设计问题（PDF p.9）。遥测用 Prometheus 采集 557 个指标，间隔 1 秒；向量库为 Faiss，MySQL 5,138 个、PG 1,158 个 768 维向量（PDF p.10）。

阅读者分析：MySQL Run 中 30 个问题由作者设计，且 SuccessRate 由专家判定，未报告专家人数与一致性；测试规模较小（49–174 题）。

依据：§6.1、Table 1，PDF pp.9–10。
