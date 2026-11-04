# 增量181：Potsdam Commentary Corpus，原件取得，暂不加入合格湖

本轮 SOURCE_DOWNLOADED / NATIVE_INSPECTED，合格开发来源仍10/15；不声称长环境必要性或Agent优势。一个PCC只算一个湖。

## 来源与实际下载

- [官方页](https://angcl.ling.uni-potsdam.de/resources/pcc.html)、[完整2.2发布包](https://angcl.ling.uni-potsdam.de/resources/pcc2.2.zip)：9,880,412 bytes，5074 ZIP成员（含发布者打包的.git），CRC通过；未运行其中代码。
- [原始2.2论文](https://aclanthology.org/2020.lrec-1.133.pdf)：220,824 bytes。
- [手册原件](https://publishup.uni-potsdam.de/files/8276/pcss8.pdf)：4,261,765 bytes，PDF实际234页；是PCC2.0手册。RST章印刷145–184约40页；共指所需名词表达及共指两章55–88约34页，不能把全书页数当每个任务必要长度。
- [摘要原论文](https://aclanthology.org/2022.coling-1.63.pdf)：1,561,149 bytes；[完整作者仓库](https://github.com/fhewett/pcc-summaries) commit `e08259f02e3b09491843946053e2afb9b8a3db59`，176 tracked files。
- 原件：`data/shared-environment-audit-20260908-v181/`；逐文件bytes/SHA256：`artifact/evidence/shared-environment-audit-20260908-v181/downloads.json`；统计/原始具体样本：同目录`audit.json`。
- 语料README明确CC-BY-NC-SA4.0；手册出版页为版权保护、无公共许可证，公开下载不等于可重新许可。摘要仓库自身未单独澄清许可范围。

## 原生数据核验

176篇RST全部XML可读，3018 EDUs、2437 groups、5102 parent边，无悬空parent。175篇有2根、1篇3根；例maz-19372标题是独立segment1，不能仅按多根判断错误，下一轮需核对标题与正文森林规范。

PDTB TSV按标准带引号TAB读取2204行，176篇：1112 explicit、905 implicit、96 AltLex、56 EntRel、35 NoRel。尚未与standoff XML逐项parity，因此行数是源表统计，不是已验证端到端评分契约。

摘要JSON174篇1990个句子键，rank1/2/3各174，0共1468；缺主语料的maz-00001与maz-00002。JSON以句子字符串作键，不能依赖字典顺序恢复文章；需对齐原文句号/句子ID。README说明30篇双标后按积分合并，平分随机选择，不能把排名看成唯一客观答案。

## 表1：查询和公开/私有输入

| Query | 数据湖 数据1：真实文章 | 数据湖 数据2：共享E | 数据湖 数据3：可选上游 | private gold |
|---|---|---|---|---|
| 每篇构造RST结构，并汇总reason/cause关系清单 | 176篇评论；例maz-19372讨论军用射击场争议 | 手册RST章及其分段约定，约40页主体 | 若给定人工EDU必须显式annotation-given；group/parent/relname隐藏 | 3018 EDUs上的5102原生parent边，含span；非全部都是语义关系 |
| 每篇识别名词表达与同一实体共指链 | 同176篇原文 | 手册第5、6章约34页及PCC适配 | 原生tokenization可公开；ParZu自动解析不能当人工gold | MMAX2尚待完整span/链审计；本轮不报实体量 |
| 给定论元，判定PDTB关系方向并聚合让步例 | maz-10110 relation6：前句说明求职困难，后句以Trotzdem转向企业仍提供帮助 | 2.2论文适配＋PDTB3规范；不能只用2.0手册 | 给定连接词/论元是annotation-given任务 | `Comparison.Concession.Arg2-as-denier`；2204条源表含多种type |
| 每篇选3句生成摘要，测RST中间步骤下游影响 | maz-19372，17句键 | 仓库短摘要说明；长RST规范只服务中间步骤 | 系统预测的RST可作为资源；用gold RST仅oracle诊断 | 174篇522个有序选择；不另算一个长E湖 |

## 表2：确定DAG与具体值

| 类python的DAG | 具体数值/源例 | 边界 |
|---|---|---|
| `scan(docs).sem_map(parse_rst,E).explode(edges).filter(rel in {reason,cause}).groupby(doc).count()` | maz-19372 EDU8→7为reason；group30→EDU14为cause；全库reason267/cause101 | 原生边方向必须保留；结构变换需官方/显式评分投影，不能只比较节点ID |
| `scan(docs).sem_map(markables,E).sem_map(coref,E).project(clusters)` | 176份MMAX层待审计 | 不能借用当前gold链、自动解析或总结答案 |
| `scan(argument_pairs).sem_map(sense,E).filter(sense == concession).project(doc,pair)` | maz-10110/6应输出Arg2-as-denier | 这是原生gold目标，不是LOTUS或Agent实测；全表不等于独立文档数 |
| `scan(docs).sem_map(parse_rst,E).sem_map(rank_sentences,summary_rule).topk(3)` | maz-19372 gold依次：射击场争议已持续十年；Freie Heide不放弃；未来场地可能不再需要 | 不预断RST必要；直接原文摘要/固定特征程序应作对照，rank平分机制需披露 |

## 表3：方法预期，均未执行

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| RST parse目标包含EDU8→7 reason；实际是否正确未知 | 固定sem_map获取原文/给定EDU与同一手册；允许固定检索和图检查；汇总用普通程序 | 同一结构/语义目标；没有证据一定更准确 | ==核对标题是否独立、读取核/卫星及reason/cause规则== → 输出关系 → 工具检查引用/结构 → 汇总 | `RSTParser(E_version, segmentation_contract, relation_inventory, title_policy, graph_validator, abstain_budget)`；仅设计，未学习 |
| PDTB例目标Arg2-as-denier；实际未知 | sem_map论元与版本固定规范，普通filter统计 | 相同目标 | ==确认2.2采用PDTB3、查让步及方向定义== → 比较论元 → 输出标签/依据 | `SenseClassifier(E_index, arg_orientation, type_rules, evidence_refs)` |
| 摘要目标rank1/2/3对应原生三个句子；实际未知 | 同资源固定RST→摘要流程，另设直接摘要 | 相同目标，不能预言Agent更接近主观排名 | ==核对摘要规范和句子对齐== → 读取预测RST → 排名并输出句子ID | `SummaryRanker(sentence_index, predicted_rst_features, rank_rule)`；短规范，不单独证明长E |

E-only编译、Coding Agent、批量共享缓存与固定检索均须同资源比较。==只表示可观察工具/文档探索，不记录私人思维链==。完整构造/示范/提取成本尚未测量。

## 下一步与不计入原因

核对标题/森林约定和RST标签定义、MMAX词/跨度/共指链引用，检查手册示例文章污染及跨版本变化；PDTB源表与XML对齐，摘要句序/重复句及两篇缺失原因。完成这些之前不升格为可构造合格湖。无模型执行、无冻结public/private快照、无独立确认、无E必要性实验。
