# 工作负载

本文是综述，没有自有数据集、查询集或实验负载。

文献组织范围（按 §I-A 的数据生命周期）：
- **数据管理**：配置调优（LLMTune、GPTuner、λ-Tune 等）、查询优化（逻辑：DB-GPT、GenRewrite、LLM-R2、E3-Rewrite；物理：LLMOpt、LLM-QO；L2：SERAG、R-Bot、QUITE）、系统诊断；
- **数据准备**：清洗、集成（模式匹配、实体解析）、发现（描述性画像、语义标注）；
- **数据分析**：TableQA、NL2SQL、NL2VIS、非结构化文档（含“DocumentDB”类系统 QUEST、Doctopus）、报告生成；
- **Proto-L3**：Data Interpreter、SiriusBI、iDataLake、AOP、DeepAnalyze、JoyAgent、AgenticData，以及 Snowflake Cortex、BigQuery、ByteDance Data Agent、Databricks 等工业产品（Table IV）。

参考文献共 209 条；配套资源列表为 GitHub 仓库 HKUSTDial/awesome-data-agents。

阅读者分析：与语义查询处理直接相关的是 §IV 中非结构化数据分析的 DocumentDB 小节，以及 §V 中基于预定义语义算子编排管线的 iDataLake 与 AOP；作者把“依赖预定义语义算子”视为通向 L3 的限制。

依据：[arXiv:2510.23587v2，20 页](https://arxiv.org/abs/2510.23587)，§III–§V、Tables II–IV，PDF pp.4–15。
