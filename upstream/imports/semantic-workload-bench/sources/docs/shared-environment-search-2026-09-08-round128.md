# 第128轮：DrugProt原论文、官方语料与规范取得

状态：候选来源核验，尚不合格，累计7/15。CHEMDNER已在54–55轮核验，不重复列入新湖；DrugProt与ChemProt存在源摘要继承关系，未来不能再将ChemProt算独立湖。

## 实际下载

原论文[Overview of DrugProt](https://upcommons.upc.edu/bitstreams/4a4e2dc2-df18-4bcd-893a-ffeadc9bf2b3/download)：24页8183221bytes，SHA25603cb9596d5d243c37423083aa8a6a7441b222fd1a01ebc68a8a93914a352a45b。完整[官方评分仓库](https://github.com/tonifuc3m/drugprot-evaluation-library)commit6b939554de38dbb69c462cc0d45c1cb17c3eaf57，19075bytes16ZIP成员，CRC通过。

完整[官方语料发布5119892](https://zenodo.org/records/5119892)，13418218bytes13ZIP成员，CRC通过，SHA256679ca89698ca471a7fedc9af95acc8722c127c04eba19660fead406b5b9b52c9，全部解包。不是只下载第三方转换数据。发布包含test-background但不含其关系gold，本轮不把该部分计入关系任务N。

官方链接的三份规范全部下载：关系33页9292regexwords/516341bytes，基因22页7343words/274734bytes，化学24页5640words/732478bytes。关系规范为2017-08-01 ChemProt v6，不能因总页数79就宣布DrugProt规则全部冻结。语料/三个规范Zenodo元数据均CCBY4.0，评分库MIT分别记录。原始数据、下载哈希和元数据位于v128目录。

## 原生数据审计

训练3500摘要89529实体17274关系；开发750摘要18858实体3761关系。合计4250摘要108387实体21035关系。以title+单空格+abstract解释offset，所有实体surface和关系引用/参数类型检查通过；训练开发无PMID交集、无完全相同文本。未进行近重复/其他数据集或训练污染审计。

训练201、开发30个实体对带多关系，关系完整四元组无重复；必须用多标签/关系集合评分。训练5388、开发1150条INHIBITOR，合计6538。实际13关系类型详见audit.json。下载页面旧统计17288/3765与本次不符；原论文Table3的17274/3761支持本次文件计数，不能以网页旧计数改源数据。

关系手册包含5大类16子类以及NOT等当前13标签外类型。需结合原论文、FAQ、评分源码冻结可执行映射；本轮尚未完成该核验，也没有排除规范示例泄漏。给定实体的关系任务不需要把两本NER手册都算必要E；端到端NER+RE则要单独定义上游和评分。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 从文献中建立药物—蛋白抑制关系证据清单 | 4250篇真实PubMed标题摘要 | 已给定108387个人工实体作为上游输入 | 33页关系规范及待核对的发布映射 | 21035关系，其中6538INHIBITOR；23017395的EPA→HMG-CoA reductase为INHIBITOR |
| 建立化合物—蛋白代谢产物清单 | 同批摘要与给定实体 | 同一关系规范 | 17380207：Asparagine secretion与ASNS表达关系 | Asparagine[1102:1112]→ASNS[1161:1165]为PRODUCT-OF；这是文本标注不是临床处方结论 |
| 从原文识别化合物及基因实体，再进行关系抽取 | 同批原始标题摘要，上游不提供gold实体 | 化学24页、基因22页、关系33页规范 | 实体跨度与方向是独立中间输出 | 108387实体及21035关系可分别评分；任务尚未构造 |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold |
| --- | --- | --- | --- |
| `abstracts.sem_map(extract_relations,given_entities,E).explode().filter(type=='INHIBITOR')` | 4250摘要→21035 gold关系→6538抑制关系 | 多标签实体对关系集合 | 化合物/蛋白mention四元组清单，不自动归一到全局实体 |
| `abstracts.sem_map(extract_entities,E_ner).sem_map(extract_relations,E_rel)` | 4250→108387实体→21035关系为gold参照 | 预测实体及关系，不能混入gold实体 | 上游跨度质量与下游关系质量分别评估 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；23017395目标含EPA→HMG-CoA reductase的INHIBITOR | 同E与给定实体→固定多标签关系抽取→参数校验→过滤 | 未执行，目标相同无优势证据 | ==查直接/间接调节与抑制规则==→==核对具体证据与类型优先规则==→生成关系集合 | `DrugProteinRelations(text,entities,E_version)`允许一对多标签，不读取private关系 |
| 未执行；17380207目标含Asparagine→ASNS的PRODUCT-OF | 同E类型定义→固定关系提取→产物过滤 | 未执行，目标相同 | ==查PRODUCT-OF与SUBSTRATE方向==→原文定位→校验参数 | 同一关系operator的下游投影；不是另一个独立湖或另一个全新语义任务 |
| 未执行，无准确率预期数值 | NER→RE固定DAG；同资源工具允许固定缓存 | 未执行，不预设更准 | ==区分化学/基因边界规范==→抽取实体→==处理关系规则==→校验 | 分离实体与关系两个算子，分别保留证据和ABSTAIN |

复跑：`python3 artifact/evidence/shared-environment-audit-20260908-v128/audit.py`。无模型调用、公开快照、正式运行器或单元测试、无commit。下一步核验13类规范映射、人工示例泄漏、与既有CHEMDNER的实体来源交集，才能判断是否构造。
