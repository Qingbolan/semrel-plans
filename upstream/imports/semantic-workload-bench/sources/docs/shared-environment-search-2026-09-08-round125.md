# 第125轮：VetClaims规范的实际内容与判定依赖

累计7/15不变；本轮复用已下载作者源和原论文。124轮实际构造检查包属于进展；本轮核验环境内容，未重复做来源检查。

## 词数纠正与例子重叠

六PDF39页，按各自Part II切分：Part I共6807正则词，Part II例子共11878词，总18685。120/124等此前总数18785为加总错误，多100词，此处纠正，单文件计数没有改变。Part I仍有行内带标签例子和页眉，不能直接作为无泄漏规范。按页边界Part I跨18页，但各节切分可能同页，不把它当独立18页PDF。

新25案的12条整句匹配对应12个不同源行（其中两条引文文字相同但源数组位置不同），标签为Citation2、LegalRule10。全部是法规/通用法律规则内容；没有发现此项检查命中的新案Finding或Reasoning句。这不等于完整语义近重复审计通过，也不否定这些通用例子带有角色监督。旧案1302554具体Reasoning例仍属已确认标签示例，必须单独处理。

## 规范给出的实质依赖

Finding协议Part I明确要求结合最终service-connectedness结论、规则树条件、FINDINGS OF FACT与REASONS AND BASES的对应句进行判断，并区分裁决者结论与其转述的证据。Evidence协议解释，虽然句子由Board书写，若它只是将命题归于clinician，则是Evidence而非Finding。Reasoning协议进一步要求区分证据描述与证据证明力评价。

因此默认输入需包括未标注案件上下文和共同规则树，不能仅给一句话。124开发包已提供这两者。案件最终裁决对本角色任务是合法上下文；如果改做获赔预测，就需要完全不同的输入/泄漏契约，不能复用。

原协议的阶段依赖可固定实现：Sentence→Citation→LegalRule→Finding→Evidence→Reasoning（精确处理顺序及默认Sentence归属仍需保持原协议定义）。固定流程本身不是Agent独有能力，不能从跨句依赖推断Agent优于LOTUS或Coding Agent。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 区分事实认定、证据陈述与证据评价 | 新25案2665句及未标注完整上下文 | 39页原协议；6807词规则部分仍含行内例子 | 同队列19节点规则树 | 188 Finding、539 Evidence、227 Reasoning |
| 检索抽象法律规则及引用 | 同批完整上下文 | Citation/LegalRule阶段规则，注意主要功能而非出现引号即Citation | 12个协议匹配源行均属通用规则或引文 | LegalRule334、Citation453；原生标签统计，不是预测 |

| 类python的DAG | 具体数值 | 关键语义步骤 | 下游gold |
| --- | --- | --- | --- |
| `cases.rows.sem_map(role_with_context,E19).filter(role=='FindingSentence').project(id)` | 2665→源188 | 判断当前裁决者是否对规则条件作决定；不把医生意见当Board认定 | 原生188；不以单句弱基线失败证明环境收益 |
| `cases.rows.sem_map(role_with_context,E19).filter(role=='ReasoningSentence').count()` | 2665→源227 | 区分证据描述和证明力评价，参考同段事实认定 | 原生227；质量/成本未执行 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未运行；船舶记录证明力例正确目标Reasoning | 同E+全文固定语义调用或分阶段流程→角色过滤；共享缓存允许 | 未运行；目标相同，优势未知 | ==查Finding/Evidence/Reasoning边界== → ==核对句子归属、证明力评价与规则条件== → 输出角色 | `role_with_context(sentence,case,E19)`；可冻结阶段程序，也可有界工具流程，必须通过同资源比较 |

当前证据支持“协议实际要求上下文/规则树”，不证明必须读取全部39页，或不能用短规范编译得到同样结果。确认仍需划清协议例子与历史监督、源实体隔离，并实测完整规范相对摘要/仅任务的增益。不满足这些之前不把长度当作必要性证明，保持待定。

产物：artifact/evidence/shared-environment-audit-20260908-v125/protocol-audit.json；六协议文本及124开发包保持不变。计数命令在本轮工具记录中，无新下载、数据构造、模型调用或单元测试，无commit。
