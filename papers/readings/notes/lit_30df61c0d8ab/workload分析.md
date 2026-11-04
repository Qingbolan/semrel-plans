# 工作负载

**数据集（Table 1，PDF p.17）**：

| 用途 | 数据集 |
|---|---|
| 分类 | AIDS Clinical Trials Group Study 175、NHANES、Breast Cancer Wisconsin、Wine；Iris 用于案例研究 |
| 回归 | Concrete Compressive Strength、Combined Cycle Power Plant、Airfoil Self-Noise；Abalone 与 Heart Disease 标为“回归-案例研究” |
| 高维数据 | TCGAmirna（544 行×802 列）、EMTAB386（129×10360）、GSE49997（194×16051） |
| 缺失数据 | Framingham Heart Study、Student Admission Records |
| 图像 | MNIST |
| 文本 | SMS Spam |

高维数据规模见 Table 3（PDF p.19）。所有设置均用 5 折交叉验证，分类报告准确率、回归报告 MSE（§4.1，PDF p.17）。

**知识整合任务（§4.2，PDF pp.21–22）**：三项领域任务——用 PAMI 库做模式挖掘（PM）、用 Qi & Sun（2006）的 Newton 型方法计算最近相关矩阵（NCM）、非负神经网络的不动点（FPNENN）。每项任务单次运行可在 1 分钟内完成，设 5 分钟运行上限。

**检查员消融（补充 A.2，PDF pp.37–38）**：在含缺失值的 Heart Disease 数据集上，用 Qwen1.5-110B 生成指令，过滤后 454 条；程序员与检查员都用 Qwen1.5-32B。

**指令来源**：经典数据实验中只提供英文提示，作者称 LAMBDA 一侧全程无人参与（§4.1.1，PDF p.19）；但具体指令文本、每个模型的超参数选择过程在正文中没有完整列出。

阅读者分析：Table 1 把 Heart Disease 标为回归案例，而 Table 5 却以准确率报告该数据集（PDF pp.17、20），任务类型存在不一致。整体上，这些是经典小型 ML 数据集，而非专门构造的智能体基准，没有固定的查询集或标准答案。

依据：§4.1–4.2、Tables 1、3、补充 A.2，PDF pp.17–22、37–38。
