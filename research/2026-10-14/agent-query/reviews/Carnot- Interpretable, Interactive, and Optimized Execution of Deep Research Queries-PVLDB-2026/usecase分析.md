# 具体用例与干预

§3产品投诉分析先生成计划，用户发现filter只处理ratings，于chat补充必须考虑review text；planner据此重规划受影响算子。另一种操作是在notebook运行若干cell，查看false negatives，直接修订语义filter提示，再从修改点继续。

图2原始界面问题为“Which of these papers is about AI?”，可查看filter谓词和map字段说明、逐步结果并下载CSV。该截图的计划来源是作者系统演示；若将其转成当前图册DAG，必须记录为演示实例，不能称运行痕迹已经在本项目复现。

此工作提示当前页面应把query、可读取数据、实际输入列、算子I/O作为并列可检查对象。环境是dataset访问上下文；用户不需要看到一排空的engine/model/hardware字段。
