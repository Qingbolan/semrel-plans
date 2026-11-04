# 工作负载

评测只有 6 个案例，覆盖 5 个数据集（§3.4，p.8）：

| 案例 | 数据集（来源） | 查询 | 对照 |
|---|---|---|---|
| 1 | nvBench department_store 的 products 表（4 列） | "What is the highest price of product, grouped by product type? Show a bar chart, and display by the names in desc." | nvBench 真值图；nvBench 标为 easy |
| 2 | NL4DV colleges | "Show debt and earnings for Public and Private colleges." | NL4DV |
| 3 | ADVISor Energy Production（2000–2011） | "What is the trend of oil production since 2004?" | ADVISor、NL4DV |
| 4 | nvBench customers_and_products_contacts 的 products 表 | "Show the number of products with price higher than 1000 or lower than 500 for each product name in a bar chart, and could you rank y-axis in descending order?" | nvBench 真值图；标为 Extra Hard |
| 5 | NL4DV movies（1996–2010） | "draw the numbr of movie by gener"（拼写错误） | 无 |
| 6 | 同上 | "tomatoes"（极度欠指定） | 无 |

来源：§4.1–4.6，pp.8–12。

**评测单位**：一个案例对应三个 LLM 生成的三张图。由作者目视判断是否正确、是否合适（§3.4，p.8）。论文没有使用 nvBench 的完整查询集，没有给出数据规模、划分或重复次数，只说明 LLM 的不确定性会导致重复提交时出图不同（p.8）。

依据：§3.4、§4，pp.8–12。
