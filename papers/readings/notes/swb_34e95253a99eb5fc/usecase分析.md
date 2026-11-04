# usecase

附录 G 的失败案例（Figure 16，“Lack domain knowledge”，PDF pp.25–26）：

- 商品：标题为 “20/50/100PCS Pink Nitrile Gloves Disposable Latex Powder Free Gloves for Household Cleaning Beauty Salon Working Kitchen Gloves”；属性 Type: Disposable、Use: Cleaning、Material: PVC、Model Number: Nitrile Disposable Gloves；价格 11.56 USD；平台类目 Home & Garden → Household Merchandises → Disposable Household Cleaning Products。
- 智能体：用 “HTSUS nitrile disposable gloves HS code 10-digit 4015.19 CBP ruling” 搜索，引用 CBP 裁定，判断丁腈属于合成橡胶，归入第 40 章，预测 4015.19.1010（硫化橡胶制无缝一次性手套）。
- 金标准：3926.20.1020，即第 39 章塑料制品中的一次性手套。依据是属性中的材质 PVC。

这个例子集中体现了任务难点：标题与属性在材质上矛盾，章级（2 位）就已经分错，后续层级全部错误；智能体也会凭检索到的历史裁定过早定下路径。

阅读者分析（项目派生，非原文评测）：若在本项目中把它做成“商品 → 层级编码”的语义分类任务，应把前缀准确率与 10 位精确匹配分开报告，并保留属性冲突这类噪声，不要只用干净标题。

依据：[arXiv:2510.19631v1（2025-10-22 提交，PDF 标注 2025-10-23），38 页](https://arxiv.org/abs/2510.19631)。
