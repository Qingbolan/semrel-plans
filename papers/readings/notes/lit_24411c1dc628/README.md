# Toledo et al. — AI Research Agents for Machine Learning: Search, Exploration, and Generalization in MLE-bench

本文把 AI 研究智能体形式化为在候选解（代码工件）图上搜索的算法，由适应度函数、选择策略、算子集合、算子策略和终止规则组成，并据此分别分析 AIDE 的搜索策略与算子。在 MLE-bench lite（22 个 Kaggle 任务）上，作者发现 AIDE 的算子是瓶颈；改进算子（O_AIRA）后再配合 MCTS，以 DeepSeek R1 为模型将获奖牌率提升到 47.7%。验证-测试泛化差距会让最终选解损失 9–13 个百分点。已阅读正文、全量 MLE-bench 附录与种子数附录。

[原文](https://arxiv.org/abs/2507.02554)

版本：arXiv:2507.02554v2（2025-11-04；文内日期 2025-07-03），34 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–4 |
| method | §3–4，PDF pp.4–7 |
| evaluation | §5、App. D、App. I，PDF pp.7–11、18、28 |
| limitations | §7.1，PDF p.12 |
