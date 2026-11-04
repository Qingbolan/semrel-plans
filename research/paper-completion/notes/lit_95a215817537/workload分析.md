# 工作负载

本文是综述，没有自己的数据集或查询集。可视为“工作负载”的是被调查的文献集合与汇总的基准。

**文献集合**（§3，pp.10–11）：

| 阶段 | 数量 |
|---|---|
| 去重后候选论文 | 587 |
| 标题与摘要筛选后 | 约 200 |
| 全文审阅后得到的不同 DS 智能体 | 45 |

检索时间窗为 2023–2025 年；检索词包括 DS agents、LLM agents、multimodal agents、tool-using agents、trustworthy AI systems、data science automation。

**汇总的基准**（Table 3，p.25）：阅读者计数共 20 个，示例如下（规模按表中原文转录）：

| 基准 | 阶段 | 规模 |
|---|---|---|
| ELT-Bench | S1、S3 | 100 条管线、835 张表、203 个数据模型 |
| Spider 2.0 | S2–S3 | 632 个任务、213 个数据库 |
| DSBench | S2–S4 | 466 个分析任务、74 个建模任务 |
| InsightBench | S2–S5 | 100 个数据集（每个 500 行） |
| DSEval | S2–S5 | 294 个集合、825 个问题 |
| Spider2-V | S2–S3 | 494 个任务、170 套环境配置、151 个脚本 |

其余包括 IDA-Bench、TimeSeriesGym、DataSciBench、LLM4DS、DA-Code、BLADE、tau-bench、Tapilot-Crossing、MatPlotBench、InfiAgent-DABench、SWE-bench、STRUC-BENCH、AgentBench、ARCADE。

阅读者分析：这些规模来自各基准原论文，本综述未重新核验。
