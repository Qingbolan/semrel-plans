# 第111轮：STAC完整作者发布包与46页规范

状态：SOURCE_ACQUIRED_AND_AUDITED，尚未计入合格湖，仍7/15。

## 原始来源下载

- [原论文](https://aclanthology.org/L16-1432.pdf)：Asher et al.2016，547765 bytes，SHA25642e229acb95baf4503593e374b502b0afd07f252a440ee9295e9f00e73521f3a。
- [作者完整指南](https://www.irit.fr/STAC/stac-annotation-manual.pdf)：46页、12747正则词，5119072 bytes，SHA256cedbcbfa5501afd94bb1c7a9cc88af7055dc21eca15c0915079e878a6ff24a56。封面2012-06-12，PDF创建2015。页1–2明确游戏规则有助理解但非标注必需，不能将游戏手册页数计为必要E。
- [作者发布页](https://www.irit.fr/STAC/corpus.html)链接的完整原生Glozz发布包：linguistic2018-05-04 ZIP6287009bytes/2132成员；situated2018-05-04 ZIP13487868bytes/2390成员；完整JSON导出ZIP2228025bytes/4成员。均完整下载解压且CRC通过，哈希在release-downloads.json。采用作者完整发布档案满足来源下载，而非第三方模型repo；未取得版本控制源码仓库，不宣称Git commit。
- README声明45局游戏切成子文档，多轮人工标注并经SDRT专家修订。CC BY-NC-SA4.0。两个版本及JSON/Glozz不是独立数据湖。

## 实际核验

作者JSON纯语言版1137段对话、12588EDU、1450CDU、12271关系、16标签；游戏事件版2593段、44399EDU、7651CDU、43058关系、17标签。两版所有关系端点/CDU成员引用均存在，未发现EDU/CDU各自ID重复。未检查所有CDU环路、原生Glozz与JSON精确一致性或全部文本边界。45局是作者说明，本轮尚未完成源局映射，不能把1137对话当1137独立游戏。

纯语言版原生Question_answer_pair2914、Clarification_question456、Acknowledgement1543等。游戏事件版新增Sequence6863条，旧纯语言指南适用性待核验。公共JSON含人工addressee，必须从默认模型输入移除；CDU结构和关系本身也属于预测目标，不可作为默认公开资源。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量恢复多人对话的回应结构，列出澄清问题与其指向对象 | 1137段真实游戏聊天，12588已分段EDU | 46页共享SDRT/对话标注规范 | 说话者和顺序；给定EDU属于annotation-given分段版本，移除人工addressee/CDU/关系 | 12271有向关系与1450复合语段结构，须冻结CDU评价契约 |
| pilot01首段中Tomm询问是否进入正确游戏，Markus回答Yes | 前一EDU为问题，后一EDU为回应 | Question-answer与Acknowledgement等关系定义 | 对话前后文及speaker，不能用人工addressee帮助匹配 | Question_answer_pair(source问题,target回应)；两者seg_id保存在audit.json |

| 类python的DAG | 具体数值 | 中间结构 | 下游gold |
| --- | --- | --- | --- |
| `dialogues.sem_map(discourse_graph,E).explode(relations).filter(type=='Clarification_question').project(source,target)` | 1137段对话→12271原生边 | 带CDU成员的有向关系图 | 原始456条澄清关系；未隔离指南例句，不作为确认集指标 |
| `dialogues.sem_map(discourse_graph,E).explode(relations).filter(type=='Question_answer_pair').project(source,target)` | 同一图复用于问答回应检索 | 示例问题→Yes的边 | 原始2914条该标签；语义由规范定义，不等于任何现实问答满意度 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 示例目标Question_answer_pair，实际预测未知 | 同E固定sem_map→图引用校验→边类型过滤；可固定章节检索并缓存共享规则 | 同目标，未假定更准 | ==定位问答、确认和澄清的区别== → ==检查对话顺序及回应内容== → 输出原生方向的边与证据位置 | `DiscourseGraph(edus,speakers,E_version)`：候选回应/复合语段→类型判定→图校验→ABSTAIN；禁止读取人工addressee与gold结构 |

以上仅拟议流程，无模型运行/单轨迹提取。固定程序、Coding Agent及E-only编译应获得相同资源和缓存权限。

## 未完成项

1. Glozz与JSON同源精确映射；完整游戏级分组及指南示例排除。
2. 46页规则的适用版本和必要范围；situated Sequence等标签的额外规范不能臆造。
3. CDU/语段分段条件、原生图评分和下游边列表契约；不能把源标签当业务满意度或交易成败。
4. 真正默认公开输入包及独立评分尚未构造；所有原始人工字段仍仅供构造侧检查。

本地原论文/完整发布档案：data/shared-environment-audit-20260908-v111/。下载收据和可重跑audit.py/audit.json：artifact/evidence/shared-environment-audit-20260908-v111/。未运行上游代码，无新增单元测试，无commit。
