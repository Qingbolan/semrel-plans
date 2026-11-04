# 已见 benchmark 的混合查询与关系算子计划图

本表整理截至 2026-10-12 已在本地看到的查询原件。“这两天”按本轮总结窗口理解；来源主要是 9 月 8 日查询采集和 9 月 15 日五湖构造，不声称 10 月 10–12 日新增实验。每条查询都保留原文、来源和一张逻辑计划图。

**最适合直接研究混合执行的是 SemBench 中的语义谓词＋结构过滤／聚合／连接。UDA-Bench 和 QUEST 则主要体现“原文抽取为关系＋SQL”；五湖体现“有共享资料的语义标注＋批量关系查询”。这三类应分开比较。**

共索引 **785 条记录和计划图**：SemBench 70、UDA-Bench 608、QUEST 列表中的 84、五湖派生 20、源码流程示例 3。这里的数量是查询文件/语句/派生任务数量，不是独立语义任务、通过候选或已执行实验数量。

| 类别 | 边界 |
|---|---|
| SemBench | 原生NL；人工重建逻辑树。仅Scan/Project接语义分类的条目标为弱结构组合。 |
| UDA-Bench | SQL按AST保留结构；SExtract为分析补充。已结构化表上执行时，本身就是纯SQL。 |
| QUEST | 源列表为伪SQL；保留未加引号、拼写及截断，不自动修复。 |
| 五湖 | 5个语义主任务及其筛选、聚合、拒答派生；不是20个独立gold任务。 |
| Palimpzest / LOTUS | 已读源码实现示例；本次未运行，不等于原论文完整benchmark。 |

SemBench 70条中，49条在语义步骤之外还有过滤、聚合、集合运算、连接或截断等结构组合；21条只有扫描/投影接语义步骤，单独标为弱结构组合。这个划分描述计划形态，不是科学有效性判定。

## 如何读图

叶子在下、输出在上；箭头是数据依赖。共享分支以DAG呈现，展开共享输入后就是关系算子树。图是语义保持目标下的一种逻辑表达，没有声称最优顺序、物理实现、实际EXPLAIN或实测代价。

| 标记 | 意义 |
|---|---|
| R · Filter / Project / Join | σ选择、π投影、⋈结构连接 |
| R · Aggregate / Distinct / Sort / Limit | γ分组聚合、δ去重、τ排序、截断 |
| R · Union / Intersect / AntiJoin / Unnest | 集合并/交、反连接、集合列展开 |
| S · SFilter / SMap / SExtract | 语义真假判定、生成属性、原文关系抽取 |
| S · SJoin / SLeftJoin | 二元语义匹配；Left保留未匹配左行 |
| S · SAggregate | 跨行语义归纳，与结构COUNT/SUM不同 |
| Lookup / ExternalSearch / Transform / ResultBundle | 辅助依赖或输出组装；不是都能直接翻译成SQL关系算子 |
| Unresolved | 源查询不完整，图不能作为可执行计划 |

## 全部查询入口

| 查询集 | 记录数 | 逐条原文与图 |
|---|---:|---|
| sembench-animals | 10 | [打开](sembench-animals.md) |
| sembench-cars | 10 | [打开](sembench-cars.md) |
| sembench-medical | 10 | [打开](sembench-medical.md) |
| sembench-mmqa | 16 | [打开](sembench-mmqa.md) |
| sembench-movie | 10 | [打开](sembench-movie.md) |
| sembench-ecomm | 14 | [打开](sembench-ecomm.md) |
| uda-art | 86 | [打开](uda-art.md) |
| uda-cspaper | 86 | [打开](uda-cspaper.md) |
| uda-finan | 86 | [打开](uda-finan.md) |
| uda-legal | 86 | [打开](uda-legal.md) |
| uda-med | 132 | [打开](uda-med.md) |
| uda-player | 132 | [打开](uda-player.md) |
| quest-wikitext | 30 | [打开](quest-wikitext.md) |
| quest-lcr | 27 | [打开](quest-lcr.md) |
| quest-swde | 27 | [打开](quest-swde.md) |
| derived-five-lakes | 20 | [打开](derived-five-lakes.md) |
| implementation-examples | 3 | [打开](implementation-examples.md) |

## 优先阅读的组合

- Animals Q8：两模态语义筛选 → 两次Union → Intersect；是集合逻辑与语义判断交织的清楚例子。

- Movie Q4：结构筛选指定电影 → 语义情感映射 → SUM/COUNT；分母必须保留全部目标评论。

- Movie Q10：逐评论语义评分 → 按电影AVG → Sort；自然语言与现有gold SQL存在明确冲突。

- Ecomm Q10/Q11：价格筛选、图文属性抽取、多路等值Join；可以比较SJoin与先SMap后结构Join，但质量等价尚未验证。

- Ecomm Q14：价格筛选＋白袜图片筛选＋图文匹配评分＋每商品Top1；不能改成全局LIMIT 1。

- MMQA Q5：抽取演员集合 → Unnest → COUNT DISTINCT film → HAVING覆盖16部电影，体现全称量词。

- 五湖Q3：语义输出 → 去重展开 → COUNT DISTINCT实体，同时保留全批coverage；标签数不等于独立实体数。

## 需要保留的差异

SemBench各条图旁记录了已观察到的NL/gold SQL冲突：Animals并列赢家、Movie缺LIMIT/评分来源、Medical Q5/Q6/Q7、Ecomm价格单位/候选匹配范围等。图默认跟随原NL；原gold不能未经修订直接评估这些计划。UDA的部分Med SQL使用未绑定表限定符，逐条标明。QUEST残句保留为不完整计划。

结构谓词如果只依赖已有价格、日期、电影ID，可以考虑前推减少语义调用；依赖语义生成属性的过滤不能提前。SJoin改为属性抽取后Join、抽取缓存、聚合共享都是待验证实现选择，不从图推断准确率、K或成本收益。

## 未纳入混合查询计数的材料

TOFFEE/DataSpace已有SQL示例主要是schema探索后执行确定性SQL，Agent参与不自动产生行级语义算子；不为凑混合任务加语义节点。DocETL的本地评测脚本不足以恢复全部原始流程；没有逐条编造。单纯语义分类仍可登记，但标记scan_projection_only，不把扫描和投影包装成复杂结构组合。ZenDB/UQE的同源Bench-U副本不重复计算。28候选的判定仍为0 Strong / 5 Partial / 23 Reject，本图册没有升级任何候选。

## 追溯与验证

[机器可读全部计划](../../artifact/evidence/benchmark-query-plan-atlas-20261012/plans.json) · [来源文件哈希](../../artifact/evidence/benchmark-query-plan-atlas-20261012/sources.json) · [结构与链接检查收据](../../artifact/evidence/benchmark-query-plan-atlas-20261012/validation.json) · [生成脚本](../../artifact/query-plans/build_atlas.py) · [已有57条原题＋20派生精选稿](../benchmark-mixed-query-plans-2026-10-12.md)

SemBench采集固定commit：`c814e3807e72d4cf876b852b17e77f3cc94575c2`；Bench-U：`f2da981b5d37c058345f27f23c7979eb44697f0c`。其他本地源码按本次文件SHA-256追溯，不以旧README版本代替当前字节。SQL AST解析使用sqlglot 30.22.0（临时工具依赖）。验证覆盖唯一ID、70/608清单覆盖、图节点/边连通与无环、源文件存在及哈希；未运行SQL/模型或图形渲染器，未核验语义正确率、许可与科学有效性。
