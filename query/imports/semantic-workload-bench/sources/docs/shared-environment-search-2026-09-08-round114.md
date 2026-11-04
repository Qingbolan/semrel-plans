# 第114轮：STAC指南泄漏确认与新开发包

结论：确认指南包含当前开发数据的原文及正确关系；按整局排除后构造944段/39局新包，949资产验证通过。不增加合格湖，仍7/15。

## 新证据

完整46页原指南（111轮原始PDF）逐页渲染1800px并Tesseract eng OCR，4 worker，全部完成。用8个连续小写正则词、至少40字符匹配113轮开发语段，命中5记录、2游戏pilot01/pilot03；这比上轮纯文本12gram检查更敏感，因此上轮零命中不能作为无泄漏证据。

视觉核对PDF21页例64：Dave的“While we're talking about trading,”和“does anyone have sheep?”被明确标为Background。113包record_0003的e16→e17原生gold同为Background。确定是真实答案示例泄漏，不只是相似话题。其他4个命中仅为候选，本轮保守排除pilot01、pilot03整局共81段。

旧113包保持原样，不能用于声称完整指南无泄漏。新114 inspection-v2保留944段、39局、10019EDU、1111CDU、9732边；其中378澄清、2359问答关系。949资产的独立哈希/公开字段/source映射/文本及关系/CDU成员精确一致检查通过。

## CDU语义检查

对113旧包的1302CDU做递归结构签名诊断：46个嵌套CDU，2501边涉及CDU，270边两端都是CDU。没有重复递归成员结构；这些是旧包数值，不能直接作为新944包统计。

例record_0000中c6包含e40与c5，而c5包含e41/e42；直接摊平为三个EDU会丢失嵌套。原论文讨论CDU-to-head和CDU-distribute等不同转换，转换改变图/任务，不能静默使用。递归结构签名只是诊断设计，没有实现或验证正式评分器，且不能拿预测CDU字符串ID与gold ID直接比较。

## 三表

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
| --- | --- | --- | --- | --- |
| 批量恢复回应结构并检索澄清问题 | 新944段，39局，10019已分段语段 | 原始46页共享指南 | 文本、speaker、turn顺序；不公开受话者/CDU/关系 | 9732有向边及1111CDU，原生未改写 |
| 泄漏诊断：Dave的交易引入语与询问sheep的语段 | 已排除pilot01原文两段 | 指南PDF21例64直接给Background | 与113原生记录匹配，不供确认运行 | e16→e17为Background；这只能用于开发审计 |

| 类python的DAG | 具体数值 | 中间输出 | 下游gold |
| --- | --- | --- | --- |
| `dialogues.sem_map(discourse_graph,E).explode(edges).filter(type=='Clarification_question').project(source,target)` | 944段→9732原生边 | 包含CDU端点的图，不静默摊平 | 新包378条澄清边 |
| `dialogues.sem_map(discourse_graph,E).explode(edges).filter(type=='Question_answer_pair').project(source,target)` | 同图复用 | 源/目标可能为复合语段 | 新包2359条问答边，非现实满意度 |

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| 未执行；对泄漏例预测Background不构成泛化成绩 | 同E固定sem_map→复合结构校验→关系过滤，支持共享缓存 | 未执行；同样不得以泄漏例宣称更准确 | ==读取规范的复合语段和关系定义== → ==确定当前对话的回应范围== → 输出图，不读取private | `DiscourseGraph(edus,speakers,E_version)`；保持递归成员结构，结构匹配CDU；缺证据/非法图ABSTAIN |

仍需固定程序、Coding Agent、E-only编译及整批Agent等同资源比较；本轮没有模型调用、示范轨迹或自动提取。

## 产物及边界

- 原指南OCR：data/shared-environment-audit-20260908-v114/ocr与guide-ocr.txt。
- 新包：data/shared-environment-audit-20260908-v114/inspection-v2；旧113完整保留。
- 收据/可重跑诊断：artifact/evidence/shared-environment-audit-20260908-v114/cdu_audit.py、cdu-audit.json、overlap.py、overlap.json、build-receipt.json、verify-receipt.json。
- 新包复用113独立验证器，仅替换输入和收据输出路径。本轮构造命令保留于工具执行记录，尚未抽成独立复现脚本。
- OCR匹配仍不是完整语义近重复审计；CDU评分/公开执行/环境必要性/独立确认未完成。无新增单元测试，无commit。
