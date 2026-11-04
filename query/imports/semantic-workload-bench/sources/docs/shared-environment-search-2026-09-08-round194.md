# 增量194：X-WLP环境篇幅与双表示差异

复用193下载的两篇原论文、完整作者仓库及指南；本轮未新增下载。实际读作者peg.py的to_amr和peg_to_amr.py的edge_to_amr，并审计279原始PEG。可复现脚本/结果位于artifact/evidence/shared-environment-audit-20260908-v194/audit.py和audit.json。

指南22页3501词中，第7–22页（Reference附近至末尾，仍含操作/界面说明）合计2219词。页码只是定位，不将其全部认定为必要推理规则，更不将每条实验protocol长度计为E长度。当前没有证据证明该湖满足用户要求的长共享环境；暂不纳入，仍11/15开发可构造来源。

193的14处inputs/outputs缺失分为12处input和2处output重复目标，涉及12篇。本次所有link路由键均指向存在节点，缺失0。作者to_amr遍历反向图的edges，再由edge_to_amr读取edge_data中的slot路由；并不直接遍历节点inputs/outputs来造这些边。因此“节点元数据存在悬空引用”不等于“AMR转换必然报错”，也不证明两种表示语义全等。本轮没有运行转换、没有证明缺失产生原因、没有自动删字段。

具体protocol0/op_14的inputs仍含tl_usage_of_enum=mth_1，但mth_1不在nodes；它的相邻links只记录loc_1通过a槽连接ev_41→op_14→op_16。用node.inputs评参数绑定，与用发布AMR评图可能测试不同答案集合；必须先冻结哪个表示为任务gold，再做转换一致性核验。不得在实验失败后挑有利表示。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 协议→操作类型/参数绑定 | 279真实协议txt，与graph句子逐行一致（193） | 22页指南，参考及后续部分2219词，必要长E未证 | 明确allowlist的上游实体，不给答案边 | node.inputs与links/AMR是需分别绑定的表示 |
| 跨句物料共指→过程图 | 同协议公开上下文 | 共指和时序说明 | 前序操作预测 | 1703共指节点，不能扩大为实验结果gold |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `scan(docs).sem_map(type,E).sem_map(bind,E).assemble_graph()` | 279协议；12处缺失input、2处output | 原始元数据任务仍有一致性缺口 |
| `evaluate(predicted_graph, frozen_amr)` | link路由键缺失0 | 作者转换基于links；本轮未运行评分或证明AMR等价 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 在预先冻结表示上输出类型和绑定，实际未知 | 同资源固定调用与公共图检查，可先直接编译完整短规范 | 同目标，实际未知 | ==查槽位和跨句实体状态== → 绑定 → 检查 | `TypedOperationMapper + StateResolver` |
| 不能预设某系统会“修正”mth_1答案 | 预测过程不读private输入/边差异 | 同样禁止用gold差异修答案 | ==检查公开实体ID== | `PublicReferenceValidator`，不含私有修正表 |

未运行模型，未建立质量或成本优势。阴性结论仅为现有证据不支持长共享E，并非断言此任务容易。保留来源用于过程语义研究，但不继续以格式审计替代第12–15个独立合格湖。
