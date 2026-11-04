# 评测与边界

**基线**：LLM 类 GPTuner、DB-BERT；强化学习 UDO；降维的 LlamaTune（MLOS 内）；只调 5 个优化器代价常数的 ParamTree；索引推荐工具 Dexter 与 DB2 Index Advisor（§6.1，p.9）。

**指标**：随调优时间变化的最佳工作负载执行时间（Figures 3–4）；各方法最佳配置代价除以该场景全局最优（Table 3）；评测配置数（Table 4）。

**实验 1（Table 3，p.10，14 个场景平均的相对代价，越小越好）**：

| 方法 | 平均 | 最差场景 |
|---|---|---|
| λ-Tune | 1.41 | 4.98（TPC-H 10GB，MySQL，有初始索引） |
| DB-BERT | 1.82 | 5.16（同上） |
| GPTuner | 1.91 | 5.84（同上） |
| UDO | 2.00 | 3.76 |
| LlamaTune | 2.27 | 3.48 |
| ParamTree | 4.07 | 15.2 |

只看允许建索引的 8 个场景，λ-Tune 平均为 1.21（§6.2，p.10）。λ-Tune 并非每个场景都最佳：LlamaTune 在 TPC-H 10GB/PG/无索引最好，UDO 在有索引的 MySQL TPC-H 10GB 场景最好（Table 3）。

**实验 2（评测次数，Table 4，p.11，Postgres）**：

| 方法 | 各场景评测配置数 |
|---|---|
| λ-Tune | 5 |
| UDO | 83–707 |
| DB-BERT | 6–171 |
| GPTuner | 3–156 |
| LlamaTune | 1–19 |
| ParamTree | 1 |

**实验 3（消融，JOB/Postgres，Figures 6–7，pp.12–13）**：关闭自适应超时，找到接近最优配置的时间从不到 1,000 秒增至 1,300 秒以上；关闭查询调度，首个配置完整评测时间超过 1,800 秒；二者都不降低最终配置质量。把表名列名混淆后性能几乎不变，作者据此认为 λ-Tune 不依赖预训练数据中的提示。去掉压缩、改放 26 条完整 SQL，评测更慢、最佳配置更差且 token 更多；压缩表示在 token 少十倍以上时仍更好，只有 196 tokens 的极低预算明显退化。

**实验 4（仅索引推荐，Figure 8，p.13）**：除 TPC-DS 外，λ-Tune 不如 Dexter 和 DB2 Advisor 等专用工具。

**边界**：没有独立局限一节。阅读者分析：只针对 OLAP；只用 GPT-4，未比较其他 LLM；每个实验只跑 3 次；LLM 调用费用没有以金额报告；混淆实验仅在 JOB 上做，“不依赖预训练记忆”的结论范围有限（阅读者分析）。

依据：§6、Tables 3–4、Figures 3–8，PDF pp.9–13。
