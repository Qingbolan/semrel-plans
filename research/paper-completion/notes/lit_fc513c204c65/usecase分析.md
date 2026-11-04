# 具体用例

**场景**：一个反复提交相同查询模板的分析负载（作者引用 Redshift 舰队分析与 Microsoft 生产优化器部署的观察，认为重复查询常见），在 PostgreSQL 上运行。

**流程**（Figure 1、Figure 2 示例）：

1. 首次遇到 CEB 查询 `ceb_1a`（如 `select count(*) from ... AND 1925 < t.production_year`），按默认计划执行，记录约 300 ms 一类的执行时间存入 C_i。
2. 再次遇到时，先让 PostgreSQL 给出统计信息与默认计划，同时用该 SQL 的嵌入去 C_p 检索 k 条相似 JOB 查询及其 hint。
3. 把相似样例、当前 SQL 与统计、默认计划、历史最好计划及其收益拼成提示，LLM 输出如 `/*+ NestedLoop(...) Leading((((...)))) */` 的 hint。
4. 执行带 hint 的查询，若时间更短则更新最佳计划；若历史最佳仍慢于默认，就以负收益提示 LLM 避免重蹈覆辙。

**开销**：SFT LLaMA3.2-3B、NoRef、Join Order 设置下，平均检索 0.7 ms，推理约 236 ms（A6000）或 160 ms（A100）；CEB 上 SERAG 计划平均执行 520.67 ms，PostgreSQL 为 922.86 ms，作者据此称端到端时间仍更优（§4.4）。

阅读者分析：每次重复执行都要付一次约 0.2 s 的推理，对执行时间本就很短的查询未必划算；论文只给出平均值，没有按查询拆分。

依据：§1、§3、§4.4、Figures 1–2，PDF pp.1–4。
