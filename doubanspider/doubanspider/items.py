# -*- coding: utf-8 -*-
"""
@author:Greepex
"""
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class DoubanspiderItem(Item):
    name=Field()#电影名
    year=Field()#上映年份
    score=Field()#豆瓣分数
    director=Field()#导演
    classification=Field()#分类
    actor=Field()#演员
    how_many_people = Field()#多少人评价
    five_score = Field()#五星多少人
    four_score = Field()  # 四星多少人
    three_score = Field() #三星多少人
    two_score = Field() #两星多少人
    one_score = Field() #一星多少人
    link = Field()
