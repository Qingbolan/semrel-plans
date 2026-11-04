# 增量6：HICRIC / IMR Appeals保险真实申诉核验

**未通过完整门槛，合格清单仍0/10。**本轮找到并下载了与目标直接相关的保险申诉语料；失败点是适用环境缺失和case→policy关联，而非没有真实决定。下面为审计记录，不列为可行推荐。

## 原论文、完整仓库与数据

- [原论文（作者仓库链接的版本）](https://drive.google.com/file/d/1vsu0Ns6R6AeTX4-Hf2OdYqRvHD4yNm4y/view)：Mike Gartner，HICRIC，19页、311,018 bytes。已实际下载为`data/shared-environment-audit-20260908-v6/paper.pdf`；非仅在线摘要。
- [作者完整仓库](https://github.com/TPAFS/hicric/tree/37d88ab02833862c3f0b0ad4d0b3d52a96a705b2)：commit `37d88ab02833862c3f0b0ad4d0b3d52a96a705b2`，ZIP1,549,071 bytes，73个Git blob逐个验证。
- [IMR Appeals](https://huggingface.co/datasets/Persius/imr-appeals/tree/c68b70e0faf74cd2b5731ea02ad7ba7d99a11b8b)：固定revision `c68b70e0faf74cd2b5731ea02ad7ba7d99a11b8b`，完整train/test parquet分别79,888,366和12,689,124 bytes。
- [HICRIC](https://huggingface.co/datasets/Persius/hicric/tree/e9304975feff9ccaaf15cf547f698590d00d78c3)：固定revision `e9304975feff9ccaaf15cf547f698590d00d78c3`，本轮下载完整coverage-policy分区12,426,008 bytes；其他大分区仅查看清单，未声称下载全语料。

全部原始资产在`data/shared-environment-audit-20260908-v6/`。[下载收据](../artifact/evidence/shared-environment-audit-20260908-v6/downloads.json)、[统计](../artifact/evidence/shared-environment-audit-20260908-v6/statistics.json)、[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v6/audit_data.py)、[验证](../artifact/evidence/shared-environment-audit-20260908-v6/validation.json)。没有执行作者代码。

## 本次全量计数

| 数据 | 行数 | 决定分布 | 单位和缺口 |
| --- | --- | --- | --- |
| train | 64,067 | Overturned 30,090；Upheld 33,977 | 唯一text 61,004，唯一full_text 62,970 |
| test | 9,920 | Overturned 4,576；Upheld 5,344 | 唯一text 9,886，唯一full_text 9,890 |
| 合计 | 73,987 | Overturned 34,666；Upheld 39,321 | 是发布记录数，不是已审计独立案件数 |
| coverage-policy分区 | 3,661 | 无case gold | 4,295,700空白分词，5种source_url/relative_path |

train/test间精确text和full_text交集均0；这不证明源案件/近重复隔离。作者`src/processors/ny_dfs.py`明确把同一原case的多个审查摘要各输出一行，而发布训练/测试表没有原case_id。因此独立案件数和跨split案件重叠尚不能从发布五列确定。

案例表仅`text, decision, appeal_type, full_text, sufficiency_id`。没有保单ID、辖区、产品、适用规则版本、源案件ID。作者上游NY处理器原本保留jurisdiction、insurance_type等字段，但最终发布表未保留；仍未证明能恢复同一保单分组。

coverage分区的源结构实际为：350条Medicare NCD、2,270条Medicare articles、1,039条Medicare LCD、1份Medicare & You、1份MaineCare手册。不能把这些全部当成适用于CA/NY商业申诉的共享规则，也不能把网站表中“7 documents”直接解释为7份独立保单；发布Parquet的记录粒度不同。

论文§8.3直接说明公开库缺少商业保险合同、商业医疗政策及部分Medicaid计划材料；§5讨论短摘要不能替代裁决所需资料。该论文提供的是预期结果预测任务，不能据此主张公开E足以复作真实裁决。[原论文](https://drive.google.com/file/d/1vsu0Ns6R6AeTX4-Hf2OdYqRvHD4yNm4y/view)

## 具体Query与数据湖

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold/审计资料 |
| --- | --- | --- | --- | --- |
| 按适用保险规则，逐项判断住院医疗必要性拒付申诉是否应撤销；目标应固定policy版本 | E候选：上述3,661条coverage材料，共429.6万空白分词；与本例是否适用未知 | x：test第0行，67岁男性，2019-01-02至01-03住院申请报销，保险人以医疗不必要拒付 | 应有的保单、产品、辖区、有效时间、病历与相关临床指南未齐；不能填成已有文件 | 发布decision=Upheld；sufficiency_id=1为模型伪标签，不是专家确认输入充分 |
| 实例定位 | 同一候选E，不能因都叫health insurance就默认适用 | 输入末尾含“没有血流动力学不稳定、肾衰竭、严重梗阻、败血症或不稳定医疗问题”的片段 | full_text可见其来自审查员评估上下文；须逐句核验是原病历事实还是裁决后判断，当前不能宣称无泄漏 | full_text SHA256=`9cf62d6e4e26531f51451913f066f9ebf777bcd7b73d6e3dd7920f16a4464994`；只在构造/评分侧读取 |

这里的原gold表示申诉决定维持，不等于“患者不需要治疗”或“所有此类住院均不保”。不把一般医学常识预测对标签，视为依赖共享policy的证明。

## 类Python DAG

| 类python的DAG | 具体数值/字段 | 实际可执行性 |
| --- | --- | --- |
| `rows = load(train, test)` | 64,067+9,920=73,987 | 已实际读取并计数 |
| `R = group_by(rows, policy_id, version)` | 发布表无这些字段 | 当前无法建立用户要求的同E批次；不能把空policy_id合成一组 |
| `E = load_coverage_partition()` | 3,661行、5种来源 | 已读，但适用性和必要规则覆盖未核实 |
| `pred = sem_filter(R, should_overturn, E)` | 示例gold为FALSE（Upheld） | 未运行；输入条件不足不能用模型表现推断机制优劣 |
| `score(pred, private_decision)` | 需要case实体隔离、逐项输出和明确ABSTAIN | 现有随机记录划分不足以证明独立确认 |

## 方法预期表：解释缺口，不伪造成功

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 目标标签FALSE；实际可能TRUE/FALSE，尚未执行；命中也可能依赖审查员片段 | `sem_filter(text, should_overturn)`进行条件分类；只喂摘要不构成policy实验 | 同样无法保证复作裁决；合规的证据检查可能ABSTAIN | ==查找保险产品与辖区==→==确定适用policy有效版本==→缺失则记录未能完成；不得自行补出保单 | `resolve_policy → validate_inputs → retrieve_criteria → decide_or_abstain`；当前只有设计，没有已学算子 |
| 固定检索程序同样可以发现规则不适用并ABSTAIN | 共享索引→按明确元数据检索→固定适用性检查→sem_filter；允许与Agent相同工具 | 只有补齐适用规则和病历后才可比较判断质量 | ==检索住院/观察标准==→==核对实际病情与标准例外==→引用段落并判断 | 参数化输入字段与证据覆盖检查；不是针对67岁男性的硬编码规则 |
| E-only Coding Agent直接生成程序必须作为强对照 | 从任务与完整E提取规则和批处理程序，冻结 | one-trace不能从缺失E中学出真实policy，且当前没有可用示范 | ==执行一条公开证据完备的真实案例==→自动提取→冻结→独立批次 | 只有在上述数据缺口补齐后才评价轨迹价值；不拿ABSTAIN增多宣称Agent更强 |

## 本轮结论和可追的下一步

HICRIC不是“没有现实场景”，它恰好揭示了现实场景与公开可评测材料之间的缺口。本轮拒绝理由有原论文、发布字段和源处理代码三方证据。应从监管原始案件数据库恢复case ID/规则版本关联，优先单一公开计划的裁决，避免给商业申诉配上Medicare规则。

新增测试0、模型调用0；仅源数据统计和哈希核验。论文第8页已渲染并视觉检查。数据许可与代码许可不同，作者库也要求逐源核许可；本轮不再分发原始素材。目标继续active。
