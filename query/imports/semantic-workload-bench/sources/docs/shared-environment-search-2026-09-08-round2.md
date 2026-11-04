# 增量核验2：下载原论文/仓库，并落到具体 Query 与方法表

日期：2026-09-08，Asia/Singapore。承接[上一轮](shared-environment-search-2026-09-08.md)。结论仍为：**没有新候选通过全部门槛**。本轮新增 PrivaCI-Bench 原始发布审计，并补齐 CSMeD 论文与完整仓库下载。下面的 CSMeD 表是用户要求的具体机制说明，不是将被筛除的数据集重新推荐为最终 benchmark。

## 1. 实际下载与阅读

全部保存于 `data/shared-environment-audit-20260908-v2`，没有运行作者仓库脚本；仓库以固定 commit 的完整 ZIP 快照下载并解压，无 git 历史，非只读 README。逐 blob 对照 GitHub tree 的大小和 Git SHA1 验证，另记录下载文件 SHA256。

| 原论文/仓库 | 本次落地文件 | 精确来源/版本 | 下载字节 |
|---|---|---|---:|
| PrivaCI-Bench ACL 2025 原论文 | `privaci-paper.pdf` | [ACL原文](https://aclanthology.org/2025.acl-long.518.pdf) | 416,085 |
| PrivaCI-Bench 完整仓库快照 | `privaci-repository.zip`、`repos/PrivaCI-Bench-…/` | [作者仓库](https://github.com/HKUST-KnowComp/PrivaCI-Bench)，`cb49d187095062bfff554121d4fa31440a32578e` | 78,200,964 |
| CSMeD NeurIPS 2023 原论文 | `csmed-paper.pdf` | [NeurIPS原文](https://proceedings.neurips.cc/paper_files/paper/2023/file/4962a23916103301b27bde29a27642e8-Paper-Datasets_and_Benchmarks.pdf) | 339,308 |
| CSMeD 完整仓库快照（含全文数据包） | `csmed-repository.zip`、`repos/systematic-review-datasets-…/` | [作者仓库](https://github.com/WojciechKusa/systematic-review-datasets)，`b30e9739939f52b1e799295138791f1fd5b002a5` | 33,644,877 |

读取 PDF §3–5及相关附表、README、Arrow 数据、法规 KB、CSMeD CSV/metadata 和两篇实例的已发布全文。渲染查看 PrivaCI 第5页和 CSMeD 第8页，核对原文统计；不是全篇视觉审查。CSMeD机构镜像返回403后改用会议官方原文，未绕过访问控制。原论文指 benchmark 论文；实例全文来自作者发布的 `main_text`，未把解析文本宣称为逐篇重新下载的 PDF。

[下载哈希收据](../artifact/evidence/shared-environment-audit-20260908-v2/downloads.json)；[逐文件/数据统计](../artifact/evidence/shared-environment-audit-20260908-v2/statistics.json)；[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v2/inspect.py)。下载原文仅本地研究，未完成全部数据再发布许可审核。

## 2. 新增量：PrivaCI-Bench 为什么仍未通过

| 分区 | 实测行数 | 发布标签数 | 环境 | 门槛判断 |
|---|---:|---|---|---|
| GDPR | 3,137 | prohibit 2,462 / permit 675 | 679条法规KB记录 | 论文说明真实执法案件贡献禁止类，允许类来自政策及合成场景；不是同来源真实案件的双向判定集 |
| HIPAA | 214 | prohibit 20 / permit 87 / not applicable 107 | 591条法规KB记录 | 有真实案件来源，但规模214；逐案链接/输入充分性/版本绑定仍未核验 |
| AI Act | 3,000 | prohibit 971 / permit 1,029 / not applicable 1,000 | 842条法规KB记录 | 论文明确合成，不符合真实cases |
| ACLU | 69 | prohibit 58 / permit 11 | 未配统一法规库 | E未满足 |

上述是发布行数，不是独立案件数。GDPR仅3,105种不同 `case_content`，AI Act仅2,675种；精确文本去重也不等于实体或案件去重。原论文第5页HIPAA分项86/19/106加和211而正文写214，仓库实际87/20/107；ACLU论文70，发布69。保留差异，不用论文总数覆盖当前文件。

**最关键的来源混淆：** 只取2,462个真实GDPR禁止案例，常量 `prohibit` 就能复现该子集全部发布标签，不需要E；混入不同来源的允许样本又引入来源捷径。因此数据“有法规+千级真实案件”仍不足以证明判断依赖E。没有实测任何LLM。

原文允许传入已标注CI参数和适用法规的消融属于额外标注条件；不能将 `violated_articles`、`followed_articles` 或 gold CI 参数当作我们的公共检索工具输出。作者RAG代码另有固定BM25路径，说明固定程序本身也能访问法规。法规KB行数包含层级内容，不能换算为干净的30–100页法规净长度。

该路线下一步必须回到同来源、同版本的真实裁决事实与结果，建立适用/不适用及许可/禁止的统一语义。此次不把3,137行直接制成 benchmark。

## 3. 具体例子：患者决策辅助工具 review CD001431

这是一项真实综述的已发布全文筛选子集，源 review DOI为 `10.1002/14651858.CD001431.pub5`。用户要研究的固定任务可表述为：按照该版本筛选规则，返回这171条文献中应纳入的文献ID和数量。ID粒度为出版物，不能把一个试验的多篇论文算成独立试验。

关键环境限制：成人作真实健康选择、随机对照设计、符合定义的患者决策辅助工具、合格比较组；两种决策辅助工具彼此比较被排除。实际开发输入还需审查日期/辅助材料/重复出版等约束，不能只凭这四项实现完整规则。

**下表为数据实测与目标契约，不是已构造/运行快照。**

| Query | 数据湖数据1：共享环境E | 数据湖数据2：批量关系R | 数据湖数据3：公开证据 | 评测侧G（不得挂进模型数据湖） |
|---|---|---|---|---|
| 依据CD001431.pub5，筛选应纳入的患者决策辅助工具试验文献，返回完整ID清单及数量 | `train_reviews_metadata.json`的该review；`criteria_text`实测1,039个空白分词，含重复/非判定内容，仍须做事前规则净化；不是长protocol PDF | 171条CSV记录，171个不同document_id，全部有非空`main_text`；全文共766,375空白分词 | 文献title、abstract、main_text；原已发布内容，不附gold挑选的段落。没有人为再加知识库充数 | `decision`：68 included、103 excluded；`reason_for_exclusion`私有 |
| 单条例A：`CD001431-bib-0433`应纳入吗？ | 同一E，尤其比较组限制 | 1篇前列腺筛查决策工具试验；发布全文计数字段4,861词 | 研究比较娱乐式多媒体工具与含相同知识内容的有声手册；全文把两者作为intervention/control aids描述 | 源标签excluded；排除原因为简单/详细两种决策辅助工具比较，并注明综述更新后的排除 |
| 单条例B：`CD001431-bib-0096`应纳入吗？ | 同一E | 1篇前列腺增生决策工具试验；发布全文计数字段4,680词 | 原文112名男性、33个基层诊所，比较决策辅助干预与常规管理路径；这里112是参与人数，不是批量论文数 | 源标签included；无排除原因 |

两个实例 DOI分别为 [例A原文](https://doi.org/10.1016/j.pec.2008.07.033)、[例B原文](https://doi.org/10.1136/bmj.323.7311.493)。本次完整阅读范围为作者发布的两条 `main_text`；不声称独立医学复核或重新标注。

| 类python的DAG | 输入/中间量 | 具体数值/契约 | 当前证据状态 |
|---|---|---|---|
| `R = scan(public_papers)` | 出版物关系 | 171行；每行唯一ID；公开列须用allowlist | 源数据已核；新public快照未构造 |
| `P = sem_filter(R, eligible_under(E))` | 共享谓词，不同论文 | 例A目标False，例B目标True；正确全集应68行 | 来自源gold，不是LOTUS/Agent预测 |
| `ids = project(P, document_id)` | 纳入清单 | gold清单68个ID；必须逐ID比较 | 尚未运行 |
| `answer = {ids, count=len(ids)}` | 固定下游 | gold count=68；不能仅计数对就称清单正确 | 尚未运行 |
| `score(G, predictions)`（评测侧） | 全171行状态及清单 | coverage、逐行正确率、清单P/R/F1、count误差；失败保留 | 设计契约，未新增scorer |

## 4. 按要求展开：LOTUS、Data Agent、学习算子

**所有“预期”都是拟测试的过程/目标，不是观察结果。** 不能诚实预言LOTUS输出True、Agent输出False；两者都可能达到源标签，也可能都失败。准确率、调用次数、耗时和tokens均未知。`==...==`标记可观察环境探索/证据处理步骤，不索取或保存私人思维链。

为避免混淆，本表传统LOTUS限定为本仓库已下载的作者1.1.3源码，关闭cascade，未使用agentic operators；本次检查了`sem_filter.py`逐记录构造prompt并将列表传给模型的实现及解析默认值。不是声称所有LOTUS版本都只能这样执行。正式实验应固定模型、完整源码hash、prompt、输出预算、工具和cache；目前仅写设计。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 例A目标False/excluded；实际未知。可能辨认比较组限制，也可能因RCT+decision aid表面吻合而误纳入 | 把同一完整批准E与例A全文放进静态`sem_filter`；一次语义判定。无需预先禁止模型阅读比较组细节 | 同样目标False；实际未知，不预设优势 | ==读取固定版本E，定位比较组定义== → ==在例A方法节找到两组材料描述，区分“普通信息”与“另一种决策辅助工具”== → 输出False和证据引用；若证据不足则ABSTAIN | `extract_trial_facts(paper)` → `classify_comparator(facts,E)` → `apply_eligibility(facts,rules)`；保留证据位置和适用性检查，不记例A ID |
| 例B目标True/included；实际未知 | 同一E＋例B全文→静态判定；模型应核验所有必要条件而非只看关键词 | 同样目标True；实际未知 | ==复用本批已解析的E== → ==定位随机化、参与者、干预和比较组证据== → 核验必要条件→True；缺证据不能硬判True | 同一个事实schema和规则图；更换paper输入；不能单独给例B建特例 |
| 整批目标68个正确ID；实际数量未知 | 对171行使用同一predicate；保留原始响应，验证Boolean解析；对格式错误单列失败，不能把默认True当可靠语义结果 | 同样目标68个正确ID；实际未知 | ==一次读取E，建立批共享规则/检索索引== → 按论文调用相同公开检索工具，必要时补读全文→返回171条状态→固定project/count | E解析可共享；论文证据提取仍逐条做；只有单次示范轨迹可供B5提取，本表描述批处理不意味着可以合并171条轨迹 |
| 强固定对照亦可能全部做对：实际未知 | E-only Coding Agent预先产出规则图＋固定检索/提取流程，再用LOTUS `sem_map`/判定；相同全文、工具和预算，允许分支/缓存 | Agent仍按同资源执行；不强迫每行从零规划 | ==在预先声明的预算内定位例外或不足证据==；是否比固定流程有用必须用新文献比较 | 若E-only直接编译得到同一结构，单轨迹学习没有额外收益；保留阴性结果 |

拟议结构（伪代码，不是现有执行产物）：

```python
class ReviewEligibilityOperator:
    environment_digest: str
    rule_graph: RuleGraph       # 源条款引用、依赖、排除项、适用范围
    evidence_schema: TrialFacts # design, participants, choice, intervention, comparator
    evidence_policy: SearchPlan # 固定检索；覆盖不足时补读全文；预算与终止语义

    def evaluate(self, paper):
        check_environment_version(self.environment_digest)
        facts = extract_with_citations(paper, self.evidence_schema,
                                       self.evidence_policy)
        decision = self.rule_graph.evaluate(facts)
        if decision.has_decisive_exclusion:
            return OK(False, decision.evidence)
        if decision.all_required_conditions_verified:
            return OK(True, decision.evidence)
        return ABSTAIN(decision.missing_evidence)
```

“两个decision aids比较”是语义事实，不能用`comparator != usual_care`的字符串判断替代；E也允许其他比较类型。缺少事实是执行不充分，不能自动等同exclude。解析失败同样不能沿用LOTUS默认True而不披露。

## 5. 这个例子能说明什么，不能说明什么

能说明：同一篇RCT是否纳入取决于特定review的比较组约束；并非所有RCT或decision aid研究都被纳入。例A原排除原因提到更新，凸显E版本必须冻结。不能从该描述直接推出环境因果增益、Agent优势或必须经历执行才能学习规则。

特别是该E仅1,039词的原始字段，相比171篇全文总766,375词，主要成本可能在逐篇阅读；机械重复E产生171×1,039=177,669次词暴露，仅为无共享文本构造的算术量，**不是token成本或实测账单**。E-only直接编译完全可能已经足够。这是本例不宜直接成为论文主benchmark的原因。

该review还允许因原决策辅助材料不可获得且论文描述不足而排除。批量复现时，原审查者见过的附件和当前公开全文不一定一致；必须逐案核验输入充分性，不能将该缺口归咎于模型能力。

严格通过条件仍需：真实长事前E、同版本大量同来源案例、独立可信G、完整公开输入，以及不靠来源/措辞/标签泄漏就能证明依赖E的证据。下一增量应追同来源真实裁决档案中的许可与禁止两类，或单review注册protocol及完整原始筛选日志。当前没有构造确认集，也没有实际单轨迹合成或模型比较。
