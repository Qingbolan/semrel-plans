# 具体用例

用例：“What is the average height of New York Knicks players that went to college at Villanova?”（Fig. 2(b)、Fig. 4，PDF pp.2、8；§5.2 预取例，p.9）。

1. 编排：LLM 生成若干链式流水线，例如 Retrieve → Extract → Validate → Aggregate → Generate，改写为 DAG 后合并，每个分支以 Explain 结尾，最后由 Integrate 汇总。
2. 分层执行：第一层并行执行两个 Retrieve。R1 检索“上过 Villanova 的尼克斯球员”，未拿到目标信息；R2 检索“尼克斯球员”，成功。
3. 调整：提前终止 R1 之后的步骤，沿 R2 分支继续，抽取上过 Villanova 的球员（Josh Hart 1.93 m、Jalen Brunson 1.88 m、Donte DiVincenzo 1.93 m），再用 Aggregate 求平均，得到 1.91 m。
4. 预取：生成 Retrieve 查询时，同时生成 O1–O4 等不同粒度的候选查询（例如“Villanova 出身的 NBA 球员”“尼克斯球员”），在后台检索。主查询失败、流水线调整后可直接使用预取结果，减少延迟。

阅读者分析：这个例子本质上是语义过滤 + 抽取 + 聚合，AOP 用检索代替了全表扫描。如果数据湖中的相关记录很多，Retrieve 的召回率会直接决定 Aggregate 是否正确，而原文没有单独评测召回率。
