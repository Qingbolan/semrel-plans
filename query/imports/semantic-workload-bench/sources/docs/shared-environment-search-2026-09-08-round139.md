# 第139轮：MSLR-Bench 原论文、完整仓库和输入泄漏核验

本轮不新增合格湖，仍8/15（SOURCE_VERIFIED_CONSTRUCTIBLE_DEVELOPMENT，不代表环境增益已验证）。MSLR未满足严格共享长环境契约，记录为排除证据，不列为推荐benchmark。

来源：[原论文](https://arxiv.org/abs/2511.07979)，[作者仓库](https://github.com/yuwenhan07/MSLR-Bench)。下载21页PDF1332101bytes，SHA256 `6d1397cfa9039d4b4b8b3f5a3dcaca2bc11e1875ecaa16c77d59a1b6e6a189d4`；完整仓库commit `50592efa2fe3aa51f14b6dd48172c6d4925847b8`，ZIP9237071bytes、1409members、CRC通过，SHA256 `4da9f3871ddde61c1c9f9fcfa8f1a68262c92c22f5d6b18471d980c99672deed`。文件在data/shared-environment-audit-20260908-v139/；收据和审计在artifact/evidence/shared-environment-audit-20260908-v139/。仓库Apache2.0，README对数据另声明仅研究用途，未据此推断原法律文书可无限再分发。

实际1389个processed JSON、1389条input、全部processed具有非空最终判决。递归叶字段58382（含全文等），不是论文59771“step labels”的同义统计。作者描述人工及LLM辅助后人工复核；本轮不将其全部视为纯人工原生裁决标签。论文页数不是共享规范页数；完整仓库没有法条PDF、长标注指南或带历史版本的完整法律文本。schema只是字段模板，task2_predict.py提供短通用/CoT提示，未挂载共享法条。跨年份案件不能自行统一到最新证券法。

全量配对发现input序号与entry文件数字不能直接join：同数字仅1条案件描述相等；但1389条描述都在processed中找到精确文本，1377条可唯一配对，12条描述有多个候选，保留未决。input2→entry_10.json，而非entry_2.json（后者是2009年的不同案件）。映射保存text-join.json。按唯一文本配对，74条输入包含其完整最终判决（仅忽略空白）；139条输入含“我会决定/本院判决/判决如下/决定如下/决定不起诉”至少一个标记，后者只是粗筛，不是139条已确认泄漏。不能用错误ID配对所得0次包含来否认泄漏。

具体：input2的2020〔33〕号案件描述明确给出没收违法所得582841.53元并罚款582841.53元。把这一输入用于处罚预测存在答案复述捷径。另在entry_1原文/最终判决中，处罚依据为原证券法第一百八十三条，而结构化处罚依据给第七十三、七十六、二百零二条；未获得归一化规则前不能把结构化条文当无争议gold。

| Query | 数据湖 数据1 | 数据湖 数据2 | 数据湖 数据3 | private gold / 结论 |
| --- | --- | --- | --- | --- |
| Q1 从每案文书提取交易时间、方向和数量，生成核查表 | 1389份processed法律文书原文；entry1买入164.6757万股、卖出19.5193万股 | extract_schema字段模板 | 长历史法条环境未随仓库提供 | entry1最早买入2004-06-21、最晚2004-06-29；数量在原文，未确认独立数量gold，不扩造评分目标 |
| Q2 根据案情预测处罚类型、没收额和罚款额 | input1389条；input2对应entry10 | 同一短CoT路径；不是长规范 | 需补历史法律版本及适用规则，当前缺失 | input2已经写出没收582841.53、罚款582841.53；不能作为无泄漏预测示例 |
| Q3 从文书提取处罚依据并按法条汇总 | entry1原文 | schema字段模板 | 条文归一化规则缺失 | 原文183条与结构化202条不一致，暂不评分 |

| 类python的DAG | 具体数值 / 中间输出 | 下游与限制 |
| --- | --- | --- |
| `documents.sem_map(extract_trade_window, schema).project(id,start,end)` | entry1→2004-06-21、2004-06-29；全库1389documents | 可讨论抽取任务，不能据此证明长E或探索必要 |
| `inputs.join(gold_index,on=exact_description)` | 1377唯一匹配；12歧义保留 | 仅构造侧读取gold；映射不可作为模型答案资源 |
| `facts.sem_map(predict_penalty,E).groupby(type).aggregate(count,sum_fine)` | 当前74条唯一匹配输入含完整最终判决 | 不执行此预测实验；需先冻结无泄漏事实视图、E版本与可靠gold |

以下均为方法假设，未执行模型，不填写虚构准确率或宣称Agent更好。

| 预期关键语意算子直接交给LOTUS的执行结果 | 预期直接交给LOTUS的执行过程 | 预期关键语意算子直接交给Data Agent的执行结果 | 预期直接交给Data Agent的执行过程，用==标注环境探索步骤== | 预期产生的operator结构 |
| --- | --- | --- | --- | --- |
| Q1正确目标为entry1买入窗口2004-06-21至06-29；实际输出未测 | 文书+字段定义→固定sem_map→日期格式校验→投影 | 相同目标；无依据预言优于LOTUS | ==读取schema，确认买入窗口与信息公开日不同字段==→定位交易叙述→格式校验 | `TradeWindowExtractor(text,schema)->dates/evidence/ABSTAIN`；只用短schema即可编译，单轨迹必要性未成立 |
| Q2对input2可能直接抽出582841.53两项金额；这不是政策推理成功 | 案情中检索决定段→读金额，或直接语义调用 | 同样可复述金额；不构成探索增益 | ==检查可用法条及版本==→发现E缺失；若读到决定段则记录输入污染，不能将之包装为预测 | 暂不合成`PenaltyPredictor`；先修数据契约；不写死答案或ID |
| Q3原文目标为第一百八十三条，当前结构化目标冲突 | 固定抽取处罚段引用→条文格式化 | 同样存在评分目标不明问题 | ==对照允许的历史法条版本与归一化说明==；当前说明缺失，不从private标签补规则 | `StatuteCitationExtractor`可做原文抽取；历史条文映射须独立规范，不自动修gold |

固定检索、Coding Agent、E-only编译和整批Agent均应允许同资源、缓存及版本查找。只有资源完整且输入隔离后，才比较一次轨迹提取是否比这些对照有实质收益。

本轮只读审计，未构造public快照、未改原标签、未运行模型或正式scorer、未运行测试套件。审计脚本重复运行确认数量，保留初始错误数字join的诊断并明确标记无效；没有科学有效性或整体污染率结论。下一增量查新独立来源，MSLR等待长E与可靠事实/gold契约后才重开。
