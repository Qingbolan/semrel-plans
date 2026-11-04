# Kayali et al. — Chorus: Foundation Models for Unified Data Discovery and Exploration

Chorus 是华盛顿大学、RelationalAI 与苏黎世大学提出的系统，用同一个大语言模型完成三项数据发现任务：表类别检测、列语义类型标注、连接列预测。系统通过提示组件拼接、可行性检查以及新提出的 anchoring 机制抑制幻觉。以 GPT-3.5 为主模型，在 T2Dv2、VizNet 和 GitNotebooks 上，三项任务均优于未在测试集分布上预训练的基线，如表类别检测加权 F1 为 0.926。已通读全文。

[原文](https://doi.org/10.14778/3659437.3659461)

版本：PVLDB 17(8): 2104–2114，2024（vldb.org 出版版 PDF），11 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1 Definitions 2.1–2.3，PDF pp.1–2（pp.2104–2105） |
| 方法 | §3.1–3.2、Figs.2–4，PDF pp.3–4（pp.2106–2107） |
| 评测 | §4、Tables 2–7、Figs.5–6，PDF pp.4–8（pp.2107–2111） |
| 局限 | §5 Discussion "Limitations and risks"、§7 Future directions，PDF p.8（p.2111） |
