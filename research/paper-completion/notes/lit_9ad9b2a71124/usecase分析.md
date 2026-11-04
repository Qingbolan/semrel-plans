# 具体用例

Figure 2 右侧是 DABStep-Research 的开放研究例：指令只有“进行开放式数据科学研究并输出研究报告”。环境中有 7 个文件，包括 fees.json（518.7KB）、manual.md、merchant_category_codes.csv、merchant_data.json、payments.db（21.7MB）等。

模型先在 `<Analyze>` 中规划，从小文件和手册入手；在 `<Understand>` 中读出商户类型、MCC、ACI 与费用公式 fee = fixed_amount + rate × transaction_value / 10000。

随后写代码读取 MCC 表，执行结果为 769 个 MCC，再逐步分析费用规则。最终生成支付手续费结构报告，含执行摘要、方法、参数分布、相关性和费用模拟附录（Figure 1）。

这是“多文件、异构格式、无明确问题”的开放分析场景。报告中的数值（如 Figure 1 写作 r=327 的“相关”）原文未逐项核实，只做了 LLM 评审打分（阅读者分析）。

依据：Figure 1–2、附录 A、附录 C，PDF pp.1–2、16–23。
