# 具体用例

**客服对话中找出不满的客户（§4.1，PDF p.5）**：

`SELECT dialog_ID FROM dialogs WHERE "the customer is unhappy with the agent's manner"`

这是非聚合查询。在 token 预算 B 内，UQE 先对每条对话做嵌入，并把代理 ĝ 初始化为均匀随机值；每一步选出 ĝ 加探索噪声后得分最高的一批对话交给 LLM 判断，用新观察重新拟合 ĝ，直到达到预算。与 RAG 只按固定嵌入相似度取 top-k 不同，代理模型会随 LLM 的判断在线修正。

**影评正面数计数（§4.1，PDF p.4）**：

`SELECT COUNT(*) as count FROM movie_reviews WHERE "the review is positive"`

把 5 万条影评的嵌入聚为若干簇，在各簇中分层抽样，交给 LLM 判断，再按权重估计 N·E[f]。实验中 UQE（claude-3-haiku）在 IMDB 上的相对误差为 5.75% ± 3.43%，每查询约 $0.01（Table 1，PDF p.8）。

**取消订票对话检索（Figure 5，PDF p.10）**：AirDialog 中 cancel 仅占 1.46%，属于"罕见事件"；UQE 的 F1 为 0.741 ± 0.205，MIPS 为 0.066（Table 2）。

这些用例都是单表、单谓词或单分组；若本项目需要跨表语义连接或 MAX 类聚合，UQE 原文明确不支持（阅读者分析）。
