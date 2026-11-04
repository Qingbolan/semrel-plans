# 第61增量：OPP-115原论文与完整作者发布包，暂不合格

合格保持3/10。OPP-115是同一schema下真实隐私政策实践抽取候选；政策是每条输入x，schema才是共享E，不能把115个不同政策各自的长度算作共享长E。也不能将描述性实践gold转称GDPR合法/违法gold。

[原ACL2016论文](https://usableprivacy.org/static/files/swilson_acl_2016.pdf)11页462148bytes已下载，SHA256 18e4e3410169571abdc8b86efa8250111e13556e801fe51adcee4ea1f190f963。[作者完整发布包](https://usableprivacy.org/static/data/OPP-115_v1_0.zip)99101239bytes、7455ZIP条目CRC通过并解压，SHA256 305ccb1dddaaab5e12f49decf8b132844eb7fd31fce284650d77213e5d3e37e2。这是完整数据仓库发布包，不冒称另有Git源码仓库。已读取readme、manual、categories XML、全部原annotations和三种consolidations；未运行作者代码或原网站脚本。

共享schema版本20151115-01，10类别、36属性出现项、259值出现项；XML文本5992词，描述文本去重3655词。属性和值出现项可能重复，不能当唯一属性/枚举数。完整包未发现长标注PDF；11页研究论文不是标注协议。当前不能证明复杂共享E足以支持用户要求，不能用额外GDPR全文人为加长环境。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 提取政策中的第三方共享实践、信息类型、目的及用户选择，按政策汇总 | categories-july30.xml及默认/可选属性定义，5992词 | 115份sanitized policy，3792个|||分段，含原始网页/PDF另存 | 23194条独立标注员记录，10位标注员；非23194独立实践或裁决gold |
| sci-news.com段9开发例：does not sell, trade or rent personal information to third parties | Does/Does Not、Action Third Party、Choice Type、Unspecified等定义 | 原政策及未来可能通知用户/退出的上下文 | annotator121记录20337：Does Not；Receive/Shared with；Generic personal information；Unnamed third party；不能称三人一致 |

| 类python的DAG | 实际数值/状态 |
|---|---|
| `segments=scan(sanitized_policies)` | 115政策3792段，分段不是独立网站 |
| `practices=sem_map(segment, full_policy, shared_schema)` | 原23194条、146926个JSON属性项；不同于论文128347 annotated attributes口径，需确认not-selected等计数 |
| `select(category='Third Party Sharing/Collection')` | 原始三人记录合计5221条，含冗余 |
| `groupby(policy).collect(practices)` | consolidation阈值0.5/0.75/1.0分别17291/19720/21510总记录；未选一个当唯一gold |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 例中否定共享应显式Does Not，未来通知/退出保持条件语义；实际准确性未知 | 固定schema条件映射、属性约束与段/全文上下文；可同资源检索 | 同一目标，未预设优势 | ==检查否定作用域、当前与未来条件、可选属性默认、未说明与否定的区别==→实践结构 | schema索引→实践识别→属性赋值→否定/条件检查→聚合；未学习或执行 |

作者documentation/errant_span_indexes实际794条登记，不等于794个不同政策/唯一错误；缺mandatory span等errata另有说明。三位法律研究生独立标注，合并采用重叠阈值/多数表决和Unspecified处理，不能冒称全部专家裁决一致。pretty_print目录是人工标签派生文字，禁止给模型当辅助政策原文。

许可见[作者数据页](https://usableprivacy.org/data)：研究教学用途、非商业条件；本次仅本地审计，没有联系作者或外发成果。数据/脚本/哈希在v61目录，未建public快照。无模型、确认split、prompt/种子/预算/缓存、优势或成本结果，新工程测试0。下一步可查另有明确法规协议及人工审计决定的来源，不为凑数量强行认定本湖合格。
