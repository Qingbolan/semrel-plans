# 具体用例

**问题**（Fig. 1）：在 BigQuery 公共数据上，找出区域编号为 '6585'、位于美国州界内、且在北大西洋风速至少 35 节的已命名热带风暴（排除 'NOT_NAMED'）范围内出现次数最多的单个港口。

**流程**：

1. **压缩**：分组并保留相关表的描述与样本行，例如 `bigquery-public-data.noaa_hurricanes.hurricanes`、`bigquery-public-data.geo_us_boundaries.zip_codes`、`geo_international_ports.world_port_index`，附上 BigQuery UDF 等外部知识。
2. **候选生成**：多个线程分别给出 SOUTHPORT、CHARLESTON、PLYMOUTH 等不同答案。
3. **投票失败**：最高票出现平票，判为低置信。
4. **列探索**（4 个线程）：第一条探查 SQL 在 `SELECT DISTINCT` 中带 GEOGRAPHY 列 `port_geom` 报错，模型据此删除该列后重试；随后逐步查询区域 6585 的港口、筛出位于美国州界内的港口（如 QUONSET POINT, Rhode Island），统计 100 km 内 ≥35 节风暴点数（SWANSBORO 131、MOREHEAD CITY 130 等），最后给出 CHARLESTON。
5. **重新生成与投票**：基于探索结果重做候选，投票达成共识，输出 CHARLESTON。

阅读者分析：此例展示了方言/类型错误（GEOGRAPHY 不能 DISTINCT）通过执行反馈修正的过程；中间统计里 SWANSBORO 计数最高，而最终答案是 CHARLESTON，图中只节选了片段，无法从图中判断该差异如何解决。

依据：Fig. 1，§3.2.3，PDF pp.2、5–6；附录 D 为另一完整案例，PDF p.15 起。
