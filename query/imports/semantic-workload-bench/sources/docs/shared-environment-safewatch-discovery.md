# SafeWatch 初筛与下载状态

官方仓库https://github.com/BillChan226/SafeWatch，固定commit d6cc5648b5a4f3ffd57df28c229857b65bc4c46e。官方HF数据现重定向/迁移至Virtue-AI-HUB/SafeWatch-Bench，revision 08976ba0a25de5393854f70733d848a44993c089；已下载完整元数据。README描述真实与生成视频两个子集、六风险类、多模型共识标注，不能把总2M+当真实人工gold数。元数据中存在分风险benchmark JSON；需下载real子集逐案审查。尚未核验政策长度、20gold或D/E，不计Strong。

论文下载进程会随后获取仓库ZIP；执行session75571在本轮最后一次poll仍live且无输出，目录尚无PDF，不能写作已下载或失败。下一轮先poll该handle，勿仅因等待超时启动重复PDF请求。官方PDF链接https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf 。

本轮另发现KuaiMod官方入口https://kuaimod.github.io/，页面自述真人工短视频benchmark，尚未深入或计入候选。无模型调用。


## 仓库实核：短政策与手动门控

已独立取得完整仓库ZIP 4,856,418 bytes，commit不变，保存repository-audit.zip并解压；未运行作者代码。HF元数据明确gated=manual、private=false；固定revision下real/C1/benign_benchmark.json下载实际401。这是人工批准访问限制，非公开可直接下载；不绕过门控、不用训练生成的描述替代视频gold。

AST读取utility/prompt_template_new.py的字符串常量（不执行模块）：主要video_moderation_prompt_vg_fine_grained_final为4,880字符、664英文词；另有fine_grained版本7,812字符、1,071词。标签/模板数量不能算复杂共享环境或执行家族数量。当前直接证据更接近短政策条件视频分类，不能因2M数据规模判Strong。

论文session75571再次poll仍报告运行，无PDF文件；完整论文下载尚不成立。仓库和政策实核是本轮进展，视频20gold因门控未进行。此路线暂不优先推进；需要官方开放资产与长规则/独立gold证据才能恢复。


后续状态：75571已返回exit1，PDF read timeout，随后DNS失败。该进程已终止，不再称live；独立已下载仓库不受影响。
