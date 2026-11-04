# 工作负载

**数据**：使用 PrivaCI-Bench 的官方测试子集。PrivaCI-Bench 共 6,348 个真实与合成案例，带 Permitted / Prohibited / Not Applicable 标注。本文只用 GDPR 与 AI 法案两个领域：

| 领域 | Permit | Prohibit | Not Applicable | 合计 |
|---|---|---|---|---|
| GDPR | 150 | 478 | 0 | 628 |
| AI Act | 202 | 187 | 211 | 600 |

§5.2 称 GDPR 子集为真实情境，AI 法案子集为合成案例。GDPR 测试集没有 Not Applicable 样本，因此该子集实际是二分类加一个空类（阅读者分析）。

**样本单位**：一段情境描述。ContextLens 在 GDPR 上覆盖 32 个可标为 not sure 的语境因素；AI 法案 10 个问题中 8 个含“None of the above”。

**成本**：GDPR 每例平均输入约 3,003 token（直接提示约 149），输出 410–455 token；AI 法案输入约 522 token。开源模型实验用 2 张 H800，约 4 周 GPU 时间；API 费用约 300 美元。

依据：[ACL 2026 长文，pp.6503–6518，16 页](https://aclanthology.org/2026.acl-long.294)，§4.1、Table 1，PDF p.5；§5.2，PDF p.7；§6、Table 6，PDF pp.8–9；附录 B，PDF p.12。
