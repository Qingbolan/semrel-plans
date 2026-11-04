# 工作负载

**数据集（§5.1，PDF p.6）**：

| 任务 | 数据集 | 说明 | 指标 |
|---|---|---|---|
| KGQA | WebQSP | Freebase，答案最多 2 跳 | Hits@1 |
| KGQA | MetaQA-1/2/3hop | 基于 OMDb 的电影 KG，最多 3 跳 | Hits@1 |
| TableQA | WikiSQL（弱监督） | 过滤与聚合 | 指称准确率 |
| TableQA | WTQ | 需要排序等更复杂推理 | 指称准确率 |
| TableQA | TabFact | 表格事实核验 | 准确率 |
| Text-to-SQL | Spider / Spider-SYN / Spider-Realistic | Spider 评测集 20 个库、1,034 条 | 执行准确率 |

少样本设置中，WebQSP 使用 15 个示例，MetaQA 和表格、SQL 任务使用 32 个（§5.4，PDF pp.7–8）。实验使用 6 月版 Davinci-003 和 gpt-3.5-turbo；附录 A 补充 8 月版 ChatGPT（PDF pp.7、14）。

阅读者分析：除 Spider 外，正文没有给出其他数据集的评测样本数。KGQA 的 Hits@1 还经过人工复核（§5.2），因此它与其他论文的数字不完全可比。
