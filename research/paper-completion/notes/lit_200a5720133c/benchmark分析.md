# 评测与边界

**基线**（§6.1.1）：Baseline（LLM-Answer 直接作答、Schema-Answer 加 schema、RandomRowCol 随机取单元格）；Text-to-SQL（LLM-SQL、C3、FinSQL）；TableQA（TableRAG、ERATTA）。

**指标**（§6.1.3）：表/列检索的 Precision、Recall、F1；Context Relevance（RAGAS 方式）；报告 Accuracy（与参考报告对照）与 Report Relevance（由报告反向生成问题，计算与原问题的语义相似度）。LLM 打分统一用 DeepSeek-V2.5，0–10 分（Figure 4 提示词）。

**实现**：LangChain；LoRA 基座 LLaMA2-13B，r=32，lr=1e-4；单张 A40（46GB）。

**主要结果**：

| 数据集 | 方法 | 表 P/R/F1 | 列 F1 | Context Rel. | 报告 Acc / Rel / Avg |
|---|---|---|---|---|---|
| DA-CCKS | DAgent | 56.35 / 36.96 / 43.10 | 19.96 | 6.87 | 6.27 / 6.96 / 6.62 |
| DA-CCKS | TableRAG | 40.20 / 35.19 / 35.84 | 14.96 | 5.31 | 5.47 / 6.77 / 6.12 |
| DA-BIRD | DAgent | 81.23 / 88.82 / 82.23 | 71.21 | 7.15 | 6.43 / 7.01 / 6.72 |
| DA-BIRD | TableRAG | 65.59 / 88.97 / 72.77 | 53.89 | 5.76 | 5.83 / 6.99 / 6.41 |

（Tables 1–3，PDF pp.10–11；表格列序由文本抽取还原，阅读者按"平均=两项均值"核对了 Table 3。）

**消融**（§6.3、Figure 5）：去掉问题分解检索性能明显下降；文本+向量混合检索优于单一策略；SQL 改写后检索性能"没有显著下降"。Figure 5 只给图，正文未列具体数值。

**阅读者注意的问题**：

- 正文称 DAgent 在所有方面优于基线，但 DA-BIRD 上 TableRAG 表召回 88.97 略高于 DAgent 88.82；DA-CCKS 上 RandomRowCol 报告 Accuracy（3.57）高于 Schema-Answer（3.05），说明该 LLM 打分区分力有限（阅读者分析）。
- 报告分数集中在 6–7 分区间，差距较小，且无方差、无显著性检验、无人工评测。
- 评审模型 DeepSeek-V2.5 与 DAgent 报告生成模型相同（§6.1.4），存在自偏好风险，论文未讨论。
- 未报告延迟、token 成本。

**局限**：论文无局限章节；§7 仅提出将优化分解与检索子模块、拓展更复杂场景。

依据：[arXiv:2503.13269v2](https://arxiv.org/abs/2503.13269)，§6、Tables 1–3、Figures 4–5，PDF pp.8–12；§7，p.12。
