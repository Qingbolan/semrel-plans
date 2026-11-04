# 工作负载

**语料（Table 1，PDF p.3）**：

| 分区标签 | 文档数 | 词（百万） | 大小（GB） |
|---|---|---|---|
| legal | 330 | 86 | 0.57 |
| regulatory-guidance | 1,110 | 5 | 0.04 |
| contract-coverage-rule-medical-policy | 7 | 196 | 1.31 |
| opinion-policy-summary | 2,093 | 19 | 0.14 |
| case-description | 2,630 | 214 | 1.44 |
| clinical-guidelines | 2,150 | 82 | 0.57 |
| 合计 | 8,311 | 419 | 2.83 |
| 其中带 kb 标签 | 1,434 | 171 | 1.16 |

共 27 亿字符、616 种标签（§4、§4.2.4，PDF pp.2–3）。"kb"标签表示权威文本，由人在环自动生成；合同在部分情境下有约束力，也被标为 kb（§4.2.2，PDF p.3）。

**来源**（附录 A，PDF pp.12–13）：Justia 上的各州法典最新年度版本、美国法典（release point 118-30）、eCFR、联邦公报、CMS 指南与 Medicaid 政策指南、Medicare NCD/LCD（2024 年初有效版本）、部分州 Medicaid 手册、HHS OIG 各类报告、FDA 指南、Meditron 临床指南子集。商业保险合同、商业医学政策、Medicaid/CHIP 州计划、管理式医疗合同因许可或无批量下载渠道而缺失（§8.3，PDF pp.8–9）。

**申诉数据**：纽约 DFS、加州 CDI、加州 DMHC 三个外部申诉数据库（§5.5，PDF p.5）。共有 74,007 条案件描述经过抽取和伪标注；按来源和申诉结果分层后均匀抽样切分训练/测试集（§5.6.4，PDF p.6）。

**测试集**：9,920 条，其中 Insufficient 113、Upheld 5,284、Overturned 4,523（Table 2 说明，PDF p.7）。原文没有给出训练集条数（阅读者分析：若 74,007 条全部入集，训练集约 64,087 条，但原文未确认）。

**人群偏差**：案件多来自 50 岁以上人群和商业保险计划，只覆盖纽约和加州，且都是已提起外部申诉的拒付（§9.1，PDF p.9）。

依据：[JURIX 2024 AI4A2J，19 页](https://drive.google.com/file/d/1vsu0Ns6R6AeTX4-Hf2OdYqRvHD4yNm4y/view)，§4、Table 1、§5.5–5.6、Table 2、§8.3、§9.1、附录 A，PDF pp.2–9、12–13。
