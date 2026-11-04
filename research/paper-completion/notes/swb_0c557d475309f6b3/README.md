# Diao et al. — GuideBench: Benchmarking Domain-Oriented Guideline Following for LLM Agents

本文构建 GuideBench，用于评估 LLM 能否按"领域指南"（可能与常识冲突、且经常更新的领域规则集）作答。数据由 LLM 合成并经人工修正，共 1,272 个任务、7 类场景，含 537 条指南规则。论文评测 19 个 LLM 配置（正文称 18 个）；DeepSeek-R1 总体准确率最高，为 87.26%，数学类普遍低于 60%。已阅读正文 §1–§7、局限与伦理、附录 A（设置）、附录 C–E 的结构与关键提示；未逐条检查附录 B 的全部提示模板。

[原文](https://aclanthology.org/2025.acl-long.557)

版本：ACL 2025 长文（Volume 1），pp.11361–11399，39 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1，PDF pp.1–2 |
| 方法（数据构建与任务形式） | §3、§4，Figures 2–3，PDF pp.3–6 |
| 评测 | §5–§6、Tables 1–3、Figures 4–5，附录 A、C，PDF pp.6–9、13、35 |
| 局限 | Limitations、Ethics Statement，PDF p.10 |
