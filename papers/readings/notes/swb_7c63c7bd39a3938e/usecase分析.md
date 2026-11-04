# 具体用例

**原文用例（Figure 1、§2.3、§3 H1）**：电商平台用电脑类目（WDC-Computers）的标注对训练匹配模型，随后要把它用于鞋类商品（WDC-Shoes）。

1. 对训练集每个已标注的商品对，用 Mistral-7B-Instruct 按两条手写示例生成解释，例如 WDC-Shoes 中"Entity A 是 Laney 版本、Maize-Black-White 配色，Entity B 是 Motorsports 版本、Blue-Black 配色，因此不匹配"（Figure 2，PDF p.3；附录 C）。
2. 用"标签 + 解释"微调 FlanT5-base，部署时对新类目的候选对生成标签和解释（§2.3）。
3. 在 Table 2 中，WDC-Computers→WDC-Shoes 的 F1 从 BL 的 69.95 提升到 EA-Mistral 的 79.18（PDF p.4）。

**鲁棒性用例（H1，PDF p.7）**：把 "Kingston 128GB DataTraveler G3" 与 "Kingston 128G DT G3" 的匹配对，最小改动为 32G，正确标签应翻转为不匹配。无解释模型 71/300（23%）翻转，有解释模型 164/300（54%）翻转。

阅读者分析：在语义 join/去重场景中，可以把这个模式视为"离线用大模型生成理由、在线用小模型匹配"的成本折中；该迁移是阅读者推断，原文未评测 blocking 或端到端成本。
