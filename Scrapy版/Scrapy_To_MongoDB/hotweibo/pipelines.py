# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import datetime


class MongoPipeline:

    def __init__(self, mongo_uri, mongo_db):
        """
        Initialize mongo database.

        Args:
            self: (todo): write your description
            mongo_uri: (str): write your description
            mongo_db: (todo): write your description
        """
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        """
        Creates an : class instance.

        Args:
            cls: (todo): write your description
            crawler: (todo): write your description
        """
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        """
        Open spider connection.

        Args:
            self: (todo): write your description
            spider: (todo): write your description
        """
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        """
        Close the spider connection.

        Args:
            self: (todo): write your description
            spider: (todo): write your description
        """
        self.client.close()

    def process_item(self, item, spider):
        """
        Process a single item.

        Args:
            self: (todo): write your description
            item: (todo): write your description
            spider: (todo): write your description
        """
        self.db[str(datetime.date.today())].update({'timestamp': item['timestamp']}, {'$set': item}, True)
        return item
