# 第二十增量：CGBench SOP9完整批次检查包

本轮把已下载的原材料组成真正可检查的共享输入批次，仍标记`INSPECTION_PACKET_NOT_VALIDATED`，没有运行模型或宣称新的benchmark完成。复用[作者原论文](https://arxiv.org/abs/2510.11985)、[完整作者仓库](https://github.com/owencqueen/cgbench) commit `db9f94152ca1872c8be8d8411040dcba2610b50b`、[作者数据](https://huggingface.co/datasets/owencqueen/cgbench_data) revision `6b017e57f18ccb1e6476260d9af4daa30508a523`，以及[官方SOP9完整63页PDF](https://www.clinicalgenome.org/site/assets/files/5391/version_9_gene_curation_sop_final2.pdf)。下载与哈希依据沿用v15/v16，不冒称本轮重新下载。

实际产物：`data/shared-environment-audit-20260908-v20/public/`只有共享SOP、queries.jsonl、papers/和task.json；private/gold.jsonl单独保存专家证据。脚本、全文件哈希清单、统计与私有引用缺口位于`artifact/evidence/shared-environment-audit-20260908-v20/`。public/private是目录契约，不是OS沙箱。

## 三项硬条件与剩余证据

- 共享E存在且版本确定：所有615个query源metadata都为SOP9，同一份官方PDF。与任务直接有关的主体规则位于印刷页38–42，另有54页起的实验例。**没有证据表明全部63页都必要**，页数不能代替实际复杂度。
- 大批量真实items存在：568个不同PMID、615个(gene,disease,MOI,paper)查询；全文文本最短975/中位6281/最长25992词。数字是按query统计，非PDF完整性证明。不是615个独立患者，也不是568个独立试验实体。
- 专家gold存在：773条原始证据，117个query有多条gold，必须做集合抽取。47个query的gold文本明确出现其他PMID，32个query含源论文表缺失的PMID。不能把剩余568个query直接称为“已证明自足”：正则仅给出缺口下界，也不能依据gold缺口筛出测试集。

规则依赖具体成立：SOP要求区分患者/非患者细胞、功能改变/疾病模型、实验验证/预测的蛋白相互作用、基因级/变异级功能证据；救援还区分功能丧失与功能获得机制。这些规则确实决定证据类别与评分，不是附加无关说明。但完整输入世界和复杂规则的必要范围仍需补证。

**层级边界**：SOP还有整份gene-disease curation的分类上限2/2/4与总上限6。它们不是每篇论文每条证据的上限，也不能将一篇论文得分直接转换成最终疾病关系判定。本轮只构造逐论文证据集合，不生成临床结论。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按SOP9逐篇抽取该gene/disease/MOI的实验性证据类别与绝对分值，筛选含高于默认分值的非人动物模型证据项 | 官方SOP9 63页，共享且有hash；必要子范围仍待实测 | 615条queries.jsonl，只含query身份、gene/disease/MOI/SOP、PMID及论文路径 | 568篇作者发布全文文本，已全部落盘；不包括按gold选择的额外参考 | 773条源专家证据，独立private；模型不读解释、分值或source_primary_index |
| ABCB7 / mitochondrial disease / XL / PMID21464130，已有开发曝光 | 模型系统需基因扰动并出现与疾病一致的表型；默认2、允许调整 | 本例query与其他614条共享规则 | 8000词论文文本，包含abtm-1动物实验 | 非人模型类别、3分（括号默认2）；0.5+2+0.5是该专家具体判断，不能编译成普适打分公式 |

| 类python的DAG | 具体数值 | 下游含义 |
|---|---|---|
| `scan(queries).join(papers,on=paper_path)` | 615query/568全文；每个路径已验证存在 | PMID重复仅共享论文读取，不重复计为独立来源 |
| `sem_map(extract_evidence_set, E=SOP9)` | 对117个多gold查询保留集合输出 | 不预先用gold类别切分查询 |
| `sem_filter(any(category==nonhuman_model and absolute_score>2))` | ABCB7的gold支持选中；未计算/未预测全批筛选数量 | 一个query输出一个Boolean，ABSTAIN另列 |
| `project(record_id).count()` | 不硬编码gold count | 从预测清单导出聚合 |
| `score(frozen_predictions, private_gold)` | 尚未运行 | 证据集合质量、分值误差、筛选P/R、coverage、完整成本另报 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 本例目标是非人模型/3分→True；是否能复现专家调整未知，未执行 | 同E与全文固定sem_map；允许固定分段检索、实验抽取、共享解析和复核，再sem_filter | 同一目标，不预言更准确 | ==查SOP模型与功能改变边界==→==在论文识别扰动、疾病表型、对照与局限==→==必要时查允许的公开背景证据==→输出类别、分值与证据；缺输入可ABSTAIN | `EvidenceOperator(E_hash, category_rules, experiment_extractor, bounded_evidence_lookup, scoring_schema, abstain)`；不写死基因/论文/3分；调整理由需从允许输入产生 |
| E-only编译或Coding Agent可能达到同样质量 | 一次从SOP编译固定规则，同样允许工具及batch缓存 | 轨迹提取产物可能与固定程序相同 | ==示范中实际出现的工具调用和证据读取==用于提取；未发生则不能虚构 | 对照E-only、Coding Agent、同轨迹摘要及完整batch Agent；构造/提取/验证开销全计，尚无经济结论 |

验证：全文件集合与哈希精确一致；615条public和private record_id一对一唯一；公开query字段allowlist通过；568论文文件全部存在。新增工程测试0，仅一次构造产物契约检查，不等于科学验证。没有划分训练/确认；未依据gold排除困难项；工具不能通过公开PMID访问当前ClinGen答案页面。

下一步需公开、可重复地补充背景文献来源，确定各query的证据世界，并审计必要规则范围；不要求先证明Agent优胜，也不能因数据包完整落盘就宣称足够推导全部gold。目标继续，当前严格合格计数不变。
