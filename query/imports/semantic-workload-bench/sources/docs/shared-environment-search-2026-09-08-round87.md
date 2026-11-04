# Increment87 — IPF短图示确认泄漏：必须按事件例子审计

7/15不变。本轮发现明确的当前gold进入共享指南的证据，未构造评测快照。继续使用round85已下载的[完整作者仓库](https://github.com/ezcatdb/prism_IPFdata)及[40页原指南](https://ezcatdb.github.io/prism_IPFdata/AnnotationGuideline_IPFmechanism.pdf)，来源hash不变。

将OCR文本中的类型/角色标签和数字作为图示覆盖噪声移除后，采用6词且至少35字符匹配，150摘要中36篇出现候选命中。标签库存由当前源标签类型/角色名称提取，仅作开发诊断，不是实例答案输入，也不是已经冻结的确认集划分规则。命中包括idiopathic pulmonary fibrosis等常见表述，不能把36篇全部称为答案泄漏。

一条已确认的实例：指南PDF第30页例102，Cellular_process“Cellular crosstalk between epithelial cells and fibroblasts”，给出两个Participant。原生PMID28986417的E33正是Cellular_process:T29 Participant:T48 Participant2:T39；T29=cellular crosstalk[272:290]、T48=epithelial cells[299:315]、T39=fibroblasts[320:331]。因此该文档不能作为持有此指南时的未暴露确认案例。图示不仅共享词汇，确实给出目标事件类型和角色答案。

这说明round86的12词无匹配只能证明那个窄检测没有命中；不能证明不存在指南泄漏。图示通常只有几词且被角色标签切断，OCR必须结合视觉和结构比较。原PDF第30页已视觉查看，原始ann也已逐项读取。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold/当前边界 |
|---|---|---|---|---|
| IPF机制事件图批量抽取 | 原始150摘要 | 40页协议和图示 | 必要上下文；不带gold规范化/事件图 | 4899事件；至少28986417已因指南成为开发暴露 |
| 否定/推测事件清单 | 同全文及冻结后允许的事件库存 | Cue作用域与属性规则 | 不公开目标Cue链接 | 93否定590推测原始属性；具体未暴露批次尚未确定 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `abstracts.sem_map(event_graph,E).explode().project(type,participants)` | 原始150→4899事件 | E33的Cellular_process及两Participant由指南直接给出，不能据正确恢复声称推理迁移 |
| `events.sem_map(modifications,E).filter(Speculated)` | 原始590条推测属性 | 确认集尚未冻结，不提供伪造的新batch计数 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| E33目标是Cellular_process/两个Participant；有指南时可直接得到答案，实际未测 | 固定检索命中同一示例即可，不能把此类成功解释为复杂推理收益 | 同样可能直接读取答案，未测 | ==读取例102并对照原文==→复现示例结构；这是已暴露案例 | 可以形成schema或示例缓存，但不能作为独立迁移成果 |
| 对未来排除已暴露源后的病例恢复事件属性，结果未知 | 完整必要规则与固定程序/检索/编译对照 | 同信息目标，未知优势 | ==核对适用类型及作用域规则==→抽取→输出 | `rule_index→event_graph→modification→validation`；尚未产生或验证 |

另外明确三个新的短片段线索：PMID29363258的damaged mitochondria、29616048的LIGHT promoted cell cycle等与指南图示文字重叠，但本轮未逐条完成目标结构对等，保留为候选。不删除原始文档、不拼接异常N行、不按gold修正Theme。下一步可以仅把确认暴露记录分配到历史/开发，并在所有方法同样提供这些历史材料；独立确认仍需源实体隔离，不能把这种暴露抹掉。

脚本short_overlap.py、short-overlap.json、confirmed-example.json位于artifact/evidence/shared-environment-audit-20260908-v87。无模型、无能力结论、无新增合格湖。原有许可、完整规则范围及配置不一致问题仍待处理。
