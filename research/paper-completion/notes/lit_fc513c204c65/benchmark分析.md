# 评测与边界

**指标**：相对 PostgreSQL 默认执行时间的收益 η；推理与检索延迟；每轮相对执行时间 RET = Σ SERAG 时间 / Σ PostgreSQL 时间（越低越好）。Overall 收益覆盖全部查询，Filtered 只计 SERAG 计划与 PostgreSQL 不同的查询。

**实验 1（与 PostgreSQL、Bao 对比，Table 2）**：SERAG 为 SFT 小模型、NoRef；Bao 在 JOB 上训练。

| 方法 | JOB Join Order | JOB Comp. Hint | CEB Join Order | CEB Comp. Hint |
|---|---|---|---|---|
| SERAG（NoRef） | 50.79% | 62.32% | 63.62% | 45.31% |
| Bao | 47.48% | （同左） | 22.60% | （同左） |

**实验 2（变体对比，Table 1，CEB，50 轮，取每条查询的最优计划）**：

| 模型 / 变体 | Join Order Overall | Join Order Filtered | Comp. Hint Overall | Comp. Hint Filtered |
|---|---|---|---|---|
| SFT LLaMA3.2-3B NoRef | 63.62% | 71.81% | 45.31% | 52.63% |
| SFT LLaMA3.2-3B LQORef | 20.09% | 35.87% | 36.80% | 39.65% |
| LLaMA3.1-8B NoRef | 12.84% | 62.86% | 9.31% | 25.18% |
| DS-Coder-7B LQORef | −7.98% | −183.50% | 1.36% | 0.98% |

（完整表另有 PGRef 及其余组合，见 p.4。）

**实验 3（自演化，Figure 4/5）**：CEB 上 50 轮 RET 波动较大；o3-mini 约 20 轮开始收敛，SFT-LLaMA 约第 50 轮才低于 PostgreSQL 基线，vanilla LLaMA 最好 RET 0.87，DS-Chat/DS-Coder 为 0.97/0.96。Stack 上 Complete Hint 模式下 RET 随轮次下降，仅以曲线呈现。

**边界**：

- 阅读者分析：Table 1/2 的收益来自 50 轮中每条查询的最优计划，相当于事后挑选，部署时的单轮表现应看 Figure 4 的 RET，后者大部分轮次接近或高于 1.0。
- 阅读者分析：摘要称执行时间平均少 36%，但 §4.4 的 520.67 vs 922.86 ms 折算约少 43.6%，与 Table 中 63.62% 也不同，论文未说明 36% 的计算口径（阅读者分析）。
- §4.2 写作“LLaMA3.1-3B SFT”，其余处均为 LLaMA3.2-3B，疑为笔误。
- Bao 只训练在 JOB 上，未给出训练时长，也不比较 FASTgres、Balsa 或两项 LLM 优化器；无方差、无多次运行。
- 作者在 §6 只将“提高生成效率和稳定性”列为未来工作。

依据：§4.1–4.5、Tables 1–2、Figures 4–5、§6，PDF pp.1、3–4。
