# usecase

原文 §3 给出的两个实例（PDF p.3，完整提示差异见附录 D）：

1. **目标歧义：bike-sharing-demand（DSBench）**。原提示写“predict count”，数据中有 count 列；歧义版本把该列改名为 val_1，加入经校准的诱饵 val_2，并把提示改成“predict value”。两列都是合理目标，只有 val_1 计分。附录 F 记录了一个智能体自行“发明”一种看似合理但无依据的目标组合而不提问（§5.2，PDF p.6）。
2. **指标歧义：aerial-cactus-identification（MLE-bench）**。原提示按 ROC-AUC 评估、提交格式 id,has_cactus；歧义版本数据、目标与格式完全相同，只把指标句改成“a standard evaluation procedure for this task”，智能体便不知道应提交概率还是硬标签。附录 F 的 random-acts-of-pizza 例子中，智能体在指标缺失时把 AUC 概率排序任务当成硬二分类（PDF p.7）。

在 Ask 条件下，理想行为是先探索数据、意识到存在两个候选目标或指标缺失，然后提出一个 ≤50 词的问题，例如询问应预测哪一列或使用什么指标；oracle 只回答被明确问到的内容。

阅读者分析：对语义查询/数据智能体系统而言，这类用例提示应把“目标列、指标、输出类型”作为显式参数检查，缺失时应拒绝执行或请求澄清，而不是默认补全。

依据：[arXiv:2605.09698v1，32 页](https://arxiv.org/abs/2605.09698)，§3、§5.2–5.3，PDF pp.3、6–7。
