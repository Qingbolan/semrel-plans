# 第121轮：VetClaims共享规则树成立，但协议例子有答案重叠

状态仍待定，7/15。复用120轮下载的完整作者JSON仓库ccb98b19525e及两篇原论文，没有新下载；上一轮来源取得属于进展。本轮只审旧50份队列，不推断新25份。

## 新核验与纠正

50份ruleTree经显式allowlist保留name、children、siblingRelation、siblingCount、inferenceRelation后，结构与文字完全相同，每份18节点。所有50×18=900个truthValue实际为空。120轮关于“混有案件真值”的表述仅凭字段名不成立，已在120卡追加纠正；本轮未把另一个RuleTreeTopValues.pdf当作公开环境，也未审其具体内容。干净共享树尚未发布为public资产。

6153个标注句中6091句精确出现在内嵌全文，6134句在仅空白归一化后出现，19句仍不匹配。50份都有外部原始txt，其中37份与内嵌全文空白归一化相等，13份需进一步差异诊断；不直接修补句子或当作来源伪造。

另有3个重复sentID，均对应不同句子。1400029P133S1还对应两个不同gold标签（FindingSentence与CitationSentence）。不能用sentID字典覆盖；未来应按源文件+数组位置生成无答案public ID并保留private映射。

对6协议文本做不少于12词的整句匹配（忽略大小写和标点），发现157条标注句与协议重叠，涉及33份案件。该数量包含可能通用的法律模板，不等于157条全部已确定泄漏；不能用它证明剩余17份完全独立。

已确认一个直接答案例：案1302554句1302554P111S6讨论“即使存在抑郁，也发生在服役之后且非服役所致”；gold为ReasoningSentence。Reasoning协议原文收录同句并解释为什么它主要是证据推理而不是事实认定。协议因此同时是规则和历史带标签示例，不能作为全50份无泄漏的共享E。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 从案件中提取事实认定/证据推理，辅助申诉文书阅读 | 50案6153个已选句，内嵌完整判决 | 39页协议，含已确认的当前句子答案示例 | 50案一致的18节点共享规则树；truthValue全部为空，可考虑按allowlist去字段 | 1302554P111S6→ReasoningSentence，但它只能当开发/历史示例，不能原样进确认集 |
| 分开呈现裁决结论与引用 | 同批句子 | Finding/Citation协议 | 1400029P133S1源ID重复，分别是实体句和法条引文 | 两条不同文本标签Finding/Citation，必须保留两条 |

| 类python的DAG | 具体数值 | 中间约束 | 下游gold |
| --- | --- | --- | --- |
| `rows.sem_map(classify_role,context,E).filter(role=='FindingSentence').project(public_id)` | 6153原始行，490 Finding；不是6150唯一sentID行 | public_id不能只由sentID决定；标注句范围需说明人工预选 | 490源标签数，未来清洁子集另冻结；本轮不声称预测 |
| `rows.sem_map(classify_role,context,E).filter(role=='ReasoningSentence').count()` | 710原生Reasoning；已确认至少1句在协议中展示答案 | 历史示例和当前评测按case隔离，原样全50不得称独立 | 710仅当前源统计；没有无泄漏确认结果 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；复现协议里的Reasoning标签不证明泛化 | 同E分类→源行ID校验→固定过滤；可缓存共享树和规则 | 未执行；同样不得把读到示例答案当优势 | ==查看Finding/Reasoning边界及共享条件树== → 判断新句子功能→输出角色 | `SentenceRole(text,context,rule_tree,E_version)`；规则/历史示例访问量分别记录；目标句所在case不能作为可读带标签历史 |

下一步先诊断13份全文差异和19句不匹配、确认协议例子来源范围，再考察新25份能否形成隔离后续批次。不能通过删掉所有难例只为凑资格，也不能因为发现可修构造问题便丢弃来源。共享树证据进了一步，长协议必要性与可用独立批次仍未证实。

产物：artifact/evidence/shared-environment-audit-20260908-v121/audit.py、audit.json、duplicate-ids.json。复跑：`python3 artifact/evidence/shared-environment-audit-20260908-v121/audit.py`。无源数据改动、无public快照/模型执行、新单元测试或commit。gold暴露为开发，不是确认。
