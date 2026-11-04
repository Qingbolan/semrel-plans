# 正式顶会候选：输入、规则与批任务可行性审计

2026-09-05，Asia/Singapore。输入/构造审计方。本轮主动搜索 ACL/EMNLP main、NeurIPS正式 proceedings、PVLDB正式论文，并对发现方的 STAR 做源码攻击。采用已读取 [pua skill](/Users/macbook.silan.tech/.codex/skills/pua/SKILL.md) 中的原始来源、前置假设验证、多角度搜索方法；不采用对人的评价。本轮不改旧审计、不改 report、不运行付费模型，不下载媒体/权重。小型公开 JSON/CSV/ZIP 在内存读取解析，外部源码未执行。

## 结论与优先级

| 候选及正式出处 | 具体共享批任务 | 可核验的改善线索 | 输入侧裁决 |
|---|---|---|---|
| **RuleArena，ACL 2025 main** | 同一航空政策下，逐旅客/行李清单计算总费用；NBA交易合法性为第二任务 | 同 GPT-4o、1-shot完整规则，航空Level1准确率 .32→.44，Level2 .16→.33，模型生成Python后执行 | **P0开发筛选**，最符合复杂手册与固定推理；问题为合成/人工设计而非真实旅客日志 |
| **Magneto/GDC-SM，PVLDB 18(8)，VLDB 2025** | 十份癌症研究表的源字段→同一736字段GDC标准候选匹配→映射审查 | Fig11固定SLM检索+同GPT-4o-mini重排优于将所有候选给LLM；无需fine-tuned版才成立 | **P0/P1真实科学数据候选**，gold是有限上下文下人工对应关系，不是无损转换gold；本轮源xlsx直链403尚未取到 |
| **Enterprise Data Engineering，PVLDB 19(2)，2025卷/对应VLDB周期** | 一批支付→匹配一张或多张发票→未匹配清单/对账覆盖统计 | Table6同Claude3.5Sonnet多表 .58→确定性整合后的平视图 .86 F1；GPT-4o .58→.64 | **P1开发筛选**，公开完整输入和关系gold；数据按企业特征构造且注入错误，不是原始生产账本 |
| **SemBench，PVLDB19(8)，VLDB2026** | 评论情绪筛选→计数/比例；电商图文语义join | 已有LOTUS等实际实现；电商中LOTUS平均准确率最好，不是Agent增益证据 | **对照库/降级**，Movie Q10存在明确题义/gold错位，不能以该低分筛优势 |
| **STAR/VideoTool，NeurIPS2025 main（发现方核录用）** | 公开视频QA中的选帧/裁剪/时序定位 | 工具确实处理像素与视频，非读取人工答案 | **方法灵感保留**，现有异质QA没有同业务谓词批规模证据 |

正式录用证明与任务有效性分开。上述是候选，不是本地复现或Agent优势结果。尤其 RuleArena 的工具提升仅实测航空，不外推NBA或税务；三种文本候选都必须包含固定程序与一次 Coding Agent 强对照。

## 1. RuleArena：明确同规则、完整默认输入、真实计算工具

正式入口：[ACL Anthology](https://aclanthology.org/2025.acl-long.27/)，ACL2025 Volume1 Long Papers pp550–572；[camera-ready论文](https://aclanthology.org/2025.acl-long.27.pdf)。官方仓库锁定 [59f60f6b4eb93a9b6d187ec781349d4f15618903](https://github.com/SkyRiver-2000/RuleArena/tree/59f60f6b4eb93a9b6d187ec781349d4f15618903)。

本轮直接读取计数：

- `airline/synthesized_problems/comp_0/1/2.jsonl` 各100条，总300。每条有自然语言 `prompt` 和生成时结构化 `info`，后者含base_price、customer_class、routine、direction、bag_list。公开推理默认只给prompt、完整规则；info可供构造核对，不把语义解析答案偷偷预先送入某个臂。
- `nba/annotated_problems/comp_0/1/2.json` 为81/89/46，总216。每条有team_situations、player_situations、operations；answer、illegal_operation、problematic_team、relevant_rules必须留private。代码中 **answer=True 表示存在非法操作**，不能按“合法=True”直接映射。
- `tax/synthesized_problems/comp_0/1/2.json` 各100条，总300，字段dict与pydantic。未进一步审计完整税务构造器，暂不以航空结论代替。
- 独立共享规则：航空 `reference_rules.txt` 与8份费用CSV；NBA规则文件约97,804字符，包含2023 CBA定义、薪资上限、自由球员、签后交易等交叉条件。

[airline/compute_answer.py](https://github.com/SkyRiver-2000/RuleArena/blob/59f60f6b4eb93a9b6d187ec781349d4f15618903/airline/compute_answer.py)真实计算基础费、超尺寸费、超重费、免费行李分配，并取适用附加费最大值。它不是从当前实例答案表读数，但属于benchmark的gold生成器，不应直接交给被测Agent后声称发现算法。公开辅助工具应是Python/算术/独立规则表查询；由Agent或固定Coding Agent自行生成逻辑。源码还固定排除bag_list第一个行李，依赖生成器确保该件可随身携带；迁移到任意旅客清单之前必须解除或显式冻结此假设。

[Table10](https://aclanthology.org/2025.acl-long.27.pdf)实证的工具是LLM自己生成Python，并执行所得代码。其“oracle math/logic”指执行器正确执行运算，不是提供gold规则路径或答案。完整政策已在原始CoT输入，因此这个差距不靠删除必要手册。Table10：GPT-4o 1-shot航空Level1 .32→.44、Level2 .16→.33；Qwen72B .19→.42、.10→.26。这是固定推理/计算提升证据，不是Agent探索胜过同资源固定程序的证据。

可构造DAG：scan旅客清单 → sem_map{旅程区域/适用豁免/行李收费分类} → calculator → project逐旅客费用 → sum。或保持单个sem_map输出总费用，内部探索是实验变量。先冻结同一政策版本、按生成模板/路线/行李组合隔离；默认LOTUS保留完整规则和同预算输出。不把旧政策当现行实际航空收费，不发送真实财务建议。

廉价反证：20–30个开发实例，逐项核对生成info与prompt一致、规则与gold代码一致；固定程序生成和Agent共享规则/执行器。若强模型直接+Python已足够，则保留为固定推理成功案例，单轨迹价值转由无轨迹Coding Agent对照检验，不预设Agent优势。

## 2. Magneto / GDC-SM：真实源表的模式匹配

正式论文：[PVLDB18(8) pp2681–2694](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)。官方代码锁定 [6620623265fc7feac0f053996e62b68a13a72a57](https://github.com/VIDA-NYU/magneto-matcher/tree/6620623265fc7feac0f053996e62b68a13a72a57)。[Zenodo14963588](https://zenodo.org/records/14963588)公开gdc-sm-data.zip，实际179,992bytes，记录MD5 d83948e4050f272b0e5564a16747535c。

内存解包核验：10个ground-truth CSV与target表；源表不在ZIP。target为736列，4478数据行，**这些行是每列不同domain values的并置，不是4478真实患者关系**。十个groundtruth对应边数：McDermott21、Wang27、Clark25、Dou32、Huang37、Gillette22、Krug10、Cao43、Vasaikar20、Satpathy22，总259条映射边；不等于259独立研究或源字段。

原始 `papers_info.json` 逐研究给出Cell/Cancer Cell补充xlsx地址、sheet名；`gdc_download.py` 读取精确sheet，并为4份表做去行、字段去tab、白种族拼写/二手烟值清洗。本轮对McDermott补充xlsx的直链读取返回403；没有据此宣称源已无法获取，也没有把已核gold/target写成完整public快照已就绪。可继续从官方等价出版入口取得原字节并核验。

具体语义风险：McDermott中同一“取材时年龄（月）”字段被标到age_at_diagnosis、days_to_birth、age_at_index。对应关系可能表示候选可用性或需要转换，并非值可直接搬移。论文明确某些对应连专家也需补充论文/询问作者，最终gold是有限上下文下预期匹配的共识。故先测“候选模式匹配”本身；若增加原论文/字段文档改善真实含义，却与这种gold不一致，必须记录gold语义边界，不能用分数下降否定资源。

Fig11在GDC上使用zero-shot retriever，同GPT-4o-mini在小候选集重排优于All Schema；这一控制比“微调专用模型打弱模型”更有启发。LLM工具化候选检索、列类型/分布/枚举检验、标准字段文档搜索可以形成固定DAG：scan source columns → candidate retrieval → semantic correspondence → output mapping。默认应提供完整候选目录及必要列内容，检索仅改变组织而不是可访问证据。独立划分按研究表而非随意拆列；只有10研究，跨研究确认方差必须披露。

## 3. 企业支付—发票匹配：关系环境确实有用，但生产真实性需缩小

正式 [PVLDB19(2)196–209，DOI10.14778/3773749.3773758](https://www.vldb.org/pvldb/vol19/p196-bodensohn.pdf)。仓库锁定 [aa1946ae4d485091884b457db720a120473e2f82](https://github.com/DataManagementLab/llmeval-enterprise-challenges/tree/aa1946ae4d485091884b457db720a120473e2f82)。读取README、论文Table6/compound pipeline与实际ZIP。

`payment-to-invoice-matching.zip` 实际6,429,129bytes，31路径，公开输入有描述性列名、非描述性SAP列名和三张发票表三种等价表示，分别有单错/多错版本：

- 多错版15,521发票、12,332支付，10,000个gold matching group；与论文数量一致。
- 单错版15,527发票、12,262支付，同为10,000组；不能误用论文多错数量代替全部版本。
- payments字段包括Business Partner、Account Number、Memo Line、Amount、Currency、Posting Date；invoices包括客户、金额、币种、开票/到期日期及多种引用号。
- matches.csv含match_category、perturbation_categories、invoice_ids、payment_ids。它可直接支持1:N/N:1关系gold与组级划分，但错误类型/匹配分组必须private。
- 示例多错记录一个支付memo列7个引用号，对应7张发票；金额和名称是可计算/比对证据。不能对候选组合独立下结论后忽略集合金额约束，也不能把尚未检查的未列组合一律当可信负例。

Table6同模型、同基础实例，多表表示相对平视图下降：GPT-4o .64→.58、Claude3.5Sonnet .86→.58（含错误与multi-match）。逆向说明确定性join/规范化可能帮助后续语义判断；它是表示/结构处理证据，不是Agent已探索出优势。论文使用2000组合（790正/1210负），并未证明全量191M笛卡尔积可行。新实验应固定候选生成规则并单独报候选召回，防止负例抽样掩盖真实漏配。

另读 `enterprise-data-integration.zip` 364,309bytes：50/100/150/200/300客户版本均含companyA、companyB拆表/合表、schema/实体匹配/最终输出gold，真实固定DAG可观测。多个规模不当独立样本重复计数。

这些是基于企业特征构造的数据与人工注入代表性错误，不能称真实原始财务日志。最小任务可为scan payment groups → retrieve候选invoice → sem_match支付含义/名称/引用 → 集合金额与币种/时间校验 → unmatched清单。固定算法也访问相同关系表、字典与运算工具。先区分“文本别名解释”的语义错误和“数值约束没执行”的固定逻辑错误。

## 4. SemBench：正式录用不消除具体任务契约问题

正式 [PVLDB19(8)1754–1767](https://www.vldb.org/pvldb/vol19/p1754-trummer.pdf)，DOI10.14778/3811243.3811249；代码锁定 [c814e3807e72d4cf876b852b17e77f3cc94575c2](https://github.com/SemBench/SemBench/tree/c814e3807e72d4cf876b852b17e77f3cc94575c2)。读取movie README、LOTUS runner、实际Q10自然语言和gold SQL、电商builder。

Movie评论情绪有1,375,738可用行的来源规模、隐藏scoreSentiment和明确filter/count/query实现，确为可复用语义批。当前未核验额外文档/工具能够提高其准确率，不能仅从存在大量行推断值得做Agent。

具体淘汰Q10：自然语言文件要求每条评论1–5打分并按影片求均值；[gold_sql/Q10.sql](https://github.com/SemBench/SemBench/blob/c814e3807e72d4cf876b852b17e77f3cc94575c2/files/movie/query/gold_sql/Q10.sql)却直接返回Movies.audienceScore。二者不同尺度、不同统计对象，未见等价证明，不能拿该低分作为关键语义瓶颈证据。电商builder还强制保留43行以确保部分查询有解，应记录为构造选择。论文电商LOTUS本身具有最佳平均准确率；不作为本轮Agent潜力主推。正式paper中的5个场景也不能把repo新增场景自动当已发表评测。

## 5. 对发现方 STAR/VideoTool 的一轮源码攻击

正式录用由发现方从 [NeurIPS2025 main proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbdd9525c5ecd3a03fee43d8fd64bd83-Abstract-Conference.html)核验。输入侧锁定 [e252f8b9433b1b02aba3f59ef2200f3d91cff74e](https://github.com/fansunqi/VideoTool/tree/e252f8b9433b1b02aba3f59ef2200f3d91cff74e)，读取FrameSelector、PatchZoomer、TemporalGrounding、dataset.py及testcase。

- frame_selector根据已有帧描述选择未采样时段，再真实增加视频帧；patch_zoomer以cv2裁四象限/中心并resize；temporal_grounding以decord提取96帧并调用Grounded-Video-LLM。上述不是读答案工具。
- tools/python_generator.py为空，不能根据目录名宣称该工具已实现。
- 唯一演示QA询问视频中的人类演化阶段；dataset.py对接NextQA/VideoMME等异质QA。未发现同业务谓词有足够独立视频规模的证据。
- 缺视频的记录被continue过滤，迁移时必须报所有原ID与missing coverage；固定对照也应得到相同视频与帧/像素预算。

发现方已收到：保留主动选帧和局部感知机制作为启发，当前不能直接晋级固定任务batch环境。另收到OralGPT-Plus线索，但未在本轮重复审计或给出已验证结论。

## 未主推的搜索命中与验证边界

LegalBench确为[NeurIPS2023 Datasets and Benchmarks正式录用](https://proceedings.neurips.cc/paper_files/paper/2023/hash/89e44582fd28ddfea1ea4dcb0ebbf4b0-Abstract-Datasets_and_Benchmarks.html)，文件树包含大量共享规则任务，但本轮未完成独立资源增益与具体新任务审计，不用总162任务数替代可行场景。ComEM是COLING2025 main，序列化研究为NAACL Findings2025，SARA改进论文为NLLP workshop；均不混成用户指定的ACL/EMNLP main。Inducing Reasoning Primitives from Agent Traces（arXiv2606.02994）高度邻近单轨迹方向，但未核到正式录用，只有新颖性审查线索。

共完成4个主动候选的正式出版/原始文件检查及1个发现方候选源码攻击。网络读取解析成功；McDermott官方补充文件403、猜测SemBench两个电商query位置404后改读实际movie路径。小ZIP仅内存解包，没有建立数据快照或执行外部下载脚本。模型、prompt实验、种子、推理成本不适用；软件测试0（纯研究文件审计），没有本地实测优势。账本由root统一追加。
