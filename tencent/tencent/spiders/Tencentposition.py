# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类，用来提出符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 倒入CrawlSpider类和Rule
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem

class TencentpositionSpider(CrawlSpider):
    name = 'Tencentposition'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0&a']

    # Response里链接的提出规则，返回的符合规则的链接匹配对象的列表
    pagelink = LinkExtractor(allow=("start=\d"))

    rules = (
        # 获取这个元组合或者列表中的链接，依次发送请求，并且积雪跟进，调用指定的回调函数处理
        Rule(pagelink, callback='parseTencent', follow=True),
    )

    def parseTencent(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionLink'] = each.xpath("./td[1]/a/@href").extract()[0]
            item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
            item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
            item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item