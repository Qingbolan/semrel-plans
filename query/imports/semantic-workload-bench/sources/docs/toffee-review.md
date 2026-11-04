# TOFFEE：方法相关性与 workload 资格复核

已下载完整4页论文、官方仓库34文件（commit `83d202ff2f47729f36724adcd6093a2ae44d7052`），以及完整TOFFEE-30K JSON：855,734,270 bytes、30,000条记录。原始材料在 `data/toffee-review/`，哈希与全量扫描收据在 `artifact/evidence/toffee-review/`。未运行作者代码或模型。论文许可不能自动覆盖代码和数据；未核实明确的代码/语料许可。

结论：重要相关方法/对照，当前不是已验证Strong workload。完整语料结构扫描已完成，独立gold与环境重建仍未闭合；不追加正式Strong数量。后文保留初次检查与后续扫描的证据区别。

| 核验项 | 本次观察 | 对当前研究的含义 |
|---|---|---|
| 共享E | 同数据库环境下复用前缀；真实语料环境另从七个benchmark获取 | 支持环境探索有重复，未证明固定q的真实case批量 |
| 任务与gold | bottomup.py先执行SQL得到answer key，再形成问题/执行检查 | 可构造数值分析题的执行真值，不是独立真实case的专家decision |
| 复用 | prefix_cache.py按env_fingerprint分组，register排除result_exists/answer_drafted；选择schema_discovered前缀 | 主要是发现阶段的状态、消息与工具观察复用 |
| 学习对象 | LCM配置选择、MCTS轨迹搜索，输出SFT/ICL样例 | 不等于从单条轨迹自动提取参数化语义算子 |
| 固定方法 | 原生任务由可执行查询构造 | 必须纳入一次Coding Agent生成SQL、固定SQL与共享探索缓存；不能假设固定方法不足 |
| 实验 | 论文预实验比较Single-Pass、Best-of-5、无LCM与完整方法；下游KramaBench/DSBench | 非LOTUS对照；本轮无复现，无独立prefix-only收益量化 |

代码事实：search/mcts.py调用find_reusable_prefix，并通过clone_with_new_provenance启动新任务。prefix_cache.py的_selection_score使用奖励/UCB；entry_units参数未参与该分数。不能把这段实现解释为已验证的任务语义家族路由。README的bandit.py、memoization.py、agent_runtime目录名称与下载清单不一致；实际文件为lcm.py、prefix_cache.py，未见agent_runtime。

## 具体数据与可复核数值

这是官方仓库明确标注的synthetic demo。下述Query由本次研究指定，不冒充论文原题或真实客户需求。

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 |
|---|---|---|---|
| North区域Q3的订单总额是多少？ | orders.csv：240行；order_id/region/product/quarter/amount | marketing.csv：32行；本题无需使用 | returns.csv：70行；本题按订单额，未定义扣退款 |
| 类Python DAG | scan → filter(region=='North', quarter=='Q3') → Decimal sum(amount) | 不读取 | 不读取 |
| 本地实算 | 8条匹配，4534.03 | 不适用 | 不适用 |

| 预期关键操作交给LOTUS的结果 | 预期LOTUS执行过程 | 预期Data Agent结果 | 预期Data Agent执行过程（==标注探索==） | 预期operator结构 |
|---|---|---|---|---|
| 正确条件下4534.03；未实跑LOTUS | 提供明确列映射后固定filter+sum；本题无必要语义LLM算子 | 正确条件下4534.03；未实跑Agent | ==列目录、检查schema/样例、确认amount含义与Q3编码== → 执行筛选聚合 → 核对8行 | aggregate_orders(region,quarter)，固定SQL/关系程序即可 |

| 比较臂 | 本例合理预期（非实测） |
|---|---|
| 仅任务、无文件 | 不足以得到数值 |
| 完整资源固定程序/一次Coding Agent | 生成参数化SQL后可批量复用；强对照 |
| 逐题Agent | 首题探索后执行；不应人为禁止后续缓存 |
| 共享批Agent/TOFFEE式前缀复用 | 复用schema探索，后续仍需生成/执行查询；不是直接复用最终答案 |

本例不证明静态质量不足，反而具体说明：发现数据结构的成本与执行已知聚合的成本应分开。不能将demo的240行当作240个独立标注decision，或把30K轨迹当作同一E/q的30K真实cases。

完整语料字段与任务分布已在下节核验；上游环境可重建性、独立gold与20例依据闭合仍未验证。

来源：[论文](https://www.vldb.org/pvldb/vol19/p4738-cong.pdf)、[固定版本源码](https://github.com/wang0702/TOFFEE/tree/83d202ff2f47729f36724adcd6093a2ae44d7052)、[官方语料页](https://huggingface.co/datasets/toffee2027/toffee-30k)。


## 完整TOFFEE-30K下载与结构扫描（后续核验）

已完整下载指定HF revision的JSON并解析全部记录。纠正初次检查中的文件大小判断：HF usedStorage=1,593,758,984是仓库存储量，不是本文件长度。实际JSON为855,734,270 bytes，SHA256 `48c331acdec8ac20777dd2092ae877cf65d1136daf9e27ef261f2f0d79358bc4`。

| 检查 | 本次实际结果 | 可支持的判断 |
|---|---|---|
| 完整记录数 | 30,000 | 发布规模成立 |
| 顶层字段 | 全部仅messages、tools；tools全部为字符串 | 没有独立顶层answer_key、证书、source revision或环境manifest；消息内证据仍需另行审计 |
| 对话角色 | user 30,000；assistant 316,931；tool_call与tool各286,931 | 是多轮训练轨迹；不能把最后assistant输出当独立gold |
| Data file头部 | 2,274种；最大IPL.sqlite与merchant_data.db各190 | 只是文件名分组，不是已冻结环境身份；不能推断同E最大N必为190 |
| 精确用户消息 | 29,988种，单消息最大重复2次 | 不能仅凭文字不同排除同任务语义，但不支持直接当作固定q批量 |
| 同文件样例 | IPL首20个query已保存 | 可检查任务异质性，不是20条gold审计 |

IPL前四条实际任务分别是：找防守获胜驱动因素；分析140–159分与突破160分的风险；生成season×venue×toss_decision特征CSV；评估默认先追分策略。输出分别为摘要、风险memo、特征CSV和风险机会评估。共享IPL数据源并没有自动形成相同任务。

第一条工作簿任务要求分析有序重复实体属性历史，最后模型输出谈到5目标行、5事件、最多2次历史及18单元格等数值；这些仅是轨迹中模型报告，本轮未取得并重放原工作簿，不作为已验证gold。第三条CSU任务要求给研究生扩张拨款建议，其最终解释还明确缺少成本、录取和劳动力市场数据。不能将建议性最终回答当作专家批准/否决标签。

证据：corpus-audit.json（全量结构/哈希）、task-audit.json（精确query统计）、ipl-query20.json（明确顺序的20条query）、first3.json（前3条公开任务及最后输出，不执行其工具或代码）。未输出或使用轨迹内私人思维文本作为研究监督。无模型执行，C的20条独立gold依据仍未完成。TOFFEE继续列为相关方法与语料线索，不计Strong；现有正式38候选分级不变。
