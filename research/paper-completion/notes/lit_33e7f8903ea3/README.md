# Qiao, Li, Zhang, He et al.（Microsoft）— TaskWeaver: A Code-First Agent Framework

TaskWeaver 是一个“代码优先”的 LLM 智能体框架：Planner 把用户请求拆成子任务，Code Interpreter 生成 Python 代码并在有状态的 Jupyter 进程中执行，用户自定义插件以 Python 函数形式被代码调用，可直接传递 DataFrame 等富数据结构。论文以系统设计为主，评测仅比较 GPT-3.5 与 GPT-4 作为底座时的得分（如自建 23 个用例上为 0.42 与 0.87），不与其他智能体框架比较。已阅读正文 §1–§11 全部；附录 A–F（pp.25–31：执行过程截图、规划/代码示例、插件定义、改造后的测试样例）浏览确认。

[原文](https://arxiv.org/abs/2311.17541)

版本：arXiv 2311.17541v3（2024-06-20），31 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–§2，PDF pp.1–3 |
| 方法 | §3–§6、Table 1、Figures 2–5，PDF pp.3–12 |
| 评测 | §7–§9、Tables 3–5、Figures 6–11，PDF pp.12–21；Table 4、5 已用版面文本核对 |
| 局限 | 无独立局限章节；§7.3、§7.4、§7.6 的评测局限讨论，PDF pp.14–17 |
