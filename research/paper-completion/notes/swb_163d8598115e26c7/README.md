# Guo, Klein, Huang — CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs

本文把“锚记录 + blocking 候选集”的 LLM 实体匹配建模为成本感知的序列决策：用 PPO 训练的小型 MLP 控制器在 MATCH、COMPARE、SELECT、DECIDE 四类算子之间选择，以质量减成本为目标。只在 Abt-Buy 上训练一次，零样本迁移到 7 个基准，平均 F1macro 76.09、推理成本 0.13 美元，高于 COMEM 管线（74.25、0.59 美元），约为在域 DITTO（85.64）的 89%。已阅读正文、局限与附录 A–F。

[原文](https://aclanthology.org/2026.acl-long.1258)

版本：ACL 2026 Long Papers（Proceedings pp.27281–27293），ACL Anthology 2026.acl-long.1258，13 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3 开头，PDF pp.1–3 |
| 方法 | §3.1–3.3、附录 A、B、D，PDF pp.3–4、11–12 |
| 评测 | §4–5、Tables 1–4、附录 C、E、F（Tables 6–10），PDF pp.4–9、11–13 |
| 局限 | Limitations、Ethical Considerations，PDF p.9 |
