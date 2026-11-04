# 第二十三增量：UDRP事实边界与裁决标签核验

继承第22轮原论文、152页官方WIPO解释材料及作者Zenodo归档。完整归档仍在同一session11183下载，最新返回270,532,608bytes/843,037,756bytes；没有重启，尚不能声称完整仓库下载完成。审计只消费第22轮已完整接收、CRC通过的近年分片。

`artifact/evidence/shared-environment-audit-20260908-v23/audit_sections.py`按source=WIPO、date字符串=2024选取2028案，**不根据预测难度或gold筛样本**。输出统计及逐案诊断，不生成公开评测快照。

实际结果：1914 Transfer、79 Complaint denied、30 Cancellation、2 Transfer/denied混合、1含协同意见的denied、2 Request granted。1746案单域名，其余多域名（最多138个）。严格四标题及顺序检查通过1966案、失败62案；失败表示解析未覆盖，不能判断无事实。通过者事实+主张113–6708词，中位523.5。

在1674个“单域名+纯Transfer或Complaint denied+严格边界成功”诊断子集中，1670与简单结论正则一致；这个结果仅为解析一致性，不是金标准准确率，更不是用户所需模型效果。四处不匹配已检查：

- D2024-0061：换行使`Complaint is denied`匹配失败。
- D2024-1232：PDF文本`transferr ed`词内空格使匹配失败。
- D2024-1705：metadata Transfer，但裁决正文明确Cancellation。
- D2024-2133：metadata Transfer，但裁决正文明确Cancellation。

后两案已从[WIPO官方D2024-1705](https://www.wipo.int/amc/en/domains/search/text.jsp?case=D2024-1705)和[WIPO官方D2024-2133](https://www.wipo.int/amc/en/domains/search/text.jsp?case=D2024-2133)下载完整原PDF，分别137592/226735bytes。存于`data/shared-environment-audit-20260908-v23/`及哈希收据。不能用“申请人获支持”作为“域名被转移”的同义标签；撤销和转移应分开。也不能仅凭这两处差异丢弃整个数据湖，应以正式Decision核验gold，并保留差异表。

## 三张表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 在冻结UDRP环境下，逐案输出正式救济类型，再筛选Transfer | 第22轮已下载WIPO Overview3.0及所附政策/细则152页 | WIPO2024标记2028案；事实、主张、程序背景尚需完整输入契约 | 1966案四个标题顺序可解析；不能将§6分析/§7决定作为输入 | 元数据状态+文末裁决分别保存；两者有实质差异，不静默覆盖 |
| D2024-1705：sipchemgroup.com | 三要件与请求救济的规则边界 | SIPCHEM商标2019年、域名2024年，正文含冒充公司事实及双方主张 | 原官方PDF3页已下载 | 正式救济Cancellation；不是metadata的Transfer。事实是否完整包含请求救济尚待核 |

| 类python的DAG | 具体数值 | 输出/限制 |
|---|---|---|
| `scan(WIPO2024).parse_sections(strict)` | 2028→1966成功/62待解析 | 不能剔除62后声称全批覆盖 |
| `separate(facts, contentions, procedural_context, private_decision)` | 1746单域名；多域名需不同schema | 主张含过去判例引用可合法保留，不能按关键词删掉 |
| `sem_map(udrp_outcome,E).sem_filter(outcome==Transfer)` | Cancellation必须不选中 | 模型未运行；请求救济缺失时不得猜测transfer/cancel |
| `score_against_verified_formal_decision()` | 本轮查出2条实质metadata差异 | 未完成全量gold审核，不报告审批准确率 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| D2024-1705的正式结果目标Cancellation；若允许输入缺少请求救济，不能保证可推导，应ABSTAIN | 在同样事实/程序/请求及E上固定抽取三要件与救济；禁止读取metadata和Decision | 同一目标及同样的信息限制，Agent不能凭探索本案答案补足 | ==确认必要的请求救济是否公开可用==→==评估三要件==→按请求/规则输出；缺失则ABSTAIN | `UDRPOperator(elements, requested_remedy, allowed_remedies, outcome, evidence_gap)`；不会把三要件成立自动转换为Transfer |

另有19案事实/主张中出现疑似结果措辞。本轮人工读取首例D2024-0098，发现是当事人引用前案D2023-2034的判词，并非直接泄漏本案结果。这说明关键词命中只能送审，不能自动删除或排除。原文需要保留陈述来源和时间。

完成的是结构与标签来源审计。新增工程测试0，无模型/作者代码运行、无独立确认；完整归档还在下载。下一步继续同句柄，检查请求救济字段可得性、正式裁决全量映射和剩余标题格式，而不是制造一个全为容易Transfer案的子集。
