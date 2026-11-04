# 环境目录

每个 `<benchmark>/<scenario-or-domain>/manifest.json` 声明一个环境，查询通过 `environment_id` 引用，环境通过 `dataset_id` 引用数据目录。共享环境只登记一次。

当前环境均为未配置、未执行；engine、model、hardware 的 null 表示未知，不表示默认配置。目录是逻辑查询的复现环境登记，不是已部署的执行环境。
