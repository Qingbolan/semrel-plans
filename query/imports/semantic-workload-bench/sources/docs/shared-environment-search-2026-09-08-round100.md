# Increment100 — SciDTB原论文、完整仓库及树结构审计

仍7/15，SciDTB仅为待核验候选，不加入合格清单。来源：[ACL2018原论文](https://aclanthology.org/P18-2071/)、[作者完整仓库](https://github.com/PKU-TANGENT/SciDTB)、[被引用的RST手册镜像](https://gucorpling.org/gum/RSTDT-tagging-ref-manual.pdf)。

已下载原论文PDF219079bytes、完整repo1517870bytes/1673ZIP成员，commit1520d612fb19f739e099be867128360898219f24；ZIP全CRC通过并完整解包。repo实际1662文件：1355.dep（JSON内容）、306.edu、1README。README说baseline代码将来发布，不能把当前数据repo称完整baseline实现。另已下载87页RST手册，URL/bytes/SHA256均保存在v100/downloads.json；不把所有87页默认算作SciDTB必要E。

原生计数：train743份标注/492论文ID/10481非ROOT节点；dev gold154篇2133节点、second154份；test gold152篇2118节点、second152份。总798论文ID、1355份标注；292篇一份、455篇两份、51篇三份。节点总18983（包含5个正文null节点），不把不同标注当独立论文。按原生id检查无重复；parent遍历无环，但5正文节点parent=-1/relation=null，不连接虚拟ROOT，不能称完整gold树。

具体异常：train/P16-1069_anno2节点2；dev/second_annotate/P16-1163节点7；dev/gold/D14-1080节点1、D14-1099节点1；test/gold/D14-1042节点1。保留原件，不按另一标注补标签，不自动将null当ROOT或语义“无关系”。预审计最初用*.json没有找到文件；检查后确认.dep为UTF-8-BOM JSON，正式audit.py读取成功。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 根据统一篇章规则，为科学摘要构造依存篇章树，供后续按论证角色索引 | 798个真实ACL论文ID，现有文本已分词并分EDU | Carlson–Marcu RST手册＋SciDTB论文明确改写：背景细分、attribution方向、对称关系方向及多元链 | 给定EDU文本/编号的子任务；分割若作为待测节点需另核验未分割原摘要 | 1355份人工树含重复标注；默认dev/test gold306篇，3篇有不完整节点 |
| P14-1095：区分实验报告行为与报告的结果，确定哪个是篇章中心 | EDU15“实验表明”与EDU16“FactChecker准确率更高” | SciDTB规定attribution以被归属的内容为head，与通用RST相关规定方向不同 | 同摘要16个EDU，允许全部上下文 | train anno1：EDU15 parent16 attribution；EDU16 parent1 evaluation |
| 从预测篇章树提取evaluation内容用于结果索引 | 同上 | evaluation定义及树方向约束 | 固定filter/project节点消费预测关系 | 示例选出EDU16；这是依据人工树派生的索引gold，不是新的人类实用性评分 |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `abstracts.group_by(source_id).join(given_edus).sem_map(parse_dependency,E)` | 798论文ID；不能以1355标注份数扩充独立batch | 训练重复标注保留，尚未冻结唯一标签选择；dev/test306篇4251节点 |
| `predicted_tree.validate(one_parent,connected,acyclic).filter(relation='evaluation').project(text)` | 示例P14-1095的16EDU中返回EDU16 | 15→16 attribution、16→1 evaluation原件实读；未跑模型 |
| `gold.audit_parent_references()` | 全1355文件查出5处正文parent=-1/null；无环/重复id | 数据结构审计，不能当语义准确性验证；3处位于dev/test gold |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| P14-1095目标15→16 attribution、16→1 evaluation；实测未知 | 同E与完整EDU列表，固定sem_map输出树，再确定性结构校验与evaluation筛选 | 相同目标，不预设更准确 | ==核对SciDTB覆盖RST的attribution方向与内容中心规则==→判读整篇EDU→输出依存树→结构校验 | `load_versioned_rules→compare_discourse_units→choose_head→label_relation→validate_tree→project_evaluations`；拟议结构，未自动提取 |
| 无法解析的运行输出应ABSTAIN | 固定预算复核或结构错误返回，不读gold修树 | 同失败语义 | ==核对是否输入缺失或规则歧义==→预算内复核 | 可共享规则索引/缓存，静态程序同样允许；结构校验不等于人工语义判断 |

E资格仍未建立：原论文引用长RST手册用于分割/删除测试/关系，但同时删除或改变若干类别；完整适用条款到当前标签的映射未冻结。尤其给定EDU时，分割章节不能算作待测关系节点的必要开销。当前repo未提供单独SciDTB完整手册；检索到的SciARG规范属于同摘要上的另一任务，不能替代。应接着核对实际适用的RST关系定义与论文改写，审计论文示例泄漏、原生分词/EDU输入一致性及跨湖来源重叠。尚不构造确认集，不把798论文ID计数当文本去重/跨湖独立证明。

论文脚注称SciDTB按CC-BY4.0开放；当前仓库没有独立LICENSE文件，原文摘要及再分发范围仍需按来源核对。无模型/运行快照/轨迹提取/质量增益或成本实测。全部作者源文件保留，未运行作者代码。强基线仍须含相同资源的固定检索、E-only编译、CodingAgent及整批Agent。

证据：artifact/evidence/shared-environment-audit-20260908-v100/{downloads.json,audit.py,audit.json,example.json,preaudit.json}；原件data/shared-environment-audit-20260908-v100/。preaudit为初次只读诊断，正式audit.py增加了严格论文ID解析、每目录计数和唯一id断言。
