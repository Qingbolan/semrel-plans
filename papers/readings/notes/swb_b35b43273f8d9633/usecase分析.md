# 具体用例

**原因摘要**（§5.3，PDF p.7）：输入 NTSB 报告的 analysis 与 factual information 两节，模型生成"可能原因"。原文第 1 例：

- 参考："The pilots failure to maintain directional control during landing roll that resulted in a collision with an airport sign. Factors were wet runway surface and wind gust."
- 生成："The pilot's failure to maintain directional control during landing. A factor was the wind gust."

作者指出生成文本语法正确、常难与人写区分，但内容不总是正确：此例漏掉了"湿跑道"这一因素。第 2 例还生成了参考中没有的"unsuitable terrain"。

**组合使用设想**（§6，PDF p.8）：分析师写完事件叙述后，分类模型自动给出适用标签，摘要模型给出可能原因，以减少工作量并提高不同分析师之间的一致性。

阅读者分析：遗漏因素和编造因素恰是安全分析中最需要人工核对的部分，ROUGE 无法反映这一点；作者自己也说需要领域专家检查正确性与完整性。
