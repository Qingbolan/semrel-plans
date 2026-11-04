# 增量202：PICKLE植物科学实体/关系批处理，待核验

本轮新增独立来源检索，尚不计入合格数，仍12/15。已下载完整作者代码仓库、完整作者Hugging Face数据仓库、出版社原论文HTML和三个规范PDF附件。原论文PDF入口403；Zenodo原始BRAT两次超时/504，未取得。保留失败收据，不以第三方知识图谱三元组替代原文。

来源：[原论文](https://doi.org/10.1093/insilicoplants/diad021)、[作者代码](https://github.com/serenalotreck/pickle-corpus-code)、[作者数据](https://huggingface.co/datasets/slotreck/pickle)、[原始BRAT发布页](https://zenodo.org/records/10076664)。原件在`data/shared-environment-audit-20260908-v202/`，完整收据及审计在[证据目录](../artifact/evidence/shared-environment-audit-20260908-v202/)。作者代码commit9f8b31607e978a974677084098c679da653e920c，67个tracked文件；未执行其中代码或训练。原论文HTML267500bytes；附件S1实体本体4页、S2关系本体2页、S3规则25页7193词，S3日期2023-08-08，实际文件471913bytes。来自出版社公开带签名的下载链接，不是从搜索摘要重建PDF。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| Q1逐摘要抽取植物科学实体→实体清单 | 作者JSONL250摘要、2258句、原token序列 | 25页完整规则中的语义/跨度/限定词规则 | 实体本体4页；19种类型实际出现，不把21种本体终端类型误当19 | 转换后6164实体；源BRAT发布页报告6245，尚未逐条比对 |
| Q2逐摘要抽取关系→知识图谱边表 | 同250摘要；给定实体版可明确提供gold实体作为输入，端到端版消费Q1预测 | 同版关系规则；要求同句证据、缩写与全称分别标注 | 2页关系本体；is-in/activates/inhibits/interacts/produces | 转换后2094关系：647interacts、489is-in、473activates、354inhibits、131produces；原始BRAT发布页2149 |
| Q3关系表筛选/计数 | Q2预测关系 | 同任务定义 | 确定性关系过滤 | 可从2094人工边派生，非第三套独立gold |

| 类python的DAG | 具体数值 | 语义/边界 |
|---|---|---|
| `abstracts.sem_map(extract_entities,E).explode()` | 250输入→gold6164实体 | span/type对比；输入是已分词文本，未恢复原文字符坐标 |
| `abstracts.join(entities).sem_map(extract_relations,E).explode()` | gold2094边；本次所有端点都对应同句实体 | 给定gold实体和端到端任务必须分开报告 |
| `relations.filter(type=="produces").count()` | 转换后gold131 | 未取得BRAT，不声称此数代表原始完整金标 |

实际JSONL例：PMID24046061_abstract中一句讨论grain filling阶段多个starch biosynthesis genes在SERF1 knockout grains上调。源关系包含`GBSSI → is-in → SERF1 knockout grains`（文档级token闭区间114:114与136:138）。完整原token句和其他对应边见[audit.json](../artifact/evidence/shared-environment-audit-20260908-v202/audit.json)。规范将is-in限定为始终成立的位置关系；该句含时间/实验语境，因此此例需要进一步核验规则适用，而不能直接宣称已确认规范冲突或擅改gold。常驻位置与表达量变化可以是不同事实。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 按源目标输出GBSSI的is-in边；实际未运行，语义一致性待审 | 固定检索关系定义和定位规则→sem_map→端点检查 | 同目标；实际未运行 | ==查永久/临时定位、实验条件及缩写规则==→判断→输出 | `RelationRuleRetriever + RelationMapper + EndpointValidator` |
| 抽取符合规范的实体跨度/类型；实际未运行 | 固定本体检索→sem_map→跨度/type校验 | 同目标；实际未运行 | ==查实体具体性、限定词、重叠与缩写规则==→抽取→校验 | `EntityTypeResolver + SpanBoundaryMapper` |

以上均为预期设计，不是模型结果或已提取operator。固定程序/CodingAgent/E-only编译与Agent使用同资源与缓存；不能预言Agent更准确。

本轮全量静态审计：250唯一摘要，无相同token全文重复；官方split170/30/50，ID无交叉、合并等于all；实体边界及关系端点异常0。Hugging Face克隆提示4文件本应是LFS pointer但实际存正文，全部仍可逐行JSON解析；不将网站dataset viewer的Arrow报错当数据损坏。另下载的cora-hai/PICKLE_data-split是二次知识图谱划分，不能替代原文或视为独立湖。

手册与转换后摘要做Unicode字母小写八词匹配，23篇命中，已登记为例句暴露候选；尚未核PMID/PMCID显式引用并构造排除视图。规范与语料共同迭代形成，不是独立确认。原始BRAT与JSONL数量差异由发布页明确解释为tokenization对齐时丢标注，不能把丢失关系当确证负例；需获取原始版或冻结明确的转换任务及可评估范围。当前没有模型、官方scorer、E必要性消融、公开快照或确认集。

许可：作者HF卡标CC BY4.0，论文为开放获取；代码库未据此自动继承数据许可。原摘要版权另行核验。所有文件仅本地研究，无发布。

下一步：核验规范例句/显式PMID重叠、原始BRAT可达性、例中is-in适用及转换gold范围；长E作用需按实体/关系各自相关章节衡量，不能将25页全部计入仅5类关系判断。
