# -*- coding: utf-8 -*-
"""
@author:Greepex
"""
from scrapy.spider import Spider
from scrapy.selector import Selector
from doubanspider.items import DoubanspiderItem
from scrapy import Request
class DoubanSpider(Spider):
    name = "DBug"
    allowed_domains=["movie.douban.com"]
    urls = []
    for i in range(1988, 2017):
        for j in range(0, 300):
            urls.append("https://movie.douban.com/tag/%d?start=%d&type=T" % (i, j*20))
    start_urls = urls
    download_delay = 5

    def parse(self, response):
        sel = Selector(response)
        item=DoubanspiderItem()
        for i in range(1, 21):
            for item_url in sel.xpath('//*[@id="content"]/div/div[1]/div[2]/table[%d]/tr/td[2]/div/a/@href' % i).extract():
                item['link'] = item_url
                print item_url
                yield Request(url=item_url, meta={'item': item}, callback=self.parse_item, dont_filter=True)

    def parse_item(self, response):
        item = response.meta['item']
        sel=Selector(response)
        item['name'] =sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0]
        item['year']=sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')[0]
        item['classification']=sel.xpath('//span[@property="v:genre"]/text()').extract()
        item['director']=sel.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()[0]
        item['score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()[0]
        item['how_many_people']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()').extract()[0]
        item['five_score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[1]/span[2]/text()').extract()[0]
        item['four_score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[2]/span[2]/text()').extract()[0]
        item['three_score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[3]/span[2]/text()').extract()[0]
        item['two_score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[4]/span[2]/text()').extract()[0]
        item['one_score']=sel.xpath('//*[@id="interest_sectl"]/div[1]/div[3]/div[5]/span[2]/text()').extract()[0]
        item['actor']=sel.xpath('//*[@id="info"]/span[3]/span[2]/a/text()').extract()
        return item

    # def parse(self, response):
    #     item = DoubanspiderItem()
    #     soup = BeautifulSoup(response.body, "lxml")
    #     # item['name'] = nameyear[0]
    #     # item['year'] = nameyear[1]
    #     # print item['name']
    #     # print item['year']
    #     return item
