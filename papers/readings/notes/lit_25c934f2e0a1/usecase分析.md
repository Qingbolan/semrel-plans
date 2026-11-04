# 具体用例

Figure 4 的 DSEAL 示例：会话中已有人口表 `pop`，查询为“给出 2023 年与 2050 年人口密度的相关系数，保留两位小数”。

YAML 配置：验证器模板 `basic`；`namespace_intact` 允许更新的变量仅为 `pop`；结果比较容差 `atol: 0`；执行限制禁止访问名为 `pop_heldout_test` 的变量，最长执行 0.5 秒；外部数据为 `pop.csv`。参考代码是 `(pop['pop2023'] / pop['landAreaKm']).corr(pop['pop2050'] / pop['landAreaKm']).round(2)`。

评测时，智能体只看到查询和会话；DSEval 执行其代码后同时检查返回值是否与 oracle 一致、会话中的数据是否被不应有的修改、是否越权读取留出数据以及是否超时。

依据：§4.1、Figure 4，PDF p.3；§3.2，PDF p.3。
