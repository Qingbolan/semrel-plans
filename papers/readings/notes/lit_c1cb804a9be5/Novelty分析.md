# 贡献与评价

论文声称的贡献是一个系统框架而非新算法：

| 组件 | 做法（原文） |
|---|---|
| QVA 问题过滤 | 嵌入检索最高分低于 λ=0.85 判为域外，并检索 AWS 服务描述给出去向 |
| Grounding | 文档/工单检索；top-K=3 指标、默认 24 小时遥测、变点检测和经典检测器提取特征；问题 SQL 与 schema；以 JSON 汇总，文档切块只保留 top-3 |
| Feedback | 二值 Helpful/Not Helpful 存入向量库，生成时取 1–3 条正负例作为 few-shot |
| Verification | 同一 LLM 做 NLI 校验，最多重试 K=3；按句子逐字重合给出内联引用 |
| Affordance | 主要依据文档中的“通常影响”，少数动作用简单统计模型；预设高风险动作清单 |

各组件（RAG、NLI 自校验、few-shot 反馈）多为已有技术的工程组合，新意在于把它们按 DBE 排障流程组织成部署框架，并提出 Telemetry-to-Text 这一问题。影响估计在当前版本中较弱，作者自己也承认主要靠检索文档推断（阅读者分析）。

依据：[原文](https://www.vldb.org/cidrdb/papers/2024/p6-singh.pdf)，§2、§4，PDF pp.3–6。
