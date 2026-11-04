# 第113轮：STAC开发数据构造

结论：1025段/41局开发数据包已构造，11131条关系和1302个复合语段原生一致，1031资产独立工程检查通过；尚未计入合格湖，仍7/15。

原论文、完整作者发布包、46页指南沿用111轮，原生Glozz/JSON对账沿用112轮。选择公开JSON中所有语段、关系与CDU都能与纯语言原生Glozz对应且能映射到唯一游戏的完整对话；排除112段，不修补gold。CDU递归成员图检查未发现环。

指南+原论文文本层进行小写正则词12-gram、至少65字符匹配，本轮零命中。不能据此宣称指南图像例句不存在；OCR/视觉审计未完成，因此没有排除任何游戏。选择使用gold结构一致性，明确为开发暴露，不是独立确认划分。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量恢复多人对话回应结构，列出澄清问题和指向对象 | 1025段、11420EDU；41局源组 | 作者46页共同规范 | 完整语段文本、speaker、turn_no；人工分段作为给定上游 | 11131有向边、1302CDU；addressee不公开 |
| pilot01中问题“是否进了正确游戏”与Yes的回应关系 | Tomm的问题语段 | Markus的Yes及完整上下文 | 规范中的问答、确认和澄清区别 | Question_answer_pair；不靠人工addressee判定 |

| 类python的DAG | 具体输入数值 | 中间结构 | 下游gold |
| --- | --- | --- | --- |
| `dialogues.sem_map(discourse_graph,E).explode(edges).filter(type=='Clarification_question').project(source,target)` | 1025段、11420EDU | 原生方向关系及CDU成员图 | 保留集423条澄清边 |
| `dialogues.sem_map(discourse_graph,E).explode(edges).filter(type=='Question_answer_pair').project(source,target)` | 同一图复用到第二任务 | source问题→target回应，可能涉及CDU | 保留集2603条问答边；不是业务满意度 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| pilot01示例目标Question_answer_pair，实际输出未知 | 固定sem_map使用相同规范/对话，允许固定检索和共享缓存，随后图验证/过滤 | 相同目标，无优势结论 | ==查找规范中问答与确认的判定条件== → ==结合speaker和上下文定位回应== → 输出边 | `DiscourseGraph(edus,speakers,E_version)`：形成CDU/候选回应→关系分类→图检查；生成CDU须按结构匹配，不按人工ID |

以上仅预期；没有运行LOTUS/Agent、真实示范或提取。固定程序、Coding Agent、E-only编译均应有相同资源、缓存及预算。

## 文件与验证

`data/shared-environment-audit-20260908-v113/inspection-v1/public`只含EDU的id/text/speaker/turn_no、指南、任务契约。private保存完整gold、源对话/游戏映射、ID转换及排除理由。ID改名是双射，未改正文或边标签。

`artifact/evidence/shared-environment-audit-20260908-v113/build.py`构造；独立`verify.py`检查资产清单/哈希、公开allowlist、ID双射、全部正文/speaker/turn、全部边方向/类型及CDU成员与源一致。1031资产/1025记录/11131关系全部通过。

边界：不是core.Snapshot运行验收，不是OS隔离；没有CDU结构匹配评分器，不能按生成的c0/c1名字评分。没有指南图像例句隔离证明、独立确认或环境增益。下一步先审计完整指南例句，再决定能否冻结实验，不用目录和哈希通过代替科学资格。无新单元测试、无commit。
