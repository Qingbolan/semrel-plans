# 第十三增量：TrialGPT反向分组核验

2026-09-08，Asia/Singapore。来源审计，严格通过0/10；本候选不计入可行清单。

## 已下载

- [原论文](https://arxiv.org/abs/2307.15051)，PDF2,175,100 bytes。
- [完整作者仓库](https://github.com/ncbi-nlp/TrialGPT)，commit `1b3242cd50c153a9c324661d4a0bd94fc68a4226`；ZIP26,996,251 bytes，24个Git blob全部一致。未运行作者代码。
- 仓库内三队列queries、qrels、已检索试验信息及SIGIR corpus均实际取得。没有下载仓库外的完整TREC corpus/trial_info，不称已取得全部注册库或完整protocol。

原下载位于`data/shared-environment-audit-20260908-v13/`；[下载收据](../artifact/evidence/shared-environment-audit-20260908-v13/download-receipts.json)、[统计](../artifact/evidence/shared-environment-audit-20260908-v13/statistics.json)、[脚本](../artifact/evidence/shared-environment-audit-20260908-v13/audit_data.py)。

## 核验改变了什么

论文Methods明确：SIGIR病例是专家编写的理想化病历表示；TREC2021/2022是synthetic患者描述。不是公开真实EHR。在论文用户研究中另有6个semi-synthetic病例，也不等于数千真实病例开放集。

源query文件含184条（SIGIR59、TREC75+50），其中SIGIR `sigir-201428` 没有qrels，所以实际有标注183患者，与论文一致。不要把queries行数误写成184个有gold患者。

| 队列 | 有gold患者 | 配对标注 | 不同试验 | 单试验最大患者数 | 单试验患者数中位数 |
| --- | --- | --- | --- | --- | --- |
| SIGIR | 58 | 3,835 | 3,593 | 5 | 1 |
| TREC2021 | 75 | 35,832 | 26,162 | 75 | 1 |
| TREC2022 | 50 | 35,394 | 26,585 | 50 | 1 |
| 按NCT ID合并（只作结构诊断） | 183 | 75,061 | 51,431 | 76 | 1 |

按NCT ID合并不代表跨年份注册记录字节或protocol版本相同。本轮没有把这个合并视为冻结E构造。即使宽松合并，同一试验≥100个有gold患者的组也是0。

SIGIR标签1是“进一步调查后可能转介”；TREC标签1是“相关但排除/不合格”。不能混成相同临床决策类别。原论文还明确评估忽略地理位置与招募状态，因此“eligible”不等于现实可入组决定。

## 具体组

最大组NCT01994200有76个配对，全部标签0。仓库检索缓存中其入排标准合计仅82个空白分词，研究主题为甲状腺癌跨学科团队照护。条件包括新诊断、癌症类型、年龄、语言、KPS及预计生存期。这里取得的是入排标准文本，不是完整protocol。

有正例的较大组之一为NCT01994343，TREC两年合并75个配对：72个0、2个1、1个2。不能因存在一正例就称为大规模真实患者批。缓存作为实际数据示例使用；不能把按gold分组的缓存键0/1/2及当前评测配对标签暴露给模型。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 原任务：给定患者，筛选和排序候选试验 | 每个trial不同入排标准，非单一长E | 183个有gold合成患者摘要 | 检索候选与试验元数据；不是长protocol PDF | 75,061配对标签，按患者建检索池 |
| 用户方向：固定NCT01994200，逐患者判断资格 | 缓存标准82词；完整protocol未提供 | 76个有标注合成患者 | 按NCT反向分组只是本轮审计 | 76个全0；不能用于宣称复杂资格推理增益 |
| 固定NCT01994343的同类审计 | 注册标准，版本一致性待核 | 合并75个合成患者 | 允许公开患者文本，隐藏分组标签 | 72不相关/2排除/1eligible；不是现实入组记录 |

## 类Python DAG

| 类python的DAG | 具体数值 | 执行/拟议 |
| --- | --- | --- |
| `pairs = scan(qrels)` | 75,061条 | 本轮实际读取；构造侧private |
| `groups = group_by(pairs, trial_id)` | 51,431组；最大76、中位1 | 已执行计数，不假设跨年同版本 |
| `E = freeze(trial_criteria)` | 示例82词 | 拟议运行构造；不填充无关页面制造长E |
| `R = project(patient_id, patient_text)` | 示例76个 | 不允许携带gold分组键 |
| `facts = sem_map(R, E.required_attributes)` | 年龄/癌症类型等 | 未执行 |
| `eligibility = sem_map(facts, E)` | irrelevant/excluded/eligible等 | 拟议；缺信息不能随意当eligible |
| `result = sem_filter(eligibility, is_eligible)` | 示例gold选中数0 | 未执行；常量拒绝控制可能已命中全部 |

## 多种方法预期表

以下不是实测结果，未运行LOTUS、Data Agent或提取器。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 对最大组目标为空列表；是否全部命中未测 | 标准直接拆条件→sem_map患者属性→sem_filter；常量拒绝也须报告 | 同目标，不预设更准 | ==核甲状腺癌目标条件与排除项==→逐患者核事实→缺信息按冻结任务处理 | `CriteriaParser → PatientFacts → EligibilityCheck`；短标准直接编译是强基线 |
| 对NCT01994343目标1个eligible | 固定逐条件判断与固定聚合，保留排除原因 | 同一目标，但gold不证明真实入组 | ==核标准版本与患者所需信息==→==记录实际访问的标准==→输出 | 参数化条件+证据引用+UNKNOWN/ABSTAIN语义，不能写死正例ID |
| 跨队列label1不可直接统一 | 先按来源定义标签映射，再分别评分 | 同样必须遵守来源语义 | ==核SIGIR转介意向与TREC排除定义==→分开任务契约 | 来源适配属于构造，不冒充轨迹学习 |
| 学习轨迹是否有必要未知 | E-only条件编译、固定工具及Coding Agent均可用相同资源 | 单次可观察轨迹提取必须独立验证 | ==一次执行记录条件访问与工具动作==→冻结→独立批次 | 包含构造成本；不从论文TrialGPT指标外推本项目优势 |

结论：这是有用的临床匹配研究数据，但不满足本轮“长共享E＋大量真实cases”的严格要求。排除依据不只是synthetic：按trial反向分组也实证显示共享批量不足。下载/结构核验不能称临床或性能验证。新增工程测试0；模型、预算、种子、推理缓存均不适用。继续寻找独立真实来源，不用三个队列凑三个合格湖。
