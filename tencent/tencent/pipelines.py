# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    # __init__()方法是可选的
    def __init__(self):
        # 创建一个文件对象
        self.filename = open("tencent.json", "w")

    # process_tiem（）方法是必须需要的，用来出来item的数据
    def process_item(self, item, spider):
        # 将item的python数据转化为json的数据
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入有中文，需要加入utf-8的编码格式
        self.filename.write(jsontext.encode("utf-8"))
        return item

    # close_spider()方法是可选的
    def close_spider(self, spider):
        self.filename.close()
