# 具体用例

**原文示例**（Figure 3(b)，p.6；§5.2，p.7）：“如果 Stanford 和 UCLA 合并，诺贝尔奖得主会比 UC Berkeley 多吗？”

**ReAct 的做法**：先搜索 Stanford，读结果；再搜索 UCLA；再搜索 UC Berkeley；然后调用数学工具相加、比较。三次查找互不依赖，却要串行等待，每一步都重新调用一次 LLM。

**LLMCompiler 的做法**（据 §3 与 Figure 3(b) 组合描述）：
1. Planner 一次写出计划：`$1 = search(Stanford)`、`$2 = search(UCLA)`、`$3 = search(UC Berkeley)`、`$4 = math($1 + $2)`、`$5 = math($4 > $3)`；
2. Task Fetching Unit 发现 `$1–$3` 无依赖，同时发给 Executor；
3. 三个结果返回后替换占位变量，`$4` 解锁执行，随后 `$5`；
4. 最后由 LLM 汇总观察给出答案。

**效果**：ParallelQA 这类题上，gpt-4-turbo 下 LLMCompiler 平均延迟 16.69 s，ReAct 35.90 s（2.15×）；每千题估计成本 $103 对 $480（表 1、表 2）。

**原文另一个例子**（Figure 1）：“Scott Derrickson 和 Ed Wood 国籍相同吗？”两次搜索并行，HotpotQA 上平均 1.8× 加速。

阅读者分析：第 1 步的具体计划文本是阅读者按 Figure 2 的写法补全的，原文 Figure 3(b) 只画了依赖图（3 个 search → 2 个 math → output）。

依据：§3、§5.2、Figure 1–3、表 1–2，PDF pp.2–7。
