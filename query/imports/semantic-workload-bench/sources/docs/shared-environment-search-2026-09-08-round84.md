# Increment84 — MLEE：完整数据已核验，长指南未取得

状态待定，仍7/15。已取得[作者官方完整发布](https://www.nactem.ac.uk/MLEE/)MLEE-1.0.2-rev1.tar.gz，2415179bytes、2553成员；完整读取并解包，SHA256469474fbb556a453af80bbf80da910c7ef743961a15eee79aa0bef38dd768575。原论文[Event extraction across multiple levels of biological organization](https://doi.org/10.1093/bioinformatics/bts407)已下载EuropePMC原始XML及PDF镜像350692bytes，PDF SHA256e8b81bf92a169030b135676dd11b0d9aa76b7a633ba5923f6732f6873115b6ed。

本轮纠正进度说明：完整作者包是数据发布，README/许可证/standoff/CoNLL；未发现打包的评估工具或指南。项目页链接外部NERsuite/EventMine，不能说这些工具已随包下载。没有用下游第三方整理库代替原始发布。

原论文确实引用Pyysalo et al.2012a详细指南，但本次官方网页链接、完整发布成员和精确检索未取得该文档；这不证明世界上不存在公开副本。不能将29类型表或通用GENIA规则补成MLEE长E。暂不构造、不增加资格。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 跨生物层级抽取事件，建立血管生成与调控索引 | 262真实论文摘要 | MLEE特定事件/实体规则，完整长文档待取 | 原文；如使用给定实体须显式annotation-given | 6678事件、29实际事件类型；13845文本span混含实体与触发词 |
| 解析调控事件的Theme/Cause及嵌套结构 | 同262摘要 | 角色与嵌套规则尚缺完整指南 | 源实体/事件库存的信息条件需冻结 | 原生事件参数可取；389属性、108关系、368星号行另有标签，语义尚未全审计 |

全262文本span与原文切片精确一致，事件触发词/参数引用存在，0错误；未验证全部属性、等价集合和关系语义。只统计standoff/full，development与test内的train存在重复嵌套划分，不能跨目录累加。262不是6678独立文档。论文说明标注由生物学专家执行，原有专家兴趣span为参考，经扩展为事件；不能解释为临床病例或治疗决策。

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `abstracts.sem_map(event_graph,E).explode().filter(type=='Blood_vessel_development').count()` | 262→6678事件 | Blood_vessel_development855；类型筛选变体不增加独立语义任务 |
| `abstracts.sem_map(event_graph,E).explode().filter(type=='Negative_regulation').project(theme,cause)` | Negative_regulation920 | 参数有gold，但完整角色规则和嵌套评分未冻结 |

具体原生PMID-10417401：E5由upregulated[313:324]触发，Positive_regulation的Theme为vascular endothelial growth factor[200:234]；E11为administering[433:446]，Planned_process，Instrument=alinidine[468:477]，Theme=rats[425:429]。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标恢复E5的Positive_regulation/VEGF Theme；实际结果未知 | 同输入固定sem_map抽事件及角色，结构检查后投影；完整E缺失前不能宣称比较公平 | 同一目标，没有实测优势 | ==定位类型定义与Theme/Cause规则，检查事件嵌套==→读全文→输出事件图 | `entity_index→event_detection→role_resolution→nested_graph_validation`；尚未从轨迹产生 |
| 目标E11 Instrument=alinidine、Theme=rats | 固定角色映射，允许与Agent相同参考和检索 | 同目标 | ==核对Planned_process特定角色与生物层级==→绑定论元→输出 | `schema_roles→argument_binding→reference_check`；详细协议未取得，不能凭常识造规则 |

许可：官方声明CC BY-NC-SA3.0，文本和注释细节见包内LICENSE；工具/词典独立许可。无模型调用、无人工修订gold、无提取或性能结果。证据在artifact/evidence/shared-environment-audit-20260908-v84，数据同后缀。PDF文字提取完成但Poppler报告注释颜色不支持，未声称视觉复刻。后续可核查有公开具体指南的独立IPF机制语料；不以同源MLEE扩展增加独立湖数。
