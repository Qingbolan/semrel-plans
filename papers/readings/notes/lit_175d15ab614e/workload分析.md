# 工作负载

**MultimodalReportBench**：100 个真实主题，取自刊载专家图文报告的 Pew Research、Our World in Data 和 Open Knowledge Foundation，覆盖 10 个类别（Data Selection，PDF p.5；附录 A.4 Table 5，p.12）。按 Table 5 的行顺序，各类别数量如下：

| 类别 | 主题数 | 类别 | 主题数 |
|---|---|---|---|
| Technology & Media | 15 | Public Sector | 3 |
| Agriculture & Food | 13 | Energy | 9 |
| Travel | 4 | Climate & Environment | 14 |
| Population | 8 | Education | 6 |
| Healthcare | 15 | Economy & Work | 13 |

另外收集了 6 份主题不重叠的多模态报告，作为上下文学习范例（p.5）。

输入只有主题文本，没有参考报告，评测采用不依赖参考答案的成对比较。人工评测和消融实验各用随机抽取的 20 个主题（pp.6–7）。框架不训练模型，因此没有训练、测试划分。

输出规模：本方法每份报告平均 9.3 张图，DataNarrative 为 9.4 张。按 Figure 4，100 个主题下本方法生成了 15 张流程图、18 个仪表盘、280 张"其他"类图；DataNarrative 分别为 2、1、96（p.7）。

依据：[arXiv:2506.02454v3（2025-12-14，页脚标注 AAAI 2026 版权），48 页](https://arxiv.org/pdf/2506.02454v3)，Experiments、Analysis、附录 A.4，PDF pp.5–7、12。
