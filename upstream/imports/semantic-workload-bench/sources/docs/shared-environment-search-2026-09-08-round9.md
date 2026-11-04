# 增量9：完整官方E已下载；ATLAS副本的版本与划分审计

**累计完整通过仍0/10。**本轮完成两项实质补证：HSCodeComp的同版本完整税则已落地；ATLAS公开副本全量读取，发现不能直接套用同一2025税则或其原split。副本审计不冒充作者原仓库核验。

## 下载与边界

1. [USITC官方2025 Revision 15完整PDF](https://hts.usitc.gov/reststop/file?release=2025HTSRev15&filename=finalCopy)：19,160,545 bytes，4,429页，pdftotext后1,485,640空白分词。封面版本为Revision15，含总解释规则（PDF第16页）和类/章注（第XIV类标题在2528页，第71章注在2530页）。已核正文，视觉只检查2528页版本标题。它补充[增量8](shared-environment-search-2026-09-08-round8.md)的官方一致JSON，不再把完整章注记成未下载。仍需核验商品证据充分性。
2. [ATLAS原论文v1](https://arxiv.org/pdf/2509.18400v1)：243,558 bytes，已下载提取正文。
3. 作者发布HF API本轮401，未能获取原仓库，原因不能确定。另找到公开[复制仓库](https://huggingface.co/datasets/Dayanand314Krishna/cross_rulings_hts_dataset_for_tariffs/tree/0a66ad345d3fc9828f362836d86b31e20798513c)，固定revision `0a66ad345d3fc9828f362836d86b31e20798513c`，下载全部5文件（含3个JSONL）。其README自称复制自Flexify；原作者版本字节一致性尚未验证，没有绕过认证。

原始资产`data/shared-environment-audit-20260908-v9/`；[下载收据](../artifact/evidence/shared-environment-audit-20260908-v9/downloads.json)、[全量统计](../artifact/evidence/shared-environment-audit-20260908-v9/statistics.json)、[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v9/audit_data.py)。官方PDF下载地址由官方站点前端的公开下载链接构造逻辑定位；没有自行换成currentRelease。

## ATLAS本次观察

| split | 实际行数 | 单10位code | 多10位code | 正则未匹配10位code | 至少一个code不在2025 Rev15 |
| --- | --- | --- | --- | --- | --- |
| train | 18,254 | 14,638 | 3,425 | 191 | 2,444 |
| validation | 200 | 154 | 45 | 1 | 29 |
| test | 200 | 169 | 30 | 1 | 27 |

解析仅匹配答案Reasoning之前的常见10位格式；未匹配不等于无标签，多code也不等于错误，可能一个记录确实含多个商品。必须定义集合输出或明确拆分契约，不能未经说明按单code accuracy评测。

实际总18,654与论文声称18,731有77差异，原因未知。精确user question重叠：train/test 40条，train/validation 41条，validation/test 1条。不能复用为独立确认划分；这也不证明每个同文本样本同一源案件，因为源case ID已丢失。

全部记录是`messages`；未保留ruling ID、日期、URL、冻结HTS版本。27/200 test行的匹配code不在Rev15，可能源于历史版本、解析方式或标签问题，不能凭此认定gold错误；也不能把任意历史裁决默默配给2025版。

论文§2.2说明描述及解释由GPT-4o-mini根据包括gold在内的整份裁决生成。真实来源不等于公开输入未经答案条件化。原始裁决、商品事实与生成结果的逐条对应关系需要恢复。[原论文](https://arxiv.org/html/2509.18400v1)

## 具体Query与数据湖

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按冻结适用税则，对产品批量输出一个或多个HTS code；ATLAS需先恢复原始裁决日期及事实映射 | E：2025Rev15官方完整税则4,429页+官方JSON；对历史ATLAS是否适用未证 | R：18,654个生成问答记录，只可把user作为候选公开输入；assistant是私有标签/生成解释 | 应有原ruling ID、日期、商品原文、当时税则版本，当前副本未保留 | code及reasoning不能一并喂给判断器 |
| validation第0行：PET膜与PE膜层压的Polivac包装薄膜 | 同一E候选，但gold3920620000不在本版本表中 | user仅说两种材料层压并用于包装 | assistant额外说PET占60%、PE占40%；该比例不在user，不能从解释补成无泄漏输入 | 发布code3920.62.0000；具体版本和原裁决未核到 |
| train第0行：卧式注塑机与橡胶部件模具 | 机械与模具须分别归类 | 一个user同时问机器和模具 | 应有尺寸、用途等原始描述；assistant新增夹紧力220吨等信息 | 同行两个code8477.10.9015和8480.71.8045；不能强迫输出一个code |

## 类Python DAG

| 类python的DAG | 实际数值/操作 | 当前状态 |
| --- | --- | --- |
| `E = download_official('2025HTSRev15', 'finalCopy')` | 4,429页、1,485,640词 | 完成；与上轮JSON相同版本 |
| `R = load_three_splits()` | 18,254/200/200 | 完成副本读取，非原仓库校验 |
| `audit_versions(R, E); audit_overlap(R)` | test27行code不在E；train/test40个精确问题重合 | 已执行诊断，不能删掉这些行后称原benchmark通过 |
| `cases = restore_source_rulings(R); facts = separate_predecision_inputs(cases)` | 发布case ID/日期缺失 | 未完成；不从assistant复制缺失事实 |
| `codes = sem_map(facts, apply_frozen_hts)` | 集合或单项schema需冻结 | 未执行；派生任务不得冒充原任务 |

## 多种方法预期表

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| Polivac例不能在未经版本核验时要求命中旧code；实际输出未知 | 固定抽取材料→检索完整税则/章注→按条件判断→输出当前有效code或ABSTAIN | 同样不能凭缺失比例和日期可靠复作原裁决 | ==核材料比例和层压结构所需事实==→==检查适用版本与候选code==→缺失则ABSTAIN | `validate_version → extract_features → retrieve_notes → decide`，版本是输入契约 |
| 注塑机/模具例应允许两个输出；未运行 | 固定拆项→每项同资源检索/判断→集合聚合 | 同样输出集合，不预设比固定拆项更好 | ==识别同记录多个物品==→==分别核机器功能/模具用途==→判断→按原记录聚合 | `split_items → classify_each → validate_codes → aggregate_set` |
| E-only程序可能直接完成税则树遍历 | 完整E+任务一次生成固定批程序，允许索引缓存、复核和公开分支 | one-trace只有获得真实且完整示范后才能提取 | ==一条公开任务执行并记录工具证据==→提取→冻结→独立R | 不把生成的答案reasoning当真实Agent轨迹；比较完整构造及执行成本 |

标记的探索步骤仅是拟记录的外部动作；本轮模型调用0，未产出学习operator。HSCodeComp保留为优先补证路线：规则材料已齐备至官方完整税则，下一步是图像删除后的输入充分性；ATLAS先恢复原来源/日期，不能直接进入可行清单。
