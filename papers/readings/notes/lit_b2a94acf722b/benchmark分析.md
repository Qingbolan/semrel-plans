# 评测与边界

**实验 1（主结果，Table 1）**：准确率（%），三种 LLM 及平均：

| 方法 | Qwen WikiTQ | Qwen TabFact | LLaMA WikiTQ | LLaMA TabFact | 4o-mini WikiTQ | 4o-mini TabFact | 平均 WikiTQ | 平均 TabFact |
|---|---|---|---|---|---|---|---|---|
| Chain-of-Table | 68.3 | 89.7 | 62.1 | 89.9 | 67.5 | 88.9 | 66.0 | 89.5 |
| Critic-CoT | 69.0 | 89.8 | 66.8 | 88.0 | 66.3 | 86.9 | 67.4 | 88.2 |
| Table-Critic | 77.2 | 92.6 | 70.1 | 91.5 | 73.9 | 91.1 | 73.7 | 91.7 |

其他基线为 End-to-End QA、Few-Shot QA、Binder、Dater；Critic-CoT 与 Table-Critic 都建在 Chain-of-Table 之上。

**实验 2（纠正/破坏，Table 2，Qwen2.5-72B）**：WikiTQ 上 Table-Critic 纠正 9.6%、破坏 0.7%，净增 8.9；Critic-CoT 为 5.6%、4.9%、0.7。TabFact 上分别为 3.4/0.5/2.9 与 2.9/2.8/0.1。百分比相对全部样本计。

**实验 3（迭代，Figure 2）**：WikiTQ 准确率在前三轮从 67.6% 升到 76.5%，约六轮后稳定在 77% 左右；TabFact 约五轮后在 92% 左右。

**实验 4（成本，Figure 3 与附录 C）**：Table-Critic 约为 Chain-of-Table 的 1.87×/2.19× 成本；让 Chain-of-Table 做 15 次自一致性投票也只到 70.0%/90.1%。阅读者复算：附录 C 中 TabFact 输出 20.4M 与总计 17.1M 按其 0.25/0.75 加权公式不符，按公式反推输出约 2.1M（阅读者分析）。

**实验 5（消融，Table 3）**：固定模板树时 WikiTQ 76.1、TabFact 90.8，比完整版分别低 1.1、1.8。

**边界**：Limitations 只说当前仅处理文本表格，可扩展到多模态。阅读者分析：结果为单次贪心解码，无方差或显著性；模板树随测试样本更新，样本顺序的影响未讨论；消融只在 Qwen2.5-72B 上做；没有在多表、超大表或数据库规模上验证。

依据：[ACL 2025，pp.17432–17451，20 页](https://aclanthology.org/2025.acl-long.853/)，§4.2–4.6、Tables 1–3、Figures 2–3、Limitations、附录 C，PDF pp.6–9、12–13。
