# novelty

原文主张：据作者所知，这是第一个在事件层面同时标注多个元知识维度的方案（Abstract、Conclusion）。具体包括：
- 5 个维度加线索词标注；
- 由维度组合推导出的超维度；
- 方案力求可移植到其他事件标注体系，作者计划推广到 GREC、BioInfer、AIMed 等语料。

本文把该方案应用到当时规模最大的生物医学事件语料 GENIA 上。

与原 GENIA 的 Uncertainty 属性对比（Results：CL）：
- 原 Probable 事件中，33.6% 被标为 CL=L1，42.2% 被标为 CL=L2；
- 新方案中带有某种不确定性的事件（L1+L2）占 8.1%，接近原 Probable 比例 4.3% 的两倍。

阅读者评估：
- 贡献是标注方案和语料资源。
- 方案只应用于摘要；作者推测全文中 Source=Other 等类别会更多，但没有验证（Conclusion）。
- 自动识别元知识的系统留作未来工作，因此本文没有展示可学习性。

依据：[BMC Bioinformatics 12:393，PMC3222636 全文 XML](https://doi.org/10.1186/1471-2105-12-393)，Abstract、Results（CL）、Conclusion。
