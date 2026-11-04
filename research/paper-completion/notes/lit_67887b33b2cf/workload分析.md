# 工作负载

**数据集**：WikiTables-TURL-CTA 的完整测试集，共 13,025 列，由 TURL 团队从 WikiTable 语料抽取，按 255 个 Freebase 类型多标签标注。数据集为每个单元格提供真值实体 ID（Wikipedia 页面 ID）。表格平均 21 行、4 个实体列（至少有一个已链接单元格的列）。

**KG 与链接器**：Wikidata；三种 KG-Linker——真值实体 ID（完美链接）、MediaWiki API（`action=websearchentities`）、ReFinED 实体链接模型。Table 1 的 EL 列给出链接准确率：1.0000、0.4018、0.6255。

**任务设置**：多标签（模型对每个类型标 0/1，输出所有标 1 的类型）；单标签（只选一个，若预测落在真值集合内即视为正确）。

**模型**：GPT-3.5，论文未给出具体版本号与温度。无训练集，零样本；没有开发集调参的描述。

依据：[arXiv:2409.14556v2](https://arxiv.org/pdf/2409.14556v2)，§3、Table 1、附录 A，PDF pp.3–4、8。
