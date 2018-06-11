# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#aandroid",
        "http://www.itcast.cn/channel/teacher.shtml#ac",
        "http://www.itcast.cn/channel/teacher.shtml#acloud",
        "http://www.itcast.cn/channel/teacher.shtml#aios",
        "http://www.itcast.cn/channel/teacher.shtml#ajavaee",
        "http://www.itcast.cn/channel/teacher.shtml#anetmarket",
        "http://www.itcast.cn/channel/teacher.shtml#aphp",
        "http://www.itcast.cn/channel/teacher.shtml#apython",
        "http://www.itcast.cn/channel/teacher.shtml#astack",
        "http://www.itcast.cn/channel/teacher.shtml#aui",
        "http://www.itcast.cn/channel/teacher.shtml#aweb",
    ]

    def parse(self, response):
        # with open("teacher.html", "w") as f:
        #     f.write(response.body)
        # 通过scrapy自带的xpath匹配出所有老师的根节点列表信息集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 所有老师信息的列表集合
        teacherIten = []

        # 遍历根节点集合
        for each in teacher_list:

            # Item对象用来保存数据的
            item = ItcastItem()
            # name, extract()将匹配出来的结果转换为Unicode字符串
            # 不加extract() 结果为xpath对象
            name = each.xpath('./h3/text()').extract()
            # level
            level = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()
            # print name[0], level[0], info[0]
            item["name"] = name[0]
            item["level"] = level[0]
            item["info"] = info[0]

            #将结果返回给pipelines
            yield item

            # teacherIten.append(item)



