# Singh, Aggarwal, Bhagat et al. — COMPACT: Building Compliance Paralegals via Clause Graph Reasoning over Contracts

COMPACT 用 GPT-4o 把合同条款抽取为"主体—义务强度—行为—对象—时间条件"实体，建立带类型的条款图，再从图中采样复杂的条款组合，生成需要跨条款推理的合规场景，形成 ACE 基准：633 份合同、4,700 个"条款组合—场景"三分类样本（合规 / 不合规 / 不适用）。5 个 1.5B–8B 开源小模型的基础准确率为 34.5%–56.8%，用 DeepSeek-R1 推理轨迹蒸馏微调后提升 21.7–43.1 个百分点。已阅读正文 §1–§7、局限，以及附录 B（实体、聚类、建图）、C（采样、生成、验证、训练）与 E（案例）。

[原文](https://aclanthology.org/2026.eacl-long.377)

版本：EACL 2026 Long Papers，pp.8081–8112（ACL Anthology 2026.eacl-long.377），32 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2，PDF pp.1–4 |
| 方法 | §3.1–3.3，PDF pp.4–6；附录 B–C，pp.12–29 |
| 评测 | §4–§6、Tables 1–8，PDF pp.4–9；附录 E，p.30 起 |
| 局限 | Limitations and Future Work，PDF p.9 |
