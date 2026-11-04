# 增量186：CDCP真实评论有gold，但长E仍缺

本轮原件下载完成：[语料原论文](https://aclanthology.org/L18-1257.pdf)216510bytes；[官方完整发布包](https://facultystaff.richmond.edu/~jpark/data/cdcp_acl17.zip)5635976bytes、2928 ZIP成员CRC通过；README指向的[完整作者实验仓库](https://github.com/vene/marseille)commit `c86faf3d97fd9063a6fe0ee74b302f09250e36c5`、37 tracked files；[ICAIL2015论证模型原论文](https://facultystaff.richmond.edu/~jpark/papers/jpark_icail15.pdf)亦已下载。原件data/shared-environment-audit-20260908-v186，逐文件hash/统计在artifact/evidence/shared-environment-audit-20260908-v186。

## 核验与决定

731真实用户评论，train581/test150。原生4932命题：value2182/testimony1117/policy815/fact786/reference32；1172 reason支持、49 evidence支持，共1221。论文写4931命题，比本次文件统计少1，未静默改数。全部命题数量与offset配对、字符范围及关系源区间/目标下标检查通过；尚未验证重叠、环、近重复或论文修订差异。

这是评论论证分析，不是催收合法性判断或CFPB最终采纳决定。没有证据表明法律长文本是这些gold标签必要输入。完整包没有单独长标注手册；README指向2015论证模型，当前公开证据不足以通过长E门槛，仍11/15。

.txt是评论、.ann.json是人工gold；.txt.json及.pipe分别是CoreNLP3.6和PDTB-style parser2.0.2的自动输出，不冒充人工gold。作者实验类默认merge_consecutive_spans=True并把reason/evidence合并为links；这不是原生细分gold任务，复用时必须显式指定评分语义。

数据许可README为ODbL，单项内容DBCL；实验代码许可独立核验，不能用代码许可覆盖评论。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 每条评论识别命题类型和支持关系 | 731条真实债务催收评论 | 论证模型论文/定义；长共享规范未取得 | 原文URL映射可另行公开；自动句法仅资源 | 4932命题、1221支持关系 |
| 00194：该评论用什么理由支持监管建议？ | 三命题：法院与仲裁背景；认为仲裁不理想；建议CFPB要求诉讼渠道 | fact/value/policy与reason/evidence区分 | 原始396字符英文文本，保留全文上下文 | fact,value,policy；命题1→2为reason，0-based |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(comments).sem_map(propositions,E).sem_map(support,E).project(graph)` | 731评论→4932命题、1221支持为gold规模 | 预测未知；这不是法规合规结果 |
| `graphs.filter(target_type=policy).project(reason_span,policy_span)` | 00194源[1,1]支持目标2 | 源可为多个命题区间，不能自动拆成独立单边 |
| `graphs.aggregate(reason_count,evidence_count)` | 全库1172/49 | 原模型默认合并links会失去该区分 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 00194目标fact/value/policy及1→2 reason；实际未知 | 同原文和模型定义固定sem_map；可用同样句法资源 | 同一目标，无预设优势 | ==查命题定义及理由/证据边界== → 输出跨度/源区间/目标 → 引用检查 | `ArgumentParser(type_rules, source_range, support_type, validator)` |
| 目标汇总1172 reason/49 evidence；实际未知 | 原始标签契约下普通groupby | 相同结果目标 | ==核对默认merge会改变标签粒度== → 固定聚合 | 原生区间与支持类型保留；纯格式转换不属于学习证明 |

所有预期未执行。固定程序、E-only编译和Coding Agent同资源比较仍必要。==只指可观察规范探索==。无模型/正式快照/单轨迹实验，不计入15湖。
