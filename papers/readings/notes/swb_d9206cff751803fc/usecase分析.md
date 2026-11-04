# 具体用例

**按患者特征检索不良反应证据**：例句 S7"一名患有糖尿病的 60 岁女性在开始 gliclazide 治疗 6 周后出现急性黄疸性肝炎样疾病"（p.4）。标注为：药物 gliclazide、疾病 hepatitis-like illness、受试者 60-year-old woman 与 diabetes mellitus 通过 Subject_Disorder 相连，AE 事件把三者以 has_agent / affects / has_subject 连接。策展者因此可以查询"对 gliclazide 出现此类反应的患者还患有哪些疾病"。

**多药成因**：例句 S3 中 venlafaxine 与 trimipramine 的相互作用可能诱发癫痫，DDI 事件本身作为 AE 的 has_agent，并因"may have played a role"标为 Speculated（pp.3、8）。

**强度与不确定性**：S5 中 life threatening 是 Manner=High 的提示词；S6 中"may be a possible complication"使 AE 被标为 Speculated（p.3，Table 5）。

阅读者分析：这些结构可映射为"药物 × 反应 × 人群"上的结构化过滤，但原文只评测了实体与事件抽取，没有评测任何检索或问答任务；检索用途是作者的愿景（p.4、p.29）。

依据：Background pp.3–4；Methods pp.7–8，Tables 3、5。
