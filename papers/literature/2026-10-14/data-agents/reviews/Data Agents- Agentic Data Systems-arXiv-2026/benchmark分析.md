# benchmark分析

[论文原文](https://arxiv.org/html/2609.24137v1)

§6称以Qwen3为骨干、DABstep validated split与Spider 2.0-Lite 547题评测。Table III给出easy94.44%、hard50.79%；Table IV执行准确率44.50%。Table V为2.8对6.5分钟、5.1对7.4分钟；基线分别不同，不能相互混用。Tables VI–VII是按查询类别的token费用证据，非实测batch吞吐。消融支持组件作用，但公开配置、具体Qwen3版本和数据切分仍需代码确认。
