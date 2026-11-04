# 工作负载

主实验（§7.1，PDF p.10）：CRAG 数据集。每个问题原本附带 5 个网页，作者把所有问题的网页合并为一个共享的外部知识库，用来模拟真实场景。只选用 5 类复杂问题：

| 类型 | 查询数 |
|---|---|
| Multi-hop | 231 |
| Post-processing | 108 |
| Set | 249 |
| Aggregation | 315 |
| Comparison | 333 |

合计 1,236 条（阅读者加总）。

配置：所有方法都用 Llama 3.1-8B Instruct；Sentence Transformer 生成 384 维句向量，按句切块，余弦相似度取 top-20；硬件为 Xeon 6242R、4 张 RTX 3090、256 GB 内存（PDF pp.10–11）。

非结构化分析实验（§7.3，PDF p.11）：100 个 Sports StackExchange 网页转为纯文本；参考 StackExchange Data Explorer 人工设计 5 个模板，每个模板采样 5 个取值，共 25 条查询；用 LLM 生成改写并人工核对等价性；标准答案人工计算。

阅读者分析：两组实验的数据都是网页文本。原文强调的结构化/半结构化数据湖场景没有被评测。§5.2 用 Llama 3 的 8,192 token 上下文说明需要上下文管理，但实验使用的是 Llama 3.1-8B，原文没有说明实际的上下文配置。
