from pathlib import Path
import json,hashlib
R=Path(__file__).parent
items=[dict(key='palimpzest',title='A Declarative System for Optimizing AI Workloads',year=2024,venue='arXiv',url='https://arxiv.org/abs/2405.14696v2',folder='A Declarative System for Optimizing AI Workloads-arXiv-2024',loc='arXiv2405.14696v2，2024-05-29；全文§1–7，pp.1–20，附录pp.27–29程序与物理计划；表2所在p.18渲染核对。',sections=[
'''法律调查需要从邮件集合找出亲历的欺诈活动，不能把转发相关新闻算作证据；购房者同时要求价格、距离和室内采光；医疗研究者要整合不同研究的患者表。这些任务都混合常规计算、语义判断和批量数据处理。逐任务写prompt还不足以决定每个算子用哪个模型、是否可生成代码、应先过滤还是分析图像。§1–2用三个具体工作负载提出SAPP抽象，目标是让用户声明数据和操作，再由系统平衡质量、费用和时间。

技术选择由输入驱动：房源先提取价格地址并过滤，可以避免对已经不符合预算的房源调用视觉模型；不是为了建立优化器而凭空增加层级。§2提到网站1327房源只是动机，实际实验仅100房源，必须区分。''',
'''§3把程序表达为Dataset、Schema和关系算子；核心convert从输入schema补出目标schema字段，可一对一、一对多或失败丢弃。用户用字段描述和filter描述表达意图，直到Execute才触发计算。源Dataset须预注册。逻辑层重排filter/convert且依赖用户depends_on保持依赖关系，物理层选择模型、代码生成、prompt组织与输入token裁剪。

§4.3先运行GPT-4、GPT-3.5、Mixtral三个sentinel计划收集统计，再对候选计划估算成本时间和质量，保留Pareto候选并按用户policy选择。质量使用GPT-4 champion结果作代理，人工gold只用于实验。此代理不是正确性证明；表1有两个约束未达标。

§3.5缓存单位是Dataset，可重用跨程序中间结果，但带质量统计的失效机制仍是未来工作。模型级batch调度、KV缓存复用和模型蒸馏在§4.2主要是愿景，不能当已验证能力。''',
'''实质贡献是用typed convert把抽取、分类和多模态理解纳入可优化关系程序，同时把用户policy与物理实现拆开。具体的改进链条可追踪：房源文本提取→价格/距离UDF过滤→图像理解，附录PLAN2再把文本token预算降到0.5，解释了省钱来源。

优点是同一逻辑程序给出多个成本/质量折中，并真实执行选择出的计划。局限是三个工作负载各一个主程序，未覆盖复杂join/通用agent探索；234、10140、1950个候选依赖启发式剪枝；sentinel采样无严格停止条件。§3.3承认schema描述歧义，原型无法依靠用户验证样例训练，champion也可能错。9个policy仅7个满足约束，故不能写成硬质量保证。''',
'''| 工作负载 | 实际输入表/文件与列 | 数据环境需求 | gold与输出 |
|---|---|---|---|
| Legal Discovery | 1000个Enron邮件文本；File.filename、contents，convert产生sender、subject | 无独立外部数据；预注册enron-eval文件集合 | 人工50正例、30具有欺诈关键词但非欺诈例，其余随机；输出符合两条件邮件，F1 |
| Real Estate | 100房源，每行listing、text_content、image_contents列表；每房源最先3张去重图 | MIT距离条件和价格范围UDF；正文未给距离函数完整实现，不虚构地图服务 | 人工23条满足全部条件；F1 |
| Medical Schema Matching | 11电子表格文件→49表；表头/行转换为患者CaseData | 15属性目标schema是任务规范，人工harmonized table只作gold | 筛选患者年龄表并列映射，micro-F1 |

证据§5.2及图3/5/9。图3source=enron-emails与实验登记enron-eval是论文自身命名差异，记录时保留出处。图9的完整CaseData还带filename/study，不把15个医学目标属性误当所有字段数。

主执行为iterator逐记录阻塞；§5.5每convert/filter用32workers，算子间无流水，必须等整个算子完成。32是并发workers，不是32条输入合成prompt的batch size。sentinel使用5%输入，医疗1/11文件，是优化采样。论文没有给统一模型batch size或联合提交多查询合同。''',
'''最清楚的具体用例是100条房源筛选：一条输入包含房源文本和3张图片；文本先补出address/price，两个UDF排除距离和预算不合格项；剩余记录用图像生成is_modern_and_attractive、has_natural_sunlight，再过滤。输出是房源记录集合。目标schema和价格/地点约束属于查询规范，房源图像属于输入数据，不能写为“环境未配置”。

附录PLAN2说明便宜GPT-3.5处理文本、GPT-4V处理图片并裁剪50%文本。§5.3报告该候选比GPT-4基线快3.3倍、便宜2.9倍且最高1.1倍F1；这是候选计划比较。§5.4另测试优化器实际选择，二者不能互相替代。

原始query是论文Python程序而非后来生成的英文一句话。图5给完整操作链，图3的字符串含作者省略号，不能自行补全后称原文；catalog应保存原代码与另行标识的说明性重述。''',
'''模型为gpt-3.5-turbo-0125、gpt-4-0125-preview、gpt-4-vision-preview，以及Together.ai的Mixtral-8x7B-Instruct-v0.1；Modal处理非AI工作。§5.1多数实验单线程，论文未列统一本地主机配置。每负载评估20个候选/基线，优化编译耗时2.6/13.1/2.7秒；采样成本计入§5.4选择实验。

表1实际约束：医疗cost $3.16超过$2；房源F1 .79未达到>.80，其余7个policy通过。不要把policy配置值直接作为实际结果。

| 表2：32workers对单线程GPT-4 | 基线时间/费用/F1 | Palimpzest时间/费用/F1 |
|---|---|---|
| 邮件 | 16712s/$51/.97 | 185s/$5.60/.81 |
| 房源 | 1626s/$5.46/.75 | 80.9s/$1.86/.80 |
| 医疗 | 1195s/$4.96/.45 | 215s/$3.36/.46 |

90.3倍加速同时包含并发、模型、计划优化且质量下降，不能归因于单一优化器，也不是等质量公平的并行引擎对比。此处读的是2024技术报告，不把CIDR2025修订版或Abacus2026的实验混入。''']),
dict(key='sembench',title='SemBench: A Benchmark for Semantic Query Processing Engines',year=2026,venue='PVLDB',url='https://arxiv.org/abs/2511.01716v2',folder='SemBench- A Benchmark for Semantic Query Processing Engines-PVLDB-2026',loc='arXiv2511.01716v2，2026-03-16；全文§1–6、表1–5、图1，PDF pp.1–12；p.7表2–3渲染核对。',sections=[
'''单模型问答测准确率，传统TPC测关系处理开销，都不能说明一个语义查询引擎在批量图像/文本/音频上如何权衡质量、钱和时间。§1的红色汽车计数例只有图片列和语义filter再COUNT，已经可能因LLM调用成为主成本。SemBench要测系统而不是仅测模型。

作者组合带人工标签的数据为多表场景，再以标签替代语义调用产生gold，允许比较不同系统接口。目标包括能被多数引擎执行的简单任务和推动算子支持的复杂跨模态join。其价值是公开同一查询的支持情况和成本质量，不是合成一个宣称来自所有论文的统一原始工作负载。''',
'''§3把数据表达为扩展关系表：图像/音频列实际存文件路径；semantic filter、join、map、rank、classify与普通SQL混合。ground truth从原数据标签构造关系查询，不需要用另一个LLM充当裁判。

质量依据查询类型分别计算F1、聚合相对误差、Spearman和ARI；表中聚合质量用1/(1+relative_error)映射。同为Quality的列不意味着每项都是准确率。scale是主实体表行数，关联表由scale生成，系统成本应同时报query和scale。

实验固定Gemini2.5Flash并关闭推理；保留各系统默认prompt模板，所以仍测试了提示组织差异。Palimpzest关闭Abacus/model selection，这明确排除了完整优化器比较。不同系统缺算子、执行失败和超时都有实际原因，不能用0费用代表可执行。''',
'''贡献在于三维覆盖：5场景、文本图像音频、5类语义算子，并同时给成本/质量/延迟和规模。汽车场景跨四张表，商品场景既有单算子隔离测试，也有复杂查询，使问题能定位到join候选生成、prompt或早停。

论文发现LIMIT提前终止和跨模态join实现会造成数量级成本差；只固定模型不足以统一答案，因为prompt和候选过滤仍不同。设计上的局限是gold继承源标签及随机关联，不能等同于真实业务关系；不同系统支持子集使未对齐的scenario平均值不能直接排名。

原文存在编辑不一致：§4.6称E-Commerce10queries而表2和§4.3为14；§5.3文本Movie scale500而表3为2000。分析以显式表格为主并保留矛盾，不用本地目录数量替论文消歧。''',
'''| 场景 | 论文查询数 | 输入组织 | 环境数据 |
|---|---:|---|---|
| Movie | 10 | Movies(id,title)、Reviews(id,reviewId,reviewText) | 无额外外部语料；两表为任务输入 |
| Wildlife | 10 | ImageTable(image,city,stationID)、AudioTable(audio,city,stationID) | 无；city/station由benchmark随机生成，图片/音频列指向媒体 |
| E-Commerce | 14 | styles_details含id、productDescription、productImage及结构字段 | 无；标签只给gold，不能暴露给系统 |
| MMQA | 11 | 5张Wikipedia文本/表格来源表加images元数据表 | 这些表就是查询输入，不是外部搜索服务 |
| Cars | 10 | Cars、ComplaintsText、CarImage、DiagnostAudio | 合成车辆属性与真实媒体关联，不代表自然观测到的跨模态关系 |

表2全量为1582560文本、84295图像、2037音频行；表3基础scale按上述场景为2000/200/500/200/19672。论文55queries不能直接用本地60条catalog覆盖；MMQA原编号Q2a/Q2b等应保存为source id，UI1、2、3编号另存。

§5.2明确ThalamusDB join batch=10，两侧表各10行整合进同一prompt。各适用系统LLM并发20；并发不是prompt batch，BigQuery两者均由引擎管理。benchmark规模轴是输入行数，并未评测多用户或并发多query吞吐（§3.3）。''',
'''斑马/羚羊共现属于Wildlife Q7：输入是一张包含图片列和city/station列的表，语义调用读图片，关系逻辑判断同一city是否同时存在两类动物。不能把“统计斑马照片”写成输入数据本身；那是任务意图，输入是照片记录表。§5.4解释更多行让系统更容易找到每个city的支持证据。

Movie Q7是真实的评论语义join测试。表4(a)给LOTUS费用$1.81、Quality .21、431.8s；Palimpzest$7.72/.68/1056.1s；ThalamusDB$.15/.57/636.9s；BigQuery$3.31/.70/198.3s。应关联作者具体SQL文件及其输入表，不能只显示两个SCAN节点替代输入说明。

MMQA航空公司logo匹配（例4.5）把airlines文本与image配对，输入两列跨模态；本地英文自然语言描述若从SQL翻译而来，应另列description而非覆盖source_query。''',
'''§5.1主实验EC2 g4dn.2xlarge（32GB RAM、8vCPU、T4 16GB，仅embedding用GPU），扩展实验双Xeon Gold5218/384GB Ubuntu。模型Gemini2.5Flash，适用系统temperature0；LOTUS1.1.3，Palimpzest0.8.2，ThalamusDB0.1.15，BigQuery2000slots。每实验5次。

表5在共同支持子集上，join均值：LOTUS质量.614/541.1s/$2.74，PZ.703/454.3s/$3.29，ThalamusDB.487/387.3s/$.14，BigQuery.601/69.4s/$1.02。便宜与更高质量并不一致；不可把最低费解释为最好。

MMQA Q7基础scale200导致40000次pair判断，PZ约35分钟、LOTUS约40分钟；scale400为160000次。E-Commerce Q8的图像pair累积可令内存达到约250/150/100GB（ThalamusDB/LOTUS/PZ）。规模实验总模型费$9935.80、约18天，不是单query费用。超时规则是1小时后该系统不跑更大scale，但本次不强制终止。以上结果是作者报告，未复现。''']),
dict(key='uda',title='Unstructured Data Analysis using LLMs: A Comprehensive Benchmark',year=2025,venue='arXiv',url='https://arxiv.org/abs/2510.27119v1',folder='Unstructured Data Analysis using LLMs- A Comprehensive Benchmark-arXiv-2025',loc='arXiv2510.27119v1，2025-10-31；全文§1–6，pp.1–13，表1–4、图1–14；p.10表3–4渲染核对。PDF提及的附录未包含在本下载版本，未声称读过。',sections=[
'''医疗文档集同时包含疾病、药物和机构资料：用户想把症状关联疾病，再找药物或机构，需要跨文档join与过滤，单个QA实例不足以测系统。不同UDA系统输入接口、chunking、逻辑优化、物理模型选择差异很大，已有系统论文常只有少量数据/程序，难直接比较。§1提出大规模、多样性、准确标签和易评测四项目标。

关键做法是先定义可提取属性的关系视图并标注，再把SQL模板实例化为不同难度的查询。这样系统可用自己的接口执行，gold依然来自同一关系数据库，不必要求各系统采用同一DAG。''',
'''§2按数据处理、查询接口、逻辑优化、物理优化梳理7种UDA系统；§3以原始文档→统一JSON→属性schema→人工/LLM交叉校验→关系gold→查询模板构成benchmark。每JSON对象是一文档，字段含text、image URL与metadata，不是把SQL或计划节点假装成原始输入。

§3.4人工设计每数据集5模板，再用脚本采样属性、条件、literal、聚合和预设join路径。240queries中220单表、20多表；主类为Select、Select+Filter、Select+Aggregation、Select+Join和复杂组合。方法限制在预定义147属性，可重复性强，但不覆盖任意开放式问题。

实验适配各引擎：Evaporate先抽表再SQL；ZenDB和UQE由作者重实现部分组件；其他系统也有修改。因此结果是benchmark适配配置下的比较，不等于原论文原生系统的无修改排名。''',
'''贡献是把属性级关系gold与跨接口系统比较结合，并细拆chunking、filterorder、join转filter、model selection/cascade、并发等因素。长文档和干扰文档使检索遗漏证据与读全文成本之间的权衡可测。

局限需要具体保留：Healthcare大部分无关类别的NULL gold由半自动分类建立，不能称10万文档每属性都纯人工标注；复杂SQL答案受属性schema上限约束；原文不提供系统版本及所有修改细节于正文。§2的系统能力矩阵是该次适配视角，例如把Palimpzest无Agg与后文用常规groupby衔接并列，不能据此断言库永远不支持聚合。

资料版本也重要：v1是5数据集，官方Bench-U仓库现介绍6数据集，新增的科研论文不能倒写成v1已有。Legal正文570、表2566，Healthcare标注段10000/100000存在差异，应保存证据而非补造一致数字。''',
'''| v1数据集 | 表2文件数/属性数 | 平均token | 输入及来源 |
|---|---:|---:|---|
| WikiArt | 1000/19 | 789 | 艺术家文字及画作图片，WikiArt |
| NBA | 225/28 | 8047 | Wikipedia球员、球队、经理、城市文档 |
| LCR/Legal | 566/19 | 5609 | AustLII澳洲判例；正文另说570 |
| Finance | 100/30 | 130633 | Enterprise RAG Challenge公司报告，文本/图片 |
| Healthcare | 100000/51 | 10649 | MMedC文档，疾病、药物、机构及其他类别 |

环境数据：任务数据是上述文档与显式join关系，通常无额外外部知识环境；attribute descriptions/schema属于查询规范，ground truth关系表属于评测环境且不应作为待测系统输入。Finance先用MinerU解析PDF；输入对象含text、image URL、metadata。Healthcare从680000抽100000，三主类别共6100文档由人工标属性，其余NULL来自类别判断，不能称100000全人工属性gold（§3.2–3.3）。

§4.6并发实验为1/2/4/8线程，不是每prompt塞1/2/4/8文档。§4.7的512token块上限、128下限是chunk参数，也不是batch size。正文无通用prompt batch合同；不要用文件总数替代batch。论文240条与本地6个数据集代表query或目录数量不能直接互换。''',
'''§3.4疾病→药物例是模板：按症状过滤疾病文档，以疾病名称连接药物文档，再抽取和按类别聚合。输入至少疾病、药物两个文档集合，关键输入列text及标识；关系gold的disease.name=drug.disease是评测模式，未必在原始文档中现成存在。用户若只看“Scan disease”无法知道输入结构，因此每query应列文档集、读取字段及提取目标。

原文模板保留{Attribute}、{literal}、{operator}等占位符，不是一条实例化原始query。正确记录应把template和官方Query文件中的具体实例分开；本次未逐个下载核验官方240文件，不能承诺本地英文query逐字对应。

可行动的洞见来自长金融报告：只取相关块可降token，却可能漏掉跨段成本构成；先明确所求属性和证据跨度，再选择整文或分块，比统一为所有query设同一chunk策略更符合任务。''',
'''§4.1：Ubuntu、4颗XeonGold6148共80cores、2×4090、1TB RAM、6TB SSD、Python3.7；默认GPT4.1mini、Qwen3-Embedding-0.6B。成本单位是每文档每query的千token，延迟单位秒，不能标美元。7系统是Evaporate/PZ/LOTUS/DocETL/ZenDB/QUEST/UQE，含作者重实现及适配。

表3Finance extraction：PZ138.90ktoken/8.38s，LOTUS297.85/13.24，DocETL818.10/1509.08，ZenDB32.33/3.55，QUEST29.30/2.65，UQE124.02/5.83；Evaporate成本“-”不是零。WikiArt extraction UQE.92ktoken/.83s、QUEST1.20/.89s，说明短文分块未必划算。图2精度多数短数据约.85，Finance最佳约.52（图读近似，不伪造精确条形值）。

§4.6 Healthcare并发1/2/4/8：1.46/.74/.38/.20秒，F1均.53。modelcascade在困难Legal几乎总升级，反而增加费用；modelselection提升质量也可能花更多钱。图10聚类代替group属性抽取引入高相对误差，图11语义search减少join候选却误删匹配。结论应是数据条件下的折中，而非统一最佳系统。

本下载v1虽多处指向Appendix，文件在参考文献结束，没有附录模板/修改列表；详细query原文、系统commit和batch参数需作者artifact补证，不能从正文推造。'''])]
idx=json.loads((R/'review_index.json').read_text());cat=json.loads((R/'catalog.json').read_text())
files=['出发点分析','解决的问题分析','Novelty分析','workload分析','usecase分析','benchmark分析']
for it in items:
 d=R/'reviews'/it['folder'];d.mkdir(parents=True,exist_ok=True)
 source=f"\n\n来源：[原论文]({it['url']})。本分析据所列版本全文核读，未复现实验。\n"
 for name,body in zip(files,it['sections']):(d/(name+'.md')).write_text('# '+name+'\n\n'+body+source)
 (d/'README.md').write_text('# '+it['title']+'\n\n阅读状态：full_text_reviewed。'+it['loc']+'\n\n'+ '\n'.join('- ['+n+']('+n+'.md)' for n in files)+source)
 rec={k:v for k,v in it.items() if k!='sections'};rec.update(reading_status='full_text_reviewed',review_folder=str(d.resolve()),pdf_sha256=hashlib.sha256((R/'pdfs'/(it['key']+'.pdf')).read_bytes()).hexdigest());idx=[x for x in idx if x.get('key')!=it['key']]+[rec]
 match=next((x for x in cat if it['url'].rsplit('v',1)[0] in x['url'] or x['title']==it['title']),None)
 upd=dict(title=it['title'],url=it['url'],year=it['year'],venue=it['venue'],topic='semantic operators / benchmark' if it['key']!='palimpzest' else 'semantic operators / optimizer',reading_status='full_text_reviewed',evidence=[it['loc']],review_folder=str(d.resolve()))
 if match:match.update(upd)
 else:cat.append(upd)
(R/'review_index.json').write_text(json.dumps(idx,ensure_ascii=False,indent=2)+'\n');(R/'catalog.json').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
print(len(cat),'catalog records;',len(idx),'full reviews')
