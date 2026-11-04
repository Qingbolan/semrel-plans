# 第60增量：SENTiVENT第三个可构造开发湖

**累计3/10，新增SENTiVENT，资格SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT。** 本轮来源与构造可核，不是VALIDATED、独立确认或Agent优势。282篇独立源新闻对应6111事件提及，不称6111独立新闻或真实世界事件。此处batch规模为数百篇，低于用户举例的数千篇。

原33页论文、11页早期论文、完整141资产作者数据仓库、指南完整源码仓库和69页原PDF下载/哈希见round58；事件源对应见round59。本轮复用资产，不补造标签。

## 来源与任务闭合

raw事件参数直接匹配仅62/288文档通过，原因是发布格式采用canonical argument：沿PronomCanonRef的Governor→Dependent链解析代词/泛称，直到明确指称。本轮按原始链、角色及跨度复现，288/288全文、事件和参数多重集合精确匹配。所有内层ZIP CRC通过；没有读取模型输出来决定gold。

该对应检查为来源诊断：302份最终导出存在重复文档，本次查找与冻结作者发布JSON一致的原导出，不作为确认split选择。实际构造直接使用已冻结的作者发布JSON，不重新挑原标注版本。未证明作者整个构建工具链逐步复现，也未核验全部情感或事件共指关系；本任务不以那些层作为目标。

环境为原69页指南PDF的第13–64页，按pdftotext-layout逐页原文提取成protocol.txt（124321字符），包括章节3–6。第7章改进建议不作为规范。原论文不是环境；原PDF和工作流页面保留在source侧。规则包含事件触发/类型、复杂跨度、参数适用、章节4.3 canonical reference、否定/确定性及类别混淆，明确不是只给类别名。

构造排除6篇：2篇与公开指南/原论文出现12词且至少65字符的归一化连续片段重合；4篇有原始缺类型事件。后者是显式标注质量排除，含gold可用性条件，不称纯公开抽样，也不是按模型结果挑样本。未保证近重复/改写示例/训练污染隔离。

| Query | 数据湖 数据1 | 数据湖 数据2 | private gold |
|---|---|---|---|
| 为每篇新闻提取事件及canonical参数，输出SecurityValue事件清单 | 同一52页规范正文，第13–64页，124321字符 | 282篇完整新闻文本；仅document_id/text公开 | 6111事件、13535参数；720证券价值提及 |
| 原aal00开发例：The company ... | §4.3要求代词或泛称指向canonical mention；参数角色取决于事件 | The company[266:277]，前文American Airlines Group Inc. AAL[90:122] | Seller等角色使用前文明示公司的跨度[90:122]；原始PronomCanonRef链支持，关系不公开 |
| 同文shares rise 4.76 % ... $47.08 | SecurityValue_Increase与角色定义 | 完整上下文，包括时间文字 | rise触发、增加幅度、价格、时间；不能用某个字段缺失当FALSE |

| 类python的DAG | 具体数值/状态 |
|---|---|
| `docs=scan(public.documents)` | 282篇；源288中排除6篇，规则记录在private |
| `events=sem_map(docs, protocol)` | 目标6111事件，输出type/subtype/全部trigger spans/modality/negated/参数role+canonical spans |
| `selected=filter(events,type=='SecurityValue')` | 私有gold720提及；肯定/否定不等于金融情绪positive/negative |
| `groupby(document_id).collect(events)` | 原位清单与角色可评分，不输出未经gold支持的投资建议或收益 |

| 预期关键语义算子直接交LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程，用==标注探索== | 预期operator结构 |
|---|---|---|---|---|
| 正确事件及canonical参数；The company应解析到明确公司；实际质量未知 | 完整全文上的固定sem_map，固定规范检索和指称解析，可循环/检查/缓存；不限制为单句弱prompt | 同一目标，无胜出假设 | ==查询事件类别边界；定位参数角色；按4.3追踪指称链；核否定/确定性与原文跨度==→结构化记录 | ProtocolIndex→EventDetector→RoleAssigner→CanonicalReferenceResolver→Factuality→SpanValidator→聚合；结构是待检验设计，非已学产物 |
| 全批结果与成本未知 | E-only编译和Coding Agent可用相同全文/规范，需列强对照 | 整批Agent可共享预处理，不强制每行重规划 | ==首次建立规范索引，后续只检索需要的规则== | 单轨迹提取必须另行执行并冻结，当前未完成 |

## 构造与验证

`data/shared-environment-audit-20260908-v60/inspection-v1/`含public/documents、protocol.txt、task.json和private/gold.jsonl/source-map/exclusions。public不提供token标签、触发位置、共指链或事件/参数候选。任务始终从完整新闻开始，gold关系没有作为工具给模型。

build_inspection.py新目录构造287资产；独立verify_inspection.py检查精确清单、全部size/SHA256、公开字段allowlist、282文档/private一对一及6111事件/参数跨度范围通过。源切片和原始角色链对应另由v58/v59/v60审计建立。task.json保留INSPECTION_DEVELOPMENT，来源资格不自动把执行状态改VALIDATED。

论文/源码/数据许可分别见round58：annotations及规范CC BY4.0、软件Apache2.0、第三方新闻另属原权利人。当前本地研究包未公开发布。无模型或作者代码执行、新工程测试0；数据审计不是性能实验。示范/开发/确认实体分组、近重复、模型基线、资源消融、单轨迹提取和完整摊销成本均未做。公开来源原本已知的数据可能有训练污染，当前只列可构造开发湖。
