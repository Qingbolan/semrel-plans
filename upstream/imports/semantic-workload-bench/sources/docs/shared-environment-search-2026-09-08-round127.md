# 第127轮：PGxCorpus备注规范核验与任务边界

本轮复用第126轮实际下载的原论文、完整作者仓库067513c1ed0ad55c28e62aef5a5bc14b6945595e与23页原版手册，未重新下载或修改源标签。累计仍7/15；PGxCorpus仍未合格。

## 新证据

手册§2.3及Table1明确要求以BRAT Note记录neg、hyp、hyp neg，默认肯定无代码。因此“备注不是属性字段”本身不是格式错误。实际851条备注全部指向R关系且无重复目标：832条严格规范编码（651hyp、171neg、10hyp neg），19条非规范/自由备注。其余2020条关系没有备注；在严格遵循手册的编码解释下为默认肯定，但未人工逐条复核。

19条不能自动按“无规范代码=肯定”处理。例15983922_3的自由备注来自正文suggest语境，直接默认肯定可能改变语义。11555846_6的Neg是大小写变体，但本轮不自行改源gold。可以冻结一个排除19条待定关系的开发属性视图，规模2852=2020+832；尚未构造快照、运行或评分。

原论文Manual annotations段落说明：最终homogenization将metabolizes/transports合并到influences。该显式说明解释了手册与发布关系类型的部分差异，不能扩展成所有规范冲突都已解决。原论文也承认部分不一致源于未遵守规则或规则未覆盖案例；未找到对10070957_8非治疗用途内源性激素Chemical标签的明确例外。继续保留该疑点，不自行宣布标签错误或补例外。

原文与PDF可提取文本的连续12词归一匹配为0个命中文档，仅为筛查；手册包含图片标注，未OCR，不能据此宣布无示例泄漏。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / gold |
| --- | --- | --- | --- |
| 给定已识别关系，区分肯定、否定、推测肯定、推测否定，避免把不确定陈述并入肯定证据清单 | 945句、2871原生关系，给定实体/关系图是明确的上游条件 | 手册§2.3与Table1，关系类型另依论文最终合并规则 | 10430972_10：补充高剂量叶酸条件下，患者高同型半胱氨酸血症“不似由”MTHFR变异造成；R1 causes的gold为hyp neg |
| 从原句抽取完整PGx关系图，再筛选increases | 同一945句，不能给定目标图 | 23页手册加论文的发布规则 | 2871关系、243increases；Chemical内源性样例冲突仍未解决 |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold |
| --- | --- | --- | --- |
| `given_relations.sem_map(modality,E).filter(modality == 'affirmed').project(source,target,type)` | 2871总关系；19未决先不纳入确定属性gold；2852可按规范解释 | 四值modality；不是重新预测关系存在性 | 2020无备注默认肯定；651推测肯定、171否定、10推测否定；均未执行模型 |
| `sentences.sem_map(extract_graph,E).explode(relations).filter(type == 'increases')` | 945句→原生2871关系→243条increases | 实体边界/方向/类型 | 端到端规范一致性仍待定 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；10430972_10目标hyp neg，不进入肯定清单 | 同一上游关系与规则→固定结构化判定→过滤 | 未执行；目标同为hyp neg | ==查§2.3组合否定与推测规则==→判定语言作用范围→输出属性与证据 | `classify_modality(sentence, relation, rules_version)`四值输出及ABSTAIN；不能读取当前gold备注 |
| 未执行；不能保证内源性Chemical样例复现 | 完整规范与论文修订→图抽取→校验 | 未执行；没有优势证据 | ==核对类型定义与发布修订==→抽取图→报告证据不足 | `extract_pgx_graph`需先冻结规范，不允许执行中查看gold补例外 |

## 决定

属性任务的输入/独立gold可以进一步构造，但关键规则集中在一小节，无法用整本23页手册充当复杂E证据。完整图任务则仍有规范绑定疑点。因此保留为近似任务，不加入15个可行湖。接下来转向新独立来源，不再以相同静态检查推迟决定。

核验脚本与结果：artifact/evidence/shared-environment-audit-20260908-v127/audit.py、audit.json。命令`python3 artifact/evidence/shared-environment-audit-20260908-v127/audit.py`。本轮没有模型调用、快照或基准结果；语义示例均为开发曝光。来源：[论文](https://www.nature.com/articles/s41597-019-0342-9.pdf)、[作者仓库](https://github.com/practikpharma/PGxCorpus)。
