# 具体用例

原文举出的两个复杂查询（§1，pp.1–2）：

- **消歧**：多轮输入 “When did Arsenal last win the FA Cup? [SEP] 2005 [SEP] What about them compared to Chelsea in league titles?” 需要把 “them” 解析为 Arsenal 并引入 Chelsea 做比较，可能产生并行或串行子查询。
- **分解**：“What were the global shipments of iPhones in 2022 and 2023, respectively?” 拆为 “global iPhone shipments in 2022” 与 “… 2023” 分别检索，再综合回答。

附录 B.1 案例分析（p.13，Figure 5）：用 ANCE 训练的模型倾向生成多条自然语言式子查询；用 BM25 训练的模型倾向生成一条罗列全部关键词的查询；换用另一检索器评估时效果明显下降。作者据此认为查询质量应依赖检索器评价，模型生成的改写优于人类直觉上“正确”的改写（含 DeepSeek-V3 的指令改写）。

阅读者分析：这说明 ACQO 学到的是“检索器特定”的查询风格，部署时更换检索器需要重新训练。

依据：[arXiv:2601.21208v1，16 页](https://arxiv.org/abs/2601.21208)，§1、附录 B.1、Figure 5，PDF pp.1–2、13–14。
