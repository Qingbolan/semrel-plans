# 第68增量：UMR完整来源及元数据审计，不能把转换/未发布项当人工gold

合格仍3/10。UMR是新的潜在数据湖，语言版本与同源翻译不拆成多个湖。本轮取得长规范、真实源数据与图标注，但公开可执行人工gold的范围尚未冻结。

[原论文Building a Broad Infrastructure for Uniform Meaning Representations](https://aclanthology.org/2024.lrec-main.229/)完整下载518912bytes，SHA256 1fac9c3b0c5fdabc3f60d18450fed8ee0e1fef149093c82435d9034895163676。它描述UMR1.0，不能以其人工标注说明自动覆盖当前3.0所有转换记录。

| 完整作者仓库 | 冻结commit | ZIP bytes/条目 | Git blob验证 |
|---|---|---|---:|
| [umr4nlp/umr-data](https://github.com/umr4nlp/umr-data) | ae46502fe27c7bf61978cb466dd2fc8312cb2ef8，2026-08-24 | 59149442/7774，CRC通过 | 7755，tree未截断 |
| [umr4nlp/umr-guidelines](https://github.com/umr4nlp/umr-guidelines) | 215f88e27528e0ebaa798caa2ba399b311642cb5，2025-05-26 | 443430/26，CRC通过 | 22，tree未截断 |

完整guidelines.md为365742bytes、48221空白分词；SHA256 f60deebff42ef5262bc5bb95d9f69142e2792bff0308388c315c912bf75aa612。文件标题仍为UMR0.9、August8,2022；这是文件实际标识，与Git更新日期不同。当前数据README标UMR3.0，必须核实适用版本差异；未渲染规范成PDF，因此不推测页数。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 对真实文档按统一UMR语义规范构造句子图与文档图，形成带事件参与者、体貌、时序与说话者确信程度的语义索引 | 48221词规范，图结构、谓词论元、量化、体貌、模态与跨句关系 | 语言对应概念/角色资源和版本适配，是否完整须核查 | 原仓库分语言UMR文件；文本/词形/译文及graph混存，需public allowlist | 当前图标注混有人工、确定性转换、LLM辅助转换和未发布占位；不能全部作为独立人工gold |
| english_umr-0001首句：200 dead, 1,500 feared missing in Philippines landslide | 文档级模态区分已肯定事件与不完全肯定事件；未把恐惧内容当已肯定事实 | 若选给定句子图→文档模态节点，必须显式annotation-given | source Words行及完整文档；首句图有landslide/die/fear/miss节点 | author→landslide/die/fear为full-affirmative，author→miss为partial-affirmative；这是标注目标，非本轮模型结果。此类专项任务只依赖规范子集，不能借整个48K词证明必要环境长度 |

| 类python的DAG | 具体数值/本次观察 |
|---|---|
| `inventory=scan_umr_files()` | English584文件、Chinese49、Czech7086；文件不是自动独立来源实体 |
| `eligible=filter(metadata,required_text,annotation_provenance)` | 英文partial_conversion30058块/569文件；not_in_release849块/106文件；无type标记627块/94文件。文件分类可重叠，不能相加当总文件数 |
| `graphs=sem_map(public_document,applicable_full_schema)` | 可候选为完整语义图构造，未实现public构造、图解析或模型运行 |
| `modal_index=project(document_graph.modal)` | 若仅做模态，则上游句子图是否给定及所需规范长度要重新明确，不能隐含偷读gold节点/模态 |
| `evaluate(predicted_graph,private_gold)` | 未实现/执行；本轮只做结构存在性和来源清点，不报告图匹配F1或运行质量 |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 首句例的miss目标partial-affirmative，其余上述事件full-affirmative；是否预测正确未知 | 同完整必要输入下固定语义映射、规范检索与图校验；若给定句子图则两臂同时给定 | 同一目标，不预设更好 | ==区分fear事件与其内容；查UMR模态归属和强度规则；核节点与跨句指称；保留作者立场而非模型常识==→模态边 | 语义节点/作用域→立场来源→模态强度→图引用校验→可查询索引；只是预期结构，未从轨迹提取 |

**实际清点与纠错。** 初次二分partial/nonpartial会把not_in_release混入“非转换”；修正为按原type完整分组。英文849个not_in_release块仅3个有Words行，即846个缺此原文域；句子图域非空也可能是占位，不证明有gold。英文无type的627块都有Words行；中文无type976块/48文件、partial1500块/1文件；捷克全175268块/7086文件标partial_conversion。未把无type直接改称人工审核通过。

源码作者统计的nonpartial并非我们要求的可执行人工gold集合。英文README还明确记录3.0中的确定性转换、人工转换，以及3226/3295个有歧义代词决策经LLM辅助消歧；必须核对应记录是否有独立人工审核及当前所选目标是否受影响。不能拿仓库59MB或超过20万句推导出同规模人工语义决策。原论文1.0英文其实只有5文档209句，而不是209独立文档。

审计中的doc_graph计数只使用关系三元组形状检测，不能代替完整Penman解析、引用闭合或语义合法性验证。原先以字符串非空判存在会把注释/空骨架当有效图，已改为更窄的存在性诊断；当前仍不据此设置VALIDATED。句子边/节点与源词对齐、跨文档ID及必要frame库尚未核验。

英文README声明CC BY-SA4.0，中文为CC BY-NC-ND4.0；不同语言与上游文本权利须分别核对，不将仓库统一视为任意再分发许可。未发布项不可从其他gold逆向补原文。没有模型/作者代码执行或公共发布。

下载/全量Git校验/元数据audit.py与收据：artifact/evidence/shared-environment-audit-20260908-v68；原资产：data同名v68。新工程测试0，无prompt/种子/模型预算/缓存/确认split，未commit。下一步针对有原文的实际候选记录核对人工来源、完整规范适配和源实体数量；若只有小量完备记录，保留小样本路线，不将转换量包装成合格大批量。
