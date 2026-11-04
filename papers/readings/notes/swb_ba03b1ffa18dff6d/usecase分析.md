# 具体用例

**Fig.4 案例（p.9；§4.6）**：表格列出 NAACP 形象奖历年获奖者，列为 Year、Actor、Motion Picture、Nominees 等；问题为"哪位演员获得的 NAACP 形象奖最多？"

| 迭代 | 操作 | 参数 | 中间表 |
|---|---|---|---|
| 1 | `f_select_column` | Year, Actor | 只保留年份和演员两列 |
| 2 | `f_group_by` | Actor | 每位演员一行，附 Count |
| 3 | `f_sort_by` | Count，降序 | Morgan Freeman（4）排第一 |
| 4 | `[E]` | — | 进入最终查询 |

最终查询基于中间表 3 回答 "Morgan Freeman"（Fig.4，p.9）。

**Fig.1 案例（p.2）**：问题为"哪个国家前三名的车手最多？"，国籍嵌在 Cyclist 单元格中。Chain-of-Table 依次执行 `f_add_column(Country)` 抽出国籍、`f_select_row(1,2,3)`、`f_group_by(Country)`、`f_sort_by(Count)`，得到 Italy。通用 CoT 错答 Spain；生成的 SQL 因无独立国家列而无法执行。

阅读者分析：第一步抽国籍时由 LLM 生成整列单元格值（"ESP, ITA, …"），这是一种行级语义抽取，正确性依赖 LLM 而非程序。若把该方法用于语义查询场景，应把这一步单独视为 LLM 语义算子，而不是确定性的表操作。
