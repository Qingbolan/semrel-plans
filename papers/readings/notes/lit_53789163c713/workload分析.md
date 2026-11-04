# 工作负载

| 数据集 | 记录数（Table 1） | 行数 | 列数 | 答案类型 | 说明 |
|---|---|---|---|---|---|
| WikiTQ | 22,033 | 4–753 | 3–25 | string / list | 正文称训练 17,689、测试 4,344 对 |
| TabFact | 2,024 | 5–47 | 5–14 | true / false | 使用 [57] 提供的 small test set |
| TableBench（正文称 TabBench） | 886 | 2–212 | 2–20 | string / list | 只评 FC 与 NR 两类，直接复用 WikiTQ 提示 |

正文没有明确说明 WikiTQ 主实验用的是 4,344 条测试集还是 Table 1 中的全部 22,033 条；阅读者分析：按惯例应为测试集，但论文未写明。AutoTQA 基线因成本只在 WikiTQ 和 TabFact 各抽 500 条上运行，与其他方法的评测集合不同。

TransTQ 是作者借助 LLM 构造的新数据集：从 WikiTQ 中挑出可做逆变换的表，执行 pivot、stack 等变换生成非关系型表格；正文没有给出其规模。

所有方法最大输入 8,192 token、temperature 0.01；骨干为 DeepSeek-V2.5-Chat、GPT-3.5-Turbo-0613、Llama-3.1-70B-Instruct、Qwen2.5-72B-Instruct。

依据：§6.1、Table 1，PDF pp.8–9；§6.5 Exp-6，PDF p.11。
