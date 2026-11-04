# 增量209：PARSEME任务相关规范与MVC规则差异

继续[208源视图](shared-environment-search-2026-09-08-round208.md)，仍12/15。原论文、完整作者归档及1.1规范均已下载；本轮只读取原件，未下载新数据或运行LLM。原规范入口：[PARSEME1.1完整规范](https://parsemefr.lis-lab.fr/parseme-st-guidelines/1.1/fulldoc.php)。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐句识别并分类VMWE | 208视图20708句、509781词 | 候选规范子集20118词 | 结构、LVC、VID、IRV、FAQ、词汇表及MVC相关两段 | 5639表达；22MVC仍需规范一致性解释 |
| 给定表达词集合→类别 | 可从源gold明确给定边界，非端到端任务 | 同一规范 | 单句语境 | 类别人工gold；本轮只审MVC22项，不改标签 |

| 类python的DAG | 具体数值 | 证据边界 |
|---|---|---|
| `sentences.sem_map(find_and_type,E).explode()` | 20708句/5639表达 | 208已核源输入与gold；语义执行未运行 |
| `rule_index.retrieve(category_tests)` | LVC章节5455词；IRV2166；结构1046；VID1386 | 相关章节有实质内容，不代表每句必须读完 |
| `typed_expressions.filter(category=="MVC")` | 22源表达 | 是私有审计切片，不作为公开标签提示 |

本轮选择章节1—4、5总述及5.1—5.4、7.1FAQ、8词汇表，加MVC“其他语言”入口与MVC.13正文。排除VPC/IAV、其他语言专属大章、平台操作与作者贡献说明。明确非英法例子继续过滤。该选择仍有FAQ/词汇表对其他类别的提及，因此20118词是候选子集，不能称每词均为法语必要规则。完整章节清单及各段词数见[审计JSON](../artifact/evidence/shared-environment-audit-20260908-v209/audit.json)，文本在data/...v209/relevant-sections.txt；没有覆盖208冻结环境。

具体源例：`frwiki_50.1000_00039`句尾`faire valoir leurs droits à pension`，gold MVC词集合[40,41]，即faire/valoir；权利名词不在表达集合内。其他实际源例含faisant remarquer[51,52]、entendit parler[10,11]、fait savoir[18,19]。查看后的22项均为开发暴露。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| faire/valoir→[40,41],MVC为gold目标，未实测 | 固定检索MVC规范→语义分类→词集合校验；冲突处理必须预先规定 | 同一目标，未实测 | ==定位MVC分支及链接正文，发现问题表述不同==→按冻结的冲突契约处理 | `RuleIndex → CategoryResolver → TypedSetEmitter`；未生成、未学习 |
| 未解决规则冲突时可输出ABSTAIN，不能冒充FALSE | 固定流程同样可以检测规范冲突 | 同样允许ABSTAIN，不预设正确率更高 | ==记录两个原规则依据==→终止或请求契约内升级 | `RuleConflict`与`ABSTAIN`显式分开；不能用当前gold补规则 |

MVC入口使用是否保持同一事件/状态的问题；链接的MVC.13正文使用替换相关动词是否产生不合语法或异常含义的问题，二者不是同一句测试。正文还有法语正负例，但不能靠正例就证明两个判定测试等价。它也不证明22个人工标签错误；本轮只确认规范表述差异，未裁决优先级、修改gold或删除该类别。

实际执行一次audit.py，章节清单、两个MVC段落及22例完整保存。长环境存在候选证据，但环境一致性及短规则充分性仍未闭合；无E增益、模型准确率/成本或独立确认。后续应找作者修订说明或适用版本证据；找不到则保留候选而不计为最终满足条件的数据湖。
