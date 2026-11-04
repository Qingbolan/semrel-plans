# Freitas, Kalajdjieski et al. — AI-Driven Guided Response for Security Operation Centers with Microsoft Copilot for Security

本文介绍 Microsoft Defender XDR 中部署的 Copilot Guided Response（CGR）：用 PySpark 特征工程、PCA 和随机森林，为安全运营中心（SOC）提供三类建议——相似事件（调查）、真/假/良性阳性分级（分诊）和处置动作（修复），并公开 GUIDE 数据集（100 万事件、160 万告警、1,300 多万条证据）。离线分诊宏 F1 平均 0.87，动作预测宏 F1 平均 0.99；论文明确不与其他方法比较。CGR 本身不使用 LLM。已读正文全部和附录 A–C；Table 2 已渲染核对。

[原文](https://arxiv.org/abs/2407.09017)

版本：arXiv:2407.09017v4（2024-11-26），10 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2，PDF pp.1–3 |
| 方法 | §3–6、Algorithms 1–2，PDF pp.3–6 |
| 评测 | §7、Tables 2–3、Figure 3，PDF pp.6–8；附录 A–B，p.10；Table 2 已渲染核对 |
| 局限 | §7.1 Limitations，PDF p.6；§7.3–7.5 Online results，pp.8 |
