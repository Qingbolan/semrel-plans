# Increment77：AAEC基础论证任务的开发构造资格

AAEC加入SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT，累计6/15独立湖；不是VALIDATED。视图位于v76，本轮独立核验位于v77。五个源边界冲突文档按已披露的gold暴露开发清理排除，不宣称独立确认。语义类型扩展与其他变体不另算湖。

## 核验证据

原论文及完整官方基础发布包、31页11171词作者指南、完整语义扩展作者仓库/原论文下载及hash见[round75](shared-environment-search-2026-09-08-round75.md)。基础指南明确标注论证边界、majorclaim/claim/premise、supports/attacks和claim stance，正文与各自prompt公开提供。§2.1规定排除shell language及完整性判断；§3及结构说明规定claim到majorclaim通过stance表达，不补不存在的显式边。这些规则改变目标输出，环境不是无关背景材料。

实际视图397文档、6007成分、3781关系、1486stance。`verify.py`独立重新解析原始BRAT及prompt：402asset精确集合/bytes/SHA256，public字段allowlist，正文/题目与锁定读取规则一致，组件全部span和类别、关系和stance逐项源对等。关系源为Premise、目标为Premise或Claim；每个Claim恰有一个stance。全部PASS，0契约异常。此验证不包含模型预测和语义裁判。

完整31页指南以130dpi渲染并Tesseract OCR（3并发），对402源作文使用12词/至少65字符重叠检查，未见额外命中；不等于无近重复/训练污染。视觉检查PDF8页确认边界/完整性规范及shell language描述；未声称31页全部人工视觉审核。

## 三张任务表

| Query | 数据湖数据1：共享环境E | 数据湖数据2：输入items | 数据湖数据3：private gold |
|---|---|---|---|
| 按AAEC规范构造论证成分及supports/attacks结构，输出每篇反驳清单 | 31页11171词作者标注规范 | 397完整源作文（含标题）及写作prompt；Mac Roman解码推断见round76 | 740MajorClaim1486Claim3781Premise；3564supports217attacks |
| 判断每个claim相对作者主立场的For/Against（同湖目标） | 同规范的majorclaim与stance定义 | 同作文；必须从全文确定主立场，不能把prompt观点当作者观点 | 1212For274Against；当前与结构联合构造，独立annotation-given运行视图未建立 |
| 增加语义类型（扩展任务待构造） | 11页扩展规范＋必要基础规则 | 同湖；5源边界冲突保留两版、未自动合并 | 原6089条类型已下载，不称已完成扩展独立构造 |

| 类python的DAG | 具体数值 | 下游gold目标 |
|---|---|---|
| `scan(essays,prompts).sem_map(argument_graph,E).explode(relations).filter(type=='attacks')` | 397doc→3781关系 | 217attack连接；不是217独立作文 |
| `scan(essays,prompts).sem_map(argument_graph,E).explode(claims).filter(stance=='Against')` | 1486claim | 274Against；stance目标与关系类型不同 |

具体例essay001：T1[503:575]是MajorClaim；T3[591:714]为Claim/For；T4[716:851]为Premise，R1=T4 supports T3。针对attack或Against的下游查询，这两个已说明的目标对象均不应选入。该例开发暴露，未进行模型推理。

| 预期LOTUS关键算子结果 | 预期LOTUS执行过程 | 预期Data Agent结果 | 预期Data Agent执行过程（==环境探索步骤==） | 预期operator结构 |
|---|---|---|---|---|
| 上例T4 supports T3、T3/For；实际未知 | 作文+prompt+完整必要E固定sem_map，span/枚举/边校验后filter；允许固定检索/共享缓存/E编译 | 同gold目标，实际未测 | ==查shell language、成分边界及关系定义==；==对照全文主立场、当前claim和premise功能==；输出图及可查证据并校验 | `argument_graph(text,prompt,policy)`→component spans/types→relations/stance→validation→projection；预算和ABSTAIN明确 |

这是预期结构，不是已经从轨迹学出的算子。需实际一次示范、自动提取、冻结及独立执行才能主张学习。E-only编译、Coding Agent、固定工具流程与批共享Agent必须公平比较；31页存在不能证明全部页面必要或静态方法能力不足。

## 产物和剩余工作

构造：`data/shared-environment-audit-20260908-v76/inspection-v1/`，未修改既有manifest或gold。新核验/OCR脚本及收据：`artifact/evidence/shared-environment-audit-20260908-v77/`；渲染图仅本地`data/shared-environment-audit-20260908-v77/`。

许可仅学术研究且限制再分发；交付获取/构造流程，原数据不提交或外发。source资格不代表发表许可/生产适用。prompt Mac Roman为有证据推断；源实体/作者隔离、独立确认、规范必要性消融、评分器与模型执行、完整成本仍未完成。无模型准确率或Agent优势结论。旧构造receipt的INSPECTION状态记录当时阶段，本卡片新增source资格不回写历史。
