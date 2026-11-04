# 对抗搜索：研究严谨性与价值审计

时间：2026-09-05，Asia/Singapore。角色：研究攻击方；与候选发现方、真实输入攻击方交换了具体攻击。范围：公开原始论文/官方代码与数据卡、现行仓库协议及近期阴性结果。没有模型推理、数据集执行、完整新数据下载或研究确认；本文件是进入实验前的审计。候选材料被阅读后属于开发侧暴露。没有更改现有实验结论。

## 1. 判定对象分三层

固定外层 DAG 的复杂语义步骤可以由固定程序实现。固定推理、检索或规则编译有效，不是淘汰环境的理由；它们是必须接受的强基线。当前需要分别回答：

1. **环境成立吗？** 原始输入、任务定义、允许资源与独立 gold 能否形成同一可重复批任务？
2. **质量差距成立吗？** 同一完整输入、同模型的直接语义调用是否确实不足；公开资源或计算是否纠正关键错误并改善下游？
3. **单轨迹方法有增量吗？** 相对于同资源固定程序、无轨迹 Coding Agent、查询重写及简单轨迹摘要，单次真实业务执行的信息是否带来更可靠或更便宜的可复用实现？

第 1 层失败，不能花模型预算制造漂亮比较；第 2 层通过而第 3 层失败，仍是有效环境和有用阴性结果。

| 攻击 | 触发与逻辑 | 最低反驳证据 | 性质 |
|---|---|---|---|
| 缺必要规则制造差距 | 企业承保规则、trial 纳排标准决定任务本身；仅凭常识不能定义正确答案 | 所有方法获得完整任务规则；无规则条件仅作为信息消融 | 比较设计可修复；若规则不可获取则当前构造阻断 |
| 只增加预算 | Agent 多轮且固定法一次，不足以归因探索 | 同预算固定分解/复核/检索，另报质量—成本曲线 | 可修复 |
| 给 Agent 更强感知模型 | 工具输出的改进可能全部来自独立检测器 | 固定程序可访问同工具；分开报告工具替换与策略选择 | 可修复 |
| gold 自相矛盾或自动生成 | 标签权威声明不能替代实例核查 | 独立人工/可执行规则审计，冻结争议处理；不让测试预测决定改标 | 当前标签不可靠时阻断；可重新构造 |
| 伪重复批量 | 多个 QA、pair、时间参数不是独立源实体 | 先冻结业务谓词，再统计原图/患者/报告/交易重叠；按实体划分 | 可修复；无足够共享任务则降为工具测试 |
| 改了任务 | 排名、初筛、最终承保/入组不是同一 gold | 明确 sem_map/filter 的输出与 UNKNOWN，复现原评分；新任务另标注 | 可修复或构造阻断 |
| 关键步骤没影响下游 | 只减少格式错误或使引用合法 | 冻结下游关系；以 gold 替换语义中间结果估计可改善上限，报告清单和聚合 | 可修复 |
| 轨迹只是装饰 | 手册已完整表达程序，无轨迹可直接生成同代码 | 同模型同预算 task+E/no-trace，trace-summary、simple replay、单轨迹提取配对 | 方法价值可能被否证，不淘汰环境 |
| 搜索幸存者偏差 | 反复挑失败数据、示范或指标 | 保存所有候选/运行/淘汰；开发挑选后冻结新实体确认；示范失败计费 | 可修复，旧曝光不能撤回 |

## 2. 必须正面对比的最近邻

**LOTUS 的传统和当前实现需要分开。** 当前官方 `sem_map` 文档含 few-shot 与 reasoning strategy；当前 agentic operators 提供工具、批处理及共享上下文。锁定传统版本及其 `sem_map`/`sem_filter` 能测试直接语义调用，但“LOTUS 不会用工具”不再是系统级事实。[sem_map](https://lotus-ai.readthedocs.io/en/stable/sem_map.html)、[agentic operators](https://lotus-ai.readthedocs.io/en/latest/agentic_operators.html)。本次未安装/运行最新版，文档可用性不等于本地适配成功。

**DocETL/MOAR 已覆盖重写复杂语义步骤和质量—成本优化。** DocETL 将数据/任务分解作为提高文档处理质量的方法；MOAR v4（2026-04-01）进一步全局搜索多目标重写。仅展示多步固定推理胜一次 LLM，不足以说明新方法价值。外层 DAG 固定是本任务控制变量，不应因此禁止比较器在语义节点内部生成等价分解；若无法保持业务语义，应披露适配边界。[DocETL](https://arxiv.org/abs/2410.12189)、[MOAR v4](https://arxiv.org/abs/2512.02289v4)。论文数字是作者实验，不是本地增益或跨任务可直接引用的基准。

**从执行经验诱导 workflow 也已有最近邻。** Agent Workflow Memory 从经验提取可复用流程指导后续动作；其网页任务设置不同于固定批关系，但不能把“轨迹→复用”本身当新贡献。这里待检验的是一次业务轨迹对冻结算子的独立价值、质量保持和包含构造成本的摊销，而不是换一个名称。[AWM](https://arxiv.org/abs/2409.07429)。

最低方法比较：完整输入直接语义调用；同资源固定分解/工具；一次 Coding Agent 生成批程序；Data Agent 允许批内共享；同轨迹摘要/重放；单轨迹提取；无轨迹提取。DocETL/MOAR 和当前 LOTUS agentic 在适用任务作为系统最近邻，版本/优化数据量/预算单独披露。手写规则程序可作为能力上限，但其人工构造成本未知时不能写成零。

## 3. 对候选的具体裁决

### TrialGPT：保留到构造审计，尚非 Agent 优势正例

官方包含 183 个合成患者，超过 75,000 个 patient–trial 标签；提供标准分解、逐 criterion 判断和 trial 排名流程。多对关系不等于同数量独立患者，已有固定分解必须是强对照。[官方仓库](https://github.com/ncbi-nlp/TrialGPT)。

攻击：固定某 trial 筛 patients 才接近同一手册批判别，但原标签覆盖、独立患者数量与缺失事实语义需核查；反过来固定患者搜 trials 是另一个参数化工作负载。真实试验文本不把合成患者变成真实病历。不能用外部知识补出未记录的检查/治疗事实，UNKNOWN 必须保留。不能把 TREC 相关性分数直接变最终可入组 Boolean。

最低反驳：发布固定 trial/任务 family 的标签覆盖矩阵和实体数；核对至少一个完整患者→criterion→trial 的输入、标注与聚合；固定同资源 criterion 分解和 Agent 比较；只在错误来自证据关联/规则组合而非缺失临床事实时推进。状态：可修复；若共享 family 没有足够已标注患者则暂停该构造，不否认原 ranking 任务。

### DABstep：业务批处理贴近，局部 gold 和信息条件尚未解决

官方说明业务场景来自 Adyen 任务，包含交易、费用结构、商户等；输入攻击方进一步核验 payments-readme 明确交易数据为 synthetic，不能据业务来源称真实支付记录；manual 是提炼简化版。任务通过时间/商户参数扩大数量，主要测试答案隐藏，开发答案公开。[官方说明](https://huggingface.co/blog/dabstep)。

攻击：公司费用规则是任务必要定义，不能只给 Agent。整批最终数字不能独立验证每行 fee applicability；共用交易的不同问题不能当独立关系。若难点只是代码聚合，给直接 LLM 全表导致上下文溢出不是语义判断能力证据。

最低反驳：选定一个固定费用适用谓词，以同样的完整行上下文/规则比较；另行构造并独立审核逐行 gold，再验证金额聚合；按实际交易与商户时间实体隔离。规则编译固定程序若胜出应保留，随后比较是否需要示范才可得到该程序。状态：可修复，但目前不能称现成 row-level gold 环境。

### MMAD/LOCO：保留同产品视觉路线，文档价值独立证明

本仓库已有[资源审计](mmad-resource-audit-2026-09-05.md)：原图多题不能作独立图，知识描述不自动是完整装配规范，知识构造来源未决。[官方资源](https://github.com/jam-cc/MMAD)。

攻击：同原图跨 MMAD/LOCO 暴露、多 QA 放大 N；通过缺少数量规则让直接模型失败；工具读取标注；工具增强来自现成检测器而非探索。最低反驳：固定一个产品任务及完整必要规则、无答案参考；核验工具只从 pixels 计算；将同检测/裁剪/计数工具给固定程序；私有按原图/场景分组。状态：可修复，知识来源与完整性未核验前不声明资源因果优势。

### FinQA：暂不升为主候选

原任务已有检索、program generator 和程序执行评测。[官方代码](https://github.com/czyssrs/FinQA)。相同 arithmetic program 形状不代表同业务 metric；相同报告里的多个题也不是独立文档。gold program、gold evidence 不能作当前公开工具输入。

最低反驳：按任务语义先定义一个固定 metric family，再数源报告与公司；所有方法获取同一原始文本/表，分开测 operand 定位、单位/时期判断和纯执行错误。若只是计算器替代算术，属于工具价值控制，不证明资源探索或单轨迹增量。状态：可修复；当前共享 family 规模待发现方核查。

### GuideBench：当前需先审 gold，不宜凭 human-checked 标签推荐执行

本次独立读官方 README 确认优惠券例：rule_44 禁止满减券与固定金额券叠加，但参考分析使用该满减后又减 25 得 695；rule_11 也禁止此组合。输入攻击方进一步在锁定 commit 的 `data/math_tasks.json` 0-based row 27 找到同例。这里证明的是一条实际规则/参考冲突，不能推断全库错误率。[固定版本数据](https://github.com/Dlxxx/GuideBench/blob/78c5bfa42facee34db31e4ba03ad2c3b5a04bbbc/data/math_tasks.json)、[官方 README](https://github.com/Dlxxx/GuideBench)。

最低反驳：独立于模型输出明确规则冲突优先级和订单/商品作用域，以可执行枚举器加人工复核审计选定规则 family；修订答案或排除歧义要在实验前版本化。不能悄悄“修好 gold”后沿用原基准分数。状态：选定行 gold 致命，整个数据集可修复但增加标注负担。

### UNDERWRITE：概念匹配，当前公开产物不等于可运行环境

公开数据卡为 380 条轨迹记录，含 company task id、模型、reference answer 等；数据卡明确并非真实业务日志。没有在已核验发布物确认完整独立指南/SQL 环境。[官方数据卡](https://huggingface.co/datasets/snorkelai/Multi-Turn-Insurance-Underwriting)。轨迹内工具返回的正确片段不应被当作独立无泄漏资源重建测试世界。最低反驳：获得可复现的规则/DB 初态、唯一企业任务映射及独立 gold；明确合成任务属性。状态：当前执行阻断，保留来源等待，不花模型预算。

### V*Bench：工具感知控制候选，不直接当批环境

发现方报告的是高分辨率异质 QA 工具线索，本研究侧未独立完成其原始样本核查；不把这个转述写成验证结果。应先证明足够多原图共享同一物件属性/业务判别。否则只用于验证裁剪/搜索能否改善感知，不能以异质 QA 列表替代固定批谓词。

## 4. 下一步最低实验与停止条件

首先仅做构造审计：完整读入一个任务 family 的少量原始输入，画出固定 scan→semantic node→relation/aggregate，逐字段标出必要输入、可选资源、private gold。冻结抽样且不按预期模型错误挑选。真实输入不可得、标签冲突未解、任务 family 不成立时立即暂停该候选。

通过后才做开发资源屏幕：完整输入直接判断；完整输入+固定资源；固定分解/工具；Agent。对齐模型/预算或公开不能对齐的因素，记录新增正确与新增错误、coverage 和下游。预注册有业务意义的最小改善而非只追 p 值；小样本只能筛选。对资源无改善的候选不反复调到显著。

质量路径成立后再冻结一条真实示范，比较提取/no-trace/摘要/固定程序。在独立源实体确认，计入示范选择、失败、提取、验证、索引与执行成本。单轨迹同时读多条历史案例必须披露监督量。若固定编译或无轨迹生成已达到相同质量/总成本，应据实裁定单轨迹没有额外价值。

当前仓库 CUAD、BioDEX、PCB 以及 CUAD 历史实验均未建立所需 Agent 主指标优势；这些是本地限定条件下阴性/不确定结果，不是挑选新弱基线的理由。下一阶段的产物应是可被强对照推翻的 workload，而非预定要赢的数据集名单。

## 5. 第二轮质询：AnomalyClaw / LogicAD

发现方新补 AnomalyClaw 的同模型 direct/agent 表，研究侧独立打开论文核查。SDNET 和 LOCO 保留为待构造候选；固定 AnomalyVFM 在 SDNET 更强不使环境失效。这里没有确认 agent 比最佳固定法强。[AnomalyClaw v1，Table 1](https://arxiv.org/html/2605.10397v1)。

**读出方式是具体混杂。** Appendix H 显示 Qwen JSON Direct AUROC 0.7128、JSON Agent 0.7480，而 logit Direct 达 0.7643，logit 融合 0.7672。前一组同读出比较仍有增益，不能说其比较无效；但宏观结论不能扩大为强直接调用存在同样大差距。论文 Appendix J.1 明确未报告同 token 预算 direct self-consistency/CoT/reference profiling，Appendix M 的旧切分不能代替新 headline 对齐预算。AUROC 改善也未证明固定阈值后的清单质量。[论文 Appendix H、J.1、M、R](https://arxiv.org/html/2605.10397v1)。

**当前源码/版本攻击。** root 核查 `aggregate_v12.py` 的 `filter_ok` 会排除 error、无 gold、缺 direct/v9 等记录，故 published scored subset 不能代替全量 coverage；另发现 `BENCHMARK_SPEC.json` 仍为旧 11 域。此项为同组源码核查证据，研究侧没有重复运行 scorer。需要冻结同一 commit、输入清单、失败 ID 和表格映射重建；文件陈旧不直接否定所有测量。[官方仓库](https://github.com/jam-cc/AnomalyClaw)。

**最低反驳实验 A：LOCO clean reconstruction。** 以下是独立版本的 logical-only 候选，与 general/all-anomaly 不同；不能直接复用原表混合异常标签或分数。若先复现原 all-anomaly，必须保留原完整异常定义，另报逻辑子类。先选一种产品、固定“逻辑装配异常”语义，源图不按模型错例选择；仅用独立 normal 参考形成正常规则，规则缺口记录为缺口。使用固定 DAG `scan image → sem_filter(logical anomaly) → project ID → count`。同一图像解码、参考图、知识、模型与输出 schema 下比较：(a) direct；(b) direct+同资源固定 CoT/复核且预算配平；(c)固定物件识别/计数/规则执行；(d)有界 Agent；必要时加入 LogicAD 类固定实现。单独 normal/dev calibration 冻结阈值，再对未曝光 test 报告 list precision/recall、count error、ABSTAIN 全量分母。应先核对逻辑异常与结构异常标签如何处理，不能临时把难结构图删掉。若 (c) 胜出，保留为固定推理有效；再比较 Coding/no-trace 是否能自动得到 (c)。

**最低反驳实验 B：SDNET fixed-resource control。** 固定 crack 判别，按原始桥面/路面/墙面源照片而非相邻 patch 划分；若发布物无法恢复 parent image，则不声称独立场景确认。a/b/c/d 共享允许的放大/局部图/检测器；直接判断与 Agent 都比较相同 score readout，并增加固定 detector+阈值。用 dev 校准、test 冻结阈值和计数；分解“看清裂纹的感知增益”与“调用什么工具的策略增益”。若直接 logit 或固定 detector 已消除差距，只留下工具控制，不声称 agent 探索必要。

**LogicAD 是需要补的固定强对照。** 原文通过 VLM 文本特征和规则推理检测逻辑异常，说明固定分解路线本身有明确先例。规则来自 normal 资料不等于其自动覆盖真实产品所有合法变体；感知错误和逻辑执行错误须分别测。研究侧确认了原文和官方仓库链接，未核验全部文件/依赖可运行，不据 issue 讨论直接断言缺失代码。[LogicAD 原文](https://arxiv.org/html/2501.01767v2)、[官方仓库](https://github.com/jasonjin34/logicAD)。若现成实现不能复现，可明确标记重实现固定流程；不可把同名 JSON 人工特征当 pixels 感知。

本轮没有赢家。LOCO 的存活理由是正常规则与视觉计数形成可审计语义步骤；SDNET 的存活理由是具体感知工具增益线索；它们的不同研究价值必须分开，均未通过本地资源/策略/单轨迹实验。


### 最后一轮交叉复核补记

已通读[发现方](adversarial-search-2026-09-05-candidates.md)与[输入攻击方](adversarial-search-2026-09-05-input-audit.md)最终文档。研究侧接受下列限定，替代任何更宽泛的归因：

- AnomalyClaw 固定 commit `1a0c4b4e8e25d8a231f694b264a6669925b6d0b6` 的 v12 确实可 dispatch 到 v8 expert，policy/range 源码使用 test cache AUROC 与 normal/anomaly median。D3 Qwen 的 6 次 expert 调用中 3 次观测字段含 `range_hint/domain_auroc`；Seed 为 2 次中 1 次；GPT D3 无 expert 调用。日志只有字段名，没有数值 payload，因此确认的是风险路径与实际调用/字段，不能认证当时逐值内容，也不能将 GPT 增益归于该路径。三方因此不接受原表为 clean same-environment causality；GPT D3 仍保留需独立重建的探索线索。[固定源码](https://github.com/jam-cc/AnomalyClaw/blob/1a0c4b4e8e25d8a231f694b264a6669925b6d0b6/benchmark/scripts/agent_tools_v8.py)。
- root 重算的 D3 三份发布输出各 120 usable、无 error。因此通用 scorer 排除失败的代码风险不能被写成 D3 实际删失败制造优势。仍需全量 manifest 对齐与其他域 coverage 审计。
- `tool_domain_knowledge` 是再询问 LLM，而非查询独立手册；`component_counter` 计专家热图连通块，未证明对应真实组件数。重建资源卡必须按实际计算语义命名；对比同预算再问模型，不能声称已经量到手册收益。
- SDNET manifest 的母图前缀代理显示 calibration/test 9 组与 dev/test 13 组重叠，发现方独立重算一致。代理不是最终母图证明，但足以要求重新核对母照片并分组；不能沿用当前 split 声称场景独立。
- 发现方未取得 LOCO/SDNET 逐域 logit Direct 对照，故不能推断逐域强 readout 下增益仍成立。LogicAD 仅确认固定推理设计线索，完整代码可运行状态未核验。
- TrialGPT 总体 README 的合成表述不替代各子集来源核验；TREC 叙述风格不能证明真实患者。保留“病例来源依子集审计”的边界，不把全部记录笼统归为真实临床输入。

以上仍为公开论文/源码/元数据审计。没有新模型运行，不能把修订后的候选设计写成已消除泄漏的成功实验。
