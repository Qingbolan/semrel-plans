# 具体用例

原文 Fig.2（p.6）给出一句罗马尼亚语的 cupt 标注："Lidia se stingea pe picioare"，字面义"Lidia 自己在腿上熄灭"，实义"Lidia 日渐衰落"。

- token 2–3（se stingea）标为 IRV（内在反身动词）。
- token 2–5（se stingea pe picioare）整体标为 VID（动词习语）。

两者嵌套，第 11 列分别写作 `1:IRV;2:VID`、`1;2`、`2`、`2`，不属于任何 VMWE 的 token 标 `*`。

系统读取此类句子（含词元、UPOS、依存）并预测第 11 列。评测时检查 VMWE 是否完整命中（MWE-based），也检查部分 token 命中（token-based）。若该习语未出现在训练集中，它就属于"未见"子集；在这一子集上，最好的系统 F1 也不到 30（Table 9）。

阅读者分析：这个例子说明 VMWE 识别的输出是跨度可以不连续、可以重叠的结构化标注，而不是逐 token 的单标签序列标注；任何派生任务都应保留嵌套和不连续这两种结构（阅读者分析）。

依据：§4.1、Fig.2、§6、Table 9，PDF pp.6、8、18。
