# 具体用例

**原文示例**（Example 1，§1，p.2；Figure 4，p.4）：

> “We are picking a supplier for employee uniforms. Which brands sell everything under $50 and offer at least five formal, non-patterned top-wear items? For each such brand, also count the main sentiments customers express about its garments.”

**回答它需要四步**（§1）：
1. 按品牌检查价格，只保留最贵商品低于 $50 的品牌，并过滤出上装；
2. 用图片和描述判断剩余商品是否正式、无花纹；
3. 按品牌计数，保留至少五件合格商品的品牌；
4. 对这些品牌扫描评论，抽取情感并统计频次。

**朴素做法**：对每件上装都调用视觉模型分类，再按品牌聚合计数；每次阈值变化都重新生成整套计划。

**KathDB-FAO 的做法**：
- Parser 把查询拆成原子动作；契约把第 3 步“只需知道是否 ≥5”的要求向上游传递；
- Optimizer 把第 2、3 步融合进同一个函数：先用价格剔除品牌，对存活品牌逐件分类，找到第五件合格上装就停止该品牌的分类；
- 函数被参数化保存，用户把“五件”改成“三件”时可直接复用（§5）。

**相关量化证据**：论文没有报告这一单例的前后费用。契约的作用由 Figure 13 支持：在 Additional 场景上，开启自顶向下需求传播后质量提高、执行成本下降，例如判断一组照片是否包含不同物体时，看到第二个不同标签就可停止（§6.4，p.11）。

阅读者分析：“至少五件”的语义允许提前停止；若查询要求精确的合格件数，这种停止就不成立。

依据：[arXiv 2609.28761v1](https://arxiv.org/abs/2609.28761v1)，§1、§5、§6.4、Example 1、Figure 4、Figure 13，pp.2–4、8、11。
