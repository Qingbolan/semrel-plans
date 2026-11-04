# Novelty分析

相对Palimpzest早期启发式选择，Abacus把候选采样和多目标组合分开：MAB负责在有限预算里发现有价值的候选，Pareto-Cascades负责在quality/cost/latency间组合取舍。相对DocETL的质量导向逻辑拆分，主要新增能力是具显式约束的物理实现选择（§3、§6）。

实现包括model selection、Mixture-of-Agents、Reduced-Context、Critique-and-Refine，另有top-k和join规则（§4.1）。不能把可扩展框架等同于论文已实现全部可能重写。

限制直接影响应用：上游输出改变会使独立成本模型失准；采样frontier逐层推进带来优化延迟；LLM judge可替代缺失中间标签，但不等于独立ground truth。对于少量临时数据，应把优化开销与执行开销一起比较。

来源：[Abacus: A Cost-Based Optimizer for Semantic Operator Systems](https://arxiv.org/abs/2505.14661v3)。
