# 第109轮：DDI Corpus完整来源与63页规范

状态：SOURCE_ACQUIRED_AND_AUDITED；不增加合格湖数，仍7/15。需要继续public/private构造、规范例句排除和任务必要性核验。

## 已下载而非仅检索到的来源

- [原始语料论文](https://e-archivo.uc3m.es/bitstreams/714e8ec0-6fd2-4ae1-ab3f-93c564ff5a1c/download)：The DDI corpus, JBI2013，994925 bytes，SHA256 f64a0ef9fa185c9a7ecf186901224d9b1446977dba03baed13dd3667cae7b530。
- [原始共享任务论文](https://aclanthology.org/S13-2056.pdf)：319853 bytes，SHA256 743f836d98a105486c71385e5a20ef17c15571f96042afb38df23bcd18fc79fb。
- [完整作者仓库](https://github.com/isegura/DDICorpus/tree/819b0fa538ed83ab2a8b4f5417bba3c03249b7f3)：完整ZIP5279155 bytes、9成员、CRC通过；SHA256 e666699dee838f32935e3240f32671bdc6cd91abd5573cfa1a6472c09028231b。2013XML包1036成员、BRAT包2048成员全部解压并CRC通过；未运行作者代码。2011旧版同家族，不另计湖。
- [作者机构完整指南](https://hulat.inf.uc3m.es/DrugDDI/annotation_guidelines_ddi_corpus.pdf)：63页、9029637 bytes，SHA256 1ec59eed0bf192104ffc6de9de787277c608882156ea6e4aa2dd9be1fabd4509。旧York链接410后，沿作者仓库归档网页所列路径找到当前机构镜像。封面日期2012-11-22，PDF创建2013-01-08。原生文本层乱码，63页全量渲染1800px并用Tesseract英文OCR，得到24194正则词；包含XML例子/页眉，不能当纯规则词数。图像核对PDF44页的否定规则。

## 原始数据范围与缺陷

全部XML1017文档、8940句、18491实体（49个不连续）、34449pair。须区分任务目录：`Test for DrugNER task`中的112文档941个false pair没有在本轮建立关系gold依据，不并入DDI关系评测。

关系任务范围：Train714文档+DDI测试191文档=905文档，8275句、17805实体、33508pair。正例5000、负例28508；正例类型effect2047、mechanism1621、advise1047、int284，另1条正例缺type。全原始实体4个surface疑点：3个不连续span拼接空格差异，Eszopiclone文件的(R)-warfarin出现实际错位切片；未修补。所有检查到的实体区间在界内，pair引用均可解析。

缺type为Dextroamphetamine_ddi.xml的DDI-DrugBank.d236.s29.p0，文本涉及Amphetamines与plasma corticosteroid levels。保留缺失状态，不根据自己的判断填标签。

作者当前README许可CC BY-NC4.0；仓库归档网页含较早BY-NC-SA声明，需要按具体发布物核对，不能把当前README覆盖到上游DrugBank/原论文。药物信息资源（如ATC/MeSH等）在指南中出现，历史版本及是否必需尚未获取/判断。

## 按要求的三表

这里任务是“文本是否表达规范定义的DDI”，不是预测现实药物相互作用或用药建议。false只表示该文本pair未表达目标关系。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量抽取药物实体及句内相互作用，筛选药代动力学机制报告 | 905篇DrugBank文本/MedLine摘要中的8275句 | 63页共同标注规范：实体边界/类型、关系类型、否定/可能性/矛盾信息/组名及例外 | 同文档上下文；给定entity版本须明确为annotation-given，端到端版本只给文本 | 33508个原生pair的ddi值，4999条有类型正例；NER专用测试不作为负例 |
| 7599505.xml标题提及cobalt与iron，描述吸收和滞留相互作用 | cobalt字符16–21；iron27–30 | §4.2及药代术语附录区分mechanism与effect | 原句明确absorption和retention | DDI-MedLine.d34.s0.p0：ddi=true,type=mechanism |
| Abacavir.xml首句：加入lamivudine后abacavir药代性质没有改变 | abacavir30–37；lamivudine82–91 | §4.5.1否定相互作用不标注为正例 | 该句还涉及zidovudine及组合，需逐pair处理 | d610.s0.p0：false，不是现实世界“绝不相互作用” |

| 类python的DAG | 具体输入数值 | 关键语义输出 | 下游gold |
| --- | --- | --- | --- |
| `docs → sentences → given_entities → all_pairs → sem_map(ddi_type,E) → filter(type=='mechanism') → project(pair_id)` | 905文档/33508pair；given-entities仅诊断版本 | 7599505示例应为mechanism；Abacavir示例为negative | 原始mechanism1621条；未排除示例/坏span前不是可确认集 |
| `docs.sem_map(entity_spans_and_types,E).explode(entities).groupby(type).count()` | 关系范围17805实体；另有NER测试可单独定义 | 实体边界与drug/brand/group/drug_n | 原生entity标签独立于关系预测；端到端需为坏span设排除或未标注契约，本轮未构造 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| cobalt/iron示例的正确目标mechanism；实际模型输出未知 | 固定sem_map提供同E与文本/实体pair，可固定检索§4.2、附录并缓存规则，然后返回类型 | 同样正确目标mechanism，未预设准确率差距 | ==定位规范中PK过程与effect的界线== → ==核对当前句子的absorption/retention证据== → 输出类型和位置 | `DDIRelation(sentence,pair,context; E_version)`：范围/指代→否定及不确定性处理→类型判定→证据/格式校验；缺资源时ABSTAIN，不用临床知识替代文本gold |
| Abacavir示例正确目标negative | 同一固定流程检查否定范围，不能仅查药名共现 | 同一目标negative | ==读取否定排除规则== → ==确认not altered覆盖该pair== → 输出文本负例 | 共享否定范围检查可编译；是否需要执行轨迹学习仍需与E-only/Coding Agent对照 |

所有预期为研究者设计，未运行LOTUS/Data Agent、未提取算子。固定流程可以使用同资源和批内缓存，必须对齐预算并报告完整构造成本。

## 下一步与证据边界

原论文报告规模与当前1017XML有差异，需按发布历史/具体文件确认，不能从论文1025直接替代计数。下一步核对BRAT/XML原生一致性、历史药物分类资源依赖、指南原句泄漏、与PHAEDRA同来源重叠。63页不是环境必要性的充分证据，短关系子任务可能只需要数页，须分别核验实体+关系组合任务的规则覆盖。

下载、OCR、离线审计产物：data/shared-environment-audit-20260908-v109/；收据及audit.py、audit.json、relation-scope.json在artifact/evidence/shared-environment-audit-20260908-v109/。无模型实验、无public快照、无新单元测试、无commit。
