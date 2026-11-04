# 增量171：SNACS约束、官方评分和开发范围

本轮复用170的完整作者仓库、原论文及114页v2.6指南，不重复计算来源。新增证据足以登记为第9个 `SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT`：720篇真实评论、5476个显式给定目标、规范绑定及人工标签。**这是可构造的开发任务，不是长E必要性、单轨迹方法有效性或独立确认通过。15个完整科学验证任务的目标仍未完成。**

来源与完整下载哈希见[170轮](shared-environment-search-2026-09-08-round170.md)。本轮原始源文件未改；预测探针副本在`data/shared-environment-audit-20260908-v171/`，审计脚本、收据和明确开发名单在`artifact/evidence/shared-environment-audit-20260908-v171/`。

## 本次验证

1. 使用官方`supersenses.py`的v2.6层级，逐个核验5500标签对；清单外标签0，违反§5.1–5.2的Participant/Configuration/Content使用0，违反§5.3角色专用标签作为function的使用0。此检查仅覆盖这些离散限制，不涵盖语境解释或全部构式规范。
2. 官方`psseval.py --json`对train/dev/test分别执行goldid自比，3次exit0；role/function/pair的计数4553/462/485全部匹配。没有安装依赖。自比不计作模型成绩。源码MWP分组过滤条件是`lexcat != PP`，与“multiword adpositions only”注释有疑点，本轮只使用All指标，不把MWP指标当已核验语义。
3. 源中另有47个`??`表达式，官方评分忽略它们。本任务明确只给定5500个拥有确定SNACS标签的目标；不能称覆盖全部介词或端到端目标发现。若扩展目标发现，需要显式UNKNOWN与coverage契约。
4. 依据170的三篇精确示例命中排除整篇：reviews-077298、reviews-229142、reviews-388799。固定开发名单720篇、5476个目标，其中1837对role/function不同。排除未修改原gold；名单不是独立确认集，指南短例/改写及制定过程的影响仍可能存在。
5. 单例受控错误探针：在完整train预测副本中，仅把reviews-003418-0003的My从`SocialRel/Gestalt`改为`SocialRel/SocialRel`。官方role仍4553/4553，function和pair变4552/4553，pair accuracy约0.999780。该错误会令本例从role≠function清单漏掉1项。是人为错误探针，不是LOTUS实测错误。

## 用户要求的三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 根据SNACS批量生成语义关系表 | 720篇真实评论，5476个给定token目标；选择名单已登记 | 同一114页SNACS v2.6指南及层级 | 原文、token位置、可选完整评论上下文 | 5476个role/function标签对；输入禁止含ss/ss2/lextag等答案编码 |
| 具体“My insurance company…”的My是什么关系？ | reviews-003418-0003 token1 | §4.8稳定社会关系、§4.3 Gestalt、§5.3及§6.1所有格 | 保险公司是句内实体，不是外部保单 | `SocialRel / Gestalt`；无理赔批准标签 |
| 汇总场景角色与词汇作用不同的表达式 | 上游预测关系表 | 固定字段比较规则 | review ID分组 | 开发范围1837项；同一人工标注的派生查询，不算额外湖/独立任务 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(reviews).join(given_targets).sem_map(role_function, E).project(id, role, function)` | 720篇→5476个标签对 | target-given；无当前gold读取，尚未运行模型 |
| `relation_rows.filter(role != function).groupby(review_id).count()` | 开发gold清单1837项 | 错误探针漏掉示例1项；全量预测清单未运行 |
| `private_score(predictions, gold)` | 三个原split自比4553/462/485全匹配 | 只证明官方评分可执行；全量5500与开发5476分开报告 |

以下是未执行的方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标`SocialRel/Gestalt`；不能预言它会混淆 | 完整输入上的sem_map；固定检索有关定义/构式再输出两字段也允许 | 相同正确目标，无优势实测 | ==按关系与构式检索定义，检查SocialRel只能做role，保存引用==→输出 | `Context → RuleRetrieval → PairLabeler → ConstraintCheck → Row` |
| 差异清单包含该例 | 字段不等比较、ID投影、groupby；无需额外LLM | 同样包含该例 | ==首次确认两字段语义==→执行相同DAG | 语义标注后接固定派生算子；不需要为聚合制造Agent步骤 |
| E-only编译也可能达到相同质量 | 从完整E生成类别索引、例子检索与约束程序；成本包含构造 | 单轨迹提取是否额外改善仍待测 | ==记录一次真实任务中的公开检索/判断输出==→提取→冻结→独立后续批次 | 可缓存规范索引、合法标签约束与检索计划；当前结构为设计，非已学产物 |

## 可行性与未完成项

它满足开发构造所需的真实来源、同一复杂规范、大批给定目标和人工gold，且没有在本次检查中发现相应规范冲突，因此按现有8个来源同一等级登记。指南设计参与和示例暴露限制科学确认，不把8词排除当彻底去污染。只给标签名称/短定义是否已足够、完整指南是否改善下游清单、单轨迹是否优于E-only编译，均须实测。多词表达式任务仍待自己的规范与转换边界核验，未计第二个独立任务。

本轮未构造正式public/private快照、未执行LOTUS或Agent、未提取operator、无训练/模型/prompt/种子/token预算/推理并发缓存成本，无commit。3次官方自比与1次错误探针是工程诊断，非测试套件或准确率实验。
