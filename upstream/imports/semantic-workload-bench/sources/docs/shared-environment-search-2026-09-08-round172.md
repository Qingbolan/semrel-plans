# 增量172：BC5CDR来源探查及两种指南复用对照

本轮没有新增合格湖，仍9/15。下载了两篇方法原论文及各自完整作者仓库；从随库BC5CDR数据得到实际批量和原生CID gold。但找到的CDR指南只有8页，方法仓库使用的指南约1000词，不能把它们列为已经满足复杂长E的来源。两种方法则是后续实验需要覆盖的具体对照。

## 下载及身份核对

- [Refining and Reusing Annotation Guidelines for LLM Annotation](https://aclanthology.org/2026.acl-long.1760.pdf)：315151 bytes，SHA256 `0f0b205eea63f7bf4855fa9453423bc46c36f2c9261af50e49024cf60f40e15f`。
- 对应完整[作者仓库](https://github.com/KonWooKim/llm-guideline-moderation)：commit `33d58d6603ab2c6cfd5aa98e4b14ae17b1ed2ac4`，1828个tracked文件。
- [Can Frontier LLMs Replace Annotators in Biomedical Text Mining?](https://arxiv.org/pdf/2503.03261)：1248074 bytes，SHA256 `4f8ee2b501d4bdb09b79acf0f03a66c853c82681475ae01e2f9e29abc5c02a3f`。
- 对应完整[作者仓库](https://github.com/ekkkkki/LLM-Replace-Annotators-in-Biomedical-Text-Mining)：commit `0622e159c92c71a8ad7288fe92dd671ebb2cf2a8`，21个tracked文件。最初搜索把两种工作并列返回，已用各自README和原论文核对归属，没有把此仓库误归给前一篇。
- [BC5CDR指南镜像](https://huggingface.co/datasets/bigbio/bc5cdr/resolve/main/bc5_CDR_data_guidelines.pdf)：393680 bytes，SHA256 `b9210b695c6e94e22d8b2ae922de045cdb6d68f823c5488b3251b52ef7da3aa3`；实际8页、PDF创建日期2015-03-16。镜像不是作者原始主机；未完成与历史官方文件的哈希比对。

完整逐文件哈希在`artifact/evidence/shared-environment-audit-20260908-v172/downloads.json`。下载原件在`data/shared-environment-audit-20260908-v172/`。本轮未取得BC5CDR最初语料论文，也未下载历史MeSH/CTD全库，因此不是完整原始CDR来源闭环；不能据方法论文及二次打包补足此缺口。BioRED是99轮已看来源，不重复计湖。

## 实际数据与方法边界

读取Frontier仓库的BC5CDR.tar.gz内部三个PubTator文件：train500篇/9385mentions/1038CID关系，dev500/9591/1012，test500/9809/1066。合计1500篇、28785mentions、3116CID关系。这里只核验原生行数和实例，未完成offset/ID闭包、与官方发布包逐字节比对或与其他生物医学湖的PMID重叠审计。

Moderation仓库实际JSON数：BC5CDR train500/valid100，BioRED400/100，NCBI Disease593/100；这些是文件数，未逐项验证唯一PMID。随库指南空白分词分别1197、1027、1010词。它没有给出一个30–100页的共同环境作为当前实现输入。

Refining论文和README的流程是：随机抽10篇训练文档→标注→与人工gold比较→分析差异→生成原则→修订指南→重标注，阈值F1≥0.9或不再改善时结束，再用于独立valid集合。README默认示例证据上限5。**这是多样本文档的迭代监督，不是只看一条不带当前评测gold的Agent执行轨迹。** 发布包说明重组了原系统，并不保证逐比特复现论文。当前只读源码/配置和材料，没有运行模型，不引用原论文F1为本项目实测。

Frontier论文说明把指南人工切块，再按任务上下文检索。仓库CID prompt内仅三条主要规则，涉及机制关系、少量biomarker、摘要明确陈述和最具体疾病。读到prompt不等于已复现完整检索程序；人工分块、索引、检索与调用成本都应纳入比较。

## 用户要求的三表（候选/对照分析，不进入合格清单）

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量提取摘要中的chemical-induced disease概念对 | 随库1500篇PubTator标题/摘要 | 8页CDR指南；不足以称复杂长E已满足 | 可显式给定概念标准化实体表；历史术语库未取得 | 3116条CID关系；不解释为全部临床因果事实 |
| PMID227508具体例：列出该摘要的CID关系 | 标题“Naloxone reverses the antihypertensive effect of clonidine.”；摘要描述alpha-methyldopa的降压效果 | 摘要明确陈述、最具体疾病及任务关系范围 | 给定实体：alpha-methyldopa=D008750；hypotensive=D007022 | 本文原生CID行`D008750 → D007022`；标题药名并不自动决定gold |
| 批量实体识别及归一化 | 摘要原文，28785mention行 | 实体指南；归一化另需历史术语库 | 当前目标span/code不能同时作为待预测答案公开 | 存在span/type/code字段，端到端构造未验证，不能称第二个已就绪任务 |

| 类python的DAG | 具体数值 / 输出 | 边界 |
| --- | --- | --- |
| `scan(abstracts).join(given_entities).sem_map(extract_CID,E).explode().project(pmid,chemical_id,disease_id)` | 1500篇；PMID227508目标`(D008750,D007022)` | given-entity条件；不能把所有药物共现都判CID |
| `relation_rows.groupby(chemical_id).aggregate(disease_ids)` | gold全量3116边，尚未运行预测聚合 | 全文外事实不在该任务证据世界中 |
| `sample(train,10).annotate().compare(train_gold).moderate_guideline().freeze().annotate(valid)` | 仓库默认10篇；valid每族100文件 | 作者方法的监督量与单轨迹方案不同；无本次推理 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 正确结果应包含示例gold对；实际质量未知 | 固定sem_map读摘要、给定实体、规则；允许同资源的固定检索 | 同一gold目标，无优势预设 | ==核对CID任务范围、定位摘要证据、核对实体ID==→输出概念对 | `EvidenceLookup → RelationClassifier → IDProjection` |
| 指南检索有可能已经足够 | 人工或E-only分块、固定检索、结构化调用 | Agent可探索章节，但不自动比固定检索强 | ==按当前歧义检索规则并保留证据==→结构化输出 | 可复用规则索引与检索计划；必须计入人工整理成本 |
| 监督修订指南可作为额外对照，不等于直接LOTUS默认能力 | 给定相同训练监督后，固定流程也可迭代修订并冻结 | 单轨迹提取不能私用10篇gold后仍称相同监督条件 | ==观察一次执行公开动作与证据==→提取冻结；若访问历史标签则单列监督量 | 比较`E-only编译 / 固定检索 / 监督指南修订 / 单轨迹算子`，对齐模型、资源和成本 |

本轮新增的是来源缺口与对照证据，不是新模型结论。无安装、训练、API推理、prompt实验、种子、token预算、推理并发缓存、测试套件或正式快照；不适用项均不记为0成本。git clone/PDF下载均已完成，无待运行session，无commit。
