# 具体用例

Example 1（§2.1、Table 1，PDF pp.2–3）："A couple of weeks ago, the US state department in its annual report had revealed that Iran, Pakistan and some other countries are the violators of human rights."

MPQA 对这句话的标注：

| 表达 | 类型 | 极性 | 强度 | 嵌套来源 |
|---|---|---|---|---|
| 整句（隐式） | OSE | — | — | [AUTHOR] |
| in its annual report had revealed | DS | — | medium | [AUTHOR], USSD |
| are the violators of human rights | ESE | negative | medium | [AUTHOR], USSD |
| are the violators of human rights | arguing（态度） | positive | medium | 继承 DS |
| are the violators of human rights | sentiment（态度） | negative | high | 继承 DS |

在本文任务中：类型模型输入句子和表达 "are the violators of human rights"，应输出该表达所传达的类型集合；来源生成模型应输出嵌套来源链 "the US state department"（不计作者）。

阅读者分析：上表按 -layout 抽取文本的列对齐复原；同一短语既是 ESE（negative）又承载 arguing（positive）态度，说明同一 span 的不同标注项属性可以不同，下游使用时不能按 span 去重。
