# 数据目录

每个 `<benchmark>/<scenario-or-domain>/manifest.json` 登记数据集，`source_ids` 引用 `catalog/sources.jsonl` 的来源。数据文件与查询定义分离；后续实际文件放在对应数据集目录内，并显式登记 local_path、schema、record_count 和 version。

原有 88 条 DAG 仍只登记来源。新增 8-17 集合显式绑定给定 SEC、ASRS、contract-exhibit、NHTSA 外部目录，inventory.json 保存文件清单；不复制大体量语料。7-30 集合仅含查询分析，原始数据未提供。null 表示未知，不能解释为零条记录。
