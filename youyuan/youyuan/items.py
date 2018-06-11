# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouyuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    age = scrapy.Field()
    header_url = scrapy.Field()
    images_url = scrapy.Field()
    content = scrapy.Field()
    place_from = scrapy.Field()
    education = scrapy.Field()
    hobby = scrapy.Field()
    # 个人主页
    source_url = scrapy.Field()
    # 数据来源网站
    source = scrapy.Field()
    # pass
