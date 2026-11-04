# 评测与边界

**比较方法**（§7.1）：

1. Rule-based Tool + DBA：预定义工具生成报告，再由专家 DBA 分析；
2. LLM-Only：DeepSeek-R1-32B、DeepSeek-R1-671B 直接输入监控指标；
3. ChatDBA：树结构 RAG，支持 MySQL/PostgreSQL；
4. D-Bot：多智能体 + 思维树，仅支持 PostgreSQL；
5. DBAIOps：骨干分别为 DeepSeek V3、DeepSeek-R1-32B、DeepSeek-R1-671B。

排除闭源 LLM（数据隐私）、ML 方法（只输出固定标签）、Andromeda（参数推荐，问题不同）、GaussMaster（仅 GaussDB）、Panda（无开源代码）。

**指标**：根因 Precision、F1；沿用 D-Bot 的 Accuracy = (A_c − σ·A_w)/A_a（σ 默认 0.1，惩罚错误根因）；HEval 人工评分 = 根因召回 30% + 理论一致性 30% + 证据真实性 40%。

**主要结论**（§7.2 正文所述）：

- DBAIOps（R1-32B / R1-671B）综合诊断性能 0.92 / 0.94，分别比单独 R1-32B（0.57）和 R1-671B（0.70）高 61.40% 和 34.29%。
- HEval 上比 D-Bot、ChatDBA 高 37% 以上和 45% 以上；DBAIOps 各骨干平均 0.89，与 Rule-based Tool + DBA 的 0.91 相当；MySQL 上平均 Accuracy 0.94 高于后者的 0.79。
- 按场景（Figure 5）：DBAIOps 平均 0.87；单独 R1-32B 在 CPU Spikes 为 0.59，在 Excessive Dirty Page Writes 仅 0.12。
- 消融（Table 6，Oracle、R1-32B）：w/o ADF 为 P 0.75 / F1 0.86 / Acc 0.73 / HEval 0.50；w/o Graph Evolution 为 0.67 / 0.80 / 0.63 / 0.60；两者都去掉为 0.60 / 0.75 / 0.56 / 0.50。三变体平均 0.66，作者称比完整版低 34%。
- 输出与输入图内容的相似度（Table 7）：PostgreSQL 上 Levenshtein 0.10、TF-IDF 0.37 等，作者以此说明输出不是复制图内容。

**阅读者注意的问题**：

- 摘要称根因与人工评估准确率分别高 34.85% 和 47.22%，正文给出的是 34.29%/61.40% 与 37%/45%，口径未对齐，原文未解释"综合诊断性能"如何由四项指标聚合（阅读者分析）。
- Table 5 抽取文本列序混乱，本笔记只引用正文明示的数字；未渲染核对 Table 5 逐格数值。
- HEval 由人工打分，但标注者人数、一致性、是否盲评均未报告；评分细则在外部 GitHub 文件。
- 基线覆盖受限：D-Bot 只在 PostgreSQL、ChatDBA 只在 MySQL/PostgreSQL 上有结果，跨库比较主要是对 LLM-Only 与规则方法。
- 未报告诊断延迟、token 开销，也没有讨论失败案例或局限。

依据：[arXiv:2508.01136v1](https://arxiv.org/abs/2508.01136)，摘要 p.1；§7.1–7.4、Tables 5–8、Figure 5，PDF pp.9–12。
