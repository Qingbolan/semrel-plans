# 增量195：RED长规范成立，公开完整批量未取得

本轮新来源RED，不同于Rich ERE。已下载[原论文](https://aclanthology.org/W16-5706.pdf)143026bytes，完整[作者规范仓库](https://github.com/timjogorman/RicherEventDescription)commit `e9093ae763894c6f21b9afc4e3bda3a159ce250c`，5tracked files。guidelines.md为v1.7、196547bytes、29541词，确有复杂共享规范；但作者README称其为持续更新文档。LDC发布README说明随数据附规范快照，未取得该快照，不能自动视当前Git版本与发布版完全相同。

[LDC官方目录](https://catalog.ldc.upenn.edu/LDC2016T23)说明完整语料95篇（20/20/55三个来源分组），属于许可获取的LDC2016T23，页面要求登录查询适用费用；未购买、未请求用户凭证、未下载完整包。作者Git不含语料。实际下载的是官方公开sample原文1265bytes和sample标注3401bytes，以及README3075bytes、目录HTML；不能称下载了95篇数据。

实际XML样例只有11个markable（8ENTITY、2EVENT、1DOCTIME），0relation。逐span取原始文本成功得到leaves172:178、left353:357，二者DocTimeRel=BEFORE、ContextualModality=ACTUAL、Polarity=POS。标题中现在时leaves并不意味着其事件在文档时间之后，这可作为规范语义的具体开发例；但一个样例不能证明长E必要性或批量gold完整性。完整README的8731事件、4209TLINK、2049IDENT链等属于发布方报告，未本次全量复算。公开sample无关系，不能给出已核的因果关系实例。

原件data/shared-environment-audit-20260908-v195；URL、hash、完整Git清单、sample-audit.json在artifact/evidence/shared-environment-audit-20260908-v195。官方版权涵盖各新闻来源和机构，公开sample不构成完整语料自由再分发许可。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 新闻/论坛→事件与模态→实际事件清单 | 已得1篇公开sample；完整95篇未得 | v1.7完整规范29541词；发布快照绑定待核 | 文章日期和上下文 | 已核2EVENT：leaves/left，ACTUAL、POS |
| 给定事件→相对文档时间→时间线 | 同sample、日期2010-04-14 | DocTimeRel规则 | 上游给定或预测事件，明确契约 | 两个事件均BEFORE |
| 给定markables→共指/时间/因果图 | 完整95篇输入未得 | 同规范关系章节 | 上游裁决markables是原任务给定输入的一种条件 | 完整关系只有发布方统计，公开sample0关系，未核验 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(docs).sem_map(events,E).sem_map(modality,E).filter(actual)` | 实际1文档2事件，不是8731已下载事件 | 不能加入公开批量合格名单 |
| `events.sem_map(doc_time_relation,E,doc_date).groupby(doc).assemble_timeline()` | leaves172:178、left353:357均BEFORE | 非时间词面分类；模型结果未知 |
| `markables.sem_map(relations,E).assemble_graph()` | 发布方95篇/4209TLINK；本地sample0关系 | 有长规范不代表批量数据已可用 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例两事件目标ACTUAL/BEFORE，实际未知 | 同全文和规范固定事件→属性调用，可检索规范 | 同目标，不预设优势 | ==查新闻标题时间解释、文档日期与DocTimeRel定义== → 输出属性 | `EventAttributeMapper(version, modality_rules, doc_time_rules)` |
| 关系图目标待完整gold获取 | 同资源固定文档图抽取与检查 | 同目标，实际未知 | ==查时间/因果/共指及冲突规则== → 关系 → 公共schema检查 | `RelationResolver + GraphValidator` |

所有方法未执行，==为可观察查阅，不记录私人思维链。CodingAgent/E-only编译/静态程序可同样提前索引完整规范；没有证据证明必须靠一次轨迹学习。RED暂不计入，仍11/15开发可构造来源。下一轮换公开完整输入和gold能实际取得的新来源，不把授权下载渠道等同于已获取数据。
