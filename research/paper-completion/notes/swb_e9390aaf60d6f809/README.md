# Li, Ji & Han — Document-Level Event Argument Extraction by Conditional Generation

本文把文档级事件论元抽取表述为“按事件模板条件生成”：BART 编码“未填模板 + 标出触发词的文档”，解码出填好的模板，再从中取出论元。作者同时发布带完整事件与共指标注的文档级数据集 WikiEvents，并提出“最具信息量论元抽取”任务。论文报告 RAMS 上比次优模型高 7.6 F1、WikiEvents 上高 5.7 F1、信息量论元任务上高 9.3 F1；结合关键词触发词模型 TapKey，在 ACE 上只见 10/33 类时达到全监督触发词性能的 97%、论元性能的 82%。已阅读正文 §1–6、Tables 1–8 及附录 A–C；Tables 2、4–6 已渲染核对。

[原文](https://aclanthology.org/2021.naacl-main.69)

版本：NAACL-HLT 2021 论文集 pp.894–908（ACL Anthology 2021.naacl-main.69），15 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | 摘要、§1、Figure 1，PDF pp.1–2 |
| 方法 | §2.1–2.2、Figure 2、Table 1，PDF pp.2–4；附录 A、C，PDF pp.12–13 |
| 评测 | §3–4、Tables 2–8，PDF pp.4–9 |
| 局限 | §4.6 Remaining Challenges、§6，PDF pp.8–9 |
