# EAL 逻辑计划导出

运行 `python3 scripts/build.py` 会为全部查询生成 `exports/eal/*.eal`、`manifest.json` 和 `exports/eal.zip`，离线网页使用由真实 EAL 编译器产生的同一份构建快照。文件名是完整 query_id 的百分号编码，避免来源查询 ID 内的斜杠造成路径歧义。

每个唯一逻辑节点生成一个 `semrel.<operator_type 小写>` ability 调用，设备占位符为 `semrel-worker`。输入按原 `input_position` 编码为顶层参数 `input_0`、`input_1` 等，引用子节点绑定的 `.output`。共享子节点只生成一次；根节点通过 `emit "result" kind answer` 导出。每步明确使用 `on_failure abort`。

静态参数保留 query_id、node_id、operator_type、family、label 和 plan_origin。来源关系继续由规范化数据表维护。EAL 不推测 label 内的谓词，也不自动解析 CTE_REF 的文字引用。

这些文件是可编译的逻辑计划表示，不是已执行查询。运行前需要实现并注册 29 类 SemRel abilities、绑定真实设备和数据源，以及定义表达式、关系输出、NULL、重复行、排序和语义推理契约。编译成功仅证明 EAL 语法和依赖可以构建，不证明 ability 存在或查询语义已执行。

验证：`python3 -m unittest discover -s tests`。安装 easynet 时，测试将调用真实 `easynet mission compile --emit-ir`，逐条核对全部节点、标签、算子和有序输入，并验证共享 DAG 与字符串转义；没有编译器时这两项测试明确跳过。

## 实时读取与导入

`python3 scripts/serve.py --port 8765` 提供图册与只编译接口。`GET /api/plan?query_id=...` 按生成清单读取磁盘文件并编译；`POST /api/compile` 接收 `{ "source": "..." }`，在临时目录中编译导入的 EAL，不保存到查询目录。文件最大 1 MiB，编译超时 15 秒；编译错误返回原始源码和诊断，前端清除旧图。

`src/eal_reader.py` 负责编译器边界和 IR 图投影；`src/server.py` 负责本地 HTTP；`src/viewer/reader.js` 管理 idle/loading/ready/error 生命周期并取消过期请求。前端只读取 Mission IR，不另写 EAL 解析器。图按 phase 显示唯一调用节点，命名输入端口保留共享依赖；不支持的 loop 结构明确拒绝。来源和左侧目录统计对应规范化查询快照，右侧节点统计对应当前 EAL 编译结果。
