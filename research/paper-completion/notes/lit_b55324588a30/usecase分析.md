# 具体用例

**城市表的时区填补**（Figure 2，p.5）：表中有 city、country、timezone、population、postalcode 列，Copenhagen 一行的 timezone 缺失。

1. 属性级检索：`p_rm` 提问哪些属性对“填 timezone”有用，LLM 选出 country。
2. 记录级检索：`p_ri` 对候选城市（Alicante、Florence、Athens、Helsinki、Antwerp、London）按 0–3 分打相关度，取 top-k。
3. 上下文解析：把 `city: Florence, country: Italy, timezone: Central European Time` 等序列化文本用 `p_dp` 改写为 “Florence is a city of Italy and in the timezone Central European Time…”。
4. 目标提示：`p_cq` 依据示例把 claim 改写成 “Copenhagen is a city of Denmark and in the timezone __.”，再由 LLM 填空，得到 Central European Time。

**附录案例**（附录 B，p.15）：Restaurant 中 “ruth's chris steak house (los angeles)，224 s. beverly dr.” 的 city 真值为 Beverly Hills；FM 随机/人工示例均输出 los angeles，UniDM 检索到同街区 Belvedere（Beverly Hills）等记录后输出 Beverly Hills。

阅读者分析：这个例子说明语义检索出的“近邻记录”能纠正名字带来的误导，但它是挑选的单个案例，不代表整体错误分布。

依据：Figure 2、§4.2–4.4、附录 B，PDF pp.5–7、15。
