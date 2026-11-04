# 具体用例

SDSS 天体物理的三条运行示例（§2，PDF p.3）：
- **Q1**（Easy）：“Find all Starburst galaxies.” → `SELECT s.specobjid FROM specobj AS s WHERE s.subclass = 'STARBURST'`；
- **Q2**（Medium）：查询红移大于 0.5、小于 1 的光谱观测星系的 id、赤经、赤纬与红移，需要知道 `z` 表示红移、`ra` 表示赤经；
- **Q3**（Extra hard）：连接 `photoobj` 与 `specobj`，过滤 `class = 'GALAXY'` 且 `p.u - p.r` 介于 1 与 2.22 之间。

合成管道的例子（Figure 1，PDF p.2）：种子 “Find all Starburst galaxies” 抽成模板 `Select T(*) C(*) Filter(2) T(*) C(*) V(*)`，采样出 `SELECT T1.objid FROM neighbors AS T1 WHERE T1.neighbormode = 2`。GPT-3 生成多个候选问题，判别阶段淘汰把 “=2” 误述为 “smaller than 2” 的候选。

阅读者分析：这个用例说明，领域术语到缩写列名的映射和属性间数值运算是主要难点，而非 SQL 语法本身。
