# benchmark分析

[论文原文](https://arxiv.org/html/2410.05080v2)

Table 3以每题3次独立尝试中按SR/VER/CBS/成本顺序选最佳结果。Claude-3.5-Sonnet self-debug无专家知识SR32.4%、有知识34.3%，对应每任务API费用$0.057/$0.061；o1另列，不应略去后称其为所有模型最优。三次尝试不是输入batch。专家知识有时降低可执行率但提高成功率。当前官方仓库已发布2026 verified数据，复现实验须锁定版本。
