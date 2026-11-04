# 第69增量：CASIE网络安全新闻，同湖多任务与完整规范来源

合格保持3/10。CASIE提供一个贴近业务的多任务候选：批量安全新闻→事件库存→参与者/受影响系统/漏洞角色→事件状态→同一事件合并。尚需解决公开文本与标注坐标、人工字段范围，未列为已满足全部条件的数据湖。

[原AAAI论文](https://ojs.aaai.org/index.php/AAAI/article/view/6401)9页1579905bytes已下载；AAAI端连接中断、旧实验室路径404后，从作者页面实际PDF链接https://ebiquity.umbc.edu/get/a/publication/1312.pdf取得，SHA256 df8a1770b6e909f1da7eaff34f9401b3a7b011964dbf31d5c6c0acfdfb433571。标题与作者核对一致。

[完整作者仓库](https://github.com/Ebiquity/CASIE)commit 2c8beef56d48e8de6599891c6a5e0e5f0d82e20c，25562716bytes ZIP/2026条目CRC通过，非截断tree2019blob全部Git SHA1一致。SHA256 f05f191b8d88da9f2172123c7e6ff537d039a89c6459c5d3e88a8a5f3b6c9fb0。含1000source/1000annotation文件及代码，未执行作者代码。

另取得[作者博士论文](https://ebiquity.umbc.edu/get/a/publication/1144.pdf)，178页1648017bytes，SHA256 8efd29bfffcb45daeffab29df9be196ff306f7b6d9ab9ec63fa48095db888b12。必要候选规范是第3章原五事件schema（排除§3.5 DDoS扩展）及§4.2–4.3标注规则：印刷页27–45、50–58约28页，按标题精确截取5529词47581字符。**不是178页都必须读**；片段含表格，pdftotext布局保留，尚未完成视觉表格完整性校验。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold/待核字段 |
|---|---|---|---|---|
| 识别安全新闻中的数据泄漏、钓鱼、勒索、漏洞发现、补丁事件，建立事件库存 | 同schema与最短充分nugget规则 | 1000真实新闻source文件；JSON content是经过处理的正文 | 角色与实体类型规范 | 8485事件：Databreach1786、Phishing1564、Ransom1585、DiscoverVulnerability2132、PatchVulnerability1418 |
| 为事件提取攻击者、受害者、漏洞、系统及补丁等角色，建立安全事件图谱 | 同schema的20类argument实体/属性及按事件定义的角色 | 新闻上下文与给定事件（若拆成独立任务需明确annotation-given） | 标注规则限制argument候选在含事件nugget的前后相邻句范围 | 22701论元角色记录；26种role名称，不是把20种实体类型与role混为一谈 |
| 区分实际叙述、泛指和其他状态，防止把一般攻击说明当实际事件报告 | 同realis规则 | 同全文及给定nugget | 状态与共指约定 | Actual5253、Generic2106、Other1125、另1条General原值须核，不默默改名 |
| 按事件共指合并提及，减少新闻内部重复事件统计 | 同§4.3.5规则 | 同全文/事件提及 | 跨句事件身份线索 | 3903hopper；发布JSON还含自动扩展字段，hopper人工来源需逐层确认 |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `docs=join(source,annotation.sourcefile)` | 1000文件名均可连接。原source带title/source/date/text包装，与JSON content原字符串当然不同；不能把这层差异当丢失正文 |
| `events=sem_map(doc,E.nugget_rules)` | 8485原事件；没有本次预测 |
| `args=sem_map(doc,given_events,E.roles)` | 22701原论元；有规则规定候选句距，不能把未标任意远程信息当漏标false |
| `realis=sem_map(doc,given_events,E.realis)` | 原三类+1条General异常，后者在10002.json/E对应nugget Apply[1739,1744) |
| `clusters=sem_map(doc,given_events,E.coreference); groupby(cluster)` | 3903原hopper；完整人工层归属及规范对齐尚未确认 |
| `score(predictions,private_targets)` | 33文档1095处nugget/argument对JSON content切片不一致；不能直接运行精确span scorer后归咎模型 |

| 预期关键语义算子交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 2075.json的access[323,329)原gold为Databreach/Other，背景句表示没有迹象显示访问/取得敏感资料；不可误作实际泄漏 | 完整同规则语境映射→事件类型及realis；固定程序允许否定范围检查 | 相同目标，未预设更好 | ==核no indication的作用域；查Other与Generic区别；保留作者报告状态==→类型/状态 | nugget发现→局部及全文否定范围→realis→事件库存；未训练或提取 |
| 同文faked emails→Tool、an employee→Victim；泛指钓鱼说明的sent to/entice为Generic | 给定nugget的固定角色候选与语义映射，依据相同句距规则 | 同一目标，未预设跨工具探索必要性 | ==区分泛指攻击方法与具体Gannett事件；查角色与argument类型；按原文返回span==→角色及事件图 | 句距候选→实体类型→事件角色→状态→图索引 |

正文一致性继续核查：提取source的text标签并仅规范化空白后，829/1000与JSON content相等，171仍不等。坐标错误例10059.json中held to ransom标[36,50)，按content切出eld to ransom加尾空格；未自行平移/重写gold。精确处理应找到作者原文转换规则，而非按gold搜索命中补坐标。

人工与机器层必须分开：博士论文§4.5称三位计算机科学背景标注员、多数票选标注，报告token-level Cohen kappa0.81。发布论元中却有4613 external_reference、2297 role.confidence、1742 CAPEC-Meta及555 role.subtype；论文系统输出说明也含这些字段。不能因为它们放在annotation目录就称人工gold；当前优先核定nugget/type/realis/role基础层，排除扩展字段，且不把系统置信度提供给被测模型。

同一湖的事件识别、角色赋值、状态判定和共指是不同语义任务；仅换五个事件类型筛选条件不算五个任务。这些都需冻结各自输入（尤其给定事件与否）、gold视图与必要E片段。5529词schema/规则的实际使用深度与简单环境编译对照尚未实测；不声称Agent胜出。

来源代码/数据和新闻原文/学位论文许可未全面核验，公开下载不等于可统一再分发。没有新模型/作者代码执行、新工程测试（0）、prompt/种子/预算/缓存/确认split或commit。脚本/下载失败和成功收据/全量审计位于artifact/evidence/shared-environment-audit-20260908-v69，源位于data同名v69。下一步核文本转换和基础人工标注层，以决定是否可构造多个任务，而不是先计数。
