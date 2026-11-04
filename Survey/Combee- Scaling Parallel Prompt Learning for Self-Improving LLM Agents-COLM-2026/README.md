# Combee: Scaling Parallel Prompt Learning for Self-Improving LLM Agents

ACE、GEPA 等提示学习方法从智能体轨迹的反思中更新 playbook 或系统提示，但原设计是逐条或小批量更新；直接把批量调大，聚合用的 LLM 会把大量反思压成泛泛的建议（作者称 context overload）。

Combee 是叠加在这类方法上的扩展层：反思复制并打乱后分组，用两级并行扫描聚合，再用动态批量控制器选批大小。在 AppWorld、Terminal-Bench 2.0、FiNER、Formula 上，它在接近顺序学习质量的同时把学习耗时最多降低约 17×（Terminal-Bench，42.4→2.4 分钟）。

[原文](https://arxiv.org/abs/2604.04247v2)

版本：arXiv 2604.04247v2（2026-09-25，首页标注 COLM 2026），51 页；2026-11 重新取得全文，按 §1–4、表 1–3、附录 B/E/G/H/J 核对本目录数字。未复现实验。
