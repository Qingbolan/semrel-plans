# 具体用例

| 工作流 | 直接输入 | 数据环境 | 输出 |
|---|---|---|---|
| BioDEX | 药物不良反应医学报告 | 反应标签检索库 | ranked reaction labels |
| CUAD | 合同全文 | 41类条款定义；评测时有专家span labels | 各类别对应的合同span |
| MMQA | 问题表 | image/text/table三种数据集合 | 答案列表 |

BioDEX计划是map提取反应、top-k召回标签、map重排（图4）。CUAD逻辑上是一个map提取41 fields，物理上可用多个提议模型再合并。MMQA先为三种模态生成search strings，分别semantic join相关内容，再按question分组汇合回答（图5）。

评测输入与辅助标签不能混淆：gold labels用于评分，MedDRA样式候选反应标签用于检索任务；两者用途不同。图1中的研究论文检索是说明性示例，不是第四个评测数据集。

来源：[Abacus: A Cost-Based Optimizer for Semantic Operator Systems](https://arxiv.org/abs/2505.14661v3)。
