# 结构化算子 × 语义算子：逐查询 Plan 图册

整理时间：2026-10-05，Asia/Singapore。回顾窗口以本仓最近集中调研的 **2026-10-01—10-02** 为准；未发现10月3—4日的新账本条目。2026-10-05补充核对上游源码，不把今天的主分支说成两天前的冻结版本。

打开 [交互式图册](../index.html)：左侧按 benchmark / 查询筛选，右侧逐节点查看关系算子树。完整逐条文本树见本文下半部；机器版见 [plans.json](../assets/plans.json)。

## 本次列出的范围

| 来源 | 本次逐条绘制 | 完整性与口径 |
| --- | ---: | --- |
| SemBench | 60 | 当前固定commit中 movie 10、animals 10、cars 10、ecomm 14、MMQA 16；覆盖这五个已讨论场景的当前非draft查询定义。论文曾报55条，不能把两个版本数量直接等同；medical不在此前五场景范围内 |
| TAG-Bench | 12 | 选出结构不同的源码实例：0/1/3/4/5/6/8/10/11/48/50/85；不是全80条的穷尽清单 |
| UDA-Bench | 6 | 每个数据域1条实际SQL；是608条源码查询中的实例，不是完整清单；语义抽取是端到端解释节点 |
| 最近讨论的派生任务 | 10 | TAR、TREC Legal、ContractNLI、MAUD、ShARC、ClinGen、TalentCLEF，以及Trial Q1/Q2/Q3；不是10个独立benchmark |
| **合计** | **88** | 每条有单独的计划、源链接、实现口径；不以数量证明质量或研究收益 |

这不是“所有读过的论文里全部查询”的普查。LOTUS FEVER/BioDEX、Palimpzest、DocETL/MOAR等此前记录多停留于工作负载摘要，本册没有仅凭名称捏造逐查询树；BIRD普通Text-to-SQL也不自动算执行期混合查询。CRC对应简历缺失，没有列为可执行任务。

## 图的语义

- 输出在根部、输入在叶子，从下往上读。橙色 `SEM_*` 表示语义判断/抽取/排序/归纳；蓝色是确定性关系操作；灰色是输入。
- `σ` 选择，`π` 投影，`⋈` 等值或条件连接，`γ` 分组/聚合，`τ` 排序，`δ` 去重。SEM_MAP产出属性，SEM_FILTER保留满足谓词的行，SEM_JOIN判断两行的语义关系，SEM_TOPK语义排名，SEM_AGG跨行归纳。
- 这些是人工对照查询与源码整理的**逻辑计划**，不是数据库EXPLAIN、执行轨迹或自动提取出的算子。图不指定LLM、join算法、缓存或实际调用次数。
- 同时有Scan和SEM_FILTER不代表复杂混合。本册把“仅投影+语义操作”标成轻混合；重点结构有普通过滤、键连接、聚合、排序、集合运算与语义操作的组合。
- 将确定性过滤画在语义操作下方是逻辑依赖表达，不承诺源码引擎采用该执行顺序。随机LLM的重排、缓存等价性需要单独验证。
- CTE和相同子树可以形成DAG；树中重复展示不表示必须重复计算。环境文件绑定通常是语义算子的参数，不凭空画成一张关系表。
- 语义预测失败、NULL和ABSTAIN不能自动当成语义FALSE；图只刻画原查询的选择关系，不新增错误处理协议。

## 最值得对照的结构

| 查询 | 结构 | 可研究的具体问题 |
| --- | --- | --- |
| TAG 0 | 去重县名 → 语义判断 → 半连接回学校 → COUNT | 判断粒度是否可由学校行缩小到县；物化键及版本如何定义 |
| SemBench movie Q4 | 语义布尔属性 → SUM/COUNT | 为什么保留分母必须用map而不是先filter |
| SemBench animals Q6/Q8 | 多语义分支 → 反连接/交并集合 | 局部错误如何传播为漏报/误报的最终城市清单 |
| SemBench cars Q5/Q6 | 多表键连接 → 多模态判断 → 去重/不一致筛选 | 多记录乘积、车辆粒度与NULL如何改变结果 |
| SemBench ecomm q10/q11 | 多分支语义过滤 → 多次语义连接 | 一元属性物化能否替代昂贵配对，且不改变语义 |
| SemBench MMQA q4 | 多标签抽取 → UNNEST → GROUP BY | 集合值输出如何接入标准关系运算 |
| UDA Player/FilterJoin/2 | 文档→结构属性 → 四表等值连接 | 语义成本在物化阶段，之后SQL可跨查询复用 |
| TAG 85 | 普通选择/连接 → SEM_AGG | 跨行归纳不能由逐行布尔判断替代 |

最直接的观察：**混合查询已广泛存在，但复用单位不同**。可以复用单行属性、去重后的实体判断、二元配对关系或整个物化子计划。仅画出更多SEM节点不构成动态算子库证据；先选最终输出、记录粒度及错误传播明确的查询，再比较保留质量后的完整成本。

## 核对中发现的边界

- SemBench movie Q10：自然语言称rank，当前BigQuery SQL没有ORDER BY。
- SemBench MMQA q5：BigQuery文件为空；所画关系除法是候选实现。
- SemBench MMQA q7：自然语言要求欧洲航线，BigQuery SQL缺少该谓词；图按用户查询意图绘制并标出差异。
- SemBench ecomm q8：输出将同一图片ID拼接两次；q14按语义分数升序取1，不能误画成最高分。
- SemBench cars Q4：连接后按投诉行加权求车辆年份平均值；Q6存在多行放大及源码括号风险。本次没有验证其可执行性。
- TAG 4：自然语言cities与手写基线County不一致；TAG 5先取前20名字再做语义过滤，属于可能影响完整性的截断。
- UDA Med示例混用带Med_前缀限定名和无前缀表名；计划归一化名称，但没有修复源SQL。
- TalentCLEF只有正向相关性参考标签；ClinGen/MAUD等是本仓派生任务，不能称上游原生SQL benchmark。

这些是本次静态核对的发现，不是运行失败率或质量实验。没有模型推理、gold评分、数据重建或确认集访问。

## 来源与可复核性

- [此前语义系统侦察](references/research/evidence/dataset-scout-2026-10-01/scout-semop-systems.md.txt)、[UDA属性共享率](references/research/evidence/uda-attr-sharing-2026-10-01/README.md.txt)、[五个SEM_FILTER构造方案](references/research/sem-filter-workloads-2026-10-02.md.txt)、[招聘审计](references/research/recruitment-benchmark-audit-2026-10-02.md.txt)。
- SemBench commit `8c2cac89b21c6782239e8e5b03d326d0c029b655`；TAG-Bench `f97b0b5ca211573837cf3236224ac658b4a959bc`；UDA-Bench `50039a527f156eeb9cad80118637da47db94b976`。
- 每条源链接指向固定commit；本地派生任务源链接指向当前文档。源文件SHA256见 [source-receipt.json](provenance/source-receipt-2026-10-05.json)。不复制源数据、gold或私有材料。

