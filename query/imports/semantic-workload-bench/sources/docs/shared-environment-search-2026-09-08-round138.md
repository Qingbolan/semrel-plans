# 第138轮：FiNER相同输入不同gold与跨划分重复

仍8/15。复用136–137已下载原论文、完整代码/数据、官方2020分类包。本轮不修改标签或划分。

按原生token数组序列化后SHA256分组全量扫描1121256行：756301种不同token数组，364955条后出现的重复记录，其中53957条与此前不同split有相同输入；2886条后出现记录与同输入既有记录标签不同，合计1696个冲突文本组。该计数按train→validation→test扫描，重复条数不是所有成对组合数。未开展近重复或公司/报告实体划分审计。hash分组用于候选检测；展示样例已直接读取两份token列表核对。

具体输入冲突：train1825与4984文字相同，贷款期限“12 years”中的12前者B-DebtInstrumentTerm，后者O。train1867与4989同为“The Term Facility bears interest at EURIBOR plus 0.35 % .”，0.35前者B-DebtInstrumentBasisSpreadOnVariableRate1，后者O。当前公开tokens+统一E不足以确定这些记录分别需要哪份gold；原因可能是源漏标或缺上下文，不能武断归于taxonomy版本。

原论文§9.4/Figure5也讨论漏标：同句租期数字存在有标和漏标，另有续期数字未标。论文是作者的错误分析，不是本轮人工重新审核全部gold。不能将O直接作为“会计规则规定不应标注”的可靠负例；也不能用这类冲突宣称LOTUS推理失败。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / gold |
| --- | --- | --- | --- |
| 按会计概念提取贷款期限 | 相同句子“... maturity of no longer than 12 years” | 官方139概念定义 | train1825的12为DebtInstrumentTerm，4984的12为O；当前输入不能区分 |
| 提取浮息基差 | 相同句子“... EURIBOR plus 0.35 %” | 同一概念目录 | train1867的0.35为DebtInstrumentBasisSpreadOnVariableRate1，4989为O |

| 类python的DAG | 具体数值 | 可评分边界 |
| --- | --- | --- |
| `sentences.sem_map(tag,E).explode(mentions)` | 1121256行，1696同输入冲突组 | 原始gold不能无条件作为唯一正确目标 |
| `.filter(concept=='DebtInstrumentTerm').project(id,span)` | 展示两行同token异label | 需源报告回溯或明确重新标注协议；本轮不自行补标 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；一致输入原则上应给一致语义预测，不能同时承诺两份冲突gold全对 | 同句+定义→固定标签→span校验 | 未执行，同样受输入/标签冲突限制 | ==查期限或基差定义==→核对句内证据→输出；不能靠探索未提供报告解决 | `XbrlTagger(tokens,E)`不能以record_id记答案或把gold补例外；研究方法前先闭合数据契约 |

新增artifact/evidence/shared-environment-audit-20260908-v138/audit.py、audit.json；只读源，临时索引在data同名目录duplicates.sqlite。脚本拒绝已有数据库，复跑需新路径。无模型/快照/正式评分/测试套件/commit。

决定：FiNER暂保留为不满足严格要求的近似任务。虽然有大批量与官方定义，统一版本/报告上下文缺失、同输入冲突、有效定义仅3388词均尚不足支持目标。停止本路线当前构造，转向新独立来源，不继续用格式检查代替环境有效性。
