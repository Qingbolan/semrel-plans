# 第二十五增量：UDRP检查包与共享规则实际引用

本轮构造了`data/shared-environment-audit-20260908-v25/packet/`，**开发检查用途，不是已验证benchmark**。数据来自第22轮已完整收到的近年分片；原论文及152页WIPO Overview3.0沿用原下载。作者843037756bytes完整归档仍由session11183下载，最近返回734003200bytes；尚未整档MD5验证。

构造脚本`artifact/evidence/shared-environment-audit-20260908-v25/build_inspection.py`按公开WIPO/D2024/单域名和章节格式选择：1603源记录，1572可定位§1开始/§6分析/§7决定，31标题待适配。公开侧保留§1–§5（身份、域名、程序、事实、双方主张），私有侧为§6分析/§7正式裁决/源metadata。不是原始诉状及附件，不可称前瞻部署数据。源选择不依据结果类别；仍需检查裁决前章节是否含本案结论。

初始私有正式决定提取1496 RELIEF_GRANTED/59 DENIED/17 UNANNOTATED；逐条读取17条，均为`orders ... transferred to the Complainant`而非`be transferred`，已以统一句式规则更正到单独`gold-extraction-v2.jsonl`，结果1513/59/0。原packet与manifest不改写；v2收据保留来源与哈希。标签仍明确是从正式裁决提取，未冒充新增人工专家标注。类别偏斜明显，必须有常量获救济基线，不能仅报告accuracy。

## 共享E为什么与这些案件有关

1572案中1543案的专家分析明确出现Overview3.0。简单邻接引用模式取得86种章节号候选，其中81种在已下载E的编号行中找到；5种可能是引用/OCR/脚注错误，未冒称全部是真实有效规则。常见规则包括证明责任§2.1、商标权§1.2.1、混淆§1.7、附加词§1.8；还涉及被动持有、出售、权利形成前注册等例外。这是实际裁决使用同一解释环境的证据，**不是81条规则均不可删减的因果证据，也不是性能优势**。引用统计只在研究/私有侧，不给模型按gold挑条款。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 对单域名投诉逐案判断是否应获得Transfer或Cancellation救济 | WIPO解释环境152页及所附政策、程序细则 | 1572记录；每条公开文本§1–§5，另31源记录待格式处理 | 程序及双方主张保留归属，历史判例引用不自动删除 | 1513获救济、59驳回，来自正式Decision的v2提取；保留原文供审核 |
| 驳回开发例D2024-0061，transco.com | 相似性、合法利益、是否针对商标注册等规则须分别判断 | 双方承认同名；被申请人主张通用组合和域名交易；其他主体也使用该词 | 商标历史/注册时间及双方相反陈述；不能只用2023新注册日期忽略既有使用历史 | 官方Complaint denied；本轮[原始PDF](https://www.wipo.int/amc/en/domains/search/text.jsp?case=D2024-0061)148189bytes已下载。选择用于补充先前Transfer例，属于开发曝光 |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `scan(source).filter(public_cohort).split_sections()` | 1603→1572解析/31待解析 | 不依据gold选容易案例；不能声称全1603可执行 |
| `sem_map(apply_udrp,E,procedural_facts_contentions)` | 1572公开输入，实际模型未执行 | 独立返回RELIEF_GRANTED/DENIED/ABSTAIN |
| `sem_filter(label==RELIEF_GRANTED).project(id).count()` | v2参考1513，**不是预测值** | 需要完整coverage、两类P/R与下游清单 |
| `evaluate(private_gold_v2,predictions)` | 原始17条提取失败已统一修正，不是模型重试 | 尚无模型指标或独立确认 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| D2024-0061目标DENIED，是否成功未知 | 固定同资源流程先抽出既有权利、取得域名时间、双方目的主张，再对照相关规则；不能将同名待售直接判胜 | 同目标；不得假定Agent比固定程序好 | ==核对旧商标/新注册/商业使用时间==→==核对主张的证据来源及共享规则中的适用条件==→输出结论与证据；禁止读取该案分析/决定 | `UDRPReliefOperator(E_hash, dated_facts, attributed_claims, three_elements, exceptions, procedural_conditions, abstain)`；不会把示范的transco或结果写入规则 |

验证：packet文件集合/hash、record_id唯一性/public-private对应、公开query字段allowlist和文本路径全部通过。标签提取v2另存，不改旧manifest；本轮工程测试0。还需全归档/许可、正式gold抽样审核、公开侧泄漏审核、31格式适配及源实体/模板隔离。不能将“能构造”提前改成VALIDATED。


## 本轮结束前追加：完整归档已完成

同一session11183成功结束，843,037,756bytes与Zenodo大小和MD5一致；SHA256见`data/shared-environment-audit-20260908-v22/artifact-receipt.json`。完整ZIP57条目、解压918,320,938bytes，所有CRC通过，已完整解压到v22/repo。先前分片与完整归档内文件SHA256一致。软件LICENSE为MIT；不将其扩张为所有上游裁决/官方指引的重新许可。目录清单在本轮`full-archive-inventory.json`。所有进程已结束；上文下载中状态是本轮较早观察。
