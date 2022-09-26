# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class V8RankItem(scrapy.Item):
    # 贴名
    title = scrapy.Field()
    # 主贴
    body = scrapy.Field()
    # 发帖人
    author = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 链接
    post_id = scrapy.Field()
    # 回复
    comments = scrapy.Field()

