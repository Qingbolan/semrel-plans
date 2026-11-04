# 第十一增量：CodiEsp 原论文、完整仓库、金标及官方长手册核验

2026-09-08，Asia/Singapore。本轮是来源与任务语义审计，无模型运行。严格合格数仍为0/10；CodiEsp记为结构接近的编码候选，不列入通过项。不能把诊断、操作两个子任务重复计作两个独立数据湖。

## 已下载和实际核验

- [原论文](https://ceur-ws.org/Vol-2696/paper_263.pdf)：29页、1,468,724 bytes。
- [作者评测仓库](https://github.com/TeMU-BSC/codiesp-evaluation-script)：完整commit `976fc1119845d0cd252f1f1103c799c280f32a1d`，17个Git blob逐个校验一致。是官方评测实现，不是声称已取得全部参赛系统。
- [原金标包v1.4](https://zenodo.org/records/3837305)：11,239,591 bytes；500 train、250 dev、250 test真实来源的西班牙语临床病例文档。论文称这些病例是受隐私限制医院报告的替代数据，不能称原始医院账单或自然审批记录。英语文件为机器翻译，本轮使用西班牙语原文。
- [任务标注约定](https://zenodo.org/records/4121205)：11页。其引用的官方2018年[诊断手册](https://www.sanidad.gob.es/estadEstudios/estadisticas/normalizacion/CIE10/CIE10ES_2018_norm_MANUAL_CODIF_DIAG_.pdf)312页、[操作手册](https://www.sanidad.gob.es/estadEstudios/estadisticas/normalizacion/CIE10/CIE10ES_2018_norm_MANUAL_CODIFICACION_PROCEDIMIENTOS_EDICION_2018.pdf)304页，均实际下载并抽取文本核版本。
- 原代码目录包：诊断98,288行、操作87,170行。所有D/P gold代码均在相应目录中；代码存在不证明标注医学正确。
- 本次发布包实数：D共11,158条文档—代码行，P共3,246条，X共18,435条证据标注行。不能把它们当18,435个独立病例，也不能混用论文中的提及统计与去重文档—代码统计。

下载URL、大小与SHA256见[收据](../artifact/evidence/shared-environment-audit-20260908-v11/download-receipts.json)；[统计](../artifact/evidence/shared-environment-audit-20260908-v11/statistics.json)由[脚本](../artifact/evidence/shared-environment-audit-20260908-v11/audit_data.py)复算。原始下载位于`data/shared-environment-audit-20260908-v11/`，未运行作者代码。三个Zenodo文件MD5与服务元数据一致。

## 为什么不能直接称为政策决策 workload

官方任务补充约定G12允许诊断非末级代码、操作4位或7位代码；P4要求标注非当前患者主体的疾病，包括家族史。这是特定语料的编码/索引约定。长手册包含索引与表列顺序、Excluye 1/2、组合代码等规则，但“手册很长”尚不能证明当前标签需要这些复杂规则。

本轮固定读取dev第一条记录 `S0004-06142005000900016-1`（开发暴露，非确认样本）。公开原文否认肾结石、血尿、尿路感染病史；private gold仍分别列出n20.0、r31.9、n39.0。X标注也指向这些否定句中的疾病词。这里不能据gold推导“患者患尿路感染=TRUE”。G12可解释非末级代码ct13，但不能擅自宣称所有被否定疾病标注都已由规则解释；当前补充规范未找到显式的否定提及判定条款。

该记录还将“crisis renoureteral”对应n28.0，而代码目录释义为肾缺血及梗死。只记录可复核的不一致线索，不自行改标、不作临床裁决。必须进一步核原任务标注范围、术语映射与规则适用性。

## Query与数据湖

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold（不提供给模型） |
| --- | --- | --- | --- | --- |
| 对每篇病例，按CodiEsp规则输出诊断/操作代码集合及证据 | E：2018诊断312页、操作304页和任务补充11页 | 两个固定代码目录，98,288/87,170行 | R：1,000病例；原test250篇可作后续设计起点，尚未完成实体重叠审计 | D/P文档代码与X证据span；不能作为检索资源 |
| 对dev实例，是否应在编码清单中包含n39.0 | 相同E，必须先确定“标注提及”的规则语义 | 当前病例否认尿路感染病史 | 目录n39.0对应未指明部位尿路感染 | 原gold包含n39.0；这是编码集合成员TRUE，不能解释为患病TRUE |
| 对相同实例，输出操作编码 | 操作手册与G12部分代码约定 | 右肾超声、肾显像及其他原始叙述 | 公开目录中bt41zzz有右肾超声描述，ct13描述为空 | 原P集合为{bt41zzz,ct13}；不能从这个例子外推全部手术叙述标注充分 |

## 类Python DAG

| 类python的DAG | 具体数值 | 状态与语义 |
| --- | --- | --- |
| `E = freeze(manuals_2018, task_guideline, code_catalogs)` | 312+304+11页；185,458目录行 | 原资产已下载；未构造模型public快照 |
| `R = scan(original_spanish_cases)` | train500/dev250/test250 | 标注文档1000；不将background当有gold病例 |
| `mentions = sem_map(R, codiesp_scope)` | 每篇可有多项 | 拟议；不能先删掉否定或家族史提及而不核规则 |
| `candidates = retrieve(E, mentions)` | 多候选+目录路径+适用规范 | 固定检索与Agent必须使用同一允许资源；不按gold选规则 |
| `codes = sem_map(mentions, candidates, E)` | dev实例D12项/P2项为原gold目标 | 尚未运行；不能保证实现命中 |
| `selected = sem_filter(codes, contains('n39.0'))` | 例中gold派生TRUE | 仅“代码清单包含”任务；患病任务不成立 |
| `evaluate(private_gold, frozen_outputs)` | D/P集合、X证据分别评分 | 未执行；官方排名指标与新增Boolean指标分别报告 |

## 多种方法预期

下表均为实验假设，无LOTUS、Data Agent或提取器实测，不能读作方法准确率结论。`==...==`表示可记录的环境探索动作，不要求私人思维链。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 以原编码任务为目标，例中n39.0应入集合；能否命中未知 | 固定检索任务约定→提及抽取→目录候选排序→代码集合；不能用“排除否定诊断”通用prompt偷换任务 | 同一目标，不能预设Agent会纠正或更准 | ==读任务约定，区分提及编码与患者诊断==→==核否定句的处理依据==→证据不足时记录歧义 | `ScopePolicy + MentionExtractor + CodeResolver + EvidenceValidator`；否定规则未核清不得硬编码 |
| 右肾超声目标bt41zzz；ct13需要目录/规则处理，未测 | 同资源固定检索→操作属性映射→G12检查→输出 | 相同目标，无优势预设 | ==查操作码结构和G12允许位数==→==核右侧信息及未确定属性==→输出 | 代码长度/层级约束、候选检索、缺信息分支；不是直接记住两个gold |
| E-only编译或Coding Agent可能足够 | 从完整E生成固定批程序，包含查表、循环与校验 | 单轨迹提取也应和该强基线比较 | ==一次示范记录实际文档/条款访问==→冻结提取→独立病例执行 | 共享索引+任务范围+参数化映射；计入索引、示范、提取、复核及升级成本 |

## 本轮结论与后续证据缺口

已证实长共享E、1000篇统一任务文档、独立专业标注三者同时公开；尚未证实这些gold能支持“真正依赖复杂E”的决策任务。尤其否定提及与临床决策语义不同，不能列作保险/临床合规通过项。后续若继续此路线，应先核标注规范与长手册哪些规则实际决定标签，再考虑资源消融；不用模型失败来代替来源核验。

本轮没有运行实验、没有新专家标签、没有性能或成本数字，新增工程测试0。仅完成下载完整性、记录/代码计数及一个开发例子的文本—标注审计。未实施public-only隔离或完整运行器，不能称已有可运行benchmark。原始数据与官方手册的再分发许可仍需分别核验，不替它们新增许可证。
