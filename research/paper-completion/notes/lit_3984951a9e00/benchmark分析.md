# 评测与边界

**基线与指标**：提示策略之间做受控对比；整体方法对比 DIN-SQL + GPT-4、C3 + ChatGPT、RESDSQL-3B + NatSQL 等已有方法（附录 C.3，Table 12）。指标为 EM 与 EX，另计每题平均提示 token 数（§4.1、§4.5）。

**实验 1（零样本问题表示，Spider-dev）**：

- 表示形式：OD 适合全部四个 LLM，配合 GPT-3.5-TURBO 执行准确率 75.5%；GPT-4 反而偏好最简单的 BS；AS 在除 GPT-4 外的模型上较差（§4.2、Figure 1，p.7）。
- 外键：对 OpenAI 模型的执行准确率提升 0.6–2.9 个百分点（TR+GPT-4 为 −0.2，AS+TEXT-DAVINCI-003 为 −0.4）。
- 规则：“with no explanation”一致提升，去掉后 OD 的 EX 下降 1.3–2.4 个百分点。
- 最划算组合：OD + 外键 + GPT-3.5-TURBO，EM 51.5%、EX 78.4%（§4.2，p.8）。

**实验 2（示例选择，全信息组织，Table 2，p.8）**：GPT-4 执行准确率如下。

| 选择策略 | 1-shot | 3-shot | 5-shot |
|---|---|---|---|
| Random | 77.4 | 79.4 | 79.5 |
| 问题相似 | 78.8 | 79.2 | 79.9 |
| 掩码问题相似 | 79.1 | 81.5 | 82.0 |
| DAIL 选择 | 80.2 | 81.7 | 82.4 |
| Upper Limit（用真实 SQL 选例） | 81.0 | 83.4 | 84.4 |

GPT-4 零样本为 72.3。DAIL 选择的查询相似度 0.94–0.95，接近 Upper Limit 的 0.97–0.98（Table 2）。

**实验 3（示例组织）**：配 DAIL 组织，GPT-4 的 EX 在 Spider-dev 从 72.3% 升到 83.5%，在 Spider-Realistic 从 66.5% 升到 76.0%；GPT-3.5-TURBO 和 TEXT-DAVINCI-003 加示例可能下降，较弱模型更适合全信息组织（§4.3.2、Figure 4，p.9）。

**实验 4（开源模型与微调）**：零样本最好为 CodeLLaMA-34B + CR，EX 68.5%（Table 3，p.10）。在 Spider 训练集微调后，LLaMA-13B + AS 达 EM 65.1%/EX 68.6%，LLaMA-33B + CR 达 EX 69.1%；但微调模型加入示例后准确率骤降（§4.4.4、Table 4，p.11）。

**实验 5（token 效率）**：全信息组织的 token 数是 DAIL 组织和仅 SQL 组织的数倍；DAIL 组织 + GPT-4 在与仅 SQL 组织相近的 token 成本下取得最高 83.5%（§4.5、Figure 7，pp.11–12）。DIN-SQL、STRIKE、CBR-ApSQL 的准确率取自原文报告值，token 数为估算，不是同条件复跑（§4.5，p.11）。

**实验 6（与已有方法对比，Table 12，Spider EX %）**：

| 方法 | Dev | Test |
|---|---|---|
| RESDSQL-3B + NatSQL | 84.1 | 79.9 |
| C3 + ChatGPT（零样本） | 81.8 | 82.3 |
| DIN-SQL + GPT-4 | 82.8 | 85.3 |
| DAIL-SQL + GPT-4 | 83.1 | 86.2 |
| DAIL-SQL + GPT-4 + 自一致性 | 83.6 | 86.6 |

（附录 C.3，p.18）

**局限**（§5，p.13）：只测试两条规则提示；微调仅用 Spider 训练集；数据库规模可能不足；指标只看正确性，不考虑生成 SQL 的执行效率。

依据：§4.2–4.5、§5、Tables 2–4、Figures 1–7，PDF pp.7–13。
