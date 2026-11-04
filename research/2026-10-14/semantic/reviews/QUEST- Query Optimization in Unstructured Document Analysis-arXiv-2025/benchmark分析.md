# 基准评测

| Table2/3 | QUEST F1 | LOTUS F1 | QUEST tokens/文档 | QUEST秒/文档 |
|---|---|---|---|---|
| Wiki | 0.87 | 0.90 | 170 | 1.12 |
| SWDE | 0.95 | 0.96 | 190 | 1.21 |
| LCR | 0.72 | 0.45 | 2030 | 2.68 |

token包括sampling成本，时延是每文档均值；不要把2.68s标成整批500文档响应时间。正文§5.2有将LCR F1近似写成0.7等叙述，表2是本记录的精确数值依据。

过滤顺序比较Random、Selectivity、Average_cost、Exhaust；join比较Pushdown、Random和拥有真实selectivity的Optimal。图6显示接近穷举成本而搜索更快，图7显示join转filter有效；图8消融两级索引、证据、阈值、采样比例、聚类数。未独立重跑这些实验，也未从论文正文确认完整硬件/模型版本。

来源：[QUEST: Query Optimization in Unstructured Document Analysis](https://arxiv.org/abs/2507.06515v2)。
