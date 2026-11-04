# Pyysalo et al. — Event extraction across multiple levels of biological organization

本文把生物医学事件抽取从分子层面扩展到细胞、组织、器官直至整个生物体，发布 MLEE 语料库：262 篇血管生成主题的 PubMed 摘要，标注 8,291 个实体和 6,677 个事件，类型参照 CARO、GO 等本体定义。作者用 NERsuite 做实体识别（严格匹配 F1 76.52），用 EventMine 做事件抽取（叠加 GE 语料时 F1 53.43）。已阅读正文 §1–5 全部章节和 Tables 1–8；补充材料（含标注一致性评估）未获取。

[原文](https://doi.org/10.1093/bioinformatics/bts407)

版本：Bioinformatics 28(18):i575–i581（2012，ISMB 特刊），Open Access，CC BY 3.0。出版社站点被 Cloudflare 拦截，PMC 返回验证码页，因此保存的是 Europe PMC 全文 XML（PMC3436834）；XML 不带分页，下文按章节和表号定位，对应期刊 7 页。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题 | Abstract、§1 |
| 方法 | §2.1–2.5（语料与标注）、§3.1–3.3（抽取方法与实验设置）、Tables 1–2 |
| 评测 | §4.1–4.3、Tables 3–8 |
| 局限 | 无独立 Limitations 节；§4.2–4.3 讨论与 §5 未来工作 |
