# Increment96 — CRAFT公开类别补全与环境依赖边界

仍7/15。复用原论文、完整作者repo、原指南和v94检查包；[作者CHEBI规则](https://github.com/lhunter-lab/CRAFT/blob/2abe82b8bb8089448b84937d5f61d8c218011322/concept-annotation/README.md)说明，CHEBI role类别用于本语料中的物质实体时应采用相同数字、不同CHEBI_EXT前缀。完整来源收据见round56，未新下载或改变原包。

本轮仅用公开冻结OBO和上述通用规则，沿role CHEBI:50906的is_a后代遍历，生成1274个非obsolete平行物质类。生成脚本不读取当前标注、私有目录或unused_classes列表。再由独立评测侧覆盖检查确认：8621个gold提及均可由58627直接Term或1274生成类解析，其中54类447提及依赖平行角色规则；其余扩展类已在原OBO中。不能把全部CHEBI_EXT前缀都等同平行角色类。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 按CRAFT语义生成化学物质索引 | 50全文＋给定排版 | 47页通用跨度规范＋当前CHEBI语义更新 | 冻结58627 Term本体及公开生成1274类目录 | 8621提及；447使用54个平行角色类 |
| PMID14611657中dye应映射哪个类别 | 原文dye[39986:39989] | 作者区分功能角色与具有功能的物质实体 | 原CHEBI:37958=dye，生成CHEBI_EXT:37958 | CHEBI_EXT:37958，不是原role编号 |
| 同篇fluorescent probe概念映射 | 原文[46481:46498] | 同平行角色规则 | CHEBI:39442与物质类CHEBI_EXT:39442 | CHEBI_EXT:39442；同一规则复用，不算新任务/新湖 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `E.catalog = ontology.role_descendants().map(material_parallel_class)` | 1274生成类；输入只读public | 共享确定性预处理，不是模型学习结果 |
| `docs.sem_map(mentions,E).validate(concept_id,spans).groupby(doc).collect()` | 50全文→8621目标提及 | 54类447提及涉及该语义转换；全部ID可解析 |
| `evaluator.check_coverage(private_gold,E.catalog)` | 8621/8621解析成功 | 只证明类别可用，不证明模型识别准确或跨度正确 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| dye→CHEBI_EXT:37958；未运行模型 | 固定本体检索识别dye，再按公开规则确定性转物质类；允许共享生成目录 | 同类别，无优势假设 | ==核对role与物质实体语义、查dye定义==→选择概念→确定性转换 | `ontology_lookup→contextual_concept→parallel_material_id`；此处可直接从E编译，不需要轨迹 |
| fluorescent probe→CHEBI_EXT:39442；未运行 | 同固定流程与跨度校验 | 同目标 | ==检查该概念是否属于role后代==→输出 | 同算子参数化使用，非第二独立operator发现证据 |

发现作者README具体例子写solvent(CHEBI:22586)，但本冻结OBO中22586=antioxidant、solvent=46787。未修改源；生成器依赖本体is_a语义和通用前缀规则，不采用错误示例的名称/编号配对。检查包50篇恰无22586/46787目标，因此这不是已发现的当前gold错误，但属于环境版本/说明冲突。开发例选择真实dye与fluorescent probe；完整收据examples.json。

科学边界：这确实展示了E改变期望输出，但仅凭447个前缀变化无法证明“长E必须反复推理”。这一部分可由简单固定程序完成，必须计入强基线。剩余长规范处理限定语、不连续共享成分、嵌套、歧义等；需要另行证明在实际批内的覆盖和简短规则基线是否已经足够。50全文的独立规模也不能用8621提及数字掩盖，因此本轮仍不升级为满足全部目标的湖。

产物：artifact/evidence/shared-environment-audit-20260908-v96/role_catalog.py、coverage.py、coverage.json、examples.json；data同v96/public-role-catalog.json。初版诊断把非数字扩展类误归平行类，纠正为直接Term与生成类联合解析；最终58627Term不含9个Typedef。没有覆盖v94快照、运行模型、读取作者pickle、构建学习轨迹、实验费用或优势结论。
