# 评测与边界

**实验 1（InfiAgent-DABench，Table 1，p.8）**：准确率（%），∆ 相对同模型无 agent 设置。

| 框架 | 模型 | 准确率 | ∆ |
|---|---|---|---|
| 无 agent | gpt-4-0613 | 78.99（引自 Hu et al.）/ 75.21（自测） | — |
| 无 agent | gpt-4o | 75.92 | — |
| XAgent | gpt-4-0613 | 47.53 | −31.46 |
| AutoGen | gpt-4-0613 | 71.49 | −7.50 |
| Data Interpreter | gpt-4-0613 | 73.55 | −5.44 |
| Data Interpreter | gpt-4o | 94.93 | +19.01 |

摘要中的“25%”是相对增幅（19.01 / 75.92）。gpt-4-0613 版本仍低于无 agent，作者归因于上下文超出窗口（§4.2，p.8）。

**实验 2（ML-Benchmark，Table 2，p.9）**：综合分与 API 成本。

| 框架 | Titanic | House Prices | SCTP | ICR | SVPC | 平均 | 成本 ($) |
|---|---|---|---|---|---|---|---|
| AutoGen | 0.87 | 0.86 | 0.83 | 0.77 | 0.73 | 0.86 | — |
| OpenInterpreter | 0.86 | 0.87 | 0.68 | 0.58 | 0.44 | 0.77 | — |
| TaskWeaver | 0.63 | 0.68 | 0.34 | 0.74 | 0.48 | 0.69 | 0.37 |
| XAgent | 0.42 | 0.42 | 0 | 0.34 | 0.01 | 0.45 | 20.09 |
| OpenDevin | 0.87 | 0.94 | 0.93 | 0.73 | 0.73 | 0.88 | 3.01 |
| Data Interpreter | 0.91 | 0.96 | 0.94 | 0.96 | 0.89 | 0.95 | 0.84 |

平均列还包含 WR、BCW 两个 toy 任务（各框架均 ≥0.93，表中省略）。Data Interpreter 成本为 OpenDevin 的 27.9%。

**实验 3（开放任务，Table 3，p.9）**：平均完成率 Data Interpreter 0.97、OpenDevin 0.60、AutoGen 0.46、OpenInterpreter 0.40；成本 $0.41 对 OpenDevin $1.41。邮件回复（ER）任务中基线都无法登录，完成率 0.10，Data Interpreter 0.98。

**实验 4（MATH，Figure 4，p.9）**：4 类 level-5 题上都最好，N.Theory 0.82（比 AutoGen 高 0.16），Precalc 0.29（高 0.17），平均相对 AutoGen 提升 26.5%。

**实验 5（消融，Table 4、Figure 5，p.10）**：加入迭代图修订使综合分从 0.37 升至 0.85，再加可编程节点生成到 0.94；换小模型时数据加载和分析尚可，但高级编码和图像/网页工具任务失败。

**边界**：
- 原文附录 A 承认：ML 数据集为入门级 Kaggle 数据（<500 MB，列数百、行数万），以分类回归为主，未覆盖大规模数据、时间序列、多标签、多表；也未做人类数据科学家式的多轮实验优化。
- 阅读者整理：ML-Benchmark 与开放任务为作者自建，CR 依赖步骤完成度的判定；三种指标（准确率、综合分、完成率）不可合并；各实验使用的 LLM 不同，跨表比较需谨慎。

依据：[arXiv 2402.18679v4](https://arxiv.org/abs/2402.18679v4)，§4.1–4.2、Tables 1–4、Figures 4–5、附录 A、D.2，pp.7–10、15、20–21。
