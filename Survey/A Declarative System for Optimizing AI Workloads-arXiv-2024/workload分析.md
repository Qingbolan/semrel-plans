# 工作负载

**三个工作负载**（§5.2，pp.13–15；程序见 Figure 3、5、9）：

| 工作负载 | 输入数据 | 外部条件 | 标注与指标 |
|---|---|---|---|
| Legal Discovery | 1,000 封 Enron 邮件（注册为 `enron-eval`）；convert 抽出 sender、subject | 无 | 人工标注 50 封真正涉欺诈、30 封含欺诈字样但非欺诈，其余随机；F1 |
| Real Estate Search | 100 条波士顿/剑桥房源（`real-estate-eval`），每条含文本与前 3 张去重图片 | 到 MIT 两英里内、价格区间两个 UDF；距离函数实现正文未给 | 人工标注，23 条满足全部条件；F1 |
| Medical Schema Matching | 11 个电子表格文件，共 49 张表（`medical-eval`） | 15 个属性的目标 schema 是任务规范 | 先筛出患者病例表，再把列映射到目标属性；按原研究 [32] 的 harmonized table 人工对齐，micro-F1 |

**命名差异**：Figure 3 程序中的源名为 `enron-emails`，实验登记为 `enron-eval`，属论文自身不一致（阅读者分析）。Figure 9 的 CaseData 另含 filename/study 字段，15 个是医学目标属性数，不是全部字段数。

**执行方式**：默认 iterator 逐记录执行。§5.5 中每个 convert/filter 用 32 个 worker 并行，算子之间不流水，必须等上一个算子处理完全部记录（p.17）。32 是并发 worker 数，不是把 32 条输入拼进一个 prompt 的 batch size。

**采样**：sentinel 计划使用输入的 5%；医学负载例外，用 11 个文件中的 1 个（§5.3，p.15）。论文未给统一的模型 batch size，也没有多查询联合提交。

依据：[arXiv 2405.14696v2](https://arxiv.org/abs/2405.14696v2)，§5.2–5.5、Figures 3/5/9，PDF pp.6、13–17。
