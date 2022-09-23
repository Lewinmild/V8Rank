import re

import scrapy

from v8rank.items import V8RankItem


class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=v']

    def parse(self, response):
        # post_list = response.text
        resp = response.text
        # print(resp)
        # 标题
        re_info = re.compile(r'class="j_th_tit ">(?P<title>.*?)<.*?class="tb_icon_author ".*?title="主题作者: ('
                              r'?P<author>.*?)".*?title="创建时间">(?P<time>.*?)<.*?class="threadlist_abs '
                              r'threadlist_abs_onlyline ">(?P<body>.*?)<', re.S)
        info = re_info.finditer(resp)
        for it in info:
            # 标题
            title = it.group('title').strip()
            # 发帖人
            author = it.group('author').strip()
            # 内容
            body = it.group('body').strip()
            # 时间
            time = it.group('time').strip()

            # print(title)
            # print(author)
            # print(body)
            # print(time)

            v8rank = V8RankItem()
            v8rank['title'] = title
            v8rank['author'] = author
            v8rank['body'] = body
            v8rank['time'] = time
            # print(v8rank)
            yield v8rank

        # 翻页
        for i in range(1, 10):
            part_url = 'https://tieba.baidu.com/f?kw=v&ie=utf-8&pn=' + str(50*i)
            next_url = response.urljoin(part_url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )

