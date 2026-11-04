# 增量7：Medicare Part C并非单一共享保单

本轮沿HICRIC原始来源继续核验。**找到172,842条带决定字段的Part C记录，但仍不通过（0/10）**：一个公共项目包含不同保险计划的附加保障条款，发布输入还是裁决理由，不能把项目名当同一E。

## 实际获取与验证

- 原论文和完整作者仓库复用[增量6](shared-environment-search-2026-09-08-round6.md)已经下载校验的HICRIC，commit `37d88ab02833862c3f0b0ad4d0b3d52a96a705b2`。这是一条路线的继续核验，不作为独立新数据湖计数。
- 新增下载[固定HF快照的case-description第0分片](https://huggingface.co/datasets/Persius/hicric/tree/e9304975feff9ccaaf15cf547f698590d00d78c3/case-description)，134,622,387 bytes，共247,517行；仅下载四分片中的一个，不能把以下数字说成全库统计。
- 该分片按`relative_path`筛得Part C 172,842行：Unfavorable 164,115、Favorable 7,982、Partially Favorable 744、Withdrawn 1。独特text 169,755，非空172,842；独立case数未知。Withdrawn不能映射成“拒付正确”。
- 所有八列为`text, tags, date_accessed, source_url, source_md5, relative_path, decision, appeal_type`。没有plan/contract ID、原case ID、事件日期或适用年度字段；date_accessed是采集日期，不是适用日期。
- 原作者`medicare_qic.py`处理器将`decision_rationale`转为text，独立保留decision；coverage_rules去重后另外写入。这里的text不是剥离裁决的新事实材料。

原始资料：`data/shared-environment-audit-20260908-v7/`。可复算[脚本](../artifact/evidence/shared-environment-audit-20260908-v7/audit_data.py)、[统计](../artifact/evidence/shared-environment-audit-20260908-v7/statistics.json)、[下载收据](../artifact/evidence/shared-environment-audit-20260908-v7/downloads.json)。源URL对应的原CSV本轮未获取，其上游MD5只是作者记录；本轮仅独立核验下载的Parquet SHA256，不宣称复核原CSV。

另查[CMS官方入口](https://www.cms.gov/medicare/appeals-grievances/appeals-decision-search-part-c-d)与[历史FOIA发布](https://www.data-liberation-project.org/datasets/cms-medicare-appeals-level-2/)。后者的[原始数据文档](https://docs.google.com/document/d/19yAjUqR-Cx6TlgOkBxoAnoxwGMUfuDkU9cqbumqyOzU/edit)已下载：2015–2019提供的表格缺病情、裁决理由和coverage rules，不足以替代逐案判断输入。没有为确认这点下载整套统计表；不计作完成论文/仓库核验的新候选。

旧QIC API返回403，记录在本地，不将访问错误说成数据不存在。随后读取作者合法公开的历史快照，无绕过认证。

## 具体数据：550美元牙科额度

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 依据指定计划2019年的牙科附加保障，逐项判断超过年度额度的报销申诉是否应获支持 | 应有E：具体计划合同及2019有效版本。当前缺失，不能用一般Medicare规则代替 | 真实源记录涉及2019-06-10至07-10的D0220、D0140、D2950、D2740服务，要求报销超过550美元 | 应有原账单、年度累计已支付额和合同适用信息，当前只有裁决摘要中的描述 | Unfavorable；Supplemental Benefit；原text 217词，SHA256 `8ff8042caf78089c8b795f87790dd2f8a8340e5ad648c35dff47e19babcc49b0` |
| 环境依据如何出现 | 摘要陈述本计划每年牙科保障550美元，但这是当前裁决提供的条款陈述，不能冒充独立下载的合同E | text开头直接宣布无需支付，随后解释额度已耗尽 | 该条款正说明不同计划规则影响标签；仍缺“同一计划大量cases”的分组键 | 从现成裁决摘要读出Unfavorable属于答案抽取，不能称政策判断 |

以上是原始记录的构造侧审计，不是医疗/保险建议。不能凭这条摘要认定所有Medicare附加牙科计划都有550美元上限。

## 类Python DAG

| 类python的DAG | 具体数值 | 当前状态 |
| --- | --- | --- |
| `source = read(shard0)` | 247,517行 | 已读取 |
| `part_c = where(source, source_path == '.../part_c.jsonl')` | 172,842行、169,755种正文 | 已计数；不是按计划分组 |
| `batches = group_by(part_c, plan_id, benefit_year, contract_version)` | 所需字段缺失 | 不能执行目标分组；不能补一个常量ID |
| `public = extract_predecision_facts(raw_case); E = load_contract(version)` | 当前217词全是混合裁决摘要 | 未构造；删除结果句仍不保证剩下的是独立事实 |
| `pred = sem_filter(public, E, should_allow_appeal)` | 该例目标FALSE；若有550美元限额与账单，可能固定算术足够 | 未运行；不能预设需复杂Agent |

## 方法预期表

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 如果喂现text，很容易读到拒付结论；这是泄漏诊断，非有效结果 | 直接从结论句抽标签，成本低也不证明编译收益 | 同样能读到结论，不构成环境探索优势 | ==识别输入含裁决结论==→记录样本不适合作为公开预测输入 | 这是数据校验，不是已学到的coverage operator |
| 补齐合同与账单后，目标FALSE；实际结果未测 | 固定检索牙科限额→抽取年度额度及累计额→数值比较；固定程序允许同样工具 | 也可能得到FALSE，无理由预设更准 | ==确认计划/年度/服务所属利益类别==→==查限额与例外条款==→核账单→判断 | `resolve_contract → extract_limit → extract_utilization → compare → check_exceptions`；该简单实例可能由固定程序完成 |
| E-only直接编译应作为对照 | 仅任务与真实E生成批程序，冻结 | one-trace与E-only比较需真正公开输入完备的示范及独立R | ==单次可观察工具探索==→提取→冻结→后续批次；当前尚不存在这条示范 | 不写死550美元；从冻结E读取限额，记录适用范围和ABSTAIN条件 |

本轮没有模型执行、示范提取或环境消融。仅下载和源审计；因此不填预计准确率，不以缺输入导致ABSTAIN证明Agent必要。后续应转查具有明确policy ID/版本的决定来源，或恢复上游CMS病例和合同关联；不能继续把不同计划的全部Part C数据硬合成一个E。
