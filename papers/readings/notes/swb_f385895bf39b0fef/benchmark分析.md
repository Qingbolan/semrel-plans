# 评测与边界

**被测模型**：Google Perspective API（阈值 0.5，记 P；阈值 0.7，记 P\*）、OpenAI Moderation API（O）、Facebook 微调 RoBERTa（F）、CardiffNLP 微调 RoBERTa（C）；后两者是 HuggingFace 上下载量前二的仇恨检测模型（§4.1，PDF p.6）。

**实验 1（分层失败率，Table 3）**：

| 层级 | 仇恨失败率 F/C/P/P\*/O | 非仇恨失败率 F/C/P/P\*/O |
|---|---|---|
| Tier 1 | .40/.38/.35/.62/.22 | .52/.39/.65/.43/.31 |
| Tier 2 | .34/.37/.34/.60/.30 | .69/.40/.74/.55/.24 |
| Tier 3 | .63/.57/.66/.90/.50 | .39/.33/.54/.35/.27 |
| Tier 4 | .61/.53/.49/.72/.46 | .40/.36/.50/.39/.17 |

层级越严重，仇恨失败率越低、非仇恨失败率越高，说明模型优先处理严重政策。全部样本平均失败率：OpenAI 0.29（std 0.17），Perspective 0.38，CardiffNLP 0.40，Facebook 0.40（§4.2，PDF pp.7–8）。

**实验 2（微调，Table 4，失败率）**：

| 测试集 | CardiffNLP | +HM | +HM\*（平衡） | OpenAI |
|---|---|---|---|---|
| HateCheck 总体 | .365 | .199† | .235† | .011 |
| HateModerate 测试总体 | .423 | .275† | .295† | .365 |
| hatEval 总体 | .485 | .485 | .478† | .363 |
| HateXplain 总体 | .221 | .201† | .208† | .299 |

† 表示配对 t 检验 p<0.05。+HM 在部分子集上更差：HateCheck 非仇恨从 .205 升到 .229†，HTPO 仇恨从 .526 升到 .661†（PDF p.8）。

**实验 3（新增样本的贡献，Table 5）**：CardiffNLP+DynaHate（Pipeline 1）与再加 HateModerate 中非 DynaHate 样本（Pipeline 2）相比，HM-All 失败率从 0.191 降到 0.102，HC-All 从 0.097 降到 0.066，均显著（PDF p.9）。

**实验 4（偏差）**：21 个非仇恨、13 个仇恨模板句上，非仇恨预测几乎全对，仇恨预测约 15% 出错；HateCheck 非仇恨样本上 CardiffNLP 与 +HM、+HM\* 的配对 t 检验 p=0.80/0.83（§4.4，PDF p.9）。

**边界**：政策固定为 2022-11-23 版，换平台需重新标注；41 条政策不覆盖全部仇恨言论；按准则关键词检索可能偏向显式词汇，隐式仇恨较少（§6，PDF p.10）。阅读者分析：OpenAI 在 HateModerate 测试上不如 +HM，但在 HateCheck 上远好于 +HM（.011 对 .199），"超过 OpenAI"只在自家测试集上成立；RQ4 的统计推理不成立（见贡献与评价）。

依据：[Findings of NAACL 2024，pp.2691–2710](https://aclanthology.org/2024.findings-naacl.172)，§4.1–4.4、Tables 3–5、§6，PDF pp.6–10。
