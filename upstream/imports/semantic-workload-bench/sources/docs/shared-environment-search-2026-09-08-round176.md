# 增量176：Ru-RSTreebank 原件核验

新来源暂不计合格湖，仍9/15。取得原论文、官网全量数据包、官网链接的标注指南及官网链接的完整解析器仓库。没有把俄语GUM翻译版或其他派生版本算成独立湖。

## 原件

- [2017原论文](https://dialogue-conf.org/media/3938/pisarevskayadetal.pdf)：950293 bytes，SHA256 `f8d884730d46f189d6f0078be829b0458ec0a797afbbfe74417a7bf617f7b710`。官网旧dialog-21链接404，使用检索验证的新会议域名取得。
- [官网全量包](https://api.rstreebank.ru/archive/RuRsTreebank_full.zip)：4069151 bytes，SHA256 `340774f4a06c93e10591e585f92b69bce1b6a92410ae033e2c4024080ed5974c`，689个ZIP成员全部CRC通过。web工具不能读取ZIP不代表下载失败，curl已取得完整包。
- [官网链接的指南](https://docs.google.com/document/d/1wd-sgGyIo5AQq2IPj6jWa_QmU0fUohXj48qsfVDgcBs/edit)：公开PDF导出18页、5190空白分词，623196 bytes，SHA256 `67014a52dbe4ca6d41ed6576a9d997d3e576a9d1d2277c670743e62263931dd2`。文档名包含2019及补充；尚未核对其与2022数据修订的逐条一致性。
- [官网链接的解析器仓库](https://github.com/tchewik/isanlp_rst)：完整git，commit `401e71835a0718267de9ef858fe88e137de33d13`，72 tracked文件。它是当前解析器实现，不冒称2017数据生成程序。模型权重未下载/运行，代码许可与模型/新闻版权分别看待。

原件在`data/shared-environment-audit-20260908-v176/`；全部文件bytes/hash、初审统计和样本在`artifact/evidence/shared-environment-audit-20260908-v176/{downloads.json,audit.json,example.json}`。ZIP目前直接读成员核验，未构造正式公开快照。

## 实际初审结果

官网写333篇，当前压缩包含334个RS3、335个TXT；数量差异及逐文配对尚待查明。334份RS3中331可用标准XML解析，合计42730 segments、37951 groups；3份sci.comp_27/41/30含非法XML token。另sci.ling_14的节点6指向不存在的532，记录而未修补。

汇总`relname`属性得到cause2381、cause-effect392、effect35等；**这些是属性出现次数，不是已核验的语义关系实例数**，因为部分无parent节点也带relname。不可直接把它们当gold边总量。尚未查多根/循环/跨文重复、header关系清单及新版标签迁移，不能以XML可解析声称科学有效。

官网允许自由下载研究，但未取得明确覆盖所有原文与人工标注的许可证据。官方说明2022修复了新闻和博客的结构/一致性；本轮异常来自科学分区，不能据此说2022修复声明不成立。18页5190词也不自动证明复杂长E必要性。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 状态 |
| --- | --- | --- | --- | --- |
| 对每篇俄语文本构建RST层级，输出关系与核/卫星 | 官方334份RS3及335份TXT，文本配对未完成 | 同一18页标注指南及版本规则 | 新闻、科学、博客文档；给定EDU边界须明确annotation-given | 原生segment/group/parent/relname；3XML失败、1悬空指针 |
| sci.comp_1的片段33应如何连接？ | 原文“Поскольку отказы и сбои носят случайный характер,”（因为故障和失效具有随机性；辅助释义） | cause关系定义及结构约定 | 完整文章及相邻片段；不公开gold父节点 | 节点33→group145，relname=cause；group145为span，接到146 |
| 汇总每篇因果论述清单 | 上游预测图 | cause/cause-effect/effect的范围及方向需按本规范区分 | 源文档ID | 属图gold的派生查询；当前属性计数不能当清单gold |

| 类python的DAG | 具体数值 / 输出 | 边界 |
| --- | --- | --- |
| `scan(documents).sem_map(rst_parse,E).project(graph)` | 当前331份可XML解析、42730EDUs | 不是331篇已经可执行/有效的评测数据 |
| `graphs.extract_labeled_edges().filter(causal_family).groupby(doc)` | 示例33→145/cause | 须排除无parent属性、处理核/卫星及多核关系；未实现全量投影 |
| `private_evaluate(predicted_structure, native_graph)` | 原生人工结构作为候选gold | 失败源、版本和评分单位需先冻结；无模型运行 |

以下为未执行方法预期。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确识别示例cause作用及依附范围；实际未知 | 固定sem_map读完整文章与E，也允许固定规则检索和图构建 | 相同目标，无优势假设 | ==查询cause定义、核/卫星方向和局部/整体依附规则==→输出 | `DocumentContext → RelationLabeler → AttachmentResolver → RSTGraph` |
| 输出合法关系清单；固定图算法可承担投影 | 标签及边转换后确定性聚合 | 同样流程 | ==首次核对label与edge单位==→固定执行 | 规范索引可缓存；XML整理不冒称轨迹学得语义能力 |
| E-only编译可能已足够，需同资源对照 | 只读任务+E生成共享规则/解析程序 | 单轨迹增量作用待验证 | ==记录一次真实执行的工具、证据和结构输出==→提取→冻结 | 当前是operator设计示意，未提取、未运行 |

下一轮核验文件配对、图结构和指南关系清单，再决定是否值得构造开发任务。上一轮和本轮均有实质新证据。无依赖安装/LLM/模型prompt实验/训练/种子/token预算/推理并发缓存、正式快照或commit；0测试套件测试。所有下载session已exit0。
