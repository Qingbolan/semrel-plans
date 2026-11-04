# 具体用例

Table 4 的案例（world_1 数据库，§4.2.4，pp.7–8）：

- **问题**：“Return the names and surface areas of the 5 largest countries. Visualize by a pie chart.”
- **金标准 DVQ**：`VISUALIZE PIE SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 5`

| 方法 | 生成结果 | 问题 |
|---|---|---|
| Seq2Vis | `VISUALIZE BAR ... FROM hiring ...` | 表名错误，无法出图 |
| Transformer | `... FROM appellations ...` | 表名错误，无法出图 |
| ncNet | `SELECT Name, COUNT(*) FROM country` | 表对，但聚合错 |
| RGVisNet | `SELECT Name, SurfaceArea FROM country` | 缺少 `ORDER BY SurfaceArea DESC LIMIT 5` |
| Prompt4Vis | 与金标准一致 | 正确 |

作者解释 RGVisNet 缺少排序与截断可能是因为训练集中这种表达少见（§4.2.4，p.8）。同一问题也出现在 Figure 2 的模式过滤示例里：world_1 包含 city、sqlite_sequence、country 三表，过滤后只需 country（Figure 2，p.3）。

阅读者分析：此例说明两个模块的作用——模式过滤避免选错表，示例挖掘提供含 ORDER BY ... LIMIT 的相似示例；但单个案例不能代表整体错误分布。

依据：§3、§4.2.4、Figure 2、Table 4，PDF pp.3、7–8。
