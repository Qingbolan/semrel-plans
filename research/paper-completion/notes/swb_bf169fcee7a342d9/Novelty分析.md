# 贡献与评价

**原文三项贡献**（Introduction，PDF p.1）：
1. LogicAD：基于文本特征记忆库的单样本逻辑异常检测算法，结合 AVLM 与 LLM；
2. 文本特征抽取流程：Guided CoT、GroundingDINO ROI 裁剪、每区域生成 K=3 次文本，用 text-embedding-3-large 嵌入并以 LOF 过滤离群描述（Text Feature Extraction，PDF pp.3–4）；
3. 逻辑推理器：用 LLM 两样本提示把描述转为一阶逻辑，用 Prover9 判定并输出最小解释，不需要人工或动态阈值。

作者称这是首个把 AVLM 与纯逻辑推理框架（ATP）结合的异常检测方法（Related Work，PDF p.2）。

**评价（阅读者分析）**：
- 新意在于把 LINC / Logic-LM 等"LLM 翻译 + 定理证明"的神经符号思路用于工业视觉检测，并以文本嵌入代替视觉记忆库。
- 与 LogiCode 相比，LogicAD 不需要像素级分割，但仍需人工提示和 Σ_norm；两者都依赖人工写出的"正常规则"。
- 逻辑推理器只输出 0/1，无法计算 AUROC；报告的 AUROC 来自格式嵌入分支，可解释性来自另一分支，两者并非同一决策过程（Table 3，PDF p.6）。
- 声称的 "18.1% ↑" 实为与 AnomalyMoE 的绝对差 18.1 个点（86.0 vs 67.9），不是相对百分比。
