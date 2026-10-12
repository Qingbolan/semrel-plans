# workload分析

**验证什么。** 相同请求内容通过行/字段重排能否增加前缀缓存命中，从而降低批量LLM推理耗时和费用，而不是通过少处理记录取巧。

**数据、单位与gold。** 7公开数据源、16查询、5类型（filter、projection、连续调用、aggregation、RAG）。表1规模：Movies15,000、Products14,890、BIRD14,920、PDMX10,000、Beer28,479、SQuAD22,665、FEVER19,929行。源是真实评论、音乐/QA等数据；查询由作者构造。单位是逐行请求及整批任务。主要指标端到端延迟、API费用、缓存命中；部分filter人工标注检查质量，不是16查询全部有独立gold验证。

**最有说服力用例（§6.1任务重述）。** 对同一商品的大量评论判定情绪。使用前重复商品字段散在不同前缀，已有缓存也难共享；使用后把相同商品/字段组织在可共享前缀和相邻行中，仍逐条产出标签，但减少重复prefill。共享模型状态不等于共享评论结论。

**baseline及公平性。** Cache(GGR)对No Cache及Cache(Original)；统一Llama3-8B、vLLM、单L4，另测70B/8L4及GPT-4o-mini、Claude3.5Sonnet成本。精确OPHR只作小规模分析，因搜索昂贵未用于大表端到端对照。字段重排可能改变输出，论文质量检查范围有限。

**效果范围。** §6.1–6.2、表1、图3–4：16查询相对Cache(Original)为1.5–3.4×，相对No Cache为1.8–3.8×；最高32%费用节省属于论文当时API计价/配置，不是任意任务或当前价格。

来源：[MLSys2025正式版本](https://proceedings.mlsys.org/paper_files/paper/2025/file/b5dc49f44db2fadc5c4d717c57f4a424-Paper-Conference.pdf)。本分析为原文重述与比较边界判断，未复现实验。
