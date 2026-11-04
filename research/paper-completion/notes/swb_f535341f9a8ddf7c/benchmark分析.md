# 评测与边界

**实验 1（标注者一致性，p.9）**：要求类型与起止位置完全一致才算匹配，按 F1 计算。20 份培训文档上实体 76.1%、关系 60.3%；在另 99 份双标注文档上实体 78.1%、关系 60.9%。

**实验 2（基线，pp.10–12，804/202 划分，微平均 P/R/F1）**：

| 任务 | 模型 | P | R | F1 |
|---|---|---|---|---|
| 实体 | biLSTM+CRF | 80.2 | 79.6 | 79.9 |
| 实体 | PubMedBERT | 75.3 | 78.7 | 77.0 |
| 实体 | SciBERT | 79.0 | 83.7 | 81.3 |
| 关系 | SciBERT | 80.2 | 88.2 | 84.0 |
| 关系 | R-BERT+SciBERT | 82.5 | 88.0 | 85.2 |

实体与关系各训练两个模型（一般实体和细粒度实体分开）。高频实体（Condition、Eq-Comparison）以及结构规整的实体（Age 98.7、Contraindication 98.3，SciBERT）表现较好；Death（33.3）、Criteria-Count（15.5）、Family-Member（51.7）较差。关系中 Eq-Comparison 与 Minimum-Count、Treatment-For 与 Using 容易混淆。

**实验 3（质量一致性，pp.11–12）**：用 887 份单标注训练、119 份双标注测试，SciBERT NER 得 P/R/F1 = 79.7/82.5/81.4。手工部分训练、半自动部分测试 F1 为 78.6；反向为 80.0（Table 7）。

**表格疑点**：Table 6 中 Found-By 的 R-BERT 精确率印作 9.3，但 F1 为 75.4，与召回率 71.8 不相容，很可能是 79.3 的排版错误；Abbrev-Of 的 R-BERT 一行 P/R=92.3/93.1，F1 却印作 94.2，也不一致（阅读者分析）。

**局限**（p.12）：多数文档单人标注；约一半由模型预标注；语料不含查询，无法证明它更利于查询生成；没有量化语义表达能力的指标。Future work（p.13）提出用 ROUGE 比较生成查询，或加入 UMLS 概念 ID。

依据：Technical Validation、Tables 4–7、Limitations、Future work，PDF pp.9–13。
