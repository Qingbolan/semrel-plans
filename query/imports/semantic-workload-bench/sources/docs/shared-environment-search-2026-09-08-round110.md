# 第110轮：DDI双格式一致性及必要输入审计

结论：905关系文档的XML/BRAT正文已全部对齐；903实体图、904正关系图相同。外部历史药物分类资源仍缺，不新增合格湖，仍7/15。

## 真实来源与本次增量

原论文、完整作者repo commit819b0fa538ed83ab2a8b4f5417bba3c03249b7f3、63页指南均复用[109轮下载收据](shared-environment-search-2026-09-08-round109.md)。本次未改任何源数据，未运行上游代码。

`artifact/evidence/shared-environment-audit-20260908-v110/parity.py`直接解析两种原生格式。XML句子逐一映射到BRAT正文，仅允许句间空白及句末空白变化；不替换正文字符，offset按实际匹配位置转换。905/905映射成功，244篇在未经处理的拼接上也字节相同。最初572个“缺BRAT”是审计错误移除Train文件名_ddi后缀造成，已修正；最初文本不匹配由句间空格/末尾换行造成，最终规则明确保留正文字符。

类型统一大小写，XML闭区间转BRAT半开区间，以实体类型+区间+surface和无向药物pair+关系类型比较多重集合。实体一致903/905，正关系一致904/905。此检查只覆盖正关系；BRAT缺边不能单独证明XML负例的科学正确性。

三项实质/字段差异：

- Dextroamphetamine_ddi：Amphetamines/corticosteroid正例，XML缺type；BRAT为INT。可以作为后续版本选择证据，不能悄悄合并发布版。
- Eszopiclone_ddi：(R)-warfarin两段offset不同；BRAT也需独立surface检查，不能仅因是另一个作者格式就自动视为正确。
- Lenalidomide_ddi：两版区间相同，surface分别为R- warfarin与R-warfarin，属于surface规范差异。

## 长环境是否完整

已阅读的指南§3.1要求ATC作为判断国际药物审批的主要参考，并列FDA/EMA/AEMPS等数据库作补充；DrugBank/MeSH用于同义词。当前仍未锁定标注时点的这些资源。单有63页PDF不代表端到端NER输入完整。

反过来，如果固定上游给定实体，将任务缩为句内DDI关系分类，核心关系规则及附录可能只需指南的一部分；不能借用NER规则页数证明关系分类存在长E成本。此区别决定后续构造是否有研究意义。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量抽取句内DDI类型并列出mechanism报告 | 905文档8275句33508pair | 63页规范，其中关系§4与附录为候选必要子集 | 若给定entities需标注annotation-given；端到端缺历史ATC等来源 | XML5000正例中4999有类型；BRAT提供缺失一例INT但有版本差异 |
| 对比同一Amphetamines/corticosteroid句子的发布版本 | 原句描述Amphetamines使plasma corticosteroid levels升高 | 两版作者发布文件，作为构造侧核验材料，不能供模型读取 | 文本不变，pair实体范围对齐 | XML：true、无type；BRAT：INT；不自行推断mechanism填补 |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold |
| --- | --- | --- | --- |
| `docs → sentence_pairs → sem_map(ddi_type,E) → filter(mechanism) → project(pair_id)` | 905文档、33508pair | 7599505.xml cobalt/iron示例目标mechanism；预测未知 | XML1621条mechanism，仍需排除坏例/指南泄漏后重新锁定 |
| `docs → sem_map(entity_spans_types,E,reference_catalogs) → groupby(type).count()` | 17805实体作为目标，不作为默认模型输入 | drug/brand/group/drug_n及跨度 | 历史reference_catalogs未取得，不能把当前空缺设为可执行成功 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| cobalt/iron目标mechanism；未执行 | 固定语义模板/章节检索+同资源附录，规则可批内缓存 | 同目标；没有优势证据 | ==确认当前任务是文本DDI而非现实药理预测== → ==检查PK过程定义及句内证据== → 类型输出 | `DDIRelation(text,pair;policy_version)`；规范范围→否定/限定→类型→校验；缺证据ABSTAIN |
| Dextroamphetamine缺类型实例不作为单一版本混合评分目标 | 不应由LOTUS替构造侧选择gold | 不应由Agent补gold | ==可观察任务执行不包含私有格式对账==；版本问题在实验前解决 | 算子不得读取私有双格式差异表；先冻结来源及排除清单 |

无模型调用或自动提取。本轮为源一致性证据，不是gold正确性、环境必要性、独立确认或实际摊销优势证明。

产物：`artifact/evidence/shared-environment-audit-20260908-v110/parity.py`与`parity.json`。无新单元测试、无commit。下一步应冻结NER/关系任务必要资源范围，并按完整任务要求选择继续补资源或暂缓，不能以格式通过代替研究有效性。
