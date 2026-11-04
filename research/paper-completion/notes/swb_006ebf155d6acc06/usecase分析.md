# 具体用例

**显式 Cause**：“John fell because Bill pushed him.” 中，markable m1 为 “John fell”，m2 为连接词 “because”，m3 为 “Bill pushed him”。DRelML 标注为：两个 `drArg`（类型 event）、一个 `dRel`（rel=cause），以及 `explDRLink rel="#r1" result="#e1" reason="#e2"`。这里结果在前、原因在后，但角色由语义而非顺序决定。语义上对应 DRS ⟨r,x,y, cause(r), reason(r,x), result(r,y)⟩。

**隐式 Cause**：“John fell. Bill pushed him.” 没有连接词，用 `implDRLink` 标注同样的 cause 关系与角色。

**对话中的语用 Cause**：乘客问“Is it safe to put my camera through here?”接着说“It's a very expensive camera you know.”。按 ISO 24617-2，第二句是 Inform，用 `rhetoricalLink` 以 “cause reason” 关系连到前面的 Question，表示这句话是提问的理由。

阅读者分析：若项目要把篇章关系当作结构化抽取目标，这种“两论元 + 关系 + 角色”的格式可以直接作为输出 schema；但本文没有提供可用于评测的金标准语料（阅读者分析）。

依据：[Bunt 主页 PDF，10 页](https://let.uvt.nl/general/people/bunt/docs/ISA-12-DR-core-revised.pdf)，§4.3 例 (3)–(5)、§4.4 例 (6)，PDF pp.8–9。
