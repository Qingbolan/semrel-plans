# 第二十二增量：UDRP统一域名争议政策（补证中）

本轮找到新的优先方向，未计入合格湖。已下载[NDSS2026原论文](https://astrolavos.gatech.edu/articles/Manuscript_UDRP_final.pdf)18页/1,224,532bytes，以及[WIPO官方Overview3.0含政策和细则](https://www.wipo.int/amc/en/docs/2023_overview3.pdf)152页/2,055,727bytes。PDF创建日期2023-04-18、内容标记©2017，不能称其为2017下载快照。WIPO Overview总结解释共识，不是严格有约束力的判例法。

[作者网站](https://boladjivinny.github.io/)与论文均指向[完整代码/数据归档Zenodo16954717](https://doi.org/10.5281/zenodo.16954717)。单个artifacts.zip843,037,756bytes，**下载尚在进行**，进程session11183；没有重启。成功后脚本将检查Zenodo文件大小及MD5，再重命名并写SHA256收据。当前不能声称完整仓库已下载。

本轮用ZIP本地文件头读取已经完整收到的条目，逐项核对长度/CRC，不执行作者代码，也没有第二次下载归档。完整收到的`data/Jan2023-Aug2024-disputes.jsonl.gz`含12012条有正文记录，其中WIPO6749条。全部WIPO日期字段仅年份，保守取标记2024的2028条作后续审计候选，未称精确日期确认集。这个分片CRC有效不替代尚未完成的整个归档MD5校验。

原资产`data/shared-environment-audit-20260908-v22/`；可重跑前缀检查脚本与统计、私有开发例在`artifact/evidence/shared-environment-audit-20260908-v22/`。等待归档完成后须重新核对完整清单、许可和数据字段来源。先前一次pdftotext发生在论文尚未下载完成时失败，成功下载后已重跑；不以那个失败推断下载终止。

## 具体结构

| Query | 数据湖 数据1：共享E | 数据湖 数据2：items | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 同一UDRP及冻结解释指引下，逐案判断应否转移域名 | WIPO Overview3.0，152页含政策及细则；有权利、合法利益、恶意、程序及例外 | 收到的近年分片WIPO6749案；标记2024的2028案待核 | 每案原始公开文书text，包括事实、主张、分析与结论，必须拆分 | provider status及最终Decision；需核验其来自provider目录还是模型提取，并处理混合裁决/多域名 |
| 开发例D2024-0001，decathlonag2r.com | UDRP三要件与Overview对混淆、冒充、恶意的解释 | 正文事实：既有DECATHLON商标、2023-11-27域名注册、冒充车队网页、后续要求有偿出售 | 事实/双方主张位于§4/§5，专家分析§6、结论§7。主张必须标记为主张，不当既定事实 | metadata Transfer；文末也命令transfer，日期2024-02-19。该例已开发曝光 |

这里有具体规则依赖，而非只有长文本：Overview§3.8.1通常不认为商标权形成前的注册具有恶意；但§3.8.2规定针对新生商标权的例外，同时§3.8.1要求区分域名最初创建和当前被申请人取得的日期。该规则是共享E的一部分；开发例并非特意选择的§3.8例外案例，不能据此声称验证了该例外。

| 类python的DAG | 具体数值 | 当前状态 |
|---|---|---|
| `scan(recent_shard).where(provider==WIPO)` | 6749，全部有text；2024年份标签2028 | 实际结构统计，非科学通过 |
| `split_document(facts, party_contentions, private_reasoning, private_decision)` | 开发例能定位§4/§5与§6/§7 | 尚无全批解析/泄漏审核；不把全文给模型 |
| `sem_map(apply_udrp, E=frozen_overview).sem_filter(outcome==transfer)` | 单例参考为Transfer，模型未运行 | 多域名混合裁决不能默默当单Boolean |
| `project(case_or_domain_id).count(); score(private_gold)` | 单位尚需固定case或domain | 不用全部case数冒充独立domain数 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| D2024-0001目标Transfer；未实测，不预设失败 | 在同样已剥离裁决的事实/主张与完整E上，固定检索规则、评估三要件及例外、返回决定；允许共享预处理 | 同一目标，是否改善未知 | ==辨认事实、双方主张、缺省答辩==→==查混淆/合法利益/恶意规则与适用例外==→形成有来源的三要件判断→决定。不得读本案§6/§7或联网搜索其结果 | `UDRPOperator(E_hash, facts_schema, element_checks, exception_checks, outcome_set, abstain)`；独立分支处理日期/权利/合理利益，不写死本例域名和结果 |

必须保留的缺口：完整归档下载与校验；provider结果来源；年份精度；原文事实与裁决泄漏；支持材料/缺省程序的证据充分性；Overview自带历史案例与当前样本重叠；多个provider补充规则差异；case/domain输出粒度；多人多域名混合处置。不可把“被申请人未正式答辩”写成自动Transfer规则。无需先证明Agent优胜，但上述任务输入和gold语义必须清楚。

本轮保险搜索另发现InsClaimQA；原文明确其案件由事实QA重写，故不作为真实索赔工作流候选，未下载仓库也未列入合格表。未对医疗保险作专业判断。
