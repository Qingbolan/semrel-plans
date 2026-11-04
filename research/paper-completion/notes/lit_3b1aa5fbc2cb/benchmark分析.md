# 评测与边界

**基线**（§7.1，p.8）：Lotus v1.1.4（用户给定计划 + 代理级联）和 Palimpzest v1.5.3（优化器重排算子、选择实现）；两者都是算子逐个执行、请求中心 serving，底层统一为 vLLM v0.13.0rc4、开启自动前缀缓存。Lotus/Palimpzest 默认最大批 64；所有系统谓词类调用 token 上界为 8；Palimpzest 关闭 reasoning_effort 以免提示变长。硬件：4× RTX Pro 6000（96 GB）、张量并行；默认 90% 显存给 vLLM。贪心解码，每个实验跑 3 次取平均。

**指标**：端到端查询完成时间（延迟）、oracle LLM 调用数。论文没有报告查询结果准确率或任何输出质量指标。

**主要结果**（§7.3，Figure 7）：

| 工作负载 | Lotus | Palimpzest | Kalypso | 加速 |
|---|---|---|---|---|
| FEVER | 258.1 s | — | 172.6 s | 1.49× |
| MEDEC | 714.6 s | 808.2 s | 464.3 s | 1.54× / 1.74× |
| BioDEX | 910.3 s | — | 703.4 s | 1.29× |
| ContractNLI | 正文未给秒数（按 4.57× 推算约 4,855 s，阅读者计算） | 2,373.4 s | 1,062.4 s | 4.57× / 2.23× |

Figure 7 的倍数以 Lotus 为 1.00×；Palimpzest 在 MEDEC 为 0.88×、ContractNLI 为 2.05×。

**消融**（§7.4）：
- 流水线 vs 阻塞（Kalypso 内部）：1.20–1.83×（Figure 9；FEVER 506→421、MEDEC 602→464、BioDEX 946→703、ContractNLI 1940→1062 s）。
- 固定两阶段预算比例 vs 自适应：BioDEX 最佳固定比例 3:7、ContractNLI 为 1:9，无一固定比例两者皆优；自适应在 0.9 与 0.6 显存利用率下都优于最佳固定比例（Figure 10）。
- 虚拟 pin vs 显式 pin：性能相近，显式在 FEVER/BioDEX/ContractNLI 略快，虚拟在 MEDEC 更快（Figure 11）。
- token 上界：MEDEC 上固定 1 到 8k 的上界都不如 Kalypso 默认估计（0.9 显存下 495 s）（Figure 12）。
- 显存从 0.9 降到 0.5（约 190.6→38.6 GB KV cache）：MEDEC 上 Kalypso 延迟仅增 9%，Lotus 增 44%、Palimpzest 增 29%（Figure 8）。

**边界（阅读者整理）**：
- 比较条件不完全一致：MEDEC 与 ContractNLI 上 Lotus 用代理级联而 Kalypso 只用 oracle（作者以小模型高度非确定为由）；FEVER 上两者 oracle 回退数为 183.3 对 243.6。论文以“调用数相近”论证加速来自执行效率，但未报告结果质量是否一致。
- 只评测一个 oracle 模型和一种硬件；只有 4 个工作负载，每个 3 次运行，未报告方差。
- 只支持静态左深计划，CP 右侧必须是静态表（§4）。
- 死锁只在压力测试中观察到（§6），未给出频率或恢复代价。

依据：[arXiv 2607.23815v2](https://arxiv.org/abs/2607.23815)，§4、§6、§7、Table 2、Figures 7–12，PDF pp.4–12。
