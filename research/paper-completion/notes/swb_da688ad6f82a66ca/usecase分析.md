# 具体用例

原文用 advice 类说明分类难度差异：这类句子模式很固定，如 “DRUG should not be used in combination with DRUG” 或 “Caution should be observed when DRUG is administered with DRUG”，因此最好 F1 达 69.2%；而 int 类只说明存在相互作用、不给细节，最好 F1 为 54.7%。

实体识别的难点例子是 insulin：它是胰腺分泌的激素，也可人工合成用于治疗胰岛素依赖型糖尿病。系统需要判断文本描述的是体内物质还是作为药物使用，后者才标为药物实体。

阅读者分析：若用于语义查询（如“找出所有描述两种药物机制性相互作用的句子”），输入单位应为句内药物对，并保留 DrugBank 与 MedLine 两种文体的差别。

依据：[SemEval 2013，pp.341–350](https://aclanthology.org/S13-2056.pdf)，§3.2，PDF p.4；§4.2，PDF p.8。
