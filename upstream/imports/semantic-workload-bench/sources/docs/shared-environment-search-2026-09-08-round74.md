# Increment74：GUM文本/转录话语图开发候选

结论：以新建的142文档文本/转录视图计为第5个SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT独立湖，累计5/15。不是VALIDATED，不是原始音频/网页端到端任务。GUM其他视图、GENTLE、不同关系filter不另计湖。此前247文档视图不覆盖全部必要上下文，保留为INSPECTION_DEVELOPMENT_NOT_QUALIFIED，不覆盖旧收据。

## 求证与根因修正

原论文、完整作者仓库、RST/eRST论文、87页分段参考手册、11张规范图的下载和SHA见round71–72。锁定完整仓库commit `22fdf87f9c71c96bcc771461d06e689b1f90020d`，310825070bytes，6843Git blobs已核验。

对247文档全量输入审计：105篇有figure，102篇有sp@who，150篇有hi@rend。原视图漏掉2447处speaker标记、1114处强调信息。GUM规范明确back-channel attachment依赖是否同一speaker，也明确图像和caption的共同作用可影响关系判断。因此缺口有具体规范依据，不能仅用坐标验证掩盖。

新视图按源公开字段排除105个含figure文档；不依据预测或gold类别筛选。恢复允许的转录/版式字段：说话人/听者、标题/强调/列表/编号、表格、脚注、非语言事件等。它们明确属于给定的上游source TEI转录/结构注释，不宣称由本系统感知获得。不给norm日期、词法/句法标签、句子类型/transition、摘要、实体、EDU边界、关系或signal。直接排除全部figure或speech只剩59文档；本轮通过恢复speaker输入保留了83篇speech文档，而不是无理由缩到59。

实际142文档145263tokens，19271EDU、17890group、896secondary edges。非DM自动/半自动signal不作gold。RST主树与次边来源及人工流程依据eRST原论文§4.1；当前commit更新不冒充原论文旧版精确计数。

## 三张表

| Query | 数据湖数据1：共享E | 数据湖数据2：items | 数据湖数据3：private gold |
|---|---|---|---|
| 按GUM/eRST规则构造每篇话语图，产出归因/证据/条件连接清单 | 作者GUM话语规范及11图；RST-DT§2分段8634words/跨PDF2–31页；RST/eRST理论定义。GUM规则优先，参考论文总页数不是必要E长度 | 142真实文本/转录文档，tokens和源版式/speaker信息给定，无图片文档 | 19271EDU、17890group、896次边，主树关系标签 |
| 同湖实体/信息状态/共指图（候选第二任务） | 已下载作者实体规范 | 同源GUM湖；未完成此任务构造 | 原生WebAnno人工复核字段已下载，不称本轮已运行 |

| 类python的DAG | 具体数值 | 下游gold输出 |
|---|---|---|
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_attribution)` | 142文档→1202positive+81negative | 1283归因连接，可能连接group，不是1283独立文档 |
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_evidence)` | 同142文档 | 565条explanation-evidence |
| `scan(docs).sem_map(parse_erst, E).project(primary_edges).filter(is_condition)` | 同142文档 | 284条contingency-condition |

三个投影共享一个语义构图任务，不当三个独立任务凑数。具体已查看源例子是GUM_news_sensitive的EDU4“who gave it to the CBC today .”→EDU3/elaboration-attribute；它是用于解释的开发源例子，不声称自动落入本轮子集，子集成员以private source-map为准。

| 预期LOTUS结果 | 预期LOTUS过程 | 预期Data Agent结果 | 预期Data Agent过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 目标为源定义的EDU范围、group层级及关系图；具体例子目标为上述attribute边，实际未知 | 同tokens/结构/E固定sem_map，图检查后确定性投影；允许同资源固定检索、E一次编译、批共享缓存 | 同gold目标，未预设更优 | ==查分段/attribute及same-unit规则==；==读取相关speaker/结构并核对attachment范围==；构图校验 | `parse(tokens,source_structure,compiled_policy)`→EDU ranges→主树→次边→结构验证→查询投影；预算/ABSTAIN明确 |

例子用于说明评价目标，所有模型过程均为待测设计。需保留仅E编译、Coding Agent和固定工具流程对照；没有任何本轮模型正确率、质量差距或摊销收益结果。

## 验证及边界

产物`data/shared-environment-audit-20260908-v74/inspection-v1/`；脚本/收据`artifact/evidence/shared-environment-audit-20260908-v74/`。独立验证162assets精确集合/bytes/SHA256、142源正文、无figure、5993结构元素的字段/所含token多重集源对等、gold与已独立逐项验证的v73完全一致，PASS。多重集校验不额外区分文本完全相同的重复结构位置；未声明完整原网页渲染等价。

source构造资格只证明明确任务及可追溯必要输入/规范和gold来源，不能证明模型必须读全部E。已有公开规范依赖为speaker、分段、层级与标签约定；真正长环境增益仍需消融。所有资料属于开发暴露；近重复、独立源实体划分、训练污染及历史规范版本精确适用审计仍待完成。未运行模型、未实现评分器/OS隔离、未独立确认，许可按GUM各源单独处理，不承诺统一商业再发布。
