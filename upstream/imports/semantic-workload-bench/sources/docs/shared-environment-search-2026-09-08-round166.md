# 增量166：UCCA Wikipedia复杂图规范与原生数据

**新来源待核验，仍8/15。** 上一165为镜像差异补证。此轮RED受LDC限制、EventDNA需提交姓名/机构/邮箱，未取得其案例，也未联系作者。转向可直接下载的UCCA。这里真实items是百科文本上的语义标注任务，不是医疗/法律真实裁决；不改变成裁决预测。

## 原件与审计

完整[UCCA English-Wiki仓库](https://github.com/UniversalConceptualCognitiveAnnotation/UCCA_English-Wiki)commit `3aa1c50e257409d0cb0f2648b6575ecb0fdc91e9`，完整[规范仓库](https://github.com/UniversalConceptualCognitiveAnnotation/docs)commit `46d81faae821d31fecfcb9ea32450449616af731`均clone完成；[原论文ACL2013](https://aclanthology.org/P13-1023.pdf)182471 bytes，SHA256 `83ddffcbff49dc03f8ef89c4bf31d4fb93f78b1281158dae12162f7a9cc1ccbe`。数据仓库自带guidelines.pdf为**v2、2018-11-24、37页、237863bytes、17771空白分词**。规范仓库新版v2.1不自动替换此版本。README仍称nutshell摘要，而实际PDF是长指南，已读实际首页。

原件data/shared-environment-audit-20260908-v166；脚本、全部tracked文件大小/哈希、审计结果artifact/evidence/shared-environment-audit-20260908-v166。未运行上游模型。

实际367 XML、158668个layer0 token节点、362368节点、372668边，包含10667 remote边、1573 implicit节点。边标签A43814、P17440、S6682，其余完整计数见audit.json。所有edge.toID在本passage节点集中存在，0缺失引用；这不等于通过全部图语义或无环检查。metadata有368项，其中609没有XML；现有367均有来源映射，归为27篇原Wikipedia文章。README158690tokens与当前XML158668不同，尚未解释。不能称367独立文章或按passage随机切分已隔离。

README说明文本与标注CC-BY-SA3.0；论文/规范版权分别核验。规范中示例与语料的重叠未审计，确认集未构造。层级/共享参与者等复杂规则是否优于短定义仍需实验，不能用37页长度直接证明资源必要性。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 每段百科文字抽取UCCA Scene结构及参与者关系，生成可查询事件/状态表 | 367 passages，158668 tokens；固定tokenization可作为显式上游 | 随数据37页v2规范，涵盖静态/动态、修饰、共享/隐含结构 | metadata提供27源文章，用于构造分组隔离，非答案 | 原生XML非终端图/标签/remote等私有，默认不能给模型 |
| 判定跨并列Scene共享的参与者，避免漏掉省略主语 | 同一段完整token序列 | 规范remote/participant定义 | 已预测的Scene结构，或明确给定结构的独立任务 | 10667 remote边；不能将所有remote称参与者，需要按A类型核实 |
| 具体passage20：William Bradley “Brad” Pitt was born … and is the son of … | 第一Scene与第二Scene并列 | Participant包含地点；remote表示共享结构 | 原图1.2与1.11两个Scene，主语节点1.3 | 第二Scene 1.11→1.3是A/remote=True；源标签born为S，此为原标签而非本研究语义裁定 |

| 类python的DAG | 具体数值 / 实例 | 边界 |
| --- | --- | --- |
| `scan(passages).sem_map(parse_ucca,E)` | 367段→预测图 | 27文章是源隔离单位，不把段数当文章数 |
| `graphs.sem_map(resolve_remote_participants,E)` | passage20第二Scene的共享主语1.3 | 原图节点ID只用于说明，不得写死算子；端到端模型须自己产结构 |
| `graphs.project(scenes,participants).groupby(article).collect()` | 图标签P17440/S6682/A43814为原生边计数 | 边数不是独立事件数；下游集合投影尚未与原生scorer核验 |
| `audit(target_exists)` | 372668边→0目标缺失 | 仅工程引用检查，非图语义正确或研究有效 |

下表是未执行的方法预期。固定程序、Coding Agent、E-only编译与Agent都允许同一规范、工具和缓存。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| passage20第二Scene应保留共享Pitt参与者，实际能否命中未知 | 固定Scene识别→共享参与者判定→结构校验 | 相同目标，不预言更准确 | ==查并列结构和remote规范、核对第二Scene省略的参与者==→输出 | `SceneParser→ParticipantResolver→RemoteEdgeBuilder→Validator` |
| 输出规范定义的Process/State及参与者图，实际质量未知 | 固定sem_map使用完整E或同资源检索，允许共享规范缓存 | 相同图目标 | ==核对静态/动态、地点Participant及隐含节点边界==→结构化输出 | `FrozenGuidelineRules→GraphBuilder→SceneTable`；轨迹提取仍需真实执行与E-only消融 |

下一步需要文章分组划分、示例排除、官方图评分/投影契约与版本差异核验，才判断是否可构造候选。暂不加入8个名单。无模型/prompt/训练/种子/token费用预算/推理并发缓存/测试套件/正式快照/score/commit。
