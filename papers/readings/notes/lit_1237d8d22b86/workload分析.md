# 工作负载

| 查询集 | 数据库 | 构造方式 | 规模 |
|---|---|---|---|
| IMDB | IMDB 的 6 张表（title、cast_info、movie_info、movie_companies、movie_info_idx、movie_keyword），18 个属性、6 个 PK/FK 连接条件 | 随机起点沿连接图走 t 步，t 从 0 到 |T|−1，各表独立加选择谓词 | 每个 t 生成 1,000 条 |
| JOB-light | 同上 | 70 个手写 JOB-light 查询作模板，谓词字面值均匀采样 | 每模板 100 条 |
| DSB | TPC-DS，24 张表，SF=5，含非 PK/FK 多对多连接 | 选用 15 个 SPJ 模板中的 10 个（tpl018/019/027/040/050/084/091/099/101/102），排除 PostgreSQL 与 Oracle 均超过 300 秒的复杂模板 | 每模板 100 条 |

（§7.1，PDF p.8）

- 划分：默认 80% 训练、20% 测试，随机划分（§7.1、§7.2）；Fig.5 中 DSB 测试为 200 条，与 1,000×20% 一致。
- OOD：IMDB/JOB-light 以 2–4 表查询训练、5 表查询测试；DSB 以 5、6、12 个连接的三个模板测试，其余模板训练（§7.3，PDF pp.8–9）。
- 训练计划来源：PostgreSQL 12.4 与 Oracle 23.0；§7.4 额外加入 DB2 v12.1。
- 执行环境：96 CPU、512GB 内存服务器，shared buffers 128MB、work_mem 2GB，每条查询前清空缓冲以冷启动。

IMDB 查询总数原文未直接给出（依 |T|=6 推算为至多 6,000 条，属阅读者推算）。（阅读者分析）
