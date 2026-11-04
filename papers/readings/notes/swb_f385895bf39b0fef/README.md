# Zheng et al. — HateModerate: Testing Hate Speech Detectors against Content Moderation Policies

本文按 Facebook 2022 年 11 月的 41 条仇恨言论社区准则，构建逐条政策的测试集 HateModerate：共 7,704 个样本，其中仇恨 4,796 个、非仇恨 2,908 个，由 28 名研究生加 GPT 经六步流程标注。论文用它测试 4 个检测器，发现各模型都偏重严重层级政策，OpenAI Moderation 总体失败率最低（平均 0.29）。用一半数据加入微调后，在 HateModerate 和 HateCheck 上的失败率显著下降。已阅读正文 §1–§7 及附录 A.4–A.8；未逐条核对附录中 41 条政策的分政策表。

[原文](https://aclanthology.org/2024.findings-naacl.172)

版本：Findings of NAACL 2024，pp.2691–2710，20 页（含附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.2–2.3，PDF pp.1–4 |
| 方法（数据构建） | §3.1–3.4、Tables 1–2，PDF pp.4–6 |
| 评测 | §4.1–4.4、Tables 3–5、Figure 4，附录 A.5–A.8，PDF pp.6–9、15–16 |
| 局限 | §6 Limitations、§7 Ethics，PDF p.10 |
