# SemRel Plans

用于统计与分析结构化—语义混合查询的统一计划数据集，附离线图册。当前88条查询、580个逻辑节点、29类算子。SemBench五场景60条、TAG-Bench选例12条、UDA-Bench端到端选例6条、本地派生任务10条；不是全量benchmark普查。

**数据入口：[统一模型说明](docs/data-model.md) · [查询表](data/queries.jsonl) · [统计汇总](exports/summary.json) · [SQLite](exports/catalog.sqlite)**

来源入口：[论文与数据来源](docs/sources.md) · [逐查询来源关系](data/query_sources.jsonl)。论文背景、固定版本查询定义与本项目重建的 plan 分别标注；数据获取缺口保留在逐条说明中。

展示入口：[交互图册](index.html) · [逐查询文字计划](docs/catalog.md) · [范围和限制](docs/scope.md)。

```text
data/
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

遵循 SemBench 的 files 场景组织、src 实现、scripts 入口分工；统一数据不按场景复制，避免跨场景统计需要扫描不同格式。唯一编辑源为 data/ 五表与 config/operators.json；files 中只保存场景成员索引。展示树是生成的投影，不作为统计输入。

Python 3.10+（服务端仅标准库），前端组件构建需要 Node.js/npm；EAL 构建和实时读取需要 PATH 中的 EasyNet CLI。浏览器资源全部本地打包，无需外网：

```sh
npm ci
npm run build
python3 scripts/validate.py
python3 -m unittest discover -s tests
python3 scripts/serve.py
# 浏览器打开 http://127.0.0.1:8765
```

新增查询时登记queries、nodes、edges和必要的source；在files对应场景的scenario.json登记query_id，然后校验构建。新增算子类型须更新统一字典。节点谓词保留文字，尚不是可执行表达式AST；没有模型执行器。迁移前的嵌套树编辑格式已删除。

来源窗口2026-10-01—02，源码核对2026-10-05，目录迁移及统一结构2026-10-12。[SemBench参考版本](https://github.com/sembench/SemBench/tree/8c2cac89b21c6782239e8e5b03d326d0c029b655)。保留来源许可边界，无原始数据、private gold、密钥或新增模型结果。

## EAL 与交互工作台

全部查询的 EAL 导出位于 `exports/eal/`，打包文件为 [eal.zip](exports/eal.zip)。构建会同步更新网页中的 EAL 源码，可逐条查看、复制、下载，也可切换逻辑计划图和来源依据。详见 [EAL 转换契约与执行边界](docs/eal.md)。

EAL 文件是保留节点和有序依赖的逻辑表示；执行仍需实现 SemRel abilities 和数据/表达式契约。`src/eal.py` 统一负责转换和打包，规范化数据仍是唯一事实来源。

### 直接读取 EAL

启动 `python3 scripts/serve.py` 后，选择目录查询或点击“重新加载”，图册会读取磁盘上的 `.eal` 并调用 EasyNet 编译器。源码和图来自同一次读取；编译失败不会继续显示旧图。点击节点查看参数、输入引用及源码位置。

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
