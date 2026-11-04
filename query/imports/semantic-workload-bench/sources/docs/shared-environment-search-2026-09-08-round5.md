# 增量5：ECtHR裁决gold已找到，完成704案关联

本轮补齐了上一轮的关键缺口：**真实裁决标签存在，并能与先例库关联**。目前这是有实质数据支撑的待构造路线，仍不计为完整通过项（0/10）：统一冻结环境的充分性、事实边界和E依赖仍待核验。不把一个欧洲法院语料按不同条款拆成多个独立数据湖凑数。

## 实际下载与来源

| 资产 | 本地实际下载 | 来源/版本 |
| --- | --- | --- |
| ECtHR原论文 | `data/shared-environment-audit-20260908-v5/paper.pdf`，2,575,192 bytes，16页 | [NAACL2021论文](https://aclanthology.org/2021.naacl-main.22.pdf) |
| 实际裁决原始JSONL归档 | `ecthr.tar.gz`，32,852,475 bytes；内部正文119,060,538 bytes | [作者发布的Zenodo版本5532997](https://zenodo.org/records/5532997)，MD5 `b74661e9470b5dcd5edc9c0b814be064` 与发布记录一致 |
| LexGLUE原论文 | `lexglue-paper.pdf`，1,149,614 bytes | [ACL2022论文](https://aclanthology.org/2022.acl-long.297.pdf) |
| LexGLUE完整作者仓库 | `lexglue-repository.zip`，64,324 bytes，30个Git blob核验 | [commit 419a49d0fe82ecb69eb8e9343a9eb3382f1040fd](https://github.com/coastalcph/lex-glue/tree/419a49d0fe82ecb69eb8e9343a9eb3382f1040fd) |
| 历史先例库及其原论文/完整作者仓库 | 复用上轮已经下载的ECtHR-PCR | [上一轮下载与统计](shared-environment-search-2026-09-08-round4.md) |

本地相对资产路径均位于 `data/shared-environment-audit-20260908-v5/`。下载的是数据作者发布的原字段归档，保留case_id/case_no/date；没有使用丢失ID的HF标准分类投影来猜测关联。NAACL2021独立模型代码仓库未定位；下载的代码仓库是LexGLUE，不能冒充NAACL2021原实验代码。原论文、作者数据发布库及LexGLUE实现分别记录。

证据：[下载/哈希](../artifact/evidence/shared-environment-audit-20260908-v5/downloads.json)、[全量统计](../artifact/evidence/shared-environment-audit-20260908-v5/statistics.json)、[复算脚本](../artifact/evidence/shared-environment-audit-20260908-v5/inspect.py)、[校验收据](../artifact/evidence/shared-environment-audit-20260908-v5/validation.json)。未执行作者代码。

## 关联结果及其边界

11,000案、11,000个HUDOC ID，发布split为9,000 train /1,000 dev /1,000 test。字段同时含`allegedly_violated_articles`与`violated_articles`；这两者不能互换。原论文明确指出裁决预测依赖先例，声称违反预测则主要从事实出发；该论文论述为路线依据，尚不是本项目环境消融结果。[NAACL2021第2页](https://aclanthology.org/2021.naacl-main.22.pdf)

按2018-01-01切分，裁决库有825条后续案件；将申请号与精确日期关联PCR，要求唯一，得到704条，121条未匹配。仅移除PCR申请号末尾的版本字母，保留日期判别；没有按相似文本强行归并。704条对应8,826个逐案引用，其中8,533指向冻结E；其余293的原因尚未细分。

704对事实文本中，忽略空白/大小写后只有8对完全一致；进一步仅去前置标题、解码字面Unicode转义并保留字母数字比较，285对一致，419对仍不同。这是关联诊断，不证明285对语义完整，也不能把419对判为错误。后续应核对差异，公开输入优先保留原裁决库facts，而不是默默替换成PCR的事实/法律混合内容。

Article 6子任务有275条被诉案件：210条实际违反，65条未列为违反。`未列为违反`总体上不能未经审核都解释成实体裁决“没有违反”（也可能存在不可受理等程序类别）；本轮仅对下面两个实例查原判决law确认。各条款统计用于开发构造审计，不能用gold挑独立确认集。

## 具体Query/数据湖表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold（不提供给模型） |
| --- | --- | --- | --- | --- |
| 对涉及Article 6的后续案件，依据冻结E判断法院是否认定违反Article 6，并输出依据段落；先以275案开发关联集核输入充分性 | E：12,480份2018年前先例，facts+law合计68,031,172空白分词，索引一次共享 | R：275份案件facts，当前law与引用标签隐藏 | 申请号/日期/原文定位目录；必要的适用版本公约与国内法尚未完整冻结，不写成已有资源 | 210违反/65未列违反，尚需程序状态清洗；引用只作独立诊断 |
| 实例A：Nicholas v. Cyprus，63246/10，HUDOC 001-179878，2018-01-09 | 同一E，已有先例例如Ramljak 5856/13；未预先把gold选出的先例作为模型唯一输入 | 267词facts：审判法官的儿子及儿媳在对方律所工作，且与出庭律所负责人有姻亲关系，申请人在判决后才得知 | 必须区分关系本身、参与情况、披露与程序保障；这是拟检索的问题，不是硬编码结论 | TRUE；PCR存档当前判决§66确认Article 6 §1违反；当前判决§60–65仅构造审计可读 |
| 实例B：Ciocodeică v. Romania，27413/09，HUDOC 001-180288，2018-01-16 | 同一E | 1,427词facts：劳动纠纷胜诉后的执行、暂停、时效及救济过程 | 要核对债权人行动与国家执行义务；相关国内法是否已在E中尚未核齐 | FALSE；当前判决§116明确没有违反Article 6；不因债务未履行直接推为国家违反 |

两例标签已在下载的PCR当前案law中交叉检查；这些law属于private核验材料，不能加入R的模型输入。论文原始facts不包含全部当事人提交材料，预测真实判决与在完整证据下复作裁决需区分。

## 类Python DAG与具体数值

| 类python的DAG | 具体数值/输入 | 输出与状态 |
| --- | --- | --- |
| `E = freeze(PCR, date < '2018-01-01')` | 15,729份PCR源判决 | E=12,480；本轮不更改上轮时间边界 |
| `joined = unique_join(later_verdicts, PCR, case_no, date)` | 825条后续裁决 | 704唯一关联；121未匹配，不悄悄补匹配 |
| `R_dev = select_alleged(joined, article='6')` | 704条 | 275；属于开发构造审计，不是确认分割 |
| `candidates = fixed_retrieve(index(E), facts); verdict = sem_map(facts, candidates, task)` | A=267词；B=1,427词；k及工具预算待冻结 | 目标A=TRUE、B=FALSE；模型实际输出未知 |
| `score(freeze(predictions), private_gold)` | 逐案一输出，允许ABSTAIN | 尚未运行；程序性结果须先建立明确标签契约；不能过滤失败行 |

## 方法预期与operator表：未执行，不预设Agent优势

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent 的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| A的目标TRUE；实际输出未知。直接facts+简短条款可能忽视披露/关系细节，也可能正确 | B0直接语义调用；B2允许固定检索、取段、复核再判断，不强塞6800万词入prompt | 同一目标TRUE，是否改善未知 | ==定位公正审判争点==→检索E→==打开亲属关系及披露规则的先例段落==→核对事实→输出判断和证据 | `extract_issue → retrieve_precedents → check_applicability → decide`，有预算与ABSTAIN |
| B的目标FALSE；实际输出未知。不能假设看到未执行就必定误判 | 相同工具/索引，固定查询执行义务、救济和申请人行为；固定复核后sem_map | 同一目标FALSE，是否需要追加检索待实测 | ==检查执行时间线与申请人采取的救济==→==查国家积极义务与国内法适用版本==→充分则判断，否则ABSTAIN | 参数化时间线抽取+规则检索+证据覆盖检查；不得写死本案结论或申请号 |
| E-only编译程序也是强对照，可能与单轨迹产物一样好 | Coding Agent仅获任务、E与公开工具，一次生成批程序，冻结运行 | one-trace方法需真实示范后自动提取；本轮没有示范、没有已学算子 | ==一次公开任务探索，保存动作/工具结果==→提取→冻结→独立后续批次 | 共享索引、查询模板、公开分支、引用定位和终止条件；比较完整学习与执行成本 |

环境探索标记仅指可观察动作与证据检查；不要求私人思维链。可直接从E编译出有效程序是应接受的结果，不人为要求复杂Agent。

## 仍需完成

1. 核事实差异及程序结果标签，补充必要法规的准确版本；不能把当前判决解释拿来补公开输入。
2. 冻结E的时间与适用范围。不能用2018年后整理的指南重演2018年判决且宣称无未来信息。
3. 通过对照核E确实纠正具体判断错误，并评估同资源强固定程序；大库规模不证明成本必须逐行支付。
4. 完成独立确认与许可核验后才考虑计入合格清单。本轮0/10，目标持续。
