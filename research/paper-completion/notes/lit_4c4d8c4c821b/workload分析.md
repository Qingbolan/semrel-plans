# 工作负载

**微基准**（§8.2，p.9；Table 1）：在 PostgreSQL 12.5 上运行可执行脚本，模拟 6 类应用的异常，覆盖 10 种根因：sync commits、many inserts、high updates、many deletes、index missing、redundant indexes、large data insert、large data fetch、poor join、correlated subquery。

| 应用 | 异常数 |
|---|---|
| Internet of Things | 83 |
| E-Commerce | 211 |
| Financial | 31 |
| Business Intel. | 20 |
| File Sharing | 47 |
| Social Media | 147 |
| 合计 | 539 |

每个异常附有场景描述，如 "In a database of an e-commerce platform, 91 users simultaneously perform searches…"（p.9）。

**划分**：每类应用抽 10 个异常作为测试，共 60 个；其余异常作为 DNN 和决策树的训练数据（§8.3，p.9）。微调实验用 D-Bot(GPT-4) 的诊断记录，包含 5 个子任务、共 2,819 个样本，测试用 27 个案例（§8.5，p.12）。

**知识与工具规模**：从 81 页文档中抽取 188 个知识块（§4.1.3，p.6）。工具包括监控工具（pg_stat_statements 等）和优化工具（hypopg 假设索引、索引选择、改写、调参）（§4.2，p.6；§8.1，p.9）。

**指标**（§8.2，p.9）：Acc=(A_c−σ·A_w)/A_a，σ=0.1，结果为负时记 0。HEval 的公式相同，但只计"根因正确且分析过程合理"的项，由人工判定。

依据：§4、§8.1–8.2、§8.5，pp.6–12。
