# 严格口径：已审来源八维比较与五个真实实例

> 当前累计28项入场判定：0 Strong / 5 Partial / 23 Reject。下方八项与15项表是明确保留的历史快照，其局部计数不是当前总数。最新查证顺序及本轮证据更新见末节；这些名次不是合格benchmark名次。

**以下为历史八候选快照；当前排名以[五Partial横向表](shared-environment-current-five.md)为准。**

这是八个已审来源中的**查证优先顺序**，不是五个合格 benchmark。当前 0 Strong、3 Partial、5 Reject。前三区分后续证据投入；第四、第五保留为失败条件清楚的比较实例，不建议启动方法优势实验。每项原论文、完整来源下载收据、20条审查边界、四路推演和十问见链接卡片。本轮只整理已有证据，没有新下载或模型执行。

## 八维评分

分数表示当前材料支持程度，不是模型性能。`?` 表示没有证据，不能当作0或补成平均分。复杂度：0短规则、1中等、2大型多层环境；N：0不足200、1为200–999、2至少1000（提及与文档分开）；gold：0非独立目标标签、1独立但支持条件未闭合、2独立且证据完整；定位：0未定位、1位置/局部支持、2至少20条完整闭合；静态不足：0已有固定实现直接定义目标、1局部对照、2同资源强固定对照不足；分支：0算术/关键词、1固定语义比较、2存在多种语义判断线索；K/N：只有观测执行家族才能评分；真实性：0合成、1真实来源经人为抽样构造、2真实裁决/工作记录。分支2也不证明有多个执行程序。

| 顺序/来源 | E复杂度 | N | gold质量 | 依据定位 | 完整E静态不足 | 分支条件 | K/N形状 | 真实性 | 判定 |
|---|---:|---|---:|---:|---|---|---|---:|---|
| 1 [HSCodeComp](shared-environment-strict-audit-hscodecomp.md) | 2：4429页税则 | 1：632商品 | 1 | 1 | ? | 2：材质/用途/估值等线索 | ? | 1：真实商品、类别平衡 | Partial |
| 2 [UDRP](shared-environment-strict-audit-udrp.md) | 2：152页解释环境 | 2：1572提取裁决 | 1 | 1 | ? | 2：合理使用/注册时点等线索 | ? | 2 | Partial |
| 3 [AnnoCTR](shared-environment-strict-audit-annoctr.md) | 2：官方定义112331词 | 2：3348技术提及；120篇专家层报告 | 1 | 1 | ? | 1：动作与定义比较 | ? | 2 | Partial |
| 4 [CSMeD-FT](shared-environment-strict-audit-csmed.md) | 0：最大review criteria1039词 | 0：同review最多171篇 | 1 | 1 | ? | 1：资格检查表 | ? | 1：开放全文子集 | Reject |
| 5 [Latvian Procurement](shared-environment-strict-audit-latvia.md) | 1：清单及不完整外部法规 | 0：30项目/q | 1 | 1 | ? | 1：固定前置分支+语义判断 | ? | 2 | Reject |
| — [CliniCARE](shared-environment-strict-audit-clinicare.md) | ?：完整病例资源未取得 | 0：30例/q | 0：主要为模型共识 | 0 | ? | ? | ? | 1：真实病历派生场景 | Reject |
| — [ProACT](shared-environment-strict-audit-proact.md) | 0：1858词指标定义 | ?：完整输入未取得 | 0：风险代理非裁决 | 0 | 0：发布固定计算 | 0 | ? | 2：真实采购来源 | Reject |
| — [FinGuard](shared-environment-strict-audit-finguard.md) | ?：未取得完整执行环境 | 2：论文1020对；本地0 | 1：专家评合成输入 | 0 | ? | 1：分类定义 | ? | 0 | Reject |

不加总：任一硬性失败不能由其他高分抵消，未知的D/E尤其不能被环境页数抵消。HS优先是因为有明确的不同中间事实要求；UDRP次之是因为有正式裁决但外部调查和回顾性叙述风险；AnnoCTR的直接定义链接固定基线更强。没有证据支持统计显著的名次差异。

## 数据湖 × Query：真实记录

下表每列只有一个固定q，避免把同湖的不同问题数量当N。E短引只用于解释审计，不是根据测试gold给模型选取资源。

| Query/项目 | 数据湖1：HSCodeComp | 数据湖2：UDRP | 数据湖3：AnnoCTR | 数据湖4：CSMeD-FT | 数据湖5：Latvian Procurement |
|---|---|---|---|---|---|
| 固定q | 商品→10位HTS | 域名争议→是否给予救济 | 指定提及→ATT&CK技术 | 同review论文→include/exclude | 项目→固定第4题答案 |
| 真实记录/字段 | JSONL task591；玻璃管套装，each pack20，price8.3375USD | D2024-0001；decathlonag2r.com；注册2023-11-27；曾模仿车队网站，后空白，有出售情节 | linking train:3782；运行时解密循环恢复二进制内字符串 | CD001431-bib-0035；四臂RCT，三实验臂及可信公共网站对照 | APP_DI_20202ERAF_AK；q4前置No，主答案No |
| E位置/短引或概括 | 官方JSON祖先行20818等；“Valued over $5 each” | Overview 3.0 §3.3被动持有；仍需逐项满足三要件，空白网站不自动排除恶意 | mitre_entity.jsonl:515；“decode or deobfuscate” | CD001431.pub5 criteria：仅两种决策辅助工具间的比较排除；多实验臂本身不是排除项 | questions.yaml nr4、q0；MK107第196项引用；前置No按文档应输出NA |
| 源gold | 7013999090；专家标签 | Transfer→RELIEF_GRANTED；正式裁决 | T1140；专家链接 | included；综述筛选标签 | No；源答案保持原样 |
| 依据闭合边界 | 包价/件价未知；不能由8.3375自动满足每件门槛 | 本例线索可解释，不称20案完整闭合或独立重新裁决 | 局部动作符合定义；未证明必须探索大型E | 摘要与规则局部一致，未完成全文/试验实体独立复核 | 这是源规则/答案冲突实例；未判定专家错误，不能当干净评测样本 |
| 类Python DAG | `facts=sem_map(x); paths=retrieve(E,facts); y=sem_map(resolve_notes_and_value,facts,paths)` | `facts=sem_map(x); refs=retrieve(E,facts); elements=sem_map(facts,refs); y=all(elements)` | `c=retrieve(E,mention_context); y=sem_map(link,c)` | `facts=sem_map(paper); y=sem_map(eligibility,facts,E)` | `pre=sem_map(q0,x); y='NA' if pre is False else sem_map(q4,x,E)` |

DAG里的`sem_map`是语义步骤，`retrieve`、布尔组合、条件分支是固定普通控制；上述程序都可作为竞争基线，不是已经学出的算子。读取文件、扫描记录、汇总清单省略以突出决定gold的关键结果。

## LOTUS / Data Agent推演与可能的算子

“目标”指源gold或一致性约束，**不是已经观测的执行输出**。LOTUS指传统固定流程，可用同一公开E、固定检索、语义列及分支；逐记录Agent也不能取得private解释或额外网页。现有证据不允许给任一方法编造准确率。四臂完整资源条件见各卡。

| 实例 | LOTUS关键操作预期结果 | LOTUS预期过程 | Data Agent关键操作预期结果 | Data Agent预期过程（可观察探索） | 可能产生的operator结构，尚未提取 |
|---|---|---|---|---|---|
| HS591 | 不能可靠指定唯一code；源目标7013999090但缺件价口径 | 固定抽材质/套装数量/单位价值→树检索→规则比较→不足标记 | 同样应保留事实不足，不预期凭探索恢复gold | ==查玻璃器皿祖先与估值门槛==→==核公开价格单位==→不足 | `extract_facts→resolve_value_unit→classify_or_unknown`；非玻璃专用ID特例 |
| UDRP0001 | 可检验目标RELIEF_GRANTED；实际输出未知 | 固定三要件事实列→相关解释检索→逐项判定→AND | 可检验相同目标；尚无高于固定流程的依据 | ==查仿冒/出售与被动持有规则==→核注册时点及各要件→结论 | `facts→elements→conjunction`，允许固定早停；不同引用未必新家族 |
| AnnoCTR train:3782 | T1140是可合理期待的局部链接，未实测 | 候选检索→定义比较→归一ID | 同一目标T1140；不预期必有额外收益 | ==查询解密/反混淆定义==→核运行时动作→链接 | `retrieve→link→normalize`，很可能就是统一固定程序 |
| CSMeD0035 | included是局部证据支持的目标，未实测 | 固定抽设计/辅助工具/对照→资格表 | 同一目标included；增加探索未必改善 | ==定位对照组与多臂比较排除条件==→识别有效对照→include | `extract_design_and_comparator→eligibility`；可一次由E生成 |
| Latvia q4 | 遵从文档分支会输出NA，与源No冲突 | 前置语义判断→普通条件分支 | 没有可辩护的“更准确”预期；应报告契约冲突 | ==核前置题及适用条件==→发现gold/规则不一致 | `prerequisite→conditional_question`；先修独立契约再评模型 |

UNKNOWN/冲突报告是建议实验状态；原gold未提供统一不足标签，不能把这些输出直接计为原标签正确。

## 是否值得第一批实验

| 来源 | 当前适合做什么 | 最大风险/最可能击败方法的baseline | E-only能否覆盖、会否退化分类 | 家族复用与ρ拆分 |
|---|---|---|---|---|
| HSCodeComp | 先做20条独立事实与条款闭合；不是立即性能比赛 | 缺图/价格口径；固定税则树+语义事实列+排除复核 | 能覆盖树及共享规则；可能由统一层级分类程序完成 | ρE索引，ρP事实抽取，ρG材质/功能/价值模板假说，ρR事实冲突；K未知 |
| UDRP | 先审公开事实是否足以重现裁决、补外部调查收据 | 回顾性泄漏/外部知识；固定三要件RAG与E-only规则程序 | 很可能覆盖大量通用推理；不能以不同条款号证明不同程序 | ρE解释索引，ρP要件检查，ρG合理使用/时点分支假说，ρR个案事实；K未知 |
| AnnoCTR | 构造无私有字段、实体隔离的链接开发控制 | 明示ID/概念词；预编码检索+固定链接器 | 很可能就是条件实体链接，预处理可覆盖大量共享成本 | ρE定义索引，ρP检索链接，ρG未观测，ρR动作解释；K未知 |
| CSMeD | 作为短criteria控制，不补入严格目标 | N171及试验关联；固定资格表+全文事实抽取 | 很可能主要由固定语义列与资格表覆盖 | ρE规则编译，ρP同表，ρG未观测，ρR研究设计；K未知 |
| Latvia | 仅做源契约一致性检查；当前不做优势实验 | N30及前置矛盾；固定条件DAG+RAG | 已有明确固定分支；语义任务仍是证据判断 | ρE清单解析，ρP固定DAG，ρG未观测，ρR项目解释；K未知 |

所有ρ比例、耗时、K与方法质量均未测。UDRP常量正例可得1513/1572=96.2468%但拒绝类召回0，这是标签算术，不是LOTUS结果；标签偏斜也不能单独证明K=1。批Agent共享索引的收益属于ρE，不能冒充从单轨迹学习ρG。

本轮补齐已审来源的比较交付，未增加或升级候选。完整目标仍需继续逐个查证，尤其C20闭合、D强固定比较与E真实执行轨迹。


## CodiEsp 增量后的查证 Top 5（15 项已判定）

这是证据投入优先顺序，不是五个可用 benchmark；不按未知指标加总。HSCodeComp、UDRP 保留前二，CodiEsp 加入第三，AnnoCTR 第四，CSMeD 仅作第五个淘汰比较实例。其余候选详见统一入口，不因数量达到15称任务完成。

| 来源 | E复杂度 | N | gold质量 | 依据定位 | 完整E静态不足 | 分支条件 | K/N | 真实性 |
|---|---:|---|---:|---:|---|---|---|---:|
| HSCodeComp | 2 | 1：632商品 | 1 | 1 | ? | 2 | ? | 1 |
| UDRP | 2 | 2：1572裁决 | 1 | 1 | ? | 2 | ? | 2 |
| [CodiEsp](shared-environment-strict-audit-codiesp.md) | 2：2787页 | 2：1000病例报告 | 1 | 1：20例地址审查 | ? | 2：部位/侧别/术式等线索，非已测执行家族 | ? | 1：真实报告模拟编码 |
| AnnoCTR | 2 | 2：3348提及，但120文档 | 1 | 1 | ? | 1 | ? | 2 |
| CSMeD-FT（Reject比较） | 0 | 0：171/同review | 1 | 1 | ? | 1 | ? | 1 |

CodiEsp 的第一步应是任务范围与全规则闭合，而非 Agent 优势实验：真实 `S1139-76322017000100010-1` 的否认呕吐仍标 `R11.10`，说明文本编码不能改称临床症状判断；操作例 `S1698-44472005000300015-1` 的 MRI 目标 `BN39` 与任务 G12.2 允许四字符的粒度有关。详细字段、E规则、DAG、两种方法目标和四臂均见新增卡。最强未排除基线为固定提及抽取＋候选检索＋编码规则检查；E-only可消除版本读取、索引及任务粒度规则的反复解析。家族复用和ρG仍是假说，不能凭长手册或代码数量证明。


## 当前21项后的证据投入顺序

本次逐项回读四个Partial卡片的既有缺口，并对CodiEsp补了一条MRI代码到分类表及粒度规则的局部链。名次不按未知指标加总；仍然没有Strong。第五项CSMeD仅用于短criteria控制，不能补足四个Partial为五个。

| 顺序 | 候选 | 已有证据最具体的下一步 | 不能被这一检查证明的事 |
|---|---|---|---|
| 1 | HSCodeComp | 恢复图片/单位价值等必要事实及与税则版本关系，再继续20例闭合 | 找到税则祖先不能证明商品材料/用途/估价事实 |
| 2 | UDRP | 逐案区分提交事实、裁判分析、裁判员外部调查，再固定历史规则 | 正例占96%既不证明K=1，也不证明复杂家族存在 |
| 3 | CodiEsp | 用完整任务规则核对20例所有标签，区分词表定位与临床/任务依据；MRI局部链已补 | 一个四位编码解释不能证明完整病例闭合或Agent必要 |
| 4 | AnnoCTR | 与同资源固定候选检索/链接流程比较前，排除明示技术ID和私有字段 | 大型定义库不自动意味着必须动态探索 |
| 5 | CSMeD（Reject控制） | 保留短criteria及同review N171限制，不作为严格候选推进 | 不能跨review拼N或把普通资格表改名复杂环境 |

CodiEsp当前具体例子的E地址为操作分类书PDF480页/印刷461页，BN3→解剖9；任务G12.2规定四/七字符粒度。正文给双侧ATM的MRI而造影剂未说明，gold为BN39。正确的固定对照可以用技术/部位/造影剂语义列加表查找与粒度规则；这条规则仅依赖E，编译开销应归ρE，不能计作经验发现ρG。准确率、K和各ρ比例仍未知。

| Query | HSCodeComp | UDRP | CodiEsp | AnnoCTR | CSMeD控制 |
|---|---|---|---|---|---|
| 固定输出 | 商品HTS10位 | 是否给予域名救济 | 全部操作代码集合 | 提及的ATT&CK技术 | 同review纳入与否 |
| 本轮沿用真实例 | task591 | D2024-0001 | S1698-44472005000300015-1 | train:3782 | CD001431-bib-0035 |
| gold目标 | 7013999090 | RELIEF_GRANTED | MRI局部bn39，整例另有bn07/bn29 | T1140 | included |
| 未解决的关键边界 | 价格单位及完整属性 | 外部调查/裁判事实来源 | 整例所有标签规则未闭合 | 定义链接是否需大E探索 | N不足，criteria短 |
| 类Python固定对照 | `facts→tree→value_guard` | `facts→three_elements→AND` | `slots→code_table→specificity_guard` | `retrieve→link` | `facts→eligibility_table` |

上述五列仍是查证或控制样例，不是五个执行成功结果；详尽四臂过程及许可/下载收据在各卡，CodiEsp新增MRI收据供核对。

STARD在固定任务口径复核后归Partial：它是统一法条选择任务，不能因输出非裁定而淘汰。暂不改变Top5证据投入顺序；缺少C/D/E/G完整证据，不构成第六个Strong。

## 当前五个Partial的统一比较

[现行五候选八维表、Query×数据、DAG、四路推演及真实例子](shared-environment-current-five.md)。该页替代旧Top5作为当前比较入口；旧名次为历史。


本轮增量：[AFD完整镜像与20独立讨论关联审查](shared-environment-strict-audit-afd.md)。当前26项：0 Strong / 5 Partial / 21 Reject；旧条目计数保留为历史。


[Inato原件/结果表核验](shared-environment-strict-audit-inato.md)：当前27项0Strong/5Partial/22Reject；3380结果行仅20独立患者，真实协议未公开。旧计数为历史。


## 2026-09-14T22:58:41.584292+08:00 BidCorpus增量

当前累计 **28项：0 Strong / 5 Partial / 23 Reject**。新增[BidCorpus核验](shared-environment-strict-audit-bidcorpus.md)：完整原论文XML与1818条专家CSV已取得；共享完整法规和关联缺失，固定七标签流程未被排除，C完整闭合0/20。PDF与完整11.5GB仓库未取得，不声称H完成。历史计数不代表当前状态。
