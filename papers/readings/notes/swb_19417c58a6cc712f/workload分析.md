# 工作负载

本文不是数据集或评测论文，没有训练/测试划分或查询集。可确认的"负载"只有知识库规模和录入对象：

| 项目 | 原文内容 | 位置 |
|---|---|---|
| 规模 | 6,300 余条 Evidence Item、2,300 余个变异、400 余个基因 | Abstract，p.1 |
| 证据来源 | PubMed 收录文献或 ASCO 会议摘要 | p.6 |
| 证据类型 | Predictive、Diagnostic、Prognostic、Predisposing、Functional 五类 | p.7 |
| Assertion 类型 | Predictive、Diagnostic、Prognostic、Predisposing 四类 | p.8 |
| 受控词表 | Disease Ontology、Sequence Ontology、NCI Thesaurus、HPO、HGNC/Entrez | pp.2–8 |

数据通过网页界面和 API 公开（Availability，p.11）。文中没有给出各证据类型、等级的分布计数，也没有说明这些规模数字对应的数据快照日期，只能按 2019 年投稿时（Received 2019-06-14）理解。

阅读者分析：若把 CIViC 当作抽取或语义过滤任务的数据源，天然的标注单元是"文献 × 变异 × 疾病 × 证据类型"的 Evidence Item，目标字段是上表中的受控取值；但这属于派生用途，本文未定义任何自动化任务或评测。

依据：Abstract p.1；pp.6–8；Availability p.11。
