# CODE-ACCORD：法规抽取不是设计合规裁决

**Reject当前目标**。已下载[原论文](https://arxiv.org/abs/2403.02231)及[完整作者仓库](https://github.com/Accord-Project/CODE-ACCORD)，commit45f08307dd24d5ee4dc31ff40ac4eab055e8d08b，332 tracked文件/140477194字节。实读论文任务、句子筛选、12人标注、数据记录与统计，以及CSV实际字段。未运行作者代码。

| 条件 | 证据与判定 |
|---|---|
| A固定q | 原任务是法规句子实体/关系抽取；可以固定，但不是建筑案例通过/不通过 |
| B共享环境 | 33份法规是被抽取的源材料x；标注指南才是原抽取任务E，不能倒置 |
| C环境必要/20条 | 0条合规gold；尚未作20条实体标注指南闭合审查 |
| D完整E静态不足 | 无证据；论文选self-contained句子，避免大量上下文交叉引用 |
| E家族 | BIO标签/关系类别非执行K；固定抽取流程未排除 |
| F真实批 | 862真实法规句子，但没有862真实建筑设计审核记录 |
| Ggold | 人工实体/关系标注，不是官方合规裁决；公开label须私有隔离 |
| H获取 | 原论文与完整repo已下载；法规/指南/CSV齐备，资产许可仍需分别复核 |

论文来源统计为英国23文档1455页、芬兰10文档140页；是原法规总量，非每条记录需要读取的共享E成本。作者从1246个self-contained句子随机选862个标注。当前本地CSV实体all862/train689/test173；关系all4329/train3463/test866。关系行不是独立建筑或独立句子数量。

| Query | 数据湖数据1 | 数据湖数据2 | gold |
|---|---|---|---|
| 法规句子→实体BIO | annotated_data/entities/all.csv：content/processed_content | Annotation_Strategy_V1.0.0.pdf | label，862行 |
| 给定实体对→关系 | annotated_data/relations/all.csv：tagged_sentence | 同指南 | relation_type，4329行 |
| 建筑→合规 | 未提供建筑设计/检查案例 | 法规PDF确有，但不能创造案件 | 未提供 |

| 类Python DAG | 具体数据/性质 |
|---|---|
| `rows=scan_csv(entities)` | 普通读取862法规句子 |
| `labels=sem_map(tag_entities, rows.content, E.guideline)` | 语义抽取决定原BIO gold |
| `pairs=given_entity_pairs(relations)` | 普通读取给定实体边界 |
| `y=sem_map(classify_relation,pairs,E.guideline)` | 固定关系分类；不是合规判断 |

真实发布样例：relations/all.csv首行，example_id0071a7ee-a50c-44ab-a562-d99bf06d7918，metadata关联118_UK_DocS_InfrastructureForChargingOfElectricalVehicles。内容为文字应分三行显示，给定text与displayed over three lines两实体，gold为necessity。这是条款语义关系；没有实际设施是否按三行显示的信息。

| 方法 | 预期结果（未实测） | 过程 | operator结构 |
|---|---|---|---|
| LOTUS仅任务 | necessity可由句意判断；标签约定风险 | 固定关系分类 | sem_map |
| LOTUS完整指南 | necessity是原gold目标，未观测输出 | 固定指南+实体对分类 | compile_schema→classify |
| 逐条Data Agent | 同一目标，不预期天然更准 | ==查necessity定义及标注边界==→分类 | 同固定关系链接可覆盖 |
| 批Data Agent | 共享指南读取，收益未知 | ==预建标签定义==→批量分类 | 共享schema缓存，未证家族 |

ρE为指南解释，ρP固定标注程序，ρG未观测，ρR逐句解释；K和比例未知。原实体任务的信息不足状态未独立冻结，不自创合规UNKNOWN标签。十问已由q、E/x区分、标注来源、C/D/E缺口、过程及泄漏边界覆盖：目前不能证明区别于普通条件抽取。原固定实体/关系抽取也是可审查的任务，用户并未要求输出必须是案件裁决；但它尚不满足复杂共享E及家族执行要求。

[原文件统计与首行证据](../artifact/evidence/shared-environment-strict-codeaccord/source.json)。不能以缺建筑裁定gold否定原固定抽取任务；本次不补造建筑gold。原文档可作为后续环境素材，不计合格数据湖。

## 固定任务口径与实际共享指南补证

撤回以“实体/关系gold非合规裁定”为淘汰理由：人工抽取gold同样符合输出形式要求，A与真实法规句子的F应按原任务审查。实际E是Annotation_Strategy_V1.0.0.pdf，本轮读取13页、pdftotext空白分词2,988词；不是1595页被抽取法规。指南的complete-regulatory定义要求句内细节完整且无不能解析的外部引用。该选择支持自包含语句上的固定标签抽取，不支持逐记录探索庞大环境的成本主张。

仍保留Reject：实际共享指南较短，固定全指南抽取没有被排除，未证明语义执行家族；C20实体依据尚未闭合。此处Reject只针对当前研究目标，不以任务必须输出裁定为理由。页数/词数是本轮实际测量；没有模型或方法优劣实验。
