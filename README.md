# V8Rank
基于Scrapy爬取V8数据，制作饼图

适用范围
---
修改网址和关键词列表可用于统计所有贴吧的指定内容

·关键词列表位于 ./v8rank/spiders/pipelines.py 第17行

·统计检测字典位于 ./v8rank/spiders/pipelines.py 第88行

(关键词列表下的关键词字典中，字典的键与统计检测字典中的键保持一致。举例：self.keywords={"塔菲": self.taffy},字典键值对左侧"塔菲"与统计检测字典isMention={"塔菲": 0}中保持一致,右侧即是上面的列表名)
