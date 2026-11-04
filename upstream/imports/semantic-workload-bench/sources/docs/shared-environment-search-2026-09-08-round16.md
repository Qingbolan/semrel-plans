# 第十六增量：ClinGen SOP9/10历史版本与实际升分例子

2026-09-08，Asia/Singapore。续接第十五轮原论文、完整作者仓库与数据下载，不重复下载。仍未列入严格通过，优先继续补齐可行性。

## 新取得的规范

- [SOP9官方入口](https://www.clinicalgenome.org/docs/gene-disease-validity-standard-operating-procedure-version-9/)与[完整PDF](https://www.clinicalgenome.org/site/assets/files/5391/version_9_gene_curation_sop_final2.pdf)，实际63页。
- [SOP10官方入口](https://www.clinicalgenome.org/docs/gene-disease-validity-standard-operating-procedures-version-10/)当前链接为[10.1版PDF](https://www.clinicalgenome.org/site/assets/files/9232/gene_curation_sop_version_10_1_docx.pdf)，实际65页。数据仅标SOP10，不能静默认作同一精确版本。

下载位于`data/shared-environment-audit-20260908-v16/`；[URL/字节/hash收据](../artifact/evidence/shared-environment-audit-20260908-v16/download-receipts.json)。原论文及完整仓库版本见[第十五轮](shared-environment-search-2026-09-08-round15.md)。

## 增量统计

| 数据标记 | 查询—论文对 | 独立PMID | 专家证据行 | 非默认分值行 | gold显式其他PMID / 至少一篇不在论文表 | 日期train/test共享PMID |
| --- | --- | --- | --- | --- | --- | --- |
| SOP9 | 615 | 568 | 773 | 329 | 49 / 32 | 0 |
| SOP10 | 446 | 418 | 588 | 241 | 37 / 27 | 3 |
| SOP11 | 201 | 195 | 274 | 74 | 15 / 12 | 0 |

共享PMID为11980916、18852297、27066481（SOP10内部）。0重叠只表示这个精确PMID检查未发现，不表示跨版本/基因/近重复或模型预训练污染已排除。现有日期划分不是自动的源实体隔离。

[统计与可复算脚本](../artifact/evidence/shared-environment-audit-20260908-v16/statistics.json)；[audit_data.py](../artifact/evidence/shared-environment-audit-20260908-v16/audit_data.py)。PMID正则仅发现显式引用，不能将没有引用的行当作已证实自足。

## 具体升分例子

参数：ABCB7、mitochondrial disease、XL、SOP9；[PMID21464130](https://pubmed.ncbi.nlm.nih.gov/21464130/)，下载全文字段8,000词（本例恰为该值，未发现普遍8,000词截断，论文称无需截断）。原文研究ABCB7在线虫中的同源基因abtm-1，用突变和RNAi检测实验表型。

原gold类别为`Model Systems Non-human model organism`，实际3分、默认2分。专家升分解释为0.5胚胎致死＋2疾病表型再现＋0.5生化证据。摘要包括胚胎停滞、铁积累、氧化应激；更完整的表型说明在全文与专家描述中。不能只从摘要存在这些词就断言已独立复现3分，也不能将专家这次的0.5分拆法写成通用SOP规则。

SOP9实验性证据章节要求按实验对象与证据类型分类，默认分数可随证据强度调整。全文63页还有其他判读阶段；实验类别与矩阵集中在约39—42页附近，此外有通用评分原则。因此此例证明了具体规则与实验属性的关系，但尚不证明完整63页对每行都是必需输入。

[开发例子及原gold](../artifact/evidence/shared-environment-audit-20260908-v16/development-example.json)只用于构造审计，不能传给被测系统。首个SOP9非默认例为确定性开发选择，非独立确认。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按SOP9评分每个基因—疾病—论文中的实验证据 | 63页官方SOP9；相关类别矩阵与通用评分原则 | 615查询—论文对，568篇；基因/疾病/遗传方式为行参数 | 论文全文及允许的公开补充文献；缺口仍待补 | 773专家证据行，329非默认分 |
| ABCB7线虫模型是否高于默认分 | SOP9非人模型与强度调整规则 | PMID21464130全文8,000词 | 胚胎、表型与生化实验结果；不提供gold的分数拆解 | 模型类，3分（默认2）；派生“高于默认”TRUE |

## 类Python DAG

| 类python的DAG | 具体数值 | 状态 |
| --- | --- | --- |
| `R = join(SOP9_queries, papers)` | 615对/568PMID | 关联已统计，逐篇完整性待核 |
| `experiments = sem_map(R, E.experimental_categories)` | 原773个gold证据行 | 未执行，不能强制模型输出773项 |
| `score = sem_map(experiments, E, supporting_literature)` | 例3分/默认2 | 预期目标，非运行结果 |
| `selected = sem_filter(score, above_default)` | 例TRUE；329是不同于默认，不是全部高于默认 | 不能把下降分也计为升分 |
| `evaluate(private, frozen_outputs)` | 按PMID/基因疾病分组 | 未执行；先修正跨split共享论文 |

## 多种方法预期表

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| ABCB7例目标非人模型/3分；实测未知 | 固定抽取实验对象、干预、表型、功能结果→类别规则→同资源证据核对→评分 | 同目标，不能预设更准 | ==定位非人模型评分条款==→==核线虫同源基因与疾病表型关系==→==检查升分是否有独立实验依据==→评分 | `ExperimentSchema → CategoryResolver → StrengthAssessment → BoundsCheck` |
| 直接取默认2分会与本例gold不同，但不是强LOTUS基线 | 强基线允许同全文、规则、检索、循环及调整判断 | Agent也可能保守取2或错误升分 | ==查缺失证据而非默认补齐==→不充分时按契约ABSTAIN | 分值与证据充足性分别输出；不能复制专家当前0.5+2+0.5作为所有模型规则 |
| E-only编译/Coding Agent可能足够 | 直接从规范生成固定评分流程，完整成本对照 | 单轨迹提取尚未执行 | ==保存一次真实可观察规则/工具访问==→自动提取→冻结→独立实体批次 | 参数化条件、检索预算、评分上限与升级逻辑；不写死gene/PMID |

全部方法描述为预期，无模型/提取器运行。本轮补齐两个长规范文件、扩展三组缺证据与拆分审计、提供可复核升分例。下一步仍需核规范摘录与原文分值范围是否一致、补充证据的公平可访问性、完整论文质量；不能因download或计数通过就称研究有效性通过。
