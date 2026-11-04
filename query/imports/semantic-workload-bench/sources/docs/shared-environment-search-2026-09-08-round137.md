# 第137轮：FiNER概念定义匹配与IOB核验

仍8/15，FiNER未合格。复用136轮实际下载的原论文、完整作者代码及HF原生数据。

本轮取得[FASB官方2020完整分类发布包](https://xbrl.fasb.org/us-gaap/2020/us-gaap-2020-01-31.zip)：6345468bytes631ZIP成员CRC通过，SHA256043d45481d7baacb2f04ebd97dbcfecdc6706b74e38fe002c4b4703ef7a0a4d2，全部解包。最初尝试不含日期后缀的XSD/XML得到404；官方目录核实正确2020-01-31版本后成功，失败收据保留。

1121256行全量检查IOB2：无非法前缀/转移；出现139个基础概念。通过官方documentation linkbase的loc→labelArc→label解析，139/139均找到定义，无缺失；这些定义合计3388空白分词。不能把整个631文件分类包的字节数当每个判断必须阅读的推理量，也不能把匹配名字证明历史标签语义未变化。2016–2020版本绑定、缺报告身份与句子信息充分性仍待核验。

具体EquityMethodInvestments定义描述权益法投资的资产负债表账面金额，区分初始成本经收益、分配和减值调整后的金额与公允价值。train0的4.5/35.8原标签可对照该概念；定义匹配不是逐项确认两数对应的期间、单位、实体或报告。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / gold |
| --- | --- | --- | --- |
| 提取财务数字并映射至139个会计概念 | 1121256句tokens | 官方2020定义139项，共3388词；完整分类包已取得 | 373744个B提及；train0中4.5/35.8为EquityMethodInvestments；历史版本未绑定 |

| 类python的DAG | 具体数值 | 下游边界 |
| --- | --- | --- |
| `sentences.sem_map(tag_mentions,E).explode()` | 139概念、373744原生提及 | span+concept，IOB2检查通过不是语义正确性证明 |
| `.filter(concept=='EquityMethodInvestments').project(sentence_id,span,text)` | 例2个提及 | 不按缺失的报告/期间聚合金额 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；train0目标两个EquityMethodInvestments | 同定义全集与句子→固定标签提取→IOB/span校验 | 未执行，相同目标，无优势证据 | ==查权益法账面金额与公允价值区分==→==核对披露上下文==→输出标签 | `XbrlMentionTagger(tokens,E_version)`；需先冻结历史兼容性，不以完整分类包大小代替E必要性实验 |

脚本：artifact/evidence/shared-environment-audit-20260908-v137/iob_audit.py、taxonomy_audit.py；结果iob-audit.json、taxonomy-audit.json；下载收据downloads.json与taxonomy-download.json。原包在data同名目录。无模型/快照/正式评分/测试套件/commit。下一步版本间定义稳定性与上下文缺口核验；若有效环境只是3388词定义，应保留短规则直接编译作为强对照。
