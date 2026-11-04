# 增量159：MuLMS官方任务是原始图的筛选与派生视图

沿用[158下载与源锁](shared-environment-search-2026-09-08-round158.md)，无重复下载。仍8/15。本轮读取作者锁定子模块的`source/data_handling/mulms_dataset.py`与`source/constants/constants.py`，不是推测关系别名处理。

## 官方源码结论

- 读取器495–503行读取原RelationType并检查13类rel_label_set。未看到将property_value改propertyValue或sameMeasurement改sameMeas的转换；不在白名单的标签被排除。3条空类型也不在白名单。
- 506–539行明确生成两跳派生关系：MEASUREMENT→PROPERTY的conditionProperty/measuresProperty，与PROPERTY→VALUE的propertyValue连接，分别成为conditionPropertyValue/measuresPropertyValue。中间属性可以是隐含实体。不是把所有数值一概贴到测量节点。
- 373行实体过滤implicitEntity；后续按token覆盖/类型过滤、同类型同偏移去重；548行后排除自关系/同span和部分跨句关系。源码有针对nanoparticle-type的特例，本轮不修改或推广该特例。
- 因此官方论文NER/关系设置不是原生全部49733实体22639关系。更不能把原始sameMeas集合称为作者现成评测任务，因为它不在此白名单。

已知指南15篇与SOFC DOI重叠4篇的并集共19篇，排除后31篇、24599原始实体、11867原始关系。8259边在13类关系白名单内，其余associatedInfo2757、sameMeas356、usesInstrument114、refersToMaterial374、resultOf6、空类型1。8259尚未应用句/token/隐含节点过滤，**不是官方loader最终输出数量**。

在全篇原生图上找到761条conditionPropertyValue两跳路径、387条measuresPropertyValue路径；这只是句/token过滤前的结构计数，不是新增独立人工标注。具体electrolysis_04路径的测量触发与隐含属性都锚定在“was employed”，值分别100 h、500mA/cm2。不同节点允许相同表面词，不能按span或词面先合并。

收据和可重跑脚本：`artifact/evidence/shared-environment-audit-20260908-v159/audit.py`与`audit.json`。脚本从作者Python AST读原13类常量，XML计数/两跳路径审计使用标准库；未执行完整puima/datasets loader，未声称逐条复现作者评分。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 范围 |
| --- | --- | --- | --- | --- |
| 抽取测量条件与测量结果 | 31篇排除已知污染后的全文 | 15页指南及作者明确两跳派生规则 | 原生隐含属性节点允许与触发同span | 761/387原生两跳路径，最终任务投影仍未冻结 |
| 抽取显式材料/数值关系 | 同批全文 | 13类官方关系白名单及定义 | token覆盖与同句条件 | 8259仅过类型筛选，不能当官方最终gold数 |
| 聚合同测量提及 | 同文原生图 | 指南sameMeas规则 | 需另立完整图任务契约 | 剩余356 sameMeas不属于该官方评估白名单；不是现成可比论文结果 |

| 类python的DAG | 具体数值 | 必须保留的语义 |
| --- | --- | --- |
| `documents.exclude(guide_ids | sofc_dois)` | 50→31篇 | 19篇为已知重叠，未证明不存在其他近重复 |
| `raw_edges.filter(type in official_labels)` | 11867→8259 | 后续实体/句界过滤尚未应用 |
| `measure_edges.join(property_value,on=property_node_id)` | 761条件值、387测量值路径 | 节点ID连接；不能按相同文本连接 |
| `paths.project(measurement,value,kind)` | 例was employed→100h、500mA/cm2为conditionPropertyValue | 隐含属性只是中间节点，仍需确定角色证据；不将两值误当结果 |

以下仅未执行的目标与方法设计。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 例中100h/500mA/cm2归到条件值，实际未测 | 固定抽取同类测量/属性/数值与角色，按明确两跳规则投影 | 相同目标，不声称优于固定流程 | ==查隐含属性和测量条件定义，回读句子==→输出带节点ID的图 | `TypedMeasurementGraph→PropertyPathProjection`；派生join是确定性步骤，不需要伪装Agent推理 |
| 保留同span不同角色节点 | 固定程序将节点身份与表面文本分离 | 相同要求 | ==确认公开节点契约，识别隐含属性的锚定规则==→图输出 | 类型化节点、关系与输出契约；是否能单轨迹提取需真实实验 |

本轮解决了“别名是否官方修正”的疑问，结论是当前读取器通过筛选构造较窄任务；没有替原数据做修正。余下31篇的复杂E价值、2024指南绑定、完整默认路径与确认规模仍不足，暂不升级。下轮转新的长规则来源，不将层层过滤后的工程通过当科研成立。无模型/prompt/种子/训练/费用/推理预算/测试套件/正式快照/scorer/commit。
