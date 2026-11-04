# 第三十一增量：PANORAMA状态审计及ALLOW语义纠正

**累计仍1/10。** 本轮对第30轮已完整下载的2,884测试项/164申请开展源文本状态审核；没有新下载、没有模型调用，也没有把诊断正则输出直接覆盖为gold。

## 纠正上一轮容易混淆的结论

原论文附录NOC4PC提示明确：ALLOW表示相对于给定对比文献具有新颖性和非显而易见性。它**不是整体专利准予**。所以仅看到§101/§112驳回、形式异议或依赖权利要求需改写，不能直接推断其ALLOW标签错误。第30轮用“准予”概括该任务过宽，后续统一称“相对于给定对比文献不因§102/§103被驳回”。原报告保留并追加指向本轮的澄清。

上轮15886404/claim10的withdrawn仍不能提供已完成的新颖性判断；但它只是个案证据，不代表所有非allowed状态都错。不能通过对已知错误过度泛化来排除可行来源。

## 本次具体检查

用原始CTNF显式`Claims ... are rejected/allowed/withdrawn/objected to`语句抽取编号集合，保留原文跨度、上下文及复合状态，不只取第一个状态。2,884项全扫；在597个发布ALLOW中：

| 原文关键词状态组合 | 数量 | 本轮解释 |
|---|---:|---|
| 无明确正则命中 | 170 | 格式/省略等原因待审，不等于缺gold |
| allowed | 76 | 明确候选，仍需审查版本与上下文 |
| objected to | 229 | 不能自动当错误；可能依赖改写后可准予 |
| allowable + objected to | 2 | 同上 |
| rejected | 70 | 必须区分§102/103与其他条款 |
| objected to + rejected | 17 | 保留两个维度，不能折叠为一个程序状态 |
| allowed + rejected | 2 | 可能不同理由或语境，待逐项审查 |
| withdrawn | 31 | 发布ALLOW缺相应实体结论的候选，不能当已全量验证错误 |

351条命中某种表面冲突、涉及62申请。**351不是错误数量**。进一步要求rejected后紧跟明确§102或§103条款，得到7项/5申请；已逐条读取这些命中语句，包含原编号范围和具体对比专利：

| 申请 | claim | 发布 | 源CTNF明确条款/对比依据 |
|---|---|---|---|
| 13656362 | 6、12 | ALLOW | §103，Escott＋Hashimoto；源parsed_CTNF把6列为isReject=false，原文4–8及10–12等范围明确驳回 |
| 14873283 | 19、20 | ALLOW | §103，White＋Kim，原文范围13–15、19–20 |
| 16655280 | 22 | ALLOW | §103，Goldstein＋Nishizawa，原文范围1–14、16–26 |
| 15010126 | 12 | ALLOW | §103，Curtis，原文4和12 |
| 16600737 | 7 | ALLOW | §102(a)(2)，Chmara，原文范围含6–10 |

这些是明确的源语句与发布标签不一致，不是新专利专家判断，也不证明正则未发现的其他行全部正确。可修复路径成立：原文包含足够的直接裁决证据来重新提取这批标签；但还需核对审查时点、初始claim与该轮claim版本是否一致，以及全部状态/多重条款。故尚未发布修复快照或计为第二个合格湖。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 逐项判断权利要求相对于给定对比文献是否因§102/§103被驳回 | 第30轮下载的524页MPEP2100，适用版本仍需绑定 | 2,884测试项/164申请，claim依赖与版本需要核验 | 对比专利及作者按审查员引用预选段落；annotation-given条件 | 597发布ALLOW含本轮7处直接§102/103冲突；不可直接称gold清洁 |
| 13656362 claim6与12，开发例 | pre-AIA§103及具体比较标准 | 加密通信方法及其依赖claim | Escott、Hashimoto；不能读本案CTNF判断文本作为输入 | 发布ALLOW；原CTNF明确§103。尚未运行任一方法 |

| 类python的DAG | 具体数值 | 用途 |
|---|---|---|
| `construct.join(test, source)` | 2,884项/164申请 | 构造侧，不挂载source审查结论 |
| `audit.explicit_claim_status_spans()` | 597ALLOW中351表面冲突候选 | 仅筛查，保留混合状态，不变成gold |
| `audit.match_direct_102_103_ground()` | 7项/5申请，逐条读取命中 | 直接语句证据，不是全量错误率 |
| `run.sem_map(patentability,E,claim,prior_art)` | 未运行 | 需同版本必要输入和修复gold |
| `run.sem_filter(no_102_103_rejection).count()` | 正确参考数尚未冻结 | 不用597或597−7当作修复后gold总数 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 13656362/6、12的源参考为103，发布ALLOW不可用于把正确103打错；实际表现未知 | 固定claim依赖展开、特征对应、单文献/组合分析及动机规则，同资源缓存可用 | 同源参考，不预言优势 | ==核对claim版本和AIA分支==→==逐个限制对应到允许对比文献==→==检查组合动机与缺口==→输出103/102/ALLOW/ABSTAIN；当前CTNF只给评分器 | `PatentabilityOperator(E_version, claim_graph, feature_alignment, single_reference_test, combination_test, evidence_gaps)`；程序状态和实体评价分开，不能由未驳回推准予 |

原论文/完整repo/数据/官方E链接与hash沿用[第30轮](shared-environment-search-2026-09-08-round30.md)，未重复下载。新脚本和私有诊断在`artifact/evidence/shared-environment-audit-20260908-v31/`：`audit_status.py`、`check_conflicts.py`及带原文跨度的JSON。未执行作者代码，未新装依赖，使用既有audit-venv/pyarrow；无公开输入构造、确认划分或模型实验，工程测试新增0。
