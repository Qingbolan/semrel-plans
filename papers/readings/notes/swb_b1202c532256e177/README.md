# Ni, Liu, Liu, Sun et al. — Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

Trace2Skill 让一个固定的 LLM agent 在“演化集”上产生成功/失败轨迹，由并行的分析子 agent 针对单条轨迹提出 skill 补丁，再分层合并为一个可移植的 skill 目录（`SKILL.md` + 参考文件），不更新模型参数、测试时也不检索。主实验在 SpreadsheetBench-Verified（200 演化/200 测试）上进行，并迁移到 WikiTQ、HiTab、DAPO/AIME 数学、DocVQA 和 PDF/PPTX/DOCX 任务。已阅读正文 §1–6、局限、附录 A、B.1 及 G 的部分；附录 C–F、H、I 的提示模板只浏览。

[原文](https://arxiv.org/abs/2603.25158)

版本：arXiv:2603.25158v5（2026-06-04），25 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1、§2.1，PDF pp.1–3 |
| 方法 | §2.2–2.4、Figure 2，PDF pp.2–3；附录 A，pp.13–14 |
| 评测 | §3–4、Tables 1–6、Figures 3–5，PDF pp.4–9；附录 G，pp.19–20 |
| 局限 | Limitations、Ethics Statement，PDF pp.9–10 |
