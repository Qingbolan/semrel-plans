# 基准评测

§6.1：2×AMD EPYC9755、2.2TiB RAM、3×H200 NVL（各141GiB）；Qwen3-14B/32B和GPT-OSS20B。vLLM0.11.0、SGLang0.5.6、PostgreSQL18.0；对照vLLM逐query执行、OpWise、LangGraph1.0.4、AgentScope1.0.9、Parrot0.1.0。

§6.2 N=1024时W1 Halo676秒、OpWise1595秒约2.4倍；W5/W6对编排框架2.4–3.6倍。naive vLLM的约400倍来源于逐query完成后才开始下一条的基线，不代表对现代并发框架400倍。

表4 N=256：W1 Halo323.64秒/求解2.24秒，MILP322.17秒/求解1.44小时；W6 Halo545.55秒/1.15秒，MILP544.06秒/172.84秒。Opt=1是相邻GPU节点依赖对的匹配分数，不是答案准确率。

表5移除request coalescing使W1延迟+16%、W6+154%；去机会执行W6+56%。在线W5 Halo0.85QPS、LangGraph0.33QPS约2.58倍；纯LLM三节点W+为4.57对4.22QPS。论文结果聚焦性能，未提供可独立核对的每query输出质量表。
