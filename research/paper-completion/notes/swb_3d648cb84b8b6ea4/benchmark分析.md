# 评测与边界

**实验 1（CrossDomainVAD-12 主结果）**：温度 0，三骨干使用相同提示；95% CI 为按领域分层的配对 bootstrap，1,000 次重采样（§4.2，p.6）。

| 方法 | GPT-5.5 | Seed2.0-lite | Qwen3.5-VL-27B |
|---|---|---|---|
| Direct（JSON） | 0.751 | 0.688 | 0.713 |
| AnomalyClaw | 0.814（+6.23） | 0.767（+7.93） | 0.748（+3.52） |

专用基线宏平均 AUROC（Table 1，p.7）：

| 专用基线 | 宏平均 AUROC |
|---|---|
| SubspaceAD | 0.760 |
| AnomalyDINO | 0.742 |
| AD-Copilot | 0.700 |
| VisualAD（0-shot） | 0.661 |
| AnomalyVFM（0-shot） | 0.606 |
| IAD-R1（0-shot） | 0.535 |

在 Qwen 上改用 logit Direct 后，单 Direct 从 0.713 升至 0.764，融合为 0.767（§4.3，p.6）。D4 Real3D-AD 上所有方法都接近随机（0.48–0.57）。

**实验 2（MMAD）**：AnomalyClaw+GPT-5.5 平均准确率 79.15%，GPT-5.5 Direct 为 76.20%；但 AgentIAD（82.88）和 AD-Copilot-thinking（82.29）等专用方法更高（Table 2，p.8）。

**实验 3（OSR）**：Qwen 上 0.7480→0.7689（+2.09，CI [−1.56, +5.60]）；GPT-5.5 上 +0.90，CI 同样跨零（Table 3，p.8）。

**成本**：每项平均 3.07–3.42 次 VLM 调用，Direct 为 1 次；最弱骨干长尾可达 5–8 次（§3.1，p.5）。

**边界**：OSR 在两分支几乎不分歧的领域不会触发，在 D8 上还写出偏向弱分支的规则，造成 −5.0 pp（§4.5，p.9）。AUPRC、FPR@95TPR 只在 SeedVL 上报告；ECE、像素级定位、阈值迁移不在本文范围（附录 R，pp.27–28）。DINOv2 预训练数据可能与 MVTec-AD 等公开数据统计相似，作者把这一点列为局限（附录 S，p.29）。

阅读者分析：Figure 1 写三骨干平均 Δ=+6.53 pp，而 Table 1 三个增益的平均约为 5.89 pp；若 Qwen 采用 logit 融合（0.767−0.713≈5.4），平均约 6.52，可能就是 Figure 1 的口径，但原文未说明（阅读者分析）。

依据：§3.1、§4.2–4.5、Tables 1–3，PDF pp.2、5–9；附录 R、S，pp.27–29。
