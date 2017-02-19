# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

from pymongo import MongoClient
from scrapy import log

from zhilian.settings import MONGO_URI, PROJECT_DIR


class ZhilianPipeline(object):
    def __init__(self, mongo_uri, mongo_db, image_dir):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.image_dir = image_dir
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=MONGO_URI,
            mongo_db='zhilian',
            image_dir=os.path.join(PROJECT_DIR, 'images')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        if not os.path.exists(self.image_dir):
            os.mkdir(self.image_dir)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        person_detail = {
            'bussiessname': item.get('bussiessname', ''),
            'jobname': item.get('jobname', ''),
            'workaddress': item.get('workaddress', ''),
            'money': item.get('money', ''),
            'education': item.get('education', ''),
            'description': item.get('description', ''),
            'releasetime': item.get('releasetime', ''),
            'bussiessaddress': item.get('bussiessaddress', ''),
            'num': item.get('num', ''),
            'bussiessurl': item.get('bussiessurl', ''),

        }
        result = self.db['zhilian'].insert(person_detail)
        item["mongodb_id"] = str(result)
        log.msg("Item %s wrote to MongoDB database %s/person_detail" %
                (result, self.MONGODB_DB),
                level=log.DEBUG, spider=spider)
        return item
