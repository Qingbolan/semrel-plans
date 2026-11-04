# 第120轮：VetClaims-JSON，取得39页规则协议，待核验共享树与泄漏

状态待定，累计7/15，不把同一家族旧/新发布算两个湖。

## 已取得原始材料

完整[旧作者仓库](https://github.com/LLTLab/VetClaims)锁c729b0e80550ee1ad604918c37c947cbea0fd44e，311800bytes、3ZIP成员。其README说有XMI，实际全部3次提交树均只有README或README+2017原论文PDF；本轮查证没有XMI。不能依据README声称下载了那些标注。

继续检索取得完整[作者后续JSON仓库](https://github.com/LLTLab/VetClaims-JSON)，commitccb98b19525e6cd950f7517f696804841931d2c9，2258424bytes、139成员、CRC通过，SHA256 7e2c8e6da8529e59bcc1de818dc36c2ee791a8c46d285e8462aeea8e61c6f0f9。另下载对应[2019原论文](https://ceur-ws.org/Vol-2385/paper1.pdf)，503029bytes，SHA2561144ca28c0bd71c651ae442a98eabc81551c918fb95eeccee477157aafe5c4d9。2017原论文在旧库完整获得，不当作2019实验数据版本。

六份作者独立协议PDF都在后续仓库：FindingSentence8页3783词；Citation5页2161词；LegalRule8页4150词；Evidence6页2857词；Sentence6页2585词；Reasoning6页3149词。共39页18785正则词，含共享重复段落和例子，不是去重必要tokens。Finding规范2018年7月版明确依赖Sentence、LegalRule、Citation先行判定，且事实认定需对应rule tree的条件。

## 数据实读

50份旧格式6153个已选句子：Sentence477、Finding490、Evidence2420、LegalRule938、Citation1118、Reasoning710。原文50份另有完整txt。25份新格式2665句：Sentence924、Finding188、Evidence539、LegalRule334、Citation453、Reasoning227。旧rhetRole为数组，新rhetClass为字符串；不能因读旧字段为空就称新25份无标注。两队列本轮未合并评分或认定独立。

README说明人工选择PTSD及相关精神疾病事实部分，因此这是annotation-selected输入条件；完整判决其他句子不自动变成负例。50份数据中ruleTree含truthValue等案件结果，不能整体当公开共享E；其拓扑/条文版本是否完全共享及如何移除案件值待核验。ruleCondition和nlpOutput也不可不加审计就暴露给模型。

## 三表（待定候选）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 为申诉审查提取事实认定句，区分证据陈述与裁决者结论 | 50份旧格式6153个人工筛选句，具完整判决上下文 | 六协议39页；Finding依赖Sentence/LegalRule/Citation | 候选共享规则树：目前混有案件truthValue，未建安全公开版本 | 1718378P22S2：退伍军人在申诉期间被诊断为PTSD等多种疾病→FindingSentence |
| 提取从证据到事实认定的推理句 | 同批句子及上下文 | Reasoning/Evidence/Finding协议需相互区分 | 新25份不同schema，仅作另一队列待对齐 | 旧710条Reasoning、新227条；不等于案件获赔gold |

| 类python的DAG | 具体数值 | 中间操作 | 下游gold |
| --- | --- | --- | --- |
| `sentences.sem_map(classify_role,context,E).filter(role=='FindingSentence').project(sent_id)` | 旧6153→目标490 | 按依赖顺序判断句子角色，避免把法律抽象规则当当前认定 | 当前旧队列490条原生gold；不是模型结果 |
| `sentences.sem_map(classify_role,context,E).filter(role=='ReasoningSentence').groupby(case).count()` | 旧6153→710 | 同一多类输出固定过滤聚合 | 710总量，按case列表待构造；两视图不算两个湖 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；示例正确目标FindingSentence | 同规范和干净规则树的固定语义调用→角色过滤；可固定分阶段、缓存及检索 | 未执行；目标相同，优势未知 | ==读取Finding与Evidence的边界协议== → ==核对对应规则条件及上下文归属== → 输出角色 | `SentenceRole(sentence,context,clean_rule_tree,E_version)`；共享树不能含当前案件真值；角色依赖可固定编译 |

协议已具体指出资源用途，但完整长E必要性尚未测量；不能从39页直接推导Agent优势。原论文比较手工规则脚本与机器学习，已有规则程序应作为后续对照，不将其冒充轨迹学习产物。

下一步核验规则树跨案例一致性、字段泄漏、标注句与完整原文映射，以及规范例子与候选案例重叠。许可需查每份协议声明，公开下载不等于无限再发布。未构造public/private快照、未跑模型、未做独立确认，故本轮不晋级。

产物：artifact/evidence/shared-environment-audit-20260908-v120/downloads.json、history.json、audit.json；data目录完整两仓库、两原论文、六协议及提取文本。审计命令保留本轮工具记录，尚未脚本化。无新增单元测试、无commit。


后续纠正（121轮实测）：旧50份ruleTree的900个truthValue字段全部为空；不得把字段存在写成已有案件真值泄漏。带值汇总PDF仍是另一个待审资源，新25份尚未同口径审计。详见121轮卡。


125轮计数纠正：六协议总正则词数为18685，早先18785是加总错误；其中Part I为6807、Part II为11878，前者仍含行内例子。
