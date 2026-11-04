# 逐查询输入与环境核对

[全量清单（CSV）](../exports/query_inputs.csv) · [来源缺项与版本差异](../exports/input_audit.json)

每条查询在 `query/input_contracts.jsonl` 中有独立记录，页面不再根据 SCAN 节点临时拼输入，也不再把引擎、模型、硬件配置当成辅助环境资料。

- `source_checked`：从该条 SQL、函数或提供的参考计划读取输入定义，不表示已执行。
- `declared_files`：来源只声明可用文件、基础问题的输入表或数据库结构；不冒充该题实际读取的最小列集合。
- `source_gap`：已检查来源，但缺少可定位的表列或来源 SQL 为空。
- `version_mismatch`：相同 task ID 的问题文本已经变化，不能当作旧题完整核验。
- `interpreted` / `local_definition`：文档抽取解释或本仓协议定义，不是原论文执行记录。

来源包括固定提交的 SemBench/TAG-Bench/UDA-Bench 源码、提供的 8-17 逐题记录、本地 Benchmark/code 中的任务及参考代码，以及 Hugging Face 的固定版本任务文件。FDABench 使用 `46bcbbbaca95defddb99e411931763a47b3f5b65` 版本，逐条检查问题文本与 7-30 记录一致。LongDA 的数据/资料目录来自 `1365b6ab65bba290c83c7bcbb2c9bcb70a79ddd4` 的文件清单。

每条证据含路径、定位及 SHA-256。源文件保存在 `query/source-snapshots/`；上游代码仅供静态核对，不执行。SQL 表列提取使用 AST 与作用域，人工补充源 SQL 中无限定符的商品字段以及自连接输入关系。空 SQL 不生成不存在的上游定义。

复核脚本：安装 `scripts/audit/requirements.txt` 后运行：

```sh
python3 scripts/audit/contracts.py --upstream /path/to/Awesome-Dymatic-Operator/Benchmark/code
python3 scripts/build.py
```

LongDA 的调查资料表没有逐题变量代码或参考 SQL；DABstep 公布任务、数据和手册，没有逐题执行清单。页面区分提供的数据集与可由源码确认的实际读取表列。KramaBench 逐题列出 `data_sources`，同时保留参考步骤、代码列引用和源码，以免把派生列误写为输入字段。
