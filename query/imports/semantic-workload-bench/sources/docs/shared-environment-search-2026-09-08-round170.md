# 增量170：STREUSLE / SNACS 原件与任务核验

状态：新来源，原论文、完整作者仓库、114页规范与原生数据已取得；暂不加入合格清单，仍8/15。长标注指南的存在不证明长环境探索必要；本源明确参与了指南制定，示例暴露需要进一步处理。这里是批量语言关系标注，不是保险理赔审批。

## 原件和可复核证据

- [ACL2018原论文](https://aclanthology.org/P18-1018.pdf)：356367 bytes，SHA256 `9d65145f2e3a5dd9917f0b3986d332f3764b8ff52c3a7ed5cbc36b8ea0f5da70`。论文报告的是STREUSLE4.0的5455个标注单位，不能替代本次5.0数量。
- [完整作者仓库](https://github.com/nert-nlp/streusle)：commit `8ba61fe4f216e7967500a862554a4fff79d25f5d`。77个tracked文件与两份外部PDF均有逐文件bytes/SHA256收据。当前5.0以CoNLL-U为canonical；README明确4.5把SNACS更新至v2.6，后续有一致性修正与格式变更。
- [SNACS v2.6指南](https://arxiv.org/abs/1704.02134)：实际取得arXiv v8 PDF，114页、34662个空白分词，1888541 bytes，SHA256 `98d9724a16849c0907780916f6f7ed3ae6c5a62239bcea3335265162ea210c4d`。页数包括定义、说明、例子、参考等，不等同于每条判断必须读取的长度。
- 本地原件：`data/shared-environment-audit-20260908-v170/`；审计脚本/统计/完整下载哈希/指南重叠及样本：`artifact/evidence/shared-environment-audit-20260908-v170/{audit.py,audit.json,downloads.json,guide-overlap.json}`。

本次逐行统计：723篇评论、3814句、55588 tokens，5500个SNACS表达式；1849个表达式的scene role与lexical function不同。train/dev/test分别347/192/184篇、4553/462/485个SNACS表达式。按sent_id去掉末尾句号编号得到的review ID跨split交集为0；这不是作者、商家、近重复或训练污染隔离。

官方CoNLL-U→JSON转换与发布JSON的表达式、tokens和text逐项比较0差异，所有toknums引用有效。转换器会简化3处复杂MWE并输出UD与词汇类别差异警告；因此这是官方转换后JSON的一致性，不是所有原始MWE结构无损证明。本轮未运行官方psseval；源码区分goldid和autoid，并忽略第一gold supersense为`??`的单位。未来评分不能将这种忽略默认为全输入coverage。

README明确governor/object关系是启发式派生，不是独立人工gold；公开输入若给定人工target span，任务必须称target-given disambiguation。发布文件中的`ss/ss2`、编码答案的lextag/MISC、当前gold选出的上下文及标注副本都不能进入运行器。仅公开原文、token索引及显式批准的target spans；其他句法资源若使用需单独声明annotation-given条件。

标注与UD为CC BY-SA4.0；评论原文与PTB标签经Google/LDC许可随库重分发，不扩大为无条件商业使用许可。

## 三张任务表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| Q1：对每个给定介词/所有格表达式，按SNACS输出场景角色和词汇作用，生成评论关系表 | 723篇真实评论；给定5500个目标表达式的token位置 | 同一份114页SNACS v2.6指南及标签层级 | 可选完整评论上下文；不得挂载含答案JSON | 5500对`ss/ss2`；不是5500个独立评论 |
| Q1具体例：识别“My insurance company, Blue Cross/Blue Shield paid the fees and everything was fine.”中My的关系 | `reviews-003418-0003`，token 1，lemma=my | §4.8 SocialRel、§4.3 Gestalt、§5.3角色/作用限制、§6.1所有格 | 完整原句；公司名作为句内文本 | `p.SocialRel / p.Gestalt`；表示关系分析，不提供claim approval gold |
| Q2：从Q1结果筛选场景角色与词汇作用不同的表达式并汇总 | Q1预测关系表 | 固定比较与groupby规则 | review ID | 原始全量1849项；是Q1派生查询，不算新语义任务/新湖 |
| 待扩展：多词表达式识别及类型 | 原文与token位置；全量3019个strong MWE、705个weak MWE标注 | 需要另核验MWE及PARSEME规范；当前SNACS指南不能包办 | canonical与JSON的3处简化需显式契约 | 有原生标注，但本轮未完成规范绑定，不计可行任务 |

| 类python的DAG | 具体数值 / 输出 | 输入与计分边界 |
| --- | --- | --- |
| `scan(reviews).join(given_targets).sem_map(label_role_function, E).project(review_id, token_ids, role, function)` | 5500条原生目标；示例`(SocialRel, Gestalt)` | target-given任务；当前private标签只用于评分 |
| `relations.filter(role != function).groupby(review_id).count()` | 全量gold为1849条，按review输出清单及数量 | 固定派生操作，无第二种独立人工gold |
| `predictions.join(private_gold).score_pair_and_fields()` | 应分别报role、function、pair、coverage与下游清单P/R | 本轮仅原生计数/转换核验，未执行模型或正式评分 |

下表是待测试的机制预期，不是实际LOTUS/Agent输出；不预设任何一方失败或更准确。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标为`SocialRel / Gestalt`；实际预测未知 | `sem_map`读取原句、目标位置、同一指南；也允许固定检索有关章节，再结构化输出 | 相同目标；无实测优势 | ==检索稳定关系、所有格及role/function约束，保存章节证据==→输出标签对 | `TargetContext → GuidelineRetrieval → RoleFunctionLabeler → PairConstraintCheck → RelationRow` |
| 若role/function区分正确，本例进入差异清单 | 固定比较字段、投影ID、聚合 | 同一清单与计数目标 | ==开发时确认两个字段含义与目标粒度==→执行同一固定DAG | 共享规范索引与标签约束可缓存；语义判断仍需逐例处理 |
| E-only编译可能已经足够；需要作为对照 | 只从E生成类别定义/约束/检索程序，并在独立批次执行 | 单条真实Agent轨迹可提供检索路径与错误检查候选，但尚未提取 | ==轨迹记录实际使用的章节、工具参数和可观察输出==→冻结→后续批次 | 只有运行后才能声称学到operator；不能把本表手写结构称提取成果 |

## 为什么还不计入合格清单

论文§4–5明确：评论语料参与指南开发，疑难情况促使补充具体说明和例子。此次把指南与句子转换为小写ASCII单词，连续8词精确扫描命中3句、3篇评论：train的reviews-077298、reviews-388799，以及dev的reviews-229142。没有test精确命中不证明无短例、改写例或规则针对实例的暴露。

`my insurance`作为商品所有关系出现在指南，但它与样本的`my insurance company`不是同一指称，不能仅凭局部词组就断定gold冲突，也不能把样本当成独立于指南发展的确认例。

下一步应审计指南示例及规范约束对原生标签的一致性，冻结开发排除规则，再检验完整E对短定义/E-only编译的实际增益。只有这样才能区分“需要跨规则判断”与“普通条件分类加长文档包装”。本轮无LLM、无prompt/模型/种子/token预算/推理并发与缓存成本，无训练、无正式public/private快照、无commit；转换核验不是性能实验。
