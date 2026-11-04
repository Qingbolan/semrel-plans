# Increment81 — UKP protocol-specific P1/P2：第7个来源与构造开发候选

状态：SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT，7/15。此计数只证明真实来源、复杂共享规范、可构造输入和独立人工gold，不是环境增益、Agent优势或独立确认的VALIDATED结论。尚未完成15湖目标。

原论文/完整作者仓库/完整官方发布已在round79下载，round80核验版本与任务范围。[原论文](https://aclanthology.org/J17-1004.pdf)、[作者仓库](https://github.com/UKPLab/emnlp2015-ih-ig)、[大学官方发布](https://tudatalib.ulb.tu-darmstadt.de/items/d4a7ac0c-e7a8-466a-855a-917e42a24342)。精确字节与hash沿用v79下载收据，不声称本轮重新下载。

本轮独立输入审计发现v80的893文档中源4621/4654正文为空；854/917与1087正文归一化后重复。按公开规则排空正文、按lexicographic源ID保留重复组首条，未用gold选取。旧v80原样保留，不能继续作为全893完整输入结论。新v81为889非空唯一正文、456真433假。

完整45页指南130dpi渲染并Tesseract三并发OCR；原PDF无嵌入raster image。针对v80剩余文档，OCR的#ID与12词/65字符匹配没有额外命中。视觉抽查第13页，核实普通文本提取保留了规范及争议例子，不证明所有版式/近似重复完全无损。

最关键的任务语义修正：§3.3.1明确将没有总体立场、但讨论双方论据的文档标为P1。这是用于进一步论证分析的协议判定，不是普通说服意图分类。因此新task.json明确这一规则；没有改写任何原始gold。§3中历史争议案例是实际规则资源，不能声称11477词全部不可压缩；短规则编译必须成为强对照。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 根据本协议P1/P2判准筛选可进入后续论证分析的评论/帖子 | 889个真实非空唯一正文 | 原生title/topic | protocol.txt 11477词：第3页至第23页§4之前，含正式规则与历史争议处理 | 456 P1/true、433 P2/false；源标签为人工多数票，不是模型gold |
| 同湖扩展Toulmin组件识别（后续任务） | 原始340结构文档；排公开示例后294 | 主题/全文 | §4结构规则、§5示例 | 剩1071五类组件、71pathos另列；315Claim含隐式对象。未构造此视图；与说服性原始集合279源ID重叠，不增加lake数 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `scan(docs).sem_filter(P1_under_protocol).project(record_id).count()` | 889条输入，每条必须有输出或ABSTAIN | 456个选中ID，count=456；失败不从全量分母删除 |
| `scan(docs).sem_map(explicit_and_implicit_components).explode().groupby(type).count()` | 后续294篇/1071五类组件 | Backing198；不把零长度implicit Claim当普通span；任务未执行 |

具体真实例子仍用v80中的1025与1220：1025建议查阅居家教育研究，gold=false；1220表达公立学校宗教活动的立场及理由，gold=true。两条仍在v81。另以§3.3.1证明任务定义依赖本规范，但不能据此推断所有gold或实测错误率。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 目标1025=false、1220=true；批量gold456选中，实际预测未知 | 固定sem_filter提供完整必要正文/title/topic和同一E；允许固定检索、共享缓存、仅E编译 | 同一输出目标，不预设正确率优势 | ==查P1/P2判准和§3.3.1无总体立场的例外==→读全文→检查主题相关论据→输出与可观察条款 | `shared_protocol_index→assess_topic_argumentation→apply_balanced_argument_exception→emit_P1_or_P2_or_abstain`；真实轨迹提取尚未执行 |
| 目标保留文档中的显式/隐式Claim和其余组件 | 固定结构抽取及模式/offset校验；输出不能偷看gold重述 | 同一目标，独立任务视图待构造 | ==核对§4.2.2隐式表示与§4.3个别经历规则==→抽取→结构验证 | `claim_mode→component_spans→implicit_representation→schema_check`；衍生关系不冒充独立lake |

实际产物：`data/shared-environment-audit-20260908-v81/inspection-persuasion-v2`。894个资产：889公开文档、protocol/task和3份private文件。独立验证精确资产集合/hash、公开allowlist、非空正文、原始正文/title/topic、唯一gold与源ID对等全部PASS。无被测模型/真实提取/运行器评分/OS隔离；这是可供后续实现的检查快照，不是现成全实验框架。

本湖为何暂列来源构造资格：原始真实评论与人工标签可取；同一特定协议决定所有记录的标签；有效E不是另外任务章节的拼接；空输入、标签文件名、已识别示例和重复正文被处理。仍待检验：短规则是否足够、历史示例的边际价值、同模型同工具LOTUS/批Agent/Coding Agent/仅E编译比较、按作者/原始帖子划分与近重复、训练污染、完整成本与独立确认。数据研究用途及再分发限制沿用v79。

脚本/收据：`artifact/evidence/shared-environment-audit-20260908-v81/` 的ocr.py、audit_inputs.py、build_view.py、verify.py及JSON。OCR不是第二人工审核；source gold对等不是语义正确性证明。
