# 正式顶会场景搜索：研究严谨性与优先级

日期：2026-09-05，Asia/Singapore。研究攻击方独占文件。沿用本任务已读现行工作契约；本轮阅读 pua 技能，仅应用多路径搜索、原始证据核对、先验证后归因的方法，不采用评价他人的话术。没有模型推理、训练、图像/权重下载或新数据构造；下载一份小型 CaRL-EM 正式 PDF 到临时目录做 pdftotext 核表。账本由 root 统一更新。

## 结论与优先级

按当前目标，文本结构候选应优先 **实体匹配 → 生物医学 schema matching → 同语义表格事实核验**。三者均有正式研究论文入口，前两者的共享任务比任意视频 QA 更自然。文档不是唯一允许资源：候选关系、值分布、比较/筛选算子和固定计算，也能支持用户接受的固定推理提升路径。

| 优先级 | 具体场景 | 正式录用依据 | 当前支持什么 | 下一项最便宜的证伪 |
|---|---|---|---|---|
| P0构造候选；CaRL仅审计近邻 | 同产品/引用实体的候选匹配，输出一个 match 或 NONE | [ComEM COLING2025 main](https://aclanthology.org/2025.coling-main.8/)；[CaRL-EM ACL2026 long](https://aclanthology.org/2026.acl-long.1258/) | 独立匹配、候选比较、固定组合、策略控制的真实近邻 | 固定同一 source family 和候选关系，复跑同模型 pair/listwise/fixed；先核 Avg 与原始预测 |
| P1 | CPTAC 研究表列映射至共享 GDC schema | [Magneto PVLDB18(8),2025](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf) | 真实来源、新人审对应关系、固定检索+重排胜 all-schema 的线索 | 看源表能否重建；审歧义映射，完整 descriptions 加入后 gold 是否仍适用 |
| P2 | 同一类数值/量词断言对表格的真伪判断 | [Chain-of-Table ICLR2024 Conference](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f53fd88a4340063ecd258c0ae9948b40-Abstract-Conference.html)；[TabFact ICLR2020录用列表](https://iclr.cc/virtual/2020/papers.html?filter=titles) | 同模型真实表格、原始 claim gold、可执行表操作提高判断质量 | 先数同业务断言 family 的独立表，不用任意 claims 合批；现代直接强基线可能消除 gap |
| 近邻/备用 | 商品实体匹配的解释蒸馏 | [EMNLP2024 main.352](https://aclanthology.org/2024.emnlp-main.352/) | 解释监督可改善跨域泛化，数据能支持 same-entity 任务 | 监督和小模型训练成本须披露，不能解释为同模型工具推理因果 |

论文录用只通过来源门槛；不自动满足数据可达、语义稳定、无泄漏或同预算因果要求。这里的 scan→semantic step→project/aggregate 是本研究要构造的外层，不声称原论文已有完全相同查询。

## 1. 实体匹配：优先但不直接复述 CaRL-EM headline

**venue 双重核验。** Anthology 页标明 ACL2026 Volume1 Long Papers，正式 PDF 首页写 July2–7,2026、27281–27293。不能因 arXiv 最近发布就降为未录用，也不能把正式 7 个目标 benchmark 误说成 8 个测试集：AB 用于训练，另 7 个用于迁移。[正式PDF](https://aclanthology.org/2026.acl-long.1258.pdf)。

**场景契约。** 冻结 source/target 实体表与 blocking，外层为 `scan anchors → obtain frozen candidate relation → sem_map(match-or-NONE) → project matched ID pairs → downstream join`。完整输入的直接方法可以一次看 anchor+全部候选，也可以逐 pair；两者都是必须保留的直接基线。clean-clean 的至多一个匹配假设必须核对，不能移植到脏表多别名聚类后仍强制单选。pair gold 支持匹配边，不自动支持产品信息融合/数量去重的全部正确性。

**CaRL-EM实测设计的界限。** 原文使用 top10 blocking、每目标400 anchors，300有match和100无match；MATCH/COMPARE采用Flan-T5-xl，SELECT可换后端；策略先在AB用PPO训练。它提供局部动作策略研究的直接近邻，但不是单示范、不是纯同一个LLM、不是已测外部手册。成本表把训练、测试拆开，CPU推理成本按零假设处理；本项目必须实测/标未知而非继承零。[正式PDF §3–4、Appendix F](https://aclanthology.org/2026.acl-long.1258.pdf)。

**审计备忘录：具体核表问题，不作为最终推荐主依据。** 以 pdftotext 抽取正式 PDF 第7页 Table2，Python 对7域数作均值：

| 行 | 7域算术均值 | 表中 Avg |
|---|---:|---:|
| Matching | 44.41714 | 46.66 |
| Comparing | 56.50571 | 58.08 |
| Selecting | 70.47857 | 69.94 |
| COMEM | 73.22429 | 74.25 |
| CaRL-EM | 76.09286 | 76.09 |

若采用不同权重应另给定义；未经原始输出核算不直接引用宏观差距。逐域同样不是处处优胜：AG与WA的COMEM强于CaRL；IM的直接Selecting强于CaRL。因此应固定一个有来源的领域，报告全部预选实体，而非按最佳域挑成功。Appendix Table7的训练16.45、测试0.13、总16.58503，与COMEM0.59503是不同摊销位置；不能以推理便宜证明本批完整成本更低。Table10还单列训练阶段模型调用0.04+0.18+0.32，是否包含于Table7训练项需核收据。[正式PDF Tables2、7、10](https://aclanthology.org/2026.acl-long.1258.pdf)。

**可执行性。** 本次 PDF 搜索未找到 GitHub 链接，搜索未核验独立 CaRL 完整代码发布，不称即装即跑。ComEM 正式论文确认 matching/comparing/selecting 和固定组合；应优先用其开放数据/实现核对，再把CaRL列为策略强近邻。[ComEM正式PDF](https://aclanthology.org/2025.coling-main.8.pdf)。

最低比较：同一 backbone 的 pairwise、一次 listwise（含 NONE）、固定 compare→select、同预算反复判断、Data Agent；允许全部方法看相同候选关系。冻结候选召回并另报blocking失败；按实体/原来源分割，同一实体跨不同pair不能重复计独立N。若一次listwise已够好，记录环境不满足质量差距；若固定比较显著提升则保留，不必Agent动态胜出。单轨迹另对比无轨迹Coding以及CaRL类多episode训练成本。

## 2. Magneto/GDC：共享目标自然，手册增强有 gold 语义风险

**录用与源。** 正式 PVLDB论文页眉、卷页和 DOI 验证通过。官方代码卡给 GDC资源的Zenodo入口；输入攻击方实读后确认10 study 的对应关系。真实数据来自研究补充表，不是把合成表规模当真实场景。[论文](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)、[官方库](https://github.com/VIDA-NYU/magneto-matcher)。

建议外层：`scan study columns → retrieve target candidates → sem_map(semantic correspondence) → emit mapping pairs`。任务是对应关系，不能直接升为无损ETL转换。工具可以是列值采样、候选检索、单位/类型检查与共享数据字典。全部方法拿同一必要上下文，完整表对照不能刻意用超窗口序列化制造失败。

原文Fig11有同GPT-4o-mini all-schema 与零样本检索+重排对照，适合固定程序路径；fine-tuned版本另含合成训练。MRR与Recall@GT是排序指标，不是自动映射准确率。尤其Recall@GT使用gold数量来截取排序，只能用于评分，不能作为执行时可知top-k。[论文§6.4、定义2.3](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)。

**GDC 单域可引用的对照。** §6.4给出固定k=5时，零样本检索+GPT-4o-mini重排MRR0.780、Recall@GT0.475，对应bipartite为0.731/0.375。这是LLM重排相对图算法增益，不是Agent相对同LLM直接调用的数字；Fig11 all-schema曲线只作定性同backbone线索，本轮没有把图上坐标估读成精确值。Table5的GDC fine-tuned-LLM在struct-aug/llm-aug下MRR0.798/0.866，是训练数据消融，不能拿来解释查询时文档增益。跨GDC/Magellan/Wikidata与fabricated部分不汇成“全是真实数据”结论。

**具体资源/gold攻击。** 论文明确构造时舍弃GDC descriptions，只保留名字/域值；部分真实语义需原论文/数据生产者澄清，最终gold是有限上下文下“用户预期”的共识。现在加完整定义/原文档，可能揭示原对应并非精确意义相等。应先审如 age_at_diagnosis、age_at_index、days_to_birth 的歧义，不能把查文档后不符旧gold解释为Agent退步，也不能按模型预测改gold。[论文§5](https://www.vldb.org/pvldb/vol18/p2681-freire.pdf)。

输入攻击方只读资源复核：Zenodo版本14963588压缩包179,992bytes，10份gold共259边；target为736列的域值堆叠，不是4478真实患者关系。部分源属性对应多个target概念。源表需按papers_info/gdc_download从出版商补充xlsx重建，不能把gold包当输入已齐全。详情由输入方文件记录。

最低试验：先冻结两份可重建source study作开发、其余study留确认；逐映射审一对多/模糊等价，不用待测模型参与gold修订。只测correspondence清单和排序；真要下游标准化，需要另建单位转换/语义保真契约。数据集只有10源study，按列数报告样本时仍按study做不确定性分析。

## 3. Chain-of-Table/TabFact：实证明确，批任务需缩窄

ICLR2024官方proceedings明确Conference；原TabFact也在ICLR2020官方录用列表，原数据论文为真实Wikipedia表与人工构造断言，不能称真实业务审计记录。[录用页](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f53fd88a4340063ecd258c0ae9948b40-Abstract-Conference.html)、[TabFact正式PDF](https://openreview.net/pdf?id=rkeJRhNYDH)。

同GPT3.5的TabFact direct70.45、Chain-of-Table80.20，Binder79.17；同PaLM2为77.92→86.61，Dater84.63。工具/固定推理环境线索成立，但强baseline差距明显小于直接差距。原方法29个手工demo、多轮操作，select row/column还采样8次；不是同预算或一次示范结果。[正式PDF Table1、AppendixC](https://proceedings.iclr.cc/paper_files/paper/2024/file/f53fd88a4340063ecd258c0ae9948b40-Paper-Conference.pdf)。

建议仅取同一类型业务断言，例如同类比赛表中的“某实体是否满足指定期间最高/至少N次条件”，必须先统计有gold且独立表的真实family。任意claim都叫verify并不能证明一次轨迹可复用语义。当前表格是必要输入，参考文档并不是该环境现成特征；工具优势主要来自取值/组合/执行。原官方库注明cleaned TabFact raw2clean，须核清理是否保留全部必要证据、是否与gold驱动选择有关。[代码](https://github.com/google-research/chain-of-table)。

## 4. 其他正式候选与排除边界

- [EMNLP2024实体匹配解释蒸馏](https://aclanthology.org/2024.emnlp-main.352/)正式main通过；适合作为解释监督/小模型泛化最近邻。它不是本轮优先same-model tool gap证据。
- [STAR NeurIPS2025正式PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/bbdd9525c5ecd3a03fee43d8fd64bd83-Paper-Conference.pdf)的工具时空推理是新视觉方向。研究侧仅核正式页眉；方法表与实际工具由另两方审计。视频family需先固定一个行为/时序谓词，提供完整允许视频，区分extra frames/info与推理；任意VideoQA集合不能直接变批行为检测。
- [Ano-NAViLa ICCV2025 CVF正式页](https://openaccess.thecvf.com/content/ICCV2025/html/Song_Normal_and_Abnormal_Pathology_Knowledge-Augmented_Vision-Language_Model_for_Anomaly_Detection_ICCV_2025_paper.html)主会通过，但有预训练病理VLM+MLP，说明知识增强专业模型可行，不是同模型LLM查手册提升证据；patch/WSI/patient不可混作独立单位。
- [BLINK-Twice NeurIPS2025 Datasets and Benchmarks Track](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2b76873e897f3de3069b2f360c65e0c2-Abstract-Datasets_and_Benchmarks_Track.html)是正式D&B录用，明确标track，不冒称普通Main Conference Track。若硬门槛只收研究主轨则不充数，保留视觉诊断。
- [TabVer](https://aclanthology.org/2024.tacl-1.89/)是TACL期刊；虽ACL2025有报告，不能据现场报告改称ACL主会录用。Findings/industry/demo/workshop亦不充本轮主会数字。
- AnomalyClaw目前只有本任务核验的预印本，旧SDNET来源是数据期刊；因此不能拿“它用了顶会数据”直接满足新主会证据门槛。LOCO借LogicAD主会方法研究只能标“主会研究使用的已有数据”，不能改写LOCO原始发表venue。

## 5. 本轮研究价值门槛

优先任务输入、gold与固定DAG是稳定的同一use case；正式录用和多模型低分不能替代这个条件。质量因果拆成：完整必要输入直接判断→同模型固定资源/推理→Agent选择策略→单轨迹复用。固定程序达到最优允许成功进入环境，但单轨迹方法需胜同资源无轨迹Coding或降低有成本证明的构造难度。CaRL-EM、ComEM、Magneto、Binder/Chain-of-Table都应成为相关任务的强对照，不能只保留传统LOTUS。

下一步优先轻量源数据与gold审计，不立即训练CaRL或下载病理/视频大包。没有本地新准确率、成本或单轨迹结论。测试0；Python仅核算论文已发表表格，模型调用0。未commit、push、联系作者或外发本地研究材料。
