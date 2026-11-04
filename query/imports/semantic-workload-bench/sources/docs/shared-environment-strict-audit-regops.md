# RegOps-Bench / RefWalk — Reject

已实际下载[原论文](https://arxiv.org/abs/2605.29742)、[完整官方仓库](https://github.com/yeongjoonJu/RefWalk)和[全部HF数据](https://huggingface.co/datasets/Y-J-Ju/RegOps-Bench)。代码commit4477f9d99470ca34484bbc4eb47e96432eccd2f8，57文件；HF commit566773593bc60e38792db92355422d8e713c6f0a。精确大小与SHA见[来源收据](../artifact/evidence/shared-environment-strict-regops/source.json)。未执行作者代码。

| 条件 | 本次直接证据 | 判定 |
|---|---|---|
| 共享E | 12份规章、718条article，text_ko共713077字符 | 环境规模成立；必要性仍需逐例证据 |
| 真实批量F | 实际231问：56 IITP_QA_BOARD、175 LLM_GENERATED | 56真实FAQ不足数百真实cases；不以扩增补N |
| 独立gold C/G | verified字段56True/175False；论文另有60问人工审查，47扩增＋13官方 | 字段False不意味着没有任何人工评审；60题审查不等于231完整审批gold |
| 固定任务A/E | 问题覆盖不同操作请求，难度等级不等于语义算子家族 | 未证明同一固定批任务及1≪K≪N |
| D | RefWalk本身是固定anchoring、检索、1-hop扩展、rerank、生成 | 不能将其优于其他RAG解释为固定流程不足 |

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 |
|---|---|---|---|
| 根据韩国研发经费法规回答大学外部研究人员参与的手续要求 | L1_ko_001，模型生成题，非真实审批case | 经费使用标准第48条及第8款，来自12文档共享库 | answer和gt_references，只供评分 |
| 类python的DAG | `scan(questions)`：231问，只有56官方来源 | `sem_map(anchor); retrieve; expand_refs(hops=1); rerank` | `sem_map(answer_with_citations); score_private`；不把QA异质性当作固定谓词批 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标：获取所属单位参与确认文件，计列经费后通知该单位；实际预测未知 | 同资源固定检索后sem_map回答与引用 | 同一目标；实际预测未知 | ==定位大学适用条款、外部人员条件与通知义务==；检查引用后回答 | `anchor -> seed_retrieve -> reference_closure -> cited_answer`，固定图遍历可实现，未测迁移家族 |

| 具体核验边界 | 已完成 | 未完成 |
|---|---|---|
| 数据与论文 | 全部数据下载并实数统计；读论文构造及人工审查段；查看首条完整题答和字段 | 首题不是官方来源；没有声称原文支持answer中全部额外手续细节 |
| 20条gold | 因F先行失败不继续为其做准入审计 | C20=0；不冒充20已闭合 |
| 方法结果 | 仓库包含多种固定检索基线实现 | 未运行LOTUS、Agent、作者模型、抽取或成本实验 |

[数据实数收据](../artifact/evidence/shared-environment-strict-regops/data-audit.json)。可保留作引用闭合检索的方法参考，不列入Strong候选。
