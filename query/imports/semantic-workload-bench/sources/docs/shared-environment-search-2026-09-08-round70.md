# Increment70：CASIE 坐标根因核验与开发视图

结论：CASIE 可加入 SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT 候选，累计4/10个独立数据湖。不是 VALIDATED，不证明 Agent 优势或长环境的实测必要性。原论文、完整作者仓库、博士论文已下载，见 round69；本轮完成真实输入—基础人工 gold 的全量对齐及开发视图。对严格要求“至少30页”的任务，本候选仅28页有效规范，不能算30页通过；这里依据用户允许的“长/复杂”及跨事件类型、实体类型、角色、窗口和realis规则判为复杂环境候选。

## 来源和根因

- [原论文](https://ebiquity.umbc.edu/get/a/publication/1312.pdf)：9页，SHA256 `df8a1770b6e909f1da7eaff34f9401b3a7b011964dbf31d5c6c0acfdfb433571`。
- [完整作者仓库](https://github.com/Ebiquity/CASIE/tree/2c8beef56d48e8de6599891c6a5e0e5f0d82e20c)：commit `2c8beef56d48e8de6599891c6a5e0e5f0d82e20c`；ZIP25,562,716bytes，2026entries，2019Git blobs全部核对；不是只下载README。
- [作者博士论文](https://ebiquity.umbc.edu/get/a/publication/1144.pdf)：178页；仅§3.1–3.4与§4.2–4.3为本任务环境，28个印刷页、5529words。不能把整篇178页当必要输入。PDF41–59及64–72覆盖对应章节；文字提取精确按标题截断。视觉抽查PDF51（印刷37）事件、角色、realis示例；未声称逐页视觉校验。
- 作者 `code/utils.py:cuthead` 与 `code/report.py:cuthead` 都规定 `index('<text>')+7`；`codecs.open`读取文本。按该规则从原source文件抽取正文，**1000/1000文档，31186/31186事件及论元span精确匹配，0错误**。JSON `content` 有33文档1095处不匹配。此前去前导空白的正则不适合作为坐标来源。本轮没有按gold逐条改坐标或正文。
- 论文 Data and Annotations：三位计算机科学标注者、多数投票、报告κ=0.81，覆盖事件、论元及讨论的realis/coreference。博士论文第12章明确Purpose subtype及CAPEC映射由系统自动生成。因此本视图只保留原基础类型、span、论元实体类型、角色及realis；丢弃external_reference、confidence、CAPEC-Meta及角色subtype，不把它们当人工gold。coreference不作为本轮评分任务。
- 版本边界：论文Table2 nuggets合计8470，当前仓库8485（+15），不是完全同版数值；本构造锁定当前commit。当前3903hoppers与论文事件合计3903相同也不足以证明每条版本一致。

## 三张任务表

| Query | 数据湖数据1：共享E | 数据湖数据2：真实items | 数据湖数据3：private gold |
|---|---|---|---|
| Q1：按CASIE规范抽取每篇新闻的五类事件及角色化论元 | 作者28页/5529词规范；包括事件边界、角色合法性及上下文窗口 | 原1000篇2017–2019新闻；开发视图991篇完整正文 | 8380事件触发span、22471论元span/实体类型/角色；无gold事件给模型 |
| Q2：在事件抽取后标注Actual/Generic/Other，列出文中陈述已发生的事件 | 同一规范中的realis及其事件定义依赖 | 同991篇；共享同一源实体集合，不另算数据湖 | Actual5201、Generic2069、Other1109；另1个General为INVALID_SOURCE_LABEL；不得并入三分类 |

Q1与Q2具有不同目标字段，属于同湖多任务；将五种event type各自过滤不再计为五个任务或五个湖。第二任务不能把抽取错误删掉，仅报分类条件准确率；端到端评价须包含漏提、多提与标签错误。若显式提供gold event作为输入，需另建annotation-given契约，当前未构造。

| 类python的DAG | 输入具体数值 | 关键节点gold规模 | 下游目标 |
|---|---|---|---|
| `scan(news).sem_map(extract_events_and_roles, E).explode('events').project(type, trigger, arguments)` | 991独立新闻 | 8380事件；22471论元 | 跨文章事件清单及类型统计：Databreach1753、Phishing1532、Ransom1562、DiscoverVulnerability2122、PatchVulnerability1411 |
| `scan(news).sem_map(extract_events_and_roles, E).explode('events').sem_map(classify_realis, E).filter(realis == 'Actual').groupby(document_id)` | 同991新闻；事件节点不能当8380独立新闻 | 8379有效三分类标签+1无效源标签 | 按原gold目标应选5201事件mention，非5201次独立网络攻击；无效标签单列，不给其杜撰答案 |

具体例子来自源`2075.json`（Gannett钓鱼相关新闻，开发暴露）：`access[323:329]`的原gold为`Databreach/Other`；论元包含`sensitive personal data[355:378]`，role=`Compromised-Data`。因此这一mention不进入Actual清单。同篇`sent to[1257:1264]`为`Phishing/Generic`，也是不进入Actual清单。这里只给出源标签和评价目标，尚未执行任何模型。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| Q1目标：`access → Databreach`，敏感数据span→Compromised-Data；实际能否得到待运行 | 将完整必要正文和同一E交给固定sem_map；返回schema JSON；程序验证span、枚举及角色。允许同资源固定检索、缓存和共享预处理 | 相同gold目标；不预写“Agent正确而LOTUS错误” | ==检索五类事件定义及论元上下文规则==；==查该类型允许的角色及实体类型==；在正文提取候选并用span工具核验。这里是可观察动作设计，不是已采集轨迹或私人思维链 | `extract(text, compiled_schema)`；schema分派、候选提取、角色约束、span核验、预算/ABSTAIN；只能在实际单次轨迹后自动合成冻结 |
| Q2目标：`access → Other`，`sent to → Generic`；两个mention均不进入Actual；实际输出未知 | 固定realis sem_map获得同样正文与E；保留语境和嵌入事件，输出每个mention标签，再确定性filter；可用固定程序一次从E编译规则 | 相同标签目标；无预设准确率或提速 | ==查Actual/Generic/Other定义及示例==；==检索新闻内该mention的否定、未确认或一般性语境==；返回标签及可核查证据 | `classify_realis(context, event, policy)`；范围识别、一般陈述/具体事件判定、规范标签映射、校验；不要把“遇到no便Other”写成万能规则 |

`==...==`只表示拟观察的工具/证据步骤，未实际运行。强对照必须包含完整E静态调用、固定检索程序、仅E一次编译、Coding Agent及可批内共享缓存的Data Agent。较复杂E仅支持研究假设；如果仅E编译已同样有效，应保留该结果，不能主张轨迹学习必要。

## 构造和验证

- `artifact/evidence/shared-environment-audit-20260908-v70/audit.py`及`offset-audit-private.json`：全1000文档三种正文坐标审计。
- `build_inspection.py`：从公开输入与全论文/博士论文进行12词、至少65字符的词面重叠筛查，排除9文档；不是人工按结果挑样。此筛查不证明无近重复或训练污染。
- `data/shared-environment-audit-20260908-v70/inspection-v1/`：公开文件只给随机化文档ID及正文、任务、规范；私有gold和source映射分开。此目录分离不是OS隔离。
- `verify_inspection.py`及`verification.json`：**996assets精确集合/bytes/SHA256、991唯一ID、8380事件与22471论元逐项源对等、全部span精确校验PASS**。
- General1原标签保留为INVALID_SOURCE_LABEL；Q1基础事件任务可用，Q2不能宣称完整无异常gold。无全量code test，因为未改运行器；上述独立数据审计已执行。
- 尚缺：任务运行/评分适配、独立实体分组与确认集、环境消融、模型和成本测量、许可及新闻再分发权利确认。当前是本地研究构造资格，不是发布许可或生产部署资格。
