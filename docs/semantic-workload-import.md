# 来源项目的论文与查询整理

`semantic-workload-bench` 是导入项目名，不作为 benchmark 或论文集合显示。

833 条来源记录逐项保留：785 条原图册记录、46 条公开任务字段、BioDEX 指令和病理任务定义。按真实来源整理后新增 766 条查询，67 条关联同一数据范围内已有记录，当前图册共 4202 条。此前跨开发版本合并的 17 条任务已恢复各自的输入和环境。

## 目录组织

- 官方查询归入 SemBench、UDA-Bench、QUEST、DataSpace；SemBench 现为 70 条，UDA-Bench 按源码文件与查询序号完整收录 608 条（602 种 SQL，保留源码中的重复位置），QUEST 83 条不同查询（来源列表 84 条，包含同一文件内重复文本）。
- 项目派生任务归入底层数据集的 `· Derived` 集合；不标为论文原题。
- Palimpzest、LOTUS 的实现流程归入各自的 `· Examples` 集合。
- 每个集合独立顺序编号；原查询 ID、原文、输入工作区及来源快照保留。
- 数据和环境使用实际集合与任务工作区目录。同一请求的多个开发版本、审核包或验证/演示/评测工作区只保留一条查询（2026-11-03 决定）：已有逻辑 DAG 的保留 DAG 版本，否则保留最新的公开版本；其余版本在 `config/workload-registry.json` 中以 `superseded_by` 标明，其任务定义与来源快照作为保留查询的来源依据，导入收据记为 `superseded`。
- 公开任务的分类显示为 Derived tasks / Repository queries；工作区路径只用于定位环境，不作为分类名。

## 论文归属与阅读记录

`config/workload-registry.json` 显式列出每条来源记录的集合、任务性质、论文 URL、关系及证据文件；不再用标题子串或同轮文档中出现的全部论文推断查询归属。

已纠正 QUEST 对其他 Question Answering 论文的误关联。PARSEME 任务对应实际使用的 1.2 发布；MAVEN-ERE 对应关系标注论文；AAEC 基础任务不混入语义类型扩展任务。数据集论文和项目派生任务通过 `dataset_origin` 关联，系统代码示例使用 `system_implementation`，仓库查询使用 `query_source`。

238 个文献来源链接保留原始来源身份；`config/paper-identities.json` 将已确认的同篇预印本、正式版本及作者副本合并为一个论文页面，并记录标题修正。来源数不是独立论文数。

论文页面提供“查询清单”“研究记录”“环境与输入”。研究记录展示来源项目的既有文档正文与依据；它们保留原有研究结论和适用范围，不代表重新完成了每篇原论文的独立全文评审。仅被研究文档引用、没有明确查询定义的文章保留文献和研究记录，不补造查询。

## 可核对文件

- `config/workload-registry.json`：833 条查询的明确归属。
- `config/paper-identities.json`：论文标题与同篇链接。
- `exports/uda-source-coverage.json`：UDA-Bench 固定版本 43 个 SQL 文件、608 个查询位置的逐条核对收据。
- `exports/semantic-workload-import.json`：逐条导入结果、归属和文件哈希。
- `query/imports/semantic-workload-bench/records/`：逐条来源记录，包括来源项目的图和属性。
- `query/imports/semantic-workload-bench/sources/`：来源文件快照。
- `query/imports/semantic-workload-bench/literature.json`：文献与研究文档关系。

重建：先运行 `PYTHONPATH=/tmp/semrel-audit-deps python3 backend/scripts/import_workload_project.py https://github.com/Qingbolan/semantic-workload-bench`，再运行 `npm run build`。依赖见 `backend/scripts/audit/requirements.txt`。来源项目保持只读。
