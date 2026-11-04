# Increment80 — UKP 任务范围、泄漏和公开构造

仍为6/15；本轮完成说服性任务检查视图，未宣布新的环境有效性结论。上一轮为实质进展；本轮继续消费已下载的完整原论文、仓库和官方发布，不重复下载。

来源：[原论文](https://aclanthology.org/J17-1004.pdf)、[官方发布](https://tudatalib.ulb.tu-darmstadt.de/items/d4a7ac0c-e7a8-466a-855a-917e42a24342)、[作者仓库](https://github.com/UKPLab/emnlp2015-ih-ig)。完整hash与下载收据见v79。论文§4.3说服性gold为多数票；§4.4.4结构gold为多数票、冲突讨论解决，不代表不存在主观分歧。

本次纠正了两处容易造成虚假任务的表示问题：

- 990说服性文件名含P1/P2和类型，不能公开；以WebArgumentMetadata.origId匹配后与340结构文档重叠279，不能相加声称1330独立文档。初次文件名交集0是错误审计，已修正脚本及收据。
- 365个Claim中170个长度0，properties明确implicit=true，不能评分为普通span。869关系全部是538 Premise→Claim、224 Backing→Claim、68 Rebuttal→Claim、26 Refutation→Claim、13 Claim→Claim。论文明确大部分关系由组件功能隐含，不能把每条边当独立推理能力或独立lake。

全340原文及组件的(type,begin,end,properties)与EMNLP仓库版本逐一一致。此对等不覆盖关系和全部自动特征。98通用ArgumentComponent均appealToEmotion=true；论文因pathos低一致性未将其纳入主实验，因此不能直接并入五类结构主任务。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | private gold |
|---|---|---|---|---|
| 依本协议筛选具有与主题相关的说服意图的评论/帖子 | 893个匿名公开JSON，完整源正文 | 源title与topic；不带文件名标签、投票、gold或annotator metadata | protocol.txt：PDF第3页起至第23页§4前，11477词；只保留说服性相关章节与历史示例 | 456真、437假；公开示例排97篇 |
| 抽取扩展Toulmin组件 | 原始340篇，文本/ID公开示例排46篇后294篇 | §4六页核心约3078词，§5具体争议案例 | 主题、全文；隐式Claim需单独输出语义 | 剩477 Premise、198 Backing、315 Claim、59 Rebuttal、22 Refutation；71pathos另列；766关系。此任务本轮未构造 |

示例排除采用手册/原论文明确#ID引用，或连续12个词且至少65字符匹配，仅是可复现的文本污染审计，不证明无近似/图片示例污染。说服性使用源ID修正后是97排除/893保留，初次文件名审计的86/904作废。两个任务仍应按共同源网页/作者分组，未完成独立确认划分。

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `scan(public_docs).sem_filter(persuasive_under_protocol).project(record_id).count()` | 893完整源文档→893次Boolean/ABSTAIN输出 | 真456，假437；ABSTAIN不能删除后重算分母 |
| `scan(docs).sem_map(components_with_explicit_or_implicit_claim).explode().groupby(type).count()` | 294篇剩余文档；1071五类组件 | Backing198；315Claim中显隐需保留，不能用零长度span骗取匹配 |

具体源1025推荐读者查Paula Rothermel的居家教育研究，gold=false；源1220主张公立学校不应开展宗教实践，gold=true。这是协议中的说服意图判断，不是内容真伪、道德判断或论证说服力排名。源1025可能被普通“出现理由/研究引用”启发式误收，但尚未运行任何模型，不能宣称LOTUS会犯此错。公开输入含原始topic/title，未把gold理由补入。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标1025=false、1220=true；实际结果未知 | 完整必要正文、标题、主题和同一E进入固定sem_filter；也允许固定检索/共享缓存基线 | 同一目标；优势与成本未知 | ==检索§3说服意图、对其他评论的回应及叙事判准==→读取全文→判定→输出record_id及状态 | `load_rules→identify_topic_stance_and_intent→apply_context_rules→emit_boolean_or_abstain`；从真实单轨迹提取仍未执行 |
| 目标区分显式/隐式Claim并保持Backing数量；未实测 | 固定sem_map输出显式span或独立implicit字段，按原协议校验 | 同一gold契约 | ==核对§4.2.2隐式Claim、§4.3.1个别经历规则==→整体解释→输出结构 | `detect_claim_mode→extract_explicit_spans→represent_implicit_claim→classify_components`；不把原始gold rephrasedContent当公开资源 |

§4.3.1准确含义：个别经历即便是唯一理由仍标Backing，这是对一致标注的补充说明；不能理解成“唯一理由就改成Premise”。暂不预言需要Agent动态探索；完整E固定编译器、固定检索和Coding Agent均为必要强对照。

实际构造：`data/shared-environment-audit-20260908-v80/inspection-persuasion-v1`。公开字段仅record_id/text/title/topic，加task.json/protocol.txt；private持gold/source-map/exclusions。独立验证898资产精确集合、bytes/hash、893记录allowlist/原始正文主题标题和gold逐条对等，PASS。仅本地结构化检查视图，没有模型执行、评分器、环境消融、实际沙箱或确认划分；数据许可沿用v79研究用途/限制再分发。

脚本和收据：`artifact/evidence/shared-environment-audit-20260908-v80/`。后续先检查PDF图示/近似重复与源语境，再决定是否具备第7个构造资格；11477词大部分为争议案例，必须与短规则/E-only编译对照，不能把篇幅当必要推理成本证明。
