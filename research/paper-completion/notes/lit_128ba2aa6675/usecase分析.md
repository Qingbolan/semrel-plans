# 具体用例

论文用例 2（§6.2.2，p.8，Fig.5）：Bob 分析大学数据库（student 表含 stuid、age、sex、major、advisor、city_code，另有 faculty、department 等表），输入“Analyze the age distribution of students in different majors”。

- 初始输出：DeepVIS 生成每个学生一个点的散点图，难以比较各专业。
- 定位：Bob 点开 S1 节点，看到模型理由是“散点图能展示 major 与 age 两个变量关系”，意识到自己的问题不够具体。
- 纠正：他输入“Show the average age of each major”并执行手动纠正，系统把图表从 SCATTER 改为 BAR、选择列从 age 改为 AVG(age)、加入 GROUP BY major，并自动重生成后续步骤。

用例 1（§6.2.1，pp.7–8）：Alice 要找学生最多的城市，模型最初因“问题未要求排序”省略 ORDER BY；她对排序步骤启用自我纠正，模型改为降序排序。

阅读者分析：两个用例都是作者演示，展示的是“步骤级可干预”这一交互能力；它们不构成准确率证据。对本项目而言，可借鉴的是把查询计划拆成可检查的中间决策并允许局部重算后续步骤。

依据：[arXiv v2，11 页](https://arxiv.org/abs/2508.01700)，§6.2，Figs.3、5，pp.5、7–8。
