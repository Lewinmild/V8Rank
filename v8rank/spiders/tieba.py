import re

import scrapy

from v8rank.items import V8RankItem


class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=v']

    def parse(self, response):
        # 定义模式 (0为只计算主题页, 1为计算前5楼)
        mode = 0
        # 统计页数 (默认1页，不能小于1)
        page = 5

        # post_list = response.text
        resp = response.text
        # print(resp)
        # 标题
        re_info = re.compile(r'href="/p/(?P<post_id>.*?)".*?'
                             r'class="j_th_tit ">(?P<title>.*?)<'
                             r'.*?class="tb_icon_author ".*?title="主题作者: '
                             r'(?P<author>.*?)".*?title="创建时间">(?P<time>.*?)'
                             r'<.*?class="threadlist_abs '
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
            # 连接
            post_id = it.group('post_id').strip()

            # print(title)
            # print(author)
            # print(body)
            # print(time)

            v8rank = V8RankItem()
            v8rank['title'] = title
            v8rank['author'] = author
            v8rank['body'] = body
            v8rank['time'] = time
            v8rank['post_id'] = post_id

            # print(v8rank)

            # 模式
            # while mode == 0:
            # yield v8rank
            yield scrapy.Request(
                    url="https://tieba.baidu.com/p/" + v8rank['post_id'],
                    callback=self.parse_detail,
                    meta={'v8rank': v8rank}
                )

        # 翻页
        for i in range(1, page):
            part_url = 'https://tieba.baidu.com/f?kw=v&ie=utf-8&pn=' + str(50 * i)
            next_url = response.urljoin(part_url)
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )

    # 详情页处理
    def parse_detail(self, response):
        v8rank = response.meta['v8rank']
        # print(v8rank)
        resp = response.text
        print("======================")
        # print(resp)
        re_detail = re.compile(r'j_d_post_content.*?>(?P<comment>.*?)</div', re.S)
                               # r'data-gift=\{"userId":"(?P<userid>.*?)"'
                               # r'"userName":"(?P<username>.*?)".*?'
                               # r'IP属地:(?P<addr>.*?)<', re.S)
        info = re_detail.finditer(resp)
        comments = []
        for it in info:
            # 标题
            comment = it.group('comment').strip()
            # 去除图片
            comment = re.sub(r'\<.*\>', '', comment)
            # 用户id
            # userid = it.group('userid')
            # 用户名
            # username = it.group('username')
            # 地址
            # addr = it.group('addr')

            # user_info = [comment, userid, username, addr]
            # user_info = [comment, userid]

            # print(user_info)
            comments.append(comment)

        v8rank['comments'] = comments
        yield v8rank
        # v8rank['comments'] = comments
