# 具体用例

**原文示例 1：包装合规过滤**（Figures 1–2，§2.2，pp.1–4）：

```sql
SELECT b.BrandName, COUNT(*) AS NumFlagged
FROM Products p JOIN Brands b ON p.BrandId = b.BrandId
WHERE p.Category IN ('Supplements','Cosmetics')
  AND SemFilter('Compliance-sensitive claims (e.g., "FDA approved")
                 appear on the package labels in {p.Image}.')
GROUP BY b.BrandName;
```

逻辑规划先给出两个种子计划，再由语义替代生成第三个：

| 计划 | 做法 |
|---|---|
| A（直接） | 检测图中物体，逐个问 VQA “是否满足意图”；任一物体肯定则商品通过 |
| B（代理） | 图像区域与意图文本嵌入到同一空间；最大相似度超过阈值则通过 |
| A′（替代） | 把单个 VQA 换成 OCR → TxtQA，再用关系过滤 `answer = yes ∧ Score ≥ λ` |

物理规划把 A′ 中的 OpTxtQA 编译成 router：按文本长度等廉价特征分桶，分别交给正则匹配、DistilBERT QA、GPT-4 或 RAG 式组合实现，切点、置信度阈值和 λ 由 BO 一起调。最终选 A′，因为它保持了高质量，又比 VQA 方案便宜。A′ 不预设与 A 等价，只是在同一目标下比较。

**原文示例 2：同品牌商品连接**（附录 F，Figure 9，pp.19–20）：E-Commerce 的 SemJoin 判断两件商品是否同一品牌。前三个逻辑计划：

1. 文本优先：把很长的 ProductDescriptors JSON 切段、筛出含品牌线索的段、抽取品牌候选，再用 NLI 比较；
2. 图像优先：切出图像区域、对齐相似区域，再从区域中识别品牌；
3. 文本提候选、图像做是/否验证。

由于品牌常直接写在文本里，计划 1 通常最好。ProductDescriptors 是含大量无关键的长 JSON 字符串，不是现成的 brand 列。附录 G 中注入 10%/20% 验证标签翻转后，选中的仍是计划 1 的算子序列，只是切点略有不同。

**原文示例 3：结构化前置过滤**（§7.2 Cars，p.11）：Q1“出过事故的车”只用结构化 crash 字段即可回答（F1 0.89）；Q8“图片同时显示刺穿和划痕”先用 OpImgCls 粗扫，再只对正例调 LLM 验证，F1 0.56，而各基线为 0.08–0.35。

阅读者分析：这些是 CADENZA 论文中的查询版本，应与 SemBench 仓库的原始查询通过明确来源关联，而不是把作者的简写代码当作原仓库原文。

依据：[arXiv 2606.29151v3](https://arxiv.org/abs/2606.29151v3)，§2.2、§7.2、Figures 1–2、9、附录 F–G，PDF pp.1–4、11、19–20。
