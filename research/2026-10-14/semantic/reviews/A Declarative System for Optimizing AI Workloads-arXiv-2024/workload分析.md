# workload分析

| 工作负载 | 实际输入表/文件与列 | 数据环境需求 | gold与输出 |
|---|---|---|---|
| Legal Discovery | 1000个Enron邮件文本；File.filename、contents，convert产生sender、subject | 无独立外部数据；预注册enron-eval文件集合 | 人工50正例、30具有欺诈关键词但非欺诈例，其余随机；输出符合两条件邮件，F1 |
| Real Estate | 100房源，每行listing、text_content、image_contents列表；每房源最先3张去重图 | MIT距离条件和价格范围UDF；正文未给距离函数完整实现，不虚构地图服务 | 人工23条满足全部条件；F1 |
| Medical Schema Matching | 11电子表格文件→49表；表头/行转换为患者CaseData | 15属性目标schema是任务规范，人工harmonized table只作gold | 筛选患者年龄表并列映射，micro-F1 |

证据§5.2及图3/5/9。图3source=enron-emails与实验登记enron-eval是论文自身命名差异，记录时保留出处。图9的完整CaseData还带filename/study，不把15个医学目标属性误当所有字段数。

主执行为iterator逐记录阻塞；§5.5每convert/filter用32workers，算子间无流水，必须等整个算子完成。32是并发workers，不是32条输入合成prompt的batch size。sentinel使用5%输入，医疗1/11文件，是优化采样。论文没有给统一模型batch size或联合提交多查询合同。

来源：[原论文](https://arxiv.org/abs/2405.14696v2)。本分析据所列版本全文核读，未复现实验。
