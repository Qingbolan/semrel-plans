# 五个Partial的真实输入—环境短引—gold

这是来源审计表，不是模型输入包。gold、研究者选中的证据和私有分析必须与被测系统隔离。所有例子均来自已下载原件，均未证明完整C或Agent优势。

| 数据湖/真实ID | 记录字段（原字段概括） | E短引与位置 | 原gold与对应关系 | 必须保留的限制 |
|---|---|---|---|---|
| HSCodeComp task591 | product_name为20set玻璃管与塞盖；each pack=20；price=8.3375USD | “Valued over $5 each”，HTS2025Rev15的7013.99.90祖先 | 7013999090；gold路径含该件价门槛 | 包价/件价口径未明。短引证明需要哪项事实，不证明门槛满足；不由gold补件价 |
| CodiEsp S1698-44472005000300015-1 | 原病例提及“resonancia magnética nuclear de ambas ATM”，双侧颞下颌关节MRI | “3 Imagen por Resonancia Magnética (RM)”，操作表PDF480/印刷461；同表解剖轴9=双侧颞下颌关节；指南G12.2允许4或7位 | 局部X标注bn39，跨度761–789与797–809；P/X任务须分别评分 | 只解释该操作，非整病例全gold；没有对比剂信息不能擅补七位 |
| UDRP D2024-0001 | public案文的争议域名decathlonag2r.com；投诉方Decathlon | “recognizable in the domain name”，Overview3.0 §1.7正文，讨论商标可识别与混淆相似性 | 正式命令转移域名，派生RELIEF_GRANTED | 只支持第一要件的一部分；还需权利/合法利益与恶意，不由此推导完整救济；原诉状、外部证据未全封存 |
| AnnoCTR train:3782 | 报告PurpleWave：二进制字符串加密，运行时通过解密循环恢复 | “decode or deobfuscate”，冻结mitre_entity.jsonl第515行T1140定义 | 人工链接T1140，行为与恢复混淆信息局部对应 | 固定检索加定义比较也可能足够；一个正确局部链接不证明全报告可答或K |
| STARD query0 | 问题=谁可以成为个体工商户？ | “自然人从事工商业经营”，corpus.jsonl ID705民法典54；另ID49282个体工商户条例2 | match_id=[705,49282]，人工相关法条集合 | 是相关性检索gold，不是个人许可裁定；按冻结库解释，不作为现行法律建议 |

## 逐例出处

- [HS原记录与祖先](../artifact/evidence/shared-environment-audit-20260914-v217/samples.json)，[完整来源卡](shared-environment-strict-audit-hscodecomp.md)。
- [CodiEsp跨度还原与规则](../artifact/evidence/shared-environment-strict-codiesp/mri-rule-path.json)，[来源卡](shared-environment-strict-audit-codiesp.md)。
- UDRP公开输入：`data/shared-environment-audit-20260908-v26/public-v2/cases/case_e10c6ed72502db06d572.txt`；私有决定：`data/shared-environment-audit-20260908-v25/gold-extraction-v2.jsonl`；[来源卡](shared-environment-strict-audit-udrp.md)。
- [AnnoCTR原上下文/定义](../artifact/evidence/shared-environment-audit-20260914-v216/samples.json)，[来源卡](shared-environment-strict-audit-annoctr.md)。
- STARD原文件：`data/shared-environment-strict-stard/repo/data/queries.json`和`corpus.jsonl`；[来源卡](shared-environment-strict-audit-stard.md)。

[短引字面核验与SHA](../artifact/evidence/shared-environment-top-five-quotes.json)只证明短引存在；HS和AnnoCTR引用的是先前从原文件抽取的审计记录，原文件映射见来源卡，不能把衍生收据当独立新gold。UDRP读到的正文页脚为Overview3.0；3.3是被动持有章节号，非版本；当前统一写为Overview 3.0 §3.3。

[Query/DAG/LOTUS与Agent四路推演](shared-environment-current-five.md)与此表同用一套记录；没有将预期结果写成实测输出。
