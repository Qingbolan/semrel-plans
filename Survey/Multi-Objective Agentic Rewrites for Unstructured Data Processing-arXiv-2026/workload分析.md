# workload分析

**验证什么。** 直接搜索完整文档处理流水线而非逐算子局部优化，能否找到更好的质量—费用前沿。

**数据、单位与gold。** §5.1六工作负载：CUAD、Game Reviews、BlackVault、BioDEX、Medec、Sustainability。各取40文档优化、100 held-out测试；源规模不等于测试规模：CUAD510合同、BlackVault733文章、Medec3848临床笔记、Sustainability5436报告；Game Reviews每文档合并同游戏300评论。真实公开素材模拟实际用户需求，非用户私有生产数据。gold/指标分别条款F1（Jaccard>0.15）、评论幻觉/情绪/排序、位置召回、RP@5、错误检测F1与修订相似度、部门分类/倡议总结等。BlackVault召回按方法最大值归一化，不是绝对完整gold。

**最有说服力用例（CUAD实验重述）。** 对合同抽41类条款。使用前一个map一次抽全部或局部改写；使用后搜索完整候选管线，可分解提取、改变上下文/模型并用held-out测试，避免某个局部改进伤害最终输出。表4 MOAR F1 0.762、PZ0.694、DocETL-V1 0.471，是该划分/度量下结果。

**baseline及公平性。** DocETL-V1只gpt-4o-mini且不用gold；LOTUS、PZ/Abacus可多模型；Simple Agent是gpt-5工具Agent，另MOAR(no search)给全指令库。PZ按4预算运行构造前沿，不支持reduce的任务省略，Game Reviews崩溃后采样预算降到50；BioDEX同时给PZ/LOTUS direct与retrieve-rerank程序。评价信息和支持范围不完全一致，不能只用平均涨幅宣称纯搜索算法优势。

**证据与成本。** §5.1、表4及前沿图、优化开销表。执行前沿须另计40样本上的优化费用与候选评估；收益能否摊薄取决于真实批量规模。

来源：[v4，2026-04-01](https://arxiv.org/abs/2512.02289v4)。本分析为原文重述与比较边界判断，未复现实验。
