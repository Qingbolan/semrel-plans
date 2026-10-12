# workload分析

**验证什么。** 查询与实际数据建立关联、发现桥接实体后再编译语义管线，是否比直接生成代码或搜索修复得到更好的最终答案。

**数据、单位与gold。** MMQA、HotpotQA、HybridQA、ManyModalQA、TAT-QA，每集按题型抽300题；三个后端Palimpzest/LOTUS/Nirvana。任务单位是问题及给定上下文，公开人工QA标签作参考；输出测EM、token F1与LLM judge，同时分开mapping/execution延迟及费用。Codex Agent只在6个后端—数据集组合各100题子集比较，不是全量同表。没有批量记录共享实验。

**最有说服力用例（图1原始案例重述）。** 给南摩拉维亚城市人口表和节庆文本，问“人口比Boskovice少、比其他城市多的城市的民俗节多久举办”。使用前只把问题词面接到来源会漏掉未明说的城市；使用后从人口条件找到Kyjov桥接实体，再匹配节庆段落回答频率。不得用图示城市的中间值当成整个数据集的测量收益。

**baseline及公平性。** Naive单次代码生成、Hardcoded按题型模板、CodeTree最多10轮执行修复、Codex(model)、Codex(agent) best-of-3。NL2Pipe和非Codex用gpt-5-mini，Codex用gpt-5.1-codex-mini；执行后端均gpt-5-mini。Hardcoded是LLM模拟人写predicate，mapping费用不比较。后端—数据集的离线profile/参考文档生成可摊薄，但非零总成本；在线指标不能含糊写作全部准备费用。

**证据与界限。** §3.3、§3.6、§4.0–4.2、表1–4。复杂跨源任务改善更明显；Phase A读取实际数据上下文，不能描述为只读schema。当前实验不证明巨大未知环境的取证效率，也不证明条件计划不能覆盖任务。

来源：[v1，2026-06-03](https://arxiv.org/abs/2606.04641v1)。本分析为原文重述与比较边界判断，未复现实验。
