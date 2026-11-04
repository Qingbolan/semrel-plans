# Research context and handoff

用户确认：贡献是从 Data Agent 单次执行轨迹转化出可复用算子。当前优先构造数据任务与数据湖，而非提前实现动态算子库。

默认方法可运行但关键步骤质量有限；辅助环境帮助长文本重复处理、关系梳理、逻辑判断和知识补充，并改善下游。外层业务DAG固定，不要求已有标准SOP。不能编造工单、规范或处置gold。

完整历史见 [handoff](history/research-handoff-2026-09-05.md) 与 [construction plan](history/benchmark-construction-plan-2026-09-05.md)。历史中的绝对旧路径和结果不自动属于新仓库。

迁移决策：仅导入DeepPCB源锁、相关上下文及一个固定几何baseline。24记录已有历史暴露，定位为控制/开发pilot；本次没有迁移旧动态实现或声称恢复Agent轨迹。代码来源为旧仓库scripts/pcb_demo_detector.py，保留原算法，仅更新不恰当的身份名称；新方法尚不存在。

当前优先级：BioDEX反应识别P0、CUAD条款抽取P1，先复现论文中传统LOTUS质量不足的线索，再测同环境Agent。LOCO/MMAD作为多模态P2保留；ContractNLI与金融为后续候选。详见[质量差距候选](accuracy-gap-candidates.md)。两条路线本轮已构造各8条开发pilot并运行有预算的比较；当前结果与局限见report.md和各run收据，不能将构造成功等同研究假设成立。

旧医疗CNN质量不足，不能证明成熟专用工具增益。FEVEROUS完整库是文本表格对照。MMQA场馆任务主要卡在证据和语义歧义，不证明静态能力边界。

下一步：先复现传统LOTUS关键步骤质量不足及下游损失，再检验同环境Agent改善与成本，最后从单次轨迹提取算子并在独立批次确认。该差距是待检验假设；静态表现足够的候选保留为负对照，不能换成纯降成本故事。禁止在当前24条PCB上反复调参后称独立泛化。

## 历史经验扩展（2026-09-05）

用户确认将过去执行的正确/错误记录及人工标注经验纳入异质环境。具体问题是识别经验适用条件、利用证据纠正新记录，再从一次执行提取可复用算子；不是把当前测试gold交给Agent。[协议](historical-experience.md)规定历史H、开发D、示范x0和后续R的角色、监督量、固定示例/检索强对照与完整成本。两个PCB历史案例已登记，运行集成与增益实验未完成；本地廉价模型仅为额外部署轴，不替代同模型质量比较。

旧仓库新增100条原生LOTUS对照已按来源导入收据：带模板LOTUS91%、Agent92%，改正9/退步8、p=1.0，固定程序100%。它没有验证明显Agent优势。将其中记录用于经验构造后不能再次称新确认数据；[179条开发暴露登记](../environments/pcb/history/exposure-exclusions.json)用于后续划分。当前BioDEX/CUAD pilot与主线优先级不因本次经验设计改变。

用户本次指定Vision-LLM-Integration转医疗切片batch：已导入历史PathMNIST 1,000条并复跑固定CNN（45.7%）；保留医疗范围作为开发原型，详见[pathology指南](pathology-batch-pilot.md)。原项目无可用权重，本次使用历史补建权重，不替换现有BioDEX/CUAD比较或视为成熟医疗工具。

本轮CUAD/BioDEX各8条实测已完成，均未显示Agent主指标优于固定复核。CUAD span F1为0.5079/0.5318/0.5275；BioDEX RP@10为0.3643/0.3643/0.3589（静态/固定复核/Agent），后者还有提示事件范围与gold对齐风险。当前不进入单轨迹提取；详见[结果与边界](pilot-results-2026-09-05.md)。这些是开发观察，不能当独立确认或改变既定目标。

用户要求实际Codex CLI且同模型：已完成gpt-5.4两个整批比较，CUAD F1 0.5023、BioDEX RP@10 0.3393，均无主指标优势。此前data-agent并非Codex；本次生成代码是逐实例batch产物而非可复用算子。[本轮证据](codex-cli-results-2026-09-05.md)。

人工经验条件进一步实测：[CUAD历史迁移](contract-history-results-2026-09-05.md)。官方专家标注与旧预测对照H8合同，R8新合同；固定有H较无H仅+0.0059，Codex有H较无H−0.0073，未通过筛选。人工解释规则库与自动提取仍未实现，不能把此局部阴性结果推广到所有人工经验环境。


## 用户新目标：可摊销探索原型（2026-09-06）

按本轮附件，先基于DataSpace一个workspace实现稳定任务语义、未知内部流程探索、单次轨迹合成与后续复用。此前CUAD/BioDEX阴性结果保留。DataSpace task184派生开发控制已构造1示范/16验证/300后续基金实体，提取算子299/300正确并保留1次适用性拒绝；手写SQL300/300。工程链路成立不等于新workload通过质量差距筛选。真实所需证据仅SQLite，额外CSV/JSON不能被写成异质资源因果增益。[本轮协议](dataspace-amortization-pilot.md)。

## 用户新路线：从语义基准原题合成任务（2026-09-08）

从survey/benchmark场景定位真实数据与query，再按共享语义中间关系自底向上合成上层任务，在仅挂载公开数据的原生Codex项目重复执行，保存query、候选算子和可观察轨迹。新发现阶段允许流程控制，不替代质量差距与单轨迹主线。实际已整理678条原题/变体、从57条形成15个待核或可试簇；首个SemBench Movie开发控制完成36条影评的一次LOTUS静态和三次Codex执行。静态32/36、Agent24/36、28/36、23/36；无改善，源情感gold边界也待审核。没有自动提取/独立确认。[本轮执行协议](semantic-query-composition-pilot.md)及[用户指定登记仓库的完整来源/结果](../../Awesome-Sem-Filter-Bench/docs/semantic-operator-query-composition-2026-09-08.md)。下一项获取候选CSPaper论文方法/评测证据表，未启动新数据下载或升级claim。
