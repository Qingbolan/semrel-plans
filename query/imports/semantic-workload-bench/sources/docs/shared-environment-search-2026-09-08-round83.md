# Increment83 — E3C：关系结构完整，但协议与gold存在冲突

状态仍待核验，7/15不变。承接round82完整原论文、作者仓库及随库指南，未重新下载。来源：[作者仓库](https://github.com/hltfbk/E3C-Corpus)、[原始项目论文](https://aclanthology.org/2020.clicit-1.30.pdf)；精确commit/hash见round82。

本轮得到三项可改变下一步行动的证据：

- 422文档的26394个关系槽全部恰有一个来源节点，slot类型正确、目标存在；3128 PERTAINS均为RML→EVENT。结构验证不代表语义标签正确。
- 意大利86文档的双份METADATA在共同字段上无冲突，主要是一份额外包含docLanguage；可通过一致字段合并解决，不能用任取第一条的一般fallback。
- 随库v1.2指南PDF第9页规定所有GENERIC事件的DocTimeRel为OVERLAP，但实际有277条不满足：Basque88/English35/French42/Italian73/Spanish39。官网下载新版v2.0也保留同条规则，因此换指南版本不能直接解释这批冲突。

原生English反例：EN100024的procedure[2334:2343]标GENERIC/BEFORE；EN100046的presented[31:40]标GENERIC/IS-CONTAINED。此处只判定与明确规则不一致，不据此人工改成ACTUAL或其他gold。不能通过gold筛掉这些记录后声称独立确认。

时间锚还需保持语义准确：指南将DocTimeRel锚定在患者就诊/假定记录写作时间。不能未经验证就用METADATA.docTime中的来源日期替代这一锚。实际任务若使用此字段，需逐项证明它来自可用证据且符合任务含义；当前未建立这条链。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold与问题 |
|---|---|---|---|---|
| 抽取事件时间与事实性，形成病例事件表 | 422人工层病例文档 | 随库39页v1.2时间协议 | 必要正文/时间语境；不可默认发布时间=就诊时间 | 25259事件；277条GENERIC/DocTimeRel规则冲突，不能无条件用作协议一致性gold |
| 将测量结果归到检查/测量事件 | 同文档；可定义全抽取或明确给定EVENT/RML的链接任务 | RML与PERTAINS规则及必要事件边界规范 | 完整正文、公开可得单位和上下文 | 2863 RML、3128已标链接；157 RML无链接，不能自动当真实NONE |
| 抽取事件/临床实体本身 | 同人工层 | 对应39页/19页各自适用章节 | 必要文本，不公开entityID、xtra或目标属性 | 原生span可取；本轮属性冲突不自动证明全部span错误，也不证明span任务足以需要长E |

157个未连接RML分布：Basque17/English37/French60/Italian34/Spanish9。未连接可能是任务例外、信息不足或标注欠账，当前没有证据统一定性。保留原状，不把absence等同false。

| 类python的DAG | 具体数值 | 下游gold/判定边界 |
|---|---|---|
| `cases.sem_map(event_attributes,E).explode().filter(polarity=='NEG')` | English84文档4885事件 | 原始NEG456；跨字段冲突需诊断，不能将工程检查PASS当科学有效 |
| `cases.sem_map(result_to_test_links,E).explode().project(result,test)` | English480 RML、541原生PERTAINS；37RML无链接 | 541个正链接是已标注关系，未证明所有未标配对均为负例 |
| `cases.sem_map(temporal_graph,E).explode_edges().filter(role=='BEFORE')` | 全五语言26394关系槽结构通过 | 图中只标非冗余时间边，不能用全对全关系枚举直接与原始稀疏边比较 |

原生数值例子EN100017：`10.9 g/dl`[472:481]通过PERTAINS指向`haemoglobin`[460:471]；`70`[289:291]指向`rate`；`35%`指向`volume`；`positive`指向`parasites`。这些是实际XMI来源节点→slot→目标解析结果，不是模型生成。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标把10.9 g/dl连到haemoglobin；实际预测未知 | 完整输入的固定sem_map抽取结果/检查关系；若给定span则所有方法同样提供 | 同一目标，未预设优势 | ==核对PERTAINS方向、事件边界以及值/单位规则==→定位上下文检查名→输出连接 | `measurement_detection→test_reference_resolution→typed_link→endpoint_validation`；是否需长E须单独实测 |
| 目标输出事件属性，但冲突项暂不能定义同时满足协议和原始gold的唯一正确答案 | 固定模型按冻结规则输出；将数据冲突独立诊断，不靠调prompt强制拟合 | 同样受到gold冲突限制 | ==核对GENERIC与DocTimeRel约束==→发现与评测标签冲突时由评估侧登记，不向模型泄露gold | `attribute_map→constraint_check→diagnostic_status`；不能制造Agent优势或篡改标签 |

当前不构造“已验证时间推理任务”，也不因关系解析成功计第8湖。下一步可核对冲突是否源于某批次/转换，或验证其他独立字段任务的长E必要性；RML缺链接和稀疏TLINK也须先定评分契约。原有数据与gold未改。无模型调用、性能、成本或提取结果。

脚本/收据：`artifact/evidence/shared-environment-audit-20260908-v83/audit.py`及audit.json，覆盖422文件所有四种链接槽、metadata共同字段与一条明确GENERIC规则。范围之外的规则没有被验证，不将一条规则检查泛化为全部gold质量审计。
