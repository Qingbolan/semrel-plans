# 增量189：CSTNews RST层与E用途审计

复用187已下载官方完整6.0发布、2011原论文和2014学位论文。上一轮有效进展，本轮全量检查主目录140RS3，另30文件位于一致性子目录。原件未修改，仍11/15。

原生140篇全部XML可读，5528segments、5023group出现次数；136单根、3双根、1三根。3篇有重复ID：C27/D2 id55、C36/D4 id128、C47/D4 id79，重复group属性完全相同；最后一篇group type为空。group数含重复出现，不能当唯一节点数。parent ID映射检查无悬空、未发现循环，但重复节点存在时不能声称完整树验证成功。

直接RST定义为学位论文附录A，1675词、6个提取页分隔；CST定义附录B553词。§5.2明示训练读取Mann/Thompson和Carlson/Marcu分段手册，表5.1列葡语适配：相对从句分段、归属动词/有生命或机构主语、强标记等。**长分段手册仅在端到端分段任务中可能必要；给定EDU的关系任务不能借其长度满足长E。** 需要核验完整分段规范与原文到EDU一致性，不能把两个任务的资源用途混为一谈。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 原文→分段→RST关系→摘要 | 140真实报道、50事件组 | 分段手册＋葡语表5.1适配；具体版本/完整必要章节待核 | 原文及文章/事件元数据 | 5528源EDU边界、RST图；摘要另有人类标注 |
| 给定EDU→归属关系 | C1 D1 EDU2“据联合国一位发言人”及EDU3飞机着陆情境 | Attribution等直接定义，附录A1675词 | 本篇全文 | 2→3 attribution |

| 类python的DAG | 具体数值/输出 | 边界 |
|---|---|---|
| `scan(texts).sem_map(segment,E_seg).sem_map(rst,E_rel)` | 140文档；原生5528EDUs为目标数量 | 分段与关系需分别评分；输入全文parity未完成 |
| `graphs.filter(attribution).project(source,content)` | 具体2→3；全源attribution503出现 | 不能把“据”单词检测当已验证算子 |
| `clusters.join(predicted_graphs).sem_map(summary)` | 50事件组有下游参考资源 | 本轮无模型输出/摘要对齐或质量实验 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| C1例切开消息来源与陈述，关系2→3；实际未知 | 固定分段sem_map→关系sem_map，同资源规则检索/图验证可用 | 相同目标，实际未知 | ==查葡语归属分段适配与Attribution定义== → 输出边界和图 → 固定验证 | `Segmenter(E_seg,adaptations) → RSTParser(E_rel,graph_validator)` |
| 给定EDU关系目标相同；实际未知 | 仅必要关系规范直接调用/预编译 | 相同目标，无预设优势 | ==核对当前输入已给边界== → 关系判断 | 不将已完成的分段工作计作Agent环境探索收益 |

==是可观察查阅步骤==。同资源固定程序、Coding Agent和E-only编译仍是必要对照。缺少完整默认路径、源文parity、分段E绑定及独立确认，暂不加入合格湖。下一步应判断端到端分段路线是否实际有完整证据，不为凑数保留给定EDU的长E主张。

证据：`artifact/evidence/shared-environment-audit-20260908-v189/audit.py`及`audit.json`。无新下载、安装、模型调用、源数据修复或正式快照。
