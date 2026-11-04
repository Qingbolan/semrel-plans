# LawReasoningBenchmark原始发布核验

已下载ACL2025.findings-acl.887完整论文及官方仓库commit `3c1d92baad38b00274694274df9787e04678ea2f`，797文件ZIP14,911,550 bytes。哈希及逐文件计数见artifact/evidence/shared-environment-lawtree。

| 条件 | 本次观察 |
|---|---|
| 实际数据 | dataset/test的task1/2/3输入与标签各100记录，ALL亦100；不得相加成700独立cases |
| q | 从判决描述生成待证事实、证据连接和经验解释树；不是单纯批准/拒绝决策 |
| E | 经验解释是subtask3输出，由LLM起草后人工修订；尚未发现足以证明长共享规则依赖的公开环境 |
| gold隔离 | 第一条Case_info保留明确罪名和十二年刑期及法院采信结论，只隐藏其中一段最终认定事实。不能把该输入用于无答案泄漏的定罪评估 |
| 适用边界 | 适合考察判决书结构重建；不能直接纳入当前Strong逐案决定工作负载 |

| Query | 数据湖1 | 数据湖2 |
|---|---|---|
| 重建判决推理树（原任务） | 100判决描述 | 私有树标注；不是模型资源 |
| 类Python DAG | scan → sem_map(extract_and_link) → output(tree) | evaluate only；未知正确数量 |

| LOTUS预期结果 | LOTUS过程 | Agent预期结果 | Agent过程 | operator结构 |
|---|---|---|---|---|
| 未运行，未知 | 固定分步事实抽取/证据链接/树组装 | 未运行，未知 | ==检查判决结构与证据对应关系== → 抽取/链接/核验树 | 树输出contract，不能偷换为独立裁决 |

四比较臂均无本次运行。20例gold审计未开展，因为已定位当前任务与输入边界，不为凑数将结构重建改称新裁决。当前不进入正式38候选计数；无Strong升级。原论文§3描述人机协作标注，不把生成经验称为未经模型介入的专家SOP。

来源：https://aclanthology.org/2025.findings-acl.887.pdf；https://github.com/cocacola-lab/LawReasoningBenchmark 。
