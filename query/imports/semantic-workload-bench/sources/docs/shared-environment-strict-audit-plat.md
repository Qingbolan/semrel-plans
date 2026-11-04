# PLAT：韩国附加税处罚合法性

**Reject 严格大批共享环境路线。** 固定任务和真实裁判来源有价值，但每个任务只有100个案例，不能把三种题型或双语副本累加。结构上有潜在的语义规则适用分支，更接近HSCodeComp路线；尚未证明少数可复用执行家族，也未排除固定检索/预处理。

## 表1：入场审计

| 数据湖 | 论文 / 仓库 | E组成与规模 | 记录与N / 固定q | gold来源 | C依据定位 | D静态完整E不足 | 分支/K | 泄漏与可回答性 | 可获取 / 判定 |
|---|---|---|---|---|---|---|---|---|---|
| PLAT v2 | [原论文](https://arxiv.org/abs/2503.03444v2)，已下25页；[完整官方repo](https://github.com/lbox-kr/plat) | 论文报告100判例+4042法条；repo仅4文件，无该检索语料。本次另下载论文所链KLRI完整法案HTML，不能当4042法条已获得 | MC100、MC4 100、Essay100；判断附加税处罚是否合法 | 真实判例，经o3提取并由税务人员审核；MC真/假50/50。MC4人工理由选项；essay rubric不是独立新案例 | hash20提取私有判理中的法源线索，完整E闭合0/20 | 有论文固定BM25-RAG实验，但非完整E/固定多步强对照；无本次运行 | 否定误解、合理信赖、客观履行困难等候选分支；K未知，不能用easy/hard代替 | reasoning/decision/lawfulness/gt是私有；首次病例充分性未闭合；跨语言同案 | 原论文/repo/6个完整HF数据快照已下；实际检索池未获得。Reject：F及C/G/H缺口 |

A：二分类q固定，允许don't know；MC4固定选择操作但每案候选理由不同；essay附理由可单列，不增加N。B：论文有共享法源候选，但100判例中逐案排除自身，尚无冻结的独立历史E与后续R切分。C：0完整闭合认证，20法源线索不是必要性证明。D：没有排除env-only法规整理、固定事实表+检索多步程序。E：语义分支是研究假设，未测1≪K≪N。F：每q仅100，不满足数百。G：公开完整原判/证据未封存；别将双方主张当认定事实。H：数据页与repo声明CC-BY-NC-SA4.0；论文正文较宽写CC-BY-NC，采用实际数据页具体许可，不覆盖第三方法源。

版本边界：检索曾命中2025 v1（50例、50判例池、不同模型实验）；本卡使用实际下载2026-02-08 v2（100案例、4042法条）。不混引旧版性能。源池约2800不是公开带gold的2800行。原论文表3的“F1”用answered accuracy与coverage组合定义，不等于常规二分类macro-F1；不能与仓库其他任务直接对比。

## 表2：Query × 数据湖资产

| Query | 数据1：MC parquet `case_info,facts,claims` | 数据2：E / 私有辅助字段 | 数据3：实际gold / 数值 |
|---|---|---|---|
| q1 判附加税处罚是否合法，输出True/False/UNKNOWN | `2011guhap2638`：造船公司已获企业税延期，未另申请居民税延期；请求减免附加税 | 相关旧Local Tax Act及实施令仅在主张和私有判理中有引用；KLRI另下Framework Act全文，不能替代适用地方税法 | `lawfulness=False`；修减后的罚税1,105,805,430韩元；法院撤销拒绝减免处分 |
| q2 选合法性及核心理由，输出A/B/C/D，失败ABSTAIN | 同案MC4；选项包含各候选结论及理由 | `choices`是任务给定输入；`gt,reasoning,decision`私有 | `gt=C`：严重经营危机符合减免理由。100行A/B/C/D各25 |
| q3 给合法性及法律分析，输出结构化论证 | 同案essay题；case_info/facts/claims和question_prefix | 10项共享rubric为评分标准，不是长规则环境；当前判决reasoning/decision私有 | 100个reference，与MC同源。不得将LLM-as-judge分数叫真实裁判gold |

首例证据审查：公开claims写经营危机主张，政府否认其满足减免要求；判理新增订单减少、工会罢工、2008年8月后主营业地无新订单等支撑。这些细节没有出现在三个公开输入字段中，不能从一般主张推出法院事实认定。这里只报告证据缺口，未修改gold，也不宣称所有案例都不可回答。

金额翻译需核验：同案英MC写延期1200 billion，韩文1200억与英MC4/essay的120 billion一致；韩文总额逗号本身也异常。原判未取得，不自行修复输入。该差异不能作为Agent推理优越的证据。

案号对齐：三个英文集直接字符串并集102；实际仅两处韩文法院名称与英文法院名称不同，分别2016guhap70759、2015nu53482；其余98行案号一致。保存原字符串，明确对齐理由，不默默把102算成独立案例。

## 表3：类Python DAG

| 类Python DAG | 具体数值 / 普通与语义步骤 |
|---|---|
| `r = scan(mc_test).project(case_info, facts, claims)` 普通 | 100行；官方eval.py同样只拼接这3字段，不把私有判理交给被测模型 |
| `f = sem_map(r, distinguish_facts_claims_and_tax_type)` 语义 | 首例区分企业税延期与居民税、双方争议、经营危机主张；保留UNKNOWN |
| `scope = sem_map(f, identify_applicable_version_and_rules)` 语义依赖E | 国家/地方税范围和历史版本；无完整法源时不能假设当前法适用 |
| `evidence = fixed_retrieve(E, scope, f)` 普通检索+可选语义排序 | 论文BM25 top3，E池4042法条+排除本案后的判例；本次未复现 |
| `y = sem_map(f, evidence, assess_justifiable_reason)` 关键语义 | 首例目标False；证据不足可UNKNOWN；不能拿gold保证某模型输出 |
| `result = filter(y is False).count()` 普通 | 整个MC的gold为50条False；不是模型选中数 |

## 表4：四臂预期推演；非模型执行收据

| 臂 | 预期执行结果 | 预期执行过程 | 可能产生的operator结构 |
|---|---|---|---|
| LOTUS静态，任务+记录 | 首例gold目标False；实测未知，缺事实可能UNKNOWN | 直接分类3公开字段 | 固定语义分类器；必要对照 |
| LOTUS静态+完整E | 完整池尚未获得；质量/成本未知，不能预言一定错 | 完整E一次调用须先核上下文容量；另立固定范围筛选→BM25→语义判定对照 | `extract_facts → retrieve_rules → decide`，允许固定多步及缓存 |
| 逐记录Data Agent | 无本次优势结论；不能检索补出未公开个案证据 | ==定位税种/历史版本==→==检索正当理由与例外判例==→区分主张和证据→判定/UNKNOWN | `scope_resolver → reason_family_selector → evidence_check → decision`，仅设计假设 |
| 批处理Data Agent | 可以尝试摊销索引及同类规则读取；收益未知 | ==一次整理法源及年代==→==选择误解/信赖/客观障碍等候选分支==→每案核对证据 | 冻结规则索引+按语义事实选择子程序；不得把本案gold判例保留在E |

ρE=法源整理，ρP=每案事实/主张抽取，ρG=候选相同理由规则，ρR=个案履行能力及证据评价；比例/K均未知。候选家族可尝试由早期语义事实预测，但尚无执行轨迹证明。论文强制至少3次检索的Agent与top3固定RAG预算不同；其研究不能单独证明固定程序无法覆盖，也不能直接套用LOTUS性能。当前仍可能退化为固定RAG或条件分类，而不是已证实的经验编译workload。

## 收据

实际文件在`data/shared-environment-strict-plat/`；[源锁与哈希](../artifact/evidence/shared-environment-strict-plat/source.json)、[数据数量](../artifact/evidence/shared-environment-strict-plat/data-audit.json)、[20条抽样](../artifact/evidence/shared-environment-strict-plat/sample20.json)、[20条法源线索](../artifact/evidence/shared-environment-strict-plat/reference-leads20.json)、[首例跨题型原字段](../artifact/evidence/shared-environment-strict-plat/first-case-variants.json)、[首例充分性](../artifact/evidence/shared-environment-strict-plat/first-case-sufficiency.json)。未执行作者脚本/模型/API，未改数据，未构造新split，未运行质量或成本实验。
