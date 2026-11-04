# Vidgen et al. — Learning from the Worst: Dynamically Generated Datasets to Improve Online Hate Detection

本文用"人与模型在环"的四轮动态对抗流程构造英语仇恨言论检测数据集（41,255 条，约 54% 为 Hate，含约 1.5 万条对比扰动及仇恨类型/目标细粒度标签），并逐轮训练 RoBERTa 目标模型。后续轮次的模型更难被骗（错误率从 54.7% 降到 27.7%），在 HateCheck 上准确率从约 60% 升到 95%。已阅读正文、影响声明与附录 A–E（含数据声明），未复现实验。

[原文](https://aclanthology.org/2021.acl-long.132)

版本：ACL-IJCNLP 2021 长文，pp.1667–1682（ACL Anthology 2021.acl-long.132），16 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–§2，PDF pp.1–3 |
| 方法 | §3–§5（标签体系、标注、四轮构造），附录 D，PDF pp.3–6、13–14 |
| 评测 | §6、Tables 3–4、Figure 1，PDF pp.6–8 |
| 局限 | §6.3 末段、§7 Discussion、Impact Statement，PDF pp.8–9 |
