# 评测与边界

**基线**（§7.1.3，p.9）：GPTuner、ResTune、LlamaTune、SMAC（BO 类），DB-BERT、CDBTune（RL 类，不训练神经网络），OpAdviser（自动选优化器）。**指标**：相对默认配置的延迟下降或吞吐提升（§7.1.4，pp.9–10）。

**实验 1（主结果，§7.2.1–7.2.2，Figure 6，pp.10–11）**：相对最强对手的提升——

| 基准 | 指标 | 提升 |
|---|---|---|
| TPC-H | 延迟 | 6.6% |
| JOB | 延迟 | 5.4% |
| CH-benCHmark | 延迟 | 19.2% |
| HyAdapt | 延迟 | 2.4% |
| TPC-C | 吞吐 | 9.4% |
| Twitter | 吞吐 | 6.2% |
| YCSB | 吞吐 | 12.3% |
| SmallBank | 吞吐 | 4.6% |
| HyAdapt | 吞吐 | 13.6% |

**实验 2（单次迭代算法耗时，Table 1，p.11）**：MCTuner 5.54 s、GPTuner 7.47 s、OpAdviser 6.39 s、ResTune 8.22 s、LlamaTune 2.06 s、SMAC 1.87 s、DB-BERT 14.61 s、CDBTune 0.54 s；不含负载执行时间。

**实验 3（knob 选择，§7.3.1、Table 2，pp.11–12）**：前 20 个 knob 与 SHAP 重叠数，TPC-C 上 MoE 14、CART 13、LASSO 8、zero-shot LLM 11；TPC-H 上 13、10、10、10。MoE 选择耗时 389.5 s/373.3 s，CART/LASSO 超过 3,400 s（TPC-C）。下游 BO 提升：MoE 在 TPC-C 12.9%、TPC-H 25.2%；LASSO 在 TPC-C 为 14.3%，略高于 MoE。

**实验 4（动态负载，Table 3，pp.12–13）**：warm-start 带来的提升为 0.1→1：10.5%，1→10：20.4%，10→1：12.0%，1→0.1：8.1%。作者也指出迁移后最好的配置不一定是上一阶段最好的，在线继续调优仍必要。

**实验 5（消融，§7.4.2–7.4.5，Figure 8–11，p.13）**：加入空间分解后，四种 BO 变体在 TPC-H 提升约 65%、Twitter 超过 50%；TPC-H 上 MoE 比 zero-shot LLM 多 12.1%，空间分解比纯 BO 多 39.8%；knob 数从 20 增到 30 时收益趋平。

**边界**：论文没有独立的局限章节；未来工作仅提多数据库与实时适配（§8，p.14）。阅读者分析：结果多为单次运行的曲线，未报告重复次数或方差；仅在 PostgreSQL 一个 DBMS 上评测；LLM 型号表述前后不一。
