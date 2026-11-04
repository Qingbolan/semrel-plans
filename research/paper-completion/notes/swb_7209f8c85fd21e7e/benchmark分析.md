# benchmark

**模型**：GPT-4o-mini、GPT-4o、Claude Sonnet 3.7、Qwen2.5 72B、Llama 4 Maverick（非推理），DeepSeek R1、o3-mini、o4-mini（推理）；另有随机基线（§5，PDF p.7）。GCI 只测了 4 个模型。

**主要结果**
- E-Score（Table 1，PDF p.7）：一级代码各模型 Precision@5 约 0.74–0.86；三级代码最好为 o4-mini 0.420、DeepSeek R1 0.418，GPT-4o 为 0.383。推理模型在一级代码上精确率较低、召回较高，在三级代码上更好。ICL 示例数增加时，Llama 4 与 o4-mini 的二、三级代码表现大致单调上升；GPT-4o 在 20-shot 最好（Figure 3，PDF p.8）。
- E-Ver（Table 2，PDF p.7）：F1 最高 GPT-4o 0.634，DeepSeek R1 0.629；Qwen2.5 为 0.486、o4-mini 为 0.509，接近随机 0.5。多数模型把约 2/3 样本判为 met，而真实正例率为 0.434，作者认为模型倾向过度判定“满足”（PDF p.8）。
- GCI（Table 3，PDF p.8）：类别精确率最高 GPT-4o 0.493，召回最高 o4-mini 0.835（它平均预测 3.397 条，而金标准平均 1.273 条）；DeepSeek R1 结构化输出解析成功率只有 61.61%；o4-mini 的归一化 MAE 为 0.186，ΔStrength 为 0.445。
- 解释一致性（Table 4，PDF p.9）：只在分类正确的 E-Score 样本上评，GPT-4o 30-shot 一致率为 0.704，零样本为 0.486。

**边界**（附录 B，PDF p.15）：不包含补充材料与图表中的证据；部分代码需要多篇论文才能判定，但本文只做单篇；LM 评审需更多验证；变异与基因命名在论文间不统一，可能造成额外难度。训练截止日期之后的样本上各模型均有下降，但幅度不大（附录 F.4，PDF p.22）。表中 ± 为误差条（计算方式见附录 L.4，未细读）。

依据：[arXiv:2510.11985v1（2025-10-13，NeurIPS 2025 Datasets & Benchmarks），37 页](https://arxiv.org/abs/2510.11985)。
