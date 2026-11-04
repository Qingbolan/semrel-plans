# usecase

Rotowire 的球员查询：player_info ⋈ player_to_reports ⋈̈ reports.player。先把球员信息表与"球员—比赛报道"链接表连接，再与报道文本做多模态 join，抽取每名球员在该场比赛中的得分、助攻等统计。

- **运行时间**：论文报告该查询用 ELEET 约 3 分钟，Text-To-Table 17 分钟，LLaMA 2.5 小时，GPT-3 1.5 小时，GPT-4 接近 4 小时（§6.2，PDF p.13）。原文此处写作 GPT-3，实验设置中对应的是 gpt-3.5-turbo。
- **join 为什么更快**：join 的输入表已经带有球员/球队名，可以跳过"先抽取 document-level key"的第一阶段。在 team latent 表上，join 约 26 秒，scan 和 union 约 70 秒（§6.4，p.14，Figure 9）。
- **先过滤再 join**：先对 player_info 做过滤，只需处理与选中元组相链接的报道，运行时间降到数秒（Figure 10 左）。
- **索引选择**：Scan(σ̈ Points=28(...)) 这类查询借助索引，避免先把全部文本转成表（Figure 10 右）。

阅读者分析：这个用例适合"表中每行带文档指针，需要从文档抽取字面值后再做关系运算"的场景。对于需要跨文档推理，或需要输出非原文 span 的语义判断，论文没有提供证据。

依据：[arXiv:2410.22522v1，23 页](https://arxiv.org/abs/2410.22522)，§6.2–§6.4，Figures 9–10，PDF pp.13–14。
