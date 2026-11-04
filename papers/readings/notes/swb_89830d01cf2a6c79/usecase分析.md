# 具体用例

Figure 1 的句子 “We train a deep CNN for semantic segmentation.” 中，“deep CNN” 标为 METHOD，“semantic segmentation” 标为 TASK，两者之间是 USED-FOR 关系。Table 2 给出更多例子：“We use COCO to evaluate CornerNet-Lite”对应 EVALUATED-WITH；“FlyingChairs is a synthetic dataset designed for training CNNs to estimate optical flow”一句中同时示例了 BENCHMARK-FOR、TRAINED-WITH、USED-FOR 三种关系，说明一句话可产生多条三元组。

LLM 基线的 NER 提示要求模型把输入句改写成带 `<span class="Method">CNNs</span>` 标签的 HTML，避免模型把 “CNNs” 输出成 “CNN” 等表面形式不一致。

阅读者分析：在语义查询系统中，这类标注可直接支持“找出在数据集 Y 上评测过的方法”这类关系过滤；但标注只在句子内，跨句、跨段的关系和实体共指未覆盖。

依据：[EMNLP 2024，pp.13083–13100](https://aclanthology.org/2024.emnlp-main.726.pdf)，Figure 1–2、Table 2、§4.3，PDF pp.1、5–6。
