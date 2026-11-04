# 多模态数据湖第一标杆：对抗审查

本审查基于根目录 `AGENTS.md`、`docs/workload-construction-protocol.md` 与 `report.md` 的既有记录。未运行模型、未审定新的人工 gold，以下为研究设计与待验证假设，不是静态算子失败或 Agent 成功的实验结论。

## 1. 当前标杆能证明什么

MMQA 实体资源构成的候选湖、三个共享视觉谓词和固定 logical DAG 可以成为构造起点。它们当前是 benchmark 构造需求，尚不是经过用户访谈、生产流程或真实分析请求验证的业务需求。候选资源下载、连通图构建和 annotation queue 完成，不等于 gold 已完成，更不等于 capability gap 成立。

异质性与批规模不是 Agent 必要性的充分条件。需要验证的机制是：同一任务作用于一批记录，证据路径因记录而异；中间观察能改善后续动作选择；这一策略能跨记录复用，并相对合理的固定流程产生质量或成本收益。若三个谓词都是对独立图片直接判断单一属性，它们适合作为感知/工程对照，不能仅凭旁边还有表格与正文宣称多模态自适应优势。

冻结数据湖可模拟查询时尚未定位证据的环境；它不是无限开放 Web。必须报告其资源边界、快照与可访问工具，限制结论范围。

## 2. 最强攻击及其可执行反证

| 攻击 | 必须执行的检查 | 不通过时的处理 |
|---|---|---|
| 把不同 QA 打包冒充批任务 | 每任务一个共享自然语言谓词、候选关系和 logical DAG；禁止每行附独有问题 | 降级为 QA benchmark |
| 湖虽然异质，判定却只需 caption 或图片 | 标注充分证据集；分别运行 image-only、text-only、table-only 与组合消融 | 无联合必要性则作单模态对照 |
| 数据组织被故意破坏来制造难度 | 保存原始组织与来源链接；人工扰动单列为 diagnostic view | 不作为自然环境主结果 |
| 固定程序已经能观察并路由 | 运行有限条件路由程序和 Coding Agent 生成程序，允许循环、早停、缓存 | 不能通过把程序改称 dynamic 来免除比较 |
| Agent 靠额外信息或预算胜出 | 对齐可访问资源、工具、模型及总预算；运行 oracle-evidence 诊断 | 无法对齐时缩小结论 |
| 通用 Agent 每行从零规划被人为做贵 | 增加允许批内计划复用、共享缓存的 batch-aware Agent | 逐行 Agent 只作单独具名对照 |
| 学到的算子是手工脚本或测试集特例 | 记录 trace 来源、提取过程与冻结版本，按文档/实体隔离验证 | 不称跨任务动态算子库 |
| gold 直接继承 QA 答案集合 | 对候选全集逐行审核，记录 T/F/U 与证据 | 未出现于答案的实体不得自动标负 |

固定 logical DAG 与运行期自适应不冲突。预先写出的条件程序也可以具备自适应能力。因此应比较明确的实现与动作空间，不能声称有限实验证明“任何静态程序都不行”。

## 3. 数据与标注 gates

以下 gates 可用于构造验收，不以是否获得预期 Agent 优势为数据保留条件。

1. **批语义**：每任务冻结 `candidate_relation`、共享谓词、输入输出 schema、logical DAG、候选枚举与排除规则。先用 30–50 行 pilot 检查标注与执行可行性，再扩至数百至一千行；规模建议不是统计充分性证明。
2. **候选完整性**：先定义候选全集，再标注和运行模型。不能只采 QA 提到的正实体，不能在看见 baseline 错误后偷偷删改候选集合。保留 accepted/rejected/abandoned 清单及理由。
3. **独立 gold**：每条可评分记录包含 `TRUE/FALSE/UNKNOWN`、来源定位、充分证据集和可复核推导。未完成人工审核必须记为 `UNANNOTATED`；不能以 `UNKNOWN` 隐藏标注欠账。发布 confirmatory gold 前应依项目协议独立双标与仲裁。
4. **语义与执行状态分离**：gold `UNKNOWN` 表示在冻结证据世界与既定判定规则下事实不可确定；系统 `ABSTAIN`、budget exhaustion、timeout、tool error 是执行结果。超时不能被重标成 gold `UNKNOWN`，也不能从分母丢弃。报告覆盖率、选择性质量和全量任务质量。
5. **证据开放性**：公开字段采用 allowlist。隔离 `answers`、`supporting_context`、`intermediate_answers`、生成问题、推理类型及答案实体等监督信息。候选湖的边只能来自公开原文结构，不能通过 supporting context 为 query 建 gold 捷径；所有系统使用同一公开图。
6. **多模态必要性**：标注证据模态及其作用，区分图像直接感知、图文绑定、表格约束、跨文档取证。没有组合证据必要性的任务可保留为 negative control，不充当核心多模态 gap 证据。
7. **拆分隔离**：按 source table/document/entity 的关联组拆开发与确认集，检查共享图片、文本、实体和近重复；仅按 QA ID 或行随机拆分不足。若跨源组隔离不可能，明确限制迁移结论。
8. **可复现边界**：保存来源标识、快照、hash、许可信息、转换规则及失败清单。未下载成功的图片属于资源可用性状态，不自动产生 FALSE 或 UNKNOWN gold。

## 4. 对照矩阵

所有竞争臂共享模型、公开资源与工具的访问边界；不要求所有臂收到相同的 oracle context。固定检索必须单独披露，不能暗加到原始静态算子中。

| Arm | 允许的能力 | 检验目的 |
|---|---|---|
| Native static | 被测系统原生静态语义算子 | 当前开箱能力 |
| Oracle evidence static | evaluator 提供充分证据，固定判定 | 仅诊断推理；不是部署竞争臂 |
| Fixed retrieval/extraction | 固定 top-k、OCR/图表抽取、固定判定 | 是否只是缺少常规预处理 |
| Exhaustive shared preprocessing | 全路径固定取证、共享索引与缓存 | 以成本换覆盖是否已经足够 |
| Finite conditional program | 开发集设计的观察、分支、早停、循环与缓存 | 是否需要通用运行时规划 |
| Coding Agent program | 同开发集/工具/预算下生成、调试并冻结可复用程序 | trace 学习相对直接代码合成的价值 |
| Vanilla Data Agent | 通用规划、工具使用；单列 batch-aware 复用配置 | Agent 的质量与实际重复成本 |
| Trace-derived operator | 仅用开发 traces 提取、冻结的有界执行策略 | 保质降本及跨记录迁移 |

成本必须计入探索、trace 收集、索引、OCR、工具与模型调用、代码生成、调试、策略提取及执行；报告 `C_setup + N*C_row` 和实际 break-even batch size。共享预处理按实际服务范围计费，不能将一臂预处理免费、另一臂计费。同时报告 cold/warm cache，冻结重试规则、并发与服务配置。

评价输出是带证据的关系结果；质量、覆盖率、成本、延迟分别报告。比较等总预算下的质量 frontier，以及达到相同质量后的总成本。不要将时间、token 和准确率简单相乘。

## 5. 实证 acceptance / kill gates

这些门槛须在 confirmatory 运行前冻结。下列数值只是可讨论的预注册示例，尚未据实验或任务损失校准。

- **Gap gate**：Agent 相对具名静态对照的差异在按 source 组聚类的不确定性分析下稳定为正，并超过任务预注册的实际意义阈值（示例：5 个百分点）。报告总体、各任务、T/F/U、证据充分性与失败类型；pilot 不承担确定性统计结论。
- **Mechanism gate**：若加入固定检索、全路径预处理或条件脚本后 gap 消失，拒绝“此任务必须通用 Agent”的命题；可保留“当前原生算子缺少这些能力”的较窄观察。若 oracle bundle 下仍有差距，不得单归因检索导航，需另查判定、推理和预算。
- **Budget gate**：Agent 只有更高总预算下才胜出时，不能声称已建立同条件能力优势；转为报告质量—成本曲线。禁止只看成功子集或忽略预算终止。
- **Compression gate**：动态算子相对 Agent 的质量达到预注册非劣效要求（示例：差值置信下界不低于 −2 个百分点），同时总成本下降（示例：至少 20%）。还需报告相对条件程序和 Coding Agent 的结果；追平这些程序并不自动证明新的系统贡献。
- **Causality gate**：每个候选组件有对应 strata 的禁用消融；通过强制错误 route、移除中间证据或固定决策等干预验证作用。Agent 自述“需要工具”和路线数量增加不构成必要性证据。
- **Transfer gate**：策略至少在未见文档/实体上验证；库级复用进一步要求跨任务或跨来源验证。只对同表近重复实体有效的策略保留为任务专用程序。
- **Integrity gate**：gold 不可复核、公开输入泄漏监督信息、负例来自答案补集、任务每行改变、测试集参与调参，均停止该版本的确认性结论，先修复数据与协议。

静态能力不足、Agent 更强、轨迹提取降本是三个独立命题。第一个被反证时，不得用第三个替换后继续宣称原命题成立；第三个仍可作为单独的开发/执行成本问题研究，但需要重新明确评价对象。

## 6. 当前版本的判定

当前建设可以验收为“来源可追溯的候选环境、共享任务契约、固定 logical DAG 与人工标注队列”，前提是实际文件和检查结果满足上述构造 gates。尚无模型运行、已审定完整 gold、受控质量差异或成本证据，因此不能验收为“已证明静态不足且动态算子保质降本的第一标杆”。保留未标注状态比推导虚假负例或用模型自评替代 gold 更符合该研究目标。

## 7. 首次实现审查发现（修复前观察）

本节记录对 `semfilter_bench/lake/{venues.py,workflow.py,__main__.py}` 和 `tasks/mmqa-venue-lake-v1.json` 首版的只读审查，以及对本地 `outputs/mmqa-source/MMQA_tables.jsonl.gz` 的 schema/计数核查。没有运行被测模型。以下是发现时的状态，不自动代表后续实现仍存在这些问题；关闭发现需要重新读取代码与对应检查结果。

| 编号 | 发现时的证据 | 必须落实的修复或限制 |
|---|---|---|
| R1 | `VenueInventory` 用 substring capacity 选列；真实表 `0780d0e29cce0136073677778eb3d323`（2008 Tippeligaen）同时有 `Capacity` 和 `% of Capacity`，实例化立即抛错 | 容量列选择应按经过审核的源 schema，百分比列不是容量；保持该表的正常候选行 |
| R2 | Workflow 只计算 manifest 自身 hash，不核对其中 tasks、relations、数据库和图片的 artifact fingerprints | 统一验证 snapshot 内容完整性；改变证据或任务后禁止以原 snapshot ID replay |
| R3 | `partitions.jsonl` 已生成，但 prepare/execute 不读取，无 split 参数 | 支持显式开发/验证/确认集输入与 replay coverage；不能把全量 prepare 用于策略发现 |
| R4 | 原 union 只包括 table ID 与 cell URLs；按该算法重算，`https://en.wikipedia.org/wiki/2011–12_Serie_D` 的不同表落入不同 splits | 原始页面 URL 同样纳入分组；重新冻结分区统计，后续仍需别名与重复图审计 |
| R5 | 72 行 venue cell 含多链接，其中包含城市；例如表 `4c8b5fbb13aec70e3cd6ff53aae413f5` 第 0 行同时链接 Pittodrie Stadium 和 Aberdeen，第 1 行同时链接 Celtic Park 和 Glasgow | 链接与图片仅是候选证据，不能命名或计数为已绑定的独立球场；保留 link anchor 供实体绑定，不能未经审核自动删城市链接 |
| R6 | manifest source_artifacts 收纳下载目录内所有 images，而非实际消费的资源 | provenance 白名单应准确对应消费文件，避免无关下载历史改变同一候选湖的身份 |

独立 schema 核查观察到容量候选表中的相关列名为：`Capacity`（69 表）、`Stadium Capacity`（2）、`Stadium capacity`（1）、`Capacity 1`（1），另有 `% of Capacity`（1，应作为普通百分比列）。以四种容量列名进行只读枚举得到 73 表、1,124 行、704 行可精确判定容量低于 20,000、69 行容量无法按无修饰整数解析、198 行 venue cell 无链接、72 行含多链接。这不是 semantic gold 审核，也未验证剩余图像条件。

容量 gate 对当前“本行列出的容量达到阈值 AND 语义属性”谓词是合法短路，不是 QA gold 泄漏。必须同时报告全 DAG 指标和 gate 后语义节点指标，避免大量确定负例掩盖语义节点错误。可访问证据中的无监督正文、表格、图片元数据采用显式投影；未在本次代码阅读中发现将 QA answers/supporting_context 直接投影到公开湖的路径。

任务三的 FALSE 标注还须明确存在量词范围：一个冲突容量能够被历史变化解释，不足以证明其他可访问文本中不存在真正同期间、同配置冲突。FALSE 的“充分 reconciliation”必须覆盖声明的比较范围，不能只核验检索返回的第一个文本。

## 8. 修复复核与剩余主张边界

重新读取实现后，R1–R6 均已在代码落实：容量列采用明确四类名称；`SnapshotVerifier` 校验清单内 SHA-256/字节数并拒绝额外文件；workflow 与公开 lake reader 在打开时验证；CLI 强制 `--split` 并按分区过滤输入与 replay coverage；分组包含 source-page URL；cell links 保留 anchor 且改称候选关联；source provenance 只保留实际消费的图片。`all` 明确仅用于构造诊断，不用于策略学习。

复核命令 `python -m pytest -q tests/test_venue_lake.py` 通过 34 项离线测试。实际源的 `VenueInventory(Path('outputs/mmqa-source'))` 成功，重新计算结果为 73 表、1,124 行、177 候选图、42 关联组件；discovery/validation/confirmatory 分别为 605/200/319 行，同 source-page URL 跨 split 数为 0。该检查仍不证明别名、重复图像、未链接实体已全部隔离。

两个视觉任务各有 420 行通过确定容量短路后进入语义节点；其中 145 行的 cell URLs 可精确关联至少一张候选图，18 行没有任何 cell URL。这是资源可达性的结构计数，不是图像足够支持判断的数量。候选图可能描绘城市或其他实体，仍需人工审核 identity binding；没有候选图的行可能从文本得到充分证据，不能自动标 UNKNOWN。

后续应先按候选图可达性与实体绑定歧义分层审核，再决定哪些任务能形成足够真实的可评分批次。任务三需要先核查可判定同期间、同配置冲突的实际比例。现有离线测试验证构造、投影、分区与 replay 边界，不验证语义准确率、证据充分性、预算执行、Agent 轨迹或动态算子收益。

复核另发现 prepare/execute 尚需与 annotation_queue 共享湖外输出检查，避免将结果目录写入已冻结湖、使后续 snapshot 验证失败；该问题已反馈实现者，关闭状态以随后代码与测试为准。


## 9. 输出边界修复关闭（主进程复核）

2026-09-05 13:30:11 UTC+08:00：prepare、annotation_queue、execute 已统一调用 `_check_output`，禁止在公共湖内部或其祖先目录创建运行产物。新增两个回归测试确认 prepare/execute 拒绝后目录未创建且 SnapshotVerifier 仍通过；定向 2 passed，随后新模块合计 45 tests passed。该修复不代表已经部署 public-only 运行沙箱；正式模型 runner 仍待实现。
