# 第119轮：RMU:ECHR法律论证候选，未满足严格长环境证据

本轮转查独立法律来源。完整原论文作者预印本与完整作者仓库已下载，不依赖摘要判断。仍为候选排除/待补证据记录，不计入可行清单；累计7/15。

## 下载与来源

[原论文](https://arxiv.org/abs/2208.06178)、[完整作者仓库](https://github.com/trusthlt/mining-legal-arguments)。锁定commit `a1a14832ce55c85f04c9e211f3606e04401d9c0e`，ZIP114639467 bytes、2018成员、CRC通过，SHA256 `bbffa89a63a22f2aae8c9e25d5b5735d44a3b98694553d6763c6f8d6469906b2`。论文PDF及SHA/大小见downloads.json。没有下载74GB预训练模型；模型权重不是本轮数据源核验必要输入。仓库声明Apache2.0；法院原文权利与软件许可仍需分别核验。

## 原始标注核验

解析gold_data中的375个XMI，采用UIMA的UTF-16偏移读取原文，15211个LegalArgumentation span、5个actor、15个实际出现的argument type。全部span范围有效，无全文完全重复。没有把范围检查说成人工标签正确性核验。

作者create_arg_mining_dataset.py的original_data分支显式排除001-67472、001-175007，每份3个span。因此论文373份的对应口径为15205个span；本轮没有删原始文件。源码/原生标签还有映射逻辑需逐项核验，未运行作者训练或评分。

375份原生标签统计：Subsumtion8691，法院判定1238，权衡/适当性1959，先例2015；其余见audit.json。actor为法院9953、申请人2472、被诉国2401、第三方212、委员会/审判庭173。标签数不是375个案件裁判输赢gold，也不是独立案件数量增加到15211。

论文§3.1定义两套正交标签（actor与argument type）、span边界及16类论证；该节正则词数2136，附录B示例885，总3021。计数不是tokens，包含排版页眉，不能全认作必要规则。完整仓库未找到独立PDF/guide文件。论文长篇相关工作、结果、案例全文不计入共享规范。是否存在更完整作者手册仍未知，当前不能证明这个任务需要30–100页复杂E。

## 具体三表（未合格候选）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 为法律研究检索由申请人提出的法律适用论证 | 375真实ECHR判决文本；原论文口径373 | 同一§3.1 actor/argument定义和附录B示例 | 001-100469：申请人称因婚外关系被解雇并援引公约第8条，UTF16[40335,40574) | actor=Beschwerdeführer，type=Subsumtion；是既有论证分类，不是判断是否违反第8条 |
| 汇总判决中的先例引用论证及其发言者 | 同批判决 | 同一规范区分先例、distinguishing、overruling与其他类型 | 完整判决用于区分被引述者与法院自己的论证 | 原生先例类型2015、Distinguishing88、Overruling2；actor单独标注，可提供第二种分类目标 |

| 类python的DAG | 具体数值 | 关键中间结果 | 下游gold/边界 |
| --- | --- | --- | --- |
| `cases.sem_map(extract_argument_spans,E).explode().filter(actor=='Applicant' and type=='Subsumtion').project(case_id,span)` | 375→15211原生span；交集数量尚未构造 | actor与类型联合预测；两者都须正确 | 示例span满足目标；不凭类型总量声称联合查询count |
| `cases.sem_map(extract_argument_spans,E).explode().filter(type=='Prior_case_law').groupby(actor).count()` | 375输入；2015原生先例span | 同一语义输出的固定聚合 | 总量有gold；分actor投影待独立核验，不能当作模型预测 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；示例正确目标Applicant/Subsumtion | 同E固定sem_map预测span与两标签→UTF16范围校验→过滤聚合；允许共享缓存 | 未执行；目标相同，未证明更好 | ==读取actor定义及Subsumtion规则== → ==依据上下文确定论证归属== → 输出span及标签→公开校验 | `LegalArguments(text,E_version)`返回(span,actor,type)；公共边界一致，标签映射冻结 |

固定程序、Coding Agent和E-only编译也应使用相同E。本文真实用例是论证检索而非案件裁判；用户允许sem_map，但这不放宽复杂共享E要求。外部法律理论书目不是已取得环境，也不能因模型需要法律常识就宣称长E已验证。

本轮结论：数据/人工标注真实且可读取，公开规范目前仅约3021词；严格长环境依赖证据不足，暂不深入构造。下一轮优先其他来源，若后续取得完整规范再恢复。无public snapshot、示范提取、模型执行或独立确认。

产物：artifact/evidence/shared-environment-audit-20260908-v119/{downloads.json,audit.py,audit.json}；data同名目录存完整源、paper.txt和normative-excerpts.txt。命令`python3 artifact/evidence/shared-environment-audit-20260908-v119/audit.py`。无新增单元测试、无commit。
