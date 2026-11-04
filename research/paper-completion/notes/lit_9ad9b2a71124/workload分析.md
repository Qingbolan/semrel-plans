# 工作负载

**训练数据 DataScience-Instruct-500K（§3.4）**：单能力阶段约 470K 样本（含 AM-DeepSeek-R1-0528-Distilled 的 100K 通用推理样本），序列长 8K；冷启动 20K、RL 15K，第二阶段序列长 32K。

**评测基准（§4.1、附录 A）**：

| 基准 | 规模与单位 |
|---|---|
| DataSciBench | 端到端数据科学提示（沿用原基准） |
| DSBench | 540 个 ModelOff/Kaggle 任务，分数据分析与数据建模 |
| DABStep | 450 个任务，easy 72、hard 378 |
| DABStep-Research（作者自建） | 100 个任务，五类；附检查清单，LLM 评审按内容、格式各打 1–5 分 |
| DS-1000 | 1000 道数据科学代码题 |
| TableQA × 7 | WikiTQ、HybridQA、MultiHiertt、OTT-QA、FinQA、TAT-QA、HiTab |

原文称共 12 个基准。交互轨迹的数据源来自 Spider/BIRD，原文没有讨论训练数据与评测集之间的去重或泄漏检查（阅读者分析）。

依据：§3.4、§4.1、附录 A，PDF pp.8、16–17。
