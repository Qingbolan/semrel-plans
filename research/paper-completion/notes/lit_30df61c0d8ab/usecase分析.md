# 具体用例

原文 Figure 9 给出 Wine 数据集分类分析的对话用例（PDF p.26）：

1. **用户**：“这是 Wine 数据集，我想做分类，能推荐一些模型吗？”LAMBDA 列出逻辑回归、SVM 直至 AdaBoost 共 9 种模型及简要说明。
2. **用户**：“目标列是 class，先画相关矩阵。”程序员生成 pandas/seaborn 代码，执行后返回热力图路径与解释。
3. **用户**：“标准化数据，再对 class 列做序数编码。”返回处理后的数据表预览。
4. **用户**：“基于上一步数据，对 LogisticRegression 做交叉验证，用准确率评估。”执行 5 折交叉验证，平均得分 0.9889，并保存 best_logistic_regression_model.pkl。
5. **用户**：“训练 XGBoost 并调参，打印最佳参数与交叉验证分数。”GridSearchCV 得到 learning_rate=0.1、max_depth=3、n_estimators=100，最佳分数约 0.9554。
6. 最后生成分析报告。

知识整合用例：计算最近相关矩阵时，作者先展示 GPT-4 Advanced Data Analysis 的失败，再用 LAMBDA 从知识库调入二次收敛 Newton 方法代码完成任务（§5，PDF pp.24–25；演示为视频）。

阅读者分析：用例体现的是“用户逐步下指令、智能体逐步生成并执行代码”的人在回路模式，每一步状态保存在同一 IPython 内核中。规划由用户承担，这与 InsightBench 等要求智能体自行提出问题的端到端设定不同。

依据：§3.5、§5、Figure 9，PDF pp.13、24–26。
