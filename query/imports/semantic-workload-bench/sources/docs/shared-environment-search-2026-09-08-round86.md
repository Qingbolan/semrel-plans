# Increment86 — IPF：严格标签审计、指南OCR与来源重叠

仍7/15。原论文/完整仓库/40页指南沿用round85已下载材料，commit264e3d9ba741939e81f9a1d3b522fa39aaa479f1。原始gold未修改，未生成公共实验快照。

本轮确认三条异常行是独立的无ID文本碎片，处在合法N/T记录之间，不能凭相邻位置断言它们属于哪个N名称；不自动拼接或改写。事件抽取任务可以在新版本契约中显式拒绝这些记录或分离无法解析的规范化层，但尚未选择并实施该构造。

全属性目标核对：93 Negated→E，590 Speculated→E，24 Count_sbjct→T，全部目标存在。此检查不证明属性判断正确，也未核对属性是否重复附着。无重复标准ID，未知尾行3条仍保留为格式问题。

随库annotation.conf为Gene_expression规定单一Theme:GGPs；611个该类事件中25个不满足这一组合条件，其中22缺Theme、3多Theme。文字指南说明Theme必须是genes/gene products，但未同样清楚规定只能一个，因此将这些记为配置与数据不一致，不一概称人类语义gold错误。全568无论元事件中19为Gene_expression；有些缺Theme事件仍有atLoc/Cue，因此568与缺Theme数量不是同一统计。

40页指南130dpi渲染/Tesseract3并发OCR完成。12词且≥65字符的连续匹配，150源摘要与指南文字/OCR无命中。视觉抽查第30页显示图例常只有3–8词，并混有角色标签，因此此阴性结果不能排除短示例或重排文字的泄漏。MLEE262摘要与本150篇按PMID交集0；其他GENIA/来源重叠待查，不能直接声称全部跨湖独立。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold状态 |
|---|---|---|---|---|
| 抽取机制事件图供主题/位置索引 | 150真实摘要 | 40页原始指南与图示，不能只给5866词纯文本 | 事件/实体必要上下文 | 4899事件8192论元；25个Gene_expression配置问题待定契约 |
| 按否定/推测状态筛选文献事件 | 同全文，是否给定事件库存需冻结 | 否定/推测作用域及Cue规则 | 不公开目标Cue链接与属性 | Negated93、Speculated590均附着E；不是实体属性Count_sbjct24 |
| 规范化实体与事件 | 原文和候选知识库 | UMLS2018AB/NCIm规则 | 历史词典未取得 | 13487N行关联层存在3个游离碎片，不能自动声称规范化gold完整 |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `abstracts.sem_map(event_graph,E).explode().filter(type=='Gene_expression')` | 150→4899事件→611Gene_expression | Theme结构应与配置冲突单列，不能用本批gold修补提取器 |
| `events.sem_map(status,E).filter(Speculated).project(event_id)` | 原生590条推测事件属性 | 确认目标类型E；唯一性/默认false语义仍待检查 |
| `event_graph.filter(type=='Negative_regulation')` | 570事件 | 调控下降不等于Negated，不得将两个字段合并 |

具体仍保留PMID11031344：levels→Gene_expression，Theme=chemokine，atLoc=bronchoalveolar lavage fluid。另PMID11491168的E5仅有atLoc/Cue，无Theme；原文含mRNA expression，不能将研究者自己补出的CTGF词面当官方gold。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标完整恢复11031344的事件角色；实际预测未知 | 同图示规则/完整正文的固定sem_map，可固定检索和类型检查 | 同一目标，未预设收益 | ==查Gene_expression与GGPs Theme、atLoc规则==→绑定论元→输出 | `type_rules→argument_binding→schema_diagnostics`；配置冲突不作为Agent胜出证据 |
| 目标分开标Negated与Negative_regulation | 固定作用域解析后下游筛选，输入条件与Agent对齐 | 同一目标 | ==查否定Cue作用事件及抑制调控类型差异==→状态输出 | `cue_scope→modification→downstream_filter`，没有真实轨迹提取结果 |

本轮只检查数据表示与规则一致性，不运行模型，不将工程PASS当环境因果增益。后续短示例/原论文图示审计、跨湖PMID、许可与可执行任务契约尚未结束。脚本ocr.py/audit.py/overlap.py及JSON在artifact/evidence/shared-environment-audit-20260908-v86，渲染/OCR在data同后缀。
