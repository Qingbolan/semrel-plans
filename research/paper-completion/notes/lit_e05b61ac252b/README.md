# Sui, Zhou et al. — Table Meets LLM: Can Large Language Models Understand Structured Table Data? A Benchmark and Empirical Study

本文提出 SUC 基准，用 7 个结构理解任务（表格分区、单元格查找/反查、行/列检索、尺寸检测、合并单元格检测）测试 GPT-3.5（text-davinci-003）与 GPT-4 对序列化表格的理解，并比较输入设计（NL+分隔符、Markdown、JSON、XML、HTML；格式说明、分区标记、角色提示、文本顺序、1-shot）。

结论是 LLM 有基本结构理解能力但不完善（如尺寸检测），HTML + 格式说明 + 角色提示在 7 任务上平均最高 65.43%；作者提出两阶段“自增强提示”，在 TabFact、HybridQA、SQA、FEVEROUS、ToTTo 上比 1-shot 有小幅提升。已阅读正文与附录 Tables 8–9 标题；p.6–7 表格已渲染核对。

[原文](https://doi.org/10.1145/3616855.3635752)

版本：取自 arXiv:2305.13062v5（2024-07-17），版面为 WSDM '24 会议格式（含 ACM DOI 10.1145/3616855.3635752），11 页；ACM 官方 PDF 下载返回 HTML 拦截页，未取得。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | §1–2，PDF pp.1–3 |
| 方法 | §3.1–3.4 SUC 设计、§4 结构化提示、Tables 1、6，Figs. 1–3，PDF pp.3–6、8 |
| 评测 | §5、Tables 2–5、7，PDF pp.6–8；附录 Tables 8–9，p.11 |
| 局限 | Ethical Considerations，PDF p.9（无独立局限节） |
