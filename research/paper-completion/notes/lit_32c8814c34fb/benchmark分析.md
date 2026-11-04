# 评测与边界

**比较对象（§4.1，p.4）**：Vanilla SFT（原始数据直接训练）、DataFlow-SFT（LLM 数据准备系统 DataFlow）、DataEvolver-SFT；另列基座模型不训练的分数作参考。

**主结果（Table 1，p.5）**：作者报告相对 Vanilla 平均约 +10 分、相对 DataFlow 约 +2 分，为 0–100 尺度上的未加权描述性平均（§4.3）。

- 例：Llama3.1-8B-Instruct 5k 下 Alpaca 52.5（DataFlow 48.0，Vanilla 39.4），BIRD 52.85（49.05，43.18）。
- 并非每格都最好：Qwen3-8B-Base 的 MATH 上 DataFlow 5k 69.28 高于 DataEvolver 5k 68.42；Llama 5k 的 GSM8K 上 Vanilla 89.43 高于 DataEvolver 89.34。
- 作者还称 1k DataEvolver 数据可接近 5k 的效果。

**其他结果**：
- 数据质量（Fig.3，p.6）：LLM judge 1–5 分，四维度 training-readiness、seed alignment、explanation quality、redundancy；人工–judge Spearman 0.84–0.91（Table 17）。
- 成本（Table 2，p.6）：每条训练样本准备 token 宏平均 3,402 → 1,983（−40.1%）；附录 Table 10（p.17）同一指标写为 1,978、−40.3%，Alpaca 1,225 与 1,218 也不一致，两表数值有小差异。端到端墙钟时间 ≈2.52h → ≈1.63h（Table 18，并发 1，5k 条）。
- 消融（Table 3）、失败类型（Table 4）、seed 数量/重采样/来源迁移（Table 5、13–15）、等 token 训练对照（Table 19，仅 Alpaca/ARC 的代表性子集）。

**局限（Limitations，p.9 及阅读者分析）**：作者承认只做文本数据；seed 与 LLM 反馈会影响所推导的质量要求；与近期 agentic 系统没有匹配实验。阅读者补充：系统基线只有 DataFlow；所有结论基于单次运行（只有 seed 重采样给出了标准差）；驱动系统的 LLM 未在正文写明；等 token 对照只覆盖 3 个基准。
