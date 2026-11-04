# 工作负载

**数据集**（§4.1，PDF p.5）：使用 Spider 与 BIRD 的开发集，分别含 1,034 和 1,534 个 (nl, sql) 样本。BIRD 的 SQL 更复杂，包含 Spider 未覆盖的 CASE、IIF 等关键字。

**数据库规模（Table 2，PDF p.5）**：

| 集合 | 每库表数 min/max/avg | 每库列数 min/max/avg |
|---|---|---|
| Spider 训练集 | 2 / 26 / 5.4 | 6 / 352 / 27.8 |
| BIRD 训练集 | 2 / 65 / 7.6 | 6 / 455 / 51.3 |
| Spider 开发集 | 2 / 11 / 4.1 | 7 / 56 / 22.1 |
| BIRD 开发集 | 3 / 13 / 6.8 | 11 / 199 / 72.5 |

**派生子集**：

- 难度：Spider 分 Easy/Medium/Hard/Extra，BIRD 分 Simple/Moderate/Challenging（Tables 3–4，PDF p.6）。
- SQL 特征：是否含子查询、逻辑连接词数量、是否含 ORDER BY、JOIN 数量（Exp-2，PDF p.7）。
- QVT：BIRD 中极少有同一 SQL 对应多个问法，因此只用 Spider 开发集中 469 条对应两个以上问法的 SQL（Exp-3，PDF p.8）。
- 领域：Spider 训练集 140 个库与开发集 20 个库被归为 33 个领域（Exp-4，PDF p.8）。
- 训练样本量：从 Spider 训练集抽 500 及每 1000 递增的子集（Exp-9，PDF p.10）。

工作负载是单数据库、单条 SQL 的翻译任务，数据库规模以表/列数衡量，未涉及大规模数据量下的执行，也没有非结构化文本列上的语义判断（阅读者分析）。
