# 具体用例

§5.4 与 Fig.5 的 BELKA 案例：任务是预测小分子是否与指定蛋白（sEH、BRD4、HSA）结合，输入为构件 SMILES、分子 SMILES 与蛋白名，提交二分类结合概率（PDF pp.8–9）。

AutoMind 先从知识库检索 MolTrans 和 DeepDTA，设计频繁子序列挖掘加双通道 CNN 的方案，并分步实现；去掉知识库的变体只提取分子统计特征并用 MLP；AIDE 使用 RDKit Morgan 指纹加梯度提升。Table 1 中 BELKA avg@3 AP：AutoMind(o3-mini) 0.44，AIDE(o3-mini) 0.09（PDF p.5）。

阅读者分析：该例体现“检索领域论文 → 计划 → 分步代码”的路径；但它是单个挑选案例，不能单独证明知识库普遍有效。对本项目，若把数据科学流水线视为可检索知识增强的规划任务，应记录检索来源与排除同题方案的规则；这属于项目派生思考，原文未评测。

依据：§5.4、Fig.5、Table 1，PDF pp.5、8–9。
