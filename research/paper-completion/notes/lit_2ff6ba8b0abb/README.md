# Qiu et al.（浙江大学 / 蚂蚁集团）— Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis

先导研究指出，通用过程奖励模型（PRM）在数据分析智能体上有两类盲点：察觉不到“静默错误”（代码不报错但结果错），又把必要的试错（“落地错误”，如猜错列名）当成致命错误。

本文提出 DataPRM：可在环境中执行代码、调用文档/图像查询工具核验步骤的生成式 PRM，用 {0, 0.5, 1} 三值奖励区分不可恢复与可纠正错误，以 7K+ 条步级标注训练 4B 模型。Best-of-N 下 DataPRM 在 ScienceAgentBench（78 题）与 DABStep 上领先各类 PRM 和 Qwen3-235B 自奖励；用于 GRPO 训练后在 DABench 达 78.73%、TableBench 达 64.84%。已阅读全文及附录 A。

[原文](https://arxiv.org/abs/2604.24198)

版本：arXiv:2604.24198v2（2026-06-20，ACM 会议模板），12 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1–3、Table 1、Fig.2，PDF pp.1–4 |
| method | §4.1–4.3、Fig.3，附录 A，PDF pp.4–6、12 |
| evaluation | §5、Tables 2–5、Figs.4–5，PDF pp.6–9 |
| limitations | Limitations and Ethical Considerations，PDF p.9 |
