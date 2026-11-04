# 评测与边界

基线为 7 个官方实现：PatchCore、RD、RD++、EfficientAD（S 版）、MSFlow、SimpleNet、DSR；默认用 MVTec AD 论文设置，不做场景级调参，输入一般缩放到 256×256；DSR 因训练太慢，大尺寸只跑了 Rice（§4.1，pp.7–8）。

指标：AU-PRO0.05（主指标）、AU-PRO0.30（补充）、像素级 F1 与图像级 F1（阈值=正常验证图像素均值+3 倍标准差），以及 RTX 2080Ti 上单图推理时间与峰值显存（§4.2，pp.8–9）。

**实验 1（阈值无关，Table 7）**：TESTpriv / TESTpriv,mix 的 AU-PRO0.05 均值。

| 方法 | TESTpriv | TESTpriv,mix |
|---|---|---|
| EfficientAD | 30.8 | 19.2 |
| PatchCore | 28.8 | 26.0 |
| RD++ | 27.1 | 25.2 |
| RD | 26.4 | 25.0 |
| MSFlow | 24.3 | 11.9 |
| SimpleNet | 21.1 | 13.7 |
| DSR | 20.3 | 17.4 |

**实验 2（阈值相关，Table 8）**：像素 F1 最好为 MSFlow 21.8%（TESTpriv）；PatchCore 仅 3.7%，却与他法 AU-PRO 相近，作者据此认为只看阈值无关指标不够（§4.3.2，p.9）。补充 Table 12 的图像级 F1 中 PatchCore 均值仅 8.0%，归因于其按整个输入集归一化异常图（p.14–15）。

**实验 3（输入尺寸）**：Rice 上提高分辨率可让 PatchCore、MSFlow 的 AU-PRO0.05 约翻倍，但时间和显存增加一个数量级以上，PatchCore 每图约 2 秒，SimpleNet 在最大尺寸显存不足（§4.3.3，Fig.6，pp.9–11）；半原始尺寸下 PatchCore 均值升到 62.3%（Table 11，p.15）。

边界：作者承认只测了 7 个方法；阈值估计方法简单；未研究增广能否弥补光照差距；效率测量缺乏标准硬件（p.11）。阅读者分析：私有真值使结果依赖服务器可用性；不同方法的输入缩放规则并不完全一致（RD 需 32 的倍数）。

依据：[arXiv:2503.21622v1，21 页](https://arxiv.org/pdf/2503.21622v1)，§4–5、Tables 7–12，PDF pp.7–11、14–15。
