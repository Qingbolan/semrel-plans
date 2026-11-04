# Policy Reasoning Traces / GDPR — Reject（当前发布任务）

[论文](https://arxiv.org/abs/2509.23291)与[完整官方仓库](https://github.com/imperialite/policy-reasoning-traces)已下载，commit `3ec1029bebb6e56d8f860e3f80a167efe07e9cdb`，27文件。见[精确来源/哈希](../artifact/evidence/shared-environment-strict-prt/source.json)。未执行作者脚本，未生成或读取模型私人思维链作为本次执行轨迹。

| 准入项 | 实际观察 | 边界 |
|---|---|---|
| N与gold | train764：176COMPLIANT/588NONCOMPLIANT；test326：75/251 | 1090行实数成立；独立案件/近重复尚未审计 |
| E | gdpr.txt 6983词，按Article组织的概述式文本 | 不是完整GDPR及全部国内法律/判例 |
| A/G | test row1 Facebook投诉因个人授权缺失不受理，标COMPLIANT；处理活动仍调查中 | 程序结果不能自动当实体合规gold |
| C | 确定性20条完整document/reasoning本地阅读 | 20条原判决闭合为0；逐项缺口已写JSON |
| 输入泄漏 | sample15、16的document明示unlawful/infringements等结论 | 必须单独处理，不以分数高低证明环境价值 |
| 训练完整性 | train第一条document为Canterbury；reasoning又拼入Snowdonia另一请求 | 存在记录对齐疑点，未篡改源gold |
| D/E/H | PRT多示例ICL/SFT是相关方法；同资源强固定不足和语义家族K未证明；无LICENSE文件 | 不当作单轨迹自动算子结果；许可未闭合 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 判断每个GDPR case的COMPLIANT/NONCOMPLIANT（原任务） | test326份摘要，train764可作为历史监督，但需隔离 | gdpr.txt 6983词；成员国法律与判例缺失 | verdict/reasoning/policy_clauses为私有gold；relevant_cases的选择来源需另审 |
| 类python的DAG | `scan(test)`，326行 | `sem_map(case, policy, permitted_history)` | `compare_private_verdict`；先冻结判断主体/程序与实体语义 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| Facebook例原gold COMPLIANT；实际LOTUS预测未知，不能认定这一gold表示实体合规 | 固定sem_map读取案例+同E，按既定任务输出 | 实际预测未知；若要求实体合规，现有事实不能闭合 | ==区分受理资格、主管机关、实体处理行为及仍在调查的事项==；识别需国内法的部分 | `identify_subject -> procedural_status -> applicable_law -> decision_or_unknown`；提出结构不是已提取产物 |

| 20例核验 | 本次内容 | 不宣称 |
|---|---|---|
| 抽样 | test行按SHA256('prt-gdpr20-v1'+NUL+十进制rowindex)排序取20，不重采样 | 不是独立确认集，已开发暴露 |
| 可核验例 | OpenX监管权限；PCR阴性结果依奥地利条例；Facebook程序不受理；挪威邮件案例输入含判定 | 不用同一病例的多种争点扩大N或K |
| 原源追索 | GDPRhub针对两个个案搜索未定位匹配原决定 | 不把搜索失败证明原决定不存在 |

[20条完整本地样本](../artifact/evidence/shared-environment-strict-prt/sample20.json)、[20条逐项审计](../artifact/evidence/shared-environment-strict-prt/sample20-review.json)、[数据实数](../artifact/evidence/shared-environment-strict-prt/data-audit.json)。本次发现使其不能按当前任务计Strong；修复任务与来源后需新版本，而非改gold掩盖问题。
