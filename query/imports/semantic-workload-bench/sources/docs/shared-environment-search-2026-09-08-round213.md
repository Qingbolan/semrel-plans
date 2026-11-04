# 增量213：AnnoCTR真实威胁报告与冻结ATT&CK知识库

新独立来源，仍12/15、尚未资格确认。实际下载[原论文](https://aclanthology.org/2024.lrec-main.103.pdf)447088bytes与[完整作者仓库](https://github.com/boschresearch/anno-ctr-lrec-coling-2024)，commit `d510b6949e1938d47c93a43eedd562dc538439dc`、6617 tracked文件。包含报告原文、两份标注指南、链接gold、冻结实体知识库。原件data/shared-environment-audit-20260908-v213；[全量hash/审计](../artifact/evidence/shared-environment-audit-20260908-v213/)。

论文与README范围需区分：论文400篇为通用层，其中120篇有网络安全专门标注。本地text train/dev/test为70/16/34共120篇，另train_ext70；不能用400作为当前网络安全任务批量。下面使用带CON/负例版本中的MITRE链接切片，不将多个导出版本重复计数。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| Q1给定提及与全文→技术链接 | 120篇真实CTR；技术提及3348条 | 冻结ATT&CK技术578项 | 标注指南及报告上下文 | 技术URL：train1920/dev451/test977；18行目标不在发布实体库 |
| Q2给定提及→战术链接 | 同湖战术939条 | 战术14项 | 同报告语境 | train608/dev95/test236 |
| Q3给定软件/攻击组织提及→实体链接 | 软件/组织提及 | 软件545/组织129个官方URL实体 | 同名、别名与定义 | MALWARE881/GROUP413/TOOL44；尚未核别名及源文本定位 |
| Q4从报告生成技术清单 | 同120报告 | 同共享定义库 | 先发现再链接的固定DAG | 仅给定提及链接审计不能证明端到端完整标注/负例覆盖 |

| 类python的DAG | 具体数值 | 语义与状态 |
|---|---|---|
| `mentions.sem_map(link_to_attack,E,report)` | MITRE链接5626行/117篇有正链接报告 | 所有对应报告原文存在；3篇无该切片链接不自动当全负例 |
| `linked.filter(type=="TECHNIQUE").project(url)` | 3348行，18个链接行缺KG目标 | 还未完成可执行公开投影；不能静默删掉未知目标 |
| `links.groupby(report).unique(url)` | 来源split文档ID重叠0 | 来源隔离不等于实体/模板或训练污染审计 |

实际同一报告`zscaler_2021-05-05_catching-rats-over-custom-protocols`中：提及“standard protocols like HTTP/S”链接T1071；另一提及“RATs Over Custom Protocols”链接T1437。两者gold标题都是Application Layer Protocol，但ID不同，后者不在附带KG。不能只匹配标题或把两个ID合并；平台/分类版本是否解释差别尚待核。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| HTTP/S例→T1071为gold目标，未实测 | 同KG固定检索候选→sem_map消歧→URL存在性校验 | 同目标，未实测 | ==查协议技术定义、报告语境与平台范围==→候选消歧→输出 | `DefinitionIndex → ContextualLinker → URLValidator`；未学习 |
| T1437例当前资源缺项，不假报正确结果 | 固定流程检测缺项→ABSTAIN；不得看gold描述补答案 | 同样缺资源 | ==检查KG覆盖与版本==→依冻结契约ABSTAIN | 缺资源状态与语义负例分离 |

附带实体共1545项、113377词，但其中279项为作者命名空间自定义实体。官方ATT&CK URL部分1266项、112331词；不能把全部1545称MITRE标准实体。实体含entity_context程序/实例与缓解措施，尚未做源报告暴露审计，不宜原样作为E。链接文件的label/label_id/label_title/label_link直接含gold实体及描述，只能留私有侧；公开不能直接读取整行。

数据声明CC BY-SA4.0；不能扩展为所有外部知识资产的统一许可。此次全量结构审计无重复KG URL、缺报告0、源split文档重叠0，但18缺KG链接行、规范版本、提及定位、implicit/CON语义、示例泄漏仍待核。没有模型结果、成本、E必要性或独立确认；冻结大KG不是已证明必须进行动态环境探索。
