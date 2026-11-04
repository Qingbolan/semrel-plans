# 工作负载

数据来自 BIRD 的 9 个数据库（Table 7，附录 C，p.18）：

| 数据库 | 表（行数） | 语义列 | 查询 |
|---|---|---|---|
| Appstore | user_review 10,840；playstore 64,286 | Translated_Review | Q7、Q8 |
| Chicago_Crime | IUCR 401 | primary/secondary_description 等 | Q3 |
| Superstore | product 5,298 | productName、category | Q2 |
| Food_Inspection | violations 36,050 | description、risk_category | Q4 |
| Food_Inspection_2 | violation 525,709 | inspector_comment、fine | Q5 |
| Social_Media | 3 表，twitter 99,901 等 | twitter.text | Q1、Q9、Q16–Q18 |
| Movies_4 | 7 表，movie 4,627 等 | movie.overview | Q10、Q13–Q15 |
| CoinMarketCap | coins 8,927；historical 4,441,972 | coins.description | Q6、Q11、Q12 |
| Authors | 5 表，Paper 2,254,920 等 | Paper.Keyword、Paper.Title | Q19、Q20 |

语义列为评论、描述、推文、电影简介、论文标题/关键词等文本列。部分查询带 LIMIT（如 Q1 取 32,768 条推文，Q5 取 16,384 条），所以表行数不等于实际 LLM 处理行数。

查询共 20 条，按 Table 8：Q1–Q5 单算子；Q6–Q10 连续 2–3 个 SemFilter；Q11–Q13 Proj→Filter；Q14–Q15 Proj→Proj；Q16–Q18 Filter→Proj；Q19–Q20 Filter→Agg。正文 §7.1 的分类句把 Q14–Q15 写了两次，与 Table 8 不一致，以表为准。

真值：Q1–Q5 来自原数据集已有标签（如情感分数、风险类别）；Q6–Q20 的"真值"是参考 LLM（默认 Gemma-3 27B）的推理结果（§7.1，p.8）。阅读者分析：因此 Q6–Q20 的质量指标衡量的是与更大模型的一致度，而非人工标注正确率。

AQE 案例 Q6：δ1=1/32 样本 27 行，δ2=3/32 样本 84 行（§7.5，p.11）。
