# 第四十增量：RoBBR偏倚风险评估（四份主任务与具体原论文已核验）

**累计仍1/10，RoBBR暂未计入。** 原论文、完整作者仓库、官方543页手册与四份主任务JSON均已取得；另下载并检查一篇源试验PDF。已证明存在真实论文和同一偏倚定义下的百篇批次，但尚未证明该批次必须依赖复杂长环境，而非已给出的短定义。

| 来源 | 本次事实 |
|---|---|
| [RoBBR原论文](https://aclanthology.org/2025.emnlp-main.160.pdf) | 29页、11,944,896 bytes，已下载 |
| [完整作者仓库](https://github.com/RoBBR-Benchmark/RoBBR) | commit `5bfd2554a1d2691db3ff2ab6f06d6b7b6660cf40`；30blob Git SHA1全通过、ZIP CRC通过 |
| [作者HF数据](https://huggingface.co/datasets/RoBBR-Benchmark/RoBBR) | 冻结`690b5351baae2afb90a0911b496ca902108352c6`；Cochrane测试37,816,148 bytes、RR子集3,746,615、训练35,641,248已下载。Non-Cochrane 87,649,416 bytes已取得。四文件大小及可用LFS哈希全通过；没有下载另外SSR/SJS任务文件 |
| [官方Handbook5.1](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/archive/v5.1.0) | 完整PDF543页、7,818,762 bytes，SHA256 `edece244e697e48cab2f6c419c2abf485cead4f433607647200c63d4062f9460`；通过当前官方归档入口取得，未用5.2替代 |

手册含转载/检索系统使用限制；本轮仅本地来源审计，未对外发布原文或调用模型。代码MIT不自动覆盖论文、手册和数据资产的各自权利。SSR支持句是模型辅助推导的标注，不冒充独立专家risk标签。

## 实读统计

| 子集/任务 | 行数 | 独立DOI | 备注 |
|---|---:|---:|---|
| Cochrane主任务test | 906 | 127 | 77种完全相同bias+definition组合；多个偏倚不增加论文数 |
| Cochrane主任务train | 774 | 83 | 与test有6个相同DOI，不能直接当源实体隔离确认集 |
| RobotReviewer测试子集 | 99 | 69 | 是已有任务子集，不另计湖；没有bias_definition字段 |
| 随机序列生成，同一定义 | 122 | 120 | 定义210词；low82/unclear25/high15 |
| 分配隐藏，同一定义 | 122 | 120 | 定义185词；low63/unclear44/high15 |
| 选择性报告，同一定义 | 113 | 112 | 定义206词；low92/unclear16/high5 |

原始主任务是ID到对象的dict，而RR子集是list且缺定义。首版审计假设错误，已按实际schema修正，失败不计通过。全部标签数为行级。具体同一DOI `10.1016/s1473-3099(10)70187-0` 的选择性报告风险在两个review objective下分别unclear和low；不是直接的矛盾标签，说明记录单位必须保留综述目标/结局范围，不能简单按论文去重后随意选label。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按同一冻结RoB1规则，在各自明确的结局范围下逐篇判断选择性报告风险 | 官方5.1手册543页；当前每行定义仅206词，长章节带来的必要信息未验证 | 同一bias+definition组113条、112DOI，公开full_paper解析文本实际取得；尚未逐篇对源PDF核验 | PICO、review objective；个别判断可能需注册方案，现有全文是否充分待审 | low92/unclear16/high5行级；label及其他任务支持句不能给模型 |
| main_task_test_5，DOI10.5830/cvja-2016-035 | 选择性报告偏倚定义：需判断预定与报告结局；不能把“未见方案”直接等同high | 3,190词论文文本；南非结核性心包炎33人试验，秋水仙碱与安慰剂比较 | 综述目标是结核性心包炎治疗；原文提到主要结局为心包缩窄。尚未取得该试验完整注册方案 | 发布unclear，本轮未独立专家重标 |
| 同论文main_task_test_0 | 随机序列生成偏倚，定义210词 | 文中明确采用网络计算机系统随机分组 | 同一论文/目标，偏倚任务不同，不能算第二数据湖 | 发布low；说明不同偏倚要独立任务契约 |

| 类python的DAG | 具体数值 | 当前状态 |
|---|---|---|
| `scan(test).filter(exact_bias_definition)` | 选择性报告113行、112DOI | 已实读分组；保留objective/结局参数 |
| `group_by(source_trial).split()` | train/test相同DOI6个 | 仅DOI审计，未做同试验多论文或近重复审计 |
| `allowlist(full_paper, objective, factual_pico).join(protocol_if_needed)` | 示例全文3,190词，定义206词 | PICO为综述抽取信息，是否夹带评估结论待逐项审核；不能默认安全 |
| `sem_map(risk).sem_filter(risk == low).project(record_id).count()` | 113行参考low92 | 是数据gold计数，非模型预测；按DOI汇总须先定义多review语义 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| test_5参考unclear；未运行。unclear是风险标签，工具失败另记ABSTAIN | 固定提取预定/报告结局，读取同一手册；若允许公开方案则固定检索与对照，按证据作三类判断；允许共享规则缓存 | 相同参考，不预言比LOTUS准确 | ==确认review所关心结局==→==检查全文是否足以识别预定结局==→==必要时查公开注册方案并比较报告差异==→按冻结规则给风险及证据；不能读取gold解释补方案 | `ReportingBiasOperator(E_version, outcome_scope, prespecification_evidence, reported_results, discrepancy_rules, unclear, abstain)`；应比较仅E编译、短定义、固定检索、Coding Agent、批Agent和单轨迹提取 |

当前支持继续深入，尚不支持计入合格湖：短定义已可能覆盖决策规则；543页中哪些额外信息真实影响判断未证实，必要方案缺失和综述PICO来源也未审完。没有模型优势、准确率、成本或单轨迹提取结果。

原资产data/shared-environment-audit-20260908-v40；脚本、统计、下载哈希与cochrane-detail.json在artifact/evidence/shared-environment-audit-20260908-v40。下载session9057已正常结束；源试验PDF下载88960也已结束。旧的下载中记录由本次四份主任务核验替代。


## 完成后增量：478篇同任务及一个可追溯输入缺口

Non-Cochrane主任务实际2,489行、496个DOI，low1,465/high450/unclear574；完全相同bias+definition共7组。其中“不完整结局数据”478行、478个DOI，定义269词，low327/high90/unclear61。这是同规则批量，不是把7种偏倚相加冒充同任务。各review objective仍需作为逐条参数保留。

另已下载[源试验原PDF](https://link.springer.com/content/pdf/10.1186/s13102-021-00256-6.pdf)：11页、1,063,933 bytes，SHA256 `5cabe3721f2a2a7cc9f117f401d04e1125330824116493a13af6723a3189af5c`。PDF第4页Figure2已经渲染并人工式视觉检查。摘要写34人随机分组，图显示107人评估、随机前排除62人，剩45人随机（15/15/15），最后分析12/12/10人。不能把11名随机后退出者误作随机前排除。图中包含组间退出原因，WBV组有踝痛等原因；正文自述modified intention-to-treat及simple imputation。发布的full_paper有流程图标题，却没有图内这些人数和原因。

这验证了**源PDF与解析文本的信息不等价**，不能单凭文本任务失败推出Agent必要性。更完整输入、固定图像提取和E-only编译都必须作为对照。手册§8.13.2提供处理缺失结局的详细讨论，但269词定义已包含多数上层条件；目前未证明必须反复依赖长手册，也未独立重标原gold。因此维持候选、不计入1/10合格列表。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在冻结RoB1规则下，评估478篇试验在对应review结局范围中的失访偏倚，并输出高风险清单 | Handbook5.1完整543页，重点§8.13.2；同一定义269词；规则版本与每个原review的绑定仍需审计 | 478个DOI的已发布full_paper，属于真实试验报告；未逐篇下载源PDF | objective与允许的原文图表；本轮只补齐一个源试验PDF，不能称478篇PDF全部齐全 | low327/high90/unclear61，独立于预测；专家标注未逐篇重新裁决 |
| 具体main_task_test_910：慢性踝不稳WBV试验的失访风险是什么？ | 按组间缺失数量、原因与结局关系及插补适当性判断，不能固定“超过20%=high” | 发布文本5,477词，PICO为空；源PDF11页，流程图45人随机、34人纳入分析 | 15/15/15→12/12/10；图示退出原因与正文modified ITT/simple imputation要联合读；不把摘要34当真实随机分母 | 发布high；这是目标参考，不是本次预测或独立重标 |

| 类python的DAG | 具体数值 | 输入与输出边界 |
|---|---|---|
| `scan(non_cochrane).filter(exact_bias_definition)` | 2,489行→478行/478 DOI | 同一risk定义；objective保留，不跨bias混算 |
| `sem_map(extract_attrition_facts, paper, figures)` | 示例随机45；三组15/15/15；分析12/12/10 | 源PDF核对值，不是模型实测。478篇图表覆盖未完成 |
| `sem_map(assess_risk, E, facts, outcome_scope)` | 示例目标high，输出low/high/unclear加证据；执行失败ABSTAIN | risk是标注任务；新facts字段没有独立全量gold，不冒充已标注中间步骤 |
| `sem_filter(risk == 'high').project(id).count()` | 参考90/478；示例应入清单 | 私有label评分整条DAG；90是gold聚合，不是LOTUS或Agent输出 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 示例以high为参考目标；全批high清单参考90；未运行，不能承诺达到 | 同等输入上固定提取流程图/正文人数及退出原因→按缓存的E规则判断→筛选聚合；固定程序可核查摘要与图矛盾、分支重读与ABSTAIN | 同一high目标，不预言更准确 | ==定位手册缺失数据规则并缓存==→==发现摘要34与图45分母差异，回查随机前后边界==→==按组关联退出原因、结局及插补方法==→判风险→筛选聚合；这是预期可观察操作，不是已获得轨迹 | `AttritionRiskOperator(E_version, outcome_scope, extract_flow, reconcile_denominators, reason_outcome_link, imputation_check, risk_rules, evidence, abstain)`；同E规则编译/B2固定工具/B3 Coding Agent/B4批Agent/B5单轨迹提取公平比较 |

新增收据：`attrition-example-audit.json`、`example-download.json`。没有模型调用、Agent轨迹、提取算子或准确率/成本实验；没有新增工程测试（0），数据脚本审计成功不等于科学有效性验证。
