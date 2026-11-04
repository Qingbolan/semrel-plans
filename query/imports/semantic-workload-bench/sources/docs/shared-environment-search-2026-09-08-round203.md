# 增量203：PICKLE特殊规则解释与36篇例句暴露名单

继续202，未增加候选计数，仍12/15。本轮重新检查原始BRAT API下载入口，得到504；新版论文PDF路径403，保留收据。202已下载的出版社完整HTML、作者完整代码/数据仓库、25页规范及两个本体附件仍可用。未更改原gold，也未执行模型。

来源：[原论文及附件入口](https://doi.org/10.1093/insilicoplants/diad021)、[完整作者数据](https://huggingface.co/datasets/slotreck/pickle)、[原始BRAT发布](https://zenodo.org/records/10076664)。本轮产物[audit.py](../artifact/evidence/shared-environment-audit-20260908-v203/audit.py)、[audit.json](../artifact/evidence/shared-environment-audit-20260908-v203/audit.json)，下载失败及NCBI映射收据在同目录。原件复用202，映射原文在`data/shared-environment-audit-20260908-v203/pmcid-map.json`。

重要修正：202实际例子PMID24046061_abstract中，GBSSI在SERF1 knockout grains中上调，gold是`GBSSI → is-in → SERF1 knockout grains`。本轮读到规则第17页的专门说明：上调可以提供存在/定位证据；下调则不能独凭该语句推断仍然存在，因为可能已完全抑制。因此该例与专门规则相符，不应依据2页简略本体的“always true”表述就认定gold冲突。此解释只覆盖该措辞，不证明全部489条is-in正确。

这确实提供了“额外环境纠正哪种具体错误”的可检验假设：只读本体可能漏掉上调例子的is-in；增加完整例外规则可能恢复它。不过本轮没有实际运行这个消融，固定检索/直接编译同样可能正确，不能预设需要Agent。

例句暴露：规范显式PMID命中36篇；202八词命中23篇全部包含其中。通过NCBI官方ID转换接口核两个PMCID，PMC6566436→31137463、PMC4168297→24777989，均未命中250篇。排除并集36后的**名单**为214篇、1908句、5098实体、1646关系。只是可复现选择审计，没有发布新public/private快照；原始BRAT丢标注定位仍未知，不能宣称214篇gold完整。八词/PMID检查也不是完整语义污染审计。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold与状态 |
|---|---|---|---|---|
| Q1批量实体抽取 | 拟保留214篇已分词摘要 | 实体本体4页 | 实体章节4535词，含语义/跨度/限定词规则 | 转换后5098实体；待原BRAT比对 |
| Q2批量关系抽取 | 同214篇；显式给定实体版与端到端版分开 | 关系本体2页 | 关系章节2658词，含上调/下调定位例外、同句证据及缩写规则 | 转换后1646边：interacts521、is-in378、activates363、inhibits276、produces108 |
| Q3生成产生/激活/定位关系清单及数量 | Q2输出 | 同类型语义 | 确定性filter/project/count | Q2gold派生，非独立新湖 |

| 类python的DAG | 具体数值 | 边界 |
|---|---|---|
| `select_by_frozen_exclusion_list(source)` | 250−36=214篇 | 构造侧选择，非模型运行；不删除上游原件 |
| `abstracts.sem_map(entities,E).sem_map(relations,E).explode()` | 5098实体、1646关系为所选转换gold计数 | 所有必要原文token公开；实验尚未执行 |
| `relations.filter(type=="is-in").count()` | 378 | 不能将被token转换丢掉的边当明确负例 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| GBSSI例应输出is-in；未运行 | 固定检索is-in本体和上调特殊规则→sem_map→关系端点校验 | 相同目标，未运行 | ==查定位定义与上调/下调特殊规则==→匹配句子措辞→输出 | `ExplicitEvidenceDetector + RegulationPresenceRule + RelationMapper` |
| 214篇输出与上述金标清单一致是评价目标；准确率未知 | 预建同版规则索引→固定实体/关系调用→确定性聚合 | 同一评价目标；准确率未知 | ==查实体边界、关系证据和缩写规则==→批量执行→校验 | `EntityMapper → RelationMapper → TypedEdgeValidator` |

以上规则结构是研究设计，不是从轨迹学到的产物。固定程序、CodingAgent、E-only编译都可使用同资源；如果一次环境编译已经足够，应该保留这个结果。

本轮结论：特殊规则解释得到原文支持；例句排除名单从23扩大并明确为36。仍未取得BRAT，全文必要性与转换gold完整性未证实。单独5类关系任务只对应2658词章节，不借用整本25页/7193词撑长环境。后续可在原始数据可达时恢复完整联合任务核验；目前不因一个入口失败停止全部检索，也不重复计数同一来源。
