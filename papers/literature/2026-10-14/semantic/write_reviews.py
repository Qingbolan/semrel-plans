from pathlib import Path
import json,hashlib
R=Path(__file__).parent
reviews={
'lotus':{
'folder':'Semantic Operators and Their Optimization- Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS-PVLDB-2025',
'title':'Semantic Operators and Their Optimization: Enabling LLM-Based Data Processing with Accuracy Guarantees in LOTUS','url':'https://www.vldb.org/pvldb/vol18/p4171-patel.pdf','year':2025,'venue':'PVLDB','loc':'§1–8，pp.4171–4182；表1–7、图1–7；另核对参考文献。关键实验页4179已渲染检查。',
'出发点分析.md':'''# 出发点分析

研究者需要从论文表筛选、排序、关联数据集并汇总；医生需要把长病例匹配到大量不良反应标签。逐行 LLM UDF 可以执行局部判断，却没有表达跨行排序、分组、关联的高层接口，也缺少优化后的质量契约。本文把这些 bulk semantic processing 操作提升为可组合算子（§1–2，pp.4171–4174）。

具体驱动不是“增加一个通用 agent”，而是把应用的自然语言判断与模型调用方式分离。例如同一个 semantic join 可以逐对调用 LLM，也可以先用低成本代理排除大量候选，再交给强模型。

关键判断：所谓 accuracy guarantee 的参照是指定的高质量 reference algorithm，不是人工真实标签；引用保证时必须保留参照对象和失败概率。''',
'解决的问题分析.md':'''# 解决的问题分析

§2 为 filter、join、top-k、group-by、map、aggregation 定义输入输出以及 reference algorithm。filter 对每行独立判定，join 对笛卡尔积逐对判定，top-k 使用成对比较和 quick-select，aggregation 分层归约，group-by 先发现标签再逐行归类（表1，pp.4173–4174）。

§3 的 filter 使用小模型的 True/False log-probability 作代理，采样学习正负阈值，中间区间调用 oracle；分别控制 precision、recall 的失败概率。join 在 embedding similarity 和先投影再求 similarity 两种代理计划间选低成本方案。group-by 对标签分配做代理级联；top-k 用 embedding 指导 pivot，保持同一比较过程的质量。

§7 明确当前保证只覆盖单个算子，端到端误差分配尚属未来工作。不能据此声称一个多算子 DAG 已有全局正确性保证。''',
'Novelty分析.md':'''# Novelty分析

贡献集中在三个层次：以 reference algorithm 界定自然语言算子行为；以统计采样定义近似优化允许的误差；为 join、filter、group-by、top-k 设计可由系统选择的具体实现（§2–3）。相对仅把 LLM 包进 UDF，接口携带了可用于优化的操作语义。

方法边界：代理与任务相关性决定节省幅度；reference 本身可犯错；natural-language aggregation 的结合性与交换性不是任意提示都满足，论文允许自定义 partitioner（p.4174脚注）。本文不研究 map/aggregation 的全面优化。

证据审查：§3.1写默认采样 max(1%数据量,100)，§5方法设置写0.01%且至少100；复现时必须按具体实验和实现确认，不能填一个统一数值。BioDEX 的“1000倍”比较对象是不可实际完整运行的参考算法估计成本，不能写成相对所有系统都实测加速1000倍。''',
'usecase分析.md':'''# 具体用例

| 用例 | 查询输入 | 需要的数据环境 | 输出 |
|---|---|---|---|
| FEVER事实核验 | claim文本列 | Wikipedia语料及ColBERT索引 | supported/not-supported标签 |
| BioDEX药物反应匹配 | 医学论文文本表 | 不良反应标签表 | 每篇论文的反应标签排名 |
| SciFact检索排序 | scientific claim | 论文语料和检索索引 | top-k相关论文 |
| HellaSwag-bench排序 | 含实验accuracy的摘要表 | 无独立外部证据库 | 按报告accuracy排序 |
| ArXiv主题分析 | 647篇论文文本/摘要 | 无独立外部证据库 | 5个发现的主题及文档归属 |

“数据环境”在这里表示查询所需辅助语料、标签和索引，不是 GPU。Figure 1 是示例程序：检索相关摘要，过滤声称优于指定baseline的论文，再做摘要。它不是论文中某条已编号 benchmark question。

HellaSwag-bench 的200份摘要由Llama生成并注入随机accuracy值（§5.3脚注7），是论文作者构建的合成任务，不能标成真实论文摘要。''',
'workload分析.md':'''# workload分析

§5：FEVER使用development split的1000 claims；BioDEX使用250医学文章及约24000反应标签；SciFact使用300 claims，先检索100 articles再rerank；HellaSwag-bench使用200合成摘要，20次trial、temperature0.7；主题分析647篇ArXiv文章、5个主题。

默认本地推理配置是4张80GB A100、Llama-3-70B、E5 embedding、vLLM inference batch size64。OpenAI对照使用64路线程并发；它不等于每个prompt装64条记录。BioDEX的250是评测记录数；K=5/10是输出排名指标；三者须分别记录（§5，pp.4177–4181）。

本文的批处理是一个查询对整个关系或join候选执行模型操作；没有定义把多条独立用户查询合成一个批提交。图1–3给出程序示例；完整可运行query需另对官方artifact做源码级提取，不能用本分析中文复述冒充原始英文query。''',
'benchmark分析.md':'''# 基准评测

表2：FEVER优化LOTUS accuracy91.0%，batched190.0s；未优化91.2%、329.1s；FacTool80.9%、无batched实现，unbatched5396.11s。对照必须保持batched/unbatched口径。

表3：BioDEX Llama-70B设置，LOTUS join+rank RP@5=0.265、RP@10=0.280，2503s；DocETL join+rank0.262/0.282、2342s。表4 GPT-4o-mini设置，LOTUS0.289/0.296、647s；DocETL0.268/0.287、583s。不能泛化为LOTUS在该任务总是更快。DocETL只统计3次成功运行，失败重试不包括在该表均值内。

表6：SciFact LOTUS nDCG@10=0.765、36.3s，reranker0.741、2.64s；HellaSwag-bench0.919对0.461。收益主要在复杂语义排序，而普通相关性排序的更小模型有明显延迟优势。§5.5用20/50次trial检查目标与失败概率。以上是作者实验，未重新执行。'''
},
'abacus':{
'folder':'Abacus- A Cost-Based Optimizer for Semantic Operator Systems-PVLDB-2026','title':'Abacus: A Cost-Based Optimizer for Semantic Operator Systems','url':'https://arxiv.org/abs/2505.14661v3','year':2026,'venue':'PVLDB','loc':'v3，2026-02-03，PVLDB19(5):1060–1073；§1–7及表1–3、图1–8，表2所在PDF第9页已渲染检查。',
'出发点分析.md':'''# 出发点分析

用例是研究论文筛选、贡献概括和相关性分类：同一逻辑程序可以选择不同模型、集成和context缩减方式。用户可能要求最高质量，也可能要求总费用低于1美元时尽量提高质量。逐个挑选最强或最便宜模型无法保证整个程序满足目标（图1，§1）。

Abacus把这类选择视为具约束的物理计划搜索。输入不是任意开放式agent对话，而是已指定的semantic operator program、输入数据、目标，辅以可选验证数据、先验和LLM judge（§2.2）。''',
'解决的问题分析.md':'''# 解决的问题分析

§2–3包含三个相互配合的步骤。先通过实现规则为每个逻辑算子列出物理候选；再用MAB按预算采样算子与输入组合，估计质量/费用/延迟，淘汰远离Pareto frontier的候选；最后Pareto-Cascades为各group保留非支配子计划，组成满足目标的计划。

成本模型假设算子独立：计划质量是算子质量乘积，费用相加，延迟取关键路径。这个假设使有限算子测量可组合成大量计划估计，同时会忽略上游摘要质量与下游分类质量的关联（§2.3、§5）。Theorem3.1的子计划Pareto最优性也以此独立性为前提。

§3.2明确：若找不到满足约束的计划，会返回优化目标最好的计划。因此费用/质量constraint不是任何输入上都确保满足的硬执行保证。''',
'Novelty分析.md':'''# Novelty分析

相对Palimpzest早期启发式选择，Abacus把候选采样和多目标组合分开：MAB负责在有限预算里发现有价值的候选，Pareto-Cascades负责在quality/cost/latency间组合取舍。相对DocETL的质量导向逻辑拆分，主要新增能力是具显式约束的物理实现选择（§3、§6）。

实现包括model selection、Mixture-of-Agents、Reduced-Context、Critique-and-Refine，另有top-k和join规则（§4.1）。不能把可扩展框架等同于论文已实现全部可能重写。

限制直接影响应用：上游输出改变会使独立成本模型失准；采样frontier逐层推进带来优化延迟；LLM judge可替代缺失中间标签，但不等于独立ground truth。对于少量临时数据，应把优化开销与执行开销一起比较。''',
'usecase分析.md':'''# 具体用例

| 工作流 | 直接输入 | 数据环境 | 输出 |
|---|---|---|---|
| BioDEX | 药物不良反应医学报告 | 反应标签检索库 | ranked reaction labels |
| CUAD | 合同全文 | 41类条款定义；评测时有专家span labels | 各类别对应的合同span |
| MMQA | 问题表 | image/text/table三种数据集合 | 答案列表 |

BioDEX计划是map提取反应、top-k召回标签、map重排（图4）。CUAD逻辑上是一个map提取41 fields，物理上可用多个提议模型再合并。MMQA先为三种模态生成search strings，分别semantic join相关内容，再按question分组汇合回答（图5）。

评测输入与辅助标签不能混淆：gold labels用于评分，MedDRA样式候选反应标签用于检索任务；两者用途不同。图1中的研究论文检索是说明性示例，不是第四个评测数据集。''',
'workload分析.md':'''# workload分析

§4.3每个系统在10个不同test抽样上执行；每份BioDEX split250条，CUAD与MMQA各100条。MMQA为控制费用，只保留与至少一个ground-truth question相关的数据项，不能解释成对完整开放数据湖检索。

对照实验统一允许GPT-4o-mini、text-embedding-3-small、clip-ViT-B-32；系统实现可用的模型集合更大，但不要把这个集合写成所有表2实验都混用（§4.1 vs §4.3）。

采样默认k=6个物理算子、j=4个输入；sample budget=50×semantic operator数。这是优化采样批，不是整个数据输入批大小，也不是LLM一次prompt含4条。MAB frontier内部可并行，frontier之间顺序依赖（§5）。本论文不提供多独立用户查询共享执行benchmark。''',
'benchmark分析.md':'''# 基准评测

| Table2任务 | Abacus质量 | 次高质量系统 | Abacus总费用/总时间 |
|---|---|---|---|
| BioDEX RP@K | 0.261±0.026 | LOTUS0.216±0.042 | $0.89 /450s |
| CUAD F1 | 0.662±0.010 | DocETL0.475±0.106 | $0.69 /450s |
| MMQA F1 | 0.304±0.079 | LOTUS0.284±0.046 | $13.1 /1149s |

该版摘要、§4.3叙述中的相对改进数字有不一致，本记录保留表2直接测量值，不合并成一个宣传性百分比。表2费用包括优化和执行；表3的min-cost/min-time使用execution口径。

表3也显示MMQA的min-cost均值$16.0高于max-quality execution$12.9；作者归因于embedding join估计的高方差，不能声称目标最小化在每次运行都成功。图6–8比较先验、MAB与Pareto-Cascades，约束满足率低于100%，支持“改善搜索”而非硬保证。未复现实验。'''
},
'docetl':{
'folder':'DocETL- Agentic Query Rewriting and Evaluation for Complex Document Processing-PVLDB-2025','title':'DocETL: Agentic Query Rewriting and Evaluation for Complex Document Processing','url':'https://www.vldb.org/pvldb/vol18/p3035-shankar.pdf','year':2025,'venue':'PVLDB','loc':'PVLDB18(9):3035–3048；§1–7、表1–6、图1–5；实验页3043已渲染检查。',
'出发点分析.md':'''# 出发点分析

记者要从超长警务记录提取警员及不当行为，再跨记录归并身份和事件。即使使用强模型，单次map也会因为长上下文、任务复杂、实体名称变化而漏报；降低调用费用并不能解决任务不可用的问题（Example1.1，pp.3035–3036）。

DocETL因此优化的核心是“如何拆任务/拆文档使输出更完整”。例如合同中同时抽取41类条款，可改成若干独立的小抽取任务再汇总；长文档可split、gather邻近背景、map、reduce。''',
'解决的问题分析.md':'''# 解决的问题分析

数据以JSON object为document、JSON array为collection；YAML pipeline声明prompt、输入源和output schema。map/filter处理单文档，reduce按key聚合，resolve统一实体名；split与gather分别拆文档和保留周边上下文，后者不改变chunk数量（§2，表1）。

§3列出13个rewrite directives，覆盖数据拆分、投影合成和LLM特有改进，例如gleaning、实体统一、map拆成独立并行投影。它们是由agent实例化prompt与参数的指引，不是对任意LLM输出成立的严格关系代数等价规则。

§4先生成验证准则并判断当前子计划质量，只有不足时才重写；新算子立即递归优化。候选先评分，top6再成对比较，以最多wins选择。数据按文档长度加权采样，并按上游selectivity扩大后续采样，避免后续无足够样本。''',
'Novelty分析.md':'''# Novelty分析

本文将agent限制在可解释的重写方向内，同时让另一个验证角色构造任务相关的判据。主要价值是以逻辑分解改善漏提取、上下文遗漏、实体重复等具体失败，而不只是改prompt措辞（§3–4）。

方法风险是评分也来自LLM，局部“看起来更好”不必然改善全局结果；样本可能比真实长文档短，导致完整执行时仍超context。§4承认动态调整计划尚在开发；§5.5的30个生成计划里20%有关键错误，说明验证筛选是必要组成。

原版目标偏重质量，明确把成本和延迟约束列为后续工作（p.3041）。不要把后续MOAR的多目标能力倒填进2025版DocETL。''',
'usecase分析.md':'''# 具体用例

| 任务 | 输入表/字段 | 数据环境需求 | 输出 |
|---|---|---|---|
| CUAD | 每行合同文本 | 41类条款说明 | clause_type,text_span列表 |
| Steam | 每游戏聚合300条含ID和timestamp的review | 无独立外部库；评分只作gold | 10正面+10负面review并按时间排序 |
| BlackVault | 733篇解密事件文章 | 无独立外部库；地理编码用于评测核验 | 各统一事件类别的不同地点 |
| BioDEX | 250篇医学文章 | 24300反应标签表 | 每篇文章的反应标签排名 |

辅助输入必须按用途区分：Steam的用户评分在任务输入中省略而用于评价；BlackVault的Nominatim地理编码是评测工具，不是查询检索环境。警务案例来自真实合作场景，但不应把示例代码自动归为全部公开benchmark query。''',
'workload分析.md':'''# workload分析

§5评测：CUAD510份中的前50合同、41类专家标注；Steam10游戏，每份输入文档包含300评论；BlackVault733文章，平均700words；BioDEX250文章、24300labels。

批处理有不同含义。map是一条记录一次任务；长文档split按token拆分，Steam例选择104652 tokens/chunk；BlackVault reduce按41份文档fold batch推进。41是该计划归约批大小，不能复制到所有query。线程并行、输入记录数、prompt批、输出top-k须独立记录。

论文运行环境为2021 M1 Macbook Pro调用OpenAI；execution用gpt-4o-mini，optimizer通常gpt-4o-mini，BioDEX用gpt-4o。实验主要2024-09，Aryn与非LLM基线补于2025-02（p.3043）。这是复现实验配置，不是问题页“数据环境”定义。''',
'benchmark分析.md':'''# 基准评测

CUAD用类别一致且span Jaccard>0.15判命中；表2优化F1=0.477，未优化0.379，LOTUS0.393。表3对应执行$1.46/180.30s，对未优化$0.08/23.43s，另付优化$1.58；质量提高伴随费用增加。优化选21个独立map，每个处理1–3相关条款，再reduce。

Steam表4：幻觉率0.465→0.312、Kendall tau0.470→0.631，但sentiment accuracy0.664→0.650。基线截断到context，优化处理完整输入，不能把费用差异视为相同处理量。

BlackVault表5优化抽取435地点、precision1.000；“Location Recall”列实际报告数量而非[0,1]比例。正文未优化事件类别233与表格164亦不一致，保留证据口径。BioDEX表6 DocETL RP@5/10=0.281/0.313；不同论文的LOTUS版本和模型不同，跨论文数字不可直接比较。未复现实验。'''
},
'quest':{
'folder':'QUEST- Query Optimization in Unstructured Document Analysis-arXiv-2025','title':'QUEST: Query Optimization in Unstructured Document Analysis','url':'https://arxiv.org/abs/2507.06515v2','year':2025,'venue':'arXiv','loc':'arXiv2507.06515v2，2025-07-11；§1–6，表1–3、图1–8；表2–3所在PDF第11页已渲染检查。',
'出发点分析.md':'''# 出发点分析

律师要筛选满足罪名、指控数、刑期条件的案件，或分析球员与球队信息。这些属性尚未成为结构化列，昂贵操作是从每份文档抽取属性，而不只是执行SQL比较（§1–2）。

同一属性在不同文档中需要阅读的相关片段长度不同，因此“一个查询统一一个过滤顺序”可能浪费模型token。QUEST先减少单次抽取上下文，再为每篇文档决定抽取顺序，在前置条件失败后停止无用抽取。''',
'解决的问题分析.md':'''# 解决的问题分析

§4建立文档摘要和文档片段两级embedding索引，先排除主题不符文档，再取属性相关片段。采样文档提供包含属性值的证据片段，聚类中心扩展检索以缓解属性名与实际表达不匹配；缺少证据时会用LLM合成候选证据。

§3.1基于每文档抽取token成本c和采样selectivity p排序：合取按(1-p)/c，析取按p/c；混合布尔表达式递归处理。最优性是文中成本/概率模型下的结论，不能忽略相关谓词或估计误差。

§3.2先执行一侧获取join keys，把另一侧join转为IN filter，再与其他filter一起排；多表join执行一部分后更新下一步，生成left-deep计划。目标范围是SPJ，aggregation优化被§2.1列为未来工作。''',
'Novelty分析.md':'''# Novelty分析

QUEST把优化决定下沉到document instance：便宜且能提前拒绝记录的属性先抽取；join产生的候选key也参与过滤顺序。与只缩小模型或只做检索不同，它同时优化每次调用的token和需要调用的次数（§2–4）。

需要保留的条件：两级检索与证据聚类可能遗漏信息；selectivity由样本估计；论文的join支配结论依赖建模假设。多表选择只在当前left-deep扩展中做适应性决策，不是任意图的全局最优枚举。

§2.4提到跨查询缓存和并发“可支持”，同时明确多查询优化和benchmark超出本文范围。因此不能标成已验证multi-query batching系统。''',
'usecase分析.md':'''# 具体用例

Figure1的原始SQL示例是：

```sql
SELECT name, team
FROM Players
WHERE age>35 AND all-stars>12
```

该图另给出Players与Teams的join示例。这是论文插图原文，`all-stars`保留作者写法，不能在原始query栏中悄悄改成可执行标准SQL。

输入是用户选定的文档集合与属性说明：Players文档提供name、team、age、all-stars，Teams提供球队及championships等。数据环境包括这些文档构建的两级索引；join则再需要另一集合。每条属性描述不是数据记录本身。

现有本地QUEST集合若有83条查询，只能对应其源文件版本；论文表1主评测50查询，不能直接宣称83条逐一来自论文正文或覆盖论文所有实验。''',
'workload分析.md':'''# workload分析

表1/§5.1：LCR从3000案例报告取100份，平均6247tokens，10属性、10查询；WikiText抓取200网页，10领域，平均1264tokens，20属性、25查询；SWDE取200网页，平均416tokens，16属性、15查询。主评测合计500文档50查询。

§5.4另构造60条双表join查询，以及3组各10条多表join查询。不能未经源artifact比对便把这些计数简单相加当作独立全部query ID。ground truth是LLM抽取后由10名研究生核验，查询随机选属性构造过滤再人工剔除不合理项。

默认采样约5%文档，证据聚类K=3（§4、§5.5）。5%是优化/证据采样比例，非batch size；文中没有统一的模型推理batch大小。文档可以分worker并行属于架构讨论，未做多查询联合批处理实验。''',
'benchmark分析.md':'''# 基准评测

| Table2/3 | QUEST F1 | LOTUS F1 | QUEST tokens/文档 | QUEST秒/文档 |
|---|---|---|---|---|
| Wiki | 0.87 | 0.90 | 170 | 1.12 |
| SWDE | 0.95 | 0.96 | 190 | 1.21 |
| LCR | 0.72 | 0.45 | 2030 | 2.68 |

token包括sampling成本，时延是每文档均值；不要把2.68s标成整批500文档响应时间。正文§5.2有将LCR F1近似写成0.7等叙述，表2是本记录的精确数值依据。

过滤顺序比较Random、Selectivity、Average_cost、Exhaust；join比较Pushdown、Random和拥有真实selectivity的Optimal。图6显示接近穷举成本而搜索更快，图7显示join转filter有效；图8消融两级索引、证据、阈值、采样比例、聚类数。未独立重跑这些实验，也未从论文正文确认完整硬件/模型版本。'''
}
}
for key,r in reviews.items():
 p=R/'reviews'/r['folder'];p.mkdir(parents=True,exist_ok=True)
 intro=f"# {r['title']}\n\n[原论文]({r['url']})\n\n阅读日期：2026-10-14。阅读状态：本轮全文正文核读，未复现实验。核读范围：{r['loc']}\n\n"
 intro+='本分析逐项区分直接输入、辅助数据环境、优化采样和模型批处理，原始查询只在有明确原文位置时逐字引用。\n\n'
 for fn in ['出发点分析.md','解决的问题分析.md','Novelty分析.md','usecase分析.md','workload分析.md','benchmark分析.md']:
  intro+=f'- [{fn.removesuffix(".md")}]({fn})\n'
 (p/'README.md').write_text(intro)
 for fn,text in r.items():
  if fn.endswith('.md'):(p/fn).write_text(text+'\n\n来源：['+r['title']+']('+r['url']+')。\n')
(R/'review_index.json').write_text(json.dumps([{k:v for k,v in r.items() if not k.endswith('.md')}|{'key':key,'reading_status':'full_text_reviewed','review_folder':str(R/'reviews'/r['folder']),'pdf_sha256':hashlib.sha256((R/'pdfs'/f'{key}.pdf').read_bytes()).hexdigest()} for key,r in reviews.items()],ensure_ascii=False,indent=2)+'\n')
