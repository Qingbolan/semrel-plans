# 当前五个Partial：横向Query、DAG与方法推演

本页取代旧排名中的“当前Top5”入口，旧表仍保留为历史。当前28个已审候选：**0 Strong、5 Partial、23 Reject**。以下顺序是后续证据投入优先级，不是方法性能排名；五者均未完成C20完整闭合、D强固定方法不足及E执行家族验证。原论文/仓库/资产哈希和具体问题见各卡片。

## 八维证据比较

沿用历史评分口径：0/1/2表示材料支持程度，`?`表示未知；不加总、不以其他高分抵消硬条件失败。E：短/中/大；N：不足200/200–999/至少1000；gold：非独立/独立但未闭合/独立且闭合；定位：无/局部/20完整；D：固定程序直接定义目标/局部比较/同资源强固定不足；分支：关键词/固定语义比较/多类语义线索；真实性：合成/真实来源经构造/真实工作记录。K/N只接受执行证据，标签计数不算。

| 候选 | E复杂度 | N | gold | 定位 | D | 分支线索 | K/N | 真实性 |
|---|---:|---|---:|---:|---|---:|---|---:|
| 1 [HSCodeComp](shared-environment-strict-audit-hscodecomp.md) | 2 | 1：632商品 | 1 | 1 | ? | 2 | ? | 1 |
| 2 [CodiEsp](shared-environment-strict-audit-codiesp.md) | 2 | 2：1000报告 | 1 | 1 | ? | 2 | ? | 1 |
| 3 [UDRP](shared-environment-strict-audit-udrp.md) | 2 | 2：1572裁决 | 1 | 1 | ? | 2 | ? | 2 |
| 4 [AnnoCTR](shared-environment-strict-audit-annoctr.md) | 2 | 链接单位2：3348；报告单位0：120 | 1 | 1 | ? | 1 | ? | 2 |
| 5 [STARD](shared-environment-strict-audit-stard.md) | 2 | 2：1543咨询 | 1 | 1 | ? | 1 | ? | 1 |

CodiEsp升至第二是因为本地有较完整的输入、独立标签和编码原件，适合先解决依据闭合；不是已经证明比UDRP更有家族复用。STARD新增为第五个Partial，替换旧表中的Reject控制CSMeD；没有增加Strong。

## 数据湖 × Query（实际字段和数值）

| Query/输入 | 数据湖1：HSCodeComp | 数据湖2：CodiEsp | 数据湖3：UDRP | 数据湖4：AnnoCTR | 数据湖5：STARD |
|---|---|---|---|---|---|
| 固定q | 商品映射10位HTS码 | 按冻结规则给报告的医疗操作编码 | 域名争议是否给予救济 | 给定报告提及链接ATT&CK技术 | 咨询选择相关法条集合 |
| 记录x | 632商品发布字段，原图片/网页有缺失 | 1000西语病例TXT；P任务有881份带码报告 | 1572份裁决来源中的事实；需去裁决理由/答案 | 120报告中的3348技术链接记录 | queries.json：问题、query_id |
| 共享E | 2025rev15 HTS，4429页 | 2018四册2787页+标注DOCX；操作表679页 | WIPO Overview 3.0（第三版），152页 | 1266官方定义，112331词 | corpus.jsonl：55348条，24120549bytes |
| 独立gold | 源10位code | P共3246报告-code对；X提供跨度；两者任务不要混合 | 1513给予救济、59拒绝 | 人工technique IDs | 2717相关链接；1445法条被标 |
| 实际例子 | task591：20件套玻璃制品，价格8.3375，gold7013999090 | S1698-44472005000300015-1：双侧颞下颌关节MRI，局部gold BN39 | D2024-0001：RELIEF_GRANTED | train:3782：局部目标T1140 | query0：谁可成为个体工商户？gold705/49282 |
| E依据和局限 | 价值门槛涉及每件，发布价格口径不足 | 操作表PDF480/印刷461给BN3-9；G12.2允许四位；仅局部支持 | 原卡记录三要件/解释依据；外部调查未闭合 | 解密/反混淆定义与动作局部吻合；非全部链接闭合 | 民法典54、个体工商户条例2均可定位；是一般咨询不是个人许可裁定 |

四冊页数不意味着每次判断需要读2787页；五湖原始含gold的源文件都不能直接整体交给模型。上表只描述审计数据，没有发布统一可运行public/private快照。

## 类Python DAG横向表

`sem_*`为语义步骤；`scan/index/lookup/score`为普通步骤。均为待实现契约，未把手工正确事实作为模型输入。

| 类Python的DAG | HSCodeComp | CodiEsp | UDRP | AnnoCTR | STARD |
|---|---|---|---|---|---|
| 普通共享预处理 | `tree=index(HTS)` | `tables=index(codebooks)` | `idx=index(overview)` | `idx=index(definitions)` | `idx=index(articles)` |
| 语义事实列 | `f=sem_map(material,use,value_unit)` | `f=sem_map(modality,anatomy,laterality)` | `f=sem_map(three_element_facts)` | `f=sem_map(mention_action)` | `f=sem_map(legal_issues)` |
| 关键语义操作 | `code=sem_map(f,tree,notes)` | `code=sem_map(f,tables,guidelines)` | `y=sem_map(f,idx,three_elements)` | `ids=sem_map(f,retrieve(idx,f))` | `ids=sem_filter(retrieve(idx,f),question)` |
| 普通输出/核验 | `validate_code_or_abstain` | `validate_specificity` | `validate_decision` | `normalize_ids` | `deduplicate_ids` |
| 下游 | code清单/分组统计 | code集合/提及任务分别评分 | 救济清单/拒绝召回 | 技术清单 | 法条集合Recall/MRR |

## 关键算子：LOTUS与Data Agent的预期过程

没有模型执行结果。表中gold是应对齐的目标，不是对某个模型输出的预测；环境缺少事实时，Agent也不能保证补出答案。UNKNOWN/ABSTAIN需独立契约，不能自动计为源gold正确。

| 实例 | LOTUS关键操作预期结果 | LOTUS预期过程 | Data Agent关键操作预期结果 | Data Agent过程，==环境探索== | 预期operator结构（未提取） |
|---|---|---|---|---|---|
| HS591 | 无法可靠承诺7013999090；件价事实不足 | 抽单位/价格→固定树规则→不足处理 | 同资源下同样缺事实 | ==核价值门槛与价格单位==→保留缺口 | `facts→unit_guard→tree_classify` |
| CodiEsp MRI | BN39为局部支持目标，未实测 | 抽MRI/双侧ATM→表查找→四位粒度检查 | 相同局部目标，优势未知 | ==查BN3表与G12.2==→检查缺失对比剂信息 | `semantic_slots→table_lookup→specificity_guard` |
| UDRP0001 | RELIEF_GRANTED为源目标，未实测 | 三要件事实→固定检索→AND/例外 | 相同目标，外部事实仍受限 | ==查要件解释与例外==→逐项核事实 | `elements→exceptions→decision` |
| AnnoCTR3782 | T1140局部可支持，未实测 | 候选检索→定义比较→归一 | 不预期必优于固定链接 | ==查解密/反混淆定义==→核动作 | `retrieve→link→normalize` |
| STARD0 | 705/49282是目标，未实测 | 查询改写→检索→语义重排 | 相同ID集合目标，未知输出 | ==查主体资格与登记条文==→相关性筛选 | `decompose→retrieve→rerank` |

## 四路臂与可摊销部分

| 臂 | 输入 | 允许过程与结果边界 |
|---|---|---|
| 静态任务only | 同一页任务+同一记录 | 不含E；测资源价值，不可用其弱结果证明Agent必要 |
| 静态完整E | 同任务+记录+完整公开E | 能放入上下文时整段；超长时记录不可执行，并另保留同资源固定检索/预处理强对照，不能用截断冒充完整E |
| 逐记录Agent | 同任务+记录+同一可探索E | 按上表探索，记录可观察工具与结果；没有特供private证据 |
| 批Agent | 同任务+整批记录+同一E | 可共享索引、缓存和计划；这些成本收益须区分ρ_E与ρ_G，不强制逐例重规划 |

| 候选 | ρ_E（一次预处理） | ρ_P（统一每条程序） | ρ_G（家族假设） | ρ_R（个例） | 最强固定对照/首要风险 |
|---|---|---|---|---|---|
| HS | 税则树与章注索引 | 语义事实抽取 | 材质/用途/估值路径，未测 | 属性冲突、缺件价 | 固定层级程序；输入不完整 |
| CodiEsp | 表索引/粒度规则 | 扫描提及、抽轴、查表 | 部位/侧别/操作类型，未测 | 具体表达/省略 | 语义列+固定编码表；完整标注规则与gold含义 |
| UDRP | 解释/例外索引 | 三要件检查 | 合理使用/注册时点等，未测 | 个案事实 | 固定三要件RAG；1513/1572多数类、回顾性泄漏 |
| AnnoCTR | 定义向量/候选索引 | 链接与归一 | 未观测 | 报告语境 | 固定链接器；明示ID/概念捷径 |
| STARD | 全库索引 | 分解/召回/重排 | 未观测 | 咨询措辞 | 固定RAG；标签充分性与实体隔离 |

所有K、ρ比例、方法准确率及完整成本仍未知。五者都可能被E-only预处理与固定语义程序覆盖大部分共享工作；没有证据排除它们退化为条件分类或固定RAG。当前最有依据的下一步是先闭合输入和gold，并以同资源固定程序为对手，而不是预先建设家族算子库。


[五个真实例子的集中原文短引、字段、gold和限制](shared-environment-top-five-examples.md)。


2026-09-14 BidCorpus增量：当前累计28项，0 Strong / 5 Partial / 23 Reject；本页五项排名不变。新增依据见[BidCorpus卡片](shared-environment-strict-audit-bidcorpus.md)。


AnnoCTR全文补查：Excel宏实例获得全文支持；泛指漏洞利用仍未闭合；PyInstaller报告后文直接列出T1059，存在原生ID暴露。不能把全文支持等同于mention-level证据或E必要。见[更新卡片](shared-environment-strict-audit-annoctr.md)。


CodiEsp实质补证：冻结样本第2例左侧下颌骨证据对应原gold0NBT，而2018表和随库词表T=右/V=左；已记录[侧别冲突](shared-environment-strict-audit-codiesp.md)，不改gold、不估算全库错误率。该例不能作为同资源静态质量不足证据。


本轮续查最新状态：**29项，0 Strong / 5 Partial / 24 Reject**。新增[C3PA排除依据](shared-environment-c3pa-in-progress.md)；上文28项为此前交付。HuBMAP ARMS正在审查，未计入通过或已审数量。


## 当前核验增量 2026-09-15T00:16:45.184140+08:00

当前已审32项：0 Strong、5 Partial、27 Reject。新增 OmniCompliance、PrivaCI、AIReg-Bench 均未通过；HuBMAP仍在审不计入。旧28项/29项数字属于历史批次。最新逐项事实见 [状态账本](shared-environment-strict-goal-status.json)，AIReg证据见 [核验卡](shared-environment-strict-audit-aireg.md)。用户至少5 Strong目标未完成。


## 开发数据湖与Query交付（2026-09-15）

五项已按现有public/private方式[构造为真实开发快照](shared-environment-five-lakes-build.md)，含5个主任务及15个派生query。[统一目录](../workloads/shared-environment-five.json)。本页早期“尚未生成统一快照”描述对新构造已更新；未运行语义模型或评分，所有科学判定保持原状。AnnoCTR3348条实际来自112报告，湖保留120报告；11条源TECHNIQUE行指向software，加18条缺KG共29条原gold不在技术输出目录，未改标签或删样。UDRP仍仅供审查。


## 当前核验增量 2026-09-15T00:37:30.713412+08:00

已判定36项：0 Strong、5 Partial、31 Reject。RegOps、PRT、DSO、GUIDE新增排除；MDACE、HuBMAP、CORTEX、SecAlert等未完成来源/环境核验，不计入已判定数。数字以[状态JSON](shared-environment-strict-goal-status.json)及各卡为准；历史批次数字保留。GUIDE已全量下载并计数，[实证卡](shared-environment-strict-audit-guide.md)。至少5Strong目标未完成。
