# 评测与边界

**基线**：非 LLM 方法 HoloDetect、Raha（ED），IPM（DI），SMAT（SM），Ditto、Unicorn（EM），RoBERTa（CTA）；LLM 方法 GPT-3、GPT-3.5、Table-GPT、GPT-4、GPT-4o、Stable Beluga 2 70B、SOLAR 70B。基线数值均引自先前工作中报告的最佳结果（§5.1，PDF p.6）。**指标**：DI 用准确率，ED/SM/EM/AVE 用 F1，CTA 用 micro-F1，均为百分制（§5.1，PDF p.6）。

**实验 1（已见任务，Table 4，PDF p.7）**：GPT-4 在 19 个数据集中 11 个最好，Jellyfish-13B 7 个最好。

| 模型 | 19 个数据集平均分 |
|---|---|
| 非 LLM 最佳 | 80.44 |
| GPT-4 | 84.17 |
| GPT-4o | 72.58 |
| Jellyfish-7B | 82.74 |
| Jellyfish-8B | 81.55 |
| Jellyfish-13B | 86.02 |

13B 的平均优势很大程度来自 SM 的 CMS（59.29 对 GPT-4 的 19.35）（§5.2，PDF p.6）。

**实验 2（未见任务，Table 5，PDF p.7）**：CTA 上 GPT-4 最好（91.55），Jellyfish-7B/13B 为 83.00/82.00；AVE 上 Jellyfish-8B/13B 在两个数据集都超过两个 70B 模型，AE-110k 上超过 GPT-4（59.55/58.12 对 55.50），但 OA-Mine 上 GPT-4 为 68.90，明显更高。

**实验 3（相对基座提升，Table 6，PDF p.7）**：平均分 Mistral-7B 44.17→80.14，Llama 3-8B 60.69→79.30，OOP2-13B 61.60→83.21。唯一下降是 8B 在 Flights 上（−1.50）。

**实验 4（NLP 能力保持，Table 7，PDF p.7）**：Open LLM Leaderboard 六项平均分下降 1.32（7B）、0.56（8B）、0.36（13B）。

**实验 5（数据配置与推理数据，Figures 3–4，PDF p.8）**：ED、SM 数据对其他任务普遍有益，DI、EM 有负迁移；推理数据对 7B/8B 先升后降，对 13B 始终低于不加推理数据的水平，因此 13B 不用推理数据。

**实验 6（效率与解释）**：单张 A100 每实例 0.07/0.08/0.15 秒（7B/8B/13B），GPT-4 约 1–8 秒；前缀缓存使 8B/13B 批处理提速 1.31/1.27 倍（§5.7，PDF pp.8–9）。GPT-4o 两两评判解释质量时，Jellyfish-7B 胜率 46.36%，8B 为 73.18%，各 220 次比较（附录 C.4 Table 13，PDF p.18）。

**边界**：Limitations 承认只覆盖六类任务；推理数据损害 13B；按实例而非按表处理，受 token 上限（13B 为 4096）限制，大规模数据效率较低；ED 误报后再做 DI 可能引入新错误；只处理关系表，不处理扫描件或层次表（PDF p.10）。

基线数值来自不同论文，提示与少样本设置未必一致，跨行比较只能作参考（阅读者分析）

依据：§5、Tables 4–7、Figures 3–4、Limitations、附录 C.4，PDF pp.5–10、18。
