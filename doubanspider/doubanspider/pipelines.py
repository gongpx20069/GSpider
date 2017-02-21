# -*- coding: utf-8 -*-
"""
@author:Greepex
"""
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
class DoubanspiderPipeline(object):
    def __init__(self):
        connection = MongoClient("localhost", 27017)
        db = connection["movies"] # you need no build database named testdouban
        # db.authenticate(name = "root", password = "fireling") # no name and password for localhost
        self.posts = db["result"] # you need not build collection named book
    # pipeline default function
    def process_item(self, item, spider):
        self.posts.insert(dict(item)) # convert json to dict
        return item
        #     def process_item(self, item, spider):
#         dbObject = dbHandle()
#         cursor = dbObject.cursor()
#
#         sql = 'insert into test(name,year,classification,director,score) values (%s,%s,%s,%s,%s)'
#         try:
#             cursor.execute(sql,(item['name'],item['year'],item['classification'],item['director'],item['score']))
#             dbObject.commit()
#         except Exception,e:
#             print e
#             dbObject.rollback()
#         return item
#
# def dbHandle():
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         passwd='12zx',
#         charset='utf8',
#         use_unicode=False,
#         db='test'
#
#     )
#     return conn