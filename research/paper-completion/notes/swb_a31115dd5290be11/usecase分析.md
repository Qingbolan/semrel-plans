# 具体用例

附录 A（p.9）给出一条规范化后的工单短文本：“engine oil blender running constantly”。

标注结果：

- engine → PhysicalObject/DrivingObject/CombustionEngine
- oil blender → PhysicalObject/MatterProcessingObject/MixingObject
- blender（嵌套）→ 同为 MixingObject
- running constantly → Process/UndesirableProcess
- 关系（按实体下标 head/tail 解读）：engine hasPart oil blender；running constantly hasPatient oil blender；oil blender isA blender

可见一条 5 个 token 的文本同时含嵌套实体、部件关系、异常过程及其受事。

§1 的例子“replace the blown air conditioner motor”说明期望的事实：空调含 motor 部件、motor 是 replace 的对象、motor 状态为 blown（p.1）。

阅读者分析：在维修分析场景中，这些三元组可用于汇总某类设备的故障过程或活动频次。论文只提到故障分析、根因调查和分类体系抽取等潜在用途，没有评测任何下游分析任务。

依据：§1、附录 A，PDF pp.1、9。
