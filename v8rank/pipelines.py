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
        self.taffy = ["塔菲", "taffy", "黑桃影", "tcg", "大菲住"]
        self.xing_tong = ["星瞳", "小星星", "瞳友", "瞳/", "瞳楚", "瞳子", "瞳u", "瞳子", "瞳瞳"]
        self.nanami = ["七海", "海子姐", "脆鲨", "010", "杰尼", "公海", "海海"]
        self.ruru = ["lulu", "ruru", "撸撸", "拉夫", "雫露露"]
        self.san_jie = ["3姐", "三姐", "🦶", "啵啵", "3/", "3u", "律师"]
        self.asoul = ["asoul", "阿楚", "a楚", "a➗", "a/", "ac", "图a", "as"]
        self.jia_ran = ["嘉然", "然然", "+➗", "+/"]
        self.han_jian = ["东雪莲", "罕见"]
        self.an_ke = ["安可", "红毛", "鹦鹉"]
        self.eoe = ["eoe", "ec", "e➗", "e/", "EOE"]
        self.mao_lei = ["猫雷", "陪酒"]
        self.a_zi = ["阿梓", "孝孩梓"]
        self.nai_lv = ["奶绿", "文静", "奶学长"]
        self.xiang_wan = ["向晚", "晚子", "顶碗"]
        self.lu_zao = ["露早"]
        self.kino = ["kino", "吉诺儿", "KINO"]
        self.bing_tang = ["冰糖", "冰子"]

        self.keywords = {
            '塔菲': self.taffy,
            '星瞳': self.xing_tong,
            '七海': self.nanami,
            'るる': self.ruru,
            '3': self.san_jie,
            'asoul': self.asoul,
            '嘉然': self.jia_ran,
            '东雪莲': self.han_jian,
            '安可': self.an_ke,
            'eoe': self.eoe,
            '猫雷': self.mao_lei,
            '阿梓': self.a_zi,
            '奶绿': self.nai_lv,
            '向晚': self.xiang_wan,
            '露早': self.lu_zao,
            '吉诺儿': self.kino,
            '冰糖': self.bing_tang
        }

    def process_item(self, item, spider):
        # 强转字典
        item = dict(item)
        print(item)
        # 标题与正文合并
        item['title'].join(item['body'])

        for name in self.keywords:
            for keyword in self.keywords[name]:
                if keyword in item['title']:
                    Statistics.mention(name)
                Statistics.plus(name)
            for keyword in self.keywords[name]:
                for comment in item['comments']:
                    if keyword in comment:
                        Statistics.mention(name)
                    Statistics.plus(name)

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

    isMention = {"塔菲": 0, "星瞳": 0, "七海": 0, "るる": 0, "3": 0,
                   "asoul": 0, "嘉然": 0, "东雪莲": 0, "安可": 0, "eoe": 0,
                   "猫雷": 0, "阿梓": 0, "奶绿": 0, "向晚": 0, "露早": 0,
                   "吉诺儿": 0, "冰糖": 0}

    result = {"塔菲": 0, "星瞳": 0, "七海": 0, "るる": 0, "3": 0,
                   "asoul": 0, "嘉然": 0, "东雪莲": 0, "安可": 0, "eoe": 0,
                   "猫雷": 0, "阿梓": 0, "奶绿": 0, "向晚": 0, "露早": 0,
                   "吉诺儿": 0, "冰糖": 0}

    @classmethod
    def mention(cls, v_name):
        cls.isMention[v_name] += 1

    @classmethod
    def plus(cls, v_name):
        if cls.isMention[v_name] > 0:
            cls.result[v_name] += 1
            cls.isMention[v_name] = 0

    @classmethod
    def show_result(cls):
        print(cls.result)
