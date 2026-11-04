# 贡献与评价

**贡献**：

1. 一个通用的 ML 实验任务规格框架（任务描述 + 起始文件 + 评测器），记录完整交互轨迹（动作、理由、观察、每步工作区快照）；
2. 13 个跨模态、跨难度与时效的任务；
3. 一个 ReAct 风格智能体，在响应格式中加入 Reflection、Research Plan and Status、Fact Check、Thought，并提供调用 LM 的复合动作；
4. 对 7 个 LM 与 AutoGPT、LangChain 的比较，以及失败模式与成本分析。

与同期 AgentBench、WebArena 相比，它的特点是任务需要长程实验迭代且结果可被数值评测；“提升 10%”的成功阈值简单可比，但对不同指标与基线强弱并不等价（阅读者分析）。

阅读者分析：几处评测细节削弱结论稳健性：

- 附录 B 说明 house-price、spaceship-titanic、imdb、fathomnet 的起始代码不能直接运行，基线取随机预测（如 imdb 取 0.5 准确率）；
- Table 4 的 house-price 列所有模型都恰为 100.0，像是封顶值；
- Table 4 标题末尾残留一句作者内部批注，追问无基线任务的提升如何计算、任何非零提升是否都是无穷大百分比；
- Table 3 的 Baseline 列在 identify-contrails（40.0）与 CLRS（42.9）上也有非零成功率，论文未解释（阅读者分析）。

依据：§1–3，pp.1–6；Tables 3–4，pp.7–8；附录 B，p.15。
