# 第136轮：FiNER-139完整来源与全量读取

累计8/15；FiNER暂未合格。原论文[ACL2022](https://aclanthology.org/2022.acl-long.303.pdf)920212bytes，SHA2567d96c43344ecd3782e80f2bc3ae6dafdb959f709c390e279002f7cc7c904936a。完整[作者代码仓库](https://github.com/nlpaueb/finer)commit863bb37e877e462e0b1cf9c211994978a348234a，25774bytes21成员CRC通过。

完整[作者数据仓库](https://huggingface.co/datasets/nlpaueb/finer-139)revision080f677a026e304c38666d759ef625d621dc8cb9，全部5文件取得，包括finer139.zip103199131bytes/4成员CRC通过，SHA256b9932fb2b936da766df79634e5438bd34fb9c035d7fd9209154ea3c740abced2。不是第三方小样本。

原生全量：train900384句40827499tokens179195带标签句307994个B开头提及；validation112494句5194320tokens21603带标签句35167提及；test108378句5120260tokens18789带标签句30583提及。总1121256句，token/ner_tags长度全部相同。标签原生是IOB字符串，不是整数；初次审计误按整数0检查导致带标签句计数不正确，已在脚本改为'O'并全量复跑，最终audit.json为修正值。未作IOB合法转移、重复句或标签语义审计。

论文说明源为约一万份2016–2020年报告，选139个高频US-GAAP标签（279含IOB/O），而发布每行仅id、tokens、ner_tags；没有原报告accession、日期或taxonomy版本。论文链接2020US-GAAP不证明所有历史标签都按该版规范统一。此前46轮2024官方XSD/定义不能无证据直接挂载。需核验版本绑定与句子上下文充分性、原标签专业审核来源；不把源XBRL提取自动称完全独立人工审计。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / private gold |
| --- | --- | --- | --- |
| 将财务披露数字映射到统一会计概念，建立可检索提及表 | 1121256句原生tokens | 139标签；完整定义及统一历史版本尚未冻结 | train id0的4.5和35.8均EquityMethodInvestments；test id1012885的47.6和13.4均EffectiveIncomeTaxRateContinuingOperations |

| 类python的DAG | 具体数值 | 下游gold |
| --- | --- | --- |
| `sentences.sem_map(extract_xbrl_mentions,E).explode()` | 三split共373744个B提及（IOB合法性待查） | token span+concept；不等于有单位/年份的完整财务事实 |
| `.filter(concept=='EquityMethodInvestments').project(sentence_id,span,value)` | 具体train0有2个提及 | 不能跨缺失报告/时期直接求和 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；train0目标两个EquityMethodInvestments提及 | 同版本定义与句子→固定跨度/概念抽取→校验 | 未执行，同目标不预设更准 | ==查概念定义及邻近概念边界==→==核对句内披露上下文==→输出提及 | `XbrlMentions(tokens,E_version)`，前提是版本与信息充分性已冻结；不得从当前gold选概念说明 |

产物v136 data完整源，artifact同名目录downloads.json、dataset-downloads.json、commit.json、dataset-metadata.json、audit.py/audit.json。复跑`python3 artifact/evidence/shared-environment-audit-20260908-v136/audit.py`。无模型/public快照/正式评分/单元测试套件或commit；没有完整E，暂不计可行湖。下一步核验taxonomy版本、标签定义与句子来源可追溯性。
