# Novelty分析

本文将agent限制在可解释的重写方向内，同时让另一个验证角色构造任务相关的判据。主要价值是以逻辑分解改善漏提取、上下文遗漏、实体重复等具体失败，而不只是改prompt措辞（§3–4）。

方法风险是评分也来自LLM，局部“看起来更好”不必然改善全局结果；样本可能比真实长文档短，导致完整执行时仍超context。§4承认动态调整计划尚在开发；§5.5的30个生成计划里20%有关键错误，说明验证筛选是必要组成。

原版目标偏重质量，明确把成本和延迟约束列为后续工作（p.3041）。不要把后续MOAR的多目标能力倒填进2025版DocETL。

来源：[DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing](https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf)。
