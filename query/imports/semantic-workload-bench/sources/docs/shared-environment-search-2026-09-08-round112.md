# 第112轮：STAC原生Glozz与JSON版本审计

结论：发现真实发布版本差异，不能直接将两种导出互换。保持7/15，未构造新合格湖。

原论文、完整46页规范及三份作者发布ZIP均复用[111轮](shared-environment-search-2026-09-08-round111.md)，没有重复下载或改写源。此轮直接解析Glozz XML/.ac正文，对照完整作者JSON。统一仅涉及文件名与关系名中的连字符/下划线，未改关系语义。源局由真实目录获取，未再按JSON对话ID猜测。

## 实际结果

| 项目 | 纯语言 | 带游戏事件 |
| --- | --- | --- |
| 原生Glozz实际游戏目录 | 41 | 45 |
| JSON EDU文本与Glozz完全一致 | 11431/12588 | 44398/44399 |
| JSON关系与Glozz方向/标签一致 | 11143/12271 | 43050/43058 |
| JSON CDU成员一致 | 1302/1450 | 7651/7651 |
| 原生关系数 | 11143 | 43059 |
| 原生schema数（尚未过滤类型） | 1303 | 7693 |

纯语言Glozz缺少pilot02、s1-league3-game3、s2-league4-game2、s2-leagueM-game4四局。JSON中111段对话未建立单一源局的文本映射。所有11143条原生纯语言关系均在JSON中准确出现；额外1128条JSON关系不能据此认定为错误，而是缺少同版本原生对应。

游戏事件版所有2593段都能映射到单局。发现8条JSON关系差异（6条类型变化、1条target变化、1条无对应原生关系）和1处EDU文本差异；另有2条原生关系不在JSON。所有7651个JSON CDU在原生中成员一致；原生额外42个schema的类型/范围尚未审计，不直接称为缺失CDU。

例：pilot01同一对语段“so it's OK.”→“But I had to dig deeper than I wanted.”，同一rel_id的Glozz类型为Result，JSON为Contrast。不能让模型预测后选择更匹配的一版gold，必须在运行前冻结版本或排除该源记录。

## 按要求的三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量恢复多人对话关系，筛选澄清与回应边 | 纯语言JSON1137段；对应原生仅41局 | 46页共同标注规范 | 已分段EDU、speaker、顺序；默认隐藏人工addressee/CDU/关系 | JSON12271关系；原生11143条同向同类对应，额外范围待冻结 |
| 核验pilot01回应类型的版本变化 | so it's OK. | But I had to dig deeper than I wanted.及完整对话上下文 | Result/Contrast规则与来源版本；版本对账材料不提供给模型 | situated Glozz=Result，JSON=Contrast，均是作者来源但不相同 |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold |
| --- | --- | --- | --- |
| `dialogues.sem_map(discourse_graph,E).explode(edges).filter(type=='Clarification_question').project(source,target)` | 1137原始JSON段，尚未形成冻结可评分集 | 带CDU的关系图 | 原始JSON456澄清边；不能宣称原生41局也有相同计数 |
| `dialogues.sem_map(discourse_graph,E).explode(edges).groupby(type).count()` | 同一语义图复用 | Result/Contrast等 | 上述版本差异会改变类别计数，必须先固定版本 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 对冲突例不提供混合gold目标；实际预测未知 | 冻结规范/输入后固定sem_map→图验证→下游过滤 | 相同版本约束，不能由Agent决定哪个gold更“正确” | ==读取冻结任务与规范== → ==检查完整对话的回应关系及复合语段范围== → 输出关系；不接触私有版本差异表 | `DiscourseGraph(edus,speakers,E_version)`，明确CDU/方向/标签及ABSTAIN；语料修复不属于被测算子 |

拟议过程非模型实测。固定检索、Coding Agent、E-only编译、批内缓存均为必要同资源对照；没有证据支持Data Agent更准确。

下一步：优先使用同版本可对应的41局纯语言原生数据，核验CDU类型/示例泄漏和完整输入，或获取额外4局同版本发布；不能仅靠改变gold来源提高模型得分。规范必要性及下游实验仍未执行。

脚本/收据：artifact/evidence/shared-environment-audit-20260908-v112/parity.py、parity.json、game-difference.json。未构造public快照、未运行上游代码/模型，无新单元测试、无commit。
