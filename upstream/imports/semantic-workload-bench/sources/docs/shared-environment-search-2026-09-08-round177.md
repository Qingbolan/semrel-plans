# 增量177：Ru-RST规范与原生标签的版本差异

复用176原件，仍9/15。上一轮为有效进展；本轮解释文件数和多根结构，并发现当前指南与大量原生标签不一致，不能只修几份XML就升级为可行湖。

334份RS3均有同stem TXT，额外TXT是README，故335不是335篇正文。官网333与包334的差1仍未解决。README为CP1251编码（UTF-8严格解码失败后按CP1251成功）；开头自称1.1、2022年8月版本，但其正文和CC BY-NC-SA4.0许可句仍指1.0，不能不加说明地扩展为所有新增分区的明确许可。

指南开头明确只要求段落级树，短段可依语义合并到相邻树。因此331份可解析文件中的329份多根不自动构成错误。全量已解析节点ID无重复、父链无循环；176已发现的1个悬空parent仍保留。

按指南关系表（包括结构span）只计有parent的边，得到74967条边，排除所有无parent的relname属性。当前清单外标签共4346次：cause2381、evaluation1419、antithesis8、effect35、motivation1、interpretation2，涉及278篇。各分区受影响文档：sci.comp43/46、sci.ling50/50、news249/50、news123/79、blogs103/106。

指南已把Cause和Effect合为Cause-Effect，并对核/卫星的因果方向作出明确说明；把Interpretation/Evaluation合为一类，Antithesis并入Contrast。**名称归并未必保持原树的核/卫星或因果方向**，尤其原标签Cause与Effect的区分需要核对历史版本。不能把这些自动视为拼写别名直接改gold。motivation更不能无依据映射到purpose。

本轮机器收据在`artifact/evidence/shared-environment-audit-20260908-v177/audit.json`。图检查只验证实际读取的331份，3份XML失败没有被悄悄修复。现行规范表由本轮读取提取，尚未穷尽所有例外、例子暴露及历史规则。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 逐篇构建段落级RST森林 | 334正文/RS3文件配对 | 18页5190词现行规范 | 分区及2022包README | 331份可解析、74967有parent边；不强制全文单树 |
| 对sci.comp_1片段33识别因果关系与核/卫星 | 原文“因为故障和失效具有随机性……” | 当前Cause-Effect规范及历史Cause方向待核对 | 完整文档与EDU | 原标注33→145/cause；不能未经审计改名后称语义不变 |
| 抽取因果论述清单 | 上游预测森林 | 方向和关系类别冻结规则 | 文档ID | 4346清单外标签影响278篇，当前不能直接统一评分 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `pair_by_stem(txt, rs3).parse_forest()` | 334配对；331解析；0重复ID/循环 | 配对存在不等于全文与EDU逐字一致 |
| `edges = nodes.filter(parent_exists); audit(label in E.inventory)` | 74967边；4346清单外、278文档 | 有parent字段不代表parent合法；1悬空已单列 |
| `sem_map(rst_forest,E).project(causal_relations).groupby(doc)` | 目标必须保留因果方向 | 先冻结规范/gold版本，再运行模型；未执行 |

以下为未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 合法输出可为段落级森林；实际质量未知 | 同一规范上的固定检索与sem_map，再校验森林 | 相同目标，不能把多根判错来制造差距 | ==读取段落范围及短段合并约定，记录规则证据==→构图 | `ParagraphContext → AttachmentResolver → Forest` |
| 因果方向需符合冻结规范 | 固定核/卫星与类别映射；不能临时修gold | 同一约束 | ==检索因果定义和方向==→关系输出 | `RelationLabeler → NuclearityResolver → CausalProjection` |
| 版本差异由构造侧解决 | 基线只获得冻结的公开E | Agent也不得读当前private gold纠正 | ==构造阶段核对原始与现行规范==，不计作被测Agent能力 | 来源版本审计不是学得semantic operator |

下一步应查历史规范或作者发布的有依据迁移版本；没有依据前保留候选，不绕过方向问题。无下载/安装、LLM/模型prompt实验/训练/种子/token预算/推理并发缓存、正式快照/commit；0测试套件测试。原件未改。
