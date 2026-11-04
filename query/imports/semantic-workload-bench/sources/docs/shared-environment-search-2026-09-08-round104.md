# Increment104 — MaintIE工业维修工单：全量gold核验，规范仍不完整

仍7/15。本轮下载[原论文](https://aclanthology.org/2024.lrec-main.954/)13页及[完整作者repo](https://github.com/nlp-tlp/maintie)，commit825e7710e4129598da997276a38b3cb40b200bc2，ZIP1175249bytes/104成员/88文件，CRC通过。精确PDF/ZIP字节与SHA256见v104/downloads.json及paper-download.json。源代码、数据、SCHEME.md、GUIDELINES.md均实际读取，不运行作者训练代码；外部模型权重未下载，不宣称已复现模型。

真实来源：论文称从重型移动设备、铁路、矿物加工及基础设施维修工单随机抽样。公开的是专家规范化并脱敏的短文本，非原始缩写工单；ID/日期等被占位符替代。不能把后续语义抽取称为解决原始缩写解析，也不能按已隐藏设备ID验证资产分组隔离。

本轮全量gold1076条、1075种文本，3397实体、2341关系，实体跨度和关系索引全部有效。六类关系：hasPart533、hasPatient1206、isA364、hasAgent166、contains38、hasProperty34。README某段1067与实际1076不符，本轮以原文件计数为准。silver7000另列，不并为人工细粒度gold；与gold有7种精确重叠文本。gold索引874/875同文同标签（disconnect motor and reconnect new motor），不能算独立案例。

共享E实际：GUIDELINES.md约1893词，SCHEME.md约2698词（含表格/引用），224类均可与gold类型连接，但224行仅2行Definition非空；3371/3397实体提及对应空定义行。这不意味着3371个错误：类别名和例词提供部分信息，总类也有文字说明。问题是未获得作者直接采用的IEC81346-2:2019细粒度功能分类完整依据，不能凭表格行数声称长且完备的环境。仅实体名称的大目录也不自动证明探索推理必要。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 将维修短文本转为部件—状态—操作关系图，再统计故障部件类型 | 1076条规范化脱敏文本，1075种独特字符串 | 同一MaintIE层级类型表与关系规则；IEC完整定义未取得 | token边界可作为必要输入；不向模型暴露实体/关系 | 3397实体、2341关系，专家细粒度gold；不是维修成败、故障严重度或报废决策 |
| 具体gold索引0：识别空调中的故障部件 | `<id> air conditioner thermostat not working` | 物件按固有功能分类；State/Process区分；hasPart与hasPatient规则 | token1–2 air conditioner；3 thermostat；4–5 not working（此分段是评估结果，端到端模型不可直接获得） | air conditioner=ElectricCoolingObject；thermostat=TemperatureSensingObject；not working=FailedState；air conditioner hasPart thermostat，FailedState hasPatient thermostat |
| 索引874/875：抽取拆接操作与对象 | disconnect motor and reconnect new motor | Isolate/Assemble及电磁旋转驱动物件分类；关系方向操作→对象 | 两处motor是两个提及，不自动合成同一真实设备 | disconnect→首个motor、reconnect→第二个motor均hasPatient；重复两行完全同gold |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `orders.sem_map(extract_entities_and_relations,E).explode()` | 1076源行→原生3397实体2341边，模型输出规模未测 | token跨度/完整类型/关系端点评分；不可只按大类准确率冒充细粒度 |
| `graphs.filter(state='FailedState').join(patient).groupby(patient_type).count()` | 索引0派生输出TemperatureSensingObject计1 | 是从人工关系确定性派生的故障提及统计，不是独立设备故障率 |
| `graphs.filter(activity in ['Isolate','Assemble']).join(patient)` | 索引874目标两项操作，各1对象 | 875为重复文本，确认时需源文本分组，不当额外独立证据 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 索引0目标3实体、2关系，汇总thermostat类型故障1；实际未测 | 同公开类型表/规则＋完整tokens固定sem_map，再schema校验/固定关系聚合 | 同目标；不能保证填补缺失IEC定义或更准确 | ==核对物件功能分类、State与Process边界及关系方向==→抽取→校验→汇总 | `taxonomy_lookup→span_typing→part_relation→state_patient→schema_validation→aggregate`仅候选，未从轨迹提取 |
| 索引874目标Isolate、Assemble分别作用于两个motor提及 | 固定类型检索与抽取，允许缓存 | 同样输出，未知实际质量 | ==核对动作类型和对象功能类==→返回两组关系 | 共享词表索引＋语义抽取；须与E-only编译、CodingAgent及共享缓存Agent比较 |

另一个待核验点：GUIDELINES把“light in cabin not_working”列在Process示例下，但实际gold中精确“not working”21个提及均FailedState。不同上下文/下划线形式可能影响标注，因此这不是已确认gold错误，但不能按一个词面模板宣称规范完全一致。README演示change out engine的token跨度也不能替代原生全量检查；本轮原生跨度无错误。

本轮判定：工业use case明确、真实批量和专家结构gold已求证；共享规范完整性、复杂性仍不成立，暂不计第8湖。优先下一步查IEC分类定义的合法公开可得版本及其与224类映射，再检查规范示例/正文近重复、源资产不可见导致的划分限制。仅换成6种关系分类虽然更易执行，但规则更短，不能借此满足原长E目标。

证据：artifact/evidence/shared-environment-audit-20260908-v104/{audit.py,audit.json,examples.json,downloads.json,paper-download.json}。原件data/shared-environment-audit-20260908-v104/。无public快照、模型调用、下游运行、独立确认或成本优势；代码/数据MIT声明与原论文CC-BY-NC4.0、IEC标准权利分别处理。
