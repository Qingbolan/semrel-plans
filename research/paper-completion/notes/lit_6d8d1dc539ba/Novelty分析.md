# 贡献与评价

原文声称的贡献（§1，PDF p.2）：
1. 归纳时间序列图表摘要的要素（Fig.2）与 LLM 幻觉类型。分类基于 4 个 LLM（GPT-4、Claude3、GPT-4o、LLaMA-3.1-70B）对 20 张真实图表生成的 80 份摘要、1,083 句，其中识别出 199 个幻觉实例；4 位作者先独立分类再讨论达成一致（§3.3，PDF pp.3–4）。
2. ChartInsighter 流水线（§4，PDF pp.4–6）分三步。Brainstorming：Uni-Insighter 调用数值模式分析模块，按显著极值把序列切成 patch，并按方差阈值合并；Multi-Insighter 生成三次多维描述并多数投票，再调用多维关系分析模块。Refining：Multi-Insighter 与 Writer 迭代补充，至多 5 轮。Self-consistency Test：专门复查极值错误和比例感知错误。
3. 一个带逐句幻觉标注的基准（§5）。

方法本质上是把统计计算外包给代码模块，再加 LLM 多数投票和自检，组合了 PoT、self-consistency 和多代理等已有思路，创新在于针对时间序列摘要的具体设计。论文没有消融实验，无法判断各模块分别贡献多少。（阅读者分析）
