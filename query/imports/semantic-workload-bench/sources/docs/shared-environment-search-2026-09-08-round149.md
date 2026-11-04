# 第149轮：AMELIA意大利VAT判决，完整原数据与三任务求证

未qualified，仍8/15。新独立来源，不是同名多语模型AMELIA。上一轮148原论文/完整规则仓库核验有进展，本轮避免Zenodo依赖，已下载本来源原论文、完整GitHub仓库和完整HF发布。

[原论文](https://aclanthology.org/2024.clicit-1.124.pdf)266128bytes，SHA256 `f490fa55d1b6a024ac768f1d31024df825f980244bde2a9805a4aa45058e9a6e`。[作者GitHub](https://github.com/adele-project/AMELIA)commit `76868635e15c9266fdc359f9f11b41dd4d9a6bcc`，ZIP2165194bytes476membersCRC通过，SHA256 `571055e0855db98d74e469e6346c4ad2fe25b9f04b08e1fffb8d82161f0f2fd5`。[作者HF](https://huggingface.co/datasets/nlp-unibo/AMELIA)revision `93765c5d15791aca372eeec0db95c957adbfc3c8`，全部5文件下载含3Parquet/README/.gitattributes，HF元数据CCBY4.0；部分原判决来自大学许可数据库，不把该标注许可外推为任意上游再分发授权。

原件data/shared-environment-audit-20260908-v149；downloads.json/hf-downloads.json/audit.py/audit.json/hf-audit.json/parity.json在artifact/evidence/shared-environment-audit-20260908-v149。没有运行作者模型或论文实验。

## 全量实际核验

两目录data与data_with_arg_links各235 XML，共470文件，但逐文全文相同、去除5种关系字段后的标签全相同，不计两个湖。235个全文哈希不同不代表已完成近重复/同案审计。每版2910prem、401conc，共3311组件。235个XML字节直接ElementTree.parse失败；先显式UTF8 decode再fromstring全部成功，原件声明utf8相关解析问题不可直接说成坏标注。未改任何上游字节。

HF：train2108组件/135文档，val609/44，test594/46，共3311组件225文档；三个划分文档名交集均0。XML多出的10份均0组件，不得将它们当全篇负例。按Document/Chain_id连接，所有HF标签与XML的Component/Type/Scheme集合一致，0缺失/冲突。去两端空白仍有3165文本不同，折叠空白后3114不同；样例Id0等去掉末尾句点，但未穷举全部变换，不能宣称文本字节相同或完整文本变换已核验。HF是给定组件分类，不是端到端找边界。

类型：F1572、L1018、L|F314、F|L6（后两种相同集合，共320双类型）。scheme多标签；1596个prem无S字段，23个为空；有1个Itpr|Acon超出论文五scheme定义，不自动更名/删除或当标准类别。关系版五字段SUP/ATT/REPH/SFF/INH按竖线拆分3185目标token，其中22不能解析到同文ID（含空串），不是3185条已验证独立关系。完整关系语义和标注来源说明不足，不作为第四个现成gold任务。

共享环境缺口：论文§3.2说基于Demosthenes的指南为意大利判决改编并迭代，但完整仓库无PDF/单独指南、HF只有短定义和数据。不能把旧英文指南直接当此版本。论文现有三分类prompt和五scheme定义均短；标签规范复杂性和长E必要性尚未求证。研究的是论证分析，不是判断VAT违法或税款应否返还。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 给定判决论证组件，判prem/conc | 225份有组件的原判决；公开上游给定span/原文上下文 | 分类口径，完整改编指南未找到 | 组件边界明确给定，不算模型发现 | HF3311组件：2910prem、401conc |
| 给定prem判断事实/法律/两者 | 同一组件和上下文 | Type集合定义 | 法律前提可引用法条/判例，不能所有有引文都自动一类 | F1572、L1018、F+L320 |
| 给定法律前提，标多种论证scheme并聚合 | 同一判决组件关系 | Rule/Prec/Class/Itpr/Princ规范；含1个未解释Acon | 官方原text允许检索邻接上下文，不能公开gold关系作oracle | 样例2015_1360…的A2=prem,L,Prec；A3=prem,L,Itpr |

| 类python的DAG | 具体数值 | 上下游边界 |
| --- | --- | --- |
| `given_components.sem_map(component,E).filter(prem).sem_map(type,E).filter(has_L).sem_map(schemes,E)` | oracle路径3311→2910→1338含L前提 | oracle数量仅说明目标；级联执行须评上游漏筛对后续覆盖影响，不能只报幸存者 |
| `schemes.groupby(document).count_by_scheme()` | 2015_1360 A2引用最高法院判例目标Prec；A3判断该判例不具决定性目标Itpr | 多标签计数不能等同组件数；原始XML有完整上下文，选定标签由private提供 |
| `validate_graph_refs()` | 3185引用token、22无目标，且5种关系定义未闭合 | 构造诊断而非已实现语义任务；不自动补a23大小写或猜A2A15应拆分 |

模型均未运行，以下仅目标和设计。具体样例在audit.json保留原文和标签。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| A2目标prem/L/Prec，实际输出未测 | 固定串联三sem_map，以同一公开定义及段落上下文分类；五scheme多标签 | 同一目标，不预设更准确 | ==读取类别集合并确认前提类型可双标签==→==核对最高法院引文和当前论证用途==→输出Prec | `ArgumentClassifier(E_version)->component,type_set,scheme_set,evidence,status`，显式适用范围，未生成实现 |
| A3目标prem/L/Itpr，实际输出未测 | 对“被引用决定并非决定性”的上下文做同资源解释，不能只按没有引文字面判否 | 同一目标Itpr | ==读取A2与A3的承接关系，核对Itpr具体定义==→若规范无法解释则记录未决而非借gold补规则 | 可固定邻句检索+分类；未取得完整规范时不声称探索已解决歧义 |

必须比较同资源固定检索、Coding Agent、E-only编译和整批Agent，官方短定义本身可能已经足够，不能为轨迹学习人为加复杂度。本轮三个任务和真实数据匹配已有证据，但共享长规范缺口仍在；不纳入第9个。后续优先寻找完整规范可直接下载的新来源，AMELIA仅保留可求证的多任务候选。论文中的法律专业知识不能自动视为冻结E。
