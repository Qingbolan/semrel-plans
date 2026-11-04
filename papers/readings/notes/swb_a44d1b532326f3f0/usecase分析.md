# 具体用例

**查看 Revenge 框架**：在交互式提示符执行 `fn.frame('Revenge')`，得到 Fig.1 的展示（p.3）：框架 ID 347、定义、1 个框架关系（继承自 Rewards_and_punishments）、18 个 LU（如 `avenge.v`、`revenge.n`、`vindictive.a`）、14 个 FE（核心 FE 为 Avenger、Injured_party、Injury、Offender、Punishment），以及 2 个核心集合。

用户由展示中的属性名继续深入：`f.lexUnit['revenge.n']` 取 LU 对象，再用 `exemplars[20]` 得到 Fig.2 的例句"A short while later Joseph had his revenge on Watney 's ."，其中标出 Time、Avenger、Offender，以及零形式实例化 `[Injury:DNI]`（§4.5，pp.4–6）。

**按模式搜索**：`fn.frames('(?i)creat')` 返回 Cooking_creation、Create_physical_artwork 等框架；`fn.lus(r'.+en\.v')` 返回 awaken.v、betoken.v 等动词 LU（§4.2，p.3）。

依据：[EMNLP 2017 Demo，D17-2001，6 页](https://aclanthology.org/D17-2001.pdf)，§4.2–4.5、Figs.1–2，PDF pp.3–6。
