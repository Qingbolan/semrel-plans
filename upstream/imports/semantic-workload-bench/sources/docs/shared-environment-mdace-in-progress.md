# MDACE / RAG-Coding：来源增量核验，未计入 Strong

本项仍在核验，未加入32项已判定清单。原始 MDACE 论文与完整官方仓库已下载；RAG-Coding v2论文已下载，但未定位其官方代码与MDACE-2025新版标注。本次未取得病历原文，C20=0，不把标注偏移当成证据闭合。

| 项目 | 下载/实数 | 缺口 |
|---|---|---|
| 原MDACE | [ACL原论文](https://aclanthology.org/2023.acl-long.416/)、[官方仓库](https://github.com/solventum-oss/MDACE)，commit bf438d0d3a0dd905439011bcf423de66ee85d3ce；929文件 | 正文需MIMIC NOTEEVENTS，未获取 |
| 记录单位 | 708个data JSON；302个独立hadm_id；IP ICD10/ICD9各302，Profee各52 | 不能把版本/同患者多个note重复计为N |
| 证据 | note_id/category/description/annotations；annotations有begin/end/code | 0个note text字段，不可从代码描述反推事实 |
| 许可 | 仓库MIT；论文明确正文受PhysioNet Credentialed Health Data License约束 | MIT不能覆盖病历下载权限 |
| RAG-Coding | [v2论文](https://arxiv.org/abs/2605.27377v2)已下载 | 代码/新版数据未获得，不能复现或核验新版20例 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 给每次住院的全部允许病历分配ICD10代码与证据 | 原MDACE 302个encounter，正文缺失 | 冻结年份的tabular list与guidelines；本轮未下载 | 人工代码与偏移，已下载，仅私有评分用 |
| 类python的DAG | `scan(encounter).load_notes()`，N=302 | `sem_map(assign).map(validate_KG).map(audit_guidelines)` | `merge_by_encounter; compare_private_gold`；暂不可运行 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 高血压伴慢性肾病例：论文报告修正I10→I12.9；LOTUS预测未知 | 输入完整病历与同版规范，用sem_map；可加入固定KG检查与规范摘要 | 目标同左，实际预测未知 | ==定位共存疾病、代码关联、章节规则和排除条件==；保存可核验证据再修订 | `candidate_codes -> KG_audit -> cached_guidelines -> final_audit`；四阶段固定程序也是合法强基线 |

| 论文证据 | 实际含义 | 不可推导 |
|---|---|---|
| RAG-Coding附录H：20样本，step4有31次修改，删除17/19正确，新增2/10正确，两次替换正确 | 作者中间步骤分析；未提供本次可核验20个原病例 | 不是本研究C20；不能宣称Agent已解决规范应用 |
| Table13：GPT4.1总112822.08 tokens，$0.25；step3 85636.73 tokens/$0.17可缓存 | 作者报告、非本次计费；与固定缓存对照有关 | 缓存规范摘要不是从一次执行自动学得算子 |
| 原MDACE表2：384 Number of Annotations；表3：302 Encounters | 修正后续论文将384转述为encounters的数量问题 | 不扩大真实N |

固定流程是否足够、环境是否必要、语义家族K、完整gold闭合均未确认。代码类型/章节类别不能代替执行家族。RAG-Coding可作为CodiEsp路线的同资源固定检索/规范摘要基线参考，不能把仅参数知识自纠正消融当成强固定流程对照。

收据：[MDACE来源](../artifact/evidence/shared-environment-strict-mdace/source.json)、[记录实数](../artifact/evidence/shared-environment-strict-mdace/data-audit.json)、[RAG-Coding来源](../artifact/evidence/shared-environment-strict-ragcoding/source.json)。未运行任何作者代码、模型或实验。
