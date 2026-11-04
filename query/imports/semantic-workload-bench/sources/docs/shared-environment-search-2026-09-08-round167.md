# 增量167：UCCA图结构、划分和官方评分契约

复用166原论文/两完整repo，不重复计湖，仍8/15。新增完整[官方ucca工具仓库](https://github.com/huji-nlp/ucca)commit `31e381f2b2693e82c8402b09a6d28f97d595a1eb`、126个文件。原件data/shared-environment-audit-20260908-v167/ucca-repo；全部哈希与标准库审计脚本artifact/evidence/shared-environment-audit-20260908-v167。下载最初暂置artifact，结束后移入本次ignored data，仅保留收据，无覆盖既有文件。

## 本次实查

对367个原始图做Kahn拓扑排序、节点ID唯一性和非remote主父计数：0环、0重复ID、0多主父节点。所有边引用已在166通过。24122个节点直接有P或S孩子，可定义为一个待审计Scene投影，但不是已经核验的24122个独立真实事件。

remote边细分：A9765、C221、D238、T50、P228、S86、R52、G15、E7、H5，总10667。因此共享参与者任务应针对A9765，不能把全部remote当参与者。是否可将当前图结构显式给定需另设任务；端到端抽取不应读gold结构。

官方SemEval train296段/22文章，dev38段/4文章，test33段/3文章。train/dev共享metadata中Angelina Jolie与Maria Carey两个来源；test与二者无文章交集。文章名是源字段，没有纠正拼写。本轮未重分配数据，也未把3文章的test称独立充分确认。

规范全文与原token串做小写ASCII词序列的连续8词重合筛查，0命中。**这是保守词面探针，不是示例泄漏排除**：PDF包含插入标签、图示、短例和改写，因此不能据此断言无重叠。未做逐页图示比对。

## 官方评分源码的含义

`ucca/evaluation.py`与`ucca/constructions.py`表明它按节点覆盖的terminal位置集合（yield）对齐，并非按原node ID对齐。标点被排除；remote、implicit分别有默认construction；implicit使用父节点覆盖位置。多个节点覆盖相同yield时，不等于逐节点一对一完整图匹配。weak_labeled模式把P/S等类别对视为等价，所以需要区分Process/State的任务不能用该模式宣称类别准确。

本轮只读源码，没有安装spaCy2.3.5旧依赖或执行官方scorer，未证明当前解释器兼容。源码GPLv3，数据CC-BY-SA3.0分别保留。正式图评分和下游Scene表评分仍需明确契约及实际运行。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 逐段抽取UCCA语义图，再生成Scene/Participant表 | 367段来自27文章 | 37页随数据v2规范 | 固定token上游；文章分组作构造隔离 | 原图；24122个带P/S孩子节点仅候选投影 |
| 恢复并列场景中共享参与者 | 完整passage上下文 | remote规范 | 预测场景图，或独立契约明确给定上游结构 | 9765个A/remote目标，不是全部10667remote |
| 具体passage20第二Scene共享Pitt | 166例子原文与图 | 并列、省略、参与者规则 | 第二Scene到首Scene主语的remote A连接 | 原1.11→1.3仅用于展示，算子不能写死ID |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `scan(passages).sem_map(parse_graph,E)` | 367段、27源文章 | 不能将官方train/dev当源隔离 |
| `graphs.project(scene_participant_edges)` | remote A9765；带P/S孩子节点24122 | 边数/节点数不是独立文章/事件总量 |
| `validate_dag_and_primary_parent()` | 0环/重复ID/多主父 | 工程有效性，不证明语义标签正确 |
| `score_yields(labeled=True)` | 默认remote与implicit分开 | 尚未实际执行；Process/State不用weak_labeled替代 |

以下均为未执行方法预期，所有方法允许相同规范、工具和缓存。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 保留passage20共享参与者，实测未知 | 固定语义解析→共享参与者解析→yield投影 | 相同目标 | ==核对remote适用范围与省略主语的文本依据==→输出图 | `SceneDetector→ParticipantResolver→RemoteLinks→YieldProjection` |
| 输出完整规范图并派生Scene表 | 同资源E-only编译、固定程序与Coding Agent可用 | 同样目标，不预言优势 | ==核对implicit/remote及静态/动态类别==→图校验→聚合 | `RuleSet→GraphDecoder→Validator→SceneTable`；不能用弱标签评分掩盖类别差异 |

本轮补齐原图结构和评分范围证据；未解决完整示例审计、规范必要性及下游投影/官方评分运行，暂不升级名单。无模型/prompt/训练/种子/token费用预算/推理并发缓存/测试套件/正式快照/score/commit。
