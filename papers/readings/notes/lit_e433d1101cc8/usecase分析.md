# 具体用例

**CIFAR-10 改进任务**：工作区含 train.py（简单 CNN 基线）、数据与说明；目标是在 10 个 epoch 内把测试准确率提升 10% 以上，并把测试集各类概率写入 submission.csv。

附录 D.1 记录的一次 Claude v1.0 运行：

1. 第 0 步制定计划：理解脚本与数据 → 试超参数、正则化、架构 → 先跑基线 → 逐项试验 → 达标后写提交文件。
2. 运行基线：5 个 epoch 后测试准确率 52.53%。
3. 试验：学习率提到 0.3 效果明显变差；加 dropout（p=0.5）得 49.34%；把卷积层滤波器增加到 32 与 64 得 64.31%。
4. 第 10 步：用改进架构生成 submission.csv 并提交。

Figure 2 展示单步结构：提示含工具说明、任务描述、响应格式与最近 3 步历史；响应依次为 Reflection、Research Plan and Status、Fact Check、Thought、Action 与 JSON 格式的 Action Input。

**失败样例**（附录 D.2–D.3）：有的运行把 26.35% 声称为比 51.80% 基线“提升 10%”；在 parkinsons 任务中，智能体不知道 SMAPE 越低越好，反而努力提高它。

依据：Figure 2，p.5；附录 D.1–D.3，pp.15–18。
