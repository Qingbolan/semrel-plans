# 具体用例

**原文业务场景**（§9.3）：作者咨询金融领域专家后，把 XBRL 标注器设定为推荐引擎。会计师或审计师事先知道哪些 token 需要标注，选中一个数字后，模型给出最可能的 k 个 XBRL 标签，专家只需从短列表中挑选，而不必在数百个标签中查找。

**结果**（Figure 4、§9.3）：用 SEC-BERT-SHAPE 计算测试集 Hits@k。曲线在 k=1 到 5 之间陡升，k=10 时接近饱和，Hits@10 为 99.4%；作者据此说在多数情况下正确标签在前 5 个推荐中。

**数据中的例子**（Figure 5、§9.4）：一句租赁条款里，数字 "1" 被正确标为 Lessee Operating Lease Term Of Contract，但同义的 "16" 未被审计师标注；"0.1" 和 "6" 本应标为 Lessee Operating Lease Renewal Term 却也没有标签。作者推测审计师可能不知道存在续租期限标签，推荐引擎或许能帮上忙。

阅读者分析：Hits@k 设定假设"哪些 token 要标注"已知，回避了片段检测这一难点；Figure 4 中除 k=10 外的具体数值正文未列出，这里不做引用。

依据：[ACL 2022，13 页](https://aclanthology.org/2022.acl-long.303)，§9.3–9.4、Figures 4–5，PDF pp.7–8。
