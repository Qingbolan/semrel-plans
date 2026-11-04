# Zhang et al. — MLRC-Bench: Can Language Agents Solve Machine Learning Research Challenges?

MLRC-Bench 把 7 个近期 ML 会议竞赛整理成统一的仓库级代码环境（任务描述、基线代码、开发/测试划分、算力限制），让 LLM 代理提出并实现新方法，再以"相对人类最佳方案的提升"（基线=0，人类第一=100）客观打分。最好的配置 MLAB（gemini-exp-1206）平均只填补 9.3% 的差距；作者还发现 o1 评审给出的创新性分数与实际效果几乎不相关（Spearman −0.06）。已阅读正文 §1–5、附录 A 的任务说明、附录 D 局限与 Table 4–6 说明；附录 F 的轨迹分析只看了正文摘要的结论。

[原文](https://arxiv.org/abs/2504.09702)

版本：arXiv:2504.09702v3（2025-10-24，NeurIPS 2025 Datasets and Benchmarks Track），45 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1–2、Table 2，PDF pp.1–3 |
| method | §3.1–3.4、Table 1、Figure 1，PDF pp.2–6；附录 A 任务说明，pp.24–27 |
| evaluation | §4.1–4.6、Table 3、Figure 2–6，PDF pp.6–10；附录 B–C、Table 4–5，pp.27–31 |
| limitations | 附录 D Limitations，PDF p.31；§4.2 对 rainfall/backdoor 结果的说明，p.7 |
