# 基准评测

§7.1环境为AMD EPYC9554、2×94GB H100 NVL，Qwen3-8B/14B，每GPU独立模型引擎；各LLM使用greedy采样。对照vLLM、OpWise、LangGraph、AgentScope、Parrot、KVFlow；KVFlow使用其SGLang实现，其余主要用vLLM0.16.0。

表2微基准相对KVFlow最大1.56倍、平均1.32倍；§7.2复杂Trading相对KVFlow最大1.34倍。表4单独关闭主动KV与结果缓存后，调度149.76秒，LSPF188.93秒，Random193.54秒，OpWise419.03秒，QueryWise658.54秒。

表5小规模MILP比较平均最优gap0.9%、最大3.6%，每例求解上限6小时。端到端延迟包含Helium优化调度；热身、工作流profiling和模型/输入规模需要与每项实验一起读。未独立重测输出等价或速度。
