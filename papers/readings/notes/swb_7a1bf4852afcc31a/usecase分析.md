# 具体用例

**从一句话填充实验记录**：Fig.1 的句子"The corresponding SOFC with Pt / SmNiO3 / Pt geometry demonstrated dramatic power output of 225 mW cm−2 at 500 °C."中，触发词 demonstrated 标为 EXPERIMENT；SOFC 为 DEVICE 并填 Device 槽；第一个 Pt 填 AnodeMaterial，SmNiO3 填 FuelUsed，第二个 Pt 填 CathodeMaterial；225 mW cm−2 填 PowerDensity，500 °C 填 WorkingTemperature（p.1，按原图 Fig.1 的标注，已渲染核对）。

流水线做法是先用句子分类器挑出实验句，再在这些句子上做实体与槽位序列标注（§4，p.4）。由此得到的记录可用于知识库，例如按工作温度、阳极材料检索已报道的功率密度（§1，p.1）。

**难例**：枚举式句子"极化电阻在 800、700、600 °C 下分别为 0.027、0.11、0.88 Ωcm²"中，所有电阻与温度都链接到同一触发词，不拆分配对；配对留作未来工作（§3.3，p.4）。阅读者分析：若下游按"温度—电阻"成对查询，这类句子需要额外的分组逻辑。

依据：[ACL 2020，2020.acl-main.116，14 页](https://aclanthology.org/2020.acl-main.116.pdf)，§1、§3.3、§4、Fig.1，PDF pp.1、4。
