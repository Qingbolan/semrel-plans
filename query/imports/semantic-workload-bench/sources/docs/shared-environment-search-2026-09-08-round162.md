# 增量162：ACE / COMPACT，下载核验后不纳入可行名单

本轮新增来源，不重复计数CUAD/ContractNLI。**仍8/15，ACE不满足真实case、长共享环境及同E大batch三项要求。** 此卡保存排除证据，不把它列作合格湖。

## 原件与实际数据

已下载[原论文COMPACT，EACL2026](https://aclanthology.org/2026.eacl-long.377.pdf)，32页、5,058,314 bytes，SHA256 `c23f53d4cc56a31af1a0085e3690de54705aef7d332df5f14c31f59974782c5e`；完整克隆[作者仓库](https://github.com/FujitsuResearch/Fujitsu-Assessing-Compliance-in-Enterprise-Dataset)，commit `d79c5712c899da1289b7090cddde0b06f6cd50f9`，5个tracked文件，含完整train/test JSON。未下载底层633份合同全集，也不能声称发布行自带全文。原件在`data/shared-environment-audit-20260908-v162/`；逐文件哈希和标准库审计脚本在`artifact/evidence/shared-environment-audit-20260908-v162/`。

论文§3.2.3明确GPT-4o生成场景、Claude Sonnet4审查相关性及标签；§4.1的633指真实来源合同，不是真实合规事件。人工抽检不把所有模型生成标签变成独立真实业务判定。论文§4.2训练3240/验证360/测试1100，发布仅train3600/test1100，没有独立validation文件或ID，本轮不自行复原该划分。

实际4700行。train三类各1200；test合规380、不合规400、不适用320。每行只有1–4个evidence键，2895行仅1键；键数不等于原合同条款数。435行同一行多个键给相同文本。去重后的条款词数中位数train161/test164，最大3409/3404。按排序、精确去重文本集合定义公开E，共2153组，每E场景中位数2、最多14；这不是合同级分组，发布无合同ID映射，不能以4700/633替代组大小实测。

跨split有662个完全相同E、336个完全相同scenario_text，但只有**1个完整(场景,E)输入对相同**，该对标签相同。不能将336都称重复任务；同情境在不同规则下可能是有意条件对照。仍需源合同隔离，不能称官方split已证明独立。train的教师输出全部排除于被测公开输入，不把现成教师轨迹当本研究单次Agent示范。

## 用户要求的具体三表（仅说明这个被排除来源能做什么）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 对每个给定条款集判定场景合规/不合规/不适用，汇总不合规清单 | 4700个生成scenario_text | 行内clauses，非长合同全集；2153个精确E | 固定三分类任务定义；无来源合同绑定表 | gd_tr；主要模型生成并验证，不是4700次真实业务裁决 |
| 具体test[0]：ConvergTV把节目放到后来新建平台的归档栏目，未突出展示，是否违反给定许可？ | 场景说在许可地域及期限内发行；对方抱怨展示与通知不足 | evidence_5涵盖现有/未来发行渠道，起始2012-11-15、两年 | 不得自行增加首页展示/正式通知义务 | 发布目标Compliant；本轮展示已成为开发暴露 |
| 按缺失条件输出义务/例外证据图 | 相同场景 | 相同条款 | 图可作为方法中间产物 | 发布没有逐节点/边独立人工gold，不能追加为第二个已验证gold任务 |

| 类python的DAG | 具体数值 / 实例 | 边界 |
| --- | --- | --- |
| `scan(test).project(clauses,scenario_text)` | 1100行；883种精确E | 不读gd_tr/教师输出 |
| `groupby(exact_E).compile_rules()` | 全数据2153组，中位2、最大14行 | 缓存可实现，但不是大批同长E workload |
| `rows.sem_map(classify,E)` | test[0]目标Compliant；允许未来渠道且没有给定突出展示要求 | 预期目标，未调用模型，不能承诺命中 |
| `filter(label == 'Non-Compliant').collect(id)` | 测试发布目标400行 | ABSTAIN留在全量分母；不能直接读取标签生成清单 |

以下全部为**未执行的方法设计**，不是精度、延迟或Agent优势结果。固定程序、Coding Agent和E-only编译允许使用同一资源、检索、循环与共享缓存。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| test[0]应对齐发布Compliant，实测未知 | 固定sem_map读取给定许可、抽取发行渠道/期限/地域，检查是否存在通知或展示义务 | 同一个Compliant目标，实测未知 | ==定位许可范围和期限，检查抱怨事项是否对应给定义务==→条件核对→三分类 | `ClauseSet→RightsAndObligations→ScenarioFacts→Applicability→Decision`；需E-only编译对照，不能认定轨迹必要 |
| 不合规ID清单目标400项，不能预报实际值 | 相同E共享一次解析，逐场景执行固定判定，汇总 | 相同目标 | ==核对重复条款、例外引用及证据是否充分==→缓存规则→批执行 | `ExactECache→RuleEvaluator→Decision/ABSTAIN→Aggregate`；发布不含完整合同，未解析引用应暴露为限制 |

实际技术结论：它可用于合成条件推理诊断，但论文页数不是E长度，来源合同真实性不是场景真实性，跨条款推理也不自动意味着同E有足够摊销批量。没有模型运行、质量增益、成本或独立确认实验。README声明CC-BY4.0；上游合同/论文权利仍分别处理。
