# Novelty分析

贡献是把属性级关系gold与跨接口系统比较结合，并细拆chunking、filterorder、join转filter、model selection/cascade、并发等因素。长文档和干扰文档使检索遗漏证据与读全文成本之间的权衡可测。

局限需要具体保留：Healthcare大部分无关类别的NULL gold由半自动分类建立，不能称10万文档每属性都纯人工标注；复杂SQL答案受属性schema上限约束；原文不提供系统版本及所有修改细节于正文。§2的系统能力矩阵是该次适配视角，例如把Palimpzest无Agg与后文用常规groupby衔接并列，不能据此断言库永远不支持聚合。

资料版本也重要：v1是5数据集，官方Bench-U仓库现介绍6数据集，新增的科研论文不能倒写成v1已有。Legal正文570、表2566，Healthcare标注段10000/100000存在差异，应保存证据而非补造一致数字。

来源：[原论文](https://arxiv.org/abs/2510.27119v1)。本分析据所列版本全文核读，未复现实验。
