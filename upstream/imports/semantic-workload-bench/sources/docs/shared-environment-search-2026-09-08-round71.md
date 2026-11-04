# Increment71：GUM完整来源与跨标注层核验（待资格确认）

本轮没有新增合格湖，仍4/10。GUM提供真实来源文本与多层人工标注，有同湖多任务潜力。已完成完整作者仓库及论文下载、源文件全量校验、实体/话语层计数与文本对齐审计。尚未完成共享规范完整性/版本适用性、公私输入构造及标签映射验证，不能仅以多层标注宣称满足复杂E要求。

## 下载证据

- [GUM原论文作者版](https://gucorpling.org/amir/pdf/GUM_paper_prepub.pdf)：32页、808460bytes，SHA256 `e0977d372b83c8895a324b970f3e5459509c67f96de2df431cfa4eff751cc20b`。旧原论文不自动证明2026仓库每层现状。
- [完整作者仓库](https://github.com/amir-zeldes/gum/tree/22fdf87f9c71c96bcc771461d06e689b1f90020d)：锁定commit `22fdf87f9c71c96bcc771461d06e689b1f90020d`，ZIP310825070bytes、7126entries；CRC通过，6843个Git blobs SHA1全匹配，递归tree未截断。ZIP SHA256 `6f50ec7f2d29fc168a843fcf649aa8506734e3d23cd2db95d86661fea0fdfe51`。没有执行作者代码/构造脚本。
- [eRST方法原论文](https://aclanthology.org/2025.cl-1.3.pdf)：2107444bytes，SHA256 `f04807264324631d1ad79aade3529215afc7729cf874ef311edf5094ab52a6da`。全文已下载，但尚未逐节核验哪些部分是当前任务必要规范。
- 作者[实体/信息状态规范](https://wiki.gucorpling.org/gum/entities)与[话语规范](https://wiki.gucorpling.org/gum/rst)HTML已冻结。含UI的文本分别5535/6396words，不能当精确规范字数或PDF页数。`?do=export_raw`返回相同HTML，不是原始Markdown；收据记录了真实响应。话语规范还引用RST segmentation外部PDF，尚未下载/确认版本。
- [作者标注层说明](https://gucorpling.org/gum/annotations.html)明确：ref实体/共指/信息状态人工复核；const除8个test文档外尚未完整人工纠正，其他形态/转换层也有程序生成。不得将整个仓库视为纯人工gold。

## 本次实际计数

| 来源分区 | 文档 | tokens | 实体mention | 话语EDU | primary parent edges | secondary edges |
|---|---:|---:|---:|---:|---:|---:|
| GUM非Reddit | 257 | 256739 | 72415 | 33007 | 63122 | 1290 |
| GUM Reddit（正文未完整提供） | 18 | 16364 | 4552 | 2263 | 4352 | 106 |
| GENTLE外域扩展 | 26 | 17799 | 5681 | 2717 | 4880 | 65 |

不将GENTLE计为第二个独立湖；当前构思只使用GUM非Reddit。tokens/mentions/EDUs不是独立文档数。文档可能是源文本摘录，不能称257篇完整原始长文。primary edges含`span`等结构边，不等于全部语义relation标签。关系entry计数尚未完成图去重/端点验证，故不作为gold关系总数。

257个非Reddit文档的XML tokens与WebAnno TSV tokens全匹配。XML与原生RS4有4文档不同、共11tokens：artist大小写1处，court_property人名Lavan/Levan2处，letter_cricket引号4处，letter_travel引号4处。无静默规范化，无逐条gold驱动修补。Reddit有7文档XML/TSV不匹配，且存在遮蔽正文，整体不进入当前可读候选范围。

## 用户要求的三张表（待构造，不列入已验证合格清单）

| Query | 数据湖数据1：E | 数据湖数据2：items | 数据湖数据3：gold |
|---|---|---|---|
| 按GUM规则抽取实体mention、类型、信息状态和共指/bridging，构建每篇实体图 | 作者实体规范；嵌套mention、事件指称、predication/cataphora、信息状态等约定 | 257真实非Reddit文档文本，所有目标标注须移入private | 72415原生WebAnno mention，标签/边端点解析与隔离尚未完成 |
| 按eRST构建话语结构，提取归因/证据/条件等关系清单 | 作者eRST规范及其必需segmentation规则；不能只把32类名字当E | 同257文档；本轮发现4篇跨层文本差异 | 33007EDUs及其原生RS4树/secondary关系；完整转换评分未实现 |

| 类python的DAG | 具体数值 | gold输出与下游 |
|---|---|---|
| `scan(texts).sem_map(extract_entity_graph, E).project(mentions, infstat, edges)` | 257文档，72415mention源计数 | 每篇实体图；不能把Coref生成的派生cluster数量冒充已审计结果 |
| `scan(texts).sem_map(parse_erst, E).project(relation_edges).filter(label.in_(query_relations))` | 同257文档，33007EDUs | 归因/证据等关系清单；筛选后的精确数量待解析，不填猜测数字 |

源例子`GUM_news_sensitive`：标题“Sensitive Canadian document found on rainy streets”同时包含一个覆盖整个标题的`event` mention、覆盖“Sensitive Canadian document”的`object`、覆盖“rainy streets”的`place`，三个标注可嵌套。该文RS4第1个EDU是`organization-heading → parent77`；第4个EDU“who gave it to the CBC today .”是`elaboration-attribute → EDU3`。这些是已查看的开发gold，不是模型输出。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期LOTUS执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期Data Agent执行过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 目标为标题event/object/place嵌套结构；实际未知 | 同完整文本与E固定sem_map，span/类型/图端点验证；允许固定检索和共享编译 | 相同gold目标，实际未知 | ==查事件指称及嵌套mention约定==；==查当前mention的信息状态和共指条件==；输出并工具校验 | `entity_graph(text, schema)`：候选span、schema类型/状态、链接、图一致性、预算/ABSTAIN |
| 目标为上述heading与elaboration-attribute关系；实际未知 | 同资源固定sem_map构树，再程序抽取查询关系；不能给其中一方goldEDU边界而不披露 | 相同目标，实际未知 | ==查segmentation及attribute关系定义==；==查单元层级、parent和secondary规则==；构树并检查覆盖/端点 | `erst_parse(text, policy)`：分段、主树、允许的次边、结构验证、relation投影 |

所有方法表是设计预期，未运行LOTUS/Data Agent。需包含仅E编译、Coding Agent、固定工具程序对照；不能因普通NER没有event/place嵌套就宣布LLM静态方法必然失败。

## 下一步与产物

需冻结去UI的规范正文，获取必要segmentation文件并核验适用版本；分析手册示例与文档重叠；解析原生mention/infstat/typed edges，确认哪些标签由人工直接产生、哪些为程序转换；选择明确的文本坐标来源，构造公开纯文本与私有gold，独立核验。不能公开XML完整metadata（含human summaries）或TSV annotation列。

全部下载位于`data/shared-environment-audit-20260908-v71/`；可复查脚本/收据在`artifact/evidence/shared-environment-audit-20260908-v71/`。许可证按仓库LICENSE.md不同来源分别判断，不能统一承诺无限商业再分发。本轮没有模型、独立确认或环境增益实验。下载sessions43994/29946均正常结束。
