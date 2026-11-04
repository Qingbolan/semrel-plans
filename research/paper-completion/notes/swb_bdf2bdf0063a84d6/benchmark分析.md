# 评测与边界

**实验 1（主结果，Table 2）**：Longformer/BigBird 截断到 2,048 token，其余模型 512 token；指标为准确率，5 个种子平均。

| 设置 | 模型 | 准确率 |
|---|---|---|
| Full Text | Longformer / BigBird | 62.87±2.06 / 63.26±3.40 |
| Unified Allegations | BERT / LegalBERT / CaseLawBERT / LegalRoBERTa | 65.06 / 65.57 / 65.87 / 65.95 |
| Separated Allegations | BERT / LegalBERT / CaseLawBERT / LegalRoBERTa | 64.98 / 65.57 / 66.82 / 65.97 |

作者认为指控比事实更有信息量；法律预训练模型只比 BERT 高约 0.5–2 个点。附录中过滤超长文本（Table 3）结果变化不大，XGBoost 分类头（Table 4）无提升，预处理中只有词干化有帮助。

**实验 2（校准，Table 5）**：Unified Allegations 上 TS 前 ECE 约 23–28，TS 后约 1.9–5.1；法律模型校准前更差、校准后更好。

**实验 3（人类专家，§7、Table 6）**：200 件上专家准确率 53%，Longformer 63%；只看专家把握为 4–5 的 45 件，专家 60%，Longformer 67%。Full Text 上 Longformer 的 ECE 经 TS 从 5.14 降至 2.34，专家为 17.5。

**边界**：作者承认最佳准确率仅约 66%，可能是任务困难或模型优化不足；只用到 512/2,048 token，未用 4,096 或层次模型；可解释性分析有限。另：专家为公司员工和法学院末年学生，样本仅 200 件（阅读者分析：统计功效有限，原文未报告显著性检验）。

依据：[arXiv:2211.00582v1，16 页](https://arxiv.org/abs/2211.00582)，§5.3、Table 2、§6.1、§7、§8 Limitations，附录 B Tables 3–6，PDF pp.6–9、14–15。
