# 评测与边界

**实验 1（KGQA，Table 1，PDF p.7）**，Hits@1：

| 方法 | WQSP | MQA-1 | MQA-2 | MQA-3 |
|---|---|---|---|---|
| UniKGQA（全监督） | 75.1 | 97.5 | 99.0 | 99.1 |
| ChatGPT | 61.2 | 61.9 | 31.0 | 43.2 |
| ChatGPT + IRR | 72.6 | 94.2 | 93.9 | 80.2 |
| ChatGPT + IRR 少样本 | 69.6 | 97.1 | 97.3 | 87.0 |

**实验 2（TableQA，Table 2，PDF p.8）**：

| 方法 | WTQ | WikiSQL | TabFact |
|---|---|---|---|
| TAPEX（全监督） | 57.5 | 89.5 | 84.2 |
| DATER | 65.9 | – | 93.0 |
| Davinci-003 | 34.8 | 49.1 | 80.7 |
| Davinci-003 + IRR | 39.2 | 51.8 | 76.5 |
| ChatGPT | 43.3 | 51.6 | 82.9 |
| ChatGPT + IRR | 48.4 | 54.4 | 87.1 |
| ChatGPT + IRR 少样本 | 52.2 | 65.6 | 87.6 |

Davinci-003 加 IRR 后 TabFact 从 80.7 降为 76.5。

**实验 3（Text-to-SQL，Table 3，PDF p.8）**，执行准确率：

| 方法 | Spider | Spider-SYN | Spider-Realistic |
|---|---|---|---|
| RESDSQL-3B + NatSQL（全监督） | 84.1 | 76.9 | 81.9 |
| ChatGPT | 70.1 | 58.6 | 63.4 |
| ChatGPT + IRR | 74.8 | 62.0 | 70.3 |
| ChatGPT + IRR 少样本 | 77.8 | 64.0 | 72.0 |

**错误分析（Figure 3，PDF pp.8–9）**：每个数据集抽取 100 个错误。WebQSP 中 74% 是选择错误，Spider 中 62% 是推理错误。正文称所选数据集为 WebQSP、WTQ 和 Spider，但图中标注为 WikiSQL，存在不一致（阅读者分析）。

**边界**：全监督基线结果均引自其他论文；只测试了两个指令跟随能力强的 OpenAI 模型，且模型版本会变化（附录 A：8 月版 ChatGPT 在 WTQ 上降到 41.1）。§7 承认只评测问答任务，并且存在答案格式错误。
