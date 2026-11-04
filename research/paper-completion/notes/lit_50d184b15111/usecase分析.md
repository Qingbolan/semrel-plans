# 具体用例

原文 §5.6.1 与 Fig.11（PDF p.13）给出 Movie 上 q8 的案例：查询要求统计“获得 2 项奥斯卡且评分高于 9”的电影数量（附录 F 中的 NL 描述为“Count the number of movies that has won 2 Oscars with rating higher than 9”）。

- 初始计划：两个 semantic_filter（Awards 列判断奥斯卡数、IMDB_rating 列判断评分）加一个 semantic_reduce 计数。
- 逻辑优化：(a) 随机交换两个 filter 的顺序（优化器不知道选择率）；(b) 把 NL 操作替换为计算函数，如把“whether the movie has ever won 2 Oscar”改写为 `lambda x: 'Oscar' in x and int(x.split('Oscar')[0].strip())==2`，计数改写为 `df.agg(len)`。
- 结果：运行时间与成本分别下降约 98% 与 89%。

失败案例（Fig.12，§5.6.2）：Estate 上从房产描述抽取价格并求平均时，生成的 UDF 只对部分记录正确（价格写法有“430 Million Naira”“N250m”等），reduce 也无法处理字符串；LLM-as-a-judge 因样本覆盖不足未能拦截。物理优化中 GPT-4o-mini 因与 GPT-4.1 给出相同的错误输出而被选中。

该案例说明非 LLM 替换收益很大但对数据格式异质性敏感，样本级等价检验无法保证全表正确。（阅读者分析）
