# workload

**数据库**（§3.1、Table 1，pp.2–3）：从 BIRD 的 11 个库中选 4 个；删去过于专门、通用模型无法回答的库（如金融）。

| 数据库 | 表数 | 平均每表行数 | 删除列数 |
|---|---|---|---|
| European Football | 7 | 31,828 | 12 |
| Formula One | 13 | 39,561 | 12 |
| California Schools | 3 | 9,980 | 12 |
| Superhero | 10 | 1,061 | 11 |

（Table 1 统计为“模式整理后”的库；列名为 Tables、Rows/Table、Cols Dropped，表格按 layout 文本读取。）

**问题**（§3.5，p.3）：每库 30 题，共 120 题；每题配有物化表式混合 SQL、BlendSQL 混合 SQL、BIRD 金 SQL。问题来源于 BIRD 问题，经修改数据库使其变为 beyond-database。题型涉及取值选择（如出版商）和自由生成（如学校网址、由地址推城市）。论文正文未给出题型分布的完整统计，只给出 California Schools 约 1/3 题含 LIMIT、Superhero 约 1/10 题含 LIMIT（p.6）。

**生成规模**：HQDL 零样本总计输入 6.3M、输出 1.5M token，平均每题约 52k 输入、12k 输出；HQ UDF 零样本输入 23M、输出 2M（Table 5，p.7）。

**示例/划分**：没有训练/测试划分；few-shot 示例为从原库随机选取的静态行（HQDL）或每库人工整理的问答对、由 BlendSQL 按句向量相似度挑选（HQ UDF）（§5.2、§5.4，pp.5–6）。

**与本项目查询的关系**：本 atlas 引用该论文的 120 条查询（`swan/<db>/…`，四库各 30 条）来自作者 SWAN 仓库的 questions CSV，数量与论文 §3.5 的 4×30 一致（阅读者推断，逐题对应未核对）。
