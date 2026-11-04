# Increment93 — MI论坛对话：真实批量与人工标签成立，长E绑定未成立

仍7/15。本候选不计入合格湖。实际下载[原论文](https://aclanthology.org/2022.coling-1.293/)PDF6237739bytes16页、[完整作者仓库](https://github.com/anuradha1992/Motivational-Interviewing-Dataset)commit `ced27c305c06cc587109c76f66b504efd1c06d05` ZIP981370bytes3成员（2文件，全部CRC通过），以及[官方MITI4.2.1手册](https://casaa.unm.edu/assets/docs/miti4_2.pdf)40页512779bytes。精确SHA256、URL收据在artifact/evidence/shared-environment-audit-20260908-v93/downloads.json。

实际CSV20462行、2000dialog_id，其中speaker3201行不标目标、listener17261行；listener最终15类有效标签16811行、未决“-”450行。原论文声称16812已标，当前字节少1，未擅自修复。分句不等于独立对话，2000对话也尚未审计同帖/同人重复。源为CounselChat及Reddit真实帖子，不是模拟临床治疗；不能推断治疗效果。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 根据完整对话，将每句listener回复归入作者15类支持行为 | 2000对话、17261目标句、3201speaker上下文行 | 论文表1的修改标签规则；源于MITI2.0与4.2.1 | turn、author、dialog_id可恢复上下文顺序，仍需结构校验 | 16811已达成一致标签、450未决；所有ann/judge/stage/final字段仅评测侧 |
| 统计回复中是否先获许可再建议 | 同上下文 | Advise with/without Permission的任务定义 | 前文是否询问建议不可只从目标句看 | with484、without2285；属于同分类的派生视图，不算独立湖或独立标注任务 |
| 统计对话支持行为分布 | 同批对话 | 15类映射 | 确定性groupby，不人为加入新语义步骤 | 原生类别计数可派生，未决不能当Other或负例 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `dialogs.explode(listener_sentences).sem_map(adapted_miti,E,context).groupby(dialog).count_by(label)` | 2000→17261目标句 | 16811有效＋450未决；评测覆盖及分母需冻结 |
| `classified.filter(label in permission_advice).groupby(label).count()` | 2769条已标建议类 | with484/without2285；未决中是否存在建议未知 |
| `classified.filter(label=='Direct').project(record_id)` | 原生Direct898条 | 仅类别投影；不代表临床不适当或实际伤害判定 |

具体源例：`RED | 163 - MentalHealthSupport`的turn4句子要求点击右上角信封、再点击发送私信链接，人工最终标签Direct。这是网站操作指令，说明Direct标注的是语言行为，不能直接解释为危险治疗。完整例句仅保存在本地audit.json。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 上述网站操作句目标Direct；未跑模型 | 完整上下文＋作者修改规则固定sem_map，再确定性投影 | 同Direct目标，不预设优势 | ==核对Direct指命令式语言行为而非临床风险==→分类→投影 | `dialog_context→adapted_behavior_code→aggregation`；仅设计 |
| 建议许可目标取决于前文；本轮未指定另一个实例gold | 固定检索同对话前文、按相同规则判断许可 | 同目标 | ==核对显式/隐式许可及建议定义==→读取前文→分类 | `permission_context→advice_type`，不能用当前ann/judge字段做工具 |

为何40页手册尚不能充当本任务E：论文明确混合MITI2.0和4.2.1，并新增Self-Disclose、Other，按listener句子分配标签；4.2.1原手册把Question作为行为编码，而本任务分Open/Closed，原手册还包含本数据未标注的global scores。论文表1有15类短定义，但未证实全部长规则在修改后如何适用。不能为了满足长E条件把整本手册拼入输入，更不能把该数据改称标准MITI治疗忠实度评估。

作者仓库声明CC BY-NC-SA3.0；论文与手册权利分别处理。本轮无模型调用、无public快照、无优势结论。后续若能取得作者实际培训/标注完整规范及版本映射，再继续；当前留待核验并优先搜索其他来源。脚本download.py/audit.py与收据同v93，raw在data同后缀。
