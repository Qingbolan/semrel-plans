# Zheng et al. — Can We Predict Before Executing Machine Learning Agents?

本文提出"数据驱动的方案偏好"（Data-centric Solution Preference）任务：给定任务描述、经核验的数据分析报告和两份 ML 方案代码，让 LLM 在不执行代码的情况下判断哪份方案在测试集上更好。作者从 AIDE/AutoMind 在 MLE-bench 26 个任务上的真实轨迹构建 18,438 个方案对，DeepSeek-V3.2-Thinking 达到 61.5% 准确率（随机 50.0%、复杂度启发式 50.8%），并把该预测器作为过滤器嵌入 AIDE，得到 ForeAgent（报告 6× 收敛加速、Beat Ratio +6%）。已阅读正文 §1–8、Limitations 以及附录 B、C（语料统计、轨迹来源分析、ForeAgent 细项与 k 消融）；未逐项核对附录 D/E 的案例与提示词。

[原文](https://arxiv.org/abs/2601.05930)

版本：arXiv:2601.05930v2（2026-04-07），34 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2，PDF pp.1–3 |
| method | §3（任务定义、语料、数据报告），§6.2，PDF pp.3–4、7–8 |
| evaluation | §4–5、Tables 2–4，§6.3–6.4、Figure 4；附录 C、Tables 11、13–15，PDF pp.4–8、21–28 |
| limitations | Limitations 节，PDF p.9；Discussion 6.1，PDF p.7 |
