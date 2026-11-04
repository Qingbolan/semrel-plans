# 第130轮：DrugProt完整手册OCR与开发快照

状态：INSPECTION_ONLY_DEVELOPMENT，累计仍7/15。原论文、仓库、完整语料及规范下载复用128–129轮；本轮无新网络下载，不修改源gold。

33页关系手册逐页渲染并OCR（110dpi，tesseract psm3，4并行）；结合原始提取文本、官方FAQ、论文和评分仓库README进行连续12token与7–8位PMID筛查。额外按PMID排除既有CHEMDNER来源。

原4250篇排除2082篇后，保留2168篇、61730实体、13452关系、145多标签实体对。排除原因可重叠：CHEMDNER源2069、资源中PMID12、连续文本示例17。排除策略是开发清理，不是随机确认划分；OCR/字符串筛查不证明穷尽语义改写、近重复或模型训练污染。

## 环境与任务边界

手册G0禁止仅凭共现或模糊关联建边，G1规定从句子推断、疑难时参考整篇摘要并尽量限制外部查询，G4规定同一上层类别内选择有证据支持的最细子类。不同上层分支允许多标签。原论文Figure3冻结13类发布范围，未发布类型不合并。该规则链与任务输出直接相关，但尚未测出整本规范相对短规则的收益。

公开环境只含33页关系PDF与不带实例的发布范围/接口约定，未挂载论文、FAQ全文或NER手册。公开records提供原文与人工给定实体；GENE-Y/GENE-N统一GENE，属于官方关系任务上游条件，不能称端到端NER。private保存完整关系gold和PMID/split来源映射。当前无Agent模型或生成代码执行，目录分离不声称OS沙箱。

## 实际产物

`data/shared-environment-audit-20260908-v130/inspection-v1/`含public/private和精确manifest，2173个资产。build.py拒绝已有目标。独立verify.py核验文件集合、大小、hash、公开allowlist、2168篇全文、61730实体和13452gold关系与原生文件逐项一致，全部通过。未运行有缺陷的官方scorer，也未计算任何模型准确率。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 建立药物—蛋白关系证据清单并分类型检索 | 清理后的2168篇真实标题摘要 | 61730个给定实体（实体ID、类型、字符跨度） | 33页共享关系规范及13类范围；private13452关系 |
| 建立抑制关系清单 | 同一公开文档与实体 | 相同完整关系规则 | 4420条INHIBITOR，目标是文献关系不是临床禁忌 |
| 建立代谢底物/产物清单 | 同一公开文档与实体 | 同一规范的方向与代谢定义 | SUBSTRATE1442、PRODUCT-OF807、SUBSTRATE_PRODUCT-OF21；它们是同一语义抽取的下游视图，不另计湖 |

| 类python的DAG | 具体数值 | 输出与gold |
| --- | --- | --- |
| `records.sem_map(extract_relations, E).explode(relations)` | 2168→13452原生gold四元组；145多标签对 | 全关系集合，模型未执行 |
| `.filter(type=='INHIBITOR').project(record_id,arg1,arg2)` | 4420条gold | 文献抑制证据清单及逐文档计数 |
| `.filter(type in metabolic_types).groupby(type).count()` | 1442/807/21 | 三类分别聚合，不能把SUBSTRATE_PRODUCT-OF拆分成两个未标注gold |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；需输出多标签四元组集合 | 同规范、给定实体与原文→固定抽取→引用/类型检查→下游过滤 | 未执行；同一质量目标，不预设优势 | ==检索G0/G1证据充分性规则==→==核对直接/间接分支及粒度==→原文定位→关系集合 | `DrugProteinRelations(text, entities, E_version)`固定接口、关系集合、证据与ABSTAIN；可固定检索缓存，不能把探索强制为每行重做 |

具体已核验样例仍见129轮16920841的choline→BHMT双标签；该例因FAQ泄漏已经排除，不能冒称保留快照测试样本。下一轮应从当前快照选择未被手册展示的开发例并完善独立四元组评分，再判断构造资格。当前“public可读取”不等于模型默认路径已经执行。

命令：`python3 artifact/evidence/shared-environment-audit-20260908-v130/build.py`（仅未存在输出）与`python3 artifact/evidence/shared-environment-audit-20260908-v130/verify.py`。证据同目录construction.json、verification.json。无模型/prompt/种子/经济预算/cache实验、无单元测试套件或commit；这是构造/结构核验，非科学VALIDATED。
