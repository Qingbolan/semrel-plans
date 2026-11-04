# 具体用例

**论文贯穿全文的例子：导演—类型—年度评分表（Fig.2、Example 1–4、Fig.4，pp.2–7）**

- **源表**：movies（如 (1, "jurassic park", 101, "Sci-Fi")，genre 可为 "Sci-Fi, Action" 这样的多值字段）、ratings（含 movie、value 等列）、directors。
- **目标 schema**：表级描述 "I need a table containing ratings by genre for each director in 2019 and 2020."；列级描述 director_name（导演姓名）、genre（单个电影类型）、2019 / 2020（该年电影的平均评分）。

**树式推理过程（Example 4，p.7；Fig.4，p.6）**：
1. 初始化：从对应源表的根节点 n0 出发，⟨plan⟩ 决定先清洗 movies 并选取 ratings 的相关列；⟨expand⟩ 生成 Deduplicate、ValueTransform、SelectColumn，执行后得到 n1、n2、n3。
2. 执行失败：随后的计划用 ExeCode 整合评分数据，但执行时出现缺列错误，失败记录在父节点上，不新建状态。
3. 回溯与替代扩展：新的 ⟨plan⟩ 分析错误，发现 SelectColumn 丢掉了 ratings 的 values 列，于是选 n2 作为父节点，修正 SelectColumn，并另外提出 (SplitColumn, Filter, Pivot) 的替代序列，产生 n5–n8。
4. 终止：某叶节点满足目标 schema 后，⟨answer⟩ 抽取根到叶的算子路径作为最终流水线。

Example 1（p.2）强调，若按线性 ReAct 方式过早连接聚合，修正多值 genre 需要回到 movies 处插入 Explode，DeepPrep 可以直接从出错状态分支而不必从头重来。

阅读者分析：这个例子与 atlas 中“多表语义整合 → 透视聚合”类查询的形态接近；但目标仍是确定性的表变换，语义判断只体现在 LLM 选算子与写 ExeCode 代码上，没有逐行调用 LLM 的语义算子。
