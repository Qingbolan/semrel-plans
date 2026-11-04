# 增量211：实际取得PARSEME-FR依据gold

仍12/15，新增实质证据但未新增资格。下载[官方Sequoia9.2完整发布包](https://deep-sequoia.inria.fr/download/sequoia-9.2.tgz)，4561684bytes、11归档成员，安全解包成功；[PARSEME-FR原论文](https://jlm.ipipan.waw.pl/index.php/JLM/article/download/265/249/2149)65页550793bytes；完整[FrSemCor作者仓库](https://github.com/FrSemCor/FrSemCor)commit `23f3f1c383302525647a9fab5c0d9ff70567e1d0`，含原论文/标注指南。210完整法语Wiki仍为规范来源。原件data/shared-environment-audit-20260908-v211，hash和审计见[211证据](../artifact/evidence/shared-environment-audit-20260908-v211/)。

JLM首次curl HTTP2收到非法upgrade头并超时；使用HTTP1.1正常TLS重取成功。INRIA GitLab网页返回访问限制，没有绕过；官方公开下载入口正常取得完整包。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| Q1识别非动词表达 | 3099真实源句、70567整数word | 法语项目Wiki与论文操作标准，相关规范长度待核 | 词形及明确允许的输入字段 | 2470非动词表达；本轮原始12列含gold，尚未构造公开allowlist |
| Q2给定表达→判定依据 | 同2470源表达词集合；边界明确给定 | CRAN/LEX/IRREG等适用测试 | 原句语境 | 全2470有CRITERIA，12种；一个充分依据，不是所有成立依据的穷尽标注 |
| Q3实体识别及语境类别 | 同源句 | 同Wiki NE指南 | 语境与prim/final类型定义 | 另有NE标签，尚未审完整实体映射/评分 |
| Q4给定名词→语义类别 | 同源另有FRSEMCOR:NOUN列 | 完整作者仓库内名词语义指南 | 单词/多词语义单位 | 该列已取得，但本轮未核数量和实例对齐，不报已可评测 |

| 类python的DAG | 具体数值 | 状态 |
|---|---|---|
| `sentences.sem_map(extract_nonverbal,E).explode()` | 3099句→2470源表达 | 原生字段审计完成；LLM未执行 |
| `given_expressions.sem_map(resolve_basis,E)` | LEX1544、IRREG361、DET210、CRAN155、INSERT74、ZERO46、SYNT33、MORPHO32、PRED8、ID4、CL2、seV1 | 各依据是记录值，其他依据也可能成立；评分契约待定义 |
| `expressions.groupby(basis).count()` | 共2470 | 只能评价标注依据分布，不能冒充全部真实依据分布 |

实际源例annodis.er_00003：[1,2,3]“à peu près”→`ADV|MWE|IRREG`；annodis.er_00005：[5,6]“hauts fourneaux”→`_|MWE|INSERT`，同句[26,27]“lettres patentes”→`_|MWE|LEX`。这些是本次读取的gold，不是模型输出。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| à peu près→IRREG为记录目标，未实测 | 固定检索IRREG定义→给定边界语义映射→依据字段校验 | 同目标，未实测 | ==查不规则结构标准及表达的词性处理==→输出依据 | `CriteriaIndex + BasisResolver + OutputValidator`，设计未提取 |
| hauts fourneaux→INSERT为记录目标，其他依据是否也成立未知 | 同资源固定测试顺序→输出一个依据 | 同一评分边界 | ==查插入测试及适用限制==→应用→输出 | 候选测试与充分条件解析；不可用当前gold指定优先顺序 |

原生审计：句ID无重复，12列结构完整，表达标签恰有声明，未见缺失类别声明；2470非动词表达全部带依据。许可README为LGPL-LR。名词语义单独仓库实际只有6列，完整12列来自官方发布包，不能混淆。

65页论文报告的数量与当前9.2字段统计尚未逐类对齐，不能直接把论文表格当当前结果。单word表达如aujourd’hui也存在；本轮不自动判错或删改。Sequoia与此前PARSEME法语数据重叠，扩展层不算新的独立湖。下一步核相关规范长度、依据的非穷尽评分语义、版本计数与实例暴露，再决定是否可作为同湖多任务路线。
