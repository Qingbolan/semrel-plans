# 第三十七增量：CliniCARE-Bench共享临床规范审计

**累计仍1/10；本来源为接近目标、待取得数据的候选，不计入可行湖。** 已下载52页原论文和完整作者仓库，确认真实病例来源、固定任务模板和共享规范目录；缺患者名单、病例输入及精确gold，无法完成具体患者的端到端求证。不能将25种任务计成25个独立湖，也不能将750例当成一种任务的批量。

| 原始来源 | 本次取得与边界 |
|---|---|
| [原论文v1](https://arxiv.org/abs/2608.07796v1) | 52页、979,077 bytes；pdftotext提取完成但报告PDF字典字符串语法警告，保留原字节；本文核验结合公开源码 |
| [完整作者仓库](https://github.com/scaleapi/clinicare) | commit `bbce780bc0dab07aae584f4dbc097601916b0905`；215 blob逐个Git SHA1验证、ZIP CRC通过；未执行作者代码 |
| `benchmark/_scenarios` | 25个scenario.toml；原论文每场景30例，总750，属于来源报告而非本地患者计数 |
| `benchmark/corpus_manifest.csv` | 实读67条；16条ship-md、29条fetch-pdf、17条download-pdf、1条download-epub、4条fetch-html |
| `benchmark/corpus_public` | 16篇Markdown实际取得；例如SAMHSA TIP63为144,823词、CDC抗菌药管理11,978词、CMS再入院方法24,541词；其余51篇只有获取配方，不能宣称全67篇已取得 |
| `DATA_ACCESS.md` | full750.csv与dev148.csv均不在仓库；MIMIC及cohort须凭证获取；精确标签不能用construction的silver重新生成替代 |

病例来自MIMIC-IV v3.1、Note v2.2、ED v2.2。本文未使用凭证、未下载受控患者数据、未申请或联系他人。规范库的本地PDF转录并非逐字节确定性过程，仓库也明确原实验语料不可逐字节复现；未来必须另行冻结本地版本。长文档存在不自动证明每条病例都需要它的全部内容。

gold由多模型独立审定并以Clinical Board子集审核校准，不是750例均获独立临床专家全量重标。本次未取得精确gold，也未核验患者去重。公开scenario中的标签规则、policy_gold和policy_facts属于评测材料，不能当病例公开输入。代码许可和第三方指南/MIMIC使用权分开，不将代码可下载解释成患者或指南可再发布。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 对同一规范下的MICU病例，逐案判断SEP-1 bundle是否在时间窗内完成或有合理例外 | 67篇共享规范目录，16篇已取得；SEP-1 BPCI摘要1,484词，CDC sepsis core elements12,895词，不能仅凭后者长度证明判定必需 | MIMIC-IV结构化病历：lactate、blood culture、EMAR实际给药、vitals；未下载 | ED triage及转院史、出院叙述；Note/ED未下载 | 论文该场景30例；full750精确标签不可得，不能伪造具体患者答案 |
| 已实际读取的具体任务模板scenario-06-sepsis-bundle | 问题要求适用bundle、时间窗、合理理由，并说明就诊前已开始治疗可能不能用当前triage作零点 | 参数subject_id/hadm_id仍为占位符，不是真实患者实例 | 公开prompt要求时间戳；标签契约区分医嘱时间和实际给药时间 | 四类YES、NO、缺数据不确定、医学歧义不确定；不把两种语义不确定折叠为执行ABSTAIN |

| 类python的DAG | 具体数值 | 当前状态 |
|---|---|---|
| `scan(cohort).filter(scenario == sepsis_bundle)` | 来源设计N=30，本地病例N未取得 | 750不是同一任务N；未构造快照 |
| `join(edstays, emar, labs, cultures, notes)` | 5类以上真实表/叙述来源 | 只核验工具和模板所需字段，未读取患者表 |
| `sem_map(resolve_episode_and_time_zero)` | 转入前病程可导致本地时间零点不可确定 | 必须读取公开叙述，不能拿隐藏标签提示当前病例 |
| `sem_map(applicable_elements_and_justification).compute_windows()` | 模板含3h/6h窗口、条件触发；这是benchmark契约，不作为通用临床建议 | 固定流程可有分支与计算器，无理由预设Agent优胜 |
| `sem_filter(verdict == YES).project(case_id).count()` | 输出/真实选中数未知 | 四类全量判定另报，执行失败独立记录 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 无真实患者输入，不能给YES/NO预期值。若转院前时间零点确实缺失，契约参考是缺数据不确定，而非自动不合规 | 固定检索叙述、识别转院和起始时间，取同一指南及给药/检查记录，计算窗口，再查合理理由；允许条件分支、共享索引与缓存 | 同契约；没有实测结果或准确率差距 | ==确认本次就诊是否为病程起点==→==若为转院，查既往治疗与时间记录==→==区分给药医嘱与实际执行==→==识别适用规范、触发条件与例外==→有据输出四类之一；工具失败为ABSTAIN | `SepsisAuditOperator(E_version, episode_resolver, administration_timeline, applicable_elements, timing_checks, justification_reader, semantic_unknown, abstain)`；单轨迹提取未实现，必须对照仅E编译、固定程序、Coding Agent和批Agent |

这一路线的具体价值是“多个表与叙述共同决定时间锚点及例外”的真实审计结构。但当前每任务30例、受控病例和gold缺失、全规范未取得，所以尚未完成用户要求的可行性求证。下一步需要可访问的精确cohort及病例，然后才能检查同任务批量与公共输入充足性；不因模型共识或长目录直接计数。

原资产data/shared-environment-audit-20260908-v37；审计脚本audit_source.py、统计及SHA256收据位于artifact/evidence/shared-environment-audit-20260908-v37。没有模型执行、作者程序运行、工程测试或独立确认结果。
