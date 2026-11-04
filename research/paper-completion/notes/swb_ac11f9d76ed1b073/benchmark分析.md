# 评测与边界

**基线**（§4.1，p.6）：有监督的 Ditto、HierGAT；无/自监督的 ZeroER、Sudowoodo；LLM matching（Peeters et al. 2025，零样本与 6-shot）。指标为 F1；成本以美元计，开源模型按 A40 云 GPU 时价和训练/推理时间估算。

**实验 1（总体，Table 4，p.7，8 个数据集平均 F1 / 成本 $）**：

| 方法 | GPT-3.5 Turbo | GPT-4o Mini |
|---|---|---|
| Matching | 64.02 / 4.52 | 67.80 / 0.46 |
| Matching（6-shot） | 69.99 / 32.75 | 77.94 / 3.21 |
| Comparing | 66.86 / 11.75 | 84.36 / 1.21 |
| Selecting | 81.60 / 1.71 | 82.26 / 0.17 |
| ComEM | 85.61 / 0.92 | 86.42 / 0.09 |

参照：Ditto 80.69、HierGAT 83.34、Sudowoodo 70.32、ZeroER 49.67。

**实验 2（位置偏差，Figure 3）**：匹配记录在候选列表中的位置越靠后，comparing 与 selecting 的 F1 越低；ComEM 可缓解（§4.3）。

**实验 3（开源 LLM，Figure 4、Table 6）**：8 个开源模型中 6 个以 selecting 最好、2 个以 comparing 更好；ComEM 在多数模型上最好，但 Solar-10.7B 的 ComEM（70.29）略低于其 selecting（70.60）（附录 C，p.13–14）。

**实验 4（排序能力，Figure 5）**：按 recall@1，matching 在各参数规模下都优于 comparing_all-pair（§4.4）。

**实验 5（消融，Figure 6）**：保留候选数 k 从 1 到 5，GPT-3.5 Turbo 波动大，GPT-4o Mini 较稳定（§4.5）。

**边界**：

- Limitations 节说明：LLM 选择受流行度、可得性和成本限制；模型可能在网页数据中见过这些记录甚至匹配结果，未来应在新数据或非公开数据上评测；只用了基础的零样本/少样本提示（p.9）。
- 实验只覆盖记录链接（两个数据源），未测单源去重。（阅读者分析）
- 结果为单次运行，未报告方差。（阅读者分析）

依据：§4、Limitations，Tables 3–4、Figures 3–6，PDF pp.6–9；附录 C、Table 6，pp.13–14。
