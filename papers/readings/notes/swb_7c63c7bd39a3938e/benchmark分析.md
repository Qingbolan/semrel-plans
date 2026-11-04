# 评测与边界

**实验 1（同域基线，Table 1，PDF p.2）**：全监督下 FlanT5-base 与 Ditto（RoBERTa-base）F1 接近，如 Abt-Buy 89.92 vs 89.33、WDC-Shoes 90.20 vs 88.07；Mistral-7B ICL 少样本仅 18.53–53.94。

**实验 2（分布外，Table 2，PDF p.4）**：指标为 F1，比较 BL、EA-Alpaca、EA-Mistral。

| 例子 | BL | EA-Alpaca | EA-Mistral |
|---|---|---|---|
| Amazon-Google → Beer | 70.27 | 90.80 | 92.30 |
| WDC-Computers → WDC-Cameras | 73.26 | 91.26 | 93.77 |
| Walmart-Amazon → iTunes-Amazon | 51.72 | 72.19 | 75.63 |
| Walmart-Amazon → Abt-Buy | 63.75 | 72.84 | 67.52 |

平均提升：跨 schema 22.32、跨领域 14.47、跨分布 13.67（§2.3，PDF p.5）。

**实验 3（消融 A–E，Table 3、Figure 3，PDF pp.5–7）**：相对 EA-Mistral 的聚合 F1 变化：

| 消融 | 改动 | 聚合 F1 变化 |
|---|---|---|
| A | 乱码解释 | −26.99 |
| B | 随机删词 | −5.57 |
| C | TF-IDF 删词 | −5.69 |
| D | 通用（与实例无关）解释 | −14.35 |
| E | 随机替换为 `<unk>` | −4.98 |

Figure 3 中有解释平均 74.22、无解释 59.34。原文指出 E 的影响在不同组合间不一致，例如 iTunes-Amazon → Walmart-Amazon 上明显更差（PDF p.7）。

**实验 4（人工，§3，PDF pp.7–8）**：H1 见 usecase；H2 由三位作者标注 300 条解释，10.9% 有内在错误、15.1% 含幻觉，Fleiss κ 为 0.75 / 0.86。

**实验 5（附录 D/E，PDF pp.14–15）**：BL 下 Ditto 平均 F1 55.28、FlanT5 59.28；5 个指令模型少样本均不如训练后的小模型。

**边界**：主要是"单源训练、N−1 测试"；只有 WDC-All 一组接近留一领域设置。仅英文电商类数据，单一学生模型，无端到端成本或延迟测量；摘要写 ↑10.85、Limitations 写 ↑10.86，口径未说明（Limitations，PDF p.9）。
