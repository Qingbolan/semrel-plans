# 具体用例

论文 Figure 1 给出 AnCora-Verb-Esp 中动词 mejorar（“改善”）义项 01 的词条（§2.2，p.7）：

| 语义类 | 句法功能 → 论元-题元 | 例句 |
|---|---|---|
| LSS1.1（A1，及物-致使） | SUJ → Arg0-CAU；CD → Arg1-TEM；CC → ArgM-TMP/ADV | “obligará a mejorar la calidad del ataque” |
| LSS2.2（B2，非宾格-状态，反致使） | SUJ → Arg1-TEM；CC → ArgM-ADV/FIN | “las técnicas de diseminación han mejorado mucho” |

标注流程中，树库里 mejorar 作及物用法时，规则先把主语标为 Arg0-CAU、直接宾语标为 Arg1-TEM；若是被动（带 PASS 语素），主语改标 Arg1-PAT 一类（§2.1.3 规则 a，p.6）。多义动词只自动填入无歧义部分，其余人工补全。

阅读者分析：对语义查询而言，这类标注可支持“找出所有以 X 为受事（Arg1）的改善事件”，并区分“谁致使改善”和“什么自己变好”。这是项目派生用法，论文本身只描述资源，没有评测此类查询。

依据：§2.1.3、§2.2、§5.1，Figure 1，PDF pp.6–7、26–31。
