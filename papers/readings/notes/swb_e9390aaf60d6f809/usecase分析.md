# 具体用例

**例子：Erawan 神社爆炸案起诉**（Figure 6，PDF p.8）。新闻标题为“Thai Authorities Indict 2 over August Shrine Attack”：曼谷军事法庭起诉两名被控实施 8 月 17 日神社爆炸（造成 20 人死亡）的男子；下一句才写出两人姓名 Bilal Mohammed 和 Mieraili Yusufu；第三句提到 Erawan Shrine。

在最具信息量论元抽取任务中，模型需要为 ChargeIndict 事件找出被告，为攻击事件找出地点。原文称，即使触发词与论元相隔数句，模型也能为全部起诉事件正确抽出“Bilal Mohammed and Mieraili Yusufu”作为 Defendant、“Erawan Shrine”作为攻击地点，而非“two men”或“popular shrine”这类信息量较低的提及（Figure 6，PDF p.8）。

**下游应用**：作者把模型接入 NIST SM-KBP 2020 多媒体多语种知识库构建流水线，相比原系统 OneIE 新发现 53% 的论元，尤其是离触发词较远的论元（§4.5、Figure 5，PDF pp.7–8）。

阅读者分析：这对应“从长文档中按 schema 抽取结构化记录（事件 × 角色）”的语义抽取需求；“最具信息量提及”的口径与面向数据库填充的抽取尤其相关，因为代词论元对下游表无用。
