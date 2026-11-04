# 工作负载

**端到端评测数据**（§7）：从 NTSB CAROL 数据库取 100 份 PDF，覆盖 2024 年 6–9 月的航空事故，每份 4–7 页，含事故摘要、可能原因与结论、事实信息、管理信息等章节，多张表格（飞行员背景、飞机与运营方、气象、残骸、伤亡）及照片或航迹图。

**ETL**：DocParse 解析后用 llmExtract 抽取 19 个字段（Table 3，如 accidentNumber、aircraft、aircraftDamage、injuries、location、windSpeed 等），写入 OpenSearch 索引；文本另行切块并嵌入为向量。模型：gpt-4o、all-MiniLM-L6-v2、OpenSearch 2.17。

**问题**：作者称不存在此类文档分析的标准基准，因而手工构造 30 个问题，例如“按州统计事故数”“造成严重损坏的事故中因发动机问题的比例”“涉及 Piper 飞机的事故中最常损坏的部件”“7 月涉及鸟类的事故”。少数问题可直接查表 3 的字段，多数需要查询期 LLM 抽取或过滤。标准答案由人工检查确定。论文未公开完整的 30 题列表。

**分割评测**：DocLayNet 竞赛基准，COCO mAP/mAR，11 类。

依据：[arXiv:2409.00847v3，CIDR 2025，10 页](https://arxiv.org/abs/2409.00847)，§4.1、§7–7.1、Tables 1、3，pp.4、7–8。
