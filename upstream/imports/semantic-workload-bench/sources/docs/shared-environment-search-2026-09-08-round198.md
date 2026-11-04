# 增量198：FrameNet1.7配套规范、词典和人工全文标注

新来源，仍未计入，先完成原件与原生结构求证。实际下载：

- [项目原论文](https://aclanthology.org/P98-1013.pdf)，459289bytes。
- [1.7版本API论文](https://aclanthology.org/D17-2001.pdf)，134932bytes，作者说明通过NLTK下载完整发布。
- [NLTK分发的完整1.7发布包](https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/framenet_v17.zip)，99207152bytes、14937成员，ZIP CRC全部通过。是完整发布包，不是作者Git源码仓库；本轮没有克隆整个NLTK仓库。
- 另下载[手册教学镜像](https://my.eng.utah.edu/~cs6961/papers/FrameNet_book.pdf)1459282bytes，但以发布包内book.pdf为后续依据，避免外部版本混用。

原件data/shared-environment-audit-20260908-v198；收据、audit.py/json在artifact/evidence/shared-environment-audit-20260908-v198。包内README明确book.pdf是2016-11-01修订129页annotator manual，连同1221框架定义、13572词汇单元及XML schema/框架关系一同发布。配套书实际提取129页70034词；不是说整书每页均必要。发布说明确认网站内容可能比1.7更新；当前资源应冻结包内版本，不访问当前网页来悄悄补规则。

本次直接XML审计107个fulltext文件、10147句；共28208 MANUAL annotationSet，其中28171带frameID，为当前候选gold单位。另10917 UNANN不得作独立人工框架gold。manual+frameID下rank1 FE有58461标签（含隐式/空实例）；遍历Target/FE得到8272无位置标签计数。全部28171框架引用存在；rank1角色名属于其框架；显式Target/FE位置边界异常0。没有全量重跑标注、scorer、来源近重复或词典例子泄漏审计。

必须注意：fulltext目录并非107份均完整标注所有谓词。发布说明称新增7个WikiTexts文件是每分句一个lemma的词汇标注实验。未标注谓词不能自动判negative；若定义给定目标词的框架/角色任务，应公开目标跨度，但隐藏当前frame/FE。各句同一任务、同一冻结词典/规范；不是把每个框架当独立湖。

具体ANC__110CYL067、sentence4106339：句意为“你对Goodwill的捐助意义超出你的想象”。人工target contribution→Giving；Donor为Your，Recipient为to Goodwill（包含介词）。这体现角色跨度规范与框架词义；不能用普通NER只抽组织名代替原gold，也未证明Agent必要。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 给定目标词→识别框架→按框架聚合句子 | 107源文件10147句；给定目标跨度任务待构造 | 1221框架/13572LU的冻结定义 | 129页配套标注手册与关系文件 | 28171 MANUAL带frameID的annotationSet；例contribution→Giving |
| 给定目标词（是否给frame另立契约）→抽取角色→参与者清单 | 同句和明确给定上游目标 | 该框架角色定义及完整共享词典 | FE跨度/空实例规则 | rank1 FE58461，例Donor=Your、Recipient=to Goodwill |
| 同目标→区分隐式论元类型→缺省论元统计 | 同公开句子 | null-instantiation分类规范 | 下游统计程序 | 空实例标签需进一步分类型与缺字段审计，不能视为执行ABSTAIN |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(given_targets).sem_map(frame,E).groupby(frame).count()` | 候选28171人工框架判断 | 给目标不等于给框架答案；未标注目标不作负例 |
| `targets.sem_map(frame,E).sem_map(frame_elements,E).explode().project(role,span)` | 58461 rank1角色标签 | 包含隐式论元；需显式输出契约，不能全当span |
| `role_outputs.groupby(instantiation_type).count()` | 8272无位置标签是本次遍历计数 | 需确认类型/注释层和去重，不等于8272独立句 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| contribution→Giving；实际未知 | 固定LU候选检索→同句框架消歧；可缓存全词典 | 同目标，实际未知 | ==查contribution候选框架、Giving定义及邻近框架区别== → 选择框架 | `FrameDisambiguator(lexicon_version, candidate_index, rules)` |
| Donor=Your、Recipient=to Goodwill；实际未知 | 同资源固定角色抽取→跨度/角色schema检查 | 同目标，实际未知 | ==查Giving角色定义与介词短语跨度规则== → 输出角色 | `RoleExtractor(frame_schema, boundary_rules, null_rules)` |

==是可观察资源查阅，不记录私人思维链。没有模型执行或质量差距结果；固定程序/CodingAgent/E-only编译也可预处理同词典，不预设轨迹提取优于直接编译。角色gold中保留的介词是任务规范，不是人工制造难度。

发布说明要求论文/产品引用FrameNet；原始文本来源与词典权利需分别保留。本轮仅原生初审，未完成public allowlist、规范例句重叠、句子/文档划分及人工状态细节。下一步针对这些实际缺口核验，不能仅凭CRC或引用范围通过就称合格，当前仍11/15开发可构造。
