# 工作账本


## 2026-10-12T16:18:00.770769+08:00 — SemRel Plans 目录组织

目标：按用户指定将既有88条混合查询计划组织到 `/Volumes/Element/Github2/semrel-plans`，参考SemBench代码结构。先检查两个仓库git status；目标为空Git仓库，原仓修改保留。读取原图册JSON/HTML/来源收据；临时只读clone SemBench，HEAD为8c2cac89b21c6782239e8e5b03d326d0c029b655，与原图册固定版本一致。参照files/<scenario>/query、src场景与构建职责、scripts入口分工。

产物：8场景88个独立query/logical JSON、场景manifest、统一Scenario/Catalog与SiteBuilder、独立HTML/CSS/JS、离线index、文字图册、来源文本快照和迁移/验证收据。无模型执行器或空占位框架。原图册未修改。实际命令：git status/clone/rev-parse，Python迁移，scripts/build.py、scripts/validate.py、node --check，以及逐字段一致性、本地Markdown链接和重复构建hash核对，均通过。验证收据位于目标docs/provenance/validation.json。

研究判断与数据条件未变，不新增研究版本或升级准备度；这是既有RV018/s01展示材料的目录重组。无数据构造、gold读取、模型推理、提取、评分、commit或发布。split/模型/prompt/预算/并发/cache不适用；整理与网络费用未计量。


## 2026-10-12T16:22:48.929054+08:00 — 统一统计数据模型 v1

按用户要求将展示导向的嵌套JSON迁移为queries/nodes/edges/sources四张JSONL事实表，算子字典统一29类型。原8场景目录只引用query_id，移除88份旧嵌套查询，避免双写。图册由同一规范化数据生成。新增CSV、SQLite、查询级和算子级统计；88查询/580节点/492边/84来源。逻辑节点统计不是模型调用或科学结果。

实际读取git status、原Scenario/Catalog/SiteBuilder、原查询标签；实施Python迁移与根因重构。执行build、validate、5项完整性/统计单测、node --check、88条树逐字段比对、Markdown链接、重复构建CSV/JSON/Markdown hash验证，均通过。收据normalization-validation.json。无模型/gold/独立split/预算/缓存相关操作，不适用；整理费用未知。未commit或发布。研究结论及数据条件未变。
