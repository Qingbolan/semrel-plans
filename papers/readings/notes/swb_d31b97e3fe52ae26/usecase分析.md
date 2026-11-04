# usecase

对抗样本生成例（Fig.2b）：原始 VQA 样本"这双手拿着汉堡吗？——否"（原图中的"汉堡"其实不是真汉堡）。MLLM 先理解图像与问题，生成结构化编辑指令（区域、物体类型、参照），如"编辑图像，使双手拿着一个真汉堡"，再由 GPT-4o 编辑得到答案为"是"的对抗图像。两张图外观相近、答案相反，模型若靠常识或表面感知作答，至多答对一张。

定性例（Fig.4b）：QVQ 先识别关键视觉线索"一只手拿着杯子，但似乎是屏幕前另一个人的手，而不是 Thor 的"，再用"Just to make sure""Wait a minute"等自我反驳后给出答案。Fig.3 中，即便答案正确，模型也可能漏掉"远处车辆暗示真实地面"这类关键线索，因而 CoT-Score 只得 1/2。

依据：[NeurIPS 2025 D&B 论文集 PDF，20 页](https://proceedings.neurips.cc/paper_files/paper/2025/file/2b76873e897f3de3069b2f360c65e0c2-Paper-Datasets_and_Benchmarks_Track.pdf)，§3.2（p.5）、§4.2–4.3、Fig.3–4（pp.6–8）。
