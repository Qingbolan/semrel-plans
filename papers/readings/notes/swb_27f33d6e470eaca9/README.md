# Kulkarni et al. — An Annotated Corpus for Machine Reading of Instructions in Wet Lab Protocols

本文发布 Wet Lab Protocol Corpus：从 protocols.io 选取 622 篇湿实验协议，标注动作（Action）、17 类实体和 12 类关系，用于把自然语言实验步骤解析为浅层语义结构（动作图）。作者用 MaxEnt 与 BiLSTM(-CRF) 做实体/动作识别，并用 MaxEnt 做关系分类；BiLSTM-CRF 的动作 F1 为 86.89，实体识别加分类 F1 为 72.61。已读正文全部章节与附录 A（标注指南、Table 8 关系规则）；Figure 4 的统计图仅在提取文本中粗看。

[原文](https://arxiv.org/abs/1805.00195)

版本：arXiv:1805.00195v1（2018-05-01），10 页（正文 5 页 + 参考文献 + 附录）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1–2，PDF pp.1–2 |
| 方法（标注方案、标注流程、模型） | §3–5，附录 A，PDF pp.2–4、8–10 |
| 评测 | §4.1、§6、Tables 3–7，PDF pp.3–5 |
| 局限 | 无独立局限章节；§6.1 对 POS 标注器的讨论、§7，PDF p.5 |
