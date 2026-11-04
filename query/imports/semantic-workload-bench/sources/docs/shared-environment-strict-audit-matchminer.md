# MatchMiner-AI：真实大规模验证存在，公开数据不满足目标

**Reject 公开真实患者批任务。** 本轮用系统综述2509.19327定位线索后，下载并阅读原研究，不以综述表格作为最终判定。结构有不同癌种/阶段/生物标志物/既往治疗语义判断，接近HSCodeComp候选；但公开的是合成数据，真实患者评估集明确不可共享。

## 表1：入场审计

| 数据湖 | 原论文/仓库 | E规模 | 记录与N / q | gold来源 | C / D / E | G / H | Verdict |
|---|---|---|---|---|---|---|---|
| MatchMiner-AI | [原论文](https://arxiv.org/abs/2412.17228)，下载版本内部3.0/August2026、68页；[训练repo](https://github.com/dfci/matchminer-ai-training)和[推理repo](https://github.com/dfci/matchminer-ai-inference)完整克隆 | 本次实际CSV7695条space、3000不同NCT；repo另有470试验示例；不是完整protocol PDF | 真实评估论文7982入组事件/7056患者，另11393标准治疗开始/5758患者；单试验真实带gold N未知 | 实际入组及研究评估与公开模型训练标签区分；没有取得真实患者gold | C0/20；D完整E/强固定流程不足未证；E的K未知 | 真实DFCI数据含PHI不能共享；公开合成库与代码CC-BY-NC-ND4.0；不以合成代替真实 | Reject |

A可定义固定“对某试验筛患者”，但论文主要提供临床考虑/排序建议，不等价最终入组资格。B试验标准可以共享，公开space是模型从标准提取的目标人群，非完整protocol。F大规模真实应用存在，但公开真实批未获得。H两个完整代码repo可得，原论文Data sharing明说真实评估集不能共享；旧HF MatchMiner-AI API返回401后已按新版论文找到公开新仓库，不把旧链接失败当总体闭源。

论文旧版常见数字16139入组/13425患者/1534试验不用于本卡当前版统计。当前论文真实数据段还描述814候选试验/2990spaces与标准治疗组500试验/1347spaces。这些是候选池，不是每患者全部配对有独立gold，更不是每试验有7056个完整资格判定。

## 表2：Query × 实際数据

| Query | 数据1 | 数据2 | gold/边界 |
|---|---|---|---|
| q1 固定试验→候选患者匹配/不匹配/UNKNOWN | CSV首例NCT06139419，局部晚期不可切除NSCLC，成人、ECOG0/1等标准，排除自身免疫病等 | 本次7695条space文件含eligibility_criteria与this_space；真实该试验患者未取得 | 不能给真实患者例或真实gold，不捏造 |
| q2 固定患者→筛选试验 | repo note_set_1首行synthetic患者ID1722，58岁男性，胃食管结合部腺癌病理记录 | repo470个试验摘要与标准；与该患者的完整独立判定未取得 | 生成病历是真实下载文件内容，但不是现实患者事实；无人工gold |
| q3 核查排除项→Boolean/UNKNOWN | repo模型输出首对11609/NCT05785741 | final_matches.csv的passes_exclusion_criteria=False | 这是上游模型预测，不是gold。35行/12患者ID不可当验证集 |

示例notes两文件分别117和56行，各12个患者ID；不能把173份笔记当173患者。sample_trial_space_lineitems.csv实际完成下载后为296790803bytes、7695行，训练6093/test901/val701；下载期间读到的6833行是未完成文件，不纳入最终统计。没有下载全部大型合成病历库或权重。

## 表3：类Python DAG

| DAG | 具体字段和边界 |
|---|---|
| `trials = scan(csv).project(nct_id,eligibility_criteria)` 普通 | 3000个NCT，7695space行不等于7695试验 |
| `summary = sem_map(patient_notes, clinical_summary)` 语义 | 公开示例为合成；当前患者生成标签及目标space不可泄漏 |
| `candidates = retrieve(index(trials),summary)` 普通/向量检索 | 固定程序可执行；没有本次实际模型运行 |
| `matches = sem_map(summary,candidates,core_match)` 关键语义 | 输出临床可考虑程度，不自动转最终eligible |
| `excluded = sem_map(summary,exclusion_criteria)` 语义 | 时间/病史及信息不足须保留；published prediction不是独立评分依据 |
| `rank_or_filter(matches,excluded)` 普通 | 本次没有真实gold可评分，不能生成精度或摊销曲线 |

## 表4：四路推演，未运行

| 臂 | 预期结果 | 执行过程 | 候选operator |
|---|---|---|---|
| LOTUS任务+患者 | 无真实gold目标可核；仅靠任务无法验证特定试验标准 | 直接语义匹配，可能依赖模型记忆 | 固定分类控制 |
| LOTUS完整E | 完整protocol未获得；给定标准可做固定检索+判定对照，质量未知 | 预处理trial spaces→患者摘要→检索→固定匹配/排除项检查 | 原论文流程本身提供固定分阶段替代，不等于逐案Agent |
| 逐记录Data Agent | 不保证优于固定程序；无法恢复未公开EHR | ==查标准与排除条件==→==查纵向病程和时间==→临床考虑/UNKNOWN | `history_summary→scope_match→exclusion_check`假设结构 |
| 批处理Data Agent | 共享标准预处理可能降成本；真实N及gold缺失，不能证实收益 | ==一次索引试验==→==按早期临床字段选择匹配分支==→逐患者判断 | 共享标准索引+参数化规则；未提取或确认 |

ρE为标准提取/索引，ρP为病史摘要及共用匹配流程，ρG可能是癌种/阶段/生物标志物/治疗状态的中间检查，ρR是个体病情与时间解释；比例/K均未知。癌种数量、space数量不是执行家族数量。未排除固定向量检索+判别器+排除检查能够覆盖，不以缺失真实gold论证Agent能力。

十问边界：q及信息不足见表2；E是标准及模型派生space；x公开合成、真实私有；y独立真实标签未获；20条真实闭合0；静态不足未证；家族K未知；探索涉及病程/适用标准；生成字段/预测输出不能当public事实或gold；无法证明超出固定RAG/分阶段匹配，因此不纳入Strong。

## 收据与许可

[下载与commit](../artifact/evidence/shared-environment-strict-matchminer/source.json)、[实际CSV统计及首试验](../artifact/evidence/shared-environment-strict-matchminer/data-audit.json)。推理repo117 tracked文件，训练repo21；本地均未执行。HF0526固定revision62866925d1e8bd30ee72d8b659407b6bca6ff24f，README许可CC-BY-NC-ND4.0；不同旧版许可不得替换。没有新split、模型实验、工程测试或commit。真实患者/完整protocol/独立gold不可用，未以合成样例填20条真实审计。
