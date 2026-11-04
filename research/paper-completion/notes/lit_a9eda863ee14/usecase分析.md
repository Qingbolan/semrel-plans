# 具体用例

论文的 Figure 1 和 Figure 2 给出两个完整流程（pp.3、6）。

**零样本**（Figure 2 下）：输入列有 550mm、608mm、600mm、520mm、595mm 等值，提示形如 `INSTRUCTION: Select the option which best describes the input. INPUT: … OPTIONS: text, date, age, …, coordinates ANSWER:`，模型输出 number。

**重映射**（Figure 1）：列中是 Nevada、New Jersey、Alaska 等州名。采样阶段选出代表性的值，序列化阶段按 K 风格模板把 `<CONTEXT>` 和 `<CLASSNAMES>` 填入提示。若模型回答 "State Names"，它不在标签集中，contains 规则会把它映射到 State。

**微调**（Figure 2 上）：输入除样本外还加入表名 `diaridegirona` 和长度类摘要统计（std 4.76、mean 27.52 等），输出 "sporting event"。

阅读者分析：从这个用例可以看出，CTA 在 LLM 时代变成了"列样本 → 受限标签集分类"。真正影响结果的是采样哪些值、标签集多大、输出不在集合中时怎么处理。若把 CTA 当作语义算子（如列级 semantic classify）的预处理步骤，就要把标签集大小（Figure 7 显示 91 类明显比 27 类差）和重映射策略写进代价与质量模型。

依据：§3、§5.4，Figures 1–2、7，pp.3–12。
