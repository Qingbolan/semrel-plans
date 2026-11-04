# 第67增量：MAVEN-ERE公开／私有构造包完成，科学有效性仍未通过

合格保持3/10。本轮将候选推进到实际INSPECTION_DEVELOPMENT构造：不再只有来源介绍，已有可独立核对的公开文档、显式给定上游节点、私有关系gold和manifest。**不是模型运行或VALIDATED，不因文件构造成功自动计入合格。**

原论文和完整作者仓库/语料下载见[round65](shared-environment-search-2026-09-08-round65.md)；完整RED仓库commit e9093ae763894c6f21b9afc4e3bda3a159ce250c见[round66](shared-environment-search-2026-09-08-round66.md)。本轮使用原字节，不重复下载、不运行作者程序。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 对每篇文档的**给定事件簇与TIMEX节点**，输出时间、因果和parent→child组成边，构成可查询事件图 | RED两个原文片段：文字证据/时间因果定义（不含TLINK features）及关系边界例，共5820词38758字符 | `maven-adaptations.json`：研究者转录论文§2.2–2.4和README适用约定，明确不是新专家SOP，列出尚未解决项 | public/documents中3497篇，80258事件簇/87465事件mention、19869TIMEX；文本及tokens保留源值 | temporal920597、causal44093、subevent11574，共976264边；源关系映射后逐条相等 |
| `doc-0919f27d91f7b51bcd17`，Expedition of the Thousand | 整体事件的组成与时空包含不能只按共现判定；数组是parent→child | 整篇来源文本与给定节点 | Expedition与sailed/landed的节点及mention | Expedition分别指向sailed/landed的subevent及CONTAINS；此例已查看，只作开发解释 |

| 类python的DAG | 具体数值/本次产物 |
|---|---|
| `docs=exclude_public_issues(train+valid)` | 原3623，排除126：125有UNK，2与规范/三篇原论文12gram重合，两个条件有1篇重叠；未发现本轮选序下额外完整文本重复 |
| `public=project(text,tokens,given_event_clusters,given_timex)` | 保留3497：原train2811/valid686；不提供目标关系、源split、原节点ID或gold统计 |
| `graph=sem_map(public,red_excerpt,maven_adaptations)` | 预期输出关系图；未调用LOTUS或Agent |
| `timeline=project(graph.temporal); components=project(graph.subevent)` | 920597时间边和11574组成边为私有目标，不是在执行前给模型的提示 |
| `evaluate(graph,private_graph)` | 976264边源值映射相等；尚无预测、F1、下游质量/成本或独立确认 |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| Expedition例目标为parent→child及CONTAINS，其他边准确性未知 | 固定全文/给定节点关系映射→同资源证据检索→图一致性检查→输出；允许规范预编译与批缓存 | 同一目标，不预设更高质量 | ==查组成与纯时间包含的差别；读节点上下文；确认数组方向；区分初始候选与最终补边==→图 | 适用规范加载→上下文配对→语义关系→显式方向/闭包→文档图；并非已提取产物 |

公开结构严格allowlist：document_id、sentences、tokens、given_nodes；每节点只有node_id、kind、mentions。给定事件簇本身是**上游人工共指标注**，已明确annotation-given；不能把本任务称为从裸全文端到端抽取或共指推理。不同关系层的人工标注/推导才是本轮目标gold。节点重新编号、文档ID散列，source-map在private。

构造目录`data/shared-environment-audit-20260908-v67/inspection-v1/`包含3503个manifest资产，独立verify_inspection.py重新读源数据并验证：精确文件集合、所有大小与SHA256、公开字段allowlist、3497文档ID双射、107334节点mention跨度、所有目标边端点、公开文本/节点与源一致、私有976264边与源映射一致。全部通过。不是OS隔离，也不等于模型已无法读取private；执行Agent前仍须实际public-only挂载。

本轮范围仍有限：

- RED实际摘录5820词，不能继续用全指南29541词宣传必要环境长度。边界例含原作者待定表述，研究者适用转录明确不将这些当MAVEN已解决的规范。
- 论文规定的补边规则没有完全明确所有组合标签的实现，当前完整来源库未发现原始稀疏图/闭包代码；构造保存发布结果，没有猜测补齐。
- 规范历史适用、图层一致性和专家复核仍缺，未证明长规则对固定任务的资源增益，更未证明单轨迹提取比直接环境编译更好。
- 12gram检查只排除已知文字重合，不能证明Wikipedia实体/主题近重复、训练污染或独立确认隔离。所有既有查看样本属于开发暴露；未用模型分数选样或修gold。

新增build_inspection.py与verify_inspection.py及构造/验证收据在artifact/evidence/shared-environment-audit-20260908-v67。新工程测试0；两个审计脚本实际执行并通过。无模型/作者代码运行，模型prompt/种子/预算/缓存不适用；没有commit。下一步转核其他独立的长规范公开标注来源，MAVEN保留此可检查构造包与剩余缺口，避免把进一步工程包装误称合格研究证据。
