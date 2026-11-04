# 工作负载

**原始数据（附录 B.1、Table 6，pp.12–13）**：7 个公开基准的官方训练集（HuggingFace 快照），分 4 个任务组。

| 任务组 | 基准 | HF ID | #Train | 评测指标（Table 9） |
|---|---|---|---|---|
| 通用指令 | Alpaca | tatsu-lab/alpaca | 52k | AlpacaEval 2.0 win-rate |
| 选择题 QA | ARC-Easy / ARC-Challenge | allenai/ai2_arc | 5.2k / 2.59k | Accuracy |
| 数学推理 | GSM8K(main) / MATH | openai/gsm8k、EleutherAI/hendrycks_math | 8.79k / 12k | Exact match |
| Text-to-SQL | Spider / BIRD | xlangai/spider、xu3kev/BIRD-SQL-data-train | 8k / 9.43k | Execution accuracy |

**采样与预算（附录 B.1，p.13；§4.2，p.4）**：1k / 5k 指准备后最终 SFT 实例数；训练集多于 5k 的数据集以固定随机种子抽 5k 原始实例作为来源池，少于 5k 的全部使用；三种方法共享同一来源池。GSM8K 与 MATH 合成一个数学原始池，但分别评测。

**Seed（附录 B.2，pp.14–15）**：主设置每任务 20 条人工构造 seed，规定字段、输出结构和答案规范化；附录给出四类 seed 示例（如 BIRD california_schools 的 SQL seed 含 schema_context、join_keys、evidence）。鲁棒性实验用 5 条 seed、重采样的 B/C 两组以及跨 GSM8K/MATH 的 seed 来源迁移（Tables 13–15）。

**训练/评测配置（附录 C，pp.15–16）**：三骨干 Qwen3-8B-Base、Gemma-3-4B-it、Llama3.1-8B-Instruct；ms-swift 全参 SFT（lr 2e-5、2 epoch、最大长度 15,000），OpenCompass + vLLM 评测（温度 0，最大输出 2,048）。主表共 42 个“模型–预算–基准”设置（§4.3，p.5）。

阅读者分析：工作负载是“训练集改写 → SFT → 标准测试集”，原始数据与评测基准同源（如 Spider 训练集准备后在 Spider 上测），并非开放域或跨域数据准备；未报告准备后数据的去重/泄漏检查。
