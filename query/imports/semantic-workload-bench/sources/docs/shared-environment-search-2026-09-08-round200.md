# 增量200：FrameNet词典中的当前样本答案泄漏

复用198完整原论文/发布包。本轮扫描全部LU文件及frame定义，不下载或安装。可复现artifact/evidence/shared-environment-audit-20260908-v200/audit.py/json。

LU子目录共200751句子出现记录；其中27719条与全文句子经Unicode字母小写、去数字/标点归一化后匹配，涉及5193个全文句子位置。它们不是27719独立句。LU文件不仅有词义，还嵌入人工FE实例和valence统计。直接挂载完整lu/会暴露当前候选答案；应在构造侧按字段allowlist提取词义/候选frame/POS/lexeme等定义，排除header来源、sentenceCount、subCorpus句子/annotationSet、valences及annotated统计。

frame XML亦含&lt;ex&gt;例句和&lt;fex&gt;角色标记。对所有definition字段移除明确ex块再去标记后，仍有364543词的框架/角色/LU等定义文本，八词精确匹配与全文句子重叠0组。这是词典规模与表面泄漏检查，不证明全部36.5万词对每个实例必要，也不证明没有未用ex包装的标注例子；最终public资源还需实际构造与检查，不能只凭该统计宣称隔离完成。

INC：sentence.xsd明确允许INC枚举，手册§3.2.4定义了Frame element incorporation，但本次未找到码与文字含义的直接注释。实际18条INC例子包括fish.v/Hunting的Food无显式跨度。这与词义整合现象相符，仍区分“源值INC”与“本研究解释”。可以原样保留枚举，不能改作FALSE、UNKNOWN或ABSTAIN。

该例LU14767的文件header列出当前Goodwill信所在docID23791，并包含统计；这展示词典与gold并非天然独立目录。公开目标必须来自原句和指定跨度，不给gold LU ID，因为LU ID直接绑定框架，可使框架识别退化成查表。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 给定词段→框架→句子清单 | 原句及target起止；不提供gold luID/frameID | 同版frame/POS/词义定义，需allowlist构造 | 129页规则 | 28143目标键；8多框架键需后续处理 |
| 给定词段→全部角色及隐式论元 | 同句和允许上下文 | frame/FE定义去ex后集合；不挂原LU目录 | 角色跨度/多层/省略规则 | 两rank角色及DNI/INI/CNI/INC原枚举 |
| 开发实例fish.v→Food的词义整合 | 原句，后续public只保留必要字段 | Hunting与鱼类获取词义定义 | incorporation规则 | INC；不是工具失败或临床结果 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `build_public(definitions_allowlist, raw_text, target_spans)` | 原LU200751句出现，其中27719匹配5193全文位置 | 构造DAG必须隔离，非被测算法 |
| `targets.sem_map(frame,E).sem_map(roles,E).explode()` | 定义去ex后364543词 | 完整共享E候选，不等于每次必需读全文 |
| `outputs.groupby(frame,role,itype).count()` | 保留source INC以及两rank | 不能给gold luID后称frame推理 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 根据contribution上下文得Giving；实际未知 | 公开候选词典索引→固定框架消歧→角色抽取 | 同目标，实际未知 | ==查词段候选sense与frame定义== → 消歧 → 输出 | `LexicalCandidateIndex + FrameResolver` |
| fish例Food输出源枚举INC；实际未知 | 同规则固定隐式角色分类 | 同目标，实际未知 | ==查incorporation与省略类别规则== → 枚举 | `RoleMapper + NullTypeClassifier` |

==为可观察查阅。固定检索/CodingAgent/E-only编译可访问同一去实例资源；不能将更大的未经净化词典只交给Agent。无模型结果，本轮仍11/15。下一步实际public allowlist和目标去重/多解构造、保留两层角色；原生资源可用性的证据增加，但独立确认尚无。
