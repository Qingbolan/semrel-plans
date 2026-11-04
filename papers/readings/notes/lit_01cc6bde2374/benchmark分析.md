# 评测与边界

**实验 1（同一阅读模型 UnifiedQA-3B，有无 RAPTOR，Tables 1–2）**：

| 检索器 | NarrativeQA ROUGE-L 有/无 | QuALITY 准确率 有/无 | QASPER F1 有/无 |
|---|---|---|---|
| SBERT | 30.87 / 29.26 | 56.6 / 54.9 | 36.70 / 36.23 |
| BM25 | 27.93 / 23.52 | 52.1 / 49.9 | 27.00 / 26.47 |
| DPR | 30.94 / 29.56 | 54.7 / 53.1 | 32.23 / 31.70 |

**实验 2（不同阅读模型，Tables 3–4）**：

| 检索 | QASPER F1（GPT-3 / GPT-4 / UnifiedQA） | QuALITY dev 准确率（GPT-3 / UnifiedQA） |
|---|---|---|
| RAPTOR | 53.1 / 55.7 / 36.6 | 62.4 / 56.6 |
| DPR | 51.3 / 53.0 / 32.1 | 60.4 / 53.9 |
| BM25 | 46.6 / 50.2 / 26.4 | 57.3 / 49.9 |

**实验 3（与已有最佳系统比较，Tables 5–7）**：QASPER 上 RAPTOR+GPT-4 为 55.7，CoLT5 XL 为 53.9；QuALITY 测试集 82.6（HARD 76.2），CoLISA 为 62.3（54.7）；NarrativeQA 上 RAPTOR+UnifiedQA 的 METEOR 为 19.1，为表中最高，但 ROUGE-L 30.8、BLEU-1 23.5 低于 Retriever+Reader 的 32.0、35.3。

**边界**：

- 与已有系统的比较混合了不同阅读模型，GPT-4 的贡献无法与 RAPTOR 分开。
- NarrativeQA 指标使用作者修改过的评测脚本（BLEU 平滑、BLEU-4 均匀权重、METEOR 先分词），与引用的旧结果不完全可比。
- §4 正文称 NarrativeQA 的 ROUGE-L 比 BM25 和 DPR 高 7.3 和 2.7，并指向 Table 6，但 Table 6 没有这两行；Table 3 图注写“比 BM25 至少高 5.3”，而表中最小差为 5.5。（阅读者分析）
- 未报告方差或显著性；查询方式只在 QASPER 20 篇上选择。

依据：[arXiv:2401.18059v1](https://arxiv.org/pdf/2401.18059v1)，§4、Tables 1–7、附录 H，PDF pp.6–9、20–21。
