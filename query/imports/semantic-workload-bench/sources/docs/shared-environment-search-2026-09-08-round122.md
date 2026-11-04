# 第122轮：VetClaims新25案可读，但环境树与旧版不相同

复用120轮完整源commitccb98b19525e；本轮无新下载。累计7/15不变，未将新25案算独立湖，也未将其认定为确认集。

## 实读结果

新25案2665句、188 Finding、227 Reasoning、539 Evidence、334 LegalRule、453 Citation、924默认Sentence。所有句子ID在各自文档内唯一。与旧50案相比无相同案号、无空白归一化全文完全重复；这不是患者实体/近重复/训练污染隔离证明。

25案各自规则树完全相同，每份19节点，共475节点，字段仅ruleID/label/operation/nodes。旧50案是18节点；新树多一条“There is adequate evidence that the veteran suffered from the claimed disease or injury while in service.”，其余节点文字均在旧树中存在。尚未逐边验证两schema逻辑等价，不能只重命名字段就共用旧E。可考虑分别冻结版本，但不额外计湖。

2665句中2569精确出现在内嵌原文、2609空白归一化后出现、56句不匹配。显式排版诊断（NFKC、弯引号→直引号、en/em dash→hyphen、去soft hyphen、空白归一化）可解释34句，仍22句不匹配；未改原字节或gold。至少两条默认Sentence是页脚与“ATTORNEY FOR THE BOARD”粘连，其他剩余差异待查，不统称语义错误。

与六协议进行≥12词整句匹配，12条匹配涉及5案。首例18151264P27S2引用PTSD stressor规则，与Citation协议匹配；这是通用法规引文，不能直接说整案来自规范示例，更不能把命中5案全部判成独立性失败。此前旧案1302554的具体Reasoning例仍属已确认直接答案示例，两者证据等级不同。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 在后续案件中提取事实认定与证据推理 | 新25案2665句，带内嵌判决原文 | 同家族39页作者协议，版本适用性仍需核验 | 新队列共享19节点规则树，不能默认为旧18节点树 | Finding188、Reasoning227；gold为角色，不是获赔结果 |
| 按案件汇总引用、法律规则和事实讨论 | 同一新队列 | Citation/LegalRule/Sentence等协议 | 18151264P27S2为PTSD法规引文，协议也展示此引文 | CitationSentence；该示例用于结构说明，不作为泛化正确案例 |

| 类python的DAG | 具体数值 | 中间条件 | 下游gold |
| --- | --- | --- | --- |
| `new_cases.sentences.sem_map(role,E19,context).filter(role=='FindingSentence').project(row_id)` | 2665→188源gold | E19版本冻结，源句/上下文映射先明确 | 188未实测预测；排版可解释34句不等于已完成构造 |
| `new_cases.sentences.sem_map(role,E19,context).filter(role=='ReasoningSentence').groupby(case).count()` | 25案→227源gold | 22句仍需来源说明，不能自动当执行失败或改标签 | 227仅总量，确认split与源投影未建立 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；引文例应CitationSentence，不能推断性能 | 同E19+协议固定分类→角色过滤；相同排版工具对各臂开放 | 未执行；同一目标，优势未知 | ==读取对应协议与E19规则== → ==确认句子在上下文的功能== → 输出角色 | `SentenceRole(text,context,E19,protocol_hash)`；单次提取不能忽略环境版本变更，不能读private角色 |

有意义的下一步是解决剩余22句来源映射、明确协议版本与新19节点树绑定，以及定义规则/示例隔离。旧与新队列共有75案并不自动构成同一个已冻结E的大批次。没有public快照、自动提取、模型运行或确认成绩。

产物：artifact/evidence/shared-environment-audit-20260908-v122/audit.py、audit.json、typography-diagnostic.json。可复跑`python3 artifact/evidence/shared-environment-audit-20260908-v122/audit.py`；排版诊断命令在工具记录中。无新单元测试、无commit，gold已查看仅开发用途。
