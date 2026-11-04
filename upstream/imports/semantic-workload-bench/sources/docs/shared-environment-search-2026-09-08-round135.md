# 第135轮：EventStoryLine去重及共享规范范围

仍8/15；该候选暂不合格。复用134已下载原论文与完整repo46edefee5e82e0917b823abe0a18bf8c7770f15c，不修改源标注。

v1.0的512文件由258个原数字topic目录文档与254个dev/test副本构成。全254组按XML节点标签、属性、去两端空白文本比较均相同。显式选原数字topic目录得到258篇，7129事件，2290PLOT_LINK其中2272非空（PRECONDITION1160、FALLING_ACTION1112、空18），8030TLINK其中7901非空。token_anchor和关系source/target引用全通过；这不等于事件标注完整或语义正确。

climaxEvent：TRUE294、FALSE6040、MISSING795。795缺字段不能按FALSE评分。指南climax段还标注v0.9无此层，同时描述后续人工选择及基于关系图计算的流程，v1.0层的具体完整性与独立来源仍待核验。不会把字段存在就当完整第二任务。

实际任务规范范围：给定事件后的Plot Link Annotation段1811regexwords；Identification of Climax Events到文末含references180words。17页总规范其余大量为时间表达、时间关系等上游任务规则。当前情节抽取任务没有理由要求读取全部上游28页ECB规范，不能靠拼接页数构造复杂E。端到端联合任务可能另需这些资源，但尚无必要性证据，不能临时扩展任务凑条件。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 给定新闻事件识别情节解释关系 | 258文档、7129事件 | 1811词情节规范 | 2272非空专家关系；例double murder→killing为FALLING_ACTION |
| 选择climax事件 | 同批事件与全文 | 约180词规则（包含references） | 294TRUE/6040FALSE/795缺标，不能用缺标补负例 |

| 类python的DAG | 具体数值 | gold边界 |
| --- | --- | --- |
| `docs.sem_map(plot_links,E).explode()` | 258→2272非空标注边 | 18空PLOT_LINK须解释是否未决，不自动NO_LINK |
| `events.sem_map(climax,E).filter(label==TRUE)` | 已标TRUE294，缺失795 | 未构造独立可评分完整任务 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；示例FALLING_ACTION | 给定事件+1811词规则→固定关系抽取→方向校验 | 未执行，相同目标，无优势证据 | ==查解释关系的方向及与因果属性区别==→原文核验→输出边 | `PlotRelations(text,events,rules)`；短规则直接编译对照必须保留，不能预设轨迹提取必要 |

核验脚本artifact/evidence/shared-environment-audit-20260908-v135/audit.py及audit.json；复跑同脚本。无模型/快照/scorer/测试套件/commit。共享E复杂性与climax完整gold均不足，停止本路线当前构造，转查其他独立来源；阴性结果保留。
