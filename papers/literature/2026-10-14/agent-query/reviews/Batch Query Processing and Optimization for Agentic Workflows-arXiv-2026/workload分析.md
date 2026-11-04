# 工作负载、数据环境和批量

表3有六个合成workflow，节点数按GPU/CPU列出：IMDb-Diamond8/9、IMDb-TripleChain10/3、FineWiki-LongChain9/6、FineWiki-Bridge9/3、TPCH-Trident7/9、TPCH-Fanout9/12。

数据环境是PostgreSQL中的三个数据库：FineWiki精选20000条英文page及metadata/raw wikitext，主键/title上B-tree索引；IMDb规范化后超过2亿行，包含电影、人物、演职员多对多关系及外键索引；TPC-H SF10，标准8张关系表、数千万tuple。TPC-H工具查询由Q1–Q22模板按上下文实例化。

每次输入由workflow YAML、model/system prompt/父节点/SQL/API配置和一批用户query组成。数据库是query可查询的环境数据，用户query批次不是2万篇页面本身。正文未列每条query完整原文和全部参数，不能凭workflow名称生成所谓原始JSON。

§6.2主batch=1024 query；§6.3 scheduler比较N=256；规模测试256–2048。图10另有Processor batch size（每次处理的LLM或SQL请求数），分别在总负载256和1024下扫描；与模型引擎continuous batching仍为不同层次。在线模式用持续异步输入队列。
