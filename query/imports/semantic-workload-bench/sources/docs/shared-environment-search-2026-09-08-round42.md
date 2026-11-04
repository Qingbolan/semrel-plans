# 第四十二增量：ECtHR Article6负例语义与历史规则补证

**累计仍1/10；本轮补充证据，未认定第二湖。** 上一轮有真实数据/文档进展；本轮复用第4–5轮已经下载的原论文、完整ECtHR-PCR和LexGLUE作者仓库、Zenodo裁决归档，不重下大包。版本与哈希沿用[第4轮](shared-environment-search-2026-09-08-round4.md)、[第5轮](shared-environment-search-2026-09-08-round5.md)。NAACL2021独立模型代码仓库仍未定位，LexGLUE仓库不冒充它。

## 本轮实读及边界修正

实际重新读取11,000条裁决与15,729条PCR记录，以申请号去末尾版本字母+精确日期唯一关联。2018年后Article6组仍275案，210实际违反、65未列违反。逐个抽取65负例的Article6结论候选并初筛：40条命中明确no violation表达，7条命中程序性表达，18条需要人工复核。210正例中150条命中明确violation固定表达，60条未命中。**这是启发式候选统计，不是40/7/18个已完成独立重标；非命中不等于标签错误，引用先例或当事人主张也可能误命中。** 脚本保留完整候选段落以便继续逐案核对。

三个实读例：

- Ciocodeică v. Romania，27413/09：当前判决§116明确Article6没有违反。
- Čeferin v. Slovenia，40975/08：§79明确Article6申诉不可受理；Article10的损害赔偿不能误作Article6胜诉。
- Libert v. France，588/13：§54–56处理Article6，认为有关审判公正的指控未获支持，按Article35拒绝受理。不能把这个负例表述成已经完成Article6实体审理并认定合规。

因此可以清楚定义“法院是否认定Article6违反”的Boolean任务，FALSE表示未认定，而不表示行为合法；但若目标是纯实体合规判断，65条不能直接当作同质阴性。此前第5轮要求先做独立确认/实测E增益再计可行，属于过强实验门槛：**可构造性不必先证明Agent优势**。本轮继续保留候选的原因是案例证据世界和标签核对尚未完成，而不是没有模型胜出。

长E有具体内容用途：冻结库内Ramljak v. Croatia（5856/13，2017-06-27）§29–39讨论法官亲属在对方律所工作、是否参与案件、是否披露以及程序保障；不是“只要亲属关系就自动回避”。该先例真实早于Nicholas v. Cyprus（63246/10，2018-01-09），也在下载库中。Nicholas当前§27–39另涉及国内救济可获得性和是否用尽，说明仅提供267词facts并引用亲属关系先例，未必足以完成整个案件判断。当前案law只能用于private审计，不能拿其事后解释补公开输入。

本轮经web实际打开[官方历史公约](https://rm.coe.int/1680063765)，确认是Protocols11/14版本的13页文本；与当前Protocols15版本区别明确。直接本地下载返回HTTP403，未保存PDF，不写成已下载。正文足以定位Article6和35，但该13页本身不是长环境证明；共享复杂部分仍为冻结先例库。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 对275条Article6被诉案件，预测法院是否认定违反，输出对应案件清单 | 冻结2018年前12,480份先例；68,031,172空白分词 | 275份裁决库facts，已下载并唯一关联；不含当前案law | 公约历史版本已web核验未本地取得；个案国内法/救济材料充分性未完成 | 210认定违反/65未认定；后者包含实体与程序结果 |
| Nicholas，63246/10 | Ramljak等历史先例在完整E中，不用当前gold选定的片段替代全环境 | 267词facts：法官亲属与对方律所关系 | 先例要求核关系性质、披露与程序保障；当前案另有国内救济争议 | TRUE，先前已核当前§66；本轮不重复声称新重标 |
| Čeferin，40975/08 | 相同E及公约Article6/35规则 | 事实与程序流程；应区分Article10和Article6 | 相关法官实际是否参加裁决需核对；不能只看其他条款获赔 | FALSE，因为Article6不可受理；不是Article6实体合规gold |

| 类python的DAG | 具体数值 | 解释 |
|---|---|---|
| `freeze(PCR,date<'2018-01-01')` | 12,480条共享E | 研究者冻结，原PCR候选库本来随案件日期变化 |
| `unique_join(verdicts,PCR).where(alleged_article=='6')` | 704关联案→275个目标案 | 保留源映射供private审计，不依gold删除困难案 |
| `sem_map(issues_and_procedure,facts).retrieve(E).sem_map(violation_finding)` | 目标210 TRUE/65 FALSE | 中间争点/程序字段没有全量独立gold；终点Boolean有源标签 |
| `sem_filter(finding).project(id).count()` | gold参考210；模型输出未知 | 不把FALSE合计65描述成实体合规65 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| Nicholas目标TRUE、Čeferin目标FALSE；均未运行 | 固定争点与程序要件抽取→同E检索与证据复核→判断是否认定违反；可共享索引、规则缓存和条件分支 | 同一参考，不预言更准 | ==辨别诉称条款与实际争点==→==检查受理/救济前提==→==从共享E核亲属关系、参与、披露和保障规则==→证据充分则输出，否则ABSTAIN | `Article6FindingOperator(procedure, issue, shared_index, precedent_applicability, factual_coverage, decision, abstain)`；必须与E-only编译、固定工具、Coding Agent、批Agent比较 |

产物：`artifact/evidence/shared-environment-audit-20260908-v42/audit_outcomes.py`；negative-screening-private与positive-screening收据；完整current-law核验输出在`data/...-v42/outcomes-private.json`，不能挂载到被测系统。本轮下载失败收据保留。新工程测试0、模型调用0、作者代码执行0；无确认split或性能结论。
