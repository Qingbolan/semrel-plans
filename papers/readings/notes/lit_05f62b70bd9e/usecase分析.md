# usecase

**用例：为含多个语义算子的查询选择连接与过滤顺序前先估基数**（§1、Figure 1，p.2）。

一个分析查询在 SemCEB 数据上包含 products⋈products 与 products⋈reviews 两个语义连接，每个关系先施加 2–3 个语义过滤；reviews 在过滤前约为 products 的 10 倍。所有谓词为合取，因此任何过滤/连接顺序结果相同，但中间基数不同。

- 若优化器使用固定 20% 连接选择率，会选择 ((products⋈products)⋈reviews)；
- 实际最优计划先做 products⋈reviews，因为 reviews 上的过滤高度选择；
- 96 个等价计划成本从 $0.119 到 $2.869（24.1×），过滤顺序单独错误也带来 1.43× 成本。

SemCEB 把这一需求拆成可评测的原子问题：例如 Table 1 中的过滤“review is positive”“no price mentioned”“rated above 4 stars”，连接“products are the same item”“A has more items than B”；估计器给出 ĉ 后与指定 LLM 实际执行得到的 c 比较 q-error，并计入估计花费的美元与秒数。

阅读者分析：对本项目而言，SemCEB 的查询是“单算子 + 基数”标签，而非端到端答案；若用于计划代价建模，应保留其“真值随模型/提示变化”的前提，不应把某一模型下的基数当作通用语义真值。
