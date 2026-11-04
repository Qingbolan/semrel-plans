# 增量154：SitEnt跨格式一致、指南示例排除与多数票边界

沿用[153原论文/完整仓库下载与哈希](shared-environment-search-2026-09-08-round153.md)，不重复下载。仍8/15；本轮是实质来源核验，不是模型实验。

## 新证据

- 全367份`annotated_xmi`的sofaString与原raw_text逐字符一致。全部50009个SituationEntities的instanceid、begin/end、SE_Type与XML零差异。由此确认153的数量不是XML导出器偏移/标签丢失导致，未恢复论文40940范围。
- 全367份`gold_xmi`实含505118 Token、23663 Sentence及元数据，无SituationEntities语义标签。目录名称不能证明有gold，不能将其作为第二个独立人工标注来源。
- 将手册与片段按Unicode词字符规范化，筛≥65字符完整片段子串，命中2条、均为wiki_tennis。整篇排除后366文档49903片段，40701七类已决：STATE18307、EVENT9657、QUESTION1056、IMPERATIVE1046、GENERIC_SENTENCE7558、GENERALIZING_SENTENCE1461、REPORT1616。该筛选仅发现完整文本匹配，不排除省略/改写/短句/近重复；未声称完成无污染审计。
- 对每条已决SE标签核对三位标注员冒号分隔的原标签：除260 REPORT及48 SPEECH_ACT外均至少有两人直接支持。260 REPORT全部只有一人标REPORT，其余人给EVENT（具体组合在收据）；48 SPEECH_ACT在发布个人标签中没有两人直接支持。REPORT可与EVENT同现，可能存在更细子类优先约定，但本轮没有找到对应构造实现，不能当已证明的原因，也不自动改为EVENT。
- 不能以删除上述记录就证明全库有效；当前Gold范围和上位标签/优先级仍须明确，六类的直接支持也不是临床或事实真值证明。E必要性实验仍未做。

收据及可重跑全格式/示例审计：`artifact/evidence/shared-environment-audit-20260908-v154/audit.py`、`audit.json`、`parity-errors.json`、`example-matches.json`、`majority-audit.json`。最后一项含逐例人工标签，仅供构造审计；不可作为模型资源。多数票核对为本轮一次Python标准库命令，命令见会话工具收据，尚未独立封装scorer。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 生成同规范的片段类型索引 | 排除已知指南例文后的366真实文本 | 153已下载49页手册，相同字节与绑定版本 | 49903给定原片段与全文上下文 | 40701七类已决；余9202不自动当negative |
| 词汇体/习惯性分布 | 同批文本与给定切分 | 手册不同属性定义、coercion及例外 | 自动mainVerb/mainReferent不能冒充人工gold | 153字段计数不是排除后计数，本轮未重新冻结此视图 |
| 报道行为索引 | 原文段落及上下文 | REPORT与EVENT层次规范 | 不给当前个人标注或发布标签 | 全库260 REPORT单人明确支持，构造优先级未明，暂不确认此任务 |

| 类python的DAG | 具体数值 | 核验含义 |
| --- | --- | --- |
| `native_xml.join(xmi,on=instanceid).validate(text,offset,label)` | 50009，零标签/偏移差异；367完整原文一致 | 两种发布格式一致，不是两次独立标注 |
| `documents.exclude(guide_example_docs).explode(given_segments)` | 367→366文档；50009→49903片段 | 排除wiki_tennis整篇，开发构造选择，未创建正式快照 |
| `segments.sem_map(situation_type,E,context).filter(type=='EVENT')` | 当前已决视图目标9657 EVENT | 只评价已决范围；原文全部实际事件数量未知 |
| `private_labels.audit(annotator_support)` | 全库260 REPORT只有1个直接支持；48 SPEECH_ACT无2个直接支持 | 仅评估侧操作，绝不可放到被测公开DAG中 |

下表为未执行的设计目标，均允许同资源固定检索、缓存和批共享计划。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 153的未遭受袭击例应STATE，词汇体DYNAMIC；实际未测 | 固定多字段sem_map按同否定/特定指称规则分类，输出后固定filter | 相同目标，不声称更准 | ==查手册否定、泛指例外，结合全文判定指称==→类型输出→确定性聚合 | `ContextResolver→AspectClassifier→SECoercion→TypedResult`；需真实轨迹才可称提取产物 |
| REPORT例不能先预设模型错于发布gold | 固定程序同样可理解上下位类别；需先冻结评估语义 | 同样不能用模型共识裁决gold | ==读取公开层次规则并返回依据==，不访问三位当前标注员答案 | 类型层次校验与ABSTAIN；未证明“单人细类优先”不能固化此规则 |

本轮完成了跨格式核验和一个真实污染排除，并将“全是多数票gold”的说法收窄。未将SitEnt升级。下一步转新的独立长规范来源，同时保留其明确待决项：发布gold优先级、实验范围和指南样例/来源重叠。原来源完整下载已满足，但15个合格数据湖的总目标仍未完成。无模型/费用/训练/种子/推理预算/测试套件/正式评分/commit。
