# EAL 逻辑计划导出

运行 `python3 backend/scripts/build.py` 会为具有 logical_dag 的查询生成 `exports/eal/*.eal`、`manifest.json` 和 `exports/eal.zip`，离线网页使用由真实 EAL 编译器产生的同一份构建快照。文件名是完整 query_id 的百分号编码，避免来源查询 ID 内的斜杠造成路径歧义。

每个唯一逻辑节点生成一个 `semrel.<operator_type 小写>` ability 调用，设备占位符为 `semrel-worker`。输入按原 `input_position` 编码为顶层参数 `input_0`、`input_1` 等，引用子节点绑定的 `.output`。共享子节点只生成一次；根节点通过 `emit "result" kind answer` 导出。每步明确使用 `on_failure abort`。

静态参数保留 query_id、node_id、operator_type、family、label 和 plan_origin。来源关系继续由规范化数据表维护。EAL 不推测 label 内的谓词，也不自动解析 CTE_REF 的文字引用。

这些文件是可编译的逻辑计划表示，不是已执行查询。运行前需要实现并注册 目录中登记的 SemRel abilities、绑定真实设备和数据源，以及定义表达式、关系输出、NULL、重复行、排序和语义推理契约。编译成功仅证明 EAL 语法和依赖可以构建，不证明 ability 存在或查询语义已执行。

验证：`python3 -m unittest discover -s tests`。安装 easynet 时，测试将调用真实 `easynet mission compile --emit-ir`，逐条核对全部节点、标签、算子和有序输入，并验证共享 DAG 与字符串转义；没有编译器时这两项测试明确跳过。

## 实时读取与导入

`python3 backend/scripts/serve.py --port 8765` 提供图册与只编译接口。`GET /api/plan?query_id=...` 按生成清单读取磁盘文件并编译；`POST /api/compile` 接收 `{ "source": "..." }`，在临时目录中编译导入的 EAL，不保存到查询目录。文件最大 1 MiB，编译超时 15 秒；编译错误返回原始源码和诊断，前端清除旧图。

`backend/atlas/eal_reader.py` 负责编译器边界和 IR 图投影；`backend/atlas/server.py` 负责本地 HTTP；`frontend/reader.js` 管理 idle/loading/ready/error 生命周期并取消过期请求。前端只读取 Mission IR，不另写 EAL 解析器。图按 phase 显示唯一调用节点，命名输入端口保留共享依赖；不支持的 loop 结构明确拒绝。来源和左侧目录统计对应规范化查询快照，右侧节点统计对应当前 EAL 编译结果。

reference_program 任务没有可编译依赖图，不生成 EAL，也不调用编译接口；选择这类任务会清除旧图并进入 reference 状态。

## 8-17 与 7-30 参考计划整理

两套集合的 3,348 条参考描述均转换为规范化逻辑 DAG，并通过同一 EAL 导出器生成源码。8-17 共 228 条、1,831 个逻辑节点；7-30 共 3,120 条、6,398 个逻辑节点。原始参考计划、答案、评估和分析证据继续保存在 task_details，网页可同时查看“逻辑计划”“EAL 源码”“参考计划”和“原始 JSON”。

`backend/atlas/reference_plans.py` 只解析计划结构：顶层箭头、命名分支、赋值、显式左右输入和嵌套 JOIN。字符串和括号内的谓词保持原文，原计划里的未转义英文所有格也原样保留。共享分支只生成一次；多个末端结果通过 PROJECT 打包为命名结果，不作为 UNION 合并。未知语法直接报错，不猜测依赖。

映射：SCAN_TABLE / SCAN_DOCS → SCAN；ORDER_BY → SORT；GROUP_BY → AGGREGATE；DEDUP → DISTINCT；SEM_EXTRACT → SEM_MAP；SEM_AGGREGATE → SEM_AGG；SEM_GROUP_BY 独立保留。LEFT / CROSS JOIN 使用对应关系算子。每个节点 label 保留参考表达式；EAL 同时携带查询文本。

7-30 的自然语言分析阶段保持原粒度，例如“relational/SQL/Python analysis only”仅映射为一个 COMPUTE 节点；SEM_JOIN 若未提供两路关系分支，也不虚构扫描输入。该集合的图是最小计划描述的结构投影，不是完整的关系代数执行计划。以上节点数不能当作实际执行工作量或与细粒度计划直接比较。

重新整理：`python3 backend/scripts/lower_reference_plans.py`，随后 `python3 backend/scripts/build.py`。重新导入集合时也会调用相同转换器。query/imports 与 task_details 的原始证据不被改写。编译验证只证明语法与引用有效，未执行能力、查询或验证 gold。

字符串契约：导出参数声明 `string_encoding = "json-string-content-v1"`。EasyNet IR 原样保留 EAL 字符串转义；SemRel 展示层通过 `backend/atlas/eal_strings.py` 对声明该编码的参数解码一次，能力实现也应遵守同一契约。未声明的外部 EAL 参数保持原样。IR 本身不被改写。

服务每次请求读取当前已发布的 EAL 清单，新增或移除查询无需重启服务。构建以原子替换发布每个 EAL 文件，随后发布清单，避免暴露半写入文件。读取失败、清单问题、文件问题、编译器忙和编译失败分别提示；查询页提供“重新加载”按钮。更新服务代码本身仍需重启 Python 进程。
