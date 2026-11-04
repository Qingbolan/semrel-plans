# 具体用例

论文用例子说明 AMR 如何把不同说法归并为同一意义（§1、§3，pp.1–3）。

**例 1（框架论元）**：“The man described the mission as a disaster.”、“The man's description of the mission: disaster.”、“As the man described it, the mission was a disaster.” 都表示为 `(d / describe-01 :arg0 (m / man) :arg1 (m2 / mission) :arg2 (d / disaster))`；“as”“it”等被视为句法糖，不进入 AMR（§3，p.3）。

**例 2（情态与否定）**：“The boy cannot go.” 表示为 `possible` 概念，其 :domain 为 `go-01`，并带 :polarity -；“It's possible for the boy not to go.” 则把 :polarity - 放在 `go-01` 上，两者区分清楚（§3，p.3）。

**例 3（疑问）**：“What did the girl find?” 用 `amr-unknown` 占据 `find-01` 的 :arg1 位置（§3，p.3）。

论文设想的应用包括语义解析共享任务、自然语言生成，以及基于语义的中英机器翻译：用 AMR 标注中英双语数据，训练中文→AMR、AMR→英语的组件（§8，pp.7–8）。

阅读者分析：在语义查询场景中，AMR 可作为把自然语言陈述规范化为“谓词–论元”三元组的中间层，便于跨表达方式匹配同一事件；但 AMR 不区分真实与假设事件、不表示时态，用于事实抽取时需额外处理。

依据：§1、§3–§4、§8，PDF pp.1–3、6–8。
