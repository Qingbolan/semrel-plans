# 具体用例

**场景**：把 Dou 等人发表的子宫内膜癌临床补充数据（源表）映射到 GDC 标准（目标表），见 Table 1 与 §5（PDF pp.2、7）。

1. 对每个源列（如 `Path_Stage_Primary_Tumor-pT`，值 “pT1a (FIGO IA)”），Magneto 用优先级抽样取值、按 Srepeat 序列化（列名重复 k=5 次，以 `[SEP]` 分隔值），经微调 MPNet 编码，按余弦相似度检索目标列候选（§3.1，PDF pp.4–5）。
2. 取前 k=20 个候选（如 `uicc_pathologic_t`、`ajcc_pathologic_t`），连同样本值放入 Figure 5 的打分提示，交给 GPT-4o-mini 给每个候选打 0–1 分（§4、§6.4，PDF pp.6–7、11）。
3. 返回排序列表给领域专家确认；作者强调这类匹配连专家也常难以确定，因此输出是辅助审查的排序而非自动映射（§2、§5）。

阅读者分析：在本项目的语义算子语境下，这对应“列级语义连接/映射发现”；论文只评测排序质量（MRR、Recall@GT），不涉及值转换（如 “FIGO grade 1”→“G1”），值映射需另行处理（阅读者分析）。

依据：§3–§5、Table 1、Figure 5，PDF pp.2、4–7。
