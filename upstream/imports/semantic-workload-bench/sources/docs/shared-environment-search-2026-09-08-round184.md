# 增量184：PCC给定EDU的可构造开发范围

按当前清单统一的SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT等级，将PCC登记为第11个来源。**这只证明来源、复杂规范和可构造gold任务；不证明判断必须依赖长E、不证明Agent质量优势、不代表完成15湖科学验证目标。** 主原论文/官方完整包/摘要论文及完整仓库/234页手册均已下载，来源、hash、许可见181；MMAX格式工具见183，不重复下载。

## 本轮选择与验证

176篇中排除35篇，保留141篇；排除理由可重叠：全手册明确点名的22篇、与手册连续8个规范化词匹配的20篇、10篇disjunction版本冲突、1篇额外正文根。八词匹配新增未被前次点名名单覆盖的maz-00001、maz-9725、maz-9884。算法Unicode字母分词/小写，并连接手册跨行连字符；并非语义近重复或完整污染审计，可能有漏报/误报。选择已查看gold，全部属于开发暴露。

保留141篇共有2410 EDUs、1937 groups、4065 parent边：1498结构span、2567非span边。全部根形状是一标题segment加一正文group；所有非span边在本文件关系声明中存在。复用182全库无重复节点、parent循环和181无悬空引用检查。剩余实际非span关系均有手册同名定义标题；没有将disjunction重命名或给三根文章补边。

这141篇均在独立摘要JSON中，支持探索“RST解析→摘要排序”的下游任务。但摘要自身规范短；它只作为同一湖中的独立下游gold，不增加湖数，也不能预断依赖RST。独立摘要指另行人工标注，并不意味与RST作者/数据开发完全独立。排名平分随机处理的局限仍适用。

原生MMAX仍有未解决空前件和一项悬空group目标，所以共指任务保留候选，不随RST路线一起标为核验完成。任务范围变化明确记录，不声称整湖所有标注层合格。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 对评论正文构造RST图，形成每篇理由/因果清单 | 141真实评论，2410给定人工EDU；包括单独标题 | PCC同一手册RST章约40页及分段/标题约定；不是全234页皆必要 | 原始全文与EDU顺序，parent/group/relname不公开 | 1937groups、4065原生边，span单列 |
| 衡量预测RST结构对摘要排序的影响 | 同141篇的文章与句子 | 摘要仓库短排序说明 | 系统预测RST；gold RST仅oracle诊断 | 每篇独立3句排名；句子ID对齐与评分尚待实现 |
| maz-19372：哪句解释另一句？ | EDU7称元旦抗议游行的报道几乎多余；EDU8表示情况早已为人熟知 | Reason与Evidence/Justify区分，以及依附方向约定 | 完整评论中反复发生的场地争议 | 原生8→7为reason；不是关键词命中造标签 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(given_edus).groupby(doc).sem_map(parse_rst,E).project(graph)` | 141篇、2410EDU→结构预测 | annotation-given分段任务；不声称原文分句 |
| `graphs.explode(relations).filter(rel in {reason,cause}).project(doc,source,target)` | maz-19372保留8→7/reason | 这是同一图的下游投影，不是第二份独立gold |
| `docs.join(predicted_graph).sem_map(rank_sentences).topk(3)` | maz-19372三个gold摘要句依次涉及争议持续十年、Freie Heide坚持、未来场地不再需要 | 需与原文直接摘要/固定图特征/同资源Agent比较，不能假定图有增益 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例正确目标8→7/reason；实际未知 | 同资源固定规范检索+sem_map，可用标题/图检查器 | 相同目标，实际未知 | ==查询Reason/Evidence/Justify边界及核卫星规则== → 输出正文图 → 校验标题独立 | `RSTParser(E_version, relation_index, title_policy, attachment_rules, validator, abstain_budget)` |
| 摘要排序目标与独立JSON一致；实际未知 | 同一预测图+固定摘要sem_map；另设无图直接调用 | 相同目标，无预设准确率 | ==核对摘要说明与句子对齐== → 用预测结构排序 → 输出句子ID | `SummaryRanker(predicted_rst, sentence_index, summary_rule)` |
| E-only编译可能足够；未测 | 仅从E生成固定程序/检索索引 | 单轨迹产物必须与此竞争 | ==记录一次真实执行的查阅和工具收据== → 自动提取 → 冻结 → 未参与提取文档 | 目前均为结构设计，没有学习产物 |

==只标记可观察环境查阅==。所有系统可访问同样规范、工具与缓存；需比较批量Agent、Coding Agent和E-only编译，成本包含提取/校验，不能以逐行重复阅读弱基线证明摊销收益。

## 证据与剩余工作

`artifact/evidence/shared-environment-audit-20260908-v184/audit.json`含141完整名单、35排除及逐文匹配串；audit.py记录选择算法（额外根/声明校验结果在JSON）。未构造正式public/private快照、未跑官方结构评分、未穷尽跨层文本一致性/交叉跨度、未跑LLM或E增益消融。必须额外做独立确认；当前来源登记不能替代这些步骤。手册版权与语料CC-BY-NC-SA4.0分别适用。
