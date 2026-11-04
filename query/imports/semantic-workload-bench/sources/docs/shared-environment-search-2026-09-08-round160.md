# 增量160：RoBIn回到医学偏倚任务，但公开上下文由gold证据选择

本轮先查重，确认RoBBR已在40审计，未重下载；新增的是RoBIn（不同作者/任务，不先假设原论文池独立）。状态`SOURCE_ACQUIRED_NATIVE_AUDITED_NOT_QUALIFIED`，仍8/15。

## 来源与下载

[原作者预印本](https://arxiv.org/pdf/2410.21495)已下载，1618683 bytes，SHA256 `5df90d3172ebe5fdfbb84f05c922d726b2e247a44e2bb822307970de55ecc247`；README现在引用2025 JBI正式文章，本轮未声称下载出版社终稿。

[作者完整仓库](https://github.com/phdabel/RoBIn)通过git clone取得，commit `8b84a6fe975d3926fc07b25131a9e4da18712dba`。两份原生data JSON共29463532 bytes：train23579343、test5884189；精确哈希见`artifact/evidence/shared-environment-audit-20260908-v160/downloads.json`。原件位于`data/shared-environment-audit-20260908-v160/`。源码/models目录下载不等于取得作者训练所需的所有外部权重。本轮没有购买或下载作者NDA下的Cochrane原RM5。

## 原生核验与不合格原因

| 发布split | 行 | 独立filename数 | review-study组合 | LOW/HIGH/UNCLEAR | context空白词中位数 / 最大 |
| --- | ---: | ---: | ---: | --- | --- |
| train | 13554 | 4428 | 5068 | 9146/1934/2474 | 167/2083 |
| test | 3404 | 2237 | 2436 | 2303/488/613 | 165/1421 |

共16958行、4712个filename。train/test交集：1953 filename、2105 review-study组合、1026个完全相同context。不是以论文隔离的后续确认集；filename数量还不是近重复/多报告试验实体数。全部answers.text的answer_start子串匹配，0失败；这只证明发布偏移一致。

论文§4.2明确：用Cochrane人工支持句检索源论文句子，cosine similarity大于0.5后选最高匹配并提供上下文。上下文选择依赖gold支持句，因此适合明确的evidence-given诊断任务，不能直接当公开全文检索任务。人工reviewer评论/改写可能导致对齐误差，偏移通过不证明语义支持关系准确。

JSON有LOW/HIGH/UNCLEAR三种原标签；论文方法部分讨论low与high/unclear合并，正式实验应明确二/三类映射，不能混报。公开记录没有完整长Cochrane规范，也不是全部全文。即使复用40已下载的543页手册，仍需绑定原review规范版本，不能借长文件补成必要环境。

首个训练例：review CD000011、study STD-Apter-2011、filename PMC3164914.txt；问题为随机分配序列是否随机。提供的上下文包含“第二次访视用计算机生成算法按1:1随机分配PS/AE”的句子，发布LOW，answer_start473。测试首例同一研究评估人员盲法，体现跨bias不等于跨研究独立。例仅用于开发解释，不作为重新确认数据。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 限制 |
| --- | --- | --- | --- | --- |
| 给定已选证据，判断随机分配偏倚 | QIT-01 train4047/test1014行 | 信号问题与偏倚名称，缺绑定长规范 | 公开context由gold支持句检索选择 | LOW/HIGH/UNCLEAR；不是独立全文审查 |
| 在给定段落中定位支持证据 | 16958短上下文与问题 | 原任务问题定义 | context而非完整论文 | 全答案偏移一致；取证输入已含gold选择信息 |
| 全文审查后输出低偏倚研究清单 | 需要原始4712论文全文及review范围，当前不齐 | 需要绑定版本的规范与具体结局范围 | 原支持句不得用于预选公开输入 | 当前数据不直接支持该端到端DAG |

| 类python的DAG | 具体数值 | 语义边界 |
| --- | --- | --- |
| `scan(provided_contexts).sem_map(extract_support,question)` | 16958行；0原生偏移错误 | annotation/evidence-given，只能按该信息条件评价 |
| `contexts.sem_map(assess_bias,question,E)` | QIT-01共5061行；不是5061篇独立论文 | E缺长规范绑定；不能宣称长上下文成本 |
| `predictions.groupby(review,study,bias).collect()` | train/test共享2105 review-study | 重复/冲突聚合还未定义，不能自动多数票制造gold |

以下均未执行模型，不用实际标注推断哪种方法更强。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 随机序列例目标LOW；实际未测 | 固定调用读取已给上下文，定位计算机算法随机分配依据并输出类别 | 相同目标，无优势预期 | ==确认当前偏倚是序列生成，区分分配隐藏==→读已给段落→标签 | `BiasSpecificEvidenceReader→Decision`；此短任务可能完全不需要学习复杂算子 |
| 支持句位置目标start473 | 同context语义抽取再确定性匹配offset | 相同目标 | ==核对问题所需证据范围==→返回句子与位置 | 有界span抽取；不得把gold预检索成本漏记后称端到端收益 |
| 全文任务当前无可宣称结果 | 必须补齐完整公开输入与独立文档split后运行 | 同样不能由Agent弥补缺失gold契约 | ==来源核验属于构造侧==，未完成则不启动声称完整任务 | 不制造输入fallback；不能把当前短context自动扩成全文结果 |

可重跑audit.py/audit.json/span-errors.json及download收据位于v160 evidence。未提供合格新湖，因为E缺失、上下文由gold选择且原split论文大量重叠。无模型/prompt/训练/种子/token费用预算/推理并发缓存/测试套件/正式快照/评分/commit。
