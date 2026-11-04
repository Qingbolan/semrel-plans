# 评测与边界

基线：PostgreSQL 12.4、Oracle 23.0 内置优化器，学习型优化器 Bao、HybridQO；所有计划转换为 PostgreSQL 物理计划并在 PostgreSQL 引擎执行，指标为执行时间的均值、中位数与 75/95/99 分位（§7.1–7.2，PDF p.8）。

**实验 1（总体效果）**：Table 1（PDF p.9）平均执行时间，单位秒。

| 方法 | IMDB | JOB-light | DSB |
|---|---|---|---|
| PostgreSQL | 27.88 | 9.94 | 9.64 |
| Oracle | 26.49 | 10.11 | 5.45 |
| Bao | 28.10 | 10.07 | 3.09 |
| HybridQO | 27.55 | 9.97 | 9.14 |
| LLM-QO (Qit) | 26.68 | 9.73 | 4.65 |
| LLM-QO (Qdpo) | 25.48 | 9.38 | 3.02 |

作者称 LLM-QO 生成的计划全部有效。

**实验 2（OOD 模板）**：Table 2只报告 Qit：IMDB 均值 79.24 对 PostgreSQL 86.59，DSB 4.40 对 5.32；但 HybridQO 在 DSB 95/99 分位更低；用 OOD 模板做 Qdpo 会产生大量无效计划（§7.3）。

**实验 3（消融、无效计划与延迟）**：去掉统计或示范显著变差（Table 3）；不同 7B 骨干均有提升，Mistral-7B 在 Qdpo 后有无效生成风险（§7.5.3）；OOD 下无效计划分为表数不符、表不符、算子错误三类，示范与 planning path 都能减少无效（Table 4，§7.7）；生成延迟随查询复杂度上升，DSB 最慢（Fig.9）。

IMDB 与 JOB-light 的提升幅度较小（约 5–9%），DSB 的大幅提升主要来自对 PostgreSQL 的比较，相对 Oracle 与 Bao 差距小得多；评测均在 PostgreSQL 引擎上，Oracle 计划需转换后执行。未报告多次运行方差，也未把 LLM 推理时间计入执行时间对比。（阅读者分析）
