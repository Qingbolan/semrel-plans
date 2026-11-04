# Rogers et al. — NarrativeTime: Dense Temporal Annotation on a Timeline

NarrativeTime 是一个基于时间线（而非事件对）的时间关系标注框架：标注者把事件放到整篇文本的动态时间线上，再由时间线推出全部 tlink。作者用它对 TimeBank-Dense 的 36 篇新闻做了双人全量重标，得到 TimeBankNT：每套标注 102,313 个 tlink（不含逆关系），密度约为 MAVEN-ERE 的 5 倍；事件顺序 IAA 为 Krippendorff α 0.68。LongT5 基线的宏平均 F1 最高仅 0.31，人类对人类为 0.57。已阅读正文 §1–7、伦理声明及附录 A–C，附录 D–E 按需查阅；未复现实验。

[原文](https://aclanthology.org/2024.lrec-main.1054)

版本：LREC-COLING 2024，pp.12053–12073，ACL Anthology 2024.lrec-main.1054，21 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1–2、Table 1，PDF pp.1–3 |
| 方法 | §3 框架（事件类型、事实性、分支、聚类、timex 锚定、工具），附录 B，PDF pp.3–6、15–16 |
| 评测 | §4 标注评估（Tables 3–4、Figs 7–8）、§5 基线（Table 5），PDF pp.6–9 |
| 局限 | §5 末尾、§6 Future work、附录 B–C，PDF pp.9、15–16 |
