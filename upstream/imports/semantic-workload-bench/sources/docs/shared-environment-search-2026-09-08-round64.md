# 第64增量：NLM-Chem历史词表实下载，发现规范与gold的版本冲突

合格仍3/10。上一轮是实质进展；本轮补齐两个年度的完整共享术语资源，获得了更具体的否决依据：**原始gold不能直接按2019/2020完整词表评分，而下载包内规范已使用部分新ID。** 不把换词表造成的分数损失解释为模型语义能力差距。

原论文、完整作者语料发布包、规范已于[第63轮](shared-environment-search-2026-09-08-round63.md)取得，本轮未重复下载或运行作者软件。新增官方[2019 XML目录](https://nlmpubs.nlm.nih.gov/projects/mesh/2019/xmlmesh/)及[2020 XML目录](https://nlmpubs.nlm.nih.gov/projects/mesh/2020/xmlmesh/)各自完整Descriptor/SCR压缩文件；四个gzip均完整解压、CRC通过。它们是明确标年的候选环境，**不声称已证明作者标注时使用这两个版本**。

| 文件 | 压缩bytes | 解压bytes | 记录数 | Term节点数 |
|---|---:|---:|---:|---:|
| desc2019.gz | 15671542 | 291913618 | 29351 | 238580 |
| supp2019.gz | 46894712 | 606177308 | 249906 | 604271 |
| desc2020.gz | 15857500 | 295095609 | 29640 | 242208 |
| supp2020.gz | 48414535 | 640876217 | 270453 | 635419 |

SHA256及URL见artifact/evidence/shared-environment-audit-20260908-v64/downloads.json与downloads-2019.json。年度XML只有术语节点总数，不是独立任务数；本轮未下载qualifier/pharmacological-action文件，不称整个MeSH全家族归档。指南要求的化学候选、描述符树与SCR映射读取自这两类完整文件。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 同第63轮：按共享规则提取并归一化全文化学实体，产生文档—概念检索索引 | 3043词规范，要求最具体MeSH/SCR及类回退 | 完整2019/2020 Descriptor+SCR；应冻结一个有正确绑定依据的版本 | 原150篇全文 | Chemical38339；2061种完整字段值，诊断提取1810种原子ID；原子化只是覆盖审计，不是最终组合语义scorer |
| PMC4311586的trans-resveratrol | 同包规范以系统名称3,5,4'-trihydroxy-trans-stilbene举例，给Resveratrol的D000077185 | 2020 Descriptor D000077185名为Resveratrol，明确含trans-Resveratrol词项；创建日期字段2018-07-09 | 该全文实际化学名称 | 该文162条使用C059514的记录，包含trans-resveratrol；C059514在2019和2020 SCR均缺失 |
| PMC2980163的复杂含氮硫化合物 | 最具体项不可得时允许类组合归一化 | D014230=Triazoles，D013871=Thiones；2020分别有D03.383.129.799及D01.928/D02.886.753树路径 | 标题中长IUPAC表达及分子式C22H26N4O2S | 多处原字段MESH:D014230,MESH:D013871；是否能仅凭公开材料复现类选择仍未模型/专家验证 |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `env=load(frozen_descriptor,scr,rules)` | 2020共有300093 Descriptor/SCR记录；大量资源确实存在，不等于其版本已正确 |
| `mentions=sem_map(doc,env)` | 150真实文档；无本次模型输出 |
| `ids=parse_for_coverage(private_gold)` | 1810种原子ID；所有Chemical identifier符合本次诊断语法，允许逗号和'-' |
| `missing=gold_ids-env.ids` | 2020缺12种，涉及281次ID出现、11篇文档；2019缺11种，不能简单换2019解决 |
| `index=groupby(doc,normalized_concepts)` | 版本绑定解决前不执行方法准确率比较；不把旧ID映射成新ID后继续称原始gold |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 依2020词表，trans-resveratrol应检索到D000077185；原gold C059514会造成评分冲突，实际模型未运行 | 固定同义词检索+全文语境+规范映射；允许同完整词表、树与类回退程序 | 同样应面对版本冲突；不能期待Agent靠猜旧gold获胜 | ==核冻结词表版本；查词项及ID；检查规范示例一致性；输出证据与版本不一致诊断== | 版本化术语索引→语境实体识别→exact/class/combination归一化→证据校验→索引；旧ID迁移须独立、官方依据及新评分契约，不从确认gold补特例 |

另有SapC-DOPS-CVM字段MESH:D049231,MESH:C042511,-，说明'-'可与已知ID共存；不能把整条记录判为模型ABSTAIN或直接删掉。规范区分分号表示省略列表、逗号表示多化学类，但当前Chemical字段无分号；其导出编码与应有组合语义仍需核验。

本轮定位的是特定来源不一致，未证明全部gold错误，也未证明2018或某个更早版本必然正确。未合并年度词表造一个从未发布的E。没有public快照、模型调用、自动提取、独立确认或成本/准确率结论。新工程测试0；解析脚本读取全部四XML，原始失败/原词表字节保留。下一步优先核查其他独立来源的长规范与真实批量gold；NLM-Chem保留这一明确版本缺口，不继续仅凭年度近似推进合格。
