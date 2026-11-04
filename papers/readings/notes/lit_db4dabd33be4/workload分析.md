# 工作负载

**评测环境**（§9，p.6）：D-Bot 与基线都用 OpenAI GPT-4，接入 PostgreSQL 的指标/视图和 Prometheus。正文未说明数据库规模、负载生成方式、异常注入方式和每类根因的案例数。

**根因集合**（Table 1，p.6，已渲染核对）：11 种单一根因，分三组。

| 类型 | 根因 |
|---|---|
| 数据插入 | INSERT_LARGE_DATA |
| 慢查询 | FETCH_LARGE_DATA、REDUNDANT_INDEX、LACK_STATISTIC_INFO、MISSING_INDEXES、POOR_JOIN_PERFORMANCE、CORRELATED_SUBQUERY |
| 并发事务 | LOCK_CONTENTION、WORKLOAD_CONTENTION、CPU_CONTENTION、IO_CONTENTION |

**多根因示例**（附录 B，p.10）：一个 WORKLOAD_CONTENTION + POOR_JOIN_PERFORMANCE 的测试案例，展示 Chief DBA、CPU Agent、Memory Agent 逐轮调用 `obtain_cpu_metrics`、`knowledge_matching`、`obtain_slow_queries` 等工具的记录。其中慢查询是一个多表 JOIN 的 `SELECT MIN(mi.info) ...`，涉及 cast_info、movie_info、keyword 等表。

**文档来源**（§4，p.4）：Figure 3 的经验来自一份"超过 100 页的维护指南"中不同章节，未给出文档名称或总规模。

阅读者分析：附录 B 的表名看起来来自 IMDB/JOB 类模式，但论文没有说明所用数据集，此处不作认定。

依据：§4、§9、Table 1、附录 B，PDF pp.4、6、10。
