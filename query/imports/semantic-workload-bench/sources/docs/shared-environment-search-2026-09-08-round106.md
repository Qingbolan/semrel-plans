# 第106轮：ECB+ 原始来源与适用性核验

结论：原论文、完整作者仓库和完整数据已下载。暂不增加合格数据湖；累计仍为7/15，均为开发构造层级，未达到科学VALIDATED。

## 原始来源及实际核验

- [原论文（出版方）](http://www.lrec-conf.org/proceedings/lrec2014/pdf/840_Paper.pdf)：Cybulska & Vossen, LREC 2014，8页、118809 bytes，SHA256 `6c0e70e527b52c50e93ee3bd4ec6a62b31076524a5e38dcb327d7077921d0818`。HTTPS拒绝连接，但原HTTP成功，未用摘要代替论文。
- [完整作者仓库](https://github.com/cltl/ecbPlus/tree/3aa071e12fd08fc0705b16bb1841e7a9c5c22420)：commit `3aa071e12fd08fc0705b16bb1841e7a9c5c22420`，完整ZIP 4827364 bytes、11成员，CRC通过。仓库内ECB+.zip完整解压1030成员，含982篇XML；未运行上游代码。
- 随仓库指南 `NWR-2014-1.pdf`：28页、7940正则词；§3共指及相邻表格所在PDF23–24页共512词（含页眉，不是精确正文长度）。PDF26–27页列出topic与两组seminal event的对应，不能作为无泄漏公共环境直接提供。
- 官方selected-sentences清单1840行，对应976篇；清单文件均存在。另6篇没有指定评估句子，不把它们当负例。
- 全XML：377367 tokens、32297 mentions；指定句子内15095 mentions，其中6821个ACTION/NEG类型提及。185条intra-document关系、10650条cross-document XML关系记录；后者不是独立事件数。
- 指定句子中的显式跨文档动作关系涉及923个(topic, instance_id)键。该数不含仅文内事件/未链接单例，不是最终事件总数。token anchor及关系引用错误为0。
- 完整语料上的选择清单检查通过；未构造隔离public/private快照，未做训练污染、指南例句去重或全量共指闭包评分。

## 具体数据及固定任务：仅供适用性诊断，不列为合格推荐

以下明确采用annotation-given mention任务：给定提及边界，预测共指。提及边界是上游人工输入，不能宣称端到端新闻事件抽取结果。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 按ECB+定义判断新闻中的事件提及是否指同一事件，然后统计事件簇 | 官方指定句子的新闻上下文；976篇中1840句 | 给定提及边界：6821个动作提及；上下文允许使用对应完整新闻 | 作者事件/共指指南；移除topic答案附录；仅共指时§3约2页 | XML原生共指关系；需补全合法单例/文内簇契约，跨topic未标注不能随意当FALSE |
| 具体正例：两处“case”是否同一案件 | `1_5ecbplus.xml` m71：上下文涉及Lohan驾车轻罪案与法官要求的治疗 | `1_8ecbplus.xml` m46：上下文涉及Lohan重新聘请律师Shawn Holley处理案件 | §3要求判断同一事件实例；不能只匹配词面“case” | 两者原生同属topic1的`ACT15731894703034277`；该簇还含另两篇指定句子中的case |

| 类python的DAG | 输入具体数值 | 中间输出 | 下游gold及限制 |
| --- | --- | --- | --- |
| `docs → select_official_sentences → given_mentions → candidate_pairs → sem_map(same_event, E, contexts) → constrained_cluster → count` | 982篇原始；976篇有指定句；6821动作提及 | 正例pair目标为True；证据不足允许ABSTAIN，不能当False | 示例4个case提及为同簇，诊断子集count=1；不是整个topic仅1事件。全量簇数尚未构造 |
| `docs → sem_map(event_component_type, E) → groupby(type) → count` | 原始32297提及分30标签；指定句15095提及 | 类型与共指可形成同湖第二任务 | 需先明确给定边界/端到端范围及被完整标注句子的实体覆盖；本轮不报该任务可行性通过 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 示例pair正确目标为True；实际预测未知 | 固定模板提供相同指南/上下文，对pair调用sem_map；可固定检索、缓存共享规则、批内复用实体归一化 | 相同正确目标True；无实测支持其更准确 | ==读取任务定义、选择句清单和指南共指范围== → ==定位两份新闻中的人物、案件及时间线证据== → 返回decision与证据位置 | `SameEvent(context_a, context_b, mention_a, mention_b; frozen_rules)`；类型检查→人物/时间/地点兼容性→事件身份判断→True/False/ABSTAIN；不得固化case或Lohan答案 |

上述为研究者拟议流程，不是LOTUS实测、Agent真实轨迹或已提取算子。为公平比较，固定程序、仅E生成程序的Coding Agent及整批Data Agent均可访问相同资源并共享缓存；需另设无轨迹编译对照。

## 为什么本轮不计入

1. 对给定提及的共指任务，相关核心规则只有短章节；文档总页数不能证明长E必要。若扩大到类型抽取+共指，仍需用具体错误和资源消融说明整份指南的贡献。
2. 指南附录直接透露主题核心事件，必须隔离；主题/子主题目录也不能不加说明地作为模型输入。其划分含人工构造信息。
3. 只有指定句子有可靠共指评估覆盖，尚未冻结全量公共输入及独立评分契约。原始关系记录不能直接当完整pair分类gold。
4. 原论文已讨论同人物不同事件与词汇多样性问题，但这不证明从一次轨迹提取优于从规则直接生成程序。

## 本地产物

原论文/完整仓库/语料：`data/shared-environment-audit-20260908-v106/`。
下载收据、bundled-assets哈希、可重跑audit.py及audit.json：`artifact/evidence/shared-environment-audit-20260908-v106/`。
数据许可文件为仓库CC BY 3.0相关声明；新闻原文权利与作者标注许可不能自动等同，外发前仍需核验。
