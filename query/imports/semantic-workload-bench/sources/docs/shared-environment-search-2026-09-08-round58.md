# 第58增量：SENTiVENT完整来源与首轮全量核验

新增独立候选，合格保持2/10。具体用途为财经新闻事件结构化和逐文档事件清单；不是投资收益预测或事实核查。下载和数据审计已完成，但原始XMI与转换gold的语义对应、示例隔离、public构造仍待核，尚不计入合格。

## 实际下载

- [原论文](https://doi.org/10.1007/s10579-021-09562-4)：33页2532494bytes；[早期论文](https://aclanthology.org/2020.fnp-1.36.pdf)：11页208384bytes。
- [作者完整数据仓库](https://huggingface.co/datasets/GillesJacobs/sentivent/tree/6a9e8f9fc11ba7db3d8dffe3e5df9e7b062e6441)，所有141个资产已下载，没有只取数据卡；与两篇论文和指南源码ZIP共144资产343980376bytes，全部成功。
- [指南完整源码仓库](https://github.com/GillesJ/sentivent-event-annotation-guidelines)，commit e845a5eb632580317832535abf9af9dda7aa8384，ZIP21条目CRC通过。虽然README说包括PDF，本次目录未发现PDF，另从作者大学库取得[原指南PDF](https://backoffice.biblio.ugent.be/download/8644921/8644923)：69页321919bytes，SHA256 daf38f3f93b058213f3677372a4c4748aa2cdf8d1e2dedc4c77b39392716e4db。
- 数据库含原WebAnno XMI发布ZIP，590条目CRC通过并解压。作者说明其匿名化了标注员ID，排除二进制CAS及项目元数据；不称其为未经处理的全部作者工作目录。

资产在data/shared-environment-audit-20260908-v58；下载脚本/哈希/全量审计在artifact/evidence/shared-environment-audit-20260908-v58。没有运行作者代码、模型或加载不可信序列化对象。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 按同一SENTiVENT规范提取公司新闻事件，返回证券价值事件清单及参数 | 69页协议：触发词、事件类型/子类、参数、否定/确定性、共指与类别混淆规则；v1.1含后续改进计划，不能把计划当已标注规则 | 288篇真实新闻全文；train228/dev30/test30；转换token可作公开预处理，但annotations/relations是目标 | 6245事件、13800参数；另3669情感标注不并入本轮事件任务，5事件type为空 |
| 实读训练例aal00：shares rise 4.76 % to $ 47.08，时间at the close of business on Apr 9 | SecurityValue_Increase规则 | 原全文及触发词rise[138:142]附近上下文 | Increase_SecurityValue；Security=shares，IncreaseAmount=4.76 %，Price=$ 47.08，TIME对应原时间文字 |
| 实读test开发检查例aapl15：Apple stock is preforming in line with my 2015 prediction | SecurityValue_Stable定义，参数跨度和事实属性规则 | 原文保留拼写preforming | Stable_SecurityValue，trigger[322:341]；Price参数是文字in line with my 2015 prediction，而不是杜撰数值价格 |

| 类python的DAG | 实际数值/状态 |
|---|---|
| `docs=scan(full_articles)` | 288篇；不能把不同转换格式重复计数 |
| `events=sem_map(docs, frozen_annotation_protocol)` | 官方转换gold6245事件，含5个缺类型需回查；字符跨度及参数切片全量通过 |
| `securities=filter(events,type=='SecurityValue')` | 原gold743提及；不等于743独立证券走势或743家公司 |
| `groupby(doc_id).collect(subtype,trigger,arguments)` | 重要语义节点的下游结构清单；尚未实际模型执行/评分 |

| 预期关键语义算子直接交给LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| aal00目标Increase与对应幅度/价格/时间；准确性未知 | 固定全文sem_map、规范检索、参数跨度验证和类别一致性检查；允许共享缓存 | 同一目标，未预设优势 | ==查SecurityValue与FinancialReport边界；定位触发词和角色；检查确定性/否定；检查完整上下文==→结构化事件 | 协议索引→触发检测→类型/参数判断→事实属性→跨度校验→聚合；未从轨迹学习或冻结 |

事件属性的polarity在当前表示中涉及肯定/否定，与投资情感positive不是同一概念；不将asserted简单解读为新闻真实或事件已经发生。原始XMI事件/论元关系已开始读取，尚未完成与全部转换记录的对照。默认任务应只给text及允许的公共预处理，不能直接把JSON整行输入模型。69页还包含工作流与改进计划，不声称每页均必需或已经证明长上下文成本。

许可明确人工标注/原规范CC BY4.0，软件Apache2.0，新闻原文仍归原权利人。本轮仅本地核验，没有发布授权扩张。新工程测试0；无模型、prompt、种子、推理预算、缓存或独立确认配置，无Agent优势/轨迹提取/成本结论。
