# 第二十四增量：UDRP政策族与输出粒度

本轮修正第22/23轮的候选范围：**WIPO是提供机构，不是政策版本标识**。2024标记的2028个WIPO案件含24种case前缀，包括.eu ADR语言决定，不能整体称为共享UDRP的批次。统计见`artifact/evidence/shared-environment-audit-20260908-v24/policy-family-statistics.json`。

按公开case编号`D2024-数字`确定候选（不按结果筛选）得到1874案，其中1603单域名。其他154案仅退出这一政策族，尚未判断其是否能另成任务，更不能把它们拆成多个合格湖凑数。1871案正文包含完整英文UDRP名称；另外3案中两案写成“Uniform disputed domain name…”，一案缺乏那句程序模板但提及UDRP和Overview。故单纯字符串未命中不是另一政策的证据；它们仍待具体源核。

原论文、152页WIPO解释材料及来源收据继承第22轮。作者完整代码/数据ZIP仍在session11183下载，最新已返回408944640bytes；尚未完成843037756bytes的整档校验。没有另起下载。

## 任务选择需要由用途决定

1. **转移清单**：只选Transfer。必须知道请求及正式救济，Cancellation不可混同。第23轮发现的两处metadata差异继续保留。
2. **投诉获救济清单**：选择实际获得Transfer或Cancellation的案件。用于统计获得这两类UDRP救济的投诉，不能称“所有程序请求成功”或“所有三要件在对抗审理中成立”。这是另一个明确任务版本，不覆盖原转移任务。

第二种任务不需要强迫模型区分这两种救济，但仍需判断是否应给予救济，不是只看域名相似。对于缺省答辩、同意救济、混合域名结果等情形，需要保留程序信息和集合语义。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在同一UDRP及冻结解释材料下，批量判断投诉是否应获得Transfer或Cancellation救济 | 已下载官方Overview3.0及政策/细则152页 | D2024编号1874案，1603单域名，政策名称3案需人工核验 | 事实+双方主张+必要程序背景；不能给专家分析及本案最终决定 | 文末正式救济优先核验；metadata只作对照；输出包括MIXED/ABSTAIN而非强行二值 |
| D2024-1705 / sipchemgroup.com | 与第23轮相同规则 | 当前开发输入来自文书§4/§5，不保证请求救济已完整表述 | 官方原PDF已在v23下载 | 正式Cancellation；“转移”任务False，“转移或撤销救济”任务True。二者不冲突 |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `scan(recent).where(source==WIPO & case_id.matches(D2024))` | 1874，公开来源选择 | 替代错误的2028全部共享同一政策假设 |
| `parse(facts, analysis, decision)` | 1827有这三个标题的正确顺序，47失败 | 比上一轮四标题条件更宽，仅用于本次诊断，不声称覆盖改善已验证 |
| `derive_private_formal_remedy()` | 1762获救济、63denied、1mixed、1未匹配 | 只解析正式决定；不是模型推理结果 |
| `sem_map(apply_E).sem_filter(relief in {Transfer,Cancellation})` | 1824可与纯metadata粗类别对照的记录一致；未执行模型 | 粗类别一致不抹掉细粒度标签错误，不是gold独立正确率 |
| `project(case_id).count()` | 待建立不混同multi-domain的契约 | 不预填全量正确count |

事实/主张中的“请求转移/撤销”简易正则在1874案中命中150案，这只是**显式模式命中的下界**，不能推断其余1724案都缺请求。剩余未匹配决定D2024-1663的`transf erred`属于文本空格；不改源字节、不特判答案，后续应统一做有审计的PDF词内空格处理。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| D2024-1705粗救济目标True，细救济目标Cancellation；均未实测 | 相同允许输入/E，固定抽取权利、合法利益、恶意及程序条件，再输出；可固定检索和批缓存 | 同一目标，不预设更优 | ==确认适用UDRP及必要程序条件==→==查三要件与具体例外==→输出救济集合/缺口；不得搜索当前裁决结果 | `UDRPReliefOperator(E_hash, policy_applicability, facts_with_attribution, elements, procedural_conditions, relief_set)`；与精确remedy任务分开版本化 |

审计脚本`audit_remedies.py`及`--udrp`输出保留全WIPO与D2024两套统计，不覆盖差异。没有根据gold删除不一致、混合或解析失败记录；未生成public确认集。下步仍需完整归档/许可、正式决定提取验证、程序信息完整性和事实泄漏审计。目标0/10继续；没有将粗任务的结构计数当方法效果。
