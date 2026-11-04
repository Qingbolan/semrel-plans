# 具体用例

Figure 1（PDF p.2）的例句："Electrochromic properties during water electrolysis were characterized for the WO3 films on transparent substrate (indium tin oxide)." 标注中 "were characterized" 是 MEASUREMENT 触发词；measuresProperty 指向 PROPERTY "Electrochromic properties"，usesTechnique 指向 "water electrolysis"，两条 conditionSampleFeatures 指向被测材料；图中还标出 hasForm（材料→形态 films）、usedAs 等与测量无关的材料关系。阅读者分析：图为 PDF 绘制，文本抽取无法逐一确认每条边的端点，此处只列图中出现的关系名。

第二个例句 "Transmittance varied between 10% and 78% and the coloration efficiency at a wavelength of 528 nm and the overpotential of 400 mV was 40 cm2 C-1." 展示了 PROPERTY –propertyValue→ VALUE（由 NUM/RANGE/UNIT 嵌套组成）以及 conditionProperty（wavelength、overpotential 作为条件）。

阅读者分析：若把它转化为引言中的检索设想（"材料 X、条件 Y、测得值 ≥Z"），需要在关系图上做值解析与单位归一，而论文没有实现或评测这一步；该用法属于派生任务。

依据：Figure 1、§1、§3.2，PDF pp.1–4。
