# 增量199：FrameNet目标多解、二层角色与隐式论元

复用198完整发布包和原论文，无新下载。本轮可复现audit.py/json在artifact/evidence/shared-environment-audit-20260908-v199。

28171 MANUAL带frameID集合实际对应28143个(文档,句子,Target位置序列)键：28键有两份标注，其中8键的frameID不同，不能盲目去重成单值分类。没有缺Target的集合。37个MANUAL无frameID的集合例子是带cxnID/cxnName的构式标注（如Ones_very_eyes），不是37个坏框架；当前框架任务排除它们需明确任务范围。

FE rank1为58461标签，rank2还有740标签，rank3为0。手册§3.2.1/§3.2.5说明次层用于frame element conflation等语义：一个成分可以表达不止一个角色，例如报复对象同时包含受害者与伤害。它们不是重复annotation或仅语法装饰。若目标是完整角色抽取，198的rank1统计不是完整gold；可以明确研究rank1，但不能称完成所有角色。

无位置标签在rank1中DNI3452、INI3229、CNI1573、INC18；rank2另DNI11、INI4、CNI1。DNI/INI/CNI分别关联特定可恢复、非特定、构式许可的省略，属于语义输出；不等于系统执行ABSTAIN。手册另有§3.2.4 Frame element incorporation，但本轮尚未核INC代码的格式定义，不据缩写自行填映射。

对全部10147句与整本手册做Unicode字母分词、小写、连续8词精确匹配，重叠0句。此为表面暴露审计，不证明无语义例句重叠或训练污染；frame定义例句、LU exemplars尚未审计。归一化全文句子有276组重复，也包含短句/标题；尚未建立跨文档分组隔离。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 给定目标→框架→按框架汇总 | 28143唯一目标位置键 | 同版1221框架/LU定义 | 配套129页规范 | 28多标注键，其中8不同框架；单值输出契约未冻结 |
| 给定目标→完整角色→参与者清单 | 原句和公开目标位置 | 角色定义、次层/合并规则 | 手册§3.2.5与省略规则 | rank1 58461加rank2 740；不能丢次层后称全量 |
| 隐式论元分类→缺省信息统计 | 原句上下文 | DNI/INI/CNI规则，INC格式待核 | 公开schema和词典 | rank1 8272，rank2 16无位置标签；不是执行失败 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(targets).sem_map(frame,E).groupby(frame).count()` | 28143键，不是28171互不重叠输入 | 多解8键需预先定义集合gold或其他来源合理规则 |
| `targets.sem_map(frame,E).sem_map(all_FE_layers,E).explode()` | 59201 FE标签（两rank） | rank本身应保留或明确投影，不暗删740标签 |
| `FE_outputs.groupby(instantiation).count()` | rank1 DNI3452/INI3229/CNI1573/INC18 | INC映射未证；未知代码不能默填常量 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 198例Giving及Donor/Recipient，实际未知 | 同词典固定候选检索、消歧、全部角色层抽取 | 同目标，实际未知 | ==查框架候选与次层角色合并规范== → 框架/角色集合 | `FrameResolver + LayeredRoleExtractor` |
| 隐式论元输出语义类型，实际未知 | 同规范固定分类和公开schema检查 | 同目标，实际未知 | ==查省略是否可恢复、是否构式许可== → 类型 | `NullInstantiationClassifier`，执行ABSTAIN独立字段 |

未运行模型或性能实验。==为可观察查阅；固定程序、CodingAgent和E-only编译共享所有资源。仍11/15，FrameNet接近可构造但尚需重复目标、词典例句泄漏、完整层级和INC码核验，不能把结构通过扩写为科学确认。
