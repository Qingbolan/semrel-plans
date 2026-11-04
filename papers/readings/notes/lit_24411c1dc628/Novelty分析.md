# 贡献与评价

原文贡献：
1. 把研究智能体形式化为“搜索策略 × 算子”的组合，便于做受控对比（§2）；
2. AIRA-dojo 框架：Jupyter 动作空间、Apptainer 隔离、预装 CUDA/PyTorch/TensorFlow 的 superimage，可在 HPC 上大规模并行（§3.1–3.2；作者称 Docker 依赖 root 权限，不适合 HPC，§6）；
3. 新算子集 O_AIRA，包括按子节点数调整复杂度提示（minimal/moderate/advanced）、限定记忆范围（Draft/Improve 只看兄弟节点，Debug 看完整调试链）、显式鼓励思考 token，补全 token 平均约增加 2 倍（§4.1，PDF p.6）；
4. 三个智能体：AIRA greedy、MCTS（UCT，不做 rollout，直接用代理适应度作为叶子值）、Evo（按适应度比例选择父代，Improve 或 Crossover）（§4.2）；
5. 对泛化差距的定量分析（§5.3）。

阅读者评估：最有说服力的发现是“算子是瓶颈”。使用 AIDE 算子时，MCTS/Evo 相比 greedy 没有优势（Fig. 3）；换成新算子后，各策略的排序才发生变化。不过各策略之间的差距（例如 47.7 对 45.5）与 95% 置信区间相比并不大，原文也承认排名会随时间变化。另外，摘要中“39.6% → 47.7%”的基线数值，与正文中 AIDE greedy R1 的 39.8% 不完全一致；39.6 更接近 Fig. 1 中 AIDE greedy o3 的 39.55，原文没有说明对应哪个基线。
