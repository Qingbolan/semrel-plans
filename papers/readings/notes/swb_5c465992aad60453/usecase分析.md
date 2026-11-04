# 具体用例

**数据构建示例**（Figure 1，PDF p.6）：CDSR 的 RoB 表中一行被解析为 `<Zhou 2015, Random sequence generation (selection bias), Low Risk, Quote: "Random number table method">`。系统在已索引的 Zhou 2015 论文句子中检索这句引文，取支持句及其前后至多 3 句作为上下文，对应信号问题为"Was the allocation sequence random?"，标签为低风险。

**推理示例**（§6.4，PDF p.11）：问题"Was the allocation sequence random?"，金标答案为"randomization was stratified by patients' BMI (non-obese <30 kg/m2 and obese 30-35 kg/m2) using mixed block sizes"。RoBIn_Ext 和 RoBIn_Gen 都精确匹配；Llama3.1 多返回了关于随机化列表由统计师用 nQuery Advisor 生成的句子，GPT-4o-mini 和 Gemma2 则生成改写内容，因此 EM/F1 降低。

随后分类器根据证据判断：仅说"随机"而无细节，不足以判为低风险（§5，PDF p.8）。

阅读者分析：放到系统综述流水线中，这相当于对"试验 × 信号问题"批量做带证据的语义判定；但论文的输入已是定位好的上下文窗口，真实使用还需要先在全文中检索。
