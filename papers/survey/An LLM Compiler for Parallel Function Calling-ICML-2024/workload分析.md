# 工作负载

**要验证的问题**：把工具依赖整体写成 DAG 并并行调度，能否在不降准确率的前提下降低延迟与 token 成本；覆盖静态依赖和需要重规划两种情况（§5，p.5）。

**数据集与规模**：

| 工作负载 | 规模 | 调用模式 | 工具 | 来源 |
|---|---|---|---|---|
| HotpotQA comparison（dev） | 约 1.5K 题 | 2 路完全并行 | Wikipedia search（去掉 lookup） | §5.1，p.5 |
| HotpotQA bridge | 未给题数 | 顺序依赖，需重规划 | 同上 | 附录 E.3，p.18 |
| Movie Recommendation（BIG-bench） | 500 题 | 8 路完全并行 | search | §5.1，p.5 |
| ParallelQA（作者构建） | 113 题，56 个实体 | 2–5 路并行 + 多次 join | search + math（LLM 驱动的 numexpr） | §5.2、附录 I |
| Game of 24 | 100 个实例 | 每轮重规划 | thought proposer、state evaluator、top-k select | §5.3，p.8 |
| WebShop | 500 条指令（LATS 为 50 条） | 并行探索商品 | search、explore | §5.4、表 3 |

**任务单位**：一次问答（或一次购物指令）是一个任务；准确率按 3 次运行取平均（附录 D）。

**模型与设置**（附录 D，pp.15–16）：HotpotQA/Movie 用 gpt-3.5-turbo-1106；ParallelQA 用 gpt-4-turbo-1106；24 点用 gpt-4-0613；开源模型为 LLaMA-2 70B（2×A100-80GB，vLLM）。温度为 0（24 点的 proposer/evaluator 为 0.7）。少样本数：HotpotQA 3、Movie 1、ParallelQA 5，各方法用相同示例。

阅读者分析：这些都是基准题或作者构造的题，不是生产流量；单题工具调用数很少（2–10 次左右），并行度上限由题目本身决定。

依据：§5.1–5.4、表 3，PDF pp.5–9；附录 D、E.3、I，pp.15–18、21。
