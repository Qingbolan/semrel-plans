# 增量187：CSTNews多文档湖原件核验

新来源，尚未合格，仍11/15。[官方数据页](https://sites.icmc.usp.br/taspardo/sucinto/cstnews.html)的[完整6.0发布包](https://sites.icmc.usp.br/taspardo/sucinto/files/CSTNews%206.0.zip)已下载，4362成员CRC通过；这是官方完整数据发布，不声称存在已下载的Git仓库。并下载[2011原论文](https://sites.icmc.usp.br/taspardo/RST2011-CardosoEtAl1.pdf)、[2008原始报告](https://sites.icmc.usp.br/taspardo/NILC-TR-08-05.pdf)和[Cardoso2014学位论文](https://sites.icmc.usp.br/taspardo/Thesis2014-Cardoso.pdf)。旧nilc论文地址超时后从同项目Publications链接取得，未用第三方转述替代。原件data/shared-environment-audit-20260908-v187，bytes/SHA256和统计artifact/evidence/shared-environment-audit-20260908-v187。

## 已观察/未确认

原始Textos-fonte有140正文、50事件cluster。剔除精确路径/concordancia/后仍有151 CST文件，解析为多根XML片段包裹后全部可读，共1838 relation元素、13种标签。**这还是文件层统计：151文件可能含名称/大小写不同的一致性标注副本，尚未去重，不当最终gold量。** 无关系的句对是否完整负例也未建立，不能把缺边直接作为FALSE。

学位论文§5.1与附录B明确为此语料描述CST关系方向和适用条件；论文还描述RST与子话题分割。尚未切出实际必要E长度，也未核对版本、手册例子污染。不能把整本学位论文当长规范。官网允许研究用途；没有补造商业许可。

人工单/多文档摘要、人工抽取式摘要与源句对齐另有目录；自动CSTSumm及PALAVRAS句法输出不能当人工gold。部分自动摘要的人类重排版本也不能直接称独立人工内容选择。后续必须逐层区分。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 每事件组识别报道之间的信息包含、冲突、更新 | 50事件组140篇原始葡语新闻，句子分割另给 | CST适配关系定义/方向/约束；必要篇幅待核 | 多新闻源、报道时间和完整上下文 | CST原生关系；1838是未去重文件层计数 |
| 每事件形成去重摘要并检验关系质量 | 同组多篇报道 | 摘要构造规范需进一步取证 | 系统预测CST关系，gold关系仅oracle | 人工摘要/抽取/对齐目录已存在，数量和契约待逐项核验 |
| C1刚果空难：D2句1是否包含D1句1信息？ | D1句1说刚果客机坠毁至少17人死亡；D2句1另给Bukavu、时间、联合国来源 | Subsumption方向与Equivalence边界 | 原始UTF8葡语全文；本表中文为解释 | 原生D2/1→D1/1 Subsumption |

| 类python的DAG | 具体数值/目标 | 边界 |
|---|---|---|
| `scan(clusters).cross_document_sentence_pairs().sem_map(cst,E).project(graph)` | 50组140正文；C1三篇 | 句对采样和未标注负例规则未冻结 |
| `graphs.filter(Subsumption).project(source,target)` | C1 D2/1→D1/1；文件层Subsumption227 | 不能把含更多信息的一句机械删除；方向需规范固定 |
| `clusters.join(predicted_graph).sem_map(select_content).render_summary()` | 以人工摘要作为独立下游目标 | 未读取gold来生成上下文；同资源直接摘要仍须比较 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| C1例正确目标Subsumption及方向；实际未知 | 固定sem_map读取同样句对、全文/时间和规范；可用固定检索 | 相同目标，无预设优势 | ==核对关系方向、报道时间和语料适配定义== → 对照信息覆盖 → 输出关系 | `CSTRelationClassifier(version, pair_context, directional_rules, multilabel_policy, abstain)` |
| 摘要内容需与人工参考比较；实际未知 | 预测关系→固定选择/摘要，另做无关系强基线 | 同一参考目标 | ==核对摘要长度及冗余处理规范== → 内容选择 → 输出 | `ClusterSummarizer(predicted_relations, content_selector, budget)` |

所有方法过程为待测设计，==表示可观察查阅==。不默认Agent逐对重读E，固定程序、E-only编译和Coding Agent均可共享缓存。未完成关系文件去重/引用闭合、E绑定与示例隔离、许可细查、模型与成本实验。下一轮先处理151文件与事件文档对数关系。
