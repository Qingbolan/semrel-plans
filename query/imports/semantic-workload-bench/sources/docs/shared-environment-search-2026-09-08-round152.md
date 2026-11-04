# 第152轮：Softcite指南泄漏、文本span及有类型关系审计

仍8/15，不升级Softcite。本轮不重复下载151的原论文/完整仓库；延用commit4aaf7b281f0aecf6039edb30813dca89cf54b3bd。上一轮原生全库、holdout引用核验有进展。本轮将“指针能解析”进一步推进为“指针语义类型是否有效”，并验证公开文本与private span分离。

来源与下载哈希见[151](shared-environment-search-2026-09-08-round151.md)及[作者仓库](https://github.com/softcite/softcite_dataset_v2)。本轮可重跑audit.py及audit.json/private-spans.json/example-text-audit.json/scope.json/typed-relations.json/typed-link-counterexample.xml在artifact/evidence/shared-environment-audit-20260908-v152。private-spans.json含gold，仅供构造审计，不是运行器资源；尚未创建正式public/private快照。

## 本次实测

1. 扫指南中的原document ID、PMC与DOI，命中holdout4篇：c6676625dc、d984c41c4d、a4888e8278、a4367c2269，保守排除整篇。指南25个code fence中20个去标签后至少60字符的样例全文，经空白规范化匹配，命中2篇，均已包含在上述4篇。不能排除省略/改写/截断示例及近重复，所以这不是无污染证明。
2. 留989篇35717段27021765字符；513段有标注、1529实体（949software、283version、250publisher、41url、6language）。逐段递归构造原文本和实体偏移，文本与itertext逐字符一致，1529实体全部substring一致。仅证明TEI文本与原生标签正确投影，不证明原PDF/OCR准确或全部章节覆盖。
3. 保留软件类型745standalone、180environment、14implicit、10component。实际software带corresp17条：16指向software，1指向publisher；因此不能称17条都为合法依赖边。其余属性边282version→software、249publisher→software、40url→software、6language→software，另1version→publisher；共595条引用token。
4. 关键反例d8bf6fa9c8：原TEI将DiceKriging-package标software/component，却corresp指向type=publisher的R Development Core Team；2009标version也指向publisher。目标ID名字含software-10不等于目标type=software。这两条违背期望软件依赖/属性目标类型，不能直接当正确依赖gold，也不能因名字R就自动修成R环境。原文及属性完整保存。151的“602指针解析成功”仍成立，但不足以证明类型正确，本轮收窄了结论。
5. 指南3966空白词，其中code fence857、其余3109；后者仍含例子/格式说明，不全部是不可省略语义规则。没有证据表明需要整个规范反复推理，也未声称Agent优于E-only编译。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 不足 |
| --- | --- | --- | --- | --- |
| 从公开文章构造软件及属性清单 | 排除已知指南示例后989篇TEI纯文本 | 同仓库规则3966词；算法/软件、语言/环境、隐式代码边界 | 35717原段落供所有方法，不能先选513个gold段 | 1529实体已验证span投影；实体正确性和原文来源仍待确认 |
| 提取组件—环境依赖 | proCIs/R段落仍保留 | 指南要求component指向environment软件实体 | 源词/上下文保持，关系只在private | proCIs→R例有有效类型；DiceKriging→publisher为未解决反例 |
| 检索依赖R的研究清单 | 上游实体与有类型边 | 冻结“明确依赖”的范围及去重口径 | 需跨段关联时双方同样可读整文 | 不将R Development Core Team误当R软件；未构造全量派生查询gold |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `holdout.exclude(known_guide_documents).map(strip_annotation)` | 993→989篇；文本投影0失败 | gold文档排除属于开发构造；当前已观察，不是独立确认 |
| `texts.sem_map(extract_software_graph,E).explode()` | 目标1529实体、949software；段落35717 | 不用private span先裁剪；无标注段要保留 |
| `edges.filter(source_is_component_or_implicit).validate(target_is_software)` | 17software指针仅16目标type=software；其中component/implicit需分别定义 | 类型验证仍不等于全部16条语义正确。当前另1version指向publisher |
| `software_graph.groupby(environment).collect(article)` | proCIs→R样例贡献1来源 | DiceKriging边未经修订确认不能进入可信R依赖聚合 |

以下均未执行模型，只写目标/预期操作，异常不人为改gold。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| proCIs为component、R为environment，连接proCIs→R；未测实际输出 | 同指南固定全文语义抽取，绑定类型后连接，确定性检验目标类型 | 相同目标，无质量优势结论 | ==确认软件依赖规则与R在上下文的角色==→生成实体/边→相同类型校验 | `MentionExtractor -> TypedLinker -> InventoryAggregator`；保留输入输出证据与ABSTAIN |
| DiceKriging反例不能以当前有问题gold评价语义正确率 | 可按同规范生成输出，但评价侧须先解决该源标注冲突；不能用原错误边惩罚正确预测 | 同样无法凭模型共识建立独立gold | ==读取同一规则，区分发布组织与运行环境==→输出证据或未决；不得借private反例作训练特例 | 输出实体类型和边端点契约；校验错误是源问题，不冒充Agent发现后的正确答案 |

## 结论与下一行动

文本/偏移构造已闭合到989篇、1529实体，有类型关系也定位到具体缺口；未创建算子或推理实验。Softcite可保留为开发抽取候选，但严格“复杂共享E+可信关系gold”尚不足，仍不计第9个。下轮转新的长规范来源，不为凑数量只删一个错误后宣称整体有效。原论文与完整仓库已下载，用户三表持续补证，无模型/种子/费用/运行预算/测试套件/快照/正式评分/commit。人工示例观察导致开发暴露，需独立确认来源。
