# AGENTS.md — Semantic Workload Bench 工作契约

本文件适用于整个仓库，面向研究、数据构造、运行器实现、评测及文档维护。所有设计从 concrete use case 和可核验证据出发，不为机制寻找任务。不要评价用户或他人；可以提出有依据的技术 insight，专注实现与验证。

## 1. 接手顺序与事实来源

开始工作先检查 `git status --short` 和相关文件，保留共享工作区的既有修改、未跟踪文件与运行产物。依次阅读：

1. [BENCHMARK_SPEC.md](BENCHMARK_SPEC.md)：研究单位、状态与语义。
2. [docs/research-context.md](docs/research-context.md)：用户确认的方向及迁移边界。
3. [docs/environment-validity.md](docs/environment-validity.md)：环境有效性证据与缺口。
4. [docs/evaluation-protocol.md](docs/evaluation-protocol.md)：比较臂、划分、质量及成本。
5. [README.md](README.md)、[docs/artifact-guide.md](docs/artifact-guide.md)：运行与复现入口。
6. `report.md` 最近条目（如存在），相关 workload/resource card、JSON、源码和测试。

研究背景见 [历史接手文档](docs/history/research-handoff-2026-09-05.md) 和 [历史构造计划](docs/history/benchmark-construction-plan-2026-09-05.md)。根目录两个同名日期文件也是迁移的历史材料。`docs/history/` 的旧路径、命令、数据就绪状态、测试数量和模型指标不自动属于本仓库，不可直接作为执行指令或当前结果。

当前用户指令优先于仓库约定。现行 SPEC 定义应有行为，实际源码与本次验证说明已实现行为；有差异时记录并按任务范围修正，不能把未实现规范写成现成功能。新实验遵循现行协议，不默默改写历史。

## 2. 研究目标与当前范围

核心问题：从 Data Agent **一次任务执行的可观察轨迹**自动提取可复用语义算子，在独立后续批次上保持关键步骤和下游质量，并降低包含构造开销的总成本。

研究单位为 `(E, T, x0, R, G)`：冻结环境、固定任务、一条示范、未参与提取的后续关系、独立私有 gold。批内共享谓词或参数化转换目标；任意 QA 集合不自动构成可复用 workload。

默认路径应获得完整必要输入并能输出结果。辅助文档、关系、知识、参考与工具可能改善质量；每项资源必须说明纠正哪种具体错误。分别验证两条证据链：

- 真实来源 → 正确构造 → 默认路径可执行 → 实测资源增益 → 下游改善。
- 一次真实 Agent 示范 → 自动提取 → 冻结算子 → 独立执行 → 质量保持与完整摊销收益。

固定外层关系语义和 DAG，内部是否需要自适应是实验变量。接受固定程序等于或优于 Agent；提取产物可以是固定程序。资源缺失、任务歧义、弱基线失败、异质目录规模均不能证明动态能力必要。

当前包含 Python 独立骨架、DeepPCB 24 条探索控制，以及本轮新增的 CUAD/BioDEX 各8条开发pilot构造、LOTUS静态流程、固定复核和有预算的工具型Agent比较。运行/评分状态以 `report.md` 和新pilot收据为准，不能将实现或进行中的实验写成优势结论。DataSpace单示范自动提取开发原型现已实现并运行；尚无动态算子库、独立确认或完整实际金额测量。PCB固定运行的 `trace.json` 不是Agent学习来源证明。

最新用户确认：先实测传统LOTUS静态实现准确性/任务质量不足，再检验同资源Agent改善与成本，最后从单次轨迹提取。优先BioDEX、CUAD，LOCO保留为多模态候选，PCB仅为控制。详见[质量差距候选](docs/accuracy-gap-candidates.md)。不得将目标放宽为静态质量已足够时仅追求降成本；也不能人为制造差距。锁定具体LOTUS版本与调用模式，现行agentic operators不应被描述为传统静态实现。随后建设可观察示范及提取接口，最后在独立文档上确认。不预先建设庞大动态框架、通用权限平台或同时实现全部候选数据集。

## 3. 目录职责与架构要求

| 位置 | 职责 |
| --- | --- |
| `src/semantic_workload_bench/cli.py` | 参数解析、命令分派、JSON 输出，不承载算法 |
| `src/semantic_workload_bench/core.py` | 快照校验、源构造、公开执行、独立评分与共享文件契约 |
| `src/semantic_workload_bench/pcb_geometry.py` | 固定几何算法、不可变配置，不读 gold 或负责评分 |
| `contracts.py`、`biodex.py` | 各领域的源构造、私有评分和领域资源，禁止互相借用gold |
| `contract_experiment.py`、`biodex_experiment.py` | 各领域公开执行和有界工具编排 |
| `inference.py`、`public_tools.py` | 共享推理传输/可观察收据、公开文本检索；不承载gold或领域判断 |
| `pilot_analysis.py` | 冻结输出后的配对分析，不驱动模型调参 |
| `environments/pcb/` | evaluator 侧源锁、资源说明和工具描述 |
| `workloads/pcb-copper/` | 固定谓词、DAG、标签映射与适用范围 |
| `experiments/plan.json` | 实验计划及已实现控制列表，不是完成收据 |
| `artifact/` | 控制复现脚本与主张到证据映射 |
| `tests/` | 离线契约和失败边界验证 |
| `docs/`、`docs/history/` | 现行协议与历史背景 |
| `data/`、`runs/` | Git 忽略的构造与运行产物，不作为源码依赖 |
| `report.md` | 追加式研究/实现账本，首次记录时若缺失则创建 |

保持现有对象所有权明确：`Snapshot` 校验和封存清单；`PCBBuilder` 验证来源、构造 public/private 并发布；`PublicRunner` 只消费公开快照并输出预测/日志/收据；`Evaluator` 读取 private gold 与预测评分，不反馈答案给运行器；`SpuriousCopperDetector` 只比较图像，`DetectorConfig` 表达算法参数。

采用 industrial textbook architecture：高内聚、低耦合、职责与所有权清晰、命名与边界语义一致。使用恰当 OOP 抽象，避免过程式分支堆积，也不为简单数据操作强建继承层次。共享路径、构造、状态和评分逻辑应有单一实现，优先根因重构并消除重复，不堆局部补丁。

新增 workload/system 时按实际变化点拆分职责，不把其他领域塞进 PCB 类或将业务逻辑写入 CLI。内部重构保持公共行为和接口兼容；确需改变任务语义则显式版本化。迁移完成立即删除废弃实现，不保留 SPEC 未要求的兼容层，不添加只为延续旧架构的 fallback。

## 4. DeepPCB 控制任务不变量

- 获取依据是 [sources.lock.json](environments/pcb/sources.lock.json)：commit `08e98c4db5922613fb97176eb3d6497d48260cb1`；24 条、48 张图、24 份标注，共 2,349,259 bytes。
- 样本继承自官方 test 行按 `SHA256("manufacturing-pilot-v1" + NUL + line)` 排序取前24条。builder 消费锁定名单，不重新抽样；不得描述为新确认集。
- 单位是 tested PCB 图及对齐 clean template。gold 为官方 bbox 是否存在 class 5 copper；其他缺陷不自动意味着目标为真。
- 外层为 scan → sem_filter → project record ID → count。定位/结构化抽取须独立契约或 sem_map，不暗改 Boolean filter 语义。
- 原图字节不变；公开 ID 不含答案；source ID、bbox 与分组映射保留在 private。
- 来源含人工增补缺陷，不是纯自然生产缺陷，也没有返修、严重度、报废或制造合规 gold。
- 24 条已被历史研究查看；当前全24条评分仅为控制/开发 smoke，不是本仓库“一示范+23测试”。确认需要新数据与源实体分组隔离。
- `always-false` 是常量负例 sanity control，不是有竞争力的默认语义算子。
- `fixed-geometry` 是迁移的手工固定算法，不是学到的算子。假设暗色铜、同尺度预对齐，以完整8连通分量与模板支撑比较；3px 容差、8像素面积下限、10%支撑比例是工程参数，不是工业公差。无训练、无配准或校准概率。

详见 [resource card](environments/pcb/resource-card.md) 和 [workload card](workloads/pcb-copper/workload-card.md)。改变任务时核对 workload JSON、builder 生成的 `task.json`、卡片和评分映射。当前描述文件并非都由运行器自动加载，不能只改 JSON 就声称执行行为改变。

## 5. 构造、泄漏和产物保护

构造侧可访问源锁与标签；被测系统只能获得允许的 public 资产。源锁含标签 URL，即使位于仓库 `environments/` 也不是模型资源。`construction.json` 含类别统计，不应无意加入模型上下文。

公开字段采用 allowlist。禁止从公开路径推断当前评测 gold，禁止泄漏当前评测答案目录、bbox/mask、QA answers、supporting context、实例解释、gold 选出的参考/裁剪或隐藏人工感知。工具必须从公开材料实际计算；读取当前评测人工标注的工具只能明确作为 annotation-given/oracle 诊断。

历史纠错经验 H 可以作为有明确来源的环境资源，详见 [历史经验协议](docs/historical-experience.md)。历史人工标签与当前 R 的 private gold 必须分开；H/开发/示范/确认按源实体与近重复审计划分。官方人工标注、模型输出、程序复核和研究者归纳规则分别标记，不冒充专家SOP。当前 environments/pcb/history 是未挂载的开发登记材料；不可因新增JSON就声称builder支持历史库，不得递归挂载源锁或暴露登记表。测试记录用于构造经验后转为开发暴露，需另立独立确认。

快照记录来源、版本、选择/转换规则、许可、精确清单、大小与哈希；缺失、额外、篡改文件均拒绝，不能自动重写 manifest 掩盖损坏。哈希证明字节一致，不证明科学有效、gold 正确或无训练污染。

build/run 必须使用未存在的新目录，保留既有产物。结果位于冻结快照之外。构造先暂存校验后发布，失败只清理本次暂存，不留下可误用的目标快照。当前 score 会写入 run 的 `metrics.json`，不是只读操作；需要保留旧评分时先在快照外归档并记录评分版本。

目录分离与 `within()` 不是 OS 沙箱。当前执行器信任仓库工具；引入不可信 Agent/生成代码执行前须实现 public-only 挂载或等效实际隔离，防止读取仓库 private 材料。这是实验执行边界，不要求建立通用权限产品。

## 6. 生命周期与失败语义

规范生命周期是 `PLANNED → SOURCE_VERIFIED → BUILT → EXECUTED → SCORED → VALIDATED`，每次转换需产物与前置证据。当前没有完整状态机框架：builder 写 `BUILT`，runner 写 `EXECUTED`，evaluator 写 metrics；评分成功不自动获得科学有效性认可。

扩展时集中定义合法转换、产物及失败处理，不在各模块散落状态猜测。文件存在、命令返回0或哈希通过都不足以设置 `VALIDATED`。

当前 PCB 每行预测为 `record_id, label, status`：成功为 `status="OK"` 与 JSON Boolean；未完成为 `status="ABSTAIN"` 与 `label=null`，日志保存原因。每个 gold ID 必须且仅出现一次；拒绝重复、遗漏、额外行和非法状态组合。ABSTAIN 计入全量分母并视为未正确完成，另报 coverage，不能删失败行。

其他任务的语义 `UNKNOWN` 表示冻结证据世界下事实不可确定，不等于 FALSE 或执行 ABSTAIN；`UNANNOTATED` 表示标注欠账，`INVALID_RECORD` 表示无效记录。当前 PCB scorer 不支持这些扩展，新增须显式契约及验证。工具失败、预算终止、缺资源不能自动生成事实标签。

## 7. 单轨迹与比较协议

每个提取算子只使用一条真实 Agent 执行轨迹。记录示范选择、失败尝试、重试、提取输入、版本及人工介入。多个 one-trace episodes 可以分别测方差，不能合并轨迹后仍称一次示范。

单次轨迹可以访问多条批准的历史案例，但“单轨迹”不等于“仅一个带标签样本”。分别报告历史监督量、访问条目、历史轨迹读取量及提取器实际输入；不得拼接多条原始执行轨迹后仍声称只用一次执行。对照必须包含同一历史库上的固定示例、固定检索/工具流程及Coding Agent；历史整理、标注/审核和索引成本单列，未知不填0。

保存可观察动作、工具输入/输出、证据、错误、预算及终止原因，不要求私人思维链、不记录密钥。冻结算子须有输入输出、依赖、适用范围、参数化规则、分支、预算及 ABSTAIN/升级行为；不得写死示范答案、实例 ID 或不具迁移依据的坐标。

示范/开发/确认按板组、原图场景、物件、患者、合同、报告等源实体隔离，审计近重复、模板、参考、训练数据及跨数据集重叠。禁止确认 gold 调参、挑示范或补特例；修改后属于新版本/开发，需要新的独立确认依据。

现行矩阵见 [evaluation protocol](docs/evaluation-protocol.md)：

| Arm | 定义 |
| --- | --- |
| B0 | 完整必要输入上的直接语义调用 |
| B1 | 同模型加入固定知识/参考 |
| B2 | 固定检索/工具程序，允许公开分支、循环、早停与缓存 |
| B3 | Coding Agent 一次生成批程序 |
| B4 | Data Agent，允许批内共享计划和缓存 |
| B5 | 单轨迹自动提取的冻结算子 |
| B6 | 同轨迹摘要/简单重放 |
| B7 | 仅任务与环境、不提供轨迹的提取消融 |

这是目标矩阵，并非全部已实现。新pilot只覆盖具体静态/固定复核/工具Agent流程，尚缺完整DocETL、Coding Agent和提取比较；两次复核与多轮Agent的预算差异须披露。方法比较对齐模型、可访问资源、工具、预算和评分；不能对齐就披露并缩小结论。环境消融的信息条件不同，只说明资源价值。不能禁止固定程序用同一工具、忽略 Coding Agent 或强制 Agent 每行重规划以制造优势。

## 8. 指标、成本与有效性

同时报告关键步骤、证据充分性、coverage/失败类型及下游清单/聚合质量。当前 evaluator 输出 accuracy、coverage、abstentions、混淆矩阵、选中数、gold 数和 count absolute error；macro-F1、清单 precision/recall、聚类置信区间及非劣效分析是后续要求，不能称已自动提供。

确认前冻结数据、任务、模型/prompt、预算及非劣界；按源实体做配对和聚类不确定性分析。小样本点估计、AI 共识和工程测试不能证明总体优势。通过 gold 替换中间步骤检验下游影响，分别消融知识、工具、关系、缓存和轨迹。

完整成本为 `C(N) = C_demo + C_extraction + C_validation + C_shared_preprocess + Σ C_execution(i) + C_fallback`，包括示范筛选、失败与重试。分别报告 tokens、已知实际金额、工具计算、CPU/GPU、初始化、进程启动及批 wall-clock，注明并发、cold/warm cache。未知不填0，不将时间×token×准确率作为唯一指标。

当前 `run.json` 记录固定运行时间、Python/平台/包版本及代码哈希，`trace.json` 记录固定动作；它们不是完整经济账单或受控延迟研究。模型实验另存精确模型/日期/prompt/参数/种子（如支持）/重试/并发/缓存配置及允许保存的原始输出。存储响应回放只验证分析流程。

## 9. 开发与验证

Python 3.11+；core 构造、校验、常量运行和评分只用标准库。从仓库根目录执行，`python3` 指向所选环境：

```sh
export PYTHONPATH="$PWD/src${PYTHONPATH:+:$PYTHONPATH}"
python3 -m semantic_workload_bench.cli --help
python3 -m unittest discover -s tests -v
```

工程 smoke，目录必须尚不存在，重复运行更换名称：

```sh
python3 -m semantic_workload_bench.cli build --lock environments/pcb/sources.lock.json --output data/pcb-check-v1
python3 -m semantic_workload_bench.cli verify --snapshot data/pcb-check-v1/public
python3 -m semantic_workload_bench.cli verify --snapshot data/pcb-check-v1/private
python3 -m semantic_workload_bench.cli run --public data/pcb-check-v1/public --system always-false --output runs/sanity-check-v1
python3 -m semantic_workload_bench.cli score --private data/pcb-check-v1/private --run runs/sanity-check-v1
```

build 默认下载72个锁定资产。`--source /path/to/matching-source` 可读取与锁相对布局一致的本地源（`public/images/...`、`private/gold/...`），仍校验字节；不是任意上游 checkout，也不依赖旧仓库。缺失/不匹配应报错，不静默换源。

视觉控制在隔离环境安装：

```sh
python3 -m pip install -e '.[vision]'
python3 -m semantic_workload_bench.cli run --public data/pcb-check-v1/public --system fixed-geometry --output runs/geometry-check-v1
python3 -m semantic_workload_bench.cli score --private data/pcb-check-v1/private --run runs/geometry-check-v1
```

依赖以 `pyproject.toml` 为准，当前 NumPy 2.2.6、opencv-python-headless 4.12.0.88。选择依赖支持的解释器，不能因 core 可运行就断言该 Python 有 vision wheel。安装后有 `swb` 入口。

完整控制复现：`SWB_ARTIFACT_DIR=/absolute/unused/path bash artifact/reproduce.sh`，可追加匹配的本地源目录作为首参。脚本内部用 `python`，须指向正确环境；默认 `runs/artifact-v1` 不可重复覆盖。

按变更做必要验证：文档检查链接/命令/事实；构造评分检查离线契约和失败边界；视觉改动另检查实际解码、正负例及假设失效情况。当前离线测试使用占位图像字节，不能验证视觉质量。不要为低影响文档新增无价值测试，不将零测试、旧测试数量或工程通过说成研究验证。

## 10. 工作账本与交付

每次研究、构造、实验或实现工作都追加 `report.md`，缺失则创建，不覆盖旧条目。至少包含：

- 带时区时间（默认 Asia/Singapore）、目标和范围。
- 实际读取/修改/执行内容、命令、产物位置。
- 数据来源/commit/hash、split、选择规则、记录单位/数量/用途；无数据运行写明不适用。
- 代码/模型/prompt/依赖、种子、预算、并发和缓存；未使用项明确不适用。
- 观察、失败及修正、实际测试数、结果与局限、未完成项。

区分计划、历史转述、本次观察和验证结论。文档与源码不符、缺失报告或共享文件更新时重新核对，不推断未执行结果。按影响同步 SPEC、卡片、环境有效性账本、实验计划和 `artifact/claim-map.json`，不批量将计划改成成功。

交付说明完成内容、验证及其边界。新 workload 至少有真实输入、共享任务、有用途的资源、独立 gold、可运行默认路径和可追溯产物；单轨迹成果还需真实示范、自动提取、冻结及独立运行。保留阴性和不确定结果。

## 11. 历史候选边界

- LOCO/MMAD：核验图像、完整装配规则及知识来源泄漏；LogiCode 同名 JSON 标注读取不是实际感知。
- ContractNLI：nda-20 是同命题跨合同路线；原 test 123合同，多命题不增加独立文档数。
- TAT-DQA/TAT-QA：先做同指标 family 统计及来源重叠审计；QA 数不是同任务批量，页面不是完整报告。
- MMQA 场馆：历史问题主要为证据充分性和实体/时期/量词歧义，未决比例不是静态能力边界。
- FEVEROUS：历史完整库和测试未迁入本仓库，不替代当前多模态目标。
- 医疗原型：历史弱模型、多数类结果和训练测试重叠不是成熟工具增益，不能称恢复的原模型或临床验证。

需要某路线时先读对应历史文件，再核验当前材料，不自动启动旧实验、下载大包或将旧绝对路径变成必需依赖。

## 12. Git、保密与发布

只在用户要求时 commit，作者与提交者均只能为 `Silan.Hu <silan.hu@u.nus.edu>`。使用本次命令或仓库范围配置，不改全局身份。提交前检查 diff/暂存内容，只纳入本任务文件，不全量暂存共享未跟踪成果，不删除他人产物。

不提交密钥、`.env`、原始数据、权重与运行目录。不外发未发表论文、私有标注、内部轨迹或材料；本地工作不构成联系他人或公开发布授权。

代码、数据、模型和迁移代码的许可分别核验。DeepPCB MIT 文件与 research-only 数据声明不能混为图像无限商业许可；迁移 detector 外发权利仍待核验。不自行增加覆盖上游材料的新许可证。

发布门槛为两个有依据的 workload families、冻结任务与划分、独立 gold、环境有效性实验、强可比基线、完整成本、可复现主张到图表映射、许可和独立复现检查。这是项目设计门槛，不是官方 VLDB 认证清单；本地 artifact 不代表论文结论或认证完成。

## 13. 本轮质量差距 pilot

冻结设计见 `docs/heterogeneous-gap-pilot.md` 与 `docs/biodex-gap-pilot.md`，操作偏差见 `docs/pilot-execution-notes.md`。模型来自用户指定.env服务的gpt-5.4别名，不能宣称已核验官方snapshot。每族串行、两族可重叠，无自动任务重试；服务超时为ABSTAIN，不能当语义能力失败。工具只有公开对象上的allowlist，无任意代码/文件系统/外部检索。

CUAD使用精确类别、一对一span Jaccard匹配；与DocETL模糊类别匹配旧scorer不等价，禁止直接对比表中F1。BioDEX公开目录24,369项，固定程序也使用向量检索和LLM排序。两族都是8条开发筛选，词面/报告ID检查不等于实体/训练污染隔离。现有对照不足以直接证明异构资源因果增益；需预算对齐、资源消融和独立确认。

新增pilot依赖为 `.[pilot]`（lotus-ai1.2.4），实际安装清单在 `experiments/pilot-requirements.lock.txt`。与PCB vision配置分别用隔离环境，因为LOTUS要求NumPy<2而vision固定NumPy2.2.6。不要把两个extras一起安装。新命令见 `artifact/reproduce-cuad-pilot.sh` 和 `docs/pilot-artifact-guide.md`。


## 14. DataSpace 可摊销探索开发原型

本轮用户新目标与冻结协议见 `docs/dataspace-amortization-pilot.md`；复现入口为 `python -m semantic_workload_bench.cli amortization --help` 和 `artifact/reproduce-dataspace-amortization.sh`。源锁 `environments/dataspace/sources.lock.json`、LOTUS源码锁 `experiments/dataspace-lotus.lock.json`。不能仅凭包版本1.2.4认定具备本轮agentic接口，必须核对commit/pipeline hash。使用Python3.12和独立LOTUS依赖，不混装PCB vision。

目录：`dataspace.py`负责真实源导入，`fund_workload.py`负责task184的实体构造；`workspace_agent.py`只执行公开Agent任务；`operator_synthesis.py`只从单次可观察轨迹合成/冻结并在Docker执行生成代码；`fund_experiment.py`/`fund_fixed.py`负责LOTUS/手写SQL；`fund_analysis.py`负责私有评分与错误诊断；`amortization.py`/`amortization_report.py`负责冻结结果后的统计与成本。禁止在本轮R上修补冻结算子。

实际构造1示范/16验证/300后续基金实体，按基金管理人分组隔离；仍属开发、非独立确认。SQLite是任务必要来源，CSV/JSON是原生干扰资料；不能把该派生任务称为多模态资源增益。原题存在多个简称字段，静态结果的其他公开简称不证明推理不足；澄清命名约定需新任务版本，不能默默改v1评分。固定SQL300/300；native整批Agent与冻结算子均299/300、1ABSTAIN。完整学习tokens与真正整批Agent比较须一起报告，不用16记录线性外推替代300记录实测。

原生LOTUS预算包括最终tool-free回答；有效最终回答应评分，不能由适配层自动丢弃。`lotus_receipt_replay.py`仅修正已执行响应的结果投影，非新推理，也不是B6轨迹重放研究臂。HTTP403、使用量适配故障、预算最终化和实际语义错误分别记录；原始失败收据保留。未来复现用新输出目录，评分拒绝覆盖metrics.json；完整科学有效性仍未建立。
