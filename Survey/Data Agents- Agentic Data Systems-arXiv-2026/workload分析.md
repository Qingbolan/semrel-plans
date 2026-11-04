# 工作负载

**基准**（§6，p.11）：

| 基准 | 规模 | 内容 | 指标 |
|---|---|---|---|
| DABStep | 450 题，分 easy / hard；使用官方 validated split | 多步数据分析，输入含非结构化文档、查找表和 schema 元数据；hard 部分强调跨文档语义对齐 | easy / hard 准确率 |
| Spider 2.0-Lite | 547 例 | 跨 BigQuery、Snowflake、SQLite 的真实 text-to-SQL，含 schema 噪声与多种方言 | 执行准确率（排行榜协议） |

**查询类别**（用于消融与成本分析，§6-B/C，Fig. 2、Tables VI–VII）：

| 基准 | 类别 |
|---|---|
| DABStep | Simple Query、Single Data Statistic、Multiple Data Statistic、Matching with Complex Logic |
| Spider 2.0-Lite | Aggregation Query、Multi-table Query、Nested Query、Recursive Data Analysis |

论文说按推理深度和数据源使用复杂度分类，但没有给出每类题数或划分规则。

**配置**：骨干 LLM 为 Qwen 3（未说明具体型号与参数规模）；与基线使用相同输入文档和问题；默认解码与工具设置，无任务特定微调（§6，p.11）。§5-A 描述了批处理、级联、共享前缀分组等执行优化，但没有给出 batch 大小、阈值或级联所用模型。

阅读者分析：两个基准都是公开排行榜任务，偏向“回答一个分析问题”，不覆盖论文主打的主动发现、跨源取证（如外部天气 API）等场景；类别划分未公开，消融与 token 分析难以复现。

依据：[arXiv 2609.24137v1](https://arxiv.org/html/2609.24137v1)，§5-A、§6，pp.10–12。
