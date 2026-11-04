# 具体用例

**用例：从课程到技能入库的一次循环（Figs. 3–6，PDF pp.3–6）**：

1. **课程提出任务**：物品栏中有木镐和若干石头时，GPT-4 推理"应升级为石镐以提高效率"，提出任务"Craft 1 stone pickaxe"；在夜晚且附近有僵尸、已装备石剑和盾牌时，提出"Kill 1 zombie"（Fig. 3）。
2. **检索技能**：针对"Craft Iron Pickaxe"，GPT-3.5 先生成一般性建议（需要 3 个铁锭和 2 根木棍），与环境反馈一起作为查询，检索出 top-5 相关技能，如冶炼铁锭、制作木棍、制作工作台、制作熔炉、制作木镐（Fig. 4）。
3. **生成与修正**：执行程序后得到环境反馈"I cannot make stick because I need: 2 more planks"，或执行错误"No item named acacia_axe"，GPT-4 据此修正，例如改为制作木斧（Fig. 5）。
4. **自我验证**：任务"Craft a spyglass"时，物品栏有 3 个铜锭但没有紫水晶碎片，评审判定失败并给出"Find and mine an amethyst shard underground"（Fig. 6）。
5. 成功后程序（如 `craftStoneShovel()`、`combatZombieWithSword()`）存入技能库（§1）。

**人类反馈变体（§3.5）**：人类可充当评审（提供视觉批评）或课程（拆解建造任务），使 Voyager 建造下界传送门和房屋等 3D 结构。

阅读者分析：对语义算子/数据系统而言，技能库相当于"按自然语言描述嵌入检索的可执行算子目录"，迭代提示则是以执行反馈为信号的程序合成循环。

依据：§1、§2.1–2.3、§3.5，Figs. 3–6、10，PDF pp.2–9。
