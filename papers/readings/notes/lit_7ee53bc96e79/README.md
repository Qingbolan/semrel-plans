# Yang et al. — Process-Reward Tactic Evolution for Long-Horizon Bioinformatics Workflows

本文提出 PRTE：智能体在 Galaxy 平台上反复执行课程化的生物信息工作流任务，用十通道过程验证器给轨迹打分，再由“语义梯度”更新器把成功/失败片段提炼为带适用条件、过程、后置条件、失败签名和公开证据的 tactic 文件库；推理时冻结该库并检索使用。

在自建 BioWorkflow Bench 的 35 个留出任务上，PRTE 总分 0.5013，略高于 GEPA 的 0.4953，优势集中在 long/xlong 任务；但除 GEPA 与 PRTE 外，其余基线行是从 quick10 换算的 test35 估计值。已阅读正文、附录 B–D（任务表、提示词、tactic 演化与 Hi-C 案例）。

[原文](https://arxiv.org/abs/2606.20839)

版本：arXiv:2606.20839v1（2026-06-18），18 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | Abstract、§1、§2.1，PDF pp.1–2 |
| method | §2.2–2.4、附录 C（Figs.6–8、Table 10），PDF pp.2–3、11–15 |
| evaluation | §3–4、Tables 1–6、Figs.2–5，附录 B（Tables 7–8）、附录 D，PDF pp.3–6、8–10、15–17 |
| limitations | Limitations、Ethics Statement，PDF p.6 |
