# 第108轮：ChEMU-Ref 可追溯开发检查数据

结论：构造1067条开发检查记录、14920条原生边，独立工程校验通过；尚未计入合格名单，仍7/15。本轮推进数据可执行输入构造，没有运行模型。

## 与上轮相比新增证据

原论文、完整仓库commit及指南哈希见[第107轮](shared-environment-search-2026-09-08-round107.md)，本轮复用已下载字节，没有重复下载或改写原始数据。作者仓库是token化JSON发布版，原始BRAT尚未获取。

[2022官方任务页](https://chemu.au/2022/)明确共指评分需要传递闭包，关系方向为anaphor→antecedent。下载入口实际跳转登录，未获得账户访问。指南PDF4页同时明确，其例子记号是(antecedent, anaphor)，语义方向仍是anaphor→antecedent；这不是gold方向冲突。不得直接把JSON数组位置反转。

构造规则：排除含任一空端点的完整源记录；完全相同token序列按source ID保留首条；排除与公开指南/论文/README匹配12个连续正则词且至少65字符的记录。后两项是保守开发选择，不是完备泄漏检查。共排除58条，保留1067条（原train852/dev215）。不重写空端点，不只删除坏边后保留整条文档。

保留边数：Coreference3027、Transformed565、Reaction-associated3784、Work-up7183、Contained361，共14920；其中1535个端点为多区间。后续模型公开输入只有record_id、原始sentences token列表、完整指南和任务契约；gold、source IDs、原split、排除原因在private。

## 按要求的三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 从批量实验描述中建立物质指代与来源图，列出后处理所得物质及其来源 | 1067条完整token化片段 | 28页共享作者规则：10640正则词 | 同片段全部步骤上下文，不提供gold挑出的mentions；不是专利全文 | 14920条原生有向关系，未补传递闭包 |
| 0516中白色晶体、8.56g产物、前期沉淀是什么关系？ | 前期沉淀后经过过滤和干燥 | §4.3后处理关系、§2同物质关系与§3跨度规则 | 给定源token化文本，85%为原文报告值 | 产物89–102→沉淀71–72为Work-up；白色晶体104–106→产物89–102为Coreference |

| 类python的DAG | 具体数值 | 中间gold目标 | 下游gold |
| --- | --- | --- | --- |
| `snippets.sem_map(resolve_relations,E).explode(edges).filter(type=='Work-up').project(anaphor,antecedent)` | 1067条→14920条原始边 | 类型、方向及不连续跨度精确匹配 | 保留集7183条Work-up；0516为1条。仅定义预期，不是模型输出 |
| `snippets.sem_map(resolve_relations,E).explode(edges).groupby(type).count()` | 同一语义图复用到5种计数 | 0516：Coreference2、Reaction-associated3、Work-up1 | 全量5类计数如上；原生边计数不等于实体数或2022闭包边数 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 0516的正确目标为上述Work-up与Coreference边；实际预测未知 | 同规则固定sem_map→类型/跨度校验→下游关系过滤；允许固定检索和共享规则缓存 | 同样正确目标；不能推定更准 | ==检查指南中数量、跨度与后处理规范== → ==追踪过滤/干燥前后对象及其身份== → 输出带位置的边 | `ResolveMaterialRelations(sentences, frozen_E)`；建立步骤/对象状态→识别来源/同一性→输出原生方向关系→非法输出ABSTAIN；禁止源ID/答案特例 |

固定程序、Coding Agent、仅E无轨迹编译和整批Agent都应有相同工具、资源、缓存许可；本轮没有单轨迹示范或自动提取产物。

## 工程验证与科学边界

- 新目录`data/shared-environment-audit-20260908-v108/inspection-v1/`，1072个资产及独立manifest。
- `build_inspection.py`构造；另一脚本`verify_inspection.py`独立检查资产集合/哈希、公开字段allowlist、ID一一对应、全部token与14920条关系的原生精确一致、非空端点、闭区间范围。全部通过。
- 这是离线inspection数据包，不是core.Snapshot运行器验收，也不是OS级模型隔离。
- 58条选择已查看gold结构，用途明确为开发。不能用这批数据声称独立确认；尚无专利级分组或全量近重复隔离。
- 未将原始发布边映射到官方2022闭包评分。后续需冻结surface/atom/closure语义，再实现真正的评分器。
- 未解决原始BRAT字节对齐、指南示例完整泄漏审计及规则必要性的实测，因此不增加合格湖数。

收据和脚本：`artifact/evidence/shared-environment-audit-20260908-v108/`。无模型调用、无新增单元测试、未commit。
