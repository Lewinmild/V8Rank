# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


class V8RankPipeline:
    def __init__(self):
        # 写入json 备份
        self.file = open('v8rank.json', 'w')
        # 关键词列表
        self.taffy = ["塔菲", "taffy"]
        self.xing_tong = ["星瞳", "小星星", "瞳友"]
        self.nanami = ["七海", "海子姐", "脆鲨"]
        self.ruru = ["lulu", "ruru", "撸撸", "拉夫"]
        self.san_jie = ["3姐", "三姐", "🦶", "啵啵"]
        self.asoul = ["asoul", "啊楚", "a➗", "a/"]

    def process_item(self, item, spider):
        # 强转字典
        item = dict(item)
        # 标题与正文合并
        item['title'].join(item['body'])

        # 计数 塔菲
        for keyword in self.taffy:
            if keyword in item['title']:
                Statistics.mention_taffy()
        Statistics.plus_taffy()

        # 计数 星瞳
        for keyword in self.xing_tong:
            if keyword in item['title']:
                Statistics.mention_xing_tong()
        Statistics.plus_xing_tong()

        # 计数 七海
        for keyword in self.nanami:
            if keyword in item['title']:
                Statistics.mention_nanami()
        Statistics.plus_nanami()

        # 计数 るる
        for keyword in self.ruru:
            if keyword in item['title']:
                Statistics.mention_ruru()
        Statistics.plus_ruru()

        # 计数 3
        for keyword in self.san_jie:
            if keyword in item['title']:
                Statistics.mention_san_jie()
        Statistics.plus_san_jie()

        # 计数 asoul
        for keyword in self.asoul:
            if keyword in item['title']:
                Statistics.mention_asoul()
        Statistics.plus_asoul()

        # 字典数据序列化
        json_data = json.dumps(item) + ',\n'
        # 写入文件
        self.file.write(json_data)
        # 使用完将数据返回引擎
        return item

    def __del__(self):
        Statistics.show_result()
        self.file.close()


class Statistics:
    isMention = {"塔菲": 0, "星瞳": 0, "七海": 0, "るる": 0, "3": 0, "asoul": 0}
    result = {"塔菲": 0, "星瞳": 0, "七海": 0, "るる": 0, "3": 0, "asoul": 0}

    @classmethod
    def mention_taffy(cls):
        cls.isMention['塔菲'] += 1

    @classmethod
    def plus_taffy(cls):
        if cls.isMention['塔菲'] > 0:
            cls.result['塔菲'] += 1
            cls.isMention['塔菲'] = 0

    @classmethod
    def mention_xing_tong(cls):
        cls.isMention['星瞳'] += 1

    @classmethod
    def plus_xing_tong(cls):
        if cls.isMention['星瞳'] > 0:
            cls.result['星瞳'] += 1
            cls.isMention['星瞳'] = 0

    @classmethod
    def mention_nanami(cls):
        cls.isMention['七海'] += 1

    @classmethod
    def plus_nanami(cls):
        if cls.isMention['七海'] > 0:
            cls.result['七海'] += 1
            cls.isMention['七海'] = 0

    @classmethod
    def mention_ruru(cls):
        cls.isMention['るる'] += 1

    @classmethod
    def plus_ruru(cls):
        if cls.isMention['るる'] > 0:
            cls.result['るる'] += 1
            cls.isMention['るる'] = 0

    @classmethod
    def mention_san_jie(cls):
        cls.isMention['3'] += 1

    @classmethod
    def plus_san_jie(cls):
        if cls.isMention['3'] > 0:
            cls.result['3'] += 1
            cls.isMention['3'] = 0

    @classmethod
    def mention_asoul(cls):
        cls.isMention['asoul'] += 1

    @classmethod
    def plus_asoul(cls):
        if cls.isMention['asoul'] > 0:
            cls.result['asoul'] += 1
            cls.isMention['asoul'] = 0

    @classmethod
    def show_result(cls):
        print(cls.result)
