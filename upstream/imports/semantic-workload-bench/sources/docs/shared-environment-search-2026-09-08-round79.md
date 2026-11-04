# Increment79 — UKP 真实网页论证：完整手册已取得，暂不新增合格数

状态：SOURCE_DOWNLOADED_AND_AUDITED，仍为6/15。完整45页手册不是所有任务都必须读取45页的证据；未完成构造、泄漏排查和环境消融。

原始来源：[CL原论文](https://aclanthology.org/J17-1004.pdf)、[EMNLP原论文](https://aclanthology.org/D15-1255.pdf)、[完整作者仓库](https://github.com/UKPLab/emnlp2015-ih-ig)、[大学官方完整发布](https://tudatalib.ulb.tu-darmstadt.de/items/d4a7ac0c-e7a8-466a-855a-917e42a24342)。均已下载，具体字节/hash在 `artifact/evidence/shared-environment-audit-20260908-v79/` 的下载收据；仓库commit662bd4d411147840b1d1ffced58cac15f93c956a，596Git blobs全部校验，ZIP CRC通过。官方ZIP2931320bytes，内层tar5674entries已解包。

手册413701bytes、45页、27287空白分词，SHA256 b14d0f844530fafe4a364ed02130a5aa3a9c2dd9669955736479d11e5119cf3e。§3主要为说服性与争议例子（4–22页），§4结构规则（23–28页），§5评论示例（29–45页）。不能把前一任务章节硬加给后一任务；例子可能来自当前gold，需隔离后再确定有效E。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | private gold |
|---|---|---|---|---|
| 按本协议抽取网页论证组件、区分一般理由与个人经历、连接论证关系 | 340真实文档：216评论、73论坛、46博客、5文章 | 手册§4及实际适用的§5示例 | 原文争议主题/标题；作者及URL仅用于后续分组审计 | 538 Premise、224 Backing、365 Claim、68 Rebuttal、26 Refutation；另98通用ArgumentComponent，869关系 |
| 按协议筛选有说服意图的评论/帖子 | 990真实文档 | §3规则与争议处理示例 | 文档主题及必要语境 | 每文档恰1个isGold=true；524真、466假 |

4334未标注文档不是负例；不能与990/340相加声称独立带gold批量。990与340的重叠尚未审计。98通用组件不是第六种Toulmin角色，具体properties见secondary-audit.json；不能简单混为同一分类。作者仓库的情感、句法、RST与向量特征不是全人工gold。

| 类python的DAG | 具体数值 | 下游结果/边界 |
|---|---|---|
| `docs.sem_map(extract_components, E).explode().groupby(type).count()` | 340文档；1221五类组件，另98通用组件 | Backing原生gold总数224；不是224独立文档 |
| `docs.sem_map(extract_graph, E).explode_edges().project(src,dst)` | 原生869关系，端点存在检查0错 | 关系含义与隐式Claim表示需继续审计，尚非可执行评分器 |
| `comments.sem_filter(is_persuasive, E).project(id).count()` | 990→524 | gold总数可求；E示例暴露排除后数量会变化 |

具体真实例子1021：学校教育讨论中，一般性环境理由[428:505]为Premise；个人学校经历[522:713]为Backing；结尾反对一刀切[787:853]为Claim。§4.3.1将一般理由与个别经历区分，但存在“个别案例是唯一理由”的例外，因此不能把第一人称固定等同Backing。UTF16范围和关系引用检查通过；无独立surface字段，不声称第二来源全文一致。

以下均是待测执行设计，不是模型运行结果。LOTUS指固定语义调用流程，不代表所有当前agentic接口。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标输出1021的Premise、Backing、Claim及位置；实际正确与否待测 | 固定prompt提供完整必要原文、主题和适用E，sem_map输出结构再校验offset；固定检索也可作为同资源对照 | 同一gold目标；不能预言优于LOTUS | ==读取§4.3.1、核对一般理由/个别经历例外==→读取整篇定位Claim→抽取组件→工具检查offset | `load_protocol→identify_stance→classify_reason_function→emit_spans→validate`，规则来源/例外明确；是否能从单条轨迹自动提取待测 |
| 目标524个原始gold ID；实测清单未知 | 对990文档固定sem_filter，保留全部失败行，随后project/count | 相同目标，准确率/成本未知 | ==核对§3中隐含意图、叙事、讽刺的判准==→判断文档→记录可观察条款与输出 | `shared_rule_index→assess_intent→handle_context_exception→boolean_or_abstain`；需与仅E编译器和整批缓存Agent比较 |

许可：手册CC BY-SA3.0；数据附独立协议，限学术研究并限制再分发，不能拿仓库许可替代网页文本权利。当前仅本地忽略目录保存原始材料。待完成：逐任务有效E长度、例子泄漏、两个gold集重叠及版本对等、原文语境充分性、公开allowlist构造和独立验证。无模型调用、无优势结论，不计第7个。
