# 具体用例

附录 H 给出三个取自 MLE-Bench 真实运行的案例（PDF pp.21–24）：

**分支内演化（aptos2019-blindness-detection，视网膜病变分级）**：某分支经过 6 步起草与改进后停滞，此前的 EMA、Mixup、交叉验证等正则化尝试都没有提升分数。Evolution Agent 回看本分支轨迹，判断瓶颈在于架构归纳偏置（ViT 的 16×16 patch 可能稀释微小病灶），提出把 DINOv3 主干与 ResNet50 融合；规划器只指定 `model_design` 模块，编码器用 diff 模式修改代码。

**跨分支参考（mlsp-2013-birds）**：当前分支用对称 Focal Loss 停滞，Fusion Agent 从另一分支的强解中找到 Asymmetric Loss，并以 diff 编辑替换损失函数。

**多分支聚合（同一任务）**：检测到全局停滞后，Aggregation Agent 把多个分支的成功组件（EfficientNet-B1 + GeM 池化、带通滤波、多标签 Focal Loss、5 折交叉验证）合成为根节点下的新分支起点。

阅读者分析：这三个案例说明触发条件（分支停滞 τ_branch=3、全局停滞 τ_global=6，Table 4）如何映射到不同算子，但只是定性示例，论文没有统计各算子被触发的频率或各自带来的平均增益。
