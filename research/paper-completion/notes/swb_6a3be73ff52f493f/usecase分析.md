# 具体用例

论文 §2.6 的例句（12）（p.10）：

> “The US fears a spill-over,” said Xirao-Nima, a professor of foreign affairs at the Central University for Nationalities.

对应三个框架：

| 框架 | 锚点 | 来源 | 其他属性 |
|---|---|---|---|
| 客观言语事件 | 整句（隐式） | ⟨writer⟩ | implicit: true |
| 客观言语事件 | said | ⟨writer, Xirao-Nima⟩ | – |
| 直接主观 | fears | ⟨writer, Xirao-Nima, U.S.⟩ | 强度 medium，表达强度 medium，态度 negative |

含义是：作者如实报道 Xirao-Nima 说了这句话；Xirao-Nima 客观地转述美国的立场；在最内层，美国对外溢持负面的担忧（p.10）。

阅读者分析：对“哪些来源对美国表达了负面态度”这类语义查询，需要嵌套来源链和目标，而不只是句级情感标签。论文语料中的目标只覆盖“主体且为正负态度对象”的子集（§2.2），所以以目标为条件的查询会有覆盖缺口。这是项目派生用法，论文没有评测此类查询。

依据：§2.2、§2.5–2.6，PDF pp.6、9–10。
