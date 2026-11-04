# Yang et al. — Multimodal DeepResearcher: Generating Text-Chart Interleaved Reports From Scratch with Agentic Framework

本文提出一个从单个主题出发、自动生成图文交错报告的智能体框架：先联网检索，再用"可视化形式描述"（FDV）把人类专家报告中的图表转成文本供上下文学习，然后规划大纲与风格指南，最后写作、用 D3.js 编码并迭代修图。作者构建了 100 个主题的 MultimodalReportBench；以 Claude 3.7 Sonnet 为生成器时，在 GPT-4.1 成对评判下对改造版 DataNarrative 的总体胜率为 82%。已读正文全部及附录 A、B、E；附录 C 的提示词和 D、F 的示例只做了浏览。

[原文](https://arxiv.org/abs/2506.02454)

版本：arXiv:2506.02454v3（2025-12-14，页脚标注 AAAI 2026 版权），48 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Introduction、Method 开头任务定义，PDF pp.1–3 |
| 方法 | Method 四阶段、Algorithms 1–2、附录 A.1–A.3，PDF pp.3–5、10–12 |
| 评测 | Experiments、Tables 1–4、Figure 4、附录 A.4–A.5 与 Tables 5–7，PDF pp.5–8、12–13 |
| 局限 | Error Analysis、Efficiency Analysis、Conclusion，PDF p.8；附录 E，PDF pp.34–36 |
