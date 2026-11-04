# 工作负载

**数据来源**（§3.2，PDF pp.4–5）：从企业 SOC 收集端到端调查，覆盖 10 个场景，包括云身份、SaaS 文件访问、终端检测和 IAM 策略变更。每条告警记录原始遥测、分析师操作、工具查询、中间推理和最终裁决；用户名、主机名、IP 等敏感字段被假名化。

**规模与结构**（§3.2，p.5）：

| 项目 | 原文描述 |
|---|---|
| 轨迹数量 | "数千条"，未给具体数字 |
| 每条轨迹的行为规则 | 通常 2–4 条 |
| 每条规则的属性 | 通常 6–12 个 |
| 数据源 | Azure AD、AWS、OneDrive、SharePoint、终端 |
| 标签 | 可行动 / 不可行动（再分 4 个子类） |

属性类别包括身份（Username、ARN、UserType）、网络（ClientIP、City、Country、ISP）、系统（OS、Hostname）、操作语义（Operation、EventName、CmdLine、ParentProcess）、工件（FileName）和安全注释（MFA、Severity、Verdict）。

**示例轨迹**（p.5）：O365 登录（IP 地理位置、ISP、操作系统、首次登录标记）；AWS IAM 修改（如 `PutRolePolicy` 调用）；Defender 记录的 Azure AD 组中添加来宾账户；终端上的 PowerShell 命令行与父进程。

**评测划分**：所有实验使用该数据集，Table 4 标注为"测试集"结果（§4.1–4.2，pp.5–6），但原文没有说明测试集大小、划分方式，以及是否与工作流阈值的设定数据分开（阅读者分析）。
