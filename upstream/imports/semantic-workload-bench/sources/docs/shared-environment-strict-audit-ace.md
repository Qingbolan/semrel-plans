# ACE / COMPACT：合同合规场景

**Reject 本目标的真实共享环境批任务。** 合同来源真实，但场景由模型生成，标签由模型校验；抽查人工认可不等于全量独立人工gold。现成任务给每条记录选定条款集，完整共享合同及来源映射未发布在本仓库。多条款交互在结构上接近HSCodeComp的候选导航，但不满足真实批量与gold要求。

## 表1：入场审计

| 数据湖 | 论文 / 仓库 | E组成与规模 | 记录与N / 固定q | gold | C定位 | D完整E静态不足 | 分支与K | G泄漏/可回答性 | H下载 / Verdict |
|---|---|---|---|---|---|---|---|---|---|
| ACE | [COMPACT原论文32页](https://aclanthology.org/2026.eacl-long.377/)；[官方完整repo](https://github.com/FujitsuResearch/Fujitsu-Assessing-Compliance-in-Enterprise-Dataset) | 论文源633合同/26协议类型；实际文件为每行clauses字典，没有完整合同或source_contract_id | 实际train3600/test1100，共4700；判场景Compliant/Non-Compliant/Not-Applicable | GPT-4o生成，Claude Sonnet4校验；50条法律专家抽查46条label认可；不是4700人工判案 | 抽20条已打开条款/情景/gold，完整共享E闭合0；条款片段存在不等于完整法源认证 | 论文主要SFT蒸馏比较；未排除固定条款图预处理、完整E、固定检索多步程序 | 6类图关系不等于执行家族K；K未知 | gd_tr及全部DeepSeek字段私有；选定条款为原任务允许资源，改成合同探索时须与oracle选证据区分 | 原PDF、完整repo与全train/test已下；完整633合同映射未获得；CCBY4声明，源许可另核。Reject |

A固定三分类成立。B单一共享长E未认证；逐行条款集不是单一完整合同。C0/20完整闭合。D/E未验证。F合成场景，不是自然发生的合同执行案例；4700不能自动视为同一合同下N。G必要事实及完整条款闭合未查证，源文档隔离无法由当前字段确认。H已取得发布物，但缺完整合同关联键、构造实现和graph资产。633/26为论文来源统计，未从仓库反推认证。

## 表2：Query × 具体资产

| Query | 数据1：`test.json.scenarios[].scenario_text` | 数据2：`clauses` | 数据3：私有gold/边界 |
|---|---|---|---|
| q1 对指定条款判断场景合规，输出三标签；证据无法确定另报UNKNOWN | 第0行ConvergTV在新平台StreamSphere播放节目，未置首页、通知非正式；场景声明播放在地域及期限内 | evidence_5允许现有及未来渠道分发；节目2年，自2012-11-15起；缺完整合同及原表结构 | `gd_tr=Compliant`；是发布参考，不是本次任何模型输出 |
| q2 筛出不受给定条款支配的场景，输出Boolean | 全1100情景，同一输入规范 | 同一行给定条款 | `gd_tr == Not-Applicable`共320；从同一gold派生，不是新独立任务数据 |
| q3 筛出违反给定条款的场景，输出Boolean并聚合数 | 全1100情景 | 同上 | `gd_tr == Non-Compliant`共400；Compliant380；不能将三类分别计成3300个案例 |

第0行的合同依据允许未来distribution outlets，未在该条款中要求首页推荐或正式通知。因此“缺首页曝光”本身未违反给定许可条款；但这仅说明发布片段任务，不能由此推断完整合同没有其他通知义务。案例是生成场景，不是发生过的ConvergTV争议。许可起止时间和地域属于场景给定事实，未外查真实性。

实际数据结构与README加载示例不同：顶层为`{'scenarios': [...]}`，不是直接list；初次按README取`d[0]`失败KeyError，已改本地只读审计路径，无需运行或修改作者代码。论文3240train/360val合并为发布3600train，repo明确无独立val，不擅自重划分。

## 表3：类Python DAG

| 类Python DAG | 具体数值 / 性质 |
|---|---|
| `rows = json_load(test)['scenarios']` 普通 | 1100行 |
| `public = project(rows, ['clauses','scenario_text'])` 普通 | 去除gd_tr；train还必须排除所有DeepSeek输出 |
| `facts = sem_map(scenario_text, extract_action_time_scope)` 语义 | 第0行：新渠道、2年许可、地域内、低曝光、非正式通知 |
| `duties = sem_map(clauses, parse_permissions_exceptions)` 语义依赖给定片段 | 第0行许可未来渠道；未得到完整文档，不能补出独立通知义务 |
| `y = sem_map(facts,duties,compliance)` 关键语义 | 第0行发布gold Compliant；各方法结果待测 |
| `count = filter(y == 'Non-Compliant').count()` 普通 | gold目标400；非模型count |

## 表4：四路推演（未运行，不保证Agent更优）

| 臂 | 预期执行结果 | 预期执行过程 | 候选operator |
|---|---|---|---|
| LOTUS静态仅任务+场景 | 未测；情景本身引用条款，第0例可能已有充分线索，不能预设必错 | 单次语义分类；区分场景自述合同允许与真正规则证据 | 固定prompt；须审计词面捷径 |
| LOTUS静态+完整E | 当前只能测给定条款集臂，不能冒充完整合同臂；第0例目标Compliant | 读取全部给定条款→固定合规分类；另可一次预处理权限/例外表 | 固定解析+字段检查，可能覆盖多数路径 |
| 逐记录Data Agent | 未测；缺完整合同不能声称找到了所有相关例外 | ==检查许可期限及地域==→==寻找未来渠道许可与通知义务==→核对场景事实→标签或UNKNOWN | `parse_scope → check_permission → check_exceptions → decide`假设结构 |
| 批处理Data Agent | 共享片段解析可缓存；天然大批摊销条件未成立 | ==对相同条款集一次解析==→==按语义事实选权限/例外分支==→逐案判定 | 内容寻址条款缓存+固定语义判定；不读取训练教师输出作为确认E |

ρE为条款/图解析，ρP为共同事实抽取，ρG为权限/时间/例外分支，ρR为情景特定事实；比例及K未测。论文构图本身已有定义、依赖、例外等规则化步骤，因此env-only预处理是必须保留的强对照，不能从存在多跳推出逐案Agent必要。

## 实际统计与证据局限

- test精确条款字典902组，最大相同字典6行；train2025组，最大10行。精确字典组不是完整合同组，不能据此推断每合同最大N。
- test700/1100行只有1种不同的条款字符串；字符串内部可含多个拼接条款，因此不据此断言没有多条款推理。另2/3/4种分别275/78/47。
- train独特scenario_text2949、test1043；同一情景可以配不同条款集用于Not-Applicable，重复文本不自动是重复任务，也不增加真实事件数。
- 20哈希抽样给定条款总字符范围53–15405；只证明片段大小，未认证长共享环境必要性。源合同ID/条款原始位置未给，无法完成20条原合同闭合核验。

收据：[source](../artifact/evidence/shared-environment-strict-ace/source.json)、[全量字段与分组统计](../artifact/evidence/shared-environment-strict-ace/data-audit.json)、[20条原样例](../artifact/evidence/shared-environment-strict-ace/sample20.json)、[20条范围审计](../artifact/evidence/shared-environment-strict-ace/sample20-scope-audit.json)、[最大test相同字典组](../artifact/evidence/shared-environment-strict-ace/largest-exact-test-group.json)。数据在`data/shared-environment-strict-ace/`，无作者代码执行、模型运行、调参、新split、质量/成本测试。训练集自带教师文本不是本项目采集的真实执行轨迹，不将其称为单次Data Agent示范。
