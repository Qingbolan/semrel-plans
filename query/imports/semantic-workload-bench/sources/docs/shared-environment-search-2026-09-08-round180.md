# 增量180：Persian RST给定EDU开发任务登记

复用179下载的原论文、完整作者仓库commit `28494a2e46baf9770ae67257019e58709b87c8f6`及87页参考指南。按现有清单相同等级，登记为第10个 `SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT`。这是来源和可构造性登记，**不是独立确认、E必要性或方法优势验证**。不把150新闻变成5789独立文档，也不把任务变体当新湖。

## 本次范围与证据

CorpusMetadata.pdf提取出150个唯一rs3文件名、150个URL，与所有150源文件名集合完全一致；未逐个重新访问原新闻页面，未证明链接仍可访问、日期/作者OCR准确或跨文章无近重复。语料的EDU文本本身已随库公开，执行输入无需从新闻站重新抓取。

固定本轮开发选择：原生单根且所有有parent边的关系名位于论文粗类别可直接对应的清单。排除4篇：

- shargh031：两个根，暂不补边。
- etemad003：含topidrift（细粒度成员），不静默折叠成粗类别。
- meidan002：含Background大小写及comparisonmult/jointmult/temporalmult，保留其原始表示但不纳入此开发范围。
- shargh035：含causemult/contrastmult/jointmult，同上。

不是说这些变体或全部4篇有错，而是当前开发范围不需要未经核验的标签/结构转换。选择已查看gold，属于开发暴露；未来确认不能把这批叫未知测试。

保留146篇，5643 EDUs、5600 groups、11097条有parent边，其中3641条结构span、7456条非span标签边。沿用179全源检查：0悬空/重复ID/循环；选择后单根。跨度交叉、近重复与所有RS3结构细节未穷尽验证，不称完整官方树评分通过。

显示映射仅把same称Same-unit、topichange称Topic Change、topicomment称Topic-Comment；预测和评分可保留原始键，不改gold。87页指南§4.1提供粗类及成员，Same-unit为中断片段结构关系。论文§3明确采用该指南的粗类别并规定波斯语适配；其核选择/优先关系偏好未完全形式化，这影响标签可重复性与E充分性，必须在实验中保留不确定结果。

任务明确给定人工EDU文本与顺序。这样不依赖尚未下载的波斯语动词配价材料去重做分句，但也不能宣称端到端原文分句能力。模型不能接触父指针、group、relation、gold对应的图例及选择时排除理由。示范、资源、验证与独立后续文档仍须另行隔离；当前只登记选择名单，未构造正式快照。

机器名单和统计：`artifact/evidence/shared-environment-audit-20260908-v180/audit.json`。原件哈希和样本在179证据目录。CC-BY-NC声明见作者README，不能把它改成无限商业许可。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 给定EDU，逐篇构建新闻RST结构与关系 | 146真实新闻、5643给定EDU | 同一87页26235词指南+论文§3适配 | 原文顺序及源文档元数据；当前图标签不公开 | 5600groups、11097边；结构span与语义边分开 |
| etemad001：第二EDU为何接到第一EDU？ | EDU1讨论分析住房市场需考察整体经济；EDU2说明住房受宏观经济影响，实际使用原波斯语 | Explanation与其他粗关系边界、核/卫星约定 | 完整新闻上下文 | 原生EDU2→EDU1/explanation，EDU1→group54/span |
| 形成每篇解释论述清单 | 预测RST关系表 | 固定选取explanation并保留依附方向 | 文档ID与源EDU | 来自同一人工图的派生清单；不是新的独立标注任务 |

| 类python的DAG | 具体数值 / 输出 | 边界 |
| --- | --- | --- |
| `scan(given_edus).groupby(doc).sem_map(rst_structure,E)` | 146篇→结构化图；5643给定EDUs | 输入已知分句边界，不声称分句质量 |
| `graphs.project(attachment,nuclearity,relation)` | 11097边，3641span与7456非span边 | 这些是原生边数，不直接等于二叉树parseval单位 |
| `relations.filter(explanation).project(doc,nucleus,satellite)` | 具体例保留2→1解释关系 | 全量语义投影/评分及模型输出未执行 |

以下为未执行的方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确目标为该例explanation及依附；实际预测未知 | 同模型完整输入sem_map，允许固定章节检索/图工具 | 相同目标，无预设优势 | ==检索Explanation定义及核/卫星规则，保存证据==→输出图 | `DocumentContext → RelationLabeler → AttachmentResolver → Graph` |
| 解释清单包含该例 | 固定图投影与类别过滤 | 同样清单 | ==开发时核对源关系键和输出单位==→固定聚合 | 解析/过滤代码不冒充轨迹学习成果 |
| 短定义/E-only编译可能已够用 | 从同一E生成规则和固定程序，计构造成本 | 单轨迹提取应与之同资源比较 | ==一次真实执行中记录使用的规则、工具和公开输出==→提取→冻结→独立批次 | 可缓存索引、结构约束；尚未合成或运行operator |

## 未完成项

来源已闭环不等于科学充分：需要原论文图例/近重复暴露审计、完整图投影和独立评分、同资源强基线、E/短定义消融及独立确认。二阶任务如自动摘要没有独立摘要gold，不能把RST核直接当人工摘要答案。没有扩大本文结论来补足15个目标。

上一轮和本轮均为有效进展。无下载、安装、LLM/模型prompt实验/训练/种子/token预算/推理并发缓存、正式快照或commit；0测试套件测试。原标注未修改，选择和显示规则均已记录。
