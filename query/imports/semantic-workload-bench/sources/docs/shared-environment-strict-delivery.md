# 28个候选的下载与交付缺口总表

本表汇总已经逐个审查的结果，不增加候选或通过数。当前 **0 Strong / 5 Partial / 23 Reject**。这是下载与交付索引；完整入场表、Query×数据、DAG、方法推演见每行卡片。下载成功不代表C–G通过；表中“完整库”指固定提交的仓库文件，不表示其引用的外部数据也齐全。

| 候选及四表 | 判定 | 已取得的主要原件 | 剩余材料或硬性失败 |
|---|---|---|---|
| [annoctr](shared-environment-strict-audit-annoctr.md) | Partial fit | 原论文、完整官方库、报告与定义 | 20条定义定位不等于完整依据闭合；D/E未证 |
| [hscodecomp](shared-environment-strict-audit-hscodecomp.md) | Partial fit | 原论文、完整官方库、632条商品、4429页HTS | 商品图片/价格单位事实缺失；C/D/E未闭合 |
| [csmed](shared-environment-strict-audit-csmed.md) | Reject | 原论文、官方库与数据压缩包 | 同一长环境天然批及完整事实不足；固定检查表未被排除 |
| [clinicare](shared-environment-strict-audit-clinicare.md) | Reject | 原论文、完整官方库 | 真实受控病历/cohort未取得；30例/q及模型共识gold |
| [proact](shared-environment-strict-audit-proact.md) | Reject | 2016原始方法论文、完整官方库 | 2022方法报告及全输入未取得；程序风险分数非独立裁决 |
| [finguard](shared-environment-strict-audit-finguard.md) | Reject | 原论文、完整团队代码库 | FinGuard专属记录/规则未取得；团队库不等于数据发布 |
| [latvia](shared-environment-strict-audit-latvia.md) | Reject | 原论文、官方数据归档 | 外部依据未完整取得；30项目及异质问题 |
| [udrp](shared-environment-strict-audit-udrp.md) | Partial fit | 原论文、完整作者归档、152页Overview、1572案件 | 20条引用不是事实与规则闭合；裁决所用外部调查未冻结 |
| [trialgpt2](shared-environment-strict-audit-trialgpt2.md) | Reject | 2.0原论文、旧版TrialGPT完整官方库 | 2.0配套数据未取得；不得把旧版库当2.0完整交付 |
| [inslogic](shared-environment-strict-audit-inslogic.md) | Reject | 28页原论文 | 官方仓库/完整数据未取得；公开描述为合成案例 |
| [gdprxiv](shared-environment-strict-audit-gdprxiv.md) | Reject | 原论文、sdist及部分精确仓库子树 | 完整官方仓库未取得；原始案例PDF仍缺失 |
| [codeaccord](shared-environment-strict-audit-codeaccord.md) | Reject | 原论文、完整官方库与862条规则标注 | 实际E为13页2988词指南；固定抽取及D/E未被排除 |
| [regbench](shared-environment-strict-audit-regbench.md) | Reject | 两个完整官方仓库及827条JSON | 原论文未取得（站点占位）；完整E缺失、案例合成 |
| [chicagofood](shared-environment-strict-audit-chicagofood.md) | Reject | 完整城市官方库、2019独立研究论文、20条API记录 | 完整历史手册未取得；预测检查风险非独立政策裁定 |
| [codiesp](shared-environment-strict-audit-codiesp.md) | Partial fit | 原论文、完整官方评测库、1000报告/标签、四册2018编码书、指南 | 2018 SEDOM词典及完整许可核查未闭合；20完整病例C未通过 |
| [vetclaims](shared-environment-strict-audit-vetclaims.md) | Reject | 原论文、完整官方库75份JSON、39页标注协议 | 完整历史法源及中立输入未闭合；75案不满足天然大批 |
| [deonticbench](shared-environment-strict-audit-deonticbench.md) | Reject | 原论文、完整官方库、242条USCIS数据 | 底层完整原裁决与统一E未取得；Accepted含发回重审 |
| [cail2018](shared-environment-strict-audit-cail2018.md) | Reject | 原论文、完整官方库、984MB官方数据ZIP | 完整版本法律未取得；事实充分性/实体隔离未闭合 |
| [hicric](shared-environment-strict-audit-hicric.md) | Reject | 原论文、完整官方库、73987条申诉及1110份指引 | 完整E未取得；真实保险合同/病例事实不足 |
| [plat](shared-environment-strict-audit-plat.md) | Reject | 当前25页原论文、完整官方库、六份100例数据及一部法律 | 完整法源池未发布；每题排除源判例且100例不足 |
| [ace](shared-environment-strict-audit-ace.md) | Reject | 32页原论文、完整官方库、4700条场景 | 完整合同与场景映射缺失；场景模型生成不是真实事件 |
| [matchminer](shared-environment-strict-audit-matchminer.md) | Reject | 当前68页原论文、两个完整官方库、7695条试验空间及合成示例 | 真实患者EHR不公开；模型匹配输出不能当独立gold |
| [sara](shared-environment-strict-audit-sara.md) | Reject | 8页论文、完整代码库、官方376条数据及9份法条 | 人工构造非天然批；E短，固定执行未被排除；代码许可待核 |
| [stard](shared-environment-strict-audit-stard.md) | Partial fit | 14页原论文、完整官方库、1543咨询/55348法条 | 固定相关性q成立；D/E未知，依据充分性/实体隔离未闭合 |
| [asrs](shared-environment-strict-audit-asrs.md) | Reject | 9页原论文、全作者库、16页编码表/14页缩写表、50官方报告 | 编码表非完整定义；原实验数据未取得，C/D/E未闭合 |
| [afd](shared-environment-strict-audit-afd.md) | Reject | 原论文、完整作者库、完整401810632 bytes讨论镜像；383918讨论 | 原始百科条目和历史政策文本缺失；投票预测不是已验证规则适用 |
| [inato](shared-environment-strict-audit-inato.md) | Reject | 9页原论文、完整官方库、3380行结果CSV | 结果仅20患者；真实协议NDA，原患者输入未取得，部分标签启发式推导 |
| [bidcorpus](shared-environment-strict-audit-bidcorpus.md) | Reject | 完整原论文XML、锁定官方树、1818条专家gold及README | PDF被拒；完整11.5GB库未下载；无完整法源/采购对象连接，七标签分类不等于违规裁定 |

## 统一证据边界

- 当前28份卡片的本地链接检查见下方新版收据；只检验导航和文件存在，不验证内容、许可或下载完整性。旧22/26卡收据仅为历史。
- 尚无候选同时通过20条完整gold依据闭合、完整E强固定方法不足、以及实测语义执行家族 `1 ≪ K ≪ N`。局部条款命中、代码位置或类别计数不能替代这些证据。
- 四路表是待验证执行假设，没有LOTUS/Data Agent模型运行结果。质量、K、四类执行占比和完整成本仍未知；不能把gold栏复制成“预期模型准确输出”。
- [当前五个Partial及横向四表](shared-environment-current-five.md)是后续证据投入优先级；[五个真实例子](shared-environment-top-five-examples.md)提供短引与字段。五者都不是Strong；旧排名中的Reject对照仅是历史。
- [机器可读状态](shared-environment-strict-goal-status.json)维护判定；[卡片导航收据](../artifact/evidence/shared-environment-28-card-navigation.json)保存哈希与链接检查结果。

本增量仅整合已有证据并修正ProACT的过时H行；没有新下载、模型执行、数据划分、评分或科学有效性升级。


本轮增量：[AFD完整镜像与20独立讨论关联审查](shared-environment-strict-audit-afd.md)。当前26项：0 Strong / 5 Partial / 21 Reject；旧条目计数保留为历史。


[Inato原件/结果表核验](shared-environment-strict-audit-inato.md)：当前27项0Strong/5Partial/22Reject；3380结果行仅20独立患者，真实协议未公开。旧计数为历史。


## 2026-09-14T22:58:41.584292+08:00 BidCorpus增量

当前累计 **28项：0 Strong / 5 Partial / 23 Reject**。新增[BidCorpus核验](shared-environment-strict-audit-bidcorpus.md)：完整原论文XML与1818条专家CSV已取得；共享完整法规和关联缺失，固定七标签流程未被排除，C完整闭合0/20。PDF与完整11.5GB仓库未取得，不声称H完成。历史计数不代表当前状态。


本轮续查最新状态：**29项，0 Strong / 5 Partial / 24 Reject**。新增[C3PA排除依据](shared-environment-c3pa-in-progress.md)；上文28项为此前交付。HuBMAP ARMS正在审查，未计入通过或已审数量。


## 当前核验增量 2026-09-15T00:16:45.184140+08:00

当前已审32项：0 Strong、5 Partial、27 Reject。新增 OmniCompliance、PrivaCI、AIReg-Bench 均未通过；HuBMAP仍在审不计入。旧28项/29项数字属于历史批次。最新逐项事实见 [状态账本](shared-environment-strict-goal-status.json)，AIReg证据见 [核验卡](shared-environment-strict-audit-aireg.md)。用户至少5 Strong目标未完成。


## 当前核验增量 2026-09-15T00:37:30.713412+08:00

已判定36项：0 Strong、5 Partial、31 Reject。RegOps、PRT、DSO、GUIDE新增排除；MDACE、HuBMAP、CORTEX、SecAlert等未完成来源/环境核验，不计入已判定数。数字以[状态JSON](shared-environment-strict-goal-status.json)及各卡为准；历史批次数字保留。GUIDE已全量下载并计数，[实证卡](shared-environment-strict-audit-guide.md)。至少5Strong目标未完成。
