# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ItcastPipeline(object):
    # __init__方法是可选的， 作为类初始化的方法
    def __init__(self):
        # 创建一个文件
        self.filename = open("teacher.json", "w")

    # process_item方法是必须要写的， 用来处理item的数据
    def process_item(self, item, spider):
        # 将item的python数据转化为json的数据
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        # return 是必须要的
        return item

    # close_spider()方法是可选的， 结束时调用这个方法
    def close_spider(self, spider):
        self.filename.close()
