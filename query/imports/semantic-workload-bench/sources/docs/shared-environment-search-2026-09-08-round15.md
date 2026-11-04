# 第十五增量：CGBench / ClinGen，保留为优先核验候选

2026-09-08，Asia/Singapore。此轮发现更接近的真实规范驱动任务，尚不计通过；不因一个例子的缺证据整体否定数据。严格通过仍0/10。

## 原材料已实际取得

[原论文](https://arxiv.org/abs/2510.11985v1)，PDF1,313,852 bytes；[完整作者仓库](https://github.com/owencqueen/cgbench)，commit `db9f94152ca1872c8be8d8411040dcba2610b50b`，ZIP144,874 bytes、32个Git blob一致。[作者数据](https://huggingface.co/datasets/owencqueen/cgbench_data)冻结revision `6b017e57f18ccb1e6476260d9af4daa30508a523`；下载246个GCI/VCI规范与数据文件共107,865,551 bytes。不是整个HF仓库全部资产，VCI全文等未全部下载；GCI本轮所需论文表、标注表、元数据和SOP摘录已下载。未执行作者代码。

[官方SOP11入口](https://www.clinicalgenome.org/docs/gene-disease-validity-standard-operating-procedures-version-11/)及其[完整PDF](https://www.clinicalgenome.org/site/assets/files/9851/gene-disease_validity_standard_operating_procedures-_version_11_docx.pdf)：66页，1,345,736 bytes。它是2024年发布的历史版本，不换用最新版覆盖原标注版本。

原始资产`data/shared-environment-audit-20260908-v15/`；[下载收据](../artifact/evidence/shared-environment-audit-20260908-v15/download-receipts.json)、[统计](../artifact/evidence/shared-environment-audit-20260908-v15/statistics.json)、[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v15/audit_data.py)。

## 明确任务，不能扩大成临床诊断

GCI任务：给定(基因、疾病、遗传方式、论文)，根据冻结SOP提取实验性证据，判定证据类别、分值及升降分依据。gold来自ClinGen专家的真实文献判读，不是合成病例。它不等于最终“变异致病/不致病”判断；本轮不转换为该临床标签。

SOP规定实验类别、允许分数、实验支持要求、总分上限及证据重复计算边界。是否为患者细胞、非患者细胞、模型系统或救援实验会影响类别及分数；遗传方式和疾病背景也影响证据解释。因此这比通用文章主题分类更贴近规范驱动的语义操作。

但不能以全文66页证明每条都需要66页。原基准给模型的是实验性证据相关的JSON摘录；全SOP其他部分涉及另外的判读阶段。复杂环境的实际必要范围需要按任务与规则定位核实。

## 按同版SOP实际分组

| SOP | evidence标注行 | 查询—论文对 | 独立PMID | 本轮完整官方手册 |
| --- | --- | --- | --- | --- |
| 5 | 63 | 48 | 48 | 未下载 |
| 6 | 219 | 191 | 174 | 未下载 |
| 7 | 358 | 283 | 241 | 未下载 |
| 8 | 470 | 371 | 337 | 未下载 |
| 9 | 773 | 615 | 568 | 未下载 |
| 10 | 588 | 446 | 418 | 未下载 |
| 11 | 274 | 201 | 195 | 已下载66页 |

全表2745标注行对应2155查询—论文对，与论文任务样本单位区分。每对在下载论文表都有非空full_text字段；非空不等于完整无缺页、表格或附录。本轮未做逐篇完整性审计。SOP11原日期test为199对/193篇、272证据行；train有2对/2篇。首个test例子因本轮看过gold转为开发暴露，不再称未见确认。

同一SOP不同基因/疾病是参数化同任务，但不同SOP版本不自动算多个独立数据湖，更不能用这些版本凑够10个。

## 实际例子与证据缺口

SOP11；ADAR—ADAR-related type 1 interferonopathy，AD遗传；[PMID19060901](https://pubmed.ncbi.nlm.nih.gov/19060901/)。下载全文字段4,740词。论文研究ADAR1缺失对造血干细胞和干扰素信号的影响。原gold含Biochemical Function A、分值2（默认2）。

Biochemical Function A的规范需要证明目标基因产品与该疾病其他已知基因具有共同的、实验验证的生化功能。gold说明具体引用了PMID38489753与PMID19525956，讨论TREX1及SAMHD1。这两篇均不在已下载GCI论文表中。**这给出了具体Data Agent可能需要的补充文献探索，但尚未证明单论文默认输入充分。**不能把这两个gold选出的引用直接加给模型做oracle检索；应提供同等可访问的公开文献检索工具/冻结文献库，让各方法自行找到证据。

批量诊断：SOP11的274标注行中，15行gold说明显式提到其他PMID，其中12行至少一篇不在论文表；74行分值不同于默认值。计数是正则下限，未提PMID不证明无需额外证据，默认分也不证明无需推理。[跨论文诊断](../artifact/evidence/shared-environment-audit-20260908-v15/cross-paper-diagnostics.json)，[开发例子](../artifact/evidence/shared-environment-audit-20260908-v15/development-example.json)。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按SOP11，为每个基因—疾病—论文记录提取并评分实验性证据 | 官方SOP11，66页；任务相关规则需定位 | 201查询—论文对，195独立PMID，112基因疾病记录 | 下载GCI论文表8,395行，可作来源审计；未来公开检索库须另立构造契约 | 274证据标注，类别/说明/分值/调整理由 |
| ADAR例子是否有足够依据评为Biochemical Function A | 该类别要求与已知疾病基因共享经实验验证的功能 | PMID19060901全文字段4,740词 | 其他基因的支持文献在当前单论文输入外；不能提供gold选定答案链接 | 原类别A、2分；当前输入能否独立支持仍待核 |
| 筛出需要偏离默认分值的记录供复核 | SOP类别、默认值与允许调整原则 | 每条论文实验设计、对象、结果及疾病关系 | 同资源固定检索/工具程序也可用 | 74个非默认标注行；不能当74个独立病例 |

## 类Python DAG

| 类python的DAG | 具体数值 | 状态 |
| --- | --- | --- |
| `E = freeze(SOP11, scoring_rules)` | 66页，原任务摘录JSON已下载 | 原始材料已得；公开快照未构造 |
| `R = join(query_metadata, paper_text, on=pmid)` | 201对/195PMID | 已核非空文本关联，未验证完整性 |
| `evidence = sem_map(R, E.categories)` | 274行原gold目标，不是固定预测数 | 未运行 |
| `support = retrieve_public_literature(evidence.public_facts)` | 首例需要核其他已知基因的功能依据 | 拟议工具，不许查询当前gold说明 |
| `scored = sem_map(evidence, support, E)` | 首例目标A/2；74行原分值偏离默认 | 未运行 |
| `review = sem_filter(scored, score_differs_from_default)` | 行级派生下游任务 | 必须先冻结评分与重复证据单位，不能直接拿74当文档清单数量 |

## 多种方法预期表

均为未实测假设；未运行LOTUS、Data Agent、提取器，也不引用原论文的其他模型指标作为这些方法的结果。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| ADAR首例目标A/2；仅单论文能否命中及证据充分未知 | 规则分类→论文证据抽取→同资源固定检索其他疾病基因→评分 | 同目标，不保证改进 | ==定位A类“其他已知疾病基因”的要求==→==检查当前论文是否建立该关系==→==检索公开文献核功能与疾病关联==→评分 | `CategoryRequirements → EvidenceExtractor → SupportRetriever → ScoreValidator` |
| 非默认分值可能需要实验细节审查；结果未知 | 固定类别、分值范围、实验对象/对照/强度检查，允许检索和循环 | 是否改善需要同预算比较 | ==核模型/患者细胞/救援类别==→==对照默认值与调整依据==→记录证据 | 参数化证据槽、类别约束、默认/调整分支；不能记住当前gene/PMID分数 |
| E-only编译可能足够 | 从SOP直接生成固定程序，并保留Coding Agent对照 | 单轨迹提取须独立验证增量价值 | ==一次真实执行访问规则与证据==→自动提取→冻结→独立源实体批次 | 索引与规则共享、证据不足ABSTAIN/升级、完整提取摊销成本 |

## 下一步

优先继续这条路线：取得SOP9/10的完整对应版本；审计原评分规则和摘录一致性；核对论文、补充文献与专家判读是否充分；制定统一可公开检索资源。不要因少数补充引用缺失整体排除，也不要先称所有2155对合格。74个非默认分说明有实际评分变化，但不自动证明需要Agent或一次轨迹学习。

新增工程测试0，仅源下载、Git hash、版本关联和标注计数；没有临床验证、模型结果、完整运行器或public-only隔离。许可和完整论文再分发边界仍待分别核验。
