# 具体用例

**用例：从文献句子中抽取"基因型影响药物敏感性"的知识**（Fig. 1，p.3；PHARE 扩展，p.5）

Fig. 1 中的句子涉及药物 acenocoumarol 与 VKORC1 基因型。抽取流程如下：

1. PubTator 识别出关键实体：药物 "acenocoumarol"、基因 "VKORC1"。
2. 依存分析显示 "acenocoumarol" 修饰 "sensitivity"。按 PHARE 本体，它构成 DrugSensitivity 复合实体，归入 Phenotype，于是 "acenocoumarol sensitivity" 被标为一个嵌套的表型实体。
3. "VKORC1 genotypes" 被标为不连续的基因组变异实体。
4. 人工标注者在两个实体之间添加 influences 一类的关系，并标注模态。若句子只说"研究了"某关系，例如 Fig. 2(b) 中的标题句，则标为 hypothetical。

**下游目标**（p.11）：作者希望用该语料训练有监督的 PGx 关系抽取系统，帮助综合 PGx 知识；相关工作曾把抽取出的关系并入知识网络（ref. 44，只使用 307 句和简化模式）。

这是"从文本抽取带类型与模态的三元组"的工作形态。若在项目中把它用于语义抽取或连接查询，需要注意基线把 negated/hypothetical 关系当作普通关系处理（p.11），否定陈述可能被误当成肯定事实（阅读者分析）。

依据：Figs. 1–2、Methods、Baseline experiments，PDF pp.3–5、10–11。
