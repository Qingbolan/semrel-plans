# Stoisser et al. — Ambig-DS: A Benchmark for Task-Framing Ambiguity in Data-Science Agents

Ambig-DS 是诊断数据科学智能体“任务框定歧义”的配对基准：Ambig-DS-Target 在 51 个 DSBench 任务上隐藏预测目标（改名并加入同分布的诱饵目标列），Ambig-DS-Objective 在 61 个 MLE-bench 任务上删去评测指标描述，均沿用源基准原评测器。五个代码智能体在目标歧义下有 39–63% 的运行静默提交了错误目标；允许问一个澄清问题可恢复大部分损失，但没有任何模型–提示策略组合能做到“该问才问”。已阅读正文 §1–§6 及附录中的构成表（Table 5）、提问统计说明；未逐项核对附录 C 的全部稳健性表与 F 中的完整轨迹。

[原文](https://arxiv.org/abs/2605.09698)

版本：arXiv:2605.09698v1（cs.AI，2026-05-10），32 页（正文 9 页，其后为参考文献与附录 A–G）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、§3，PDF pp.1–3 |
| method | §4.1–4.4，Figure 1，PDF pp.4–5；Table 5，PDF p.15 |
| evaluation | §5，Tables 1–3、Figure 2，PDF pp.6–9 |
| limitations | §6 Limitations，PDF p.9；附录 A，PDF p.13 起 |
