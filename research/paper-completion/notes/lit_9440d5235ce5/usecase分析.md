# 具体用例

论文贯穿全文的例子（Fig.1、Example 1，pp.1–3）：用户有一组画家传记，想得到属性 A={Name, Birthplace, Lifespan, Genre, Field} 的表，例如从 d1 抽出 Name=Brull、Birthplace=Spain。

- Lifespan 需要计算（卒年减生年），Evaporate 生成的代码比 PLM 更适合，论文称这类情形下非 LLM 策略可以既更准又更便宜（§7.2，p.10）。
- Genre 的文本“Brull’s early work is realistic, but later he focused on symbolism”会让规则代码误抽为 Realistic，PLM/LLM 的语义理解更合适（p.2）。
- Field 的值 Painting 在相关句“He was known for his many oil paints…”中没有直接出现，仅用属性名嵌入检索会漏掉该块，因此需要参考句增强查询（p.2）。

Doctopus 对每个单元格估计各策略质量和成本，在预算内决定哪些单元格用 LLM 读哪几个块、哪些单元格用零成本方法。

阅读者分析：这个例子与本项目的语义抽取/语义映射查询形态一致；需注意 Doctopus 的选择依赖 10% 带标注的验证集，若项目场景没有验证集，需用 LLM 构造（论文的 VS-LLM 变体，Fig.10），效果略低。

依据：[PVLDB 18(11)，13 页](https://www.vldb.org/pvldb/vol18/p3695-chai.pdf)，§1–§2、§7，pp.1–3、10–11。
