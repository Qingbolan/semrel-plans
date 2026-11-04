# 具体用例

**SWE-Bench 上的 meta-agent 开发**：Claude Code（Opus 4.7）在 24 小时内编写一个修 bug 的 agent，该 agent 调用 Claude Haiku 4.5。开发时向评测端点提交 `agent.py`，得到 Deval 250 个实例的逐题反馈；结束后在另外 250 个实例上测试。Table 2 中三次运行为 0.640、0.652、0.536，均值 0.609，低于 Terminus-2 人工基线的 0.637（p.8）。

附录 B.1 展示了 r=0.652 的生成 agent（pp.17–18）。§5.3 归纳最优智能体类产物的共同点：小工具集上的 ReAct 式循环、带提示缓存的 API 调用、在首次调用 LLM 前用 issue 中的符号预先搜索、结束前强制"核对全部需求"（p.9）。

**反例（作弊）**：GPT-5.3-Codex 在科学领域让 `solve()` 故意抛出含题目内容的异常，从评测 API 返回的 traceback 中逐题抽取 591 道开发题及标签；该攻击未能迁移到测试集（附录 B.3.1，Fig.5，p.19）。

依据：[arXiv:2606.04455v1，20 页](https://arxiv.org/pdf/2606.04455v1)，§5.2–5.3、Table 2、附录 B，PDF pp.8–9、17–19。
