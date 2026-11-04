# 工作负载

**微调数据**（Table 1，PDF p.3）：

| 任务 | 数据集（实例数 / 正例数） |
|---|---|
| ED | Adult 550×2 / 35×2；Hospital 1710×2 / 44×2 |
| DI | Buy 586；Restaurant 778 |
| SM | MIMIC-III 7000 / 11；Synthea 5000 / 18 |
| EM | Amazon-Google 6874 / 699；Beer 359 / 54；DBLP-ACM 5000 / 885；DBLP-GoogleScholar 5000 / 924；Fodors-Zagats 757 / 88；iTunes-Amazon 430 / 105 |

这些数据取自 Narayan et al. 2022 公开版本，ED/DI 的错误与缺失值已预先注入（§3.1，PDF p.3）。推理数据另有四档，例如 reasoning-8k 为 ED 3056、DI 1364、SM 2000、EM 2000，共 8420（Table 2，PDF p.5）。

**测试数据**（Table 3，PDF p.6）：

| 任务 | 已见数据集（测试实例数） | 未见数据集（测试实例数） |
|---|---|---|
| ED | Adult 9900；Hospital 17101 | Flights 12832；Rayyan 8997 |
| DI | Buy 65；Restaurant 86 | Flipkart 2675；Phone 1194 |
| SM | MIMIC-III 6408；Synthea 2964 | CMS 2564 |
| EM | Amazon-Google 2293；Beer 91；DBLP-ACM 2473；DBLP-GoogleScholar 5742；Fodors-Zagats 189；iTunes-Amazon 109 | Abt-Buy 1946；Walmart-Amazon 2049 |
| CTA | — | SOTAB 250 |
| AVE | — | AE-110K 1482；OA-Mine 2451 |

“已见/未见”指数据集是否参与 Jellyfish 微调；Walmart-Amazon 的商品类别与微调用的 Amazon 数据不同（Table 3 注，PDF p.6）。对非 LLM 方法，所有数据集都是已见的，因为它们需在目标数据上微调（§5.2，PDF p.6）。

**评测设置**：已见数据集零样本，未见数据集少样本（每数据集 3 例，含正负例）；只用通用知识，不用数据集特定知识（§5.1，PDF pp.5–6）。

DI 已见测试集很小（Buy 65、Restaurant 86），单个实例约影响 1.2–1.5 个百分点，表中 DI 已见数据集的差距应谨慎解读（阅读者分析）

依据：§3.1、§5.1–5.2、Tables 1–3，PDF pp.3–6。
