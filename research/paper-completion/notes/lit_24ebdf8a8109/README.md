# Du, Yang et al. — DataMaster: Data-Centric Autonomous AI Research

DataMaster 提出“任务条件下的自主数据工程”：学习算法固定，智能体只在数据侧操作（外部数据发现、选择与组合、清洗变换、特征构造），以下游训练结果为唯一反馈。系统由 DataTree（红节点做外部数据探索、黑节点做数据利用并提交训练）、共享 Data Pool 和 Global Memory 组成，并用 UCB 式调度分配预算。

在 MLE-Bench Lite（22 个 Kaggle 竞赛）上奖牌率从 35.91% 提升到 68.18%；在 PostTrainBench（Qwen3-1.7B-Base，7 项能力）上平均分从 8.47% 提升到 31.17%，GPQA 31.02% 略高于官方 instruct 模型的 30.35%。已阅读正文与附录 A–D；论文无独立局限性章节。

[原文](https://arxiv.org/abs/2605.10906)

版本：arXiv 2605.10906v2（2026-05-13，cs.LG），28 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3.1，PDF pp.1–4 |
| method | §3.2–3.5、Fig.1，PDF pp.4–7；附录 C（调度），pp.22–24 |
| evaluation | §4、Tables 1–4、Figs.2–5，PDF pp.7–12；附录 B、D，pp.16–27 |
| limitations | 无独立章节；§4.4 数据泄漏分析 p.11–12、附录 B.3 基线实现 p.18、附录 D.1 分支集中偏差 pp.24–25 |
