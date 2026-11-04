# Chalkidis et al. — Paragraph-level Rationale Extraction through Regularization: A case study on European Court of Human Rights Cases

本文提出在欧洲人权法院（ECtHR）判决中做“段落级”理由抽取：给定案件事实段落，多标签预测申请人主张被违反的 ECHR 条款，并同时选出支撑预测的事实段落。作者发布约 1.1 万案件的数据集（含正则表达式抽取的银标准理由和 50 个测试案件的专家金标准理由），比较稀疏性、连续性、完整性约束，并提出“singularity”约束；该约束的理由质量最好（金标准 mRP 53.6），但所有模型离人工理由仍有很大差距。已阅读正文全部与附录 A–F。

[原文](https://aclanthology.org/2021.naacl-main.22)

版本：NAACL-HLT 2021 正式版（ACL Anthology 2021.naacl-main.22，pp.226–241），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§3（任务定义），PDF pp.1–4 |
| 方法 | §4.1–4.2（HierBERT-HA、Eq.1–8），PDF pp.5–6；附录 B，p.12 |
| 评测 | §5–6、Tables 2–6，PDF pp.7–9；附录 C–D、Tables 7–11，pp.12–13 |
| 局限 | §6.6（模型偏差、可信度未做人工评估）、§7，PDF p.9；附录 F 图 3–7，pp.14–16 |
