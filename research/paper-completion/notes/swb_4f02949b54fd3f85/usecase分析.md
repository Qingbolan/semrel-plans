# 具体用例

**用例（原文 §4.2 与 Figure 2 的判定过程）**：候选 `conseil régional`（“地区议会”）在两个句子中出现。

- 句 (1) “Le conseil régional est l’assemblée délibérante d’une région.” 为泛指，没有特指实体，因此不是 NE；它是多词，进入非动词 MWE 规范检验。
- 句 (2) “Le conseil régional a délibéré hier soir.” 特指某个议会，但命名约定覆盖整个概念（可凭属性指称别的地区议会），所以仍不是 NE，转入非动词 MWE 判定。

相比之下，`[Anna Duval]PERS` 的命名约定只连到具体的人；`[Journal officiel de la [République française]ORG]PROD` 指唯一实体且属于产品类，因此走 NE 规范（§4.2，pp.436–437）。

**转喻**：`chauffeur-routier chez [Caillaud]` 中 Caillaud 原为人名，在此指公司，同时标原始类别 PERS 和最终类别 ORG（§5.1，p.437）。

这一用例说明 NE/MWE 的判定依赖上下文和命名约定，而不只是表面形式。若把它作为文本抽取或实体识别的工作负载，同一字符串在不同句子里可能有不同标签，且标签包含嵌套与不连续片段。论文没有给出自动系统在这些情形上的表现（阅读者分析）。

依据：[JLM 8(2) 2020, pp.415–479，65 页](https://jlm.ipipan.waw.pl/index.php/JLM/article/download/265/249/2149)，§3.2、§4.2、§5.1、Figure 2，期刊 pp.428–438。
