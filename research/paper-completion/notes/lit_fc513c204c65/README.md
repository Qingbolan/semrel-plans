# Liu et al. — SERAG: Self-Evolving RAG System for Query Optimization

SERAG 是一个 5 页的 aiDM 2025 工作坊短文：用向量库保存历史 SQL、提示（pg_hint_plan hint）和执行时间，检索相似查询拼成动态提示，让 LLM 生成 PostgreSQL 计划提示，并把每轮执行结果写回向量库，形成“自演化”反馈循环。

论文报告的最好设置是监督微调的 LLaMA3.2-3B、无参考示例、只输出连接顺序，在 CEB 上相对 PostgreSQL 的总体收益为 63.62%（Table 1/2），但该数值取自 50 轮中每条查询的最优计划。已阅读全文（含算法、Tables 1–2、Figures 4–5），p.4 已渲染核对表格；论文没有独立的局限性章节。

[原文](https://viterbi-web.usc.edu/~sabek/pdf/25_workshop_serag.pdf)

版本：aiDM ’25（SIGMOD 2025 工作坊），DOI 10.1145/3735403.3735997，作者主页 PDF，5 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1，PDF pp.1–2 |
| 方法 | §3、§3.1–3.4、Figures 1–3、Algorithm 1，PDF pp.2–3 |
| 评测 | §4.1–4.5、Tables 1–2、Figures 4–5，PDF pp.3–4；p.4 已渲染核对 |
| 局限 | 无专门章节；§6 结论的未来工作一句，及阅读者从 §4 设置推断的边界，PDF p.4 |
