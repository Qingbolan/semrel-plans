# 增量208：PARSEME原标注版本与开发视图

仍12/15。原论文与完整仓库已在[206](shared-environment-search-2026-09-08-round206.md)下载。新发现：法语1.2 README声明表达gold沿用1.1，并直接链接1.1规范，因此本轮补下[完整1.1规范](https://parsemefr.lis-lab.fr/parseme-st-guidelines/1.1/fulldoc.php)，788349bytes，SHA256 `42a95076b4befb78932246064bedb4550f132e3927888fb747f298e5361c7410`。此前1.2规范保留，不能单凭相邻版本假定规则一致。

本次实际构造`data/shared-environment-audit-20260908-v208/view/`，公开与私有分开，未调用模型。原件及数据不提交；[构造与独立核验脚本/收据](../artifact/evidence/shared-environment-audit-20260908-v208/)可追溯源commit `dd162057e57241a76737117b59d6210b913a95a0`。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| Q1逐句发现表达并分类 | 20708句、509781源word，公开text与word IDs | 原标注所链接的1.1规范 | 词汇化、开放槽位、结构/类别判定树；公开不提供源句法或lemma | 5639表达，2330不连续；LVC.full1872、VID2149、IRV1499、LVC.cause97、MVC22 |
| Q2给定表达→分类 | 可另建5639个给定词集合视图，本轮未物化 | 同版类别规则 | 原句语境 | 同一人工类别，不能称端到端发现或独立新湖 |
| Q3统计轻动词表达 | Q1预测表达清单 | 固定类别字段 | 确定性filter/count | LVC.full目标总数1872；不是另一份独立人工gold |

| 类python的DAG | 具体数值 | 本轮完成边界 |
|---|---|---|
| `sentences.sem_map(find_and_type,E).explode()` | 原train/dev/test来源分别14199/1559/4950句 | 公开输入与私有gold已构造；语义调用未运行 |
| `expressions.project(category,word_ids)` | 5639个源表达逐项保留，2330个离散集合 | 不把不连续集合变为连续区间 |
| `expressions.filter(category=="LVC.full").count()` | gold1872 | 评价目标，未报告模型计数 |
| `typed_exact_match(pred,gold)` | 类别受控变异恰少1个匹配 | 独立诊断通过；不是完整模型评测 |

具体例仍是源`fr-ud-train_09570`的`Tenue … réunion`，gold为[1,6],LVC.full。需要判断轻动词关系并保留分隔开的两个词，中间词不属于表达。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| [1,6],LVC.full为目标，未实测 | 固定检索轻动词/变体规则→sem_map→词集合校验 | 同目标，未实测 | ==定位名词事件性、动词语义弱化和开放槽位测试==→判断→输出 | `RuleRetriever → VMWEMapper → TypedSetValidator`，设计非已提取产物 |
| Q3总数1872为gold目标 | 同资源固定映射→类别过滤→求和 | 同目标，误差未知 | ==查询边界类别规则==→相同外层DAG→求和 | 可缓存规则、参数化分类器、确定性聚合；E-only编译允许同样结构 |

排除规则在构造前写入脚本：仅保留Unicode字母、转小写后相同的98组涉及248句，整组排除；此规则忽略数字/标点，可能把内容不同句子保守排除，不能称248句均为真正近重复。另排除5个单word未决句，总253句；原gold未更改。1.1过滤规范保留27327词，与源句八词匹配0。规范仍含其他语言专属正文，不能把这个词数全部计为法语必要环境。

MVC并非完全没有法语适用入口：规范有“any other language”分支，直接使用MVC.13；但该分支与全部语言章节的相关性仍需逐段冻结，不能借其他语言测试放大成本。单word格式允许多词token的通用规则不等于`contre-indiqué`已得到逐例规范确认。

验证：独立verify.py重读全部原生CUpt，20708条的词与类别/词集合多重集相同；公开字段allowlist、精确文件manifest/hash、保留/排除源ID全集划分通过；一个真实表达换类别在typed匹配中少一个匹配。官方整体分数忽略类别的边界见207。

这些是SOURCE构造证据，不是环境增益或独立确认。源split仅留私有溯源；尚未创建示范/独立后续划分，无模型、成本、短规则充分性或E必要性实验。暂不新增资格计数，下一步完成任务相关规范范围审计。
