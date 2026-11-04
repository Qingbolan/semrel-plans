# 第129轮：DrugProt标签范围、源重叠与评分反例

仍7/15。原论文和完整作者仓库/语料复用128轮来源，新取得官方FAQ v4（Zenodo5648059），90902bytes，SHA256cbf4a3e30ab0bdf9be4ada230e3a181799f79d45ecf2520727368147585613c2。详情及URL见downloads.json。没有改上游源码或gold。

## 标签范围得到解释

实际渲染并查看原论文第5页Figure3：蓝色为发布13类，灰色为未发布类别。第6页明确说明人工标注按5大类16子类进行，但部分低频类别未发布。不是把全部旧标签映射/合并到13类。发布范围：PART-OF、DIRECT-REGULATOR、INHIBITOR、ACTIVATOR、AGONIST、ANTAGONIST、AGONIST-INHIBITOR、AGONIST-ACTIVATOR、SUBSTRATE、PRODUCT-OF、SUBSTRATE_PRODUCT-OF、INDIRECT-UPREGULATOR、INDIRECT-DOWNREGULATOR。旧手册NOT、无细分REGULATOR、MODULATOR等不能随意转换成其中一类；未发布类别不意味着临床不存在关系。

官方FAQ明确：输入给定实体，预测所有关系；Arg1为chemical，Arg2为gene；同一对可多标签。FAQ举例16920841/T18-T37实际在开发集，两个gold为ACTIVATOR和INDIRECT-UPREGULATOR。因此FAQ不能全文作为未曝光确认环境；其26多标签对统计也是旧数，本次数据实测231对。

## 重叠

4250摘要与先前CHEMDNER10000摘要有2069个PMID交集（训练1718、开发351）。不会将继承源算独立确认；也不会再把ChemProt作为另一个独立湖。

33页关系手册可提取文本连续12词匹配，命中17篇源摘要。命中如10047461、10403635、23535185、10193665，具体文本存audit.json。命中不全部自动等于完整gold泄漏，但应在构造时逐例核对或保守按文档排除；未做全页OCR，不能宣布17是穷尽名单。尚未构造正式public/private快照。

## 作者评分函数反例

锁定repo6b939554de38dbb69c462cc0d45c1cb17c3eaf57/src/utils.py中的format_relations以`pos0 = pos0 + idx`推进偏移；idx是从0开始的最后一个位置，下一文档会复用上一文档末位。

实际加载未修改的作者函数，pandas3.0.1，构造两个不同文档各一个实体对：gold仅doc_a有INHIBITOR，预测仅doc_b有INHIBITOR。正确四元组交集为0，期望数组分别[[1,0]]和[[0,1]]；作者函数实际都返回[[1,0]]。反例只执行format_relations，不是全main.py或论文历史结果复现，也不证明所有历史分数受影响的幅度。后续需要独立关系四元组集合评分，不能直接沿用该函数。上游文件未修改；该工程问题可解决，不是数据永久不可用的理由。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 建立化合物对蛋白直接活性与间接表达影响的证据清单 | 4250摘要与108387给定实体 | 33页关系手册、论文13类发布范围、去实例FAQ约定 | 16920841中choline[1139:1146]→BHMT[1059:1063]同时ACTIVATOR和INDIRECT-UPREGULATOR；此例已曝光仅作开发说明 |
| 关系清单按INHIBITOR筛选 | 同批公开原文及实体 | 同一共享关系规则 | 原始21035关系中6538INHIBITOR，排除示例后的规模尚未构造 |

| 类python的DAG | 具体数值 | 中间输出/评分 |
| --- | --- | --- |
| `abstracts.sem_map(extract_relations,entities,E).explode().project(pmid,type,arg1,arg2)` | 原始4250摘要21035四元组；231多标签实体对 | 全四元组集合，不能每对压缩为单一类别 |
| `.filter(type=='INHIBITOR').groupby(pmid).count()` | 原始6538条；无模型预测 | 清单及计数对同一冻结gold计算；不能把gold计数当运行结果 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；16920841目标两个关系标签 | 同规则+上下文→固定多标签抽取→四元组集合校验 | 未执行；目标相同，无优势预设 | ==查直接活性与间接表达的区别==→==核对一句多影响规则==→输出两标签及证据 | `extract_relations(text,entities,E_version)`返回关系集合；不得读取当前gold，所有臂共享缓存和检索权限 |

产物：artifact/evidence/shared-environment-audit-20260908-v129/audit.py、audit.json、scorer_probe.py、scorer-probe.json；原论文第5页渲染在data同名目录。命令分别`python3 .../audit.py`与`python3 .../scorer_probe.py`。无模型调用、单元测试套件、public构造、正式评分或commit。本轮是来源审计与一个执行反例。下一步完成手册图例/OCR与冻结开发构造，不能因原始结构通过便增加合格湖。

来源：[原论文](https://upcommons.upc.edu/bitstreams/4a4e2dc2-df18-4bcd-893a-ffeadc9bf2b3/download)、[官方FAQ](https://zenodo.org/records/5648059)、[锁定评分源码](https://github.com/tonifuc3m/drugprot-evaluation-library/blob/6b939554de38dbb69c462cc0d45c1cb17c3eaf57/src/utils.py)。
