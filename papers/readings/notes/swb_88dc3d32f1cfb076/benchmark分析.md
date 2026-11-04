# 评测与边界

**实验 1（零样本标题/摘要排序，CSMeD-DEV-COCHRANE）**：比较 BM25、TF-IDF 与三个 Transformer 模型，查询分别用综述标题、摘要、检索策略或纳入标准。指标为 TNR@95%、nP@95%、Last Rel、nDCG@10、MAP、R@10/50/100。正文 Table 3 只列 BM25 与 MPNet：

| 模型/查询 | TNR@95% | nDCG@10 | MAP | R@100 |
|---|---|---|---|---|
| BM25/摘要 | 0.474 | 0.503 | 0.453 | 0.757 |
| BM25/标准 | 0.430 | 0.452 | 0.417 | 0.725 |
| MPNet/摘要 | 0.516 | 0.556 | 0.482 | 0.777 |
| MPNet/标准 | 0.545 | 0.514 | 0.488 | 0.784 |

BM25 以综述摘要为查询最好；神经模型以纳入标准为查询时 TNR@95% 最高，约 0.55，即在 95% 召回下平均能排除一半以上真负例。阅读者分析：§4.3 正文称最佳模型为 “MiniLM”，但 Table 3 行名为 MPNet，两者不一致；完整结果在附录 Table 9，本 PDF 未包含。

**实验 2（全文筛查，CSMeD-FT）**：微调 Longformer、BigBird、Clinical-Longformer、Clinical-BigBird（4 个 epoch）；零样本 GPT-3.5-turbo-0301、GPT-4-8k、GPT-3.5-turbo-16k。综述描述截断为上下文的一半，超长文献用滑动窗口再聚合。指标为宏平均 P/R/F1，McNemar 检验加 Bonferroni 校正。

| 模型 | TEST-SMALL F1 | TEST F1 | TEST 预测纳入比例 |
|---|---|---|---|
| ‘include all’ | 0.306 | 0.304 | 100% |
| BigBird-roberta-base | 0.572 | 0.575 | 45.1% |
| Clinical-BigBird | 0.583 | 0.609† | 32.8% |
| GPT-3.5-turbo-0301 | 0.580 | — | — |
| GPT-4-8k-0314 | 0.660 | — | — |
| GPT-3.5-turbo-16k | 0.576 | 0.475 | 75.9% |

GPT-4 只在 50 篇的 TEST-SMALL 上评测（预算原因），领先不显著；TEST 上 Clinical-BigBird 显著优于随机、Longformer 两种及 GPT-3.5-16k。

**边界**：Cochrane 标准变化导致部分综述协议无法抽取；数据依赖 PubMed/API 下载脚本，未来可能失效；CSMeD 无测试集；全文只覆盖约 27% 文献；只做二值相关。作者建议未来做前瞻式评测以避免泄漏。

依据：[NeurIPS 2023 D&B，17 页](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf)，§4.3、Table 3，PDF pp.7–8；§5.2、Table 5，PDF pp.9–10；§6，PDF p.10。
