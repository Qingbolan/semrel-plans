# 增量179：Persian RST原件、结构与任务边界

新来源待进一步核验，仍9/15。150篇新闻、共享87页规范及人工结构均已取得，但完整目标规范并不只是复制英文指南：原论文还说明波斯语分句、核选择和关系优先级的适配，必须一并审核。

## 实际取得

- [原论文](https://arxiv.org/pdf/2106.13833)：Persian Rhetorical Structure Theory；PDF已下载并读取§3的构造/标注说明。
- [完整作者仓库](https://github.com/hadiveisi/PersianRST)：commit `28494a2e46baf9770ae67257019e58709b87c8f6`，152 tracked文件：150份RS3、CorpusMetadata.pdf、README。README明确CC-BY-NC及新闻来源，metadata提供来源/日期/作者/链接，尚未逐条提取比对。
- [所引Discourse Tagging Reference Manual](https://faculty.washington.edu/fxia/lsa2011/readings/RST-tagging-ref-manual.pdf)：87页、26235空白分词，来自大学教学镜像；需与论文适配一起解释。
- 原件`data/shared-environment-audit-20260908-v179/`；逐文件bytes/SHA256、source commit及原生统计`artifact/evidence/shared-environment-audit-20260908-v179/{downloads.json,audit.json}`。

本次150份XML全部可解析，5789个EDU、5747个group、11385条带parent边；0重复ID、0悬空parent、0父链循环。总151个根，唯一双根文件是shargh031（节点94/multinuc和99/span）；未修复也未排除。二叉化、覆盖/交叉跨度和无损文本恢复未检查，不能说150份完整结构均有效。

原生标签存在`same`、`topichange`、`topicomment`、`topidrift`、`Background`及`jointmult`等表示；例如jointmult在shargh035和meidan002的header明确type=multinuc。不能只去掉后缀就假设所有结构核性不变；要与18个粗类别及header对应后冻结映射。原生`span`3736边是结构属性，不能当作独立语义类别准确率来稀释误差。

论文§3.2.1说明分句使用波斯语动词配价资料，并在资料缺项时依靠标注者判断；原始分句任务所需这些外部资源尚未取得。可以另立**给定人工EDU的结构/关系任务**，但必须显式说明输入条件。§3.2.3以摘要重要性辅助核选择，§3.2.4优先较具体/更符合篇章目的的关系，并承认某些偏好仍需更具体记录。因此完整E对gold的可决定性和标注分歧不能由87页长度代替。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 对每篇新闻建立RST层级与关系 | 150篇原生新闻EDU文本，显式给定边界 | 87页英文参考指南+论文§3的波斯语适配 | 新闻metadata及原顺序；不得公开gold父指针/类型 | 5789EDUs、5747groups、11385边；核性/类别映射待验证 |
| etemad001的第二EDU解释何者？ | EDU1：分析住房市场及未来须考察伊朗经济诸因素；EDU2：住房同其他领域一样受宏观经济影响（辅助释义，原波斯语保留） | Explanation与Cause/Elaboration类别边界，论文关系优先级 | 原文首两EDUs及完整新闻上下文 | EDU2→EDU1，relname=explanation；EDU1→group54/span |
| 汇总每篇的解释/因果论述 | 预测结构化关系表 | 冻结的粗类别与核/卫星方向规则 | 文档ID、原文片段 | 原始explanation398边、cause526边；只是标签边计数，尚未转成下游清单 |

| 类python的DAG | 具体数值 / 输出 | 边界 |
| --- | --- | --- |
| `scan(given_edus).groupby(document).sem_map(rst_structure,E)` | 150篇/5789EDU；例2→1/explanation | given-EDU，不能称端到端分句 |
| `graph.project(attachment,nuclearity,coarse_relation)` | 11385原生边中3736结构span | 结构和语义指标分开，双根及映射待审核 |
| `relation_rows.filter(target_family).groupby(doc).collect(evidence)` | 例中解释清单应保留EDU2与EDU1关系 | 未执行模型或全量派生gold评分 |

下表为未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标是示例explanation关系及依附；实际未知 | 固定sem_map读取EDU、完整文章、同一规范；允许固定章节检索 | 同样目标，无优势预设 | ==查Explanation/Cause边界、篇章目的和核/卫星约定==→结构输出 | `EDUContext → RelationClassifier → AttachmentResolver → Graph` |
| 下游保留解释关系，不把结构span混为语义正例 | 确定性投影与聚合 | 同一固定流程 | ==开发时确认源schema与粗类别==→冻结后执行 | 原始文件解析不算学得语义算子 |
| E-only编译可能足够，须纳入比较 | 从E生成分类约束/检索计划，含构造成本 | 单条真实轨迹的额外价值待测 | ==保留实际章节检索、证据和公开结构输出==→提取冻结 | 本表只是结构设计，未自动提取或运行 |

下一步应提取metadata、核对规范表与源header、检查双根及树投影，再决定可构造的开发范围。无安装、LLM/模型prompt实验/训练/种子/token预算/推理并发缓存、正式快照/commit；0测试套件测试。下载均exit0，原件未改。上一轮和本轮都提供新证据，目标保持活动。
