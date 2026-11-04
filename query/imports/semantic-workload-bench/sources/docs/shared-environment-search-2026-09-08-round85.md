# Increment85 — IPF机制语料：原论文、全仓库、40页指南已核验

当前7/15，IPF待进一步构造核验。下载[原论文](https://www.nature.com/articles/s41598-023-32915-8.pdf)2549144bytes，SHA25685d3438ee4abaeb52268cf592f6a1e05ef08b4fb743fba278d2a71a1d06ec8a3；[完整作者仓库](https://github.com/ezcatdb/prism_IPFdata)commit264e3d9ba741939e81f9a1d3b522fa39aaa479f1，5103193bytes/438entries/433Git blobs，CRC与所有blob SHA1通过。ZIP SHA256dcab105b93b294d8af55cda01c9dcf91113aa18467400de9afc9edd875f973aa。

仓库自带[实际指南](https://ezcatdb.github.io/prism_IPFdata/AnnotationGuideline_IPFmechanism.pdf)40页、4146551bytes、5866可提取词，含大量示例图；不能将可提取词数视作完整图示内容。原论文确认MetaMap Lite/UMLS2018AB自动预标注后由人工修订，150摘要中30有两名标注者，120不是双人独立一致gold。两份IAA版本不增加文档数。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 从IPF文献建立事件—角色—生物层级索引 | IPF_corpus150真实PubMed摘要 | 同一40页实体/事件/角色/修饰协议 | 完整摘要；外部UMLS只在规范化任务确有需要时加入 | 4899事件、8192论元；13049 span混合实体与触发词 |
| 筛选被否定或推测的事件，构建证据状态表 | 同150篇及事件信息 | 指南Negated/Speculated和Cue规则 | 若给定事件库存须明确annotation-given，不能提供目标Cue链接或修饰gold | Negated93、Speculated590；Count_sbjct24另属实体属性，不能混入 |
| 将实体/事件规范化到数据库ID（潜力任务） | 同源词面与上下文 | UMLS2018AB与NCIm使用规范 | 精确词典版本未取得，不允许从本批N记录造公开字典 | 13487条N行；尚未核验全部ID与完整性，不作为本轮可执行任务 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `abstracts.sem_map(event_graph,E).explode().filter(type=='Gene_expression').project(theme,atLoc)` | 150文档→4899事件 | Gene_expression611；Theme、atLoc原生gold可取 |
| `events.sem_map(modifications,E).filter(Speculated).count()` | 4899原生事件的目标属性需逐一确认默认及附着 | 590 Speculated原始属性行，不先假定全为590唯一有效事件 |
| `event_graph.filter(type=='Negative_regulation').project(cause,theme)` | Negative_regulation570 | 是已有事件图的投影，不把筛选变体算新语义任务 |

具体PMID11031344：E1 Gene_expression由levels[19:25]触发，Theme=chemokine[9:18]、atLoc=bronchoalveolar lavage fluid[29:57]。这依赖事件边界及角色规则，而不只是出现某关键词。由原始ann解析，未运行模型。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标E1 Gene_expression/Theme=chemokine/atLoc=bronchoalveolar lavage fluid，实测未知 | 固定sem_map提供全文及同一必要规则/图示；可固定检索或仅E编译 | 同一目标，未知是否优于静态 | ==查Gene_expression边界与Theme必须为GGPs、atLoc允许类型==→定位上下文→输出结构 | `entity_and_trigger_inventory→typed_role_binding→graph_validation`；尚未单轨迹提取 |
| 目标保留原生Negated/Speculated状态，实际预测未知 | 固定规则与全文判断作用域，所有方法给定输入一致 | 同一目标 | ==区分Negative_regulation与否定修饰，核对Cue作用对象==→标属性→下游筛选 | `scope_resolution→event_modification→typed_projection`；不能提前公开目标Cue链接 |

全150正文span切片及事件引用检查0错误，但发现3条不符合标准ann行结构的尾行：28353114.ann的ment、28596432.ann的r Diseases、23967151.ann的Scientific Study。不能因当前parser略过未知行而声称完整格式验证通过。需继续确认是否为N记录换行损坏，保持源字节不变。568事件没有论元；指南部分类型允许optional Theme，不能全归为漏标，也不能一概接受，需按类型核验。

下一步：严谨解析异常行、属性附着与缺省、图示OCR及示例泄漏、与MLEE/GENIA等PMID重叠、40页中目标所需范围、许可。License.html声明AIST注释/指南版权与PubMed文本分别受权利约束，没有发现明确CC授权文本；公开可下载不代表允许再分发。当前仅本地研究核验，不做外发授权推断。

脚本/收据artifact/evidence/shared-environment-audit-20260908-v85，原始下载data同后缀。无模型、评分、成本或Agent优势结论，不增加第8湖。
