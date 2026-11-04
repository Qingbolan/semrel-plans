# 增量8：HSCodeComp——共享税则与真实专家gold已闭合，公开输入仍待补证

**新增优先补证路线；完整通过仍0/10。**本轮首次在一个作者完整仓库中同时核到真实商品批量、独立专家标签，以及与官方版本逐字节一致的大型共享税则。未通过的关键是公开商品输入删掉图片/URL，且必要章注尚未冻结。不能把论文报告的图像实验当成公开数据可复现结果。

## 已实际下载

| 资产 | 实测 | 来源 |
| --- | --- | --- |
| 作者完整仓库 | ZIP77,541,590 bytes；536个Git blob验证 | [commit ee329e98f92b51bd797785f648c7c4e42e678ad7](https://github.com/ATH-MaaS/Marco-DeepResearch/tree/ee329e98f92b51bd797785f648c7c4e42e678ad7) |
| 原论文 | 仓库`assets/HSCodeComp.pdf`，10,042,953 bytes；已提取正文、视觉核第8页 | [论文](https://arxiv.org/abs/2510.19631)；下载的是作者仓库内PDF，不宣称与arXiv字节一致 |
| 商品与gold | `HSCodeComp/data/test_data.jsonl`，1,840,855 bytes | 632行、632唯一task_id、632唯一标题/属性组合、352个不同gold code、27章 |
| 冻结税则 | `hts_2025_revision_15.json`，13,731,683 bytes | 35,950行、29,932个不同非空code、描述部分251,406空白分词 |
| 官方独立副本 | 同为13,731,683 bytes，与仓库字节相等 | [USITC 2025 Revision 15](https://www.usitc.gov/2025_hts_revision_15)，官方标注发布于2025-06-23 |

税则SHA256 `83e5fc468a032b72c7f3759add0290b6bd2ba53fca40f73a5da0c59f9511a444`。632/632 gold code在冻结税则中存在；这是版本/code成员验证，**不是632条标签语义正确性验证**。

原始资料`data/shared-environment-audit-20260908-v8/`。[统计](../artifact/evidence/shared-environment-audit-20260908-v8/statistics.json)、[脚本](../artifact/evidence/shared-environment-audit-20260908-v8/audit_data.py)、[下载收据](../artifact/evidence/shared-environment-audit-20260908-v8/downloads.json)。没有运行作者代码、安装其依赖或载入其.env；完整快照仅本地保存。

## 三个条件分别到哪一步

复杂共享E有直接证据：同一美国税则版本、层级品目描述和大量候选code；商品不能仅按一般语义相似度任意挑标签。批量有632个真实电商产品资料。Gold由专家标注，而非真实通关裁决；用户要求的逐项gold可以有专家来源，但不能把它说成海关已裁定的632案。

论文描述标注者看商品网页、按规则和分类系统核验；高级专家抽查10%样本。公开版删除图片与URL；论文第8页说明图片可提供文本欠缺的材质/表面属性。因而需要逐项输入充分性核验或恢复合法完整输入，不能直接将纯文本版本的错误都归因于推理。[原论文§4、第8页及发布说明](https://arxiv.org/abs/2510.19631)

附带JSON主要为税则条目及税率/脚注，不等于完整类注/章注。仓库`gri_rules.md`是简化中文规则，不能冒充官方完整解释规则；外部CROSS/eWTP仍会变化。冻结任务需要补官方同版本章注，明确历史裁决库范围与公开工具访问条件。E-only程序是否足够尚未测试，不预设轨迹必要。

## Query与具体数据湖

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按US HTS 2025 Revision 15，对632项商品批量输出10位归类code及分类路径；也可显式派生“属于7117仿首饰”的Boolean筛选 | E1：官方一致税则35,950行，描述251,406词；固定层级表 | E2：仓库层级索引`hts_tree.json`与简化规则；官方完整章注仍待补，不把简化规则当权威E | R：632条标题、属性、价格、货币、平台分类；图片/URL缺失 | 独立`hs_code`，必须从公开输入移除；不能递归挂载仓库给Agent |
| task_id=0：绿色龙形磁性吊坠 | 7117为仿首饰；下级条目多处为Other，必须保留完整祖先条件 | 商品属性Metal/Copper，Women；141 CNY，1件；包装10×8×5cm | 标题/属性含噪声；价格不是已核实海关估价，不直接拿CNY数值套美元阈值 | `7117199000`；属于7117目标TRUE |
| task_id=1：Natural Purple Keshi Pearl Chain Necklace | 同一税则，珍珠制品与仿首饰分支不同 | 原真实商品标题与属性（详见JSONL），不是人工编造负例 | 仍需核实材质声明与必要图片证据是否充分 | `7116102500`；属于7117目标FALSE |

以上Boolean任务是研究者拟派生、需单独冻结的固定predicate；原任务是10位code预测。不得一边称复现原任务一边只评分前四位。两个商品gold为示例开发暴露，不是确认样本。

## 类Python DAG

| 类python的DAG | 具体数值 | 输出/局限 |
| --- | --- | --- |
| `E = freeze(official_hts_revision15)` | 35,950行；与作者副本SHA256相同 | 已完成版本/字节核验 |
| `R = project(products, public_allowlist)` | 632行；hs_code隔离 | 尚未发布public快照；原question也不等于自动通过泄漏审计 |
| `features = sem_map(R, extract_material_function)` | task0材质声明Copper；task1标题含Pearl | 未运行；遇缺属性应UNKNOWN/ABSTAIN而非编造 |
| `codes = apply_hierarchy(features, E, official_notes)` | 原始gold352种；全部code在E | 官方notes及证据充分性未闭合，尚未执行 |
| `selected = sem_filter(R, belongs_to_heading_7117, E)` | 示例task0 TRUE、task1 FALSE | 派生任务需独立契约；不能用gold代码作为模型输入 |
| `score(frozen_predictions, private_gold)` | 全632行计coverage/层级质量/完整成本 | 无实测结果，原论文指标不替代本次实验 |

## LOTUS、Data Agent与预期operator

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| task0目标7117199000、task1目标7116102500；实际输出未知 | 固定属性抽取→同一税则检索→按同级条件判断→code输出；禁止只给孤立Other条目 | 同目标，是否更准未知 | ==核材质/用途并区分平台营销分类==→==打开完整祖先链和适用章注==→比较候选→输出证据 | `extract_features → retrieve_headings → evaluate_notes → descend_siblings → validate_code`，字段参数化 |
| 固定检索程序也可共享树索引、缓存规则，并按缺字段分支 | B2预建索引→有界候选复核；固定程序允许同样工具、循环和缓存 | 可追加查询但不得把缺失商品图片想象出来 | ==发现纯文本无法确定材质/用途==→允许资源内补证→仍不足则ABSTAIN | 带证据充分性门槛和预算的程序，不把缺图错误当推理挑战 |
| E-only Coding Agent可能直接生成相同树遍历程序 | 任务+E生成并冻结批程序，不提供轨迹 | 单轨迹自动提取需真实Agent示范及独立R；本轮没有 | ==一条公开任务上的真实工具探索==→提取→冻结→测试 | 比较树遍历、固定检索、E-only与one-trace；不预设复杂Agent胜出，不写死示例gold |

当前状态：可追溯的真实批量/专家gold/官方共享E三者已对上，但必要规则覆盖与公开输入充分性仍欠账；因此未计入合格10项。下一步优先补章注与审计缺图依赖，同时检验另一条真实CROSS裁决来源ATLAS（本轮仅发现论文链接，尚未下载，不算新通过项）。
