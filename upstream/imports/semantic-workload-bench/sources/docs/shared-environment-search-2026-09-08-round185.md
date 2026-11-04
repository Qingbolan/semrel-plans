# 增量185：SciER，下载后不纳入长共享环境清单

本轮新来源是SciER（EMNLP2024），不是SciERC（2018），不能混为同一论文或数据。完整[作者仓库](https://github.com/edzq/SciER) commit `db347813de379eb200e0813bbfee350d67e7c701`、20 tracked files及[原论文](https://aclanthology.org/2024.emnlp-main.726.pdf)已下载。原件`data/shared-environment-audit-20260908-v185/`，逐文件hash/bytes和统计`artifact/evidence/shared-environment-audit-20260908-v185/`。

## 决定与证据

不加入合格湖，仍11/15：共享Annotation Guideline.pdf实际8页、提取1262词（包含图例，纯文本词数不是图内全部信息）。它有真实全文和人工gold，但本轮未发现复杂长共享规范。106篇论文的长度是每个x的长度，不能替代E复杂度。

原生PLM JSON实际字段为doc_id/doc_tokens/sentences/ner/relations，与README展示的doc_key模板不同。首次按README字段读取报KeyError，检查实际对象后纠正统计；没有修改源文件。

原生统计：train80篇5575句18041实体8743关系；dev10篇713句2234实体1132关系；test10篇854句2948实体1626关系；OOD6篇580句1295实体582关系。并集106文档ID，split ID无重叠；共7722句24518实体12083关系。ID不重叠不证明无近重复或训练污染。共有9个实际关系标签，指南开头声称10种；需逐定义核对版本，不能把数量差异直接归为gold错误。

指南明确关系不跨句。这削弱“每个关系必须推理全文”的直接主张；仍可能有全文实体消歧价值，需实际消融。没有本轮LLM实验、E增益或轨迹提取。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐篇构造方法/数据集/任务关系图 | 106篇原生tokenized科学文档 | 共享8页指南，1262提取词；未满足长E证据 | 句界及doc_id；PLM与LLM两种表示不是两个数据湖 | 24518实体及12083关系 |
| 示例53719258第一句：哪些名字同义？ | 讨论3D卷积网络与既有2D CNN；实际输入保留英文句子 | Synonym-Of/Part-Of及实体span规则 | 全文4207tokens；关系标注限定句内 | CNNs→convolutional neural networks为Synonym-Of |

| 类python的DAG | 具体数值/目标 | 边界 |
|---|---|---|
| `scan(docs).explode(sentences).sem_map(entities,E).sem_map(relations,E).groupby(doc)` | 106docs→7722句→24518实体/12083关系为gold规模 | 实际预测未知；不能把句数当独立长文档数 |
| `relations.filter(Synonym_Of).project(subject,object)` | 示例CNNs与convolutional neural networks；全库1215源关系 | 与实体/关系同一标注派生，不是额外独立gold任务 |
| `relations.filter(Trained_With).project(method,dataset)` | 全库478源关系 | 具体关系指针/类型约束和LLM-PLM parity未全审计 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例目标Synonym-Of；实际未知 | 固定sem_map同句与指南，固定span/引用检查 | 同一目标，实际未知 | ==读取缩写与实体边界、关系方向约定== → 抽实体 → 输出关系 | `EntityRelationExtractor(span_rules, relation_inventory, direction, validator)` |
| 训练数据集清单应匹配478原生关系投影；实际未知 | 固定关系抽取后普通filter/project | 同一目标，无预设优势 | ==核对Trained-With与Evaluated-With定义== → 抽取 → 固定投影 | 可由E直接生成规则；未证明需要单次执行轨迹 |

==只是可观察规范查阅==。短规范的E-only编译和固定程序是强对照，不能禁止它们读全文或用同工具制造差距。此来源保留为阴性检索记录，不充入15湖。

附：同轮只读发现[PedSHAC作者README](https://github.com/uw-bionlp/PedSHAC)仍表示数据待IRB及去标识后发布，因此没有启动其完整下载/任务登记，也没有联系作者。SciERC仅定位未下载，未作本轮核验成果。
