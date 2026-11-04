# 工作负载、输入和批处理

表2与§7.1列55条SemBench查询，附录J逐条给意图和核心代码（省略数据加载等）；BioDEX另1条。Medical场景因许可未纳入本评测。

| 场景 | Query数 | 论文实际输入表/列与规模 |
|---|---:|---|
| Movie | 10 | Reviews，20000行；ReviewText；查询还使用movie/review标识 |
| Wildlife | 10 | ImageData4000行：Image/City/StationID；AudioData650行：Audio/City/StationID |
| MMQA | 11 | LizzyCaplanText、BenPiazzaText、TampaInternationalAirport、Images各300行；Title/Text、Airlines/Destinations、Image |
| Cars | 10 | CarComplaint99929行Summary；CarImage19156行Image；CarAudio871行Audio；关系字段用于关联和筛选 |
| E-Commerce | 14 | StyleDetails5000行；ProductDisplayName/ProductDescriptors/Images及结构属性 |
| BioDEX | 1 | 1000篇文章×100个reaction候选；文章由title/abstract/相关章节组合；RP@5 |

查询环境为给定关系、可访问的图片/音频资源，以及算子/模型目录；不需要开放Web搜索。可选验证数据供计划选择，不能并入查询事实表。

§6.1使用DataFrame支持向量化/批推理，未给统一每请求记录batch size。parallelism20是并发数，验证50是样本数，LIMIT5/10/100或TopK是结果限制。默认阈值N≤300直接LLM执行。主实验关闭plan cache；表4另列复用计划后的摊销开销，不能当成联合执行多query的benchmark。
