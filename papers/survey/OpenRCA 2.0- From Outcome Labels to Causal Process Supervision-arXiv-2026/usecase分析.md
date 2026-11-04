# 具体用例

**原文案例：说对根因，但跳过传播服务**（§3.3，Figure 4，p.7）

TrainTicket 上的一次注入，真值是 4 跳传播：ts-basic-service 经 ts-travel-service 和 ts-travel2-service 两条分支，传到 ts-route-plan-service，再到 ts-travel-plan-service 与 ts-ui-dashboard。

Claude 正确指出根因 ts-basic-service，也找到了症状，但画出的图编造了一条从 ts-basic-service 直达 ts-route-plan-service 的边，漏掉中间的 travel 与 travel2 两个服务。

| 评分方式 | 结果 |
|---|---|
| 结果层（AnySvc） | 命中 |
| 节点 Precision / Recall | 100% / 66.7% |
| 边 Precision / Recall | 66.7% / 33.3% |
| Edge F1 | 44.4% |

这里的前后对比是“评测能否发现错误”，不是 PAVE 让智能体答得更好。作者把它归为失败模式 (1)“探索不足就过早下结论”：说中服务后停止核验，传播链便跳过了真值实际经过的中间节点。

**运行示例**（Figure 3，p.4）：真实根因是 Seat，Route 只因背景噪声显得异常。结构剪枝删掉拓扑上不可能的边（如 Route→Seat），但 Route 仍被标记；因果核验发现 Route 的偏差与基线噪声一致而将其丢弃，留下 Seat→Travel→Order。

**另外两种失败模式**（§3.3，pp.6–7）：
- 存在偏差：Pod 被杀后该服务不再产生 span，许多智能体把“没有报错”当作“没有故障”，转而怪罪因下游消失而报错的上游调用方；
- 显著性捕获：智能体锁定误差或延迟变化最大的服务，即便那只是下游放大效应；也会轻信声称超时的 SEVERE 日志，哪怕对应 span 只用了几十毫秒。

依据：[arXiv 2606.27154v2](https://arxiv.org/abs/2606.27154v2)，§2.2–2.3、§3.3、Figures 3–4，PDF pp.4、6–7。
