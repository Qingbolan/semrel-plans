# Workload 分析

**要验证的问题。** 检验看见完整工作流的结果缓存、KV缓存和调度能否减少重复计算与依赖等待。

**数据、任务单位与gold。** 五种构造的primitive workflows：MapRed、Debate、Reflect、Iterative、Parallel，使用MMLU、TAT-QA、Amazon Reviews；Amazon分别采200/100个商品，每项60评论分6块。Trading组合19个Agent、88个LLM算子，模拟财务/新闻/社交/价格分析。单位是工作流请求/批次，主要指标端到端墙钟延迟，非投资收益或最终答案准确率。

**具体use case：输入目标 → 使用前 → 使用后。** 原文图6/§7：多次交易分析请求中的公司基本面和部分社交分析已有缓存。使用前重复执行整个分支；使用后CacheFetch替换可复用结果，其他分支继续推理并安排KV局部性。缓存命中是假定输入和确定性条件满足的场景，不意味着昨日行情能当今日行情。

**Baseline与比较条件。** vLLM、OpWise、LangGraph、AgentScope、Parrot和KVFlow；除KVFlow外共享vLLM0.16.0并启用prefix caching/chunked prefill，greedy sampling，同机H100。延迟包括Helium优化/调度开销。最高约100倍来自朴素vLLM串行基线，面向KVFlow的最大值为1.56倍（表2），不可混说。

**证据边界。** 模拟工作流验证服务效率，不独立验证业务质量；§9承认动态loop/map表达及外部API成本限制，同时指出可加入控制流原语静态表达。

来源：[阅读版本](https://arxiv.org/abs/2603.16104v1)，§6–7、表1–3、图6–8、§9。本文为原文工作负载分析，未复现实验。
