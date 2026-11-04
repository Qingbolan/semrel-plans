# 增量206：PARSEME法语1.2完整源与非连续表达

新增独立来源，尚未资格确认，仍12/15。先检索1.3并下载[1.3原论文](https://aclanthology.org/2023.mwe-1.6.pdf)，但语言库与规范Git源码入口要求登录。转向实际公开完整的[sharedtask-data](https://gitlab.com/parseme/sharedtask-data)归档：完整仓库commit `dd162057e57241a76737117b59d6210b913a95a0`、1573 tracked文件，包括1.0/1.1/1.2/2.0等历史材料；本轮只审**法语1.2**，不把多个版本/语言计为新湖。公共导航仓库79文件另存，不冒充语料。

版本匹配新增下载[1.2原论文](https://aclanthology.org/2020.mwe-1.14.pdf)509769bytes、[1.2完整规范HTML](https://parsemefr.lis-lab.fr/parseme-st-guidelines/1.2/fulldoc.php)893394bytes，SHA256分别见收据。规范page-content正文提取63345 whitespace词，含多语言规则和例子；不是PDF页数，也不表示法语每句需要全部内容。原件`data/shared-environment-audit-20260908-v206/`，[hash与审计](../artifact/evidence/shared-environment-audit-20260908-v206/)。1.3实际页面页脚1.3.6与缓存显示2.0不同，保存实际字节，未混入1.2任务。

法语README说明MWE沿用1.1人工标注、1.2仅升级到UD2.5句法信息。词法/句法字段与第11列MWE gold分开；原先三千余句Sequoia有自动句法转换，MISC空格信息自动生成。法语来源含Sequoia/GSD/ParTUT/PUD，部分GSD文档来源/顺序在上游重排时已丢失；因此此轮研究单位是源句，不虚报完整原文档批量。README另述约3400万句无标注Wikipedia辅助库，本轮未下载，也不把它算gold规模。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| Q1逐句识别全部动词多词表达及类别 | 法语1.2共20961源句、511782整数word；来源ID全部唯一 | 同版多词性/词汇化/开放槽位规则 | 同版跨语言判定测试与法语适用类别；相关子集待冻结 | 5654表达：VID2156、LVC.full1878、IRV1501、LVC.cause97、MVC22 |
| Q2给定表达词集合→类型分类 | 可显式提供gold词集合的独立诊断输入 | LVC/VID/IRV/MVC区分规则 | 句内词形及允许句法 | 同5654类别；不把给定gold边界的准确率称端到端发现能力 |
| Q3将表达清单筛选/聚合 | Q1预测词集合及类别 | 固定类型契约 | 确定性explode/filter/count | 可由Q1gold派生，非独立新湖 |

| 类python的DAG | 具体数值 | 输入输出语义 |
|---|---|---|
| `sentences.sem_map(find_and_type_vmwes,E).explode()` | train14377句/3870表达；dev1573/425；test5011/1359 | 只是设计，不是可执行CLI；失败保留ABSTAIN |
| `expressions.project(sentence_id,category,word_ids)` | 2338表达不连续 | 必须保留离散word IDs，不能覆盖中间开放成分 |
| `expressions.filter(category=="LVC.full").count()` | gold1878 | 后续gold诊断需先处理重复、版本/规范边界 |

实际例来自`fr-ud-train_09570`：原句以“Tenue chez Vanderdriessche, la réunion …”开头，源gold为`LVC.full`，word IDs **[1,6]**，即`Tenue`和`réunion`。中间的地点和冠词不是该表达词集合。该例与其他前三例保存在audit.json；本次查看使它们属于开发暴露，不是独立确认。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 例中[1,6],LVC.full；未运行 | 固定检索词汇化/轻动词测试→sem_map→词集合校验 | 相同目标；未运行 | ==查轻动词、名词事件性、开放槽位和句法变体规则==→判断→输出 | `CandidateEnumerator + LinguisticTestResolver + DiscontinuousSetEmitter` |
| 全批类别/表达清单为评价目标，准确率未知 | 固定规则索引与缓存→逐句语义调用→确定性聚合 | 同目标，质量成本未知 | ==查需要的判定测试==→批量应用→检查 | `VMWEMapper + CategoryValidator`；非已学习operator |

表中流程都是预期；固定程序/CodingAgent/E-only编译能访问同一规则和缓存，不预设Agent有优势。页面本身已有决策树，必须把直接从E编译作为强对照，不能只与反复读全文的弱调用比较。

审计结果：所有表达恰有一次类别声明，源ID重复0，未见整数word的未知下划线标签；有45组相同text和5个仅一个整数word的表达，尚未判断是否源特殊情况/解析边界；未自动删除。非整数包装行另计，下一步核是否需要在其上读取表达标注。官方评测脚本已随完整归档取得，尚未运行。

数据许可分别处理：MWE人工标注CC BY4.0，UD文本README为CC BY-NC-SA4.0，Sequoia为LGPL-LR；不能把MWE许可扩展到全部文字或其他语言。规范CC BY4.0；本地研究未发布。当前无public/private构造、模型/官方scorer、规范例句重叠消除、资源增益或独立确认。下一步核5个单word、法语相关规范、重复和官方评测契约。
