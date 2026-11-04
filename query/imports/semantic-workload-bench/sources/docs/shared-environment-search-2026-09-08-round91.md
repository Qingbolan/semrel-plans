# Increment91 — MADON真实裁决、多任务gold与不完整指南

本轮新增来源核验，仍7/15，不把MADON算合格湖。已下载[原论文](https://arxiv.org/abs/2512.11374)39页704365bytes、[完整代码仓库](https://github.com/trusthlt/madon)commit `5e1c1dfb14beaf21ce74d038f36c6daf0f880925` ZIP9841550bytes481成员，以及[独立人工数据仓库](https://git-ce.rwth-aachen.de/trusthlt-public/madon-annotated-data)完整ZIP206146865bytes4522成员。两个ZIP全部CRC通过，数据仓库按下载字节锁定，尚未解析精确Git commit或逐Git blob对照。

SHA256：论文3ab20eee072dbd945c800d56c30e5087da258500b427cd611a7a8137792b4105；代码55d5dc907bf75673c3d1ef736f4ac6ec6631c99d2685f74f7f2782611bf4d181；数据899e6e439cf01f7376d3595df897087be3b0c1c302464f62c2c98d113294ed7d。下载收据见artifact/evidence/shared-environment-audit-20260908-v91。

数据仓库API返回反机器人HTML，未将其当JSON解析，也未尝试绕过；普通公开项目页面正常，从页面提供的ZIP下载链接成功取得全部数据。未执行作者代码或加载pickle。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐段识别裁判自身采用的论证类型并汇总案件论证组合 | 实际272捷克裁决、9183段 | 作者Annex B标注规范与流程图，PDF29页但有实际空白缺口 | 全案上下文；不能只靠关键词断定法院是否采纳该论证 | 1237段有论证；8类别共1913次段落标签 |
| 判定整案formalistic/non-formalistic | 同272裁决 | Holistic规范应在指南第16页，但本发布该页视觉确认为空白 | 上游论证预测可用于下游分类；不能把人工上游标签默认给模型 | FORMALISTIC161、NON FORMALISTIC111 |
| 提取案件程序结果 | 同原文 | 元数据区分不受理、驳回、支持/部分支持、其他 | 原生result_labels存在；尚未核对完整覆盖 | 只能作为潜在第三任务，不能把结果标签直接当法律事实正确性gold |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `decisions.explode(paragraphs).sem_map(argument_types,E).groupby(case).aggregate(types)` | 272→9183段→1237带论证段 | D68/CL707/TI315/PC138/PL311/LIN108/SI208/HI58；总1913是段落标签次数，未验证与原生span一一对应 |
| `decisions.join(predicted_argument_profile).sem_map(holistic_formalism,E)` | 272→272 | 161/111，两类均有人工标签；不能用数量多数表决替代原任务 |
| `decisions.sem_map(procedural_result,E).groupby(result).count()` | 原生272行带result_labels字段 | 覆盖、冲突及类别计数待核对，未称已可运行 |

具体原始记录：`ECLI_CZ_NS_2009_32.CDO.2295.2008.1.xmi`，发布doc_id=0，零基paragraph25引用Chalupa、Štenglová、Tomsa等《商法典评注》1994年版第443页及后续§536评注，人工标签为D(Doctrine)，整案FORMALISTIC。这是裁决对学术评注的引用分类，不是判断该案是否应当胜诉。

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 此段目标D；实际模型输出未测 | 同案全文/段落与同规范，固定sem_map判断引用性质与说话主体，再确定性聚合 | 同D目标，未预设优势 | ==定位Doctrine定义，核对法院采纳与仅转述/拒绝论证的区别==→提取该段D→聚合 | `case_context→court_position→argument_type_set→case_profile`；未从轨迹学习 |
| 整案目标FORMALISTIC，但目前缺完整Holistic规则 | 固定程序必须获得同完整E；不能用缺规则条件制造失败 | 相同标签目标；目前同样缺必要E | ==检查Holistic定义与图表==→当前发现缺页，不能宣称按完整规范执行 | `argument_profile + full_case→holistic_label`；仅设计，不可用私有gold补规则 |

独立CSV读取实测train189/dev54/test29；各CSV的text/labels/result_labels长度全272一致，0长度对应错误。原始仓库另含1422JSON、272XMI，尚未做curation→CSV全量语义对照。论文说明至少两名标注者/案，最终curation；不同论证类别一致性差异显著，不能把有人工标签等同确定无歧义。

关键缺口：Annex B PDF1218307bytes，SHA256 `53dfc77822a69eeb0a79f1b5dd627a82723cbc4c935f685bc0676be4ea71edfc`。文本抽取约7103词；第11–17页各只有页码。已渲染并直接查看第11、16页，确实为空白，并非仅OCR漏字；目录声称此处应有Principles/Teleology/Consequences/Holistic。尚未逐一视觉检查其他页。第22–29页仅有少量流程图标题，需继续核对。不得因目录有章节就说完整长E已取得，更不能用39页研究论文充当丢失的完整规则。

后续优先寻找同作者完整规范版本；若仍缺失则保留pending并转其他来源。代码Apache2.0不自动覆盖法院原始材料与独立数据仓库，许可证尚需分别核验。无模型、无优势/成本结论、无公开快照。本轮将两次CSV读取错误（默认field limit不足、误把纯字符串f_labels当literal）按实际schema修正，最终脚本audit.py成功完成；没有修改源数据。
