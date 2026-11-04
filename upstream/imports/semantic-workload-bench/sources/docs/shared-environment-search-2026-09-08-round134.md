# 第134轮：NarrativeTime计数来源与EventStoryLine新源

累计8/15，两个待核验候选均未新增计数。

NarrativeTime作者eda.ipynb保存公式`sum((e**2-e)/2 for e in all_n_events)`及输出103748.0，与133轮文件计数一致；原论文Table9明确without inverses而数为102313，因此不是仅以有向/无向解释即可消除的差异。未改原标签，转换/版本差异仍待定。本轮转查新来源。

## EventStoryLine下载与原生检查

完整[作者仓库](https://github.com/tommasoc80/EventStoryLine)commit46edefee5e82e0917b823abe0a18bf8c7770f15c，38668892bytes5633ZIP成员CRC通过全部解包，SHA256bb3574fc793fceb79e281ca182adf7a52890b5869ccbf4f2f28512d4272eff58。[原论文](https://aclanthology.org/W17-2711.pdf)10页135287bytes，SHA256401771b9a6e66f2f2e4725802c4606381ab2a280c17bd0936d4f870c816e3d61。

包内新增任务规范ECBStar-AnnotationGuidelines-v09.pdf17页6294regexwords；另有上游ECB+手册NWR-2014-1.pdf28页7940词。两者不能直接拼成45页必要E，须判定固定任务是否确实需要上游规范。此前106轮ECB+不可另计新湖；EventStoryLine从其继承文档，需要源实体隔离核验。

原始XML全可解析：v0.9为258文件/258doc_names/2266PLOT_LINK；v1.0为512文件但只有258doc_names，直接累加得到4580PLOT_LINK包含重复文档，不能宣布4580独立gold；v1.5为258文件/258doc_names/2626PLOT_LINK，但混合专家和众包。README明确v1.0专家、v1.2众包、v1.5混合；evaluation_format还用共指扩展关系，不是原始人工标注。需解析v1.0重复路径/内容，不能用最高数字列任务规模。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 提取新闻事件之间的情节关系，建立事件发展图 | 258个源doc_name，v1.0路径重复待审计 | 17页情节规范，必要上游定义待核验 | 32_11ecbplus.xml中source m7“double murder”→target m1“killing”，原生FALLING_ACTION，CAUSES和CAUSED_BY均FALSE |
| 定位新闻中的climax事件 | 原生分词和事件提及 | 共享climax/情节规范 | 同例m7 climaxEvent=TRUE，m1=FALSE；其全量标注完整性尚未统计 |

| 类python的DAG | 具体数值 | 中间/下游边界 |
| --- | --- | --- |
| `docs.sem_map(plot_links,E).explode()` | 258源文档；v1.0的4580为未去重路径总数，不是冻结gold | 有方向情节边，不能把FALLING_ACTION自动解释为CAUSES |
| `events.sem_map(climax,E).filter(climax).project(event_id)` | 示例m7 TRUE/m1 FALSE；全量gold数待核验 | 第二语义任务需验证缺标语义，不能从缺字段当FALSE |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；当前示例目标FALLING_ACTION，不直接输出因果TRUE | 同规范/全文/给定事件→固定情节关系判定→字段校验 | 未执行，无优势预期 | ==查climax与rising/falling角色==→==区分情节关系与因果属性==→输出边及证据 | `StoryRelations(document,events,E_version)`与独立climax任务；需要先确认gold字段与规范，不读当前gold探索 |

产物：v134 data完整源、PDF/text；artifact/evidence/shared-environment-audit-20260908-v134/commit.json、downloads.json、audit.json。本轮仅解析计数，没有跨度/引用/规范示例/许可充分核验、无模型/public快照/评分/单元测试套件/commit。下一步解析v1.0重复文件与17页规范任务依赖，决定可否继续构造。
