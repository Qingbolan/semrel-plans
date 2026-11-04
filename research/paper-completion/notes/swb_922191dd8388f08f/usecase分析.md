# 具体用例

**ALFWorld 的“找到并拿起物体”**（Example 1，PDF p.3；Figure 1，PDF p.2）。

两条成功轨迹分别是：

- 依次访问并打开 drawer1、drawer2，再去 desk1、bed，拿到 book；
- 先访问 shelf1、shelf2，再打开 drawer1、drawer2，拿到 mug。

两者经过的地点数量和对象不同，但共享同一个参数化控制流：

`repeat go_to(l); if can_open(l) then open(l); check_target(l,o) until found(o) then take(o)`

SKILL-DISCO 把这一模式编译成 `search([locs], obj)` 之类的可调用技能。技能会根据观察分支，例如容器已打开就跳过 open。

类似地，“加热物体”被编译为 go_to(mic) → open(mic) → heat(o)，打开前检查是否已开（Figure 1）。

效果方面，ALFWorld 上平均每次技能调用折叠 5.6 个原始步骤，最多 33 步，技能执行错误率为 0.0%（Table 3，PDF p.8）。

阅读者分析：这相当于把重复出现的查询或操作序列物化为带前置/后置条件的存储过程，适合模式稳定的流程。作者自己也指出，它对开放式文本生成无益（Limitations，PDF p.9）。
