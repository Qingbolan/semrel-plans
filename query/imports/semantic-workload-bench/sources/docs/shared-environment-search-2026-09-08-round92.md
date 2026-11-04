# Increment92 — MADON原始标注对照与发布转换丢标

仍7/15。复用round91完整原论文/代码/数据，未重下载。指南文件GitHub历史查询仅返回添加commit `e47762be406357ff90d5c261d38b81cef10b9868`；检索到[正式论文](https://link.springer.com/article/10.1007/s10506-026-09524-7)，其页面仍指向相同作者仓库，未找到独立补充指南。不是证明完整指南不存在，当前缺页未解决。

本轮直接读272案最终curated JSON及各案INITIAL_CAS JSON，未运行作者代码/加载pickle。9183段正文切片全部与CSV一致；1913个映射范围内原生argument feature，另64个INTIWSINTERPRETATIONWITHOUT、1个EXTCACOMPARATIVEARGUMENTS不在作者8类映射中，必须明确是排除的类别而不是原始“无论证”。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold |
|---|---|---|---|---|
| 逐段识别8类论证，汇总每案特征 | 272案/9183段，全文与原始切片逐项一致 | 作者29页指南仍缺部分内容 | 上下文与法院自身是否采纳论证 | 原始curated图及发布CSV两份证据；发现1段不一致 |
| 预测整案形式主义 | 同272案 | Holistic规则缺页尚未解决 | 不能默认按论证次数多数投票 | CSV161/111；原生一案同值重复两次，不是冲突标签 |
| 开发侧审计转换丢标 | 648399.html.xmi零基段42，[17538:18489] | 8类别映射与标注范围 | 原始JSON中ID3894空标签、随后ID3895为PL | 原始PL，CSV空列表，不能作为模型预测能力差距 |

| 类python的DAG | 具体数值 | 下游gold |
|---|---|---|
| `cases.explode(paragraphs).sem_map(argument_types,E).groupby(case).aggregate()` | 9183段；9182段映射标签与原生投影一致，1段差异 | 648399段42应先决定采用源图还是发布CSV；本轮不修gold |
| `cases.join(predicted_profile).sem_map(holistic,E)` | 272CSV标签 | 271案原生恰1标签一致，1案有2条相同FORMALISTIC；全部标签值无冲突 |
| `curation.project(label_map).compare(released_csv)` | 1913范围内源feature，65范围外feature | 数据侧校验而非实验臂；不能以总数相同代替逐项一致 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 648399段42原始人工目标PL；发布CSV却为空。实际模型输出未测 | 完整原文＋同完整规则的固定sem_map；当前完整规则尚缺 | 同一原生目标，不能用转换错误制造Agent优势 | ==定位Principles of Law定义与法院采纳范围==→标出论证类型；当前缺页不能称已按完整E执行 | `court_context→argument_type_set→case_aggregation`；仅设计 |
| 32CDO2295/2008段25目标D，整案FORMALISTIC | 固定学术引用识别＋全案判断；允许E-only编译与共享缓存 | 相同目标 | ==核对Doctrine及Holistic定义==→输出；不能把缺失Holistic规则用当前gold补齐 | `citation_kind→argument_profile→holistic_label`，尚未学习/测试 |

根因已定位：作者process_raw_data.py的collect_argument_categories遇到没有字段的LegalArgument会break，停止扫描后续标注。在648399中空对象ID3894位于PL对象ID3895之前，解释后者为何未进入发布CSV。我们的正长度区间相交检查同样定位该1段，不是边界接触误计。保留原始发布与诊断，不修改源或把开发修正称新独立gold。

首次审计误用annotated/curation而非最终raw_data/curated，并从curation找Paragraph；观察到Paragraph只在INITIAL_CAS后修正。最终按作者main.py/ReadData明确的所有权读取。原始总体271案唯一、1案重复标签；重复为ECLI_CZ_NS_2000_31.CDO.2509.99.1.xmi。完整诊断在artifact/evidence/shared-environment-audit-20260908-v92/audit.json；指南历史响应在data同后缀。

无模型调用、无测试集调参、无公开快照。下一步完整指南或其他新来源；当前不能用完整数据下载替代必要共享E的缺口。
