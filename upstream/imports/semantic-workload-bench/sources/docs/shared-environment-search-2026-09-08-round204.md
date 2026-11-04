# 增量204：AnCora西班牙语语义结构新源，转换语义待核

本轮从新的独立数据湖AnCora开始核验。**尚不计入，仍12/15。** 已取得原论文PDF、官方共指/语义/名词化规范和完整UD转换仓库；官网原始3.0.1XML ZIP入口403，未取得。不把UD转换版称作原始XML发布。

原始来源：[AnCora数据入口](https://clic.ub.edu/corpus/en/ancora-descarregues)、[规范入口](https://clic.ub.edu/corpus/en/documentation)、[原论文](https://clic.ub.edu/corpus/sites/default/files/inline-files/ancora-corpus.pdf)、[完整UD仓库](https://github.com/UniversalDependencies/UD_Spanish-AnCora)。实际原件`data/shared-environment-audit-20260908-v204/`，commit `20adddbfcdd773c6dc97ba48ea11ca9364e74185`，9个tracked文件完整；[哈希收据与audit.py/json](../artifact/evidence/shared-environment-audit-20260908-v204/)。下载过程Python urllib证书链失败，系统curl正常验证TLS成功，未关闭证书检查。

| 已下载原件 | 实际大小/规模 | 对应范围 |
|---|---|---|
| 原始AnCora论文 | 417379bytes PDF | 多层语料来源 |
| AnCora-CO v2.1，2008-09 | 163792bytes，13页5106词 | 共指，不借用其他任务手册长度 |
| Argument Structure Guidelines，2011 | 411057bytes，24页11743词 | Catalan/Spanish事件类、论元位置、20类语义角色、语态交替及词典 |
| 2009语义规范 | 268120bytes，18页7488词 | 历史版本，不能与2011无说明混用 |
| AnCora-Nom，2010 | 730479bytes，31页9728词 | 去动词名词的论元结构，是否保留对应标签待核 |

完整仓库有3个CoNLL-U split：train1312篇14287句，dev155篇1654句，test168篇1721句；全1635文档/17662句ID不重复。整数token共560137，多词包装行和空节点分开计数，不能全部当普通词。ArgTem在135287行出现，拆分后135742对；全部非空角色值属于规范20类角色，非空论元槽属于arg0–4/argM/argL。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold及缺口 |
|---|---|---|---|---|
| Q1逐文档恢复给定位置的论元位置/语义角色 | 1635篇新闻源文档的CoNLL-U文本/token；是否给定句法需单列 | 2011配套语义规范24页 | 词义/LSS/语态结构需配套词典及版本核验 | ArgTem135287行，455行多对；不能给模型当前gold ArgTem |
| Q2谓词—论元关系提取→角色关系表 | 原文+谓词/候选论元任务输入需要明确 | 同一规则 | 原始XML谓词归属或有证据的转换映射，当前未取得 | 当前字段没有显式谓词ID，不能直接把UD HEAD冒充原始语义owner |
| Q3共指链与分裂先行词解析 | 同源文档可另立任务 | 13页共指规范 | CorefUD编码及转换说明 | Entity/SplitAnte存在，但完整计数/转换核验未完成；不得视为新增独立湖 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `documents.sem_map(argument_roles,E).explode()` | gold候选135287位置/135742标签对 | 只是可构造方向，未实现运行器或私有评分 |
| `roles.join(predicate_ownership).project(predicate,argument,role)` | 455个多标签位置需要恢复归属 | ownership缺失时不能臆造join；先核原XML/转换 |
| `role_edges.groupby(role).count()` | 原标签对agt24983、pat30332、tem23761等 | 并非关系边已构造通过；合并标签可能改变计数单位 |

具体源例：文档`3LB-CAST-111_C-2`首句，词段`gobernante`（统治者）对应`arg1:tem`，并非见到人名/主语就标agent；语境是该人变得沉默。源token2、UD head32只是转换版记录，不是完整原始谓词归属证明。另`3LB-CAST-d1-14-s11`的`respuesta`为`arg1:pat,arg1:pat`，不能无依据删除一份标签。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| gobernante例目标arg1:tem；实际未运行 | 固定检索事件/语态/角色规则→sem_map→合法值校验 | 相同目标；实际未运行 | ==查事件类、语态交替与theme/agent定义==→解释句中参与者→输出 | `EventClassResolver + ArgumentRoleMapper` |
| 多标签位置应保留正确多重输出；实际归属未证实 | 先由构造契约提供合法谓词/论元单位，再固定语义调用 | 相同目标，不能让Agent补造隐藏owner | ==检查公开谓词结构及相应规则==→逐关系判断→校验 | `PredicateArgumentMapper`，以前置来源映射验证为条件 |

方法过程均是待检验设计。固定程序/CodingAgent/E-only生成算子可用同资源和缓存，不假设Agent更准确或更便宜。

另有741个拆分标签对含空组成，其中722含argL空角色，与规范“轻动词词汇化补语”的定义可能相关；不能直接当成741个坏gold，其余缺项也需核源。本轮没有修复/删除这些值。UD的共指类型曾启发式统一、Cxn属于规则生成标注，不能当独立人工监督。README旧GNU描述与后续CC BY4.0记录均存在；仓库LICENSE和源发行许可需按版本核，不给所有官网资产统一授权。

当前缺口：原始XML取得、ArgTem归属/合并转换规则、2011规范与选定发布的绑定、例句泄漏及近重复、名词化标签保留情况、公开视图/评分。无LLM、官方scorer、资源增益/成本或独立确认。本轮一次完整字段审计，不宣称通过科学有效性。下一步优先查ArgTem转换源码或原始结构，决定是否可在不丢失任务意义的前提下构造。
