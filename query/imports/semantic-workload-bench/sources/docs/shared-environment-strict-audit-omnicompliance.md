# OmniCompliance-100K：Reject

[原论文](https://aclanthology.org/2026.findings-acl.115/)与[完整官方仓库](https://github.com/HKUST-KnowComp/OmniCompliance-100K)已下载；commit07c44ff5795229ce1f205acaf6018f7b4ce569d5，204文件，ZIP26376602bytes。见[源收据](../artifact/evidence/shared-environment-strict-omnicompliance/source-progress.json)、[全量字段审查](../artifact/evidence/shared-environment-strict-omnicompliance/provenance-audit.json)。

| 入场项 | 实际证据 | 结论 |
|---|---|---|
| A固定q | 对background与给定source_rule判PERMITTED/PROHIBITED | 固定条件分类成立；不足语义未由人工gold定义 |
| B共享E | 全库规则按法规树化，原benchmark逐条给单规则 | 完整法规共享任务是派生设计，不是原实验 |
| C20依据 | 77,016项均无reference_link字段；没有其他URL来源字段，relevant_rules只是规则名称 | 原来源与20条独立依据未闭合，不伪造20通过 |
| D完整E固定不足 | 原评测直接background+source_rule；无同资源强固定对照 | 未证 |
| E语义家族 | 11,475不同source_rule字符串，每个最多33项 | 单规则不是执行家族；K未知 |
| F天然批 | 74案例JSON共77,016列表项；论文106,009 | 未核事件级去重；名称76,896种不是独立事件数 |
| G独立gold | 搜索提示要求模型生成relation_to_rule，允许找相似类比案例；人工2220项是关联度抽查 | 不满足已验证独立裁决gold；全量关系未独立核准 |
| H材料 | 原论文+完整代码/数据MIT；外部原件未提供 | 代码许可不自动覆盖引用法规与原案例 |

| Query | 数据1 | 数据2 | 输出/不足 |
|---|---|---|---|
| 给定规则判断案例是否违反 | cases/*/*.json的example_background | source_rule；rules/*提供树化规则 | VIOLATES/COMPLIES；另37null、3COMPLATES未规范，不能默默当false |
| 根据全法规判断案件最终裁定 | 同样背景未证明事实充分 | 完整适用法源/判例未冻结 | 不提供此派生任务的独立gold，不增造q |

| 类Python DAG | 操作 |
|---|---|
| `scan(cases) -> project(background,source_rule)` | 普通：排除outcome、relation、relevant_rules等答案侧字段 |
| `sem_map(background,source_rule) -> decision` | 关键语义条件分类；原评测case_eval_llm.py459–465如此构造输入 |
| `score(decision,private_relation)` | 独立来源欠账的模型生成标签，不满足本目标gold条件 |

| 方法 | 预期过程（未执行） | 结果/结构边界 |
|---|---|---|
| LOTUS任务only | 按背景判断 | 缺规则，资源消融，非强基线 |
| LOTUS完整E/给定规则 | 固定检索/规则匹配→sem_map | `retrieve→classify`尚未被排除 |
| 逐记录Agent | ==查法规适用性和关联条文==→核背景 | 原链接缺失，不能保证还原判决 |
| 批Agent | ==共享法规索引==→批量检索分类 | rho_E可摊销；rho_P固定比较；rho_G/rho_R及K未知 |

真实公开例子：eu_foundation_rights_20251220_002742.json首条Google Ireland v CNIL，给定规则为宪章序言（重申权利与解释背景），relation=VIOLATES。仅有该宽泛规则不足以推出具体域外删除义务；其process_and_outcome应留在私有侧。未逐条核原判决，所以不认定其案件叙述正确。

更接近固定条件分类而非已证明的HSCodeComp式语义执行家族。Reject的含义是当前公开材料不满足入场；不证明所有真实原案件无法重构。若取得官方裁决与真实来源链接，可另立重建任务，但不得将当前生成标签直接升级为独立gold。
