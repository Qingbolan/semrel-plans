# Egg et al. — DABstep: Data Agent Benchmark for Multi-step Reasoning

DABstep 是 Adyen 与 Hugging Face 发布的数据分析 agent 基准：450 个源自 Adyen 支付业务的真实分析任务（由 95 个核心问题参数化扩展），要求 agent 在 Python 环境中结合 payments.csv、fees.json 等结构化数据与 manual.md 等文档多步推理，并以事实型答案自动评分。Hard 集最好的 o4-mini 仅 14.55%，Easy 集除 Llama 3.2 1B（1.39%）外为 52.78–80.56%。已阅读正文与附录 A.1–A.4。

[原文](https://arxiv.org/abs/2506.23719)

版本：arXiv:2506.23719v1（2025-06-30），26 页（正文 9 页，其余为参考文献与附录轨迹截图）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–§2，pp.1–5 |
| method | §3，pp.5–6；附录 A.2–A.3 |
| evaluation | §4，pp.6–8，Table 1（p.3）；附录 A.4 |
| limitations | §4.3、§5，pp.7–9 |
