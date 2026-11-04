# 增量191：MPQA版本和原始发布核验（未计入）

本轮实际下载[MPQA3.0原论文](https://aclanthology.org/N15-1146.pdf)146250bytes；另沿[研究机构发布页](https://cogcomp.seas.upenn.edu/Data/MPQA_data/)下载完整mpqadata.tar.gz，62543699bytes、10967成员、9497普通文件，并下载对应[Choi等2006原论文](https://aclanthology.org/W06-1651.pdf)158317bytes。它是研究机构托管的2006完整数据包，不是原作者Git仓库，也不是MPQA3.0数据。所有下载URL/bytes/SHA256见artifact/evidence/shared-environment-audit-20260908-v191/downloads.json；压缩包原件在data/shared-environment-audit-20260908-v191/。未运行上游代码，未解包覆盖文件。

作者主页仍链接旧MPQA入口；mpqa.cs.pitt.edu本机DNS失败，web工具502。旧包README明确指向Database.1.2.README；不能用2009年692篇的公告或2015论文70篇的规模给当前下载包命名。无完整标注manual下载成功；包内只有两份README，无PDF。尚不满足长E与对应版本绑定，不新增合格湖，仍11/15开发可构造来源。

## 实际原生核验

选择文件名恰为gateman.mpqa.lre.1.2的535篇，不累加旧gateman/sigdial等平行版本。73508标注行：agent12410、objective-speech-event11718、direct-subjective13010、expressive-subjectivity12343、inside11112、split12915；这些不是73508个独立语义decision，包含结构行和隐式零宽表达。行格式解析异常0，不代表offset/source链接语义全通过。按任意man_anns父目录计数曾得到536，原因是目录中还有辅助文本，改为标准文件筛选后535。

默认正文原件未建立；auto_anns/gate_default含token、空白及位置，可以探索重建，但尚未全量原始字节一致性验证。intermediate_representation第2/3列直接为source/opinion labels；第9及15–18列有训练相关统计，README要求随训练划分再生成。不能整表作为public输入。

具体原生例子20010620/13.40.05-15087：850:861的GATE token为complaining；对应LRE1.2标注GATE_direct-subjective，nested-source=w,patient，polarity=negative，intensity=medium。这只是一个已核的词段及标签，不能根据孤立complaining就证明长E必要，也未把整个句子/上下文重建为冻结输入。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐新闻抽取主观表达及持有者，形成可归属的意见清单 | 535篇对应GATE token/space，原始字节重建待审计 | 同版本MPQA完整规范尚缺 | 公开来源上下文；不得包含man_anns答案或派生标签特征 | 13010条direct-subjective、12410条agent；链接和隐式对象需另审 |
| 对表达输出上下文极性和强度，再汇总 | 同一新闻；可单独定义给定表达跨度任务 | 极性/强度/嵌套来源规则，版本待下载绑定 | 例complaining，850:861 | negative、medium；w,patient |

| 类python的DAG | 具体数值 | 当前边界 |
|---|---|---|
| `scan(docs).sem_map(extract_opinions,E).explode().project(source,span)` | 535份LRE1.2标注，13010主观表达 | 非73508独立记录；public正文、完整E未冻结 |
| `scan(given_expressions).sem_map(polarity_intensity,E).groupby(source).aggregate()` | 示例complaining→negative/medium | 目标是规范下属性抽取；不是医疗审批或新闻主题分类 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标为表达/来源图；实际未知 | 完整同资源上固定抽取→链接→公开schema检查；可共享检索缓存 | 同一gold目标，实际未知 | ==查规范的主观表达与客观报道区别、嵌套来源== → 抽取并链接 → 公共检查 | `OpinionExtractor(E_version, expression_rules, source_linker, validator)` |
| 例的目标negative/medium；不是模型实测 | 给同表达与完整新闻上下文，固定sem_map返回属性 | 同目标；不预设更准 | ==查上下文极性与强度尺度及例外== → 输出结构属性 | `AttributeMapper(polarity_rules, intensity_scale, uncertainty)` |

==仅指可观察查阅/工具动作，不要求私人思维链。LOTUS固定流程、Coding Agent、仅E编译与批量Agent均应获同一公开规范和工具；尚未执行任何模型，不填写准确率/速度。研究使用授权需依据完整原发布条款再绑定，不能把代码或镜像许可覆盖新闻版权。

本轮结论是来源版本和泄漏边界的求证，未满足“原作者仓库＋长规范＋原始输入”的完整下载要求。下一步应寻找可达的原始MPQA规范/发布，若不可得则转其他独立来源，不能靠派生特征填满第12个。
