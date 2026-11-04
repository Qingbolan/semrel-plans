# 具体用例

**原文示例 1**（附录 A 与 C，Match 类，PDF pp.8–9）：“经度最高、且位于硅谷地区城市中的学校提供什么年级范围？”手写 TAG 管道（LOTUS）：

```python
schools_df = pd.read_csv("../pandas_dfs/california_schools/schools.csv")
unique_cities = pd.DataFrame(schools_df["City"].unique(), columns=["City"])
sv_cities = unique_cities.sem_filter("{City} is a city in the Silicon Valley region")
schools_df = schools_df[schools_df["City"].isin(sv_cities["City"])]
schools_df = schools_df.sort_values(by=["Longitude"], key=abs, ascending=False).head(1)
prediction = schools_df["GSoffered"].tolist()[0]
```

先取不重复的城市，只对城市列做语义过滤（判断是否属于硅谷），再回到学校表保留这些城市的学校，按经度绝对值降序取 1 行，返回 GSoffered。传给语义算子的是城市列，而不是所有学校字段。

**原文示例 2**（Ranking 类，p.10）：先按 ViewCount 取前 5 个帖子，再用 `sem_topk("What {Title} is most technical?", 5)` 按技术程度排序。这里 5 是候选数与结果数。

**原文示例 3**（Aggregation 类，p.10）：按标题定位帖子，以 `posts.Id = comments.PostId` 连接评论，再用 `sem_agg("Summarize the comments", all_cols=True)` 汇总。

**聚合问题的定性对比**（Figure 2，p.5）：问题“介绍在雪邦国际赛道举办的比赛”。RAG 只检索到部分比赛（列出 2000–2003 年）；Text2SQL + LM 没用上数据库数据，只凭模型知识作答；手写 TAG 列出 1999–2017 年每届比赛的日期与轮次。

阅读者分析：示例 1 把“经度最高”实现为按经度绝对值降序；加州经度为负数，按绝对值最大实际取的是最西边的学校，这是管道作者的解释，原文未说明（阅读者分析）。

依据：附录 A、C，Figure 2，PDF pp.5、8–10。
