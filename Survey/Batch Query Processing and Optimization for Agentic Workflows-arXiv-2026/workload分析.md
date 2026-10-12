# Workload 分析

**要验证的问题。** 检验固定逻辑工作流下跨查询调度、工具调用合并、CPU/GPU协同能否降低整批延迟并提高在线吞吐。

**数据、任务单位与gold。** 六种明确标注为synthetic yet representative的DAG：IMDb Diamond/TripleChain、FineWiki LongChain/Bridge、TPC-H Trident/Fanout（名称以表3为准）。底层FineWiki/IMDb是公共数据，IMDb关系库超过2亿行；TPC-H为合成分析数据。主批量N=1024，并测扩展至2K。单位是一条工作流请求；主要指标延迟、吞吐、GPU时间、优化耗时，不提供独立业务答案gold准确率实验。

**具体use case：输入目标 → 使用前 → 使用后。** 原文表3/图5的TPC-H Fanout作说明：输入一批参数化分析请求，目标汇总多个SQL分支的分析结果。使用前各Agent重复同一SQL调用并等待LLM；使用后同签名调用合并、相同提示前缀共享，并安排模型与工具重叠。这是作者设计的调度负载，不是真实用户执行日志。

**Baseline与比较条件。** 比较逐查询串行驱动的vLLM、逐层最大batch的OpWise、LangGraph1.0.4、AgentScope1.0.9、Parrot0.1.0；还有MILP优化oracle和消融。vLLM基线缺少跨查询并行，不能用其差距代表所有优化serving。关注相同DAG上的OpWise/Parrot等比较，并计入优化时间。

**证据边界。** 固定逻辑DAG、不在线改变结构、单机多GPU；真实底层数据不等于真实开放探索任务。不能由此推断Data Maze普遍或Agent无法批处理。

来源：[阅读版本](https://arxiv.org/abs/2509.02121v2)，§6.1–6.8、表3、图5–6。本文为原文工作负载分析，未复现实验。
