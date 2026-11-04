# 具体用例

**用例 1：家具检索**（§4，pp.9–10）。用户问"Find a black leather chair"：

1. MCP 客户端（GPT-4.1，通过 ChatGPT API）理解意图，拆成三个子任务：查询翻译、表过滤、图像分析。
2. PostgreSQL MCP 服务器在 `furniture` 表上做关系过滤，得到 126 条候选。
3. Qwen2.5-VL-7B MCP 服务器对候选图片判断"是否含黑色椅子"。
4. 客户端汇总结果。作者观察到纯 GPT-4.1 难以区分黑色椅子与黑色沙发，而 TAIJI 在 Q2 上精确率 85%（GPT 65%）。

**用例 2：迭代算子优化**（Fig.3，p.6）。问题"2023 年最后一个季度哪些供应商向加州交付了电子产品？"：第 1 轮答 Foxconn 与 Pegatron，分析认为 supplier_name 可能不在 deliveries 表中且"电子产品"含糊；第 2 轮改写后答 Foxconn、Pegatron、Jabil Inc.，分析认为类别可能更细；第 3 轮答 Foxconn、Jabil Inc.、Flex Ltd.，判定正确。

**用例 3：知识刷新**（Fig.5，p.8）："美国现任总统是谁？"——通过深度研究插入"Donald Trump 于 2025 年 1 月 20 日就职"，并用机器遗忘删除"Joe Biden 是美国总统"。

阅读者分析：用例 2 和 3 是示意图，未给出数据来源或实际运行记录；只有用例 1 对应实测（阅读者分析）。

依据：§4、Fig.3、Fig.5、Table 1，pp.6–10。
