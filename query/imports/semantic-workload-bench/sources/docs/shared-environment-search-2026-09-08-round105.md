# Increment105 — MaintIE规范补查：IEC公开预览只能提供局部依据

仍7/15。复用round104已下载的完整原论文/作者仓库及全量gold。新增实际下载[标准机构SIST公开预览](https://preview.sist.si/sist-preview/21908/1b996d119d0945b2b28359332ffa9b3f/IEC-81346-2-2019.pdf)：15页1935837bytes，SHA256 a6e55639b0be8d238f5fe2a2b097efccb9fab9a622ee31228e1e7aa9bdc5c3cb。它明确是preview，含前言、分类原则、一级类及第二级表格的B/C部分；完整三级分类Table3只在目录出现（从标准印刷页26开始），未取得。不能把原标准目录87页以上视作已下载全文。

另查到第一作者[学位论文官方页面](https://research-repository.uwa.edu.au/en/publications/automatic-knowledge-extraction-from-industrial-maintenance-short-/)，可能包含IEC代码到语义名称的转换说明，但API下载本地403，页面实际文件链接浏览也403；未下载成功，搜索摘要不能充当已读论文证据。ANSI预览也403。失败收据与成功SIST下载分列，不购买或绕过访问限制。

实际局部核验：预览BT给出temperature sensing object的功能说明与传感器/温度开关等例词，支持按功能理解MaintIE TemperatureSensingObject。gold中该类有3提及（索引0、1、39）。这仅证明一个类别与公开标准依据可对应，不能推广至224类或证明长E推理必要。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 批量从维修工单抽取功能类型、部件关系和状态 | round104全量1076gold工单、3397实体、2341关系 | MaintIE短规则＋分类表＋本轮15页IEC不完整预览 | 同公开输入，缺完整IEC类型定义 | 完整语义抽取仍未获规范闭合，不计合格湖 |
| 索引39：识别axle temperature sensor fault | 5个token，temperature sensor为2–4半开区间 | BT温度感测功能可定位；axle对应类不在当前可核验的细分表中 | fault文本不能自动升级为完全失效 | sensor=TemperatureSensingObject；axle=MechanicalEnergyTransformingObject；fault=UndesirableState；axle hasPart sensor，fault hasPatient sensor |
| 汇总温度感测物件的状态提及 | gold0/1 thermostat、39 temperature sensor | 通用失败/不良状态层级以及BT局部依据 | 三条都是状态→sensor关系 | 2条FailedState、1条较宽UndesirableState；不是3台不同设备的失效率 |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `orders.sem_map(entities_and_relations,E).join(patient_type).groupby(state_type)` | 全1076工单待运行；温度感测物件开发例3条 | 派生gold：FailedState2、UndesirableState1；不可把它们作为按gold选出的确认批次 |
| `text39.sem_map(graph)` | 3实体、2关系 | 状态较宽，不默默将fault改成FailedState |
| `audit_type_names_in_preview()` | 26类名称字符串匹配，涉及171/1994物件提及 | 只是诊断；包含Gas/Person等普通词偶合，绝不是171项定义覆盖或正确率 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 索引39目标为3实体2关系，fault为UndesirableState；实际未知 | 相同公开词表/规则/预览固定sem_map；同样允许固定检索 | 相同目标，不保证Agent能补齐未公开分类定义 | ==定位BT功能类、核对状态粒度；发现axle细类依据未完整取得==→输出并按协议处理不确定性 | `function_class_lookup→state_specificity→part_and_patient_relations→validate`仅设想，未从轨迹生成 |
| 三温度传感物件提及派生统计目标2/1 | 固定抽取后确定性分组；不读gold选择输入 | 同目标 | ==共享解析类型层级==→逐条抽取→固定聚合 | 层级映射缓存＋结构抽取；E-only编译与CodingAgent仍必须比较 |

结论：来源补查获得了可用的局部标准依据，但没有补齐关键缺口；暂缓MaintIE长E资格。若之后获得完整合法公开分类定义及作者语义名称映射，可继续；当前不通过把任务缩成单一BT类别或6种关系来凑15湖。其他候选仍可推进，非全局blocked。

证据artifact/evidence/shared-environment-audit-20260908-v105/downloads.json、audit.py、audit.json；原始预览data/shared-environment-audit-20260908-v105/sist-preview.pdf。PDF允许复制，pdftotext成功但报告链接注释destination警告；这不影响已读文字，不代表全文完整。无模型、公私快照构造、独立确认、作者代码运行或成本测量。IEC预览的查看权利不等于可整份纳入公开再分发artifact。
