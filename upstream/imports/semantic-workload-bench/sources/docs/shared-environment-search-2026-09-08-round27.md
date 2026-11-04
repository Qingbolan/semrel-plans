# 第二十七增量：AsyLex 原始下载及逐案标识核验

**本轮不新增可行湖，累计仍为1/10。** AsyLex 提供真实文书与人工复核标签，但目前不能将二者无歧义地连接为同一版长规范下的资格判定批次。这里是排查记录，不将未达条件候选列入合格清单。

## 实际取得的来源

- [原论文 AsyLex，NLLP 2023](https://aclanthology.org/2023.nllp-1.24.pdf)：14页，5,034,888 bytes，已下载并提取正文。
- [完整作者仓库](https://github.com/clairebarale/AsyLex)：commit `41f50270838c4c5fb443e8f03f579ef7b4dd87a7`；ZIP 72,782 bytes，完整解压，28个Git blob逐项SHA1验证通过。未运行作者代码。
- [作者数据集](https://huggingface.co/datasets/clairebarale/AsyLex)：冻结revision `ac20d3ac16b295bed6616f5b97d2a67596a867f8`。全部匿名原文归档324,527,253 bytes，流式完整读取59,112文件、1,102,660,000未压缩bytes；另下载完整gold测试CSV和case-cover/outcomes CSV。没有下载无关的3.9GB全实体推断文件，不称已下载整个HF数据仓库。
- [官方IRB解释手册，正文标记2020-12-31](https://irb-cisr.gc.ca/en/legal-policy/legal-concepts/Documents/Interpretation%20of%20Convention%20Refugee%20and%20Person%20in%20Need%20of%20Protection%20in%20the%20Case%20Law%20%2831%20Dec%202020%29.pdf)：425页、3,232,066 bytes，已下载。取得长手册不等于证明全部历史案件适用这一版。

下载位置 `data/shared-environment-audit-20260908-v27/`；完整URL/大小/SHA256见downloads.json、extra-receipts.json、cases-receipt.json。原文归档SHA256 `da9776b2df36d087893ea90f473a96d7e88a55f2ae952e477e006571aaaf393c`。本轮未形成可再发布的数据许可结论。

## 核验发现

1. 原论文说明1,682个测试标签由结尾关键词赋值后人工复核；训练silver使用自动推断，不可混算。实际gold CSV为1,682行，其中1,371个0、311个1；有18行空decisionID。其余包含1,645个唯一数字ID；78127和78134各同时出现0、1，原因尚未消歧，不能直接认定同一真实案件有矛盾gold。
2. 原文文件名为`年份canlii编号.txt`，gold只保留数字编号。按数字直接连接得到2,939份文件，涵盖全部1,645非空ID，但其中942个ID对应多份原文。必须恢复年份或原始文件键；不能把连接放大的行数当作更多独立样本。仓库`preprocessing/get_gold_det.py`将ID转换为数字并按其连接，尚未发现足以消歧的已验证映射。
3. case-cover中的自动TRIBUNAL不是可靠任务边界。全档文件名2022共有482份，初步关键词仅18份命中RPD，但这个计数也不是有效的18个新申请：抽查`2022canlii79105`实为2021-06-24撤销保护资格申请；`2022canlii96485`实为2020-10-14难民上诉，正文提及RPD导致启发式误分类。**发布/引用年份不等于裁决日期，同一机关也不等于同一任务。** 不用2022文件名前缀证明2020手册适用。
4. 原文含完整专家分析、结论以及尾部POSITIVE/NEGATIVE式主题标签。直接把全文作为输入会泄漏目标；仅删除最后一句不够。目前尚无公开事实与私有裁决分离包。

统计脚本和结果：`artifact/evidence/shared-environment-audit-20260908-v27/audit_data.py`、`statistics.json`、`gold-raw-join.json`、`raw-2022.json`。其中`citation_year`字段当前记录文件名年，`stage_heuristic`仅字符串筛查，不能用于冻结语义分组。第一次正文引用计年被引用旧案影响，已改为文件名计数；文中采用修正后的482，非初版483。

## 用户要求的三表：可审查的候选构造，不计为已可行

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | 私有gold |
|---|---|---|---|---|
| 对同一时点规范下的难民保护申请，筛选满足资格且不受排除条款限制的案件 | 已下载425页IRB解释手册；历史版本适用尚待核对 | 59,112匿名化真实文书，需要按真实裁决日期、机关、程序类型筛选 | 具有归属的申请人陈述、犯罪记录、证据与程序事实；尚未分离 | 1,682行作者人工复核标签，数字ID映射欠账；不能把全部当作资格准予/驳回 |
| 开发例：2010 CanLII 98086，古巴申请人，有美国1984及1993犯罪记录 | 历史IRPA§98及Convention Article1F(b)规则需要当时版本；2020手册不能自动替代 | 原文§2–§6记载犯罪、入境与恐惧迫害主张 | 已服刑不直接等于不受严重非政治犯罪排除，仍需相关标准与事实 | 本文正式§25–§26排除保护；CSV编号98086标0，但未将编号连接作为全库有效性证明 |

| 类python的DAG | 具体数值 | 状态与边界 |
|---|---|---|
| `scan(raw_documents)` | 59,112文件 | 完整读取归档；不是59,112同任务gold |
| `resolve_case_key(year, canlii_id)` | 1,645非空gold ID；942个ID多文件匹配 | 未解决；禁止任选第一条 |
| `filter(actual_date, tribunal, proceeding_type)` | 文件名2022为482；有效资格申请数未知 | 不用启发式RPD18当真实批量 |
| `split_public_facts_private_analysis()` | 尚未构造 | 结论、主题标签及前置结论均要核验 |
| `sem_map(apply_frozen_refugee_rules).sem_filter(eligible).count()` | 例98086的参考排除结果为False；全批gold总数未知 | 规范版本与输入充分性满足后才可执行比较 |

| 预期其中关键的语意算子操作直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期其中关键的语意算子操作直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索/思考的步骤== | 预期产生的operator结构 |
|---|---|---|---|---|
| 对98086希望重现False；实际未运行，未知能否正确 | 同一版本完整E，固定检索排除规则→提取犯罪/量刑/时间事实→判断排除与资格；可共享规则编译和缓存 | 相同目标，无优势预言；必要证据缺失应ABSTAIN | ==确认此案是资格申请而非撤销/上诉==→==定位当时排除标准及服刑因素==→==核对犯罪事实与证据归属==→输出结构化判断 | `RefugeeEligibilityOperator(E_version, proceeding_type, attributed_facts, inclusion_tests, exclusion_tests, missing_evidence)`；先建立E-only编译、固定工具/Coding Agent公平对照 |

这些是可观察动作设计，不是私人思维链或真实模型轨迹。原例已开发曝光，不能直接当独立确认。无模型调用、无作者代码执行、无源码修改、无新增工程测试。下一步若继续此湖，应先修复可追溯的gold键和任务/版本边界；不能用大量silver与长手册拼成“已证实的数据湖”。
