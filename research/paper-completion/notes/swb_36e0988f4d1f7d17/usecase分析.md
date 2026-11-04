# 具体用例

用例：标注者拿到一篇约 30–40 句的俄语短新闻，先切分 EDU，再在 rstWeb 中构建树。

- 若两个 EDU 一个说原因、一个说结果，第一轮手册要求区分 Cause 与 Effect，并进一步区分意愿性/非意愿性。作者发现，判断哪一方更重要（核心）以及行为是否有意都很主观。因此最终集合并为单一 Cause-Effect，且不再区分意愿性（§2.3）。需要细分的用户可在下载的 XML 中自行改写。
- 新闻中引述来源时，原先按来源是否明确区分 Attribution1/Attribution2，最终合并为 Attribution（§2.1、§2.3）。

导出的 XML 中，`<segment id="4" parent="54" relname="span">` 表示 EDU 4 是 54 号组的主核心（§2.2）。

阅读者分析：若本项目要从俄语文本中抽取因果或归属关系，该语料只提供合并后的粗粒度标签，且在本文时点仅有少量公开文本（阅读者分析）。

依据：[Dialogue 2017，12 页](https://dialogue-conf.org/media/3938/pisarevskayadetal.pdf)，§2.1–§2.3，PDF pp.4–9。
