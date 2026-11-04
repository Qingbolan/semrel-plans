# 第53增量：GENIA Meta-Knowledge——第二个可构造开发湖

**本轮新增1个来源已核验、可构造的开发湖，累计2/10。** 任务是对既有事件库存补充五维元知识，再筛选当前研究中肯定、非推测且高强度的观察/分析事件。它是文献证据整理任务，不是临床疗效判断。环境为原始66页标注protocol；不是把研究论文当规范。

资格为 `SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT`，不是VALIDATED，也没有证明Agent胜出或轨迹提取有收益。原事件图为明确给定的上游人工注释；只评测后续meta-knowledge节点，不声称端到端事件抽取。

## 原资产与求证

| 要求 | 本轮实际证据 |
|---|---|
| 原论文 | [Enriching a biomedical event corpus with meta-knowledge annotation](https://doi.org/10.1186/1471-2105-12-393)：18页674760bytes，完整PDF下载 |
| 完整作者仓库/发布包 | [NaCTeM官方完整数据发布包](https://www.nactem.ac.uk/meta-knowledge/Meta-knowledge_GENIA_corpus.zip)：5814233bytes，2036 ZIP条目全部CRC通过并解压；含1000 XML、DTD、OWL、两份指南、许可证及README。是作者数据与schema发布库；没有找到/冒称另一个Git源代码仓库 |
| 长共享E | 包内`Meta-knowledge-Annotation_Guidelines.pdf`，66页1689657bytes，SHA256 `ec328b431e305b07401252d335530a1a2b6253fafb7abdf3cb296ec4a7f59930`。独立下载页PDF哈希不同，但pdftotext后去空白全文一致；冻结随数据发布的版本 |
| 同任务真实items | 原始1000篇MEDLINE摘要、9372句、36858事件，全量XML实际读取。items为已有事件；按摘要处理事件组，不能称36858篇独立论文 |
| 独立目标gold | 五维人工标注：KT、CL、Polarity、Manner、Source。论文记录生物学和语言学两名专家训练后标注；不是模型生成目标。原事件图与后增元知识属于不同标注层 |
| E的具体作用 | protocol规定嵌套事件的属性传播、KT对其他维度的适用限制、跨句Current/Other来源判断、强度与不确定性区别；规则决定标签含义。不是只读类别名即可定义任务 |
| 本轮构造 | 968篇/35587事件检查包，32篇与手册或原论文出现归一化精确句子重合而排除；973资产哈希通过，public事件/private gold一对一，所有角色引用闭合 |

原发布包SHA256 `0c27543e7d357b14f1f495b971bd5f8f3af58f08ce96f47cebf04bb9918d9428`。资产位于`data/shared-environment-audit-20260908-v53/`，本轮脚本/收据/统计位于`artifact/evidence/shared-environment-audit-20260908-v53/`。可检查版本为`inspection-v3/`，v1/v2失败产物保留并标记FAILED，不作执行输入。

## Query与数据湖

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 对每篇摘要的既有事件图赋五维元知识；返回当前研究中“高强度、肯定、L3”的Observation或Analysis事件清单 | E：同一66页protocol；正文约第13–48页给类别、组合/传播、上下文及标注规则，后部还含UI操作说明，不能说66页全部推理必需 | 968篇完整摘要句子，保留跨句上下文；不是单句分类输入 | 上游GENIA实体/片段/复合实体及事件图，包含事件类型、trigger、Theme/Cause等。明确annotation-given输入，所有方法同等可用 | 每个事件5字段及确定性派生的selected布尔；当前标签、人工clueKT/CL/Polarity/Manner/Source及旧assertion/uncertainty均不公开 |
| 具体已下载例：在Jurkat细胞中，经P/I刺激2小时，Fas mRNA诱导约10倍 | 强度、实验观察和来源判定规则 | 原句及整篇摘要上下文 | E19 Positive_regulation，trigger=`induced`；给定Theme/Cause | `{KT:Observation,CL:L3,Polarity:Positive,Manner:High,Source:Current}`，selected=true |
| 对照开发例：ROI来源“尚待确定，可能包括5-LOX和NADPH oxidase” | Analysis/L1与事实肯定性的区别 | PMID10022882中的原句及上下文 | E7/E8为两个不同Cause的调节事件 | 两者Analysis/L1/Positive/Neutral/Current，selected=false；“未确定来源”不等于事件被否定 |

## 类Python DAG与实际数值

| 类python的DAG | 具体数值 | 语义/状态 |
|---|---|---|
| `papers = scan(public.documents)` | 968篇；32篇示例重合文档排除 | 按公开原句与公开protocol/论文比较，不按目标标签挑样本。该排除不保证无改写示例或训练污染 |
| `events = papers.join(given_event_graph)` | 35587事件 | 既有人工事件识别为上游输入；不把此层性能计为模型能力 |
| `meta = sem_map(events, full_abstract, protocol)` | 每事件输出5字段 | 尚未运行模型。DTD缺省值明确：Observation/L3/Positive/Neutral/Current；缺字段不自动当UNANNOTATED |
| `selected = meta.filter(KT in {Observation,Analysis} and CL=='L3' and Polarity=='Positive' and Manner=='High' and Source=='Current')` | 本次私有gold派生选中1000事件 | 是按protocol定义的文献证据筛选，不是1000项经临床证实的事实 |
| `selected.groupby(document_id).collect(event_id)` | 清单与计数均可评分 | 事件计数不同于独立实验数；同一实验可产生多个嵌套事件，不能拿此计数做meta-analysis样本量 |

## 多种方法预期

下表是可检验的目标与过程，不是模型实测。`==...==`指可记录的资源查阅/检查动作。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 10倍诱导例目标为五字段及true；might例目标L1及false；未运行 | 按摘要固定批sem_map；同一protocol索引检索相关规则，读取父子事件与完整上下文，联合输出五维；固定一致性检查和缓存均允许 | 同一目标，无优势预设 | ==读取当前节点及父子事件；检查Knowledge Type；核该KT下Certainty/Manner适用规则；检查跨句来源；区分否定、低确定性和弱强度==→输出带依据的五字段 | `ProtocolIndex + EventGraphContext + KTClassifier + DimensionApplicability + ScopePropagation + SourceResolver + OutputValidator`；冻结规则版本、输入结构、预算及ABSTAIN；本轮未从轨迹生成 |
| 全批质量未知，常量默认值可能在部分维度很强 | E-only编译、固定检索和Coding Agent都可使用相同66页规范及事件图；不只拿单句弱prompt作基线 | 整篇或整批Agent允许共享环境索引与缓存，不强制每事件重新探索 | ==首次建立规则映射，后续仅按公开需要检索==，必须计入构建与复核成本 | 从真实一次轨迹提取前必须先运行同资源比较；当前只有来源/构造资格 |

## 标签与构造验证细节

原全量KT实数：Observation12824、Other11536、Analysis6584、Fact2998、Method976、Investigation1940。论文表格少数类别计数略有不同；保留发布XML的实际值，不默默用论文统计覆盖。36858总数一致。

一开始构造只导出term，漏了事件可引用的frag/cons节点，v1失败；补齐节点后引用校验又漏计已公开的sentence ID，v2失败。v3显式支持原schema中的term/frag/cons/sentence/event引用，全部闭合。没有通过删困难记录绕过引用问题。另一独立脚本核验973资产大小/哈希、完整文件集合、35587事件与gold双射及public字段allowlist。

原始XML不能给模型：当前五维属性、线索标签、comment及旧assertion/uncertainty可能泄漏答案；public采用重新构造的allowlist对象而非简单复制XML。完整protocol有公开示例，已排除精确句子重合文档；近重复和更广泛示例污染仍待审计。因此当前只列可构造开发湖，不列独立确认结果。

标注许可包含CC BY-NC-SA3.0等非商业研究要求；摘要版权另属原出版来源。未新增覆盖原材料的许可证。没有运行模型或作者工具，新工程测试0；构造/来源检查不冒充科学有效性、独立复现或成本收益。
