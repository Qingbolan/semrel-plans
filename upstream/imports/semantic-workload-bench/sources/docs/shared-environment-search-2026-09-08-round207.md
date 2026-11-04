# 增量207：PARSEME评分契约与单word边界

仍12/15，本轮未新增合格湖。延续[206原件与来源](shared-environment-search-2026-09-08-round206.md)：已下载[原论文](https://aclanthology.org/2020.mwe-1.14.pdf)、[完整作者归档](https://gitlab.com/parseme/sharedtask-data)和[同版完整规范](https://parsemefr.lis-lab.fr/parseme-st-guidelines/1.2/fulldoc.php)。本轮实际执行原生官方评分器，不是LLM实验。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 逐句发现VMWE并分类 | 法语1.2共20961句、511782整数word | 同版规范，去除明确标记为非英法语言的例子后27784词；尚含其他语言专属正文 | 5654表达、2338不连续表达，五类 |
| 给定表达词集合进行类别判断 | 5654个显式给定word集合；属于边界给定任务 | 类别区分与语言测试 | 类别gold；不能用不计类别的整体指标代替 |

| 类python的DAG | 具体数值 | 验证边界 |
|---|---|---|
| `sentences.sem_map(find_and_type,E).explode()` | train3870/dev425/test1359表达 | 预期系统流程；尚未执行 |
| `evaluate(gold,pred)` | 原gold自评分三split整体MWE F1均1 | 仅确认格式与评分器读取一致，不验证语义gold正确 |
| `mutate_one_category(IRV,VID); evaluate()` | dev整体F1仍1；IRV F1=.9957，VID F1=.9968 | 本次实际受控诊断：整体指标忽略类别，类别任务必须使用分类型或明确带类别的匹配 |

具体例仍为`fr-ud-train_09570`中`Tenue … réunion`，源词集合[1,6]，类别LVC.full；中间词不应加入表达。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| [1,6],LVC.full为目标，未实测 | 固定规则检索→语义识别与分类→离散word集合校验 | 同目标，未实测 | ==查询轻动词测试与开放槽位规则==→输出词集合和类别→校验 | 候选枚举、规则解析、词集合输出；只是设计 |
| 类别错误应计错 | 固定typed matcher与分类型指标 | 同一评分契约 | ==核对类别适用条件==→分类→相同评分 | `TypedExpressionMatcher`；不是已提取的算子 |

5个单word表达全部为`contre-indiqué`，分布train3/dev1/test1。非整数包装行上的表达标注为0，排除了漏读包装行这一解释；尚未找到其对应的明确规范规则，不自动改gold。45个相同text重复组完整保存。过滤后的规范与源句八词匹配为0，仅为词面检查，不证明无语义暴露，也不证明全部27784词对法语必要。

证据见[207目录](../artifact/evidence/shared-environment-audit-20260908-v207/)：audit.py/json、三份selfscore输出、one-category-error-score.txt和receipt。变异副本存data/...v207，不修改原gold。Python3.14使作者捆绑munkres出现转义SyntaxWarning，自评分test有同名路径提示，均exit0；不能把警告当模型失败。

无LLM、构造后续独立split、资源消融或成本测量。固定程序和E-only编译同样可以使用原规范已有决策树。下一步冻结法语适用范围、重复/单word处置及public/private视图；不以官方整体自评分1.0作为合格或质量优势证据。
