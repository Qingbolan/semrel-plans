# 第126轮：PGxCorpus新候选，完整来源已取得

本轮从DrugProt/ChemProt检索中定位独立PGxCorpus作者源。尚不合格，累计7/15；它是药物基因关系抽取数据，不是临床处方或患者决策gold。

## 下载

[完整作者仓库](https://github.com/practikpharma/PGxCorpus)commit067513c1ed0ad55c28e62aef5a5bc14b6945595e，44396053bytes、72ZIP成员、CRC通过，SHA256a25a42a1d687e0abc28cd5d574503b3d49635b7bb8e55110034e922f06bde33b。原生PGxCorpus.tar的1890成员全部解包。[原论文PDF](https://www.nature.com/articles/s41597-019-0342-9.pdf)1311250bytes，hash在paper-source.json。仓库原版annotation_guidelines.pdf为2017-12-20的23页手册（split空白计5276词，非模型tokens）。许可CC BY NC4.0；不将可下载解释为无限商业权利。

## 原始核验

945句、911个PMID、6761实体、409不连续实体、2871关系，7个实际关系类型：influences936、isAssociatedWith730、isEquivalentTo293、decreases263、increases243、treats238、causes168。实体范围和关系引用全通过。3423个实体显示文本与offset提取不同，但全部可由两端strip解释；不连续片段保留源顺序，不能未经说明排序重写。

否定/推测不是A属性，而是851条AnnotatorNotes：hyp651、neg171、hyp neg10，以及Neg1、hypo2、htp neg1、not4和其他自由文本。备注目标引用有效；没有擅自把拼写变体归并成专家确定的属性gold。README称每句先双人独立标注再经第三名资深标注员复核；本轮未从原始独立标注重新算一致率。

手册§2.1.1排除非治疗用途的内源性化学物，但10070957_8讨论对照组基因型与激素水平，estrone/estradiol等被标Chemical。这是需要原论文/版本核验的具体潜在冲突，不直接宣布所有标签错误，也不自行加入例外。手册23页和数据规模不能替代规范一致性、复杂E必要性的证据。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 抽取遗传变异与药理表型关系，供文献证据检索 | 945真实文献句、911摘要来源 | 23页共享实体/关系/修饰规范 | 10070957_8：A2/A2相对A1/A1基因型，与estrone等激素水平升高相关 | A2/A2→各水平表型有6条increases；原生实体含不连续跨度，不是患者治疗建议 |
| 区分肯定关系与推测/否定的文献陈述 | 同批原文 | 共享关系修饰规则 | 备注采用hyp/neg及多种非规范变体 | 851条备注需映射核验，不能直接称851条统一属性gold |

| 类python的DAG | 具体数值 | 关键输出 | 下游gold |
| --- | --- | --- | --- |
| `sentences.sem_map(extract_graph,E).explode(relations).filter(type=='increases').project(source,target)` | 945→2871关系；increases243 | 识别实体、方向及表型边界 | 243原生gold关系，未构造公开执行或预测 |
| `sentences.sem_map(extract_graph,E).explode(relations).project(type,modality)` | 2871关系、851备注 | 备注拼写/自由文本规范先明确 | 此投影尚未冻结，不能用未知属性当FALSE |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；正确关系目标按原生6条increases；实体规范潜在冲突未解决 | 同E抽取→跨度/引用校验→固定关系过滤；所有臂同一schema | 未执行；目标相同，无优势结论 | ==查Chemical与phenotype边界== → ==读取increases方向和否定/推测定义== → 输出图与证据 | `PGxGraph(sentence,E_version)`保留不连续span；自由备注映射不能读gold临时补规则 |

原论文/完整仓库/手册已取得，先验任务可用于sem_map，但共享规范一致性与长E依赖仍待定。下一步核验备注规范和内源性激素例，而不增加其他同名版本为独立湖。

产物：artifact/evidence/shared-environment-audit-20260908-v126/downloads.json、paper-source.json、audit.py/audit.json、note-audit.json；完整源位于同名data目录。复跑原始诊断`python3 artifact/evidence/shared-environment-audit-20260908-v126/audit.py`。无public快照、模型运行、单元测试或commit，gold读取为开发。
