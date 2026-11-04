# SemRel Plans

用于统计与分析结构化—语义混合查询的统一计划数据集，附离线图册。当前 3,436 条查询记录均提供逻辑计划 EAL：原有 88 条逻辑 DAG，以及基于参考描述整理的 8-17 共 228 条、7-30 共 3,120 条。总计 8,809 个节点、30 类算子；粗粒度分析阶段保持原粒度，不是全量 benchmark 普查。

**数据入口：[统一模型说明](docs/data-model.md) · [查询表](query/queries.jsonl) · [统计汇总](exports/summary.json) · [SQLite](exports/catalog.sqlite)**

来源入口：[论文与数据来源](docs/sources.md) · [逐查询来源关系](query/query_sources.jsonl) · [语义算子 Benchmark 收录核对](docs/benchmark-coverage.md)（登记源 `config/benchmark-coverage.json`，论文页“收录核对”页签显示仓库与收录状态） · [SWAN / TAG+ / SemCEB / CAESURA 查询导入](docs/hybrid-benchmark-import.md)。论文背景、固定版本查询定义与本项目重建的 plan 分别标注；数据获取缺口保留在逐条说明中。

UDA-Bench 已按固定版本源码完整收录 **608 个查询位置（602 种 SQL）**，覆盖六个领域、43 个 SQL 文件。论文 v1 的 5 数据集 / 240 查询与仓库扩展分开标注。详见[覆盖收据](exports/uda-source-coverage.json)和[范围说明](docs/scope.md)。

展示入口：[交互图册](index.html) · [逐查询文字计划](docs/catalog.md) · [范围和限制](docs/scope.md)。

```text
query/
  queries.jsonl             查询身份、benchmark、场景、计划口径、来源
  nodes.jsonl               节点、明确的 operator_type
  edges.jsonl               有序输入连接，支持 DAG
  sources.jsonl             去重来源、论文题名、版本与核对状态
  query_sources.jsonl       查询到论文、数据、规则的多对多来源关系
config/
  operators.json            统一算子类型与 family 字典
  catalog.json              场景索引与上游版本
files/<scenario>/           SemBench 风格的场景组织，仅引用统一 query_id
src/
  scenario.py               数据加载、引用完整性与图校验
  export.py                 CSV、SQLite、统计视图导出
  build.py                  图册和文档生成
  viewer/                   可视化模板与交互
scripts/                    build.py、validate.py
tests/                      数据完整性与统计口径测试
exports/                    生成的 CSV、SQLite、汇总
assets/                     生成的浏览器数据
index.html                  生成的离线展示入口
docs/                       模型契约、来源快照、收据
```

遵循 SemBench 的 files 场景组织、src 实现、scripts 入口分工；统一数据不按场景复制，避免跨场景统计需要扫描不同格式。唯一编辑源为 query/ 五表与 config/operators.json；files 中只保存场景成员索引。展示树是生成的投影，不作为统计输入。

Python 3.10+（服务端仅标准库），前端组件构建需要 Node.js/npm；EAL 构建和实时读取需要 PATH 中的 EasyNet CLI。浏览器资源全部本地打包，无需外网：

```sh
npm ci
npm run build
python3 backend/scripts/validate.py
python3 -m unittest discover -s tests
python3 backend/scripts/serve.py
# 浏览器打开 http://127.0.0.1:8765
```

新增查询时登记queries、nodes、edges和必要的source；在files对应场景的scenario.json登记query_id，然后校验构建。新增算子类型须更新统一字典。节点谓词保留文字，尚不是可执行表达式AST；没有模型执行器。迁移前的嵌套树编辑格式已删除。

来源窗口2026-10-01—02，源码核对2026-10-05，目录迁移及统一结构2026-10-12。[SemBench参考版本](https://github.com/sembench/SemBench/tree/8c2cac89b21c6782239e8e5b03d326d0c029b655)。保留来源许可边界，无原始数据、private gold、密钥或新增模型结果。

## EAL 与交互工作台

具有逻辑 DAG 的查询的 EAL 导出位于 `exports/eal/`，打包文件为 [eal.zip](exports/eal.zip)。构建会同步更新网页中的 EAL 源码，可逐条查看、复制、下载，也可切换逻辑计划图和来源依据。详见 [EAL 转换契约与执行边界](docs/eal.md)。

EAL 文件是保留节点和有序依赖的逻辑表示；执行仍需实现 SemRel abilities 和数据/表达式契约。`backend/atlas/eal.py` 统一负责转换和打包，规范化数据仍是唯一事实来源。

### 直接读取 EAL

启动 `python3 backend/scripts/serve.py` 后，选择目录查询或点击“重新加载”，图册会读取磁盘上的 `.eal` 并调用 EasyNet 编译器。源码和图来自同一次读取；编译失败不会继续显示旧图。点击节点查看参数、输入引用及源码位置。

“打开 .eal”或拖入文件可预览本地 EAL；仅在当前页面保留，刷新后清除。外部修改导入文件后需要重新选择文件。目录内 EAL 的修改可直接重新加载，但再次运行 build 会从规范化数据重新生成并覆盖它们。

双击 `index.html` 仍可查看构建时的离线 IR 快照，页面明确标示该模式；实时编译和导入须使用本地服务。普通 `python -m http.server` 不提供编译接口。服务仅监听 127.0.0.1，调用 `mission compile`，不会执行任务。当前图形视图支持平面 DAG，loop 控制流会明确报告不支持。

### 专业计划画布

计划图使用 React Flow (`@xyflow/react`) 和 ELK (`elkjs`)。`src/viewer/graph/layout.mjs` 将 Mission IR 的命名输入转换为图边并布局，`index.jsx` 负责节点、缩放平移、小地图、布局切换和详情面板。画布只改变显示位置，不修改 EAL。旧 HTML 树和分阶段卡片渲染已移除。

- `npm ci`：安装锁定依赖。
- `npm run build`：构建本地图组件及完整图册；修改前端组件后也可单独执行 `npm run build:viewer`。
- `npm run test:viewer`：检查全部查询横向/纵向布局的节点身份、边方向、端口端点、节点不重叠以及线路不交叉、不重叠、不穿过节点，以及读取状态切换。
- `python3 -m unittest discover -s tests`：数据、EAL 编译与本地服务测试。

参考组件文档：[React Flow](https://reactflow.dev/learn/concepts/built-in-components)。构建产物 `assets/graph.js` / `assets/graph.css` 随离线图册分发，打开已构建页面不需要 npm 或 CDN。

### 布线约束

ELK Layered 同时优化节点和端口顺序，生成带避障间距的正交路径。React Flow 直接绘制该路径，不再自行生成连线。每条出边使用独立的可视端口（仍引用同一 output 绑定），避免共享主干掩盖边的身份；输入端口可调整空间位置，但名称与语义保持不变。

节点位置由布局器管理，画布支持平移缩放，节点不手动拖动，以免路径失效。当前 88 条目录查询的横纵两种布局都通过几何检查。任意新导入的非平面 DAG 不保证数学意义上的零交叉，布局器会最小化交叉。

### 曲线呈现

连线优先使用端口切线对齐的单段三次贝塞尔曲线，形成钢笔控制柄式的连续弧线。生成后按曲线采样检查节点碰撞与其他线路交叉；直接曲线受阻时保留 ELK 避障路径并平滑转弯。标签沿实际曲线定位。回归覆盖全部目录的 176 组布局和曲线采样检查；采样检查不是连续曲线无碰撞的数学证明。

### 场景导航与节点信息层级

页面使用统一深色背景与内嵌圆角内容区域。Overall 集中呈现统计、来源及文件入口。来源目录展开时占据独立网格列，推动主内容，不使用浮层。来源以文件夹组织：SemBench、TAG-Bench、UDA-Bench，以及分别归档的本地派生数据源；文件夹内标签保留 SemBench 场景、UDA 领域与任务类别。标签筛选分别保存在各文件夹内，选择查询后保持侧栏展开。可搜索查询、展开多个来源，使用关闭按钮或 Escape 收起；深链接保持有效。

节点默认突出算子名称和关键描述；绑定与完整调用信息在选中后的详情中查看，端口名称仅在悬停或选中时显示。节点缩小后仍由 ELK 重新计算尺寸、端口和线路，不对画布做视觉缩放补丁。

侧栏底部的语言按钮切换中英文界面并在本机记住选择；查询标题、节点描述、备注和来源说明同步切换；译文集中在 `config/content-en.json`，不会改写 EAL 原文、SQL 或数据库标识符。目录搜索同时匹配中英文内容。Overall 保留 SQLite、数据模型和 EAL 说明链接。

## 环境、数据和查询分离

- `query/`：查询定义、节点、依赖和来源关系，保留稳定 query_id。
- `environment/<benchmark>/<domain>/manifest.json`：环境身份、数据集引用及运行配置。
- `data/<benchmark>/<domain>/manifest.json`：数据来源、文件绑定、schema、数量和版本；当前未绑定原始数据。

每个问题持续显示来源性质，并在“环境与输入”页列出逻辑输入、输出、数据与环境目录，以及记录批处理、多查询批处理和模型批处理的定义缺口。未知值不填零、不假定已复现。

## 已接入的本地集合

| 集合 | 任务数 | 内容与状态 |
|---|---:|---|
| 8-17 / SEC10K | 42 | 输入路径、参考计划、答案与评估规则；语料为外部本地绑定 |
| 8-17 / ContractExhibit | 102 | 同上 |
| 8-17 / ASRS | 40 | 同上 |
| 8-17 / NHTSA | 44 | 同上 |
| 7-30 / FDABench | 2,007 | 原样保留最小计划分析、证据、置信度及上游定位；原始数据未提供 |
| 7-30 / DABstep | 450 | 同上 |
| 7-30 / LongDA | 505 | 同上 |
| 7-30 / DAB | 54 | 同上 |
| 7-30 / KramaBench | 104 | 同上 |

`query/imports/` 保存提供的 JSON/CSV 原始快照，SHA256 记录在 sources 表；`query/task_details.jsonl` 保留逐任务输入、参考描述、gold、评估及完整原记录。页面在“参考计划”查看原描述，在“逻辑计划”和“EAL 源码”查看转换结果，在“环境与输入”查看路径和 CSV 表头。全部 3,348 条导入任务均已整理为 EAL；7-30 的粗粒度分析步骤不会擅自展开。详见 [转换规则](docs/eal.md#8-17-与-7-30-参考计划整理)。

8-17 的 42,216 个本地文件只登记清单与路径，不复制约 11GB 语料。外部目录必须在使用机器上存在；文件存在与表头检查不代表参考答案已验证。文件数与数据记录数分开，后者未测量时为 null。7-30 的 source_file 是原分析中记录的上游定位，不宣称该路径已存在。

重导入使用 `python3 backend/scripts/import_collections.py --august <8-17目录> --july <7-30目录>`，随后 `npm run build`。重复导入按集合替换记录，保留其余目录内容和稳定查询 ID。

### 原始记录与页面交付

查询页提供独立“原始 JSON”页签：导入任务展示原 JSON 记录或 CSV 原字段；原有逻辑 DAG 展示明确标注的本仓规范化记录，不冒充上游原始 JSON。论文页提供“原始 JSON”和“环境与输入”，依据已登记 paper source ID 列出关联查询；未登记的论文显示缺口。

查询页支持 `#<编码后的query_id>?view=raw` / `?view=environment` 深链接。数据详情独立于 EAL 读取，连接失败不会遮挡这些页签。构建为脚本和样式附加统一内容版本号；默认服务地址是 `http://127.0.0.1:8765`，请使用新页面或刷新已打开页面获取更新。

8-17 和 7-30 的查询标题支持中英文切换及双语搜索。逐查询中文译文位于 `config/translations/queries-zh.json`，与英文原文和 SHA256 绑定；构建检查覆盖率及原文一致性。正常浏览离线使用本地译文，原始 JSON、EAL 和参考计划保持原文。
