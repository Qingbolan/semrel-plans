# usecase

论文 Example 1（§3.1）：Companies 表含 id、name、revenue、headquarters，但没有 sector 列。用户问"医疗行业公司的总收入是多少？"需要借助世界知识按公司名等推断行业。

原文给出的三种合法工作流：
1. **保守**：data-driven、scalar、聚合前、全量、宽投影——逐行带上总部信息推断行业，再 GROUP BY sector、SUM(revenue)。准确率最高，但需要 O(|R|) 次带宽提示的 LLM 调用。
2. **激进**：code-driven、聚合前、全量——用小样本让 LLM 合成一个 CASE WHEN 规则，在全表上以纯 SQL 执行。只需 O(1) 次 LLM 调用，但规则覆盖不到的公司会出错。
3. **均衡**：data-driven、aggregate、聚合前、定向范围、窄投影——先用 SQL 谓词缩小候选，只把公司名批量送给 LLM 一次判断哪些属于医疗，再过滤并求和。

各轴的取舍在例中有具体说明：宽投影可借助总部区分"Dearborn, MI 的 Genesis 多半是汽车而非医疗"；aggregate 调用能把 Medtronic 和 Stryker 联系起来识别为同一行业。

EnumGRPO 学到的经验示例（Table 5）："先在 SQL 中用 CDSCode 前缀抽取与县代码映射完成地理解析，完全跳过 LLM 算子"；"当相关行需要联合推理时用 llm_reduce"。

阅读者分析：哪个工作流最好取决于数据分布、表规模和用户的质量—成本偏好，原文也明确这样说；这正是该方法在运行时观察中间结果再决策的理由。

依据：[arXiv:2606.03152v2，14 页](https://arxiv.org/abs/2606.03152)，§3.1、Example 1，PDF pp.4–5；Table 5，PDF p.11。
