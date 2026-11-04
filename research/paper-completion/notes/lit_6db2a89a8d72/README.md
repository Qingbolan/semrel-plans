# Yang et al. — EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management

EvoDS 是一个基于 Qwen3-8B、经 SFT + 多角色 GRPO 训练的分层多智能体数据科学 agent，带有自主技能获取（ASA）与自适应上下文压缩（ACC）。在 DABench、DA-Code、ScienceAgentBench、MLE-Dojo（10 题抽样）上，EvoDS-evo 平均分 0.424，比最强开源基线 DataMind-14B（0.329）相对高 28.9%，但低于 ReAct+o4-mini（0.450）。已阅读正文 §1–7 与附录 B–C（基准、基线），附录 A 的理论证明只读了定理陈述。

[原文](https://arxiv.org/abs/2606.03841)

版本：arXiv:2606.03841v1（2026-06-02），KDD ’26 版本，18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3（Definitions 3.1–3.4），PDF pp.1–3 |
| method | §4.1–4.4、Figure 1、Eqs.1–10，PDF pp.3–5；§5（定理陈述），p.6 |
| evaluation | §6.1–6.6、Tables 1–4、Figures 3–4，PDF pp.6–9；附录 B Table 5，p.13 |
| limitations | §6.2 末段（ScienceAgentBench 差距），p.7；§6.5 失败分析，p.8 |
