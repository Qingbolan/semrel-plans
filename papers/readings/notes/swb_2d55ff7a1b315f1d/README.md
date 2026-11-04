# Lüders & Stohlmann — Classifying proportionality - identification of a legal argument

本文把德国联邦宪法法院（GFCC）判决中的“比例原则”（proportionality）论证作为领域特定的论证挖掘对象，发布 300 份判决、54,929 句的句级标注数据集，并在“判决理由（merits）部分”的 24,577 句上做二分类：判断每句是否属于比例原则检验。最佳模型 BERT-BiLSTM-CRF（德语 BERT）F1=0.561、召回 0.478，所有模型召回均不超过 0.5。已阅读全文正文与附录 B，Table 6 已从提取文本逐行核对；未审阅外部数据仓库与规则代码。

[原文](https://link.springer.com/article/10.1007/s10506-024-09415-9)

版本：Artificial Intelligence and Law 33:1051–1078（2025），出版社 Open Access 版本（CC BY），由 HU Berlin edoc 仓储下载（Springer 页面有机器人校验），28 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1、§3，PDF pp.1–2、5–9 |
| method | §4–5，PDF pp.9–18；附录 B |
| evaluation | §5.4、§6、Table 6，PDF pp.18–22 |
| limitations | §6.1.3、§6.2、§7，PDF pp.21–23 |

注：PDF 页码 = 期刊页码 − 1050。
