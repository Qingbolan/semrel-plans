# Increment97 — WMT-MQM完整来源、批规模与人工分歧

仍7/15，新增待核验来源不计合格。下载[原论文](https://aclanthology.org/2021.tacl-1.87/)15页PDF与[完整作者仓库](https://github.com/google/wmt-mqm-human-evaluation)commit `29acd6999aaea3586378c9dcb58d8cc4820cede3`，ZIP137971396bytes64成员，完整解包CRC通过。下载URL/字节/SHA256见artifact/evidence/shared-environment-audit-20260908-v97/downloads.json。未运行作者代码，未把不同年份/语言算独立湖。

本轮全量读取2020英德/中英原生标注文件及no-postedits版本。主文件英德79020标注行、14180系统译文段、1418不同源段、130源文档、10系统、42539评审-段组合；中英124292行、19994系统译文段、2000源段、155文档、10系统、59980评审-段组合。人工译文也在系统集合中，多个系统共享原文，标注行不是独立case。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按WMT-MQM标记译文中最多5个最严重错误 | 原文与系统译文；英德14180/中英19994段 | 作者MQM类别、严重度、最多5错、Non-translation特殊规则 | 完整文档上下文；还需恢复无标注的统一译文 | 多名专业评审的错误类别、严重度和<v>跨度标记；未裁决成唯一标签 |
| 将错误集合转换为段分数并汇总系统质量 | 同译文及预测错误 | Minor1/Major5/Neutral0，Minor标点0.1，Non-translation25 | 确定性评分、评审平均规则 | 作者avg_seg_scores；本轮一个具体例子已算对，非全量评分复现 |
| 质量诊断：误译/术语/流畅性分布 | 同批输出 | 同类别体系 | 按系统/文档聚合 | 同批人工标注的派生分布，不是新的独立湖 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `translations.join(document_context).sem_map(mqm_errors,E,max_errors=5)` | 2020英德14180系统-段；中英19994 | 不要求穷尽全部错误；最多5个最严重错误是任务契约 |
| `errors.map(weight).groupby(system,segment,rater).sum().groupby(system,segment).mean()` | eTranslation.737/seg1三名评审惩罚1、5、1 | 负均值-2.333333，与发布avg_seg_scores对应行一致 |
| `segment_scores.groupby(system).mean()` | 未完成全量复算 | 文档/段权重及缺评审处理待固定；不能直接照抄论文系统排名当本次结果 |

具体例子：英德eTranslation.737，源标题说Michael Jackson用鼻子上的胶带登上报纸头版，译文片段“zu bekommen”被rater2标Style/Awkward Minor；rater4标Accuracy/Mistranslation Major；rater6标Accuracy/Mistranslation Minor。同一输入的评审观点不同，评分目标可为原生评审分布/平均分，但不是一个无争议的错误类别。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标按相同MQM协议输出错误跨度/类别/严重度；实际模型结果未知 | 原文/译文/同文上下文＋固定规则检索sem_map，再确定性评分 | 同目标，不预设更接近某名评审 | ==核对误译与风格类别边界、严重度、最多5错规则==→检查上下文→输出 | `document_context→error_candidates→severity→top5_or_nontranslation→weighted_score`；仅设计 |
| 给定本例三份人工标注时可算-2.333333；这是评分器，不是预测 | 对预测结果使用相同权重；不能把人工错误先给模型再宣称质量识别 | 同权重评分 | ==仅在共享预处理中确认评分规则==→固定聚合 | 评分无需Agent；语义关键节点是前面的错误判断 |

输入问题：仅去除<v>标签后，主文件英德2749、中英7700个系统-段有多种target文本。作者另有no-postedits文件，英德78322行14110系统-段仍191处文本差异；中英124216行19994系统-段仍423处。暂不能把所有差异叫数据错误，需区分评审编辑、空格/编码及其他原因；不能随意选第一行并将别的跨度套用过去。

长E尚未取得：[作者链接的科学使用指南](https://qt21.eu/downloads/MQM-usage-guidelines.pdf)网页抓取及本地请求均超时，失败收据已保存。更关键的是应核验该文档如何约束本次简化类别和评分，不能把泛MQM大全任意拼入E。论文/README可证实共享规则存在，但不能证明当前拿到了复杂/长的实际标注环境。

因此保留pending：完整适用规范、原文/译文统一性及跨度对应、评审分歧评分契约、上下文完整性、许可和公开构造未完成。仓库Apache2.0不自动决定全部WMT原文/译文的再发布权。无模型运行或优势/成本结论。脚本download.py/audit.py及audit.json/no-postedits.json/example.json均在artifact同v97，完整源data同v97。
