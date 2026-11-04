# 工作负载

**任务来源**：用户接入的数据环境，或从 Spider、LiveSQLBench、SpreadsheetBench 中采样的环境（§2，PDF p.2）。原文没有给出任务池规模、各来源占比或任务难度分布。

**合成产物**：Figure 2 标注 “TOFFEE-30K Trajectories”；§4.3 称推理模式维护一个“在数百个数据环境上合成的 30K 条轨迹库”（PDF pp.3–4）。具体环境数、每环境任务数原文未给出。

**下游评测**：KramaBench 与 DSBench；TOFFEE-9B / TOFFEE-27B 分别由 Qwen3.5-9B / Qwen3.5-27B 微调（§3，PDF p.3）。原文未说明使用的评测子集、题目数或评分口径（Figure 3b 纵轴仅为 “Overall Score”）。

**运行环境**：Ubuntu 服务器，合成 worker 通过 OpenRouter 调用 LLM；Best-of-N 取 N=5；Figure 3a 横轴是每任务合成预算（美元，约 0.1–2.0）（§3、Figure 3a，PDF p.3）。

**演示用例规模**：场景 1 的学校数据库有 3 张表、17K 行（§4.2，PDF p.4）。

阅读者分析：本文的负载单位是“数据环境 × 分析任务 → 轨迹”，与语义算子查询不同；它更接近为数据分析智能体生成训练/示例数据的数据管理问题。
