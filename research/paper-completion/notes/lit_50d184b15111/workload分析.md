# 工作负载

| 数据集 | 记录数 | 属性数 | 模态 | 来源 |
|---|---|---|---|---|
| Movie | 250 | 22 | 数值、文本、图像 | OMDB，HuggingFace MovieRatingDB |
| Estate | 1,041 | 4 | 图像、长文本 | HuggingFace multimodal-real-estate-search |
| Game | 18,891 | 21 | 日期、数值、图像、文本 | Steam 游戏数据（GitHub） |

（Table 3、§5.1.1，PDF pp.8–9）

每个数据集构建 12 条查询，按算子数分三组：Small（q1–q4，单算子，通常处理全表）、Medium（q5–q8，2–3 个算子）、Large（q9–q12，≥4 个算子，通常输出单个值以便比较质量）（§5.1.2，PDF p.9）。

查询全文在附录 F（PDF pp.17–20），例如“Count the number of movies directed by Quentin Tarantino”写成 semantic_filter + semantic_reduce。质量真值为人工标注，指标为 12 条查询中答对的比例（§5.2.4）。

其他设置：执行后端 gpt-4.1-nano、gpt-4o-mini、gpt-4.1-mini、gpt-4.1；逻辑优化用 gpt-4o；N_max=3，ε=0.8，ΔI_min=20%，样本比例 5%，最多 16 个协程（§5.1.4）。

查询由作者自建、每数据集仅 12 条，没有训练/测试划分；单查询答对与否直接决定 8.3 个百分点的质量差。（阅读者分析）
