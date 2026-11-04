# 增量10：HSCodeComp前8项的事实—规则充分性审计

**完整通过仍0/10；本轮为优先候选的输入审计，没有新增数据湖。**复用已下载的原论文、完整作者仓库、官方JSON及4,429页税则。本轮没有下载新论文；不把资料展开脚本称为学习算子。

## 范围与方法

固定读JSONL前8项（task_id 0–7），先展开公开标题/属性，再读官方第71章注和相应税则路径，最后核源gold。它们全属首饰，**不是随机代表样本**。其中0/1的gold已在前轮看过，其他项也没有冻结独立预测；所以这是开发审计，不是盲测、专家重标或模型准确率实验。不能从8项外推632项的充分性比例。

官方来源为[2025 Revision15完整税则](https://hts.usitc.gov/reststop/file?release=2025HTSRev15&filename=finalCopy)。第71章注9定义相关首饰范围，注11限定7117并排除自然/养殖珍珠和天然/合成/再造宝石等材料。7116.20.05.00还要求每件价值不超过40美元。这里是对冻结历史文件的实验解释，不对现实商品提供新的海关裁定。

## 逐项观察

| task_id | 公开事实 | 源gold | 能支持的判断与尚缺条件 |
| --- | --- | --- | --- |
| 0 | 龙形吊坠，Copper/Metal，141 CNY，1件 | 7117199000 | 公开文字支持普通贱金属饰物路径；未做独立实物核验，不能声称排尽所有未描述材料 |
| 1 | 标题Natural Purple Keshi Pearl，属性Pearl/Copper，26 USD | 7116102500 | 可据珍珠声明排除7117；10位gold的Cultured与标题Natural之间需明确解释/来源，不能把营销词直接当培育方式证据 |
| 2 | Brass and Zircon/cubic zirconia；Metals Type却写None；4.2 USD、4件 | 7116200500 | 合成宝石声明支持7116方向；字段存在冲突，需冻结事实优先级，不能从gold反推哪列可信 |
| 3 | Enamel Badge/Brooch，Zinc Alloy，25 CNY | 7117199000 | 文字对贱金属装饰物的支持较强；分类核验仍须考虑适用排除项，不是图片一缺就自动不可用 |
| 4 | Ring，Zinc Alloy，cladding/inlay None，2.5933333333 USD | 7117199000 | 文字明确排除部分材料歧义，适合作为后续文本充分性审核候选，不直接升格专家确认 |
| 5 | Rings，Brass+cubic zirconia，cladding Others，63.048 CNY，标题2Pcs | 7116200500 | 需解释包/件计价及cladding字段，不能默认为无贵金属包覆；价格字段不是自动等于法定估价 |
| 6 | Beimu项链耳饰套装，Stainless Steel，4.9666666667 USD | 7117199000 | 贝母与珍珠不是可随意互换的事实；需保留名称和附加材质，不可只抓Metal关键词 |
| 7 | Crystal/Rhinestone套装，Zinc Alloy，65.6 CNY | 7116200500 | Crystal可能指玻璃或宝石，公开属性未充分消除这种材料歧义；两种解释可能改变7117排除条件 |

**本次重要判断：不能把“缺图”整体判作全部样本无效，也不能把“有材质字段”整体判作充分。**需要具体属性和决定条件的逐项对应，尤其天然/养殖、玻璃/合成宝石、包覆/电镀、按件估值等区分。当前审计没有把猜测转成新gold。

## 一个实际资源构造问题

税则中有`htsno=''`的父行，它们并非无用空白：例如7117199000的完整缩进祖先包含“Of base metal, whether or not plated with precious metal”。仅用数字code前缀查父节点会丢失该条件。仓库`hts_tree.json`中7117199000的desc只有Other；本轮不宣称所有作者工具必然误判，只指出不能把这个叶节点单独交给语义判断。

新增[可复算展开脚本](../artifact/evidence/shared-environment-audit-20260908-v10/audit_paths.py)按官方JSON原顺序与indent保留有/无编号祖先，输出[三条实际路径](../artifact/evidence/shared-environment-audit-20260908-v10/tariff-paths.json)和[来源统计](../artifact/evidence/shared-environment-audit-20260908-v10/statistics.json)。只是离线材料构造，未改现有运行器、未执行作者工具。

## Query与数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按冻结税则判断批内商品是否属于7117仿首饰；10位原任务须另行评分 | E：官方Rev15全税则4,429页，含第71章注9/11及价值条件 | R：632条真实商品记录；本轮顺序开发检查8条 | 公开可计算资源：保留无编号父行的分类路径；不能用gold选择唯一路径提供给模型 | 原hs_code；本轮8项4个7117、4个7116，仅作开发对照 |
| 对task7，Crystal套装是否应排除7117 | 章注11关于宝石/珍珠/贵金属的排除条件 | Alloy/Crystal/Metal与标题Rhinestone；没有确定玻璃还是宝石的声明 | 缺失的真实材质证据不能由Agent凭空补足 | 原标签前4位7116；不足以证明当前公开文字唯一决定该标签 |

## 类Python DAG

| 类python的DAG | 具体数值 | 输出/限制 |
| --- | --- | --- |
| `paths = expand_by_indent(official_rows)` | 35,950源行 | 构造所有非空code路径，保留无编号节点；不读取gold |
| `review = read_public_fields(records[:8])` | 8条首饰，非随机 | 本轮手工开发审计，非运行结果 |
| `facts = sem_map(x, material_function_value_schema)` | 包括material_kind、cladding、unit_value等 | schema拟议；缺失值保持UNKNOWN，不借private解释补齐 |
| `candidate_paths = retrieve(E, facts)` | 多条候选都应允许 | 三条导出路径仅审计例，不是gold oracle检索 |
| `selected = sem_filter(x, E, heading_7117)` | 原gold前缀可派生布尔值 | 未执行；不能拿8条当确认或宣称方法胜出 |

## 多种方法预期表

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| task4目标TRUE；是否正确未运行 | 材质/用途抽取→完整祖先路径与章注→sem_filter；固定程序同样可以排除不适用类别 | 同目标TRUE，未预设改进 | ==核Zinc Alloy与cladding/inlay None==→==读取7117条件及排除项==→输出证据 | 属性schema+规则条件检查；无需每行重建同一税则树 |
| task7若仅据公开材料，可能需要ABSTAIN；不能强行保证命中原FALSE | 固定证据充分性检查也可识别Crystal歧义；允许同资源补证工具 | 同样可ABSTAIN；这不表示Agent在标签评分更优 | ==区分玻璃仿石与合成宝石==→查允许公开材料→仍不能区分则结束 | `resolve_material → evaluate_exclusions → abstain_if_underdetermined` |
| 叶节点Other不足以独立支持判断 | 固定预处理完整父条件是强基线，不能故意让LOTUS只看叶节点 | 应使用相同展开路径 | ==检查命中叶节点的无编号父行==→比较完整条件 | 保留原缩进树、引用定位、缺字段分支；这是共享预处理，不等于轨迹学习 |
| E-only编译可能足够 | 从官方E直接生成条件程序，冻结 | 单轨迹提取尚未执行；需与E-only及固定工具程序比较 | ==一次真实执行访问条件与证据==→自动提取→独立批次 | 不能因为程序有分支就声称需要Agent；计入预处理/提取/复核成本 |

本轮局限：没有新增专家标注、没有环境增益实验、没有独立确认。完整10位任务的开放属性和估值条件仍待核，632条不能整体标成充分。后续应优先找保留原事实的裁决来源，同时保留HSCodeComp作为结构已接近、可明确逐项审计的候选。
