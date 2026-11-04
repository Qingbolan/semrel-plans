# 医学筛选、试验匹配、保险申诉：增量复核219

本轮复核已下载的原论文、完整作者仓库及实际数据证据，不重复将下载当作新发现。重新计算9个本地资产的大小与SHA256，全部匹配原收据；[本轮校验](../artifact/evidence/shared-environment-audit-20260914-recheck219/integrity.json)。重新打开三个官方仓库。没有执行模型、重跑旧数据构造或新增标签。

结论：CSMeD具体review为Partial，TrialGPT和HICRIC发布版本不满足目标，Reject仅针对本研究结构。后两者不进入可行清单。三个来源不是三个新合格数据湖。

## 入场表

| 数据湖 / Benchmark | 论文 | Repository | Shared Environment E | E规模/类型 | Batch Records | N | Fixed Query | Gold | Gold类型 | Environment Necessity | 是否天然Batch | 是否公开可下载 | Verdict |
|---|---|---|---|---|---|---:|---|---|---|---|---|---|---|
| CSMeD，CD001431.pub5 | [原论文](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf) | [作者库](https://github.com/WojciechKusa/systematic-review-datasets/tree/b30e9739939f52b1e799295138791f1fd5b002a5) | 同一review的criteria_text | 1039词原始字段，不是30页protocol | 有main_text的候选出版物 | 171 | 按该review筛选文献 | 68纳入、103排除 | 原筛选决定/排除原因 | 比较组规则确实影响纳入；长E必要性没有证据 | 是 | 原论文339308 bytes、完整库33644877 bytes已下载 | △ Partial fit |
| TrialGPT，反向按trial分组 | [原论文](https://arxiv.org/abs/2307.15051) | [作者库](https://github.com/ncbi-nlp/TrialGPT/tree/1b3242cd50c153a9c324661d4a0bd94fc68a4226) | 各trial注册标准；同版本完整protocol未取得 | 最大组示例82词 | 合成/专家编写患者描述 | 最大76，中位1 | 固定trial逐患者筛选 | 最大组76个全0 | 检索相关性/资格标注，非真实入组决定 | 标准相关，但长环境不存在于该示例 | 原生是患者→试验检索；本方向由反向分组诊断 | 论文2175100 bytes、完整库26996251 bytes已下载；库外全注册库未全下 | ❌ Reject |
| HICRIC / IMR Appeals | [原论文](https://drive.google.com/file/d/1vsu0Ns6R6AeTX4-Hf2OdYqRvHD4yNm4y/view) | [作者库](https://github.com/TPAFS/hicric/tree/37d88ab02833862c3f0b0ad4d0b3d52a96a705b2) | coverage材料未绑定case的适用保单 | 3661材料行、约429.6万词，非统一适用保单 | 申诉发布行，部分同案件多摘要 | 73987；同E数未知 | 按适用保单判断申诉是否撤销 | 34666 Overturned、39321 Upheld | 申诉决定；sufficiency另为模型伪标签 | 缺policy_id/version，不能证明所给E适用 | 真实申诉反复发生；同E公开batch未建立 | 论文311018 bytes、完整库1549071 bytes、完整appeals两split及coverage分区已下；非全HICRIC | ❌ Reject |

计数均继承实际源文件审计，本轮只复核资产完整性。详细逐行统计及复算入口：[CSMeD第2轮](shared-environment-search-2026-09-08-round2.md)、[TrialGPT第13轮](shared-environment-search-2026-09-08-round13.md)、[HICRIC第6轮](shared-environment-search-2026-09-08-round6.md)。

## 一个真实、可以解释，但尚不合格的例子

CSMeD能纠正“只有摘要”的过度概括：这个review确实发布了171篇解析全文。但有全文不解决共享协议偏短、原辅助材料可能缺失的问题。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 数据湖数据4 | Gold Output |
|---|---|---|---|---|---|
| CD001431.pub5：返回应纳入文献ID | metadata中的criteria_text，1039词 | CSV中171条document_id/title/abstract | main_text共766375词 | 未取得完整原始决策辅助附件；不填成已有 | 68个ID |
| 判断CD001431-bib-0433 | 同一比较组规则 | 前列腺筛查试验 | 多媒体工具与含相同知识的有声手册比较，全文4861词 | 两组均为决策辅助工具的描述 | excluded；源原因注明两种辅助工具比较及更新后的排除 |
| 判断CD001431-bib-0096 | 同一完整criteria字段 | 前列腺增生试验 | 112名男性、33诊所；决策辅助对常规管理，全文4680词 | 112为试验人数，不是论文batch数 | included |

实例原论文：[0433](https://doi.org/10.1016/j.pec.2008.07.033)、[0096](https://doi.org/10.1136/bmj.323.7311.493)。已读的实例全文来自作者发布main_text，不声称逐篇另下载PDF。下表的中间结果是基于源文本的解释，只有最终decision及排除原因是原gold。

| 类Python DAG | 具体输入值 | 中间结果示例 | Gold |
|---|---|---|---|
| `R=scan(csv).project(id,title,abstract,main_text)` | 171行 | 公开列allowlist；decision/reason隐藏 | 不参与运行 |
| `facts=R.sem_map(extract_trial_facts,E)` | 0433与0096全文 | 比较组分别为另一辅助工具、常规管理；其余条件也须检查 | 中间facts没有新增人工gold |
| `labels=facts.sem_map(eligible_under,E)` | 共享review标准 | 0433触发比较组排除；0096仍需满足全部条件 | False / True |
| `ids=labels.filter(True).project(id); count=len(ids)` | 171条逐项结果 | 正确清单68项 | 68个具体ID及count68 |

scan/project/filter/count是普通关系算子；事实抽取和按E判断是语义算子。决定性的“另一种决策辅助工具”不是字符串不等于usual_care；不能以关键词替代语义事实。缺证据必须按冻结协议报告，不能默认为exclude。

## 按要求横向推演

**全表未实测。** True/False为目标，不能把它们写成LOTUS或Agent已输出的结果。LOTUS表示固定语义调用流程，不对某个未锁定版本的API行为作承诺。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/核验步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 关键算子目标：0433 False、0096 True；实际质量未知 | 普通scan→固定全文证据提取→LOTUS判断比较组及资格→普通project/count | 同一目标，可能因附件缺失ABSTAIN；不预设更准 | 固定外层DAG→==定位E中比较组定义==→==查论文方法中的两组材料==→返回资格及证据 | `TrialFacts → ComparatorType → Eligibility`，每项附来源位置 |
| 整任务目标：68个正确ID；实际未知 | 一次解析E→每篇sem_map事实→sem_map资格→过滤聚合；允许固定检索、补读和缓存 | 同一目标；同资源下是否改善未知 | ==读取review版本/规则==→建共享索引→逐篇==按缺失字段检索方法与附件==→判断→普通清单/计数 | `RuleGraph(E_digest)`、`EvidencePlan(field)`、`evaluate(paper)`；明确预算和ABSTAIN |

| 方法 | 预期结果 / 风险 | 预期执行过程 |
|---|---|---|
| LOTUS关键operator | 比较组误分类可能造成false include | 同资源固定事实提取后，仅资格语义节点交LOTUS |
| LOTUS完整任务 | 可完全正确，也可能漏证据；未测 | 固定共享E解析、全文检索、事实提取、资格判断、聚合 |
| Agent关键operator | 能补查比较组，但无法恢复未公开附件 | ==查规则例外==、==核两组材料性质==，其余DB算子固定 |
| Agent完整任务 | 不能从合理流程推出质量或成本优势 | ==核版本==→共享索引→逐篇==补读缺证据段落==→输出标签和证据→聚合 |
| 可能的冻结结构 | 是候选结构，没有从真实轨迹提取 | 规则图+事实schema+按字段检索程序+终止条件；不得写死示例ID |

## 复用判定与十问

| 层次 | 具体可复用内容 | 当前证据 |
|---|---|---|
| Environment-only `f(E)` | 年龄、设计、干预、比较组及例外规则图 | 短E直接编译是强基线，未见必须先执行的理由 |
| Per-record `f(x,E)` | 找方法段、提取事实、判断全部条件 | 固定工作流即可表达；每篇的事实仍要重新读 |
| Group-specific | 辅助工具互比、常规管理对照、材料描述不足等分支 | 只是分支假设，未测K、覆盖或跨批收益；不能称已发现中间复用层 |

| 问题 | CSMeD该review |
|---|---|
| 1 q | 按冻结CD001431.pub5筛选文献 |
| 2 E | review metadata中的原始criteria |
| 3 复杂度 | 1039词，含非规则内容；长protocol未取得 |
| 4 x | 一篇出版物的title/abstract/main_text |
| 5 N | 171出版物，未完成试验实体去重隔离 |
| 6 y | included/excluded及排除原因，68/103 |
| 7 为何x不足 | 纳入取决于review特定比较组约定；这不证明需要长E |
| 8 探索什么 | 比较组定义、更新规则、方法段及材料充分性 |
| 9 复用什么 | 规则解析、证据字段、条件检查程序；族分支仅假设 |
| 10 是否超越普通分类/RAG缓存 | 未证明。短E编译+固定检索是必须保留的强对照 |

本轮没有使正式Strong数量增加。UDRP另有真实长规则适用依据，但其回顾性输入限制仍保留；不能借医学/保险的大总行数加强UDRP的科学有效性，也不能将真实policy任务存在等同于轨迹学习优势成立。
