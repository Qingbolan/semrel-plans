# Candito et al. — A French corpus annotated for multiword expressions and named entities

本文在法语 Sequoia 树库（3,099 句、约 70k token，四种文体）上新增命名实体（NE）与多词表达（MWE）标注层（PARSEME-FR），重点是用决策流程图和“充分条件”式语言学测试区分 NE、动词性 MWE 与非动词性 MWE。全部句子双人标注并裁决，NE+非动词性 MWE 的标注者一致性 F=71.1（精确匹配）；最终 Table 3 统计 6,579 个标注。论文是资源与标注规范论文，没有自动识别模型实验。已阅读 §1、§3–4、§5.1、§7.1/7.3、§8–12，附录与 §2 相关工作、§5.2–6 细则仅浏览。

[原文](https://jlm.ipipan.waw.pl/index.php/JLM/article/download/265/249/2149)

版本：Journal of Language Modelling Vol 8, No 2 (2020), pp.415–479，JLM 官网 PDF，65 页（PDF 页码 = 期刊页码 − 414）。状态 READ：单人阅读与自查，未经独立证据复核，未复现实验。原文已保存并记录 SHA256。

| 阅读内容 | 位置 |
|---|---|
| 问题（problem） | 摘要、§1，期刊 pp.415–417（PDF pp.1–3） |
| 方法（method） | §3 区分与类型体系、§4 顶层流程图（Figure 2）、§5.1 NE 类别、§7.1/7.3 非动词 MWE 充分条件、§8.1–8.2 标注流程，期刊 pp.427–449（PDF pp.13–35） |
| 评测（evaluation） | §8.3 Table 1 一致性、§10 Tables 3–6、§10.4 与 FTB 等比较，期刊 pp.449–463（PDF pp.35–49） |
| 局限（limitations） | §8.2 不用预标注导致规模小、§8.3 医疗子语料一致性低、§11 经验教训、§12，期刊 pp.448–466（PDF pp.34–52） |
