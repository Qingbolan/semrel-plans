# 工作负载

| 数据集 | 规模与指标（原文） |
|---|---|
| NarrativeQA | 书籍和电影剧本全文问答，共 1,572 篇文档；ROUGE-L、BLEU-1、BLEU-4、METEOR |
| QASPER | 1,585 篇 NLP 论文上的 5,049 个问题；答案类型分可答/不可答、是/否、抽象式、抽取式；F1 |
| QuALITY | 多项选择题，上下文平均约 5,000 token；报告全测试集和 HARD 子集准确率（HARD 为多数标注者在限时下答错的题） |

论文未写明 NarrativeQA 与 QASPER 使用哪一划分及问题数。Table 4 明确为 QuALITY dev 集，Table 7 为测试集。（阅读者分析）

**模型**：摘要用 gpt-3.5-turbo；阅读模型为 UnifiedQA-3B、GPT-3、GPT-4；检索器为 SBERT、BM25、DPR（Tables 1–2 用 `dpr-multiset-base`，其他实验用 `dpr-single-nq-base`）。

**其他规模**：建树成本实验在 16GB M1 Mac 上进行，文档长度 12,500–78,000 token。幻觉标注随机抽取 40 篇故事中的 150 个节点。层级分析每张表只针对 QuALITY 的单篇故事。

依据：[arXiv:2401.18059v1](https://arxiv.org/pdf/2401.18059v1)，§4、附录 A、E、I，PDF pp.6–9、15–22。
