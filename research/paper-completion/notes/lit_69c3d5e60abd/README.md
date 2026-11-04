# Zhu, Peng, Li, Luo（HKUST-GZ）— SQLConductor: Search-to-Policy Learning for Step-wise Text-to-SQL Orchestration

SQLConductor 把 Text-to-SQL 子任务（问题分解、相关值抽取、操作识别、模式剪枝、SQL 生成、SQL 修正、终止）做成动作，由一个小型策略模型（Qwen3-8B/4B）根据中间产物与执行反馈逐步选择下一动作，动作本身由冻结的大模型执行。策略的训练数据来自离线 MCTS 工作流搜索，并按 Laplace 平滑的“稳定性”打分加权 SFT，再在难题上做课程式 GRPO。

BIRD-Dev 上 8B 策略 + Gemma4-31B 动作模型达 73.2% EX；同为 Qwen2.5-Coder-32B 动作模型时为 71.2%，高于 DeepEye-SQL 70.6% 和 Alpha-SQL 69.7%，且每题成本约 0.012 美元。已通读正文（§1–7，含全部表格与案例）；论文没有独立的局限性章节。

[原文](https://arxiv.org/abs/2606.23537)

版本：arXiv:2606.23537v1（2026-06-22，cs.DB），14 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§2、Fig.1，PDF pp.1–3 |
| method | §3–4、Algorithms 1–3、Figs.2–5，PDF pp.3–9 |
| evaluation | §5、Tables 1–6、Figs.6–9，PDF pp.9–12 |
| limitations | 无独立局限章节；阅读者据 §5 实验设置与表格整理 |
