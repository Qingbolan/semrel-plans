# 具体用例

**LLM 论元抽取示例**（附录 Table 11，PDF p.18）：输入一篇关于 2010 年 2 月澳大利亚网络攻击的文档，触发词 "cyberattacks" 用 `<event>` 标记，并给出角色集 `[Agent, Location, Patient, Consequence]`。

GPT-4 输出：

- Agent = the Anonymous online community
- Location = Australia
- Patient = Australian government
- Consequence = lapses of access to government websites; disruption on multiple government websites

金标准为：Agent = Anonymous online community；Patient = Australian government；Consequence = lapses of access to government websites on 10 and 11 February 2010；Location = Australian。

可以看出，片段边界和措辞的差异会直接影响 EM，这正是作者同时报告词袋 F1 的原因（§4.3，PDF p.6）。

**未来事件预测示例**（附录 Table 12，PDF p.18）：已知事件链为 Attack → Use_firearm → Bodily_harm，主体是 Boris Nemtsov 遇袭。GPT-3.5 预测下一事件为 Criminal_investigation，GPT-4 预测为 Death。

阅读者分析：每个"事件 × 角色"相当于一次对长文档的抽取问答。若在项目中做成语义抽取算子，需要保留共指层级的判分口径，否则同一实体的不同提及会被重复计为错误。
