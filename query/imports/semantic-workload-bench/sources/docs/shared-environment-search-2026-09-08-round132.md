# 第132轮：NarrativeTime完整来源取得，暂不计数

从临床时间关系检索转到公开新闻时间线。THYME官方仓库说明原始病历需Mayo/hNLP数据使用协议，未下载受限病历，不计候选。NarrativeTime原文公开且有长规范，启动原生核验，累计仍8/15。

已下载[原论文](https://aclanthology.org/2024.lrec-main.1054.pdf)，21页1122025bytes，SHA256198ff53ee0eeb0b4781bcd8a2326f2926ef372b2f5953a1457d85371689bb5bd。完整[作者仓库](https://github.com/text-machine-lab/nt)commit742735e5434ef46f2bb88ebb9126bab96af34647，6764168bytes125ZIP成员全解包，CRC通过，SHA2566cc0f5e3bd9256f21ad70f8b4f341826db77f427af30997f984c56258d04526c。包内NarrativeTime_Guidelines.pdf33页11596regexwords，已提取文本。仓库LICENCE需结合上游新闻内容权利进一步核验，不能把代码MIT自动扩张到新闻全文。

原生nt_format：tbd_a1和a2各36篇，同一批文档，两名标注员不是72个独立文档。各含1715events、289timex、105event_coreference条目、117invisible_events条目。event_order分别1386与1377条目；当前只按JSON字典长度计数，不称1386独立专家决策。tbd_clear保留基础event/timex/coreference但event_order为空，是上游给定层而非第三份gold。

论文表格报告102313TLINKS；这些来自时间线转换，不等于102313个分别手工标注且独立的case。需验证转换算法、双标注分歧、token跨度及评分语义。36篇文档的聚类规模限制要与1715事件单位区分，不能用笛卡尔积虚增N。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 根据新闻全文和NarrativeTime规范恢复事件时间线 | 36篇新闻全文 | 给定1715事件、289时间表达，明确为上游输入 | 33页共享规范；两份人工event_order分别1386/1377条目，未冻结统一gold |
| 从时间线生成事件先后关系清单 | 同一新闻/基础事件 | 共享时间线规范与作者转换代码 | 论文报告102313派生TLINKS；本轮未实算，不能写为已核验输出 |

| 类python的DAG | 具体数值 | 中间/下游输出 |
| --- | --- | --- |
| `documents.sem_map(annotate_timeline,events,timex,E)` | 36源文档，1715给定events | 两位标注员时间线，不能直接按ID数值比较时间标签 |
| `.sem_map_or_fixed(convert_timeline).explode(tlinks)` | 派生数量尚未从作者代码重算 | 时间关系闭包/转换需单独验证；不是额外人工gold |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；ABC19980108.1830.0711需组织亚洲金融/香港地产事件时间线；不能承诺与某位标注员时间编号相同 | 同全文、基础事件与规范→结构化时间线→固定关系转换 | 未执行，同一目标，无优势证据 | ==查持续事件/分支时间与粒度规则==→==按文档定位锚点==→输出时间线→校验 | `Timeline(text,events,timex,E_version)`+固定转换；不可把人工event_order或invisible_events作为无条件公开输入 |

具体原生例：ABC19980108.1830.0711的a1 event_order0为span[0,19],type0,time6；a2 event_order0为span[0,2],type0,time10。标签编号与片段划分不同，不立即解释成语义冲突；需按规范与转换解释。native-audit.json保留两份结构。尚未完成跨度、原文分词、gold一致性或示例泄漏核验，暂不合格。

产物：data/shared-environment-audit-20260908-v132完整源与PDF/text；artifact/evidence/shared-environment-audit-20260908-v132/commit.json、downloads.json、native-audit.json。无模型、公开快照、测试套件、评分或commit。下一步核验原生跨度/事件顺序与转换派生标签，再决定是否继续构造。
