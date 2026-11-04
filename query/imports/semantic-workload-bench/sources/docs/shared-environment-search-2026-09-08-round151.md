# 第151轮：Softcite v2，993篇完整holdout与软件依赖关系求证

新独立候选，未qualified，仍8/15。上一轮UMR整文件范围/去重有实际进展，本轮先核实历史未登记Softcite，再取得原论文、完整v2仓库及同版本标注指南。

[原论文作者公开稿](https://raw.githubusercontent.com/howisonlab/softcite-dataset/18522db3b8642eef2c0ac57a5ffd043a97824cff/docs/papers/Softcite_Dataset_Description_RC.pdf)1701893bytes，SHA256 `28b24536cc5900741511daef064de9473bc3dde21019db16d4ec8d4ccaa1b027`；对应[Du等2021 JASIST](https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.24454)。该论文描述v1，v2变化以新仓库记录为准。原v1只查完整tree定位论文，并未下载整个历史仓库，不能称v1仓库已下载。

完整[softcite_dataset_v2](https://github.com/softcite/softcite_dataset_v2)commit `4aaf7b281f0aecf6039edb30813dca89cf54b3bd`，ZIP25213793bytes13membersCRC通过，SHA256 `ae522e123b2a3ac082bbc0cb5a1c9403edd080f24f7df6fdc122052e56f77695`。含3TEI XML、3JSON、转换脚本和指南。指南30979bytes3966空白词，SHA256 `ce2e5a88dd4cc3db87075dd6f6ca1b6402d1b85c7537b9daf4a254a2c661e7d0`；本文未将词数换成臆测页数。原件data/shared-environment-audit-20260908-v151，audit.py/audit.json/examples.json和下载收据artifact/evidence/shared-environment-audit-20260908-v151。

## 全量原生TEI核验

三份XML全部解析成功。working3978文档、holdout993，文档ID无重复/无交集，合集恰等full4971。full/working是软件提及相关段落，holdout按作者说明带完整文本；不得将full名字解释为4971篇均有完整输入。原PDF全文字节/所有章节覆盖还未逐篇比对。

实际full5093个software、1469version、1300publisher、229url、71language，不等于README表格的5134/1478/1311/231/71，可能版本或统计口径差异，未默默修复。working含6个corresp目标不在同文rs实体集，另1个software subtype=url；保留来源问题，不以所有4971无错误宣称。

holdout993文档含989software、283version、250publisher、41url、8language；software分775默认standalone、184environment、15component、15implicit。602个corresp指针全部同文解析成功，rs ID无重复。731文档无rs标记；在作者完整标注假设下可作为未提及，但不能把没有标记当临床/生产事实标签。holdout无完全重复段落（逐文比较）；不是近重复/跨论文实体去重证明。

gold来源要精确：holdout元数据120multiple_annotator、859unique_annotator、248with_reconciliation_and_scripts，类别可重叠，也并不覆盖所有相同维度。README称新增v2类型/关系经两人盲标和协调，不能据此宣称每一原始文档都完整双标。`resp`是最后编辑者不是完整逐实体独立专家审查日志。

共享规范确有语义边界：算法本身通常不算软件；编程语言作为环境使用与仅指实现语言不同；宏、工作流、API也有范围规定；名称和缩写同span；component→environment有专门关系规则。但3966词含标记格式/例子，不自动等于需要反复读取的复杂环境。需筛指南例子/同源重叠、核输入独立性及长规范必要性后再决定资格。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 从完整研究文本抽取软件及版本/作者/URL/语言，建立可复现的软件清单 | 993篇holdout完整TEI文本，剥离全部rs标签及答案属性后执行 | 同版本3966词软件边界/类型/关系指南 | 元数据可提供公开文章标识，但不能gold选段落 | 989软件、283版本、250发布者、41URL、8语言；602指针 |
| 提取文中明确表达的组件—环境依赖 | 同湖文章上下文 | dependency章节要求上下文明确的两种角色和指向 | proCIs/R样例的统计段落 | a954843cac中proCIs=component、R=environment，proCIs→R |
| 按软件环境汇总相关论文 | 上游软件类型和依赖结果 | 清单与去重实体口径需冻结，不凭空实体链接到外部产品ID | 可固定按原始提及字面与文档ID聚合 | 15个component提及不等于15独立依赖产品；需要后续逐关系统计 |

| 类python的DAG | 具体数值 | 下游影响与边界 |
| --- | --- | --- |
| `articles.sem_map(extract_mentions,E).explode().attach_attributes()` | holdout989个software，582个其他实体；602关系指针 | 句内名称/版本配错会污染软件清单。731篇无rs仍保留分母，不先按gold有软件筛输入 |
| `mentions.sem_map(classify_context,E).filter(component).join(environment)` | 样例proCIs→R；R在该上下文是环境而不是仅language属性 | 图构造依赖上下文角色，不是查固定软件名词典；所有方法允许同文检索 |
| `dependency_pairs.groupby(environment).collect_unique(article_id)` | 样例对R贡献1篇来源论文 | 未构造全库聚合gold；不可将单样例说明写成完整下游已评分 |

以下未运行LOTUS或Agent，无准确率/成本/优势结果。实际数据例子在examples.json，当前观察属于开发暴露。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 样例两个软件实体R/proCIs和proCIs→R，实际输出未测 | 固定全文分段/语义抽取→同指南类型判别→属性关联→校验引用；可缓存规则与全文 | 相同目标，不能声称更好 | ==读软件范围和dependency规范，区分统计检验名称与软件实现==→==核对R package proCIs结构==→生成两实体和依赖 | `SoftwareMentionExtractor(E_version)->spans,types,attributes,links,status`；链接只引用本条公开计算实体 |
| SPSS/版本13配对；SPSS=environment是已发布样例目标 | 按同规范与上下文抽取；标签争议需记录而非私改gold | 同一目标 | ==核对环境与独立软件边界是否由上下文支持==→证据不足记待复核 | `ContextTypeClassifier`可独立消融；不写死产品名称→固定类型 |

同资源fixed RAG、Coding Agent、E-only规则编译和整批Agent都应比较。不得只让Agent看完整文本而让LOTUS看残缺训练片段。不新增使用/创建/共享三种标签任务：本次v2已检数据没证明这些标签存在，不能把识别服务功能当数据gold。

## 下一步

有一组规模足够且引用闭合的完整holdout来源，这是比仅论文线索更强的候选。仍须检查指南例子泄漏/实体重叠、规范实际必要子集、当前类型与上下文一致性以及公开构造完整性。先做这些，不靠长手册名字或holdout身份直接设VALIDATED。源码没有执行、没有模型/实验预算/训练/确认划分/测试套件/快照/正式评分/commit。仓库声明数据CCBY，原文CCBY覆盖须按所选源继续核实。
