# workload

Table 3（PDF p.12）给出基准统计：

| 数据集 | 文本集合 | 表 | latent 表 | 查询 | latent 属性数 | 测试文本 | join/union/scan/selection/aggregation |
|---|---|---|---|---|---|---|---|
| Rotowire | 1 | 6 | 2 | 28 | 21、14 | 728 | 10/4/14/6/6 |
| T-REx | 3 | 6 | 6 | 12 | 8 | 221 | 2/6/4/2/2 |
| Aviation | 1 | 3 | 1 | 15 | 7 | 30 | 5/5/5/3/3 |
| Corona | 1 | 1 | 1 | 15 | 7 | 30 | 0/15/0/0/0 |

- 共 70 个查询计划，每个含 1–3 个 MMOps 和 0–1 个传统算子（§6.1，p.13）。
- Rotowire：4,850 篇篮球比赛报道，抽取的值以数字为主。
- T-REx：在 nobel、skyscrapers、countries 三个预训练未见领域上微调，但因自动构造的数据噪声较大，只在 nobel 领域评测。
- Aviation：NTSB 事故报告。
- Corona：德国 RKI 每日疫情报告，只用于 union。
- 训练规模：Exp.1 每个数据集用 64 篇标注文本；Exp.2 从 4 篇到 Rotowire 全量 3,398 篇（pp.13–14）。
- 附录 A（pp.22–23）列出全部 70 个代数查询及其选择性，例如 Scan(σ̈ Points=28 [sel=0.096](reports.Player))。

与图谱查询的关系：图谱中 benchmark_id 为 eleet 的查询共 86 条，标题形如 "rotowire · reports.Player: join on name → join text on Game ID"，对应附录 A.1 中的 join、union、scan 形式。阅读者分析：86 与论文的 70 不一致，原因无法从论文中判断，不能把两者视为同一份清单。

依据：[arXiv:2410.22522v1，23 页](https://arxiv.org/abs/2410.22522)，§6.1、Table 3、附录 A，PDF pp.12–13、22–23。
