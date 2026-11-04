# 查询目录

queries.jsonl 保存任务身份、来源性质与 environment_id；nodes.jsonl / edges.jsonl 保存人工重建的逻辑计划；sources.jsonl / query_sources.jsonl 保存查询定义、论文及数据来源。

参照 `Awesome-Dymatic-Operator/chat/benchmark/8-17 data agent query and data/` 的组织：query 声明任务与输入，data 保存语料。这里额外使用 environment 目录登记运行环境，避免把运行配置和数据文件混在一起。

原有 DAG 的页面 inputs 从规范化输入节点生成，标为 logical_only。新增任务的 task_details 保留声明输入与路径核对状态、参考计划、输出 schema、gold、评估规则和原记录。upstream/imports 保存提供文件的快照。7-30 缺少逐查询物理输入绑定时明确留空；参考描述不强行生成节点。记录批处理、多查询批次与模型 batch size 尚无执行配置，页面分别显示缺口。
