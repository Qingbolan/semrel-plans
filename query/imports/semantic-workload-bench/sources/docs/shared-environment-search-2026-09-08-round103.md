# Increment103 — MEANTIME多任务来源：原论文/作者评测仓库已得，完整数据及规范未得

仍7/15。MEANTIME不进入合格清单；本轮区分论文披露、作者代码与第三方样本，不把数据获取不完整掩盖成已验证可行。

已下载[原论文](https://aclanthology.org/L16-1699/)137759bytes，以及[NewsReader作者评测repo](https://github.com/newsreader/evaluation)完整ZIP100435bytes/72成员，commit212f7c63b91f5075258a334e2db3b29079f52ad3，CRC通过。README明确由FBK/EHU/VUA发布，Apache2软件许可；支持NER、NED、SRL、时间关系、事实性及共指，但要求另行下载gold目录，仓库不包含完整语料。未执行源码或下载其所有外部scorer依赖。

旧官网三处（数据页、文档级规范、跨文档规范）本地请求Connection refused；迁移域wordpress.let.vupr.nl同样失败。浏览工具对应502/timeout，原件缺失未通过其他途径假装补齐。规范引用为NWR-2014-2-2和NWR-2014-9，实际页数、字数与版本未核验，不能凭名称认定长E。

原论文和[作者机构资源页](https://nlplab.fbk.eu/tools-and-resources/lexical-resources-and-corpora/newsreader-meantime-corpus)说明120篇英语Wikinews，围绕Airbus/Boeing、Apple、Stock market、GM/Chrysler/Ford四主题；另外三语言为翻译，合480，不算四湖或480独立自然来源。英语为人工标注，其他语言部分投影；论文声称英语2096事件提及/1717事件实例，此数尚未全量复算。

进一步找到[第三方解析项目](https://github.com/neostrange/parseMEANTIME)，下载其完整repo commitf74539ba315c0dbd0dafb477b7f975e0b36d2102，ZIP通过CRC，只有两篇XML副本。第三方不等于原作者，也不是完整MEANTIME发布。两个文件原始token anchors检查通过，未与官方原件比对字节。只用作格式/任务实例探索。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | gold来源/状态 |
|---|---|---|---|---|
| 批量规范化新闻中的时间表达，支持时间轴 | 论文称120英语新闻；当前实际仅2篇第三方XML，不能称已得全库 | NewsReader文档级规则未下载成功 | 文档发表日期、时间表达周边正文；不是关系gold选出的上下文 | 两篇副本11个TIMEX3；整体gold完整性未求证 |
| 180695：把“yesterday”映射绝对日期 | 标题US stocks see 9% drop before making recovery；发表日期May07,2010；token22=yesterday | 应用相对日规则需日期锚；单例仅需短规则，不能据此证明长E | XML m_id8为CREATION_TIME2010-05-07 | 第三方副本m_id12 DATE2010-05-06、anchorTimeID8 |
| 提取事件/参与者并形成时间轴 | 180695副本652tokens、27EVENT_MENTION；76437副本503tokens、17EVENT_MENTION | 需要完整事件/角色/时间关系规范，尚未得 | 两篇HAS_PARTICIPANT21＋14，TLINK13＋11 | 当前仅副本记录，未冻结可运行gold；跨文档共指另需全库实例表 |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `news.sem_map(extract_normalized_times,E,date).explode()` | 样本2篇11TIMEX3，不是120篇已运行 | 180695 yesterday→2010-05-06；thirty minutes→PT30M；76437 today→2007-08-10，均副本实读 |
| `news.sem_map(events_and_roles,E).join(predicted_times).sem_map(temporal_links,E).order_events()` | 样本44事件提及、35参与者边、24TLINK | 只是原生格式计数；时间轴还需说明未标注边、跨文档相同事件等语义，不能直接排序冒充官方timeline gold |
| `xml.check_token_anchors()` | 两篇全部markable token anchor存在 | 格式检查通过不证明标签正确、来源一致或方法收益 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| yesterday→2010-05-06，实际未测 | 正文＋公开发表日期，固定sem_map或日期解析程序即可；不预设LLM必要 | 同目标，无依据认为Agent更好 | ==识别文档日期作为相对时间锚==→减一天→校验格式 | `extract_time_expression→resolve_anchor→normalize_date`；固定程序也可实现，未学习 |
| 复杂时间/事件角色图输出未知 | 完整同资源规范与正文，固定抽取/关系分类/校验 | 同输出契约、同资源 | ==检索时间范围与事件角色规则==→抽取→检查跨节点一致性；当前规范缺失不得编造规则 | `rule_index→event_mentions→participants→temporal_links→graph_checks`仅候选，未冻结 |

多任务潜力有作者评测源码支持，但不是已验证15湖之一。短相对日期例子不支持长环境必要性；跨文档关系也不能自动扩大单E数量。后续必须取得完整原始CAT/CROMER数据和实际规范，再核验标注范围（作者代码中部分模块按前5句评估，不能假设全文全任务穷尽标注）、实体/事件ID及跨文档实例表。不运行模型以弥补源材料缺失。

全部下载URL、SHA256、失败收据见artifact/evidence/shared-environment-audit-20260908-v103/downloads.json；audit.py/audit.json为两副本只读审计。原件在data/shared-environment-audit-20260908-v103/。没有公开快照、模型/成本实验、作者代码执行或联系作者。数据CC-BY的论文/机构声明与软件Apache2分开，不给第三方副本新增许可。
