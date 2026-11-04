# 工作负载

| 项目 | 原文数值 |
|---|---|
| KaggleBench notebook / 例子 | 700（正文称 700 examples / 700 datasets） |
| 49 个领域、28 类任务 | 娱乐与金融占比最高；任务最多为 Basic Data Analysis（附录 A，Fig.4–5，p.14） |
| 数据文件总数 | 4,304，平均每 notebook 6.15 个；187 个 notebook 需要多文件（Table 6，p.14） |
| QA 对 | 6,876；问题平均 11.96 token，答案平均 13.79 token（Table 6） |
| QA 生成 | GPT-4o 按 cell 批次生成 QA 并打任务/技能标签，答案取自 markdown 结论或代码输出；RAG-Token 模型核对答案来源；12.28% 因任务/技能无效被删；每个 notebook 由 LLM 选 10 个（§3，p.3） |
| 技能库 | 74 项技能，覆盖 28 类任务（Table 7，p.16），如情感分析（BERT/LSTM/朴素贝叶斯）、多表搜索（B+ 树、哈希连接、位图索引）、大表分析（MapReduce、列存、近似查询处理） |
| 人评子集 | 100 个数据集、18 类任务；10 批 × 10 题，每批 3 名标注者；招募 30 人（§6.1 p.6，附录 D p.17，Table 17–18） |
| SCORER 训练 | 上述 100 个数据集人评分数按 70/30 划分（§6.1，p.7） |

注意：正文“700 examples”指 notebook/数据集数，而 Table 6 的 QA 对为 6,876，二者口径不同。人评处的“100 datasets”与“10 batches of 10 questions”以及附录 C“每个 Dataset ID 有 3 个问题”之间单位不完全一致，原文未进一步说明（阅读者分析）。

依据：[arXiv:2504.07421v3，41 页](https://arxiv.org/abs/2504.07421)。
