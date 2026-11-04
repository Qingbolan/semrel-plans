# 具体用例

论文 Fig.3（PDF p.4）给出一个 Doc-750K 样例：一篇关于美国公用事业节能项目的经济学论文（“How Many Kilowatts are in a Negawatt? Verifying ‘Ex Post’ Estimates of Utility Conservation Impacts at the Regional Level”）被抽取为交错图文。

多轮问题要求“说明 Image-1 如何展示 1993 年各公用事业的节能影响并讨论其意义”“分析 Image-3 在与既有电价弹性研究比较中的作用”。

参考答案引用原文语句（如样本 39 家公司占全国工商业售电 19%、节能影响 40%），再结合表格图像内容作答，并指出本研究短期自价格弹性 −0.078 与既有研究接近。

这个例子体现了 Docopilot 面向的使用方式：用户在一个长文档上连续提问，答案需要把某页的表格图像与另一页的正文联系起来，而不是对单页做抽取。

阅读者分析：该例的答案文本较长、带解释，属于生成式问答；作为本项目的使用参考时，应注意它没有逐字段的结构化标注，难以直接用作精确匹配式评测。

依据：[CVPR 2025 Open Access，12 页](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf)，§3.1，Fig.3，PDF pp.3–4。
