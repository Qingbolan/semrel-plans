# 第三十四增量：GAO采购异议来源全量核验

**累计1/10，本来源暂不计入。** 已下载GAO5k完整作者仓库及全部三个LFS数据对象，并取得一篇原始采购异议经济学论文。但两者作者、时间范围和数据来源不同，不能把它们组合冒充论文对应的复现材料。尚无长共享规范、公开事实输入与独立结果的可执行构造。

## 下载及出处关系

| 材料 | 本次事实 |
|---|---|
| [GAO5k作者仓库](https://github.com/KMisener90/GAO-Bid-Protest-Dataset) | commit `fc0791030c6bcc2d4c4368a777ab58df4f198f6d`；6blob Git SHA1全通过，ZIP CRC通过，3个LFS对象分别按pointer大小/SHA256验证 |
| 完整LFS JSON/CSV/XLSX | 177,509,880 / 103,643,498 / 46,106,342 bytes；不是只下载Git LFS指针；三个对象均完成 |
| [原研究 Choose Your Battles Wisely: The Consequences of Protesting Government Procurement Contracts](https://www.aeaweb.org/conference/2020/preliminary/paper/AhGRDsyA) | Canayaz、Cornaggia、Cornaggia，2019-12-27稿；56页PDF、1,542,189 bytes已下载，研究2005–2016 FOIA异议数据及后续合同经济结果；**不是GAO5k论文**，未找到其对应完整复现仓库 |
| [官方2006异议指南](https://www.gao.gov/assets/gao-06-797sp.pdf) | 普通下载HTTP403，未取得PDF；即使取得也不能自动绑定全部后续年份实体规则 |

数据发布者声明CC-BY4.0并排除对原始政府作品主张权利；来源许可分开记录。作者README定位为RAG裁决文本库，未声明其为经审定的逐案预测benchmark。它明确缺完整FAR等法规文本。没有将研究论文的FOIA数据和GAO5k统一计数。

收据/URL/SHA256见`artifact/evidence/shared-environment-audit-20260908-v34/downloads.json`；原始资产在data同名目录。README所称约5700、2017–2025不是本次统计替代物。

## 本次实际计数

| 统计项 | 实测 |
|---|---:|
| CSV行数 | 7,004 |
| CSV唯一(B-Number, Published Date)键 | 5,659 |
| 出现多行的键 | 1,232 |
| 空Merged Details行 | 1,182 |
| JSON分块行数 | 257,998 |
| JSON唯一同类键 | 5,607 |
| CSV含BACKGROUND/含DISCUSSION标题行 | 3,863 / 3,701 |

一个B-Number单元格本身可能包含多个程序案号；键数不是已经消歧的独立招标数量。JSON与CSV键数不同，不直接互换。日期字段实际含2009–2016旧案，超出README范围；未把所有旧案自动判成错误或删除。CSV只有名称、案号组合、日期、正文和空列，没有现成独立裁决标签。正文含网页导航、Highlights、DIGEST及直接结论，不能原样给模型预测。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 按同一冻结采购法规和异议规则，逐案判断异议是否应获支持 | 完整共享FAR/异议规则尚未下载并绑定版本；不能用裁决库本身替代所有规范 | 5,659个CSV案号日期键，尚需去重和主体/招标分组 | 每次采购的RFP及资格/评价材料可能是必要输入，不能假设全部在公开事实摘要内 | 尚未提取，正文含真实裁决但无独立标签字段 |
| KE System Services，B-423881/B-423881.2/B-423881.3，2025-12-22 | interested-party程序条件与最低价技术合格采购规则 | 公司抗议陆军厨房排烟罩维护合同授予Xenturis | 原文称其自身技术不合格且未挑战该评价；完整RFP/投标材料未取得 | 原文结果dismiss；不能把程序驳回当作被诉采购实体合规False |

| 类python的DAG | 具体数值 | 当前状态 |
|---|---|---|
| `scan(csv).resolve_duplicate_case_keys()` | 7,004行/5,659键/1,232重复键 | 仅统计，尚未选择保留版本 |
| `split(background, claims, private_digest_decision)` | 3,863行含BACKGROUND、3,701含DISCUSSION | 标题命中不保证完整/无泄漏，尚未构造 |
| `join(frozen_rules, solicitation_inputs)` | 未建立 | 同一规则可共享，但每案必要RFP不一定共享 |
| `sem_map(protest_disposition).sem_filter(sustained)` | gold支持总数未知 | 必须区分dismissed/denied/sustained等程序含义 |
| `project(case_id).count()` | 不使用257,998分块数作N | 无预测或评分结果 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| KE示例参考dismissed，实际未运行；公开事实包未构造 | 固定先审资格/时限/程序，再按相同RFP与共享规则审查实体，允许固定分支、检索与缓存 | 同参考，不能预言优势 | ==识别异议主体与自身技术评价是否受到挑战==→==核对interested-party条件==→必要时==读取公开RFP与评价依据==→输出程序/实体结果或ABSTAIN；不读当前DIGEST/结论 | `BidProtestOperator(E_version, solicitation, attributed_facts, standing, timeliness, merits, abstain)`；不同RFP不能伪装为同一个共享E，程序标签不能折叠为实体违法 |

目前这是一组值得继续构造的真实来源，但尚不满足原论文与对应仓库、长共享E、独立gold和必要输入同时可追溯的要求。不因另有论文就冒充完整复现，不因数据量大就计为合格湖。无模型调用/作者代码执行/新工程测试，全部样例读取仅开发暴露。
