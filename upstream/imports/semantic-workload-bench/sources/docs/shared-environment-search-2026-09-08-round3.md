# 增量核验3：十个可行数据湖目标仍在进行

日期：2026-09-08，Asia/Singapore。目标保持至少10个通过门槛的数据湖/批任务，各有原论文、仓库下载、Query/数据湖表、DAG及LOTUS/Data Agent/operator表。目前通过数0/10；不将排除项算入10，也不将同一数据集换十个谓词就算十个独立湖。

上一轮为有进展：完成原论文/仓库下载、发布计数、来源捷径与示例表。本轮新增DeonticBench原始数据审计；当前没有外部阻塞，后续可继续搜索，目标不标完成。

## 下载与核验

[论文](https://arxiv.org/pdf/2604.04443)下载为 `data/shared-environment-audit-20260908-v3/paper.pdf`（894315 bytes）；[作者仓库](https://github.com/guangyaodou/DeonticBench)固定commit `3c168f943880fcbd3a3d717a516500312534273b`完整ZIP（9000665 bytes），解压于同目录repo，54个Git blob全部核对。未运行作者代码。另从作者[Hugging Face发布](https://huggingface.co/datasets/gydou/DeonticBench)固定revision下载USCIS whole parquet，精确URL/revision/哈希见[收据](../artifact/evidence/shared-environment-audit-20260908-v3/downloads.json)。提取PDF正文并渲染检查第3页；不是全文视觉检查。

## 本次证据改变了什么

- 完整USCIS发布242行，121 Accepted / 121 Dismissed。
- `statutes`精确不同文本221种，最大完全相同组4行；每行该字段空白分词中位数273.5。精确文本不同不证明底层法条完全不同，但不能据此认定已提供一个长共享E。
- 论文§2.3说明Accepted包含remand（发回重审），不能改写为公民身份/签证获批。源收集6483件与发布242条不是同一分母。
- 首行 `APR092024_01E2309` 的statutes字段含该申请人的出生、入境、收养事实，不是纯法规。text结尾又明确转述AAO对监护/收养文件性质的评估。因此即便字段名叫facts/statutes，也不能直接认为事实与裁决、E与x已经隔离。这是首行定点观察，不估计全库污染率。

**判定：尚不可行，不计入10。** 需要回到同一申诉类型、共同政策版本、原始证据与独立结果；不能将242个逐案法律摘录直接冒充共享数据湖。完整统计见[本次统计](../artifact/evidence/shared-environment-audit-20260908-v3/statistics.json)。

## 具体表格：保留正确标签语义的设计样例（不是通过项）

| Query | 数据湖数据1 | 数据湖数据2 | 数据湖数据3 | 私有gold |
|---|---|---|---|---|
| 判断USCIS申诉是否被接受（包括发回重审），返回ID清单及数量 | 应为冻结的共同法律/政策；当前发布的是221种逐案摘录，未通过 | 242条模型提取并人工修订的真实裁决叙事 | 原始证据和共同规则版本映射尚待取得；不能用reference_prolog冒充公开工具 | 121 Accepted/121 Dismissed；首行APR092024_01E2309为Dismissed |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `scan(cases)` | 242行，仅源审计；未构造public snapshot |
| `sem_map(case, frozen_policy, schema=AppealDisposition)` | 应保留Accepted含remand定义；实际没有统一冻结E |
| `filter(disposition == Accepted)` → `project(id)` → `count()` | 源gold目标121；不等于获批121；无模型执行 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 首行目标Dismissed，实际未知；当前含评估的输入可能泄漏答案 | 完整批准规则+充分事实→静态sem_map→合法标签验证 | 同样目标Dismissed，实际未知；换成Agent不能修复数据泄漏 | ==核政策版本与适用申诉类型==→==区分监护、收养文件及时间条件==→证据不足则ABSTAIN；这些是拟议公开证据步骤 | 版本检查→事实及文件性质提取→规则图→申诉处置；不得把remand归为最终获批 |

E-only编译/固定检索应同样允许；表格是设计，不提供预期优势、准确率或调用次数。当前禁止运行对照来制造“环境有用”的假象，先完成输入充分性与泄漏审计。

## 下一增量入口

已读[ECtHR原论文](https://aclanthology.org/2021.naacl-main.22.pdf)：11k案件，有actual/alleged两种不同标签，作者明确裁决依赖先例；单独附公约未必构成充分E。后续核作者原始数据/代码与可在时间切分前冻结的先例库，不能用alleged标签冒充裁决gold，也不能把测试裁决放进先例库。本轮尚未下载该路线原始仓库，不计入已核候选。

系统综述另有2026真实临床指南部署线索，但本轮搜索结果未核到公开完整protocol/cases/gold下载，尚不登记为可行。继续原始来源验证，不用凑满10的候选列表代替交付。
