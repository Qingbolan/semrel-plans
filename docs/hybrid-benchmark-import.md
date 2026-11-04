# 语义算子 Benchmark 查询导入（2026-11-03）

`backend/scripts/import_hybrid_benchmarks.py` 从固定 commit 的上游仓库复制查询定义，写入统一查询表。所有记录保留上游原文和程序（`task_details.reference_programs`），并带逻辑 DAG，不执行查询：

- **自动转换**（`plan_origin=source_reconstruction`，356 条）：SWAN、PLOP、BlendSQL 的 SQL 由 `backend/scripts/sql_plans.py`（sqlglot 30.22.0）转换；ELEET 的算子对象与 SemCEB 的记录由 `backend/scripts/code_plans.py` 转换。语义调用映射：`ai_filter`/`semantic()`→SEM_FILTER，`ai_classify`→SEM_CLASSIFY，`ai_complete`/`semantic_int|string|double`/`LLMMap`/`ImageCaption`→SEM_MAP，`ai_agg`/`LLMQA`→SEM_AGG，`LLMJoin`/ON 中的语义调用→SEM_JOIN；ELEET 的 MMScan/MMUnion→SEM_MAP（文本抽取），MMJoin→SEM_JOIN，MMSelection→SEM_FILTER。确定性谓词画在语义谓词下方，只表示依赖，不代表引擎执行顺序。
- **人工重建**（`plan_origin=end_to_end_interpretation`，114 条）：TAG+ 40、CAESURA 24、DataAgentBench 50 只有问题或模板，DAG 依据问题与 schema 人工写成（`query/manual-plans/*.json`，用 `backend/atlas/reference_plans.py` 的计划记法），每条记录的 notes 保留重建依据和歧义说明。这些不是上游计划。
- 混合标签按 DAG 判定：同时含语义算子与非结构关系算子为“实质混合”，只有语义算子为“轻混合（仅投影）”，没有语义算子则不标。

| 集合 | 仓库与 commit | 条数 | 原文位置 | 参考程序 | 混合标签 |
|---|---|---:|---|---|---|
| SWAN 2.0 | [ZhaoFuheng/SWAN](https://github.com/ZhaoFuheng/SWAN) `0ba4c936` | 120 | `data/questions/<db>.csv` 的 question 列 | `queries/aisql/<qid>.sql`（AISQL）与 `queries/oracle/<qid>.sql` | 按 DAG：118 / 2 |
| SEMA-SQL TAG+ | [semasql/SEMA-SQL](https://github.com/semasql/SEMA-SQL) `b4866921` | 40 | `data/queries/tag_plus_queries.csv` | 无（仓库只给问题与答案）；DAG 人工重建 | 按 DAG：33 / 7 不含语义 |
| SemCEB | [utndatasystems/SemCEB](https://github.com/utndatasystems/SemCEB) `fec6bde7` | 102 | `benchmark_queries/queries.jsonl` 的 filter 字段 | 原记录（去掉 embedding） | 按 DAG：102 条只有语义算子 |
| PLOP agent_bench | [DMoRanSky/Morrila](https://github.com/DMoRanSky/Morrila) `56780d96` | 30 | 每个 `test/semantic/agent_bench/Q<n>.sql` 的 `-- Question:` 行 | 完整 SQL（含建表语句与 `semantic()` 调用） | 按 DAG：30 / 0 |
| BlendSQL benchmark | [parkervg/blendsql](https://github.com/parkervg/blendsql) `8a75abec` | 18 | `benchmark/<db>/queries/q<n>.sql` 全文（没有自然语言问题） | BlendSQL 查询 | 按 DAG：11 实质混合；financials 7 条只有确定性测试成分 |
| ELEET benchmark | [DataManagementLab/eleet](https://github.com/DataManagementLab/eleet) `4c2c70ae` | 86 | `eleet/benchmark.py` 中各 `get_<dataset>_queries` 返回的 `Query(...)`（新增 `python_return_item` 选择器） | 对应的计划定义（MMJoin/MMUnion/MMScan 等）与 Query 调用 | 按 DAG：64 / 22（corona 展开为 14 条） |
| DataAgentBench（缺失部分） | [ucbepic/DataAgentBench](https://github.com/ucbepic/DataAgentBench) `ac11ab68` | 50 | `query_<db>/query<n>/query.json`（JSON 字符串，新增 `json_value` 选择器） | `validate.py`（答案校验器，不是计划）；gold 为 `ground_truth.csv`；DAG 人工重建 | 按 DAG：21 / 29 不含语义 |
| CAESURA 模板 | [DataManagementLab/caesura](https://github.com/DataManagementLab/caesura) `00ebb188` | 24 | `scripts/run_experiment.py` 中的 `Template(...)` 字符串 | 模板定义；DAG 人工重建 | 按 DAG：12 实质混合 / 12 不含语义 |

## 边界

- 只复制查询定义文件到 `query/source-snapshots/<org>/<repo>/<commit>/`；BIRD 数据库、Amazon 数据和模型输出都没有下载，数据 manifest 标为 `not_downloaded`。
- 原文通过选择器回指快照（新增 `csv_row` 选择器），构建时按 SHA-256 校验。
- CAESURA 论文的 48 条是从模板随机采样得到的实例，仓库没有发布这些实例，所以只收录 24 个模板，覆盖表中记为 24/48。
- SemBench 上游 HEAD `c4b2bcff` 相对图册固定的 `8c2cac89` 只改了 README 与 docs，查询没有变化。仍未收录 medical/Q11 与 Q7_filter，因为它们只有 BigQuery 方言，没有自然语言版本。
- DataAgentBench 只导入 7-30 中没有的 5 个数据集（civic_unstructured、cve、imdb、krama、usaspending）；其余 54 条保留原 7-30 / DAB 记录，不重复。
- QUEST 的双表 / 多表 join 实验查询没有公开（匿名仓库无法读取，GitHub 无公开仓库）。
- PLOP 论文的另外 14 条是 SemBench E-Commerce 查询，已由图册中的 SemBench ecomm 记录覆盖，没有重复导入。
- 没有公开查询、因此未收录：CoreSemDB（OpenReview 附件返回 403）、Sema（仓库链接无法访问）。

重建：把八个仓库按上表 commit 检出到同一目录，安装 `backend/scripts/audit/requirements.txt` 中的 sqlglot，运行 `PYTHONPATH=<依赖目录> python3 backend/scripts/import_hybrid_benchmarks.py <目录>`，再运行 `npm run build`。脚本只替换自身前缀（`swan/`、`sema-sql/`、`semceb/`、`caesura/`、`plop/`、`blendsql/`、`eleet/`、`dataagentbench/`）的记录，重复运行结果不变。
