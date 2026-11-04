# 第133轮：NarrativeTime派生关系审计

复用132轮已下载的完整原论文/作者仓库742735e5434ef46f2bb88ebb9126bab96af34647。累计8/15，NarrativeTime仍未合格。

## 实际核验

转换器utils/nt2tml.py按`text.split(" ")`解释token，跨度为闭区间。a1/a2各36文档的1715事件和1386/1377时间线片段均无越界。这里只验证范围，不证明每个词语边界或语义gold正确。

原库转换TML各36文件均可XML解析且TLINK参数引用有效，各有207496有向边。去方向各103748对，无self-edge；与原论文表中102313的差额1435对尚未解释，不能选择一个数字当独立人工case数。

a1关系计数：AFTER48808、BEFORE48808、IS_INCLUDED15518、INCLUDES15542、VAGUE63618、SIMULTANEOUS14638、OVERLAP564。a2：AFTER/BEFORE各45886、IS_INCLUDED/INCLUDES各16403、VAGUE67336、SIMULTANEOUS15168、OVERLAP414。

反向关系一致性审计：a1在ABC19980120.1830.0957有24条方向不一致（12无向对），如ei90→ei102和ei102→ei90都为INCLUDES。a2为0。未将某个方向自动修正，也不据此认定a2所有gold正确。报告/指标必须允许双标注解释差异，不能把同名时间编号直接比较。

源转换文本还有明确重复：ABC19980108.1830.0711中TIMEX3包含the last twenty four hours，后续tail又有last twenty four hours；其他多词时间表达同类现象。源码text2xml按每token遍历但生成多词tag后没有跳过其余token，静态上解释该重复；本轮没有重跑或修复转换器。原始JSON全文保留，不能直接从TML重建输入。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 / gold |
| --- | --- | --- | --- |
| 恢复新闻事件时间线并查询先后/包含关系 | 36篇原始JSON全文 | 1715给定事件、289时间表达 | 33页共享规范与两名标注员时间线；转换后各103748无向对不是人工独立样本 |

| 类python的DAG | 具体数值 | 关键边界 |
| --- | --- | --- |
| `docs.sem_map(timeline,E).map(convert).explode(tlinks)` | 36→a1的1386/a2的1377片段→各207496有向派生边 | 转换语义与人工时间线评分待冻结 |
| `tlinks.filter(type=='INCLUDES')` | a1原始15542，a2原始16403 | a1有12无向对双向INCLUDES冲突，不是已核验可信计数任务 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；以原文构建与规范一致的时间线，不能照抄冲突边作为正确目标 | 同E/全文/给定事件→时间线→经验证的固定转换 | 未执行，无优势证据 | ==查包含/同时/不确定的定义==→==按原文时间锚点判定==→时间线与证据 | `Timeline`+独立转换；金标准冲突由构造侧处理，不允许Agent读gold补规则 |

产物：artifact/evidence/shared-environment-audit-20260908-v133/audit.py、audit.json、inverses.json。命令`python3 artifact/evidence/shared-environment-audit-20260908-v133/audit.py`；反向审计为本轮独立Python脚本命令，收据保留。无模型、public快照、正式scorer/测试套件或commit。下一步核对计数差额与原始时间线到边转换，或选择其他规模更合适来源，不能把36文档扩张成十万个独立cases。
