# 第140轮：ImmigrationReason 全公开仓库与逐条件标签核验

仍8/15。本轮是新独立来源求证，不将其计入合格推荐。已下载[15页原论文](https://arxiv.org/abs/2608.20391)和[作者完整公开HF数据仓库](https://huggingface.co/datasets/afsharrad/immigration-reason)全部6个文件，revision `081d2cac29dcadfec88fdd675d7a0c4294d72b3c`。原论文544818bytes；decisions.parquet123255564bytes、findings_long.parquet9366604bytes、ocr_comparison.parquet409987bytes。逐文件URL/sha256/bytes见artifact/evidence/shared-environment-audit-20260908-v140/downloads.json。data同名目录保存原文件；不存在把Git LFS pointer算作下载完成的情况，3个Parquet均实际解析。

完整**公开数据仓库**已经下载，但它不是论文所描述完整抽取工程的交付：没有src/aao_dataset、Pydantic schema、独立人工500案复核清单或adjudicated.jsonl；论文/README检索没有找到另一个可下载代码地址。本轮不声称代码工程已下载。公开字段extraction_via为8974 v2_sync、3401 adjudication，没有逐字段人工确认标志。作者声明结构化标注CC-BY4.0、原文美国政府公共记录；转录仍是模型/文本工具产物，不等于逐字原PDF。

原生数据实查：12375个唯一ID、12375非空全文、12310个不同精确全文（65条超出唯一文本数，未做实体去重）。45290个逐条件finding，内嵌与flat表按ID/issue/prong/director/AAO/agreement元组多重集完全一致，0孤立引用。AAO五状态met8139、not_met25454、reserved8972、waived_by_petitioner1527、not_addressed1198。reserved不是not_met，状态不能压成二分类负例。

17类issue中Dhanasar3484个issue、NYSDOT1271、Kazarian step1 3787、step2 2699；这些是issue数，未冒充共享同一历史版本的独立案件数。文书日期跨越规则变更，需完整历史规范与逐案版本绑定。

13964个final order中13889个在全文中可精确找到（仅规范空白）。这支持裁决书**抽取**，不是从未裁事实预测。9936条全案层criticisms中6662条空白规范后在全文命中，其余3274条可能涉及标点/转录差异、拼接或抽取问题，尚未逐条诊断，不称全部错误。引用子串命中不证明完整专家gold质量。

长E门槛未过：论文附录A提供短抽取指令，未提供独立长指南或版本化完整规范库；指令明确只据裁决文本抽取、不能推断未陈述事实。即使另下载USCIS长政策手册，也不能据此证明完成这些抽取标签需要它。论文宣称500案专家复核，但公开包不能识别这500案，不能将全45290条自动升为独立人工gold。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | gold及用途 |
| --- | --- | --- | --- | --- |
| Q1 逐案抽取各审查条件的AAO结论，统计尚未审理事项 | 12375份裁决全文；首案2005-01-03_01_B5203 | 附录A五状态规则及历史框架简称 | findings_long为private评测源，不能作为模型输入 | 首案NYSDOT first=met、second=met、third=not_met；来源为作者抽取标签，未定位人工复核身份 |
| Q2 比较Director与AAO逐条件是否一致 | 同一全文、明确两种裁决主体 | 短规则：分别记录两个主体，不混淆 | private内嵌findings及flat对应 | 首案3个条件均agree=true；不是第二个独立湖 |
| Q3 提取AAO对原审理由的批评，汇总错误类型 | 全文 | 短faithfulness规则，要求原文引用 | private全案criticism9936条 | 首案空列表；3274条未精确命中需进一步审核，不能直接做精确span gold |

| 类python的DAG | 具体数值 / 样例 | 评分及下游边界 |
| --- | --- | --- |
| `docs.sem_map(extract_findings,E).explode(findings)` | 12375docs→45290作者目标finding；首案3条 | 保留五状态；输出数量是gold统计不是模型实际输出 |
| `.filter(aao_finding=='reserved').groupby(issue).count()` | 全量gold reserved8972；首案0 | 可评估中间状态及汇总，但共享规则较短 |
| `docs.sem_map(compare_director_aao,E).explode().filter(disagreement)` | 首案3/3一致，下游差异清单为空 | 与Q1相关派生任务，不能重复增加湖数量 |
| `docs.sem_map(extract_criticisms,E).explode(quotes)` | 作者全案列表9936条，6662条空白规范后原文匹配 | 未命中部分须审计后才能冻结精确评分 |

方法均未执行；以下正确输出是原生样例目标，不是对LOTUS/Agent准确率的预测。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| Q1目标首案[met,met,not_met]；输出未测 | 固定全文+五状态定义→sem_map→schema校验→展开聚合 | 相同目标；不预言优于固定流程 | ==读取五状态定义和NYSDOT字段==→定位AAO结论→核对主体→结构化输出 | `FindingExtractor(text,framework_schema)->list[prong,status,evidence]`；短规则直接编译也是必要对照 |
| Q2首案3个true；输出未测 | 固定分别抽取Director/AAO→同条件join→比较 | 相同目标 | ==确认director与AAO字段所有权及缺省语义==→分别取证→比较 | `CompareFindings`复用抽取结果；不需每案重新探索全部法律 |
| Q3首案[]；输出未测 | 固定找明确批评→原文子串校验→返回清单 | 相同目标 | ==读取verbatim要求==→检索批评叙述→验证引用；不能用private quotes当检索线索 | `CriticismExtractor(text)->verified_spans/ABSTAIN`；gold本身未闭合前不宣称误差是模型能力 |

固定工具程序、Coding Agent、E-only编译器与整批Agent均应共享资源和缓存权限。现有包支持大批量裁决抽取研究的来源核查，但长E必要性、独立gold和原始PDF对应尚未闭合，本轮不构造正式快照、不运行模型、不改源标签、不计为合格。

工程核验：系统Python pandas缺Parquet engine，未改全局环境，在data/v140/deps隔离安装pyarrow25.0.1，审计用PYTHONPATH指向该目录。audit.py实际解析三份Parquet（初步）并全量比较主表/flat表，结果audit.json。测试套件0，无模型/官方scorer/正式实验；源码仓库缺口保持显式待办。下一轮转新独立候选，或有新增证据时恢复此路线。
