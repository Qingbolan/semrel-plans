# 具体用例

论文 Figure 1 给出噬菌体分离协议“Isolation of temperate phages by plaque agar overlay”，共 9 步。第 6 步“Gently spread the top agar over the agar surface by sliding the plate on the bench surface using a circular motion.” 在 Figure 2–3 中被标为（pp.1–2）：

| 片段 | 标签 | 与动作 spread 的关系 |
|---|---|---|
| spread | Action | – |
| gently | Modifier | Mod-Link |
| top agar | Reagent | Acts-on |
| agar surface | Location | Site |
| sliding | Action | Using |
| plate | Location | sliding 的 Acts-on |
| bench surface | Location | sliding 的 Site |
| circular motion | Method | sliding 的 Using |

阅读者分析：上表关系按 Figure 3 的连线方向整理，提取文本中的图标签有错位，个别边以 PDF 图像为准。由此可得一个小动作图：“用环形滑动的方式把顶层琼脂涂到琼脂表面”。若项目把它用于语义抽取（如“找出所有需要离心机且转速超过 10,000 rpm 的步骤”），需要的是动作、Device、Speed 及其关系；这属于本项目派生任务，论文未评测此类查询。

依据：§1–3，Figures 1–3，PDF pp.1–2。
