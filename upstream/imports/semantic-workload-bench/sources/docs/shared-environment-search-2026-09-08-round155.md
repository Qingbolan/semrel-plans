# 增量155：SOFC-Exp实验图谱，完整来源已取得，样例污染后规模有限

状态：`SOURCE_ACQUIRED_NATIVE_AUDITED_SCOPE_PENDING`，仍8/15。此源可形成多个有关联的批任务，但未证明短句筛选需要整个长规范；跨实验关系任务更符合复杂E，却仍需核验范围与独立文档规模。

## 下载及实读

- [原ACL2020论文](https://aclanthology.org/2020.acl-main.116.pdf)已下载，357851 bytes，SHA256 `0d6a3dd57d517f45aaeb83b91dd3964c40b14684884b26561f836501a6f74799`。
- [完整作者仓库](https://github.com/boschresearch/sofc-exp_textmining_resources/tree/bbf75fdda4ba68fe8041fdc2780acd2a134e9770)，commit `bbf75fdda4ba68fe8041fdc2780acd2a134e9770`；ZIP3753032 bytes、284成员、CRC通过，SHA256 `7c66ef7c6238f55b3e5427d7b4e67bbe56b9a280ae0893b537e2b2167dbc3125`。
- 仓库原生`sofc-exp-corpus/sofc_exp_guidelines.pdf`，22页、1210222 bytes、7376空白词，SHA256 `6a3f3d84ddc5eab1e1ab8188153dcc4bd4e4e05acdda037c58ff27824a0d2ab3`。版本1.0，2020-06-02。已抽文本并渲染检查首页，含具体实验图、16种槽位及关系规则。22页含示例、图与背景，不能都当必要规则。

原件位于`data/shared-environment-audit-20260908-v155/`；收据、可重跑audit.py、audit.json、documents.json和examples.json位于`artifact/evidence/shared-environment-audit-20260908-v155/`。examples含原gold，只供构造审计。未下载每篇原文PDF；当前输入是仓库发布的PDF抽取文本，不宣称含完整图表。代码AGPL-3.0与README说明的数据CC-BY-4.0分开，指南页脚保留权利文字，外发指南授权范围应单独确认。

## 本轮原生核验

45篇文本、9466句，876句标签1。5495个SPAN：1859 MATERIAL、598 DEVICE、1547 VALUE，以及1091实验触发span（731 current_exp、93 general_info、255 previous_work、12 future_work）。1032个EXPERIMENT框架，3149条16类槽位边；另88 thickness、335 same_experiment、116 experiment_variation、268 coreference链接。

全句子/实体边界及框架/槽位/关系引用检查无失败。句子标签与“句内存在任意EXPERIMENT触发span”完全一致。首次错误地以“拥有框架实例的触发span”验证，产生25句差异；回读README后修正审计定义，未改源gold。59个触发span没有框架实例，不能把触发数1091当框架数1032。首次路径后缀误用txt，改为真实csv后完成审计。

作者明确实体/槽位仅在实验描述句中完整标注，其他句子只有部分标注。因此全9466句可做派生实验句二分类；NER/槽位质量不能用其他句子的空标注评估。句子gold本身由人工触发span派生，不是第二份独立标注。

手册出现19个PMC ID，均属于这45篇。若保守排除整篇，仅26篇、5038句、457正句、556框架。仍能批处理很多句子，但独立研究文档只有26，不能称5000个独立论文案例；本轮未重新统计排除后的槽位/关系及构造正式split。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 范围 |
| --- | --- | --- | --- | --- |
| 为燃料电池文献库建立实验描述句索引 | 45篇原生抽取文本9466句 | 同一22页规范的实验定义及触发类型 | 给定句边界与全文上下文 | 876正句；派生于人工触发span，短定义可能已够，不证明长E必要 |
| 抽取电池材料—工作温度—功率密度表 | 显式给定876实验描述句，或者先执行前述筛选 | 16槽位定义与实体/实验关联规则 | 上下文文本，所有方法同资源 | 1032框架3149槽位关系；该上游给定设置须披露，不冒充端到端质量 |
| 合并同一实验提及，区分实验变体 | 同一文档内实验提及与上下文 | same_experiment、experiment_variation、coreference规范 | 需要冻结给定或预测实验图输入 | 335同实验、116变体、268共指边；有显式原生关系gold，传递闭包/聚类未核验 |

真实原生例PMC5793538/frame3：电解质ZnO，device为fuel cell，功率密度`158–482 mW cm−2`，开路电压`1–1.06 V`，工作温度`450–550 °C`。这些是范围，不能伪造为一一对应的逐温度测量点。该文章也被指南引用，只作开发解释，不作为独立确认样本。

| 类python的DAG | 具体数值 | 必须保留的语义 |
| --- | --- | --- |
| `scan(texts).explode(given_sentence_offsets)` | 45→9466句；已知指南例排除后26→5038 | 使用句偏移，不能简单按换行当句界 |
| `sentences.sem_filter(describes_experiment,E,context)` | 全源目标876正句；排除后457 | 触发span存在即可，不要求已经有框架实例 |
| `positive_sentences.sem_map(extract_frame_slots,E)` | 全源1032框架3149边 | 实体与触发节点、16角色分别输出；多角色/多实验不能扁平化为一句一行 |
| `frames.project(material,temperature,power).collect()` | frame3：ZnO、450–550°C、158–482mW cm−2 | 保留区间和来源，不自动生成端点配对；不是数值实验表真值的额外独立核验 |
| `mentions.sem_map(link_same_or_variant,E).group()` | 全源335同实验/116变体 | 关系方向/闭包一致性与聚类gold尚未验证，暂不运行聚类评测 |

以下是目标与预期操作，不是执行结果；未调用LOTUS/Data Agent。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| frame3输出ZnO电解质及两个测量范围，实际未测 | 固定sem_map按同槽位规范抽取，按frame连接，确定性保留单位/范围 | 相同目标，不预设更高质量 | ==查电解质角色与温度/功率槽位，检查同句多实验指向==→返回结构化框架和依据 | `ExperimentMentionDetector→RoleBinder→RangePreservingProjector`，内部结构须由真实轨迹验证 |
| 实验描述句筛选目标876，未测召回 | 固定规则/语义调用识别所有相关触发，不把未来或前人工作机械排除 | 相同目标 | ==确认current/previous/general/future类型的任务范围==→输出Boolean | 带任务范围参数的判定器；短E编译是必要强对照 |
| 同实验与变体关系分别输出，不合并两类 | 固定检索与链接程序也可读相同文档和规范 | 相同目标，尚无可评估闭包结论 | ==查同实验/变体条件，回读公开实验上下文==→有类型边 | `MentionLinker→TypedGraphValidator`；需原生gold关系审计后才定义聚类算子 |

本轮完成来源下载、原生结构核验和污染规模初查。没有足够依据将SOFC-Exp列入15个已合格湖：句筛选未显示复杂E必要；关系任务仍需闭包/源实体/排除后范围核验，26篇确认空间有限。保留该来源作为材料实验图谱开发候选，不拆成三个湖。无模型/训练/费用/种子/推理预算/正式快照/测试套件/评分/commit。
