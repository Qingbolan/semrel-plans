# Cao et al. — VirtualMLE: A Virtual ML Engineer that Optimizes Sequential Recommenders

VirtualMLE 是一个用 LLM 代理调优序列推荐模型（SASRec、HSTU）的框架：每次训练试验后由 LLM 反思归因，结果写入长/短期分层记忆，并在完成一个数据集后蒸馏出可跨数据集迁移的 Cognition Summary。在三个 Amazon-2014 数据集上，论文报告其在两种骨干上所有指标格都优于网格搜索、贝叶斯优化和 OPRO，且达到最佳验证 NDCG@10 所需试验数为 17–32 次。全文 7 页（含参考文献），已通读正文全部章节与 4 张表；Figure 2 为曲线图，只采用其图注与正文描述。

[原文](https://arxiv.org/abs/2606.03221)

版本：arXiv:2606.03221v1（2026-06-02），7 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| problem | §1，PDF pp.1–2 |
| method | §3.1–3.4、Figure 1，PDF pp.2–3 |
| evaluation | §4.1–4.5、Tables 1–4、Figure 2，PDF pp.3–6 |
| limitations | 无独立章节；§4.4 脚注 1、§5，PDF pp.5–6（由阅读者归纳） |
