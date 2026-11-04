# 贡献与评价

**论文自述贡献**（§1，p.2）：

1. MoE 机制：7 个领域 LLM 专家（Access Control、Query Optimization、Query Execution、Background Processes、CPU、Memory、Disk），由 Manager 分类并分配权重，专家打 1–100 分并给理由，按 S_final=Σ Wi×Si 排序选 knob；用 Chain of Draft 控制输出长度（§5.2，pp.5–6）。例：random_page_cost 归入查询优化（0.6，85 分）与磁盘（0.4，60 分），最终 75 分。
2. 受 LA-MCTS 启发的空间分解：每个节点用聚类把样本分为高/低性能两簇（样本数 ≤ τ=50 用基于余弦相似度的谱聚类，否则 Kernel PCA + K-medoids），再用软间隔 SVM 学边界；UCB 选择叶节点，在其中用 BO 采样；每次迭代从根重建搜索树（§6.2–6.3，pp.7–9）。
3. 自称"首个"结合空间分解与 LLM 引导探索的数据库调优框架。
4. 8 个基准上的实验。

**评价（阅读者分析）**：

- 知识收集流程明确说受 GPTuner 启发（§5.1，p.4），空间分解受 LA-MCTS 启发；新意主要在两者的组合与多专家加权选择。
- 实现细节有不一致：§7.1.3 写"GPT-4-powered OpenAI API"，§7.1.5 写使用 gpt-4o-mini（p.9–10）。
- 正文两处称 LASSO 与 zero-shot LLM 的详细分析见附录（§7.3.1，p.11），但 arXiv v1 没有附录。
- 摘要中的"每次迭代快 1.4×"未写明比较对象；按 Table 1，5.54 s 相对 GPTuner 7.47 s 约 1.35×，但 LlamaTune（2.06 s）、SMAC（1.87 s）、CDBTune（0.54 s）更快（阅读者分析）。
