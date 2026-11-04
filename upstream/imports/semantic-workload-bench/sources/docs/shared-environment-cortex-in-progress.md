# CORTEX — 未确认，不计入Strong或已判定35项

[原论文](https://arxiv.org/abs/2510.00311)已下载并阅读§3.2、§4.1及结果表；[下载哈希](../artifact/evidence/shared-environment-strict-cortex/source.json)。尚未定位官方仓库/数据入口，无法满足用户要求的仓库与数据下载。精确标题+github/code搜索和第一作者62个公开仓库名称检查未定位匹配；这不证明数据不存在，也未联系作者。

| 条件 | 论文主张 | 本次可核验边界 |
|---|---|---|
| A | Actionable/Non-actionable及四子类；输出rationale与observables | 任务形态明确，Undetermined被归入Non-actionable；需单列未知语义 |
| B/F | 生产SOC数千轨迹、十余场景，日志/用户/资产/查询工具 | N与冻结共享E规模未知；每记录工具结果不自动是独立可探索E |
| C/G | analyst adjudication；JSON字段可能含Verdict/Remediation/riskScore | 没有数据可审，20gold闭合0；需确认哪些字段实际公开给模型 |
| D | 同工具单Agent对照；CORTEX有workflow routing | 未比较同资源固定多步程序；多Agent优于单Agent不能直接通过D |
| E | 10+场景，行为分析路由到workflow | 场景数不是语义执行家族K；是否主要由behaviorRule字段决定未知 |
| H | 原论文可下载；精确官方数据、许可未找到 | 不升级Strong |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 分诊每条SOC告警是否应升级 | 论文所述JSON告警，实际文件未获取 | 用户/资产记录、原始日志、结构化查询；快照未获取 | 分析员判定，未获取 |
| 类python的DAG | `scan(alerts)`，N只知论文称数千 | `sem_map(route); fetch_evidence; sem_map(adjudicate)` | `project(verdict, evidence); score_private`；仅论文流程重述 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 未知，未取得真实记录及gold | 同资源固定日志查询＋语义聚合是必要对照 | 未知，不能从论文F1预测单例 | ==按行为查用户、资产、事件与历史基线，核对预期操作==；证据不足则显式Unknown | `route -> parameterized_queries -> evidence_join -> decision`，仅假设，非已提取 |

| 比较证据 | 作者表中数值（非本次实测） | 限制 |
|---|---|---|
| Actionable F1 | prompt .61，tool-use .66，CORTEX .78 | 不等于LOTUS vs Agent同资源固定程序比较 |
| 成本 | tokens2100/4152/23600；延迟28/44.6/152.4秒 | 高质量有明显成本；完整学习/提取成本未测 |
| 复用 | cross-alert state disabled | 论文设置不能证明批共享/单轨迹提取摊销 |

没有真实案例实例可以诚实填写；本卡用“未获取”保留缺口，禁止以编造样例填补。下一步仅在找到可下载正式资产后才值得做20条和K审计。
