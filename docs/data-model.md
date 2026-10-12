# 统一数据模型 v1

`data/*.jsonl` 是唯一事实来源；一行一条记录，UTF-8。场景索引、CSV、SQLite、图册均引用或派生自这些表。查询 ID 不依赖展示顺序，节点 ID 在查询内唯一。当前所有树按原图逐节点迁移，没有根据相同标签擅自合并节点。

| 表 | 粒度与主键 | 关键字段 |
|---|---|---|
| queries | 每个来源查询的一个整理计划；query_id | benchmark_id、scenario_id、source_query_id、plan_origin、source_id、root_node_id、title、notes |
| nodes | 一个逻辑计划节点；(query_id,node_id) | operator_type、label |
| edges | 一个有序输入槽；(query_id,parent_id,input_position) | child_id |
| sources | 一个来源位置；source_id | location、original_location、source_type |
| config/operators.json | 一类算子；operator_type | family：input / relational / semantic |

`query_id` 初始分配为 benchmark/scenario/source-query-id，后续改名不应重新分配 ID。`source_query_id` 可以含 `/`，不要通过拆分 query_id 反推出字段。`source_id` 为原始来源字符串 SHA256 的前16位前缀标识，校验拒绝重复键。来源内容版本/hash沿用 docs/provenance 中的固定版本收据。

边方向为 parent（消费输入的算子）→ child（输入算子）；input_position 从0连续编号，保留左右连接输入次序。模型允许有共享子节点的 DAG，拒绝环、悬空节点和根不可达节点。图册将 DAG 展开为树，仅统计 nodes 表中的唯一节点。不同查询中相同子计划分别统计；不声称它们已被跨查询物化复用。CTE_REF 目前保留原图节点，其标签不自动变成已解析的共享边。

`operator_type` 是受控枚举，参见 [算子字典](../config/operators.json)。例如 FILTER、PROJECT、JOIN、LEFT_JOIN、AGGREGATE、SORT、SEM_FILTER、SEM_MAP、SEM_JOIN、SEM_TOPK。SEM_CLASSIFY 保留其原始独立类型，不隐式并入 SEM_MAP。label 保存原始展示语义，尚未将谓词、列引用解析成可执行表达式 AST。

## 查询口径

plan_origin 必须为以下之一：

- source_reconstruction：依据源查询重建。
- baseline_reconstruction：依据手写基线重建。
- end_to_end_interpretation：包括原 SQL 之外的语义抽取阶段。
- proposed_missing_sql：源 SQL 缺失的拟议计划。
- intent_sql_mismatch：自然语言意图与 SQL 存在差异。
- derived_workload：本地派生工作负载。

`local-derived` 是归档类别，不是一个上游 benchmark。UDA 的统计包含端到端解释节点；可用 plan_origin 单独筛选，不能混称为原 SQL 的原生语义算子。group_label、mixed_label、plan_status_label、display_order 仅保留图册展示信息；统计以独立字段和算子字典为准。mixed_label 保留原人工“实质/轻混合”口径，不把它当作已验证的复杂度指标。

## 导出与统计

运行 `python3 scripts/build.py` 会重建 exports/ 与图册。exports/ 是派生产物，不手工修改。

- queries/nodes/edges/sources/operators.csv：统一表格导出。
- catalog.sqlite：上述五表和两个统计视图。
- query_statistics.csv：每查询节点数、按family节点数、不同算子类型数。
- operator_statistics.csv：每benchmark每算子的节点出现数和查询覆盖数。
- summary.json：整体规模。

SQL 示例：

```sql
-- 哪些查询同时包含语义连接与结构化连接？不分析 label 文本。
SELECT q.query_id, q.title
FROM queries q
WHERE EXISTS (SELECT 1 FROM nodes n WHERE n.query_id=q.query_id
              AND n.operator_type IN ('SEM_JOIN','SEM_LEFT_JOIN'))
  AND EXISTS (SELECT 1 FROM nodes n WHERE n.query_id=q.query_id
              AND n.operator_type IN ('JOIN','LEFT_JOIN','SEMI_JOIN','ANTI_JOIN','CROSS_JOIN'));

-- 基于源查询或手写基线的各类算子覆盖，排除端到端解释和拟议任务。
SELECT q.benchmark_id, n.operator_type,
       COUNT(*) AS node_count, COUNT(DISTINCT q.query_id) AS query_count
FROM queries q JOIN nodes n USING(query_id)
WHERE q.plan_origin IN ('source_reconstruction','baseline_reconstruction')
GROUP BY q.benchmark_id,n.operator_type;
```

这些数值只描述整理的逻辑计划，不是推理调用数、token成本、执行性能、质量或独立数据集数量。数据规模、运行成本和模型质量没有测量，不填0。


## 来源归属（2026-10-12）

`queries.source_id` 指向具体查询定义或实现；`query_sources(query_id, source_id, role)` 为其附加论文、底层数据或规则协议。`role` 为 paper/dataset/protocol；locator 指章节或任务编号，attribution_note 说明该来源能支持什么及缺口。三元组唯一，引用须存在；每条查询须有论文或协议依据，以及数据来源（协议型候选允许明确记录数据缺口）。

`sources` 统一保存 title、version、verification、checked_on。外部数据链接可能仅由论文参考文献确认，此状态明确保留，不等同原始数据下载验证。元数据与关系一起导出 CSV/SQLite，查看器和文字计划从同一关系表生成。

论文来源的 `publication_label` 保存会议/论坛简称与年份（如 `VLDB2026`），`publication_url` 指向发表信息依据；二者与被引用的 `version` 独立，会议年份不替换 arXiv 版本年份。Findings 单独注明。非论文来源为空。
