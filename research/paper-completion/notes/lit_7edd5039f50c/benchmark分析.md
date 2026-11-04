# 评测与边界

**基线**：微调方法 T5-3B、Tapex、TaCube、OmniTab、SASP、BART-Large；同一 Codex 下的端到端 QA 与标准 SQL 语义解析（§3.1，p.5）。所有方法统一用作者修改后的评估器重评：在官方评估器前加一步预匹配，把 SQL 输出 1/0 对应 yes/no 等语义正确情形算对（§3.1，p.5；官方评估器结果见附录 C.2）。

**实验 1（主结果）**（Tables 1–2，p.5）：

| 方法 | WikiTQ dev | WikiTQ test | TabFact 小测试集 |
|---|---|---|---|
| Tapex（微调） | 60.4 | 59.1 | 85.9 |
| OmniTab / SASP（微调） | – | 63.3 | 77.0（SASP） |
| Codex 端到端 QA | 50.5 | 48.7 | 72.6 |
| Codex SQL | 60.2 | 61.1 | 80.7 |
| Codex Binder | 65.0 | 64.6 | 85.1；加检索选例 86.0 |

WikiTQ test 上 Binder 比此前最好（OmniTab 63.3）高 1.3 个百分点，比 Codex SQL 高 3.5；TabFact 上检索选例只额外带来 0.9（§3.2，p.6）。

**实验 2（WikiTQ dev 分解）**（Table 3，p.6）：程序不可解子集上 Binder 41.3、Codex SQL 31.2、端到端 QA 40.3；可解子集上 Binder 71.8、Codex SQL 68.4。不给表格时 Codex 只答对 12.4%，作者据此认为 Codex 没有记住数据集答案。

**实验 3（错误分析）**：从 dev 抽 100 个错误样例，语法错误 5%，语义错误 64%（其中未使用 Binder API 32%、结构错误 22%、token 错误 10%），执行错误 15%，标注或评估误判 16%（Table 4，p.7）。

**实验 4（扩展性与鲁棒性）**：表扩到 100/200/500 行时，端到端 QA 大幅下降，Binder 只略降，因为其输入始终只有三行（Figure 2，pp.7–8）；加入干扰后 Binder 降 1.3、端到端 QA 降 6.7 个百分点（Figure 3，p.8）。

**实验 5（Python 与多模态）**：程序不可解子集上 Binder-Python 34.4 对 Codex Python 30.7（Table 6）；MMQA dev 上 Binder F1/EM 为 57.1/51.0，高于端到端 QA 的 55.4/48.0，用 oracle 检索时 64.5/58.1，仍低于微调的 PReasM-Large 65.5/59.0（Table 7，p.8）。

**边界**：作者未写局限章节；指出评估很耗时，有效的示例选择仍是开放问题（§3.1–3.2，pp.5–6）。

结果依赖闭源的 code-davinci-002 API，修改后的评估器也让与他人报告值的直接比较需谨慎（阅读者分析）。

依据：§3–§4、Tables 1–7、Figures 2–3，PDF pp.4–9。
