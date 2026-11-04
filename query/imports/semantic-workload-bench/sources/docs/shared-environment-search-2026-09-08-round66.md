# 第66增量：MAVEN-ERE规则适用、编码方向与缺边语义

合格保持3/10；这一轮推进规则求证，尚未把MAVEN列为完成候选。原MAVEN三论文/仓库及两数据包已在[round65](shared-environment-search-2026-09-08-round65.md)下载。本轮进一步下载完整[RED作者仓库](https://github.com/timjogorman/RicherEventDescription)，commit e9093ae763894c6f21b9afc4e3bda3a159ce250c；ZIP113923bytes/7条目CRC通过、非截断tree全部5blob校验通过，SHA256 0326763a67b257cf07c9ace86ee9735aee4b58231b6de1a2620a5de63ddc409d。其中guidelines.md与v65下载字节相同。它是链接所指现存版本，尚未证明精确对应MAVEN标注时版本。

**已查清三点，不应误编译成过滤器：**

- MAVEN论文§2.2：文本不能确定的时间关系可分到不同子时间线；不同线之间不标时间关系。发布缺边不等于现实中没有时间先后。
- 论文§2.3：人工因果标注先限制在BEFORE/OVERLAP事件对，再依据因果、前置条件和subevent传递规则补边。发布边不必仍满足最初候选约束；不能机械删掉范围外的最终gold。
- README Data Format明确`subevent_relations=[parent,child]`，第二项是第一项的子事件。不能把论文文字“A SUBEVENT B”直接按同样数组顺序写入。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 给每篇文档的给定事件节点构造时间/因果/事件组成图，供后续时间线与前置条件查询 | RED原规范29541词；其中从TLINK到Event Coreference之前5533词，只有部分内容适用于本任务，不能全字数充当必要E长度 | MAVEN论文§2及README：时间子线、候选约束、补边规则、数组方向 | 3623篇作者发布文本、给定事件与TIMEX；若预测共指，不能同时提供gold簇 | 公开46014因果边、12019subevent边；时间边981373；原始人工与规则推导边未逐条分开 |
| Expedition of the Thousand（train首文） | Subevent须是事件组成且有时空包含；数组按parent→child | 全文叙述expedition中的航行和登陆 | Expedition、sailed、landed事件节点 | `[Expedition,sailed]`和`[Expedition,landed]`为subevent；两个同方向也标CONTAINS |
| Myyrmanni bombing（valid已查看开发例） | 人工候选约束与最终补边须分开 | 第2句exploded，第3句In total seven died | 对应两个事件 | 原gold同时有`exploded CAUSE died`及同方向CONTAINS；不是BEFORE/OVERLAP。此处是否由补边产生未获逐边来源证明，不能直接称标错或已解释 |

| 类python的DAG | 具体数值/实测结构检查 |
|---|---|
| `docs=scan(train+valid)` | 2913+710=3623文档；101+24=125文档含独立UNK token；未据此自动排除 |
| `nodes=given_event_timex_nodes(doc)` | 全91719事件mention的token起止和trigger字符串检查0错误；这只验证输入编码 |
| `graph=sem_map(doc,nodes,applicable_rules)` | 没有模型执行；必要规则片段和MAVEN覆盖条款仍待冻结 |
| `causal_candidates=before_or_overlap(graph)` | 仅能描述人工初始候选步骤，不可当最终gold筛选器 |
| `graph=apply_documented_closure(graph)` | 发布因果边中5355train+1462valid=6817不在同方向BEFORE/OVERLAP；未重建作者原始稀疏标注，不能证明这些全由closure解释 |
| `hierarchy=project(parent_child_edges)` | train7999/9193、valid2382/2826与同方向CONTAINS一致；反向CONTAINS均0。其余1638未满足这个简单检查，不自动判错 |
| `index=build_timeline_and_event_components(graph)` | 下游有明确语义；评分须冻结方向、同义关系、无标注边及推导规则 |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 首文例应输出Expedition→sailed/landed的parent-child边及时间包含 | 完整同资源固定节点对映射→约束/闭包；允许固定查规则与图程序 | 同一目标，不预设更高准确率 | ==确认整体远征与具体航行/登陆的组成关系；核时空包含；查数组方向==→图 | 适用规范加载→节点语境→时间/组成判断→方向规范化→图汇总；尚未执行/提取 |
| 爆炸例不应仅因CONTAINS就硬排因果边；是否预测gold CAUSE未知 | 固定程序保留最终推导空间，按照同一冻结输出契约评分 | 同样不能靠查当前gold补边 | ==区分初始候选限制与最终推导；核爆炸与死亡文字；保留证据及规则来源==→候选/最终边 | 人工协议对应的候选生成→语义判断→显式closure→结果；缺失作者稀疏图时不冒称精确重建 |

作者`causal/src/data.py:Document.get_labels`会把未列出的有向mention对映射为NONE；这是benchmark标签约定，不证明每一缺边都是人类单独审查的“无因果”。同一类任务应按发布图或明确规定的关系识别评价，不能将NONE改称世界事实FALSE。源码只读，未导入执行作者依赖。

RED并不是无条件通用知识：其TLINK章节要求文字证据、处理相邻句/并列句、区分时间包含与组成、分别定义原因与前置条件；MAVEN又简化和改动部分定义。完整必要E深度需以适用条款核实，不靠附加无用章节。尚缺版本适用审计、public-only构造、规范示例/近重复隔离、独立确认；仍不能主张学习轨迹比直接环境编译有优势。

所有文件在data/artifact对应v66；audit.py全量结果audit-private.json，source.json记录仓库完整性。无模型、作者代码、prompt/种子/预算/缓存、确认split或新工程测试（0），未联系作者/提交在线评测。下载会话89763正常结束，无活动进程。下一步可针对规范适用和公开图输入做有界构造；如必要规则仍短或不一致，应保留阴性结论而非扩大计数。
