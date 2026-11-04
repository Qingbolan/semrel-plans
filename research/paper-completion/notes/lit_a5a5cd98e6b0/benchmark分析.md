# benchmark

**主结果**（GPT-4-0613，dev 集，denotation accuracy）：

| 数据集 | 方法 | 结果 | 位置 |
|---|---|---|---|
| HybridQA | 端到端（Oracle 文档检索，Sui et al.） | 56.68 | Table 2，p.7 |
| HybridQA | 端到端（检索全上下文，截断） | 49.13 | 同上 |
| HybridQA | BlendSQL | 52.89 | 同上 |
| HybridQA | BlendSQL + 端到端回退 | 57.76 | 同上 |
| OTT-QA | FR+CBR / CARP / CORE（均微调） | 28.1 / 33.2 / 49.0 | Table 3，p.7 |
| OTT-QA | BlendSQL（BM25 文档检索） | 34.15 | 同上 |
| FEVEROUS | 端到端（Sui et al.） | 83.21 | Table 4，p.7 |
| FEVEROUS | BlendSQL（3 行 / 整表） | 65.7 / 68.03 | 同上 |

**补充结果**：BlendSQL 在 HybridQA 上 1,173/3,466（33%）无法产出预测；在 2,293 条产出有效脚本的子集上准确率 64.43%（§5.1，p.6）。Figure 4：平均提示 token 降 35%（图示，p.7）。开放模型（Table 5，p.9，作 parser 与 blender）：DeepSeek-Coder-6.7b 26.90、StarCoder2-15b 26.23、GPT-4-0613 52.89；坏语法比例 0.13 / 0.21 / 0.03（正文写 13%、21%、3%）。

**错误分析**（§6，pp.7–9）：dev 集 1,464 条得分为 0；随机抽 50 条错误，只有 17 条（34%）是 BlendSQL 真错误，其余为答案冗长、格式归一化、HybridQA 金答案错误/多答案/缺信息等假阴性。真错误中以 parser 错误最多（如把 > 写成 =、该用 LLMJoin 却用 LLMQA）；DOC→TABLE 方向的多跳比 TABLE→DOC 更难。

**局限**（p.10 原文）：GPT-4-0613 API 成本限制复现；需要先把所有上下文预处理进 SQLite。

**阅读者分析**：
- 比较条件不完全一致：端到端为零样本，BlendSQL 用 12 个示例；OTT-QA 基线均为微调且检索器不同，作者自己说难以直接比较；FEVEROUS 丢弃 NEI 后与原任务不可比；OTT-QA 的 denotation 脚本是否与前作一致作者也不确定（Table 3 脚注）。
- 摘要/贡献的 35% 与结论的 45% token 降幅不一致。
- 50 条错误样本的人工标注规模较小，34% 的比例置信区间较宽。
