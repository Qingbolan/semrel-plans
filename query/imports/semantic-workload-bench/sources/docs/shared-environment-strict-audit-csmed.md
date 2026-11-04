# CSMeD-FT：严格条件复核（增量 strict218）

结论：**Reject，针对本次严格入场标准；仍可作条件筛选开发对照。** 更像固定检查表路线，未证明中间执行家族复用。不同排除原因不是不同程序的证据。

原论文和完整作者仓库已下载，本轮重新打开论文§5.1–5.2、真实CSV/metadata。复用commit `b30e9739939f52b1e799295138791f1fd5b002a5`，不重复下载。[原论文](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf)、[官方仓库](https://github.com/WojciechKusa/systematic-review-datasets)、[下载收据及先前完整核验](shared-environment-search-2026-09-08-round2.md)。本轮[重新计算哈希](../artifact/evidence/shared-environment-audit-20260914-strict218/integrity.json)。PDF339,308bytes，仓库ZIP33,644,877bytes。源全文版权与仓库许可须分别审核，未认定允许再发布全文。

## 表1：入场审计

| 数据湖 | 原论文/仓库 | E组成规模 | 记录/N | 固定q与gold | C定位 | D完整E静态 | E分支/K | F/G/H | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| CSMeD-FT / CD001431.pub5 | 上述固定下载 | metadata中criteria_text，1,039空白分词；不是几十页protocol | 171出版物，68纳入103排除；全文766,375词 | 按该review标准纳入与否；原review人工决定 | 20条抽样均找到相关criteria节，但0条认定完成全部事实+规则闭合；不等于0准确率 | 未证明不足；论文是固定拼接/滑窗分类，非同资源Agent对照 | 设计、具体选择、工具定义、比较组等是检查维度；执行K未知，固定程序K=1仍成立 | 全发布单E最大171，未达数百；实体关联/工具附件不足；已下载，许可分资产待核 | Reject：B复杂度、D/E证据、F规模、G闭合不足 |

A固定q可写；B同E共享成立但长复杂环境不足；C20条仅定位审查不算通过；D/E未建立；F不达要求；G未完成；H原文/完整仓库可得，原全文权利边界待查。全库3333行跨213个review，不能作为单E的N。原论文§5.1仅找回平均27%出版物开放全文，是可获取子集而非完整自然筛选日志。

## 表2：Query×数据湖

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 私有gold |
|---|---|---|---|---|
| 对CD001431.pub5返回纳入出版物ID清单 | train_reviews_metadata.json对应criteria | CSV的171条document_id/title/abstract/main_text | 需额外关联试验与工具附件，目前未闭合 | decision，共68纳入 |
| 返回纳入出版物数量 | 同一E | 同一171行 | 普通count，不是第二个独立语义任务 | 68 |

一页标注表：publication_id字符串；eligible取INCLUDE/EXCLUDE/UNKNOWN；evidence为公开文献定位；rule为固定criteria节；missing为缺失事实列表。UNKNOWN仅表示公开证据不足，不能沿用原review EXCLUDE；执行失败另记ABSTAIN。study-level纳入传播至关联publication的确切规则尚未封存，不能默默改gold。

## 表3：DAG

| 类Python的DAG | 类型 | 具体数值与依赖 |
|---|---|---|
| `R = scan(csv, public_allowlist)` | 普通 | 171行，剔除decision/reason_for_exclusion |
| `rules = compile(E)` | E-only语义预处理 | 同一1,039词字段；分离事前判定与事后outcome内容 |
| `facts = sem_map(R, trial_facts)` | 逐文献语义 | 设计/真实选择/工具内容/各比较臂；需原文证据 |
| `y = apply_rules(facts, rules)` | 固定分支，必要处语义判定 | 决定gold；不能用工具自称或两个工具词命中代替判断 |
| `project(filter(y == INCLUDE), id); count()` | 普通 | gold68；预测未运行 |

## 表4：四路预期与operator

以下均为待测过程，不预言准确率或Agent优越性。==标记可观察探索动作==。

| 臂 | 预期执行结果 | 预期执行过程 | 可能operator |
|---|---|---|---|
| LOTUS任务表only | 无特定review规则时无法可靠复现；未测 | 每篇一次sem_filter，容易把RCT/自称aid当充分条件 | 通用eligible提示词 |
| LOTUS完整E | 完全可能达到或超过Agent；未测 | 同一完整criteria+全文；或E-only编译、固定检索与sem_map再判定 | TrialFacts→RuleGraph；允许分支/缓存 |
| 逐记录Data Agent | 同目标，缺工具附件仍无法恢复事实 | ==读criteria定义==→==定位设计和所有比较臂==→==检查工具定义证据==→决定/UNKNOWN | 引用型事实抽取+规则执行+缺证据终止 |
| 批处理Data Agent | 同目标，可能共享E预处理；收益未测 | ==一次解析E==→==建立试验/出版物关联候选==→逐条取证→共享规则判定 | 批共享RuleGraph/实体关联；不得把gold反向加入关联 |

ρ_E：criteria解析可一次预处理；ρ_P：同一事实schema与检查逻辑；ρ_G：潜在多臂/代理人/次级报告组，但没有轨迹证据证明是不同必要执行程序；ρ_R：每篇提取事实及歧义。无运行轨迹，四项比例、K和成本均未知。多臂结构可由早期语义列预测并交固定程序处理，因此并不自动支持目标。

## 20条真实记录核验

选最大review内SHA256(`strict218`+NUL+document_id)升序前20，未按标签筛选；开发暴露，非独立确认。逐条实际读摘要、gold原因及完整criteria；**未逐条完整全文和外部附件复核**。表内节名对应metadata的`Types of ...`键。相关节可定位不代表独立验证gold。

| publication尾号 | gold | E节 | 本次观察/未决 |
|---|---|---|---|
| 0014 | included | studies/participants/interventions/comparisons | P3P次级结果报告；与0013同试验的实体关联需核验 |
| 0013 | included | studies/participants/interventions/comparisons | P3P次级报告；不能按独立试验计N |
| 0035 | included | comparisons | 四臂含普通网站对照；不能因出现两种工具直接排除 |
| 0211 | excluded | interventions | 临终照护类别与general advance directives对应；具体边界仍需全文 |
| 0161 | excluded | studies | 两阶段工具开发pilot，无随机分配描述，与排除理由一致 |
| 0326 | excluded | interventions | gold称无具体选择；短摘要只给风险意识目的，需补全文 |
| 0042 | included | participants/interventions | 痴呆患者代理人选择允许；摘要截断，条件未全闭合 |
| 0365 | excluded | interventions | 摘要自称中性信息，gold称缺收益风险信息；需实际工具内容 |
| 0113 | included | comparisons | 三臂有control；不得把两种工具臂存在当排除 |
| 0011 | included | studies/comparisons | 随机设计、usual care；工具最低定义需核验 |
| 0127 | included | studies/comparisons | 随机两臂、usual education；未完成逐条件全文复核 |
| 0112 | included | studies/comparisons | 与0113可能同一试验；需实体分组 |
| 0099 | included | studies | 摘要为正在进行RCT方案；publication/study链接语义不能混同 |
| 0213 | excluded | interventions/comparisons | gold指无values clarification；摘要未闭合工具内容 |
| 0130 | included | studies/comparisons | 嵌套RCT的录像过程研究，非独立随机试验 |
| 0196 | excluded | interventions | 摘要称decision aid而gold否；定义边界需全文/材料判定 |
| 0188 | excluded | studies | before/after设计，直接支持非RCT排除 |
| 0160 | excluded | interventions | 为试验招募使用工具，涉及clinical trial entry排除项 |
| 0425 | excluded | comparisons | 更新后simple/detailed排除；摘要control不足以判定对照工具 |
| 0135 | included | studies/participants/comparisons | 随机、具体胚胎数选择、标准照护；需完整工具条件 |

## 具体可证伪例与十问结论

`CD001431-bib-0035`为真实四臂RCT，公开摘要描述三个实验条件及可信公共网站对照，gold为included。criteria比较组限制的关键短引为“two different types of patient decision aids”。这不表示只要文献出现两种工具就排除；需识别是否存在合格对照比较。静态完整E和Agent目标均为included，实际输出未知。相同固定多臂关系抽取程序即可表达，不需要为该ID建特例。

另一条`0099`摘要写RCT正在进行，gold仍included；`0130`是嵌套试验的录像分析。提示review纳入文献集合与“该出版物独立满足试验报告标准”不能直接等同。尚未证明gold错误，也没有补造标签。

1. q与不足输出：见一页表；研究级关联规则未闭合。
2. E：1,039词固定发布criteria，不是完整长事前protocol。
3. x/N：171出版物；多臂、代理人、工具定义、次级报告不同。
4. y：原review人工决定；排除原因私有，纳入一般无逐条件依据。
5. C：20定位审查，全部条件闭合未认证；不宣称20/20通过。
6. D：原论文使用固定拼接/滑窗，旧模型分数不能证明完整E静态不足。
7. E/K：不同检查维度不是执行家族；K未知，K=1固定程序未排除。
8. Agent：可探索规则与论文证据；主要共享E解析与schema，家族收益未测。
9. G：必须剔除decision/reason，另审review结果、论文实体重复；工具附件未必可得。
10. 非条件分类的证据：没有；这正是本轮Reject理由，不能用语义复杂替代执行结构证据。

不列入Strong或Top5推荐。本轮没有模型调用、baseline质量实测、实验构造或独立确认。严格台账只新增这一个完成边界判定的候选。
