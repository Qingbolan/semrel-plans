# 第三十九增量：CLC-UKET访问与结果语义

**累计仍1/10；未计入合格清单。** 退伍军人裁决检索引出英国就业仲裁的事实—结果路线。本轮取得原数据论文和同源后续研究原论文；未取得完整病例或作者仓库，无法满足原论文、仓库、长共享规范、真实批量与独立gold全部条件。

| 来源 | 本次核验 |
|---|---|
| [CLC-UKET原论文](https://aclanthology.org/2024.nllp-1.7.pdf) | 16页、230,768 bytes已下载；数据设计19,090标注案例、14,582预测案例为论文报告，非本地数据计数 |
| [Shortcut Learning原论文](https://arxiv.org/abs/2607.04261v1) | 25页、1,180,013 bytes已下载；33,158是claim-level规模，不能当独立案件或新数据湖 |
| [后续论文明确引用的仓库](https://github.com/JoeMarkWatson/uket_pred3) | GitHub API获取返回404，未取得，不猜测私有或删除原因。原CLC-UKET论文没有本次取得的对应代码库 |
| [官方数据访问入口](https://www.cst.cam.ac.uk/research/srg/projects/law) | 全库限符合条件研究者申请；本次未申请或联系他人。公开CLCmini为跨法院15案示例，不替代UKET全库，未下载充数 |

原2024任务为案件级四类win/lose/partly win/other；2026后续任务为claim级win/lose/other。后者附录24页明确将Withdrawn/Settled映射Lose，将程序成功映射Win。这不是同一版标签，也不是实体劳动法权利成立与否的充分判定。不能以某一版标签修正另一版结果。

2024论文讨论了从判决抽取事实可能遗漏程序细节，例如逾期、被告不应诉、费用申请所需行为。2026研究进一步审计结果提示与泄漏。两项发现说明需要核对输入和结果语义；不能据此断言所有源案例不可用，也不能拿基线失败证明环境探索必要。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 根据适用劳动法与仲裁程序，逐项判断劳动争议请求的处理结果 | 冻结劳动法、程序规则及历史判例未取得；案件日期跨年不能默认同一版本 | 2024预测集14,582案件或2026的33,158claims，均未本地取得 | 事实、claims由判决抽取；原始申请/证据包不在本轮材料 | 原版四类与后续三类不可互换；全文结论/理由不可进入公开输入 |
| 具体已读取的后续标注契约：Withdrawn/Settled | 和解或撤回的程序状态不能单由实体劳动法计算 | 没有具体患者式实例或案号可公开核验，本轮不编造事实/金额 | 若要预测程序处置，需要该事件的公开证据；若要审实体权利，则须独立gold | 后续契约规定Lose；这个值不是“原告没有实体权利”的gold |

| 类python的DAG | 具体数值 | 当前状态 |
|---|---|---|
| `scan(cases).explode(claims)` | 14,582案件与33,158claims来自两版研究 | 缺全库，不能核验join、独立实体数或每种任务N |
| `bind(law_version, claim_type, procedure)` | 原论文54种jurisdiction代码 | 跨类型总数不等于一个固定任务批量；规范未冻结 |
| `allowlist(facts, claims).audit_outcome_cues()` | 全量通过数未知 | 保留事实来源与程序证据，不能简单删关键词后声称无泄漏 |
| `sem_map(disposition).sem_filter(merits_success).count()` | 选中数未知 | merits_success需细分结果支持；不得用Win/Lose直接替代 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 缺实例不能给预测；若输入已明确和解，后续契约映射Lose只是状态映射，不代表复杂规范推理 | 固定区分实体与程序任务、核对必要事实，再检索同一规则；未知保持ABSTAIN，不能用常识猜结案 | 相同边界，无法凭探索补出未提供的和解事件 | ==识别待判断的是实体请求还是程序结果==→==核对适用版本、期限与程序事实==→==检索同一公共规范并比对条件==→输出有据细分结果；缺必要事实则ABSTAIN | `EmploymentClaimOperator(E_version, claim_type, procedural_state, factual_evidence, merits_rules, label_mapping, abstain)`；仅E编译、固定程序、Coding Agent与整批Agent使用相同来源 |

本轮没有模型运行、准确率比较、可运行公开快照或单轨迹提取。下一步是取得有授权的精确病例和代码，再确定具有足够数量的同类实体请求及版本；不将程序预测悄悄改为合规判定。论文原件在data/shared-environment-audit-20260908-v39，SHA256及失败收据在artifact/evidence/shared-environment-audit-20260908-v39/downloads.json。
