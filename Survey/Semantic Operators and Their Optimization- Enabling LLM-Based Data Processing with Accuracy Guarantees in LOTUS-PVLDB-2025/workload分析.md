# workload分析

**验证什么。** 语义算子能否简洁表达完整批量任务，且相对于参考算法以质量约束优化filter/join/top-k等处理。

**数据、单位与gold。** §5四应用：FEVER事实核验、BioDEX反应标签、搜索和主题分析。FEVER源为5.5M Wikipedia文章，实际抽1000验证声明，把Refuted和NotEnoughInfo合并为Not Supported；BioDEX源65k文章，实际250文章、约24k候选反应，gold来自专家报告，指标RP@5/10。任务单位分别声明、文章及查询/文档组。质量保证相对于指定参考模型，另用任务gold测真实性；二者不应混淆。

**最有说服力用例（§5.2）。** 医学文章需从约24k反应选出标签。使用前朴素逐对LLM join代价巨大；使用后semantic join用代理筛选并将难例交参考模型，再按文章重排候选。表3 LOTUS Join+Rank RP@5 0.265、2503s、5869调用；反应标签正确性仍依赖模型和资料。

**baseline及公平性。** FEVER对FacTool、AI UDF、UQE，统一ColBERT和Llama70B；分别报batch/nonbatch以免把FacTool顺序执行当优化器差距。BioDEX比embedding search、AI UDF、UQE、DocETL；AI UDF约609万调用/时间为估算，未实跑。DocETL只取3次成功平均，优化器使用gpt-4o且有失败；表4另按DocETL设置比gpt-4o-mini。

**效果范围。** §5表2 FEVER优化/未优化LOTUS准确率91.0/91.2%，batch时间190.0/329.1s；这是清楚的质量—速度对照。最高1000×涉及朴素join估算，不能当所有工作负载实测加速。2025论文不覆盖当前软件全部Agent接口。

来源：[PVLDB18，2025](https://www.vldb.org/pvldb/vol18/p4171-patel.pdf)。本分析为原文重述与比较边界判断，未复现实验。
