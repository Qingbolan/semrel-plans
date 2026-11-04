# 增量168：UCCA官方评分运行与规范冲突

复用166原论文/完整数据规范和167完整评分repo，不是新湖，仍8/15。上一167为结构/划分证据。本轮新增实际官方解析/评分，而非仅看源码。使用现有Python3.12.7、numpy1.26.4、tqdm4.70.0，无spaCy安装；基础评分路径可以调用，不声称所有语言工具可运行。

## 当前证据

随数据v2指南末尾Remotes条目5(a)明确R/F不应作为remote。167统计的52个R/remote经本轮保存清单，分布40个passages。具体passage106，父1.391→子1.259，子覆盖that，原标签R/remote。将其仅从内存预测副本移除，调用原官方labeled、normalize=False评分，remote匹配从参考22减为21；primary325及implicit3都保持全匹配。源文件未改。这表明该边在评分中真实计入，与该条规范存在待解释冲突；不能声称官方评分会自动忽略。

另一个并行审计对全部367图分别解析两个副本并做labeled self-score（normalize=False），用于核对基本评分链路；附带删除passage20共享A边的normalize False/True比较。脚本`artifact/evidence/shared-environment-audit-20260908-v168/audit.py`，shell session96797。**本卡初次写入时尚在运行，未填写全量通过结论**；后续以self-score.json/remote-deletion-probe.json及进程终态为准。self-score即使1.0也只是参考与自身一致，不是模型质量。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 抽取共享参与者并生成场景关系表 | 367文本passages | 37页v2规范 | 固定tokenization；27文章分组 | 9765A/remote；全图规范仍含52R/remote冲突 |
| 具体passage106重现图边 | that对应原节点1.259 | 指南Remotes5(a)不允许R作为remote | 原父1.391 | 发布R/remote；这是gold与E不一致的诊断，不应强迫模型遵循矛盾目标 |
| 具体passage20第二Scene共享Pitt | 完整文本 | remote参与者规范 | 两个Scene关系 | 发布A/remote；正常语义目标，待删除边评分探针完成 |

| 类python的DAG | 具体数值 | 边界 |
| --- | --- | --- |
| `parse_xml().score(reference_copy)` | 全367启动，初始记录时尚运行 | normalize=False基础链路自评分，不是实验准确率 |
| `delete_one_R_remote().score(reference)` | passage106：remote21/22匹配，primary325/325，implicit3/3 | 只动内存预测，原始数据保留 |
| `sem_map(parse,E).project(scene_participants)` | 原目标A/remote9765 | 需先界定规范/标签一致的任务，不以全面图F1替代下游正确 |

以下语义方法比较仍未执行。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正常共享参与者目标与原A/remote一致，实际未知 | 固定规则解析与同资源场景识别 | 相同目标 | ==核对省略参与者和remote规范==→关系表 | `SceneParser→SharedParticipantResolver→Projection` |
| R/remote冲突无法同时满足E和gold | 固定流程应记录规范冲突，不靠当前gold补特例 | 相同约束 | ==发现规则与冻结目标不一致==→报告构造缺口 | 冲突处理属于构造/评测契约，不当Agent优势或新算子 |

无模型/prompt/训练/种子/token费用预算/推理并发缓存/正式快照/commit。本轮评分是上游工具诊断；环境有效性与15湖目标未完成。下一轮先读取session96797终态，不能因观察超时重启。
