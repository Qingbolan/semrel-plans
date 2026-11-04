# 具体用例

**跨语言共指示例**（§5.3，PDF p.5）：四个对齐句子如下。

- EN："The White House is considering an auto rescue plan"
- IT："La Casa Bianca valuta il piano di salvataggio dell'auto"
- NL："Het Witte Huis overweegt reddingsplan autosector"
- ES："La Casa Blanca está considerando un plan de rescate del sector automovilístico"

实体实例 White House 用唯一 ID 和 DBpedia URI 表示（`http://dbpedia.org/page/White_House`），链接到四种语言中的四个提及。事件实例 considering 也有唯一 ID，被 "considering"、"valuta"、"overweegt"、"considerando" 四个提及引用，并通过 HAS_PARTICIPANT 关系连到 White House。

**语义角色示例**（§3.1，PDF p.3）：在 "Apple Inc. today has introduced the iPhone 4" 中，事件 "introduced" 的 Arg0 是 "Apple Inc."，Arg1 是 "iPhone 4"。

阅读者分析：这种"实例 ID + 多语言提及 + 参与者 + 时间锚点"的结构，可以支持跨文档、跨语言的事件时间线查询；但标注只覆盖文档前 5 句，构造查询时需要注意这一覆盖边界。
