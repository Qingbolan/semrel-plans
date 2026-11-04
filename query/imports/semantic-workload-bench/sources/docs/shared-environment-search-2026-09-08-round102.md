# Increment102 — SciDTB逐标签规范缺口量化，暂缓升级

仍7/15。本轮将“适用E待核验”细化成26类证据登记，决定暂缓SciDTB作为严格长E湖的升级，保留302篇开发检查包，不继续靠重复结构检查累积资格。

复用round100下载的完整SciDTB原论文与作者repo、87页RST规范；本轮另实际下载其引用的Bunt–Prasad 2016 [DR-Core原论文](https://let.uvt.nl/general/people/bunt/docs/ISA-12-DR-core-revised.pdf)，141210bytes，SHA256 74fd49d3479baa01582496cbc8770da20030b70672b0240d31c26e000aa8c813。不是ISO正式标准全文。原SciDTB论文PDF2明确说明篇幅所限没有逐类详细解释；DR-Core提供20个核心关系的开放集合，不自动给出SciDTB全部26类定义。

本轮证据分类是研究者审计，不是作者发布的标签映射或执行规则。8类仍有定义/细分/合并范围缺口：bg-compare、bg-goal、bg-general、elab-aspect、enablement、manner-means、progression、temporal。它们覆盖302篇包中1000/4201节点，291/302篇至少含一项。这个数字不代表1000个gold错误，也不代表模型一定答错；只量化当前规范核验缺口。

其中progression在RST和DR-Core未找到同名定义，SciDTB论文只列名称；bg-compare原生名称与论文Related不同；manner-means涉及两个RST类别合并；Enablement与Purpose在RST中区分，但SciDTB例图含目的不定式，未能冻结对应边界。不能凭标签字面自行合并，再把结果称原始专家规范。E-only规则编译同样面临这个来源缺口，不能把它算成Agent优势。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 对302篇科学摘要输出完整篇章依存树 | 4201个给定EDU节点；v101原件投影检查已通过 | 87页RST＋SciDTB论文规则改写＋本轮DR-Core参考论文 | 26类来源证据登记，仅研究审计，不挂作模型政策 | 4201主gold节点；其中1000个使用当前仍未充分核验的8类 |
| D14-1059：区分递进、并列和补充说明 | EDU7讲系统可提供严格有效推导；EDU8继续讲系统还可产生另一类推导，完整后续EDU仍在包中 | 论文列Progression，但未定位完整判据 | 两段以“In addition…”和“also”连接，不能只靠词面写死类别 | EDU8 parent7，progression。真实开发例，不是已证明规范可执行的案例 |
| 统计规范缺口影响范围 | 302篇原生gold，仅evaluator研究使用 | 预先按来源判定的8类缺口集合 | 固定groupby与集合交 | 291篇至少一项；1000节点，不作为模型输入或模型选择器 |

| 类python的DAG | 具体数值 | 下游gold/边界 |
|---|---|---|
| `edus.sem_map(parse_dependency,E).filter(relation='evaluation').project(text)` | 302篇4201节点目标输出，未跑推理 | 主gold原生边；全树结构须依赖完整类别选择 |
| `private_edges.filter(label in unresolved_norms).groupby(doc)` | 1000节点、291篇 | 仅规范审计，不是待测工作负载，也不能用它挑简单确认集 |
| `D14_1059.sem_map(tree)` | 局部目标8→7 progression | 原生gold实读，模型实际结果未知；完整定义未核验 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| D14-1059目标8→7 progression；当前规范不足，实际未知 | 完整EDU及同参考资料固定sem_map；不能把gold例子当定义输入 | 同目标、同资料，不能保证Agent补出正确原规范 | ==查Progression定义及与Joint/Elaboration的边界，发现当前来源缺口==→记录证据不足或预算内完成，按既定评分处理 | `rule_lookup→evidence_check→head_and_relation→tree_validation`仅候选，不将缺失定义写成猜测规则 |
| PMID式单实例规则编译不适用；这里必须处理全树类别竞争 | 固定检索、E-only编译和CodingAgent都应允许相同资源 | 同样不能按private缺口标签优先查规则 | ==先建立公开规范覆盖表==→冻结后逐篇执行 | 覆盖表须从公开E构造，不能以本轮private类别统计驱动测试时路由 |

许可纠正：round100将论文许可概括为CC-BY4.0不完整；论文脚注明确同时提到CC BY-NC-SA3.0与CC BY4.0，称遵循ACL Anthology。不同摘要究竟适用哪一许可仍需来源级判断。没有据此重新许可或公开发布数据。

结论：数据数量/真实文本/人工树已求证，但完整规范对应尚不成立。仅扩大PDF页数不能补证。后续重新开启条件为获得作者完整关系定义或可核验的适配文档；不需要向用户索取许可或联系作者来结束本次工作。全目标仍有其他候选可推进，不是全局blocked。

证据：artifact/evidence/shared-environment-audit-20260908-v102/{downloads.json,norm_audit.py,norm-audit.json,example.json}；本轮PDF位于data/shared-environment-audit-20260908-v102/。无模型运行、快照更改、测试集调参或新学到的operator。

## 逐类证据登记

以下页码为RST PDF物理页；“定义可定位”仅说明有参考定义，不等于所有SciDTB适配均已确认。

| 标签 | 节点数 | 文档数 | RST页 | 证据状态 | 说明 |
|---|---|---|---|---|---|
| ROOT | 302 | 302 |  | paper_structural_rule | 人工虚拟根；每EDU一父节点、整图树约束。 |
| attribution | 245 | 190 | 46,47 | paper_explicit_override | 论文明确内容为head；覆盖RST方向。 |
| bg-compare | 99 | 97 | 47 | subtype_boundary_unresolved | 论文Related与原生bg-compare命名不同；未找到完整细分判据。 |
| bg-goal | 114 | 113 | 47 | subtype_boundary_unresolved | 论文Goal有实例，无与Enablement等类型的充分边界定义。 |
| bg-general | 72 | 67 | 47 | subtype_boundary_unresolved | 论文General，仅总Background定义不能自动得到三类边界。 |
| cause | 18 | 18 | 48 | reference_definition_available | RST Cause可定位；全局标签优先级未提供。 |
| result | 58 | 55 | 66 | reference_definition_available | RST Result可定位。 |
| comparison | 49 | 45 | 49 | reference_definition_available | RST Comparison；论文对称关系以前项为head。 |
| condition | 58 | 53 | 51 | reference_definition_available | RST Condition。 |
| contrast | 140 | 119 | 53 | reference_definition_available | RST Contrast。 |
| elab-addition | 1341 | 298 | 53 | name_mapping_inferred | 近似RST Elaboration-additional，非作者逐标签映射。 |
| elab-aspect | 62 | 26 | 54,55 | name_mapping_unresolved | Object-attribute与general-specific/part-whole边界无作者映射。 |
| elab-process_step | 62 | 24 | 56 | reference_definition_available | RST Elaboration-process-step；名称一致。 |
| elab-definition | 11 | 10 | 53 | reference_definition_available | RST Definition。 |
| elab-enum_member | 59 | 42 | 56 | name_mapping_inferred | 近似Set-member，论文称Enumerate；映射属研究者推断。 |
| elab-example | 65 | 51 | 58 | reference_definition_available | RST Example。 |
| enablement | 267 | 169 | 57,64 | definition_application_unresolved | RST Enablement要求未实现目标；Purpose也涉及目标，论文例图有目的不定式；不能无声明合并。 |
| evaluation | 335 | 268 | 57,58 | reference_definition_available | RST Evaluation定义可读；SciDTB合并核性标签，仍用全局head判据。 |
| exp-reason | 26 | 26 | 65 | reference_definition_available | RST Reason，仍需确认Explain子类适配。 |
| exp-evidence | 25 | 23 | 58 | reference_definition_available | RST Evidence，仍需确认Explain子类适配。 |
| joint | 302 | 196 | 61 | paper_partial_rule | 论文给方向/多元链；与List对应不是明确映射。 |
| manner-means | 250 | 165 | 61,62 | merged_definition_unresolved | 两个RST类别如何合并论文未详述。 |
| progression | 92 | 79 |  | definition_not_found | RST与DR-Core没有同名定义，SciDTB只有标签名。 |
| same-unit | 98 | 80 | 66,67 | paper_definition_available | 论文明确连接被嵌入单位分开的同一EDU两部分。 |
| summary | 7 | 6 | 68 | reference_definition_available | RST Summary定义；核性由全局head判据确定。 |
| temporal | 44 | 35 | 68,69 | merged_definition_unresolved | RST多种时间关系合并的边界未明示。 |
