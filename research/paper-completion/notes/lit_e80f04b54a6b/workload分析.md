# 工作负载

**公开基准**（§VII-A，p.9；Table I，p.10）：

| 任务 | 基准 | 指标 | 备注 |
|---|---|---|---|
| NL2SQL | Spider、BIRD | 执行准确率 EX | — |
| NL2DSCode | DS-1000、DSEval | Pass Rate | DSEval 只评测 LeetCode 与 SO 子集（脚注 1，实现原因） |
| NL2Insight | InfiAgent-DABench、InsightBench | Accuracy；LLaMA-3-Eval、ROUGE-1（摘要级） | — |
| NL2VIS | nvBench、VisEval | EX；Pass Rate、GPT-4V 可读性分 | 只评测单表查询（脚注 2，因部分基线不支持多表） |

原文未给出各基准使用的样本数或划分（dev/test）。所有方法均以 GPT-4 为底座。

**腾讯内部数据**（§VII-C 至 §VII-E，pp.10–12）：

| 实验 | 规模 | 指标 |
|---|---|---|
| 知识质量 | 50 张表、629 列，专家标注语义 | 与标注的句向量相似度 SES（M3-Embedding） |
| Schema Linking | 439 个查询-表-列对 | Recall@5 |
| NL2DSL | 326 个查询-DSL 对 | Accuracy |
| 多智能体通信 | 2 个库、10 张表、111 列；每表 10 个复杂问题，共 100 条 | 成功率（每个智能体最多 5 次调用）、准确率 |
| DAG 构建 | 50 个真实笔记本，单元数 2–49 | 耗时（ms） |
| 上下文管理 | 每个笔记本 3 条查询（NL2SQL、NL2DSCode、NL2VIS），共 150 条 | Accuracy、每查询 token |

内部数据集未公开，问题由作者"从真实业务查询派生"设计（§VII-D，p.11）。
