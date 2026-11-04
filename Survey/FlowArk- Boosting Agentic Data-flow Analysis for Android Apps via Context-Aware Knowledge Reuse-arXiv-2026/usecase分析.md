# 具体用例

**原文示例**（§2.1、Figure 2，pp.3–4）：两个 agent 实例分析同一应用的两个 UI 源点。

| | Alpha（先执行） | Bravo（后执行） |
|---|---|---|
| 源点 | password 输入 | deviceId 输入 |
| 回调传入的协议/字段 | SSH / PASSWORD | WEBDAV / DEVICE_ID |
| 下游 sink 检查 | SshHandler | WebDavHandler |
| 共同经过 | 中间层的设置解析与协议处理器分发逻辑 | 同左 |

Alpha 通过跨文件分析确认两条事实：解析器把输入值写入由 field 参数选择的 profile 槽位；分发器把 profile 交给由 protocol 参数选择的处理器。这两条与 SSH/PASSWORD 无关，Bravo 走到同一段代码时同样适用。

**提炼出的知识条目**（Figures 4–5，p.7）：

- 摘要：`field` 选择要更新的 profile 槽位，`protocol` 选择下游网络处理器；
- 适用条件：活跃路径到达 `UiInputController.onFieldChanged(protocol, field, value)`；
- 可跳过：字段到 profile 的赋值与协议分发；优先检查：由 `protocol` 选出的处理器；
- 匹配规则：`require_any` 为 exact_symbol `UiInputController.onFieldChanged`，`exclude` 为 package_prefix `com.example.test`；
- 下游提示：SSH → `Handlers.kt@100 SshHandler.connect`，WEBDAV → `Handlers.kt@273 WebDavHandler.connect`。

**运行时**（§2.2 C3）：Bravo 的初始任务只说“检查 deviceId 是否流向网络 sink”，看不出会经过同一机制。当它的代码阅读工具输出出现 `onFieldChanged(WEBDAV, DEVICE_ID, id)` 时规则命中，FlowArk 注入条目，并只附上 WEBDAV 对应的下游提示；Bravo 跳过中间层，直接检查 WebDavHandler。

阅读者分析：共享代码的知识可复用，不等于泄漏结论相同；该示例是说明性的，论文没有单独给出它的费用收益。

依据：[arXiv 2607.11308v2](https://arxiv.org/abs/2607.11308)，§2.1–2.2、Figures 2、4–5，PDF pp.3–7。
