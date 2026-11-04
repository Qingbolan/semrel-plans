# GUIDE — 真实大批数据，但当前不满足语义环境准入

[原论文v4](https://arxiv.org/abs/2407.09017v4)及[Microsoft官方数据页](https://www.kaggle.com/datasets/Microsoft/microsoft-security-incident-prediction)的2024初始v1包已下载。官方数据页可作为仓库替代（原要求H）；未找到源码不等于数据不可获取。压缩包538236447bytes，两个CSV解压大小共3513372918bytes。[来源哈希](../artifact/evidence/shared-environment-strict-guide/source.json)。官方当前v2增加队列排序标签，本轮不混用该更新。

| 条件 | 原论文与本地观察 | 边界 |
|---|---|---|
| 天然批F | 客户SOC标注事件；每个事件多条evidence/alert | 不以13M证据行代替13M独立事件 |
| 共享E | 可将旧事件关系作为H；OrgId与IncidentId可连接 | 不是公开完整企业手册/资产描述/操作背景 |
| C/G | 敏感字段SHA1后随机ID，时间加噪；AlertTitle、账号、文件名等为编号 | 保留同实体关联，不保留全部可解释的语义依据；C20=0 |
| D/E | 原论文为固定特征工程、PCA、随机森林及哈希/余弦相似检索 | 未证明语义分支家族；固定方法不足无证据，不能把DetectorId类别当K |
| 判定语义 | BP在SOC内外定义不统一，论文明确讨论该问题 | 某告警可疑不足以证明应为TP，授权业务背景未公开 |
| 许可H | Microsoft数据页明确CDLA-Permissive-2.0；元数据已保存 | 许可来自官方说明；不外推到其他私有遥测或源码 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 给每个OrgId/IncidentId预测TP、BP、FP | GUIDE_Test.csv，按OrgId/IncidentId汇集证据行 | GUIDE_Train.csv历史事件，可设为同资源历史库 | IncidentGrade为私有gold；Action/LastVerdict等字段需按时间与来源审计 |
| 类python的DAG | `group_by(OrgId, IncidentId)` | `aggregate_features; retrieve_history; classify` | `compare_private_grade`；结构/监督预测并不自动成为semantic workload |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 例Org657/Incident11767的第一条证据gold BP；未运行LOTUS，不据单行推全事件 | 先汇集完整事件，给同历史库；可训练固定tabular基线 | 未运行，不能保证从匿名ID恢复合法业务理由 | ==查同组织同实体历史与关联告警，寻找授权活动证据==；缺失背景应显式未知 | `group -> history_lookup -> classifier`可能足够；无法从现有编号证明目标语义家族 |

| 实例核验 | 已打开 | 未确认 |
|---|---|---|
| 首测试证据 | AlertTitle563，Category LateralMovement，实体User，LastVerdict Suspicious，gold BenignPositive | 没有原始业务操作描述；Suspicious不是最终BP的反证 |
| 首20原始行 | 已保存两文件各20行，仅字段审查 | 不是20个完整独立事件，也不是20gold依据核验 |
| 实验 | 没有运行作者模型/LOTUS/Agent | 不能把论文CGR生产结果当本次GUIDE实验 |

全量记录统计仍以[统计收据](../artifact/evidence/shared-environment-strict-guide/data-audit.json)最终完成内容为准。


最终判定：Reject（当前公开发布的任务形态）。真实规模成立，但语义依据闭合、语义家族以及同资源固定方法不足未成立。

| 全量扫描 | 证据行 | 分集内OrgId/IncidentId组合 | 组织数 | 单组织最大事件数 |
|---|---:|---:|---:|---:|
| Train v1 | 9,516,837 | 730,778 | 5,769 | 28,522 |
| Test v1 | 4,147,992 | 303,220 | 4,400 | 12,245 |

Train有51,340行IncidentGrade为空；这不等于51,340个无标签事件。同一事件可能有多条证据，尚未审计事件内标签一致性与跨split实体重叠；上述事件数不自动等于独立gold数。全量CSV流式读取完成，无解压副本，无模型实验。不得把两分集事件数之和称为已去重全局事件数。
