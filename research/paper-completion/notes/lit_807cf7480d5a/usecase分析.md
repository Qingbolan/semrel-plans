# 具体用例

Figure 1 与附录 Figure（数据样本示例）给出的电影表用例（§1，pp.1–2；附录 B，p.30）：

- **数据**：Movies 表含 Title、World Gross、Local Gross、Genre、Creative Type、Date 等列。歧义元数据记录“gross/income/revenue”可指 World Gross 或 Local Gross，“movie style”可指 Genre。
- **查询**：“Show the gross trend of comedy and action movies by year.”
- **逐步消歧**：数据选择（World Gross 或 Local Gross，并按 Genre 过滤 Comedy/Action）→ 图表类型（“trend”可为柱状图或折线图）→ 通道映射（x = 按年分箱的 Date，y = 聚合后的 gross，color = Genre）→ 数据变换（按年分箱，y 的聚合方式如 AVG 或 MAX 未指定）→ 合成多个合理可视化。
- 附录示例的变体“Show the trend of mean gross of comedy and action movies by year”被标为歧义水平 K=4。

附录 E 的错误示例也具代表性：对“games played by team 的分布”，错误推理对行计数（COUNT(*)），正确做法是对 game_played 求和或平均（附录 E.1，pp.32–33）。

阅读者分析：对语义查询系统而言，此用例说明“返回一个答案”不足以评测，应输出候选集合并按集合覆盖与精度评分；歧义来自列别名、隐式过滤、隐式聚合和图形编码四个层面。

依据：§1、Figure 1，PDF pp.1–2；附录 B 示例与 E.1，PDF pp.30–33。
