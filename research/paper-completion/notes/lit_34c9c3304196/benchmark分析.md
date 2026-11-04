# 评测与边界

**基线**（§8.1.2，p.8）：SMAC、HEBO、CDBTune（最多 100 轮）；三者各加代价模型；随机采样 100 万配置 + 代价模型；迁移方法——工作负载映射（OtterTune 式，接 HEBO/SMAC）、模型集成（ResTune 式）、模型预训练（QTune 式，接 CDBTune，有/无在线调优）、knob 剪枝（OpAdviser、DB-BERT、GPTuner）。迁移方法使用与 E2ETune 相同的历史调优数据。

**实验 1（同 schema）**（Figure 3a，p.9）：E2ETune 在全部十个基准上调优时间最短；在 JOB、SSB-flat、Twitter、Smallbank 上性能最优，在 TPC-H、SSB、TPC-DS、TPC-C、Wikipedia 上次优。

**实验 2（跨 schema）**（Figure 3b，p.9）：Smallbank 最优，TPC-H、SSB、TPC-C、Twitter 次优；工作负载映射、模型集成、OpAdviser 依赖相似负载匹配，在跨 schema 时效果明显下降。

**实验 3（真实基准）**（Figure 4，p.10）：在 StackOverflow、SSAG、AMPS 上 E2ETune 未取得最优配置，但结果接近且耗时显著更少。

**实验 4（消融）**（Table 2，p.10；平均提升 %）：

| 设置 | OLAP 同 | OLTP 同 | OLAP 跨 | OLTP 跨 |
|---|---|---|---|---|
| E2ETune | 51.4 | 156.2 | 50.1 | 150.6 |
| 去查询计划 | 44.5 | 145.6 | 34.9 | 53.2 |
| 贪心解码（无采样-排序） | 50.1 | 152.8 | 47.0 | 144.3 |
| 直接输出数值（不分桶） | 15.1 | 45.3 | 9.4 | 36.8 |
| Few-shot GPT-4 | 35.3 | 115.4 | 30.9 | 116.4 |

另外：TPC-H 上随机森林 36.8%、MLP 51.3%，E2ETune 72.5%；TPC-C 上分别为 128.8%、177.5%、239.9%（§8.3.7，p.11）。JOB 上用 GPT 生成负载训练得 50.26%，用 CEB 模板负载训练仅 38.56%（§8.3.8，p.11）。训练数据从 1/3 增至全量，性能持续上升（Figure 5，p.10）。

**边界**：只评测 PostgreSQL 12.2 与 45 个 knob；换引擎需重新采集与训练，作者认为更适合硬件和 DBMS 统一的云环境（§9，p.13）。主要结果以曲线图呈现，正文未给出每个基准的数值表（阅读者分析）。
