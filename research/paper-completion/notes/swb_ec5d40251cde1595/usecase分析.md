# 具体用例

政策原文“A periodic oral evaluation is a payable benefit once in a six-month period”被识别为合规规则：六个月内至多一个服务单位。Clais 抽取 `hasMaxUnits(1)` 及时间条件 `hasAmountOfTime` / `hasUnitOfTime`，专家在界面确认后，系统将其规范化为不合规规则 `hasMinUnit(2)`，并把两个时间条件合并为 `hasSlidingWindowInDays(180)`（Fig. 1c–e；pp.13–14）。

执行时，`hasApplicableService` 映射为 filter，只保留该服务代码的理赔；滑动窗口映射为 splitter，把患者理赔序列切成不超过 180 天的子序列；evaluator 判断累计单位是否超过阈值。任何一个上下文中被判 true 的理赔即为 at-risk（p.14）。

界面中调查员可选中某段政策文本，查看该规则命中的理赔统计，并对单条理赔看到解释，例如 “D4355 and D1110 are mutually exclusive within 1 day(s)”（pp.5–6，Fig. 3b）。

这一流程本质是“文本 → 结构化谓词 → 对表格做分组窗口聚合过滤”，可视为语义抽取后接确定性查询执行的范式（阅读者分析）。

依据：Fig. 1 图注 p.3；Results p.5；Method pp.13–14。
