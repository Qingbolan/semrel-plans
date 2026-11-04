# 具体用例

**原文示例**（附录 C 的工具轨迹，p.18；Spider 数据发现）：问题本身在轨迹中被省略，从关键词看是关于员工及其过去职位的查询（阅读者推断）。目标是找出能回答该问题的表。

**不带工具的 LLM**：只能看到 BM25 返回的前 20 张候选表的标题和 schema，一次作答（附录 B.1）。

**SEED 的做法**（带工具的 LLM 模块）：
1. 思考：需要找员工、职位、过去相关的表 → 动作 `SEARCH_KEYWORDS(['employees', 'job', 'past'])`；
2. 观察：返回 `hr_1-employees`、`hr_1-jobs`、`hr_1-job_history` 以及若干无关表；
3. 依次对这三张表调用 `GET_SCHEMA`，确认 employees 有 `JOB_ID`、jobs 有 `JOB_TITLE`；
4. 动作 `SUBMIT(['hr_1-employees', 'hr_1-jobs', 'hr_1-job_history'])`。

可用工具共五个：`GET_SCHEMA`、`BM25`（前 20 张表）、`SEARCH_KEYWORDS`（精确字符串匹配前 20）、`SEARCH_VALUE`（Levenshtein 距离 0.2 过滤）、`JOINT_SEARCH`，外加 `SUBMIT`；只给 LLM 一个人工示例演示工具用法（附录 B.1）。

**效果**（Table 8，p.15）：Spider 上 F1 从不带工具的 50.7 提升到 85.7。

阅读者分析：这是观察驱动的数据探索，不只是缓存分类结果；但它只用于表发现任务，与实体匹配中的降本机制是两回事。

依据：[arXiv 2310.00749v3](https://arxiv.org/abs/2310.00749v3)，附录 B.1、C、Table 8，pp.15–18。
