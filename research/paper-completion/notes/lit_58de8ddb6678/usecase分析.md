# 具体用例

用户问 T4 噬菌体的组成。Encyclopedia bot 返回：“T4 噬菌体……由多种蛋白结构组成，例如头部的 HOC 或衣壳蛋白……尾部有基板……”。节点排序算法在文本中找到 head（第 143 个字符起）、HOC、capsid protein、Tail、baseplate 等节点的首现位置，自底向上更新 minimumIndex，再深度优先遍历场景树，得到 T4–head–HOC–capsid protein–Tail–baseplate 的顺序。

系统先把问题中最深的节点放入时间线；有子节点的节点生成 Overview 场景，叶节点生成 Focus 场景，并让用户从前 2 个候选中选择下一步。用户也可说“Show a bottom view”（Explorer 输出视角参数）、“Show the baseplate”（Pilot 节点导航）或“Show me the interior objects”（剖切面）。

依据：[arXiv:2304.04083v2，21 页](https://arxiv.org/abs/2304.04083v2)，§6.3、Figure 5–6、Table 1，pp.9–13。
