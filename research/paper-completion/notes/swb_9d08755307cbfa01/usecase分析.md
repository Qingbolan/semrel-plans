# 具体用例

**AcmGENTIC 的端到端流程**（Methods、Results，PDF pp.3–4、6）：用户输入一个变异坐标，例如附录命令行示例中的 chrom 2、pos 162279995、ref C、alt G（GRCh38）。

1. 调用 Ensembl VEP 获取 rsID、HGVSc/HGVSp、基因符号和 MANE Select 转录本。
2. 用 rsID 查询 LitVar2，得到提及该变异的 PubMed ID。
3. 用 metapub 拉取标题和摘要，由 LLM 按高敏感度规则筛选可能包含功能实验的论文。
4. 下载 PDF（失败时允许人工放入缓存），把整篇 PDF 交给多模态 LLM 做变异匹配和实验抽取。
5. 跨论文整合出 PS3/BS3 方向、建议强度和置信度，生成 HTML/PDF 报告（Figure 9）或 JSON。

阅读者分析：这是“按实体（变异）检索文献 → 语义过滤摘要 → 全文结构化抽取 → 跨文档聚合”的典型语义查询流水线。其中变异身份对齐充当连接键，是首要瓶颈；若在项目中复用，应把 not clear 弃权和覆盖率作为一等输出，而不是强制给出标签（阅读者分析）。
