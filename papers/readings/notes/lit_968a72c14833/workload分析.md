# 工作负载

本文没有自己的工作负载。Table 5（p.23）汇总了被综述基准的来源、任务数与任务类型，节选如下：

| 基准 | 来源 | 任务数 | 任务类型 |
|---|---|---|---|
| BLADE | 文献 | 714 | 选择题与真实分析研究 |
| InfiAgent-DABench | GitHub | 257 | 数据分析与 ML |
| ML-Bench | GitHub | 9641（168） | 多模态、时序、音频、生物医学等 |
| DA-Code | Kaggle、GitHub | 500 | 数据整理、EDA、ML |
| DSBench | ModelOff、Kaggle | 540 | 数据分析、建模 |
| DSEval | 教程、StackOverflow、Kaggle | 825 | 数据分析 |
| Spider2-V | 教程、企业应用 | 494 | 数仓、转换、可视化 |
| MLE-Bench | Kaggle | 75 | 建模 |
| DS-1000 | StackOverflow | 1000 | 数据科学代码生成 |
| GeoAgent-Bench | GitHub、教程、LLM 生成 | 19,504 | 地理空间单轮/多轮分析 |
| TheAgentCompany | 公司网站、人工示例 | 175 | 企业场景数据科学任务 |

表中共 35 行，另有 BIODSA-1K（1029）、BioDSBench（293）、TimeSeriesGym（34）等领域基准；ML-Dev-Bench 的来源标为"Unknown"，Chen et al. [2024a] 一行未给任务数。ML-Bench 的 "9641(168)" 括号含义原文未解释。

阅读者分析：这些数字直接转自各原始论文，本综述未核对版本或子集；若要引用规模，应回到原始基准论文。另一篇本批论文（Salemi et al. 黑板系统）用的是过滤后的 DSBench 253 题与 DA-Code 91 题，与此表的 540、500 口径不同（阅读者分析）。

依据：§5，p.20；Table 5，p.23。
