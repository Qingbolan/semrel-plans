# 第四十六增量：FinTagging取得真实标注与官方长概念定义

**累计仍1/10；本轮新增有字节证据的待核候选。** 财务标签映射可放在固定DAG的sem_map中，但不能只因标签库很大就视作依赖复杂规范的判定任务。

| 来源 | 本次实际取得 |
|---|---|
| [FinTagging原论文v1](https://arxiv.org/pdf/2505.20650v1) | 20页、2,573,107 bytes |
| [完整作者仓库](https://github.com/The-FinAI/FinTagging) | commit `653650cbbab525227d20228c94a65600c1209c01`；22blob Git SHA1全部通过，ZIP CRC通过 |
| 作者benchmark_ground_truth_pipeline.json | 6,599条真实财报句子/HTML表格，52,572个实体、2,288概念；论文写52,740实体，相差168，未解释成错误或静默改数 |
| [官方2024 US-GAAP XSD](https://xbrl.fasb.org/us-gaap/2024/elts/us-gaap-2024.xsd) | 4,999,840 bytes，与仓库XSD逐字节一致 |
| [官方概念定义linkbase](https://xbrl.fasb.org/us-gaap/2024/elts/us-gaap-doc-2024.xml) | 13,810,878 bytes，14,918个documentation标签、416,694空白分词；SHA256 `96b321b294493af54253a45e3694e85d501857cb4029ba2529089ad9d7880872` |

作者库的BM25表17,388行只含tag名、类型和拆词名称，不是完整概念定义。此次补取官方定义后，才能对“分部”“合并权益”“非控制性权益”等概念作可追溯比较。没有下载全部计算、维度、展示linkbase，不能称完整GAAP规范包；XSD内容保留FASB权利声明，不给上游材料另加许可证。

实读数据有2,958条空实体标注，全部已标概念都在作者taxonomy中；110组完全重复text，不能把6,599条当作独立公司/报告。论文来源30份10-K，表中时间2024-02-13到2025-02-13，正文简称2024报告；源实体映射未保留在这份标注JSON，只有text/numeric_entities，没有公司、accession、期间及字符位置。

具体第0条Hubbell权益变动表中，common stock列的0.6也被标作StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest。**这不自动是错标**：XBRL可通过维度表达权益组成部分；但发布目标只保留concept/type/value，维度被省略。必须核原始XBRL后才能判断这种schema投影是否仍足以让公开表格唯一确定原标签，不能凭表面列名重标。

当前还未证明长定义相对标签名/短定义真正改变判定，也未完成来源维度和实体隔离审计。这里缺的是任务与证据对应，不要求先证明Data Agent比固定流程强。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在固定2024 US-GAAP下，逐段/表识别数值及其会计概念，生成标准化事实表 | 官方XSD与41.7万词概念定义；全量其他linkbase未取得 | 6,599句/表的原发布text；HTML只保留表结构 | 共享17,388概念目录；原报告accession、XBRL维度/context未随标注JSON保留 | 52,572个value/type/concept；不是本轮模型生成，尚未逐项源XBRL重审 |
| 第21条：“amounts ... not allocated to our two lines of business” | NumberOfReportableSegments官方定义为需单独报告财务信息的分部数量 | text中“two”，上下文提到前一表，前表关系未显式保留 | 候选概念与定义可公开检索，不能提供本条gold选定候选 | value=two，integerItemType，NumberOfReportableSegments；来源gold，不是模型输出 |
| 第0条Hubbell权益变动表的0.6 | 权益概念与维度规则 | common stock列0.6及整表 | 缺原context/dimensions映射；不能强制只按列名定concept | 发布StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest；需源核验，未判错 |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `scan(disclosures).sem_map(numeric_entities)` | 6,599输入，52,572实体参考 | 空标注2,958；不等于这些文本没有任何数字 |
| `retrieve(E,entity_context).sem_map(concept_alignment)` | taxonomy17,388，gold2,288概念均在其中 | 同E可以固定检索/缓存；不能把全集大小当作每次必要读量 |
| `project(value,type,concept).sem_filter(concept==target).aggregate()` | 第21条参考two→NumberOfReportableSegments | 单位/期间和维度尚未保留，不能直接跨报告求和 |
| `group_split(source_report)` | 源论文30份报告；110重复text组 | 当前JSON缺报告ID，未完成源实体划分 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 第21条参考integerItemType/NumberOfReportableSegments；未运行 | 固定数值识别→同taxonomy检索→定义/上下文复核→结构化输出；同样允许上下文补取工具与缓存 | 同目标，不预言更准确 | ==定位数值所描述对象==→==比较分部数量与其他计数概念定义==→==核前文/表头是否足够==→输出或ABSTAIN | `FinancialConceptOperator(E_version, table_context, candidate_retrieval, definition_alignment, dimensional_scope, evidence, abstain)`；必须包含只用名称、完整定义、固定工具、Coding Agent、批Agent和E-only编译对照 |

脚本/统计/哈希：artifact/evidence/shared-environment-audit-20260908-v46；原资产data同名目录。36310原论文/仓库、73900官方规范下载均正常结束。未执行作者notebook/模型；新增工程测试0，数据审计通过不代表财务正确性验证。该来源仍是候选，未通过所有严格条件。
