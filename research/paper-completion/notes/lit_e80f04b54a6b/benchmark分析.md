# 评测与边界

**实验 1（公开基准，GPT-4 底座）**（Table I，p.10，已渲染核对）：

| 基准/指标 | DataLab | 基线 |
|---|---|---|
| Spider EX | 80.70 | DAIL-SQL 83.60，PURPLE 87.80，CHESS 87.20 |
| BIRD EX | 61.33 | DAIL-SQL 57.41，PURPLE 68.12，CHESS 68.31 |
| DS-1000 Pass | 53.80 | CoML 44.20，Code Interpreter 51.60，Open Interpreter 50.50 |
| DSEval Pass | 80.99 | CoML 71.90，Code Interpreter 80.58，Open Interpreter 78.10 |
| DABench Acc | 75.10 | AutoGen 71.48，AgentPoirot 75.88 |
| InsightBench LLaMA-3-Eval / ROUGE-1 | 0.37 / 0.33 | AutoGen 0.31 / 0.28，AgentPoirot 0.35 / 0.35 |
| nvBench EX | 53.90 | LIDA 54.71，Chat2Vis 53.83，CoML4VIS 51.12 |
| VisEval Pass / 可读性 | 75.99 / 3.73 | LIDA 74.66 / 3.77，Chat2Vis 71.91 / 3.70，CoML4VIS 75.27 / 3.80 |

正文称 DataLab 在 InsightBench 与 VisEval 上"超过所有基线"（p.9），但表中 ROUGE-1 与可读性分并非最优（阅读者分析）。"比 AutoGen 高 5.06% / 19.35%"是相对提升。

**实验 2（换底座模型）**（Figure 6，p.10）：

| 底座 | Spider | DS-1000 | DABench | VisEval |
|---|---|---|---|---|
| GPT-4 | 80.70 | 53.80 | 75.10 | 75.99 |
| Qwen-2.5 | 69.70 | 53.10 | 73.93 | 75.81 |
| LLaMA-3.1 | 61.90 | 42.50 | 69.26 | 76.35 |

原生 LLaMA-3.1（不经 DataLab）在 DS-1000 上为 36.90。

**实验 3（知识注入消融）**（Table II，p.11）：S1 无知识 / S2 部分知识 / S3 全部知识下，Schema Linking R@5 为 41.02 / 71.79 / 79.49，NL2DSL 准确率为 32.52 / 61.66 / 91.10。摘要中的"58.58%"是百分点差。知识质量 SES 表级 0.712、列级 0.677。

**实验 4（通信消融）**（Table III，p.11）：去掉 FSM / 去掉格式化 / 完整，成功率 73 / 85 / 92，准确率 56 / 79 / 84。失败多涉及 3 个以上智能体。

**实验 5（上下文管理）**（Fig. 7、Table IV，p.12）：DAG 首次构建 <250 ms（最大 232.22 ms，35 单元），单元更新均值 3.78 ms。使用 DAG 后准确率从 86.67% 降到 82.00%，token 从 10.69K 降到 4.10K（-61.65%），原因是部分关键 Markdown 单元未被相似度检索召回。

**边界**：内部数据不公开、规模较小（100–439 条）；无独立局限章节；基线与 DataLab 的提示和重试预算是否对齐未说明（阅读者分析）。
