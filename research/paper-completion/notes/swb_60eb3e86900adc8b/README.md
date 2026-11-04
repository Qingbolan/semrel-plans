# Kwon et al. — LogicQA: Logical Anomaly Detection with Vision Language Model Generated Questions

本文提出 LogicQA：用预训练视觉语言模型（VLM）从 3 张正常图像自动生成"正常性检查清单"问题，再对测试图像逐题问答，任一主问题回答"否"即判为逻辑异常，并以回答理由作为解释。在 MVTec LOCO AD 的逻辑异常部分，GPT-4o 版本平均 AUROC 87.6%、F1-max 87.0%，高于同为少样本的 LogicAD；另在不公开的半导体 SEM 企业数据上优于 PatchCore。已阅读正文、局限及附录 B–G；未复现实验，SEM 数据不可获取。

[原文](https://aclanthology.org/2025.acl-industry.29)

版本：ACL 2025 Industry Track，pages 411–432，22 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–2 |
| 方法 | §3.1–3.5，Figure 2–3，PDF pp.2–4；附录 A–B，PDF pp.9–12 |
| 评测 | §4–5，Tables 1–3，PDF pp.4–6；附录 C–G，Tables 4–6，PDF pp.13–22 |
| 局限 | Limitations、Ethics，PDF p.7 |
