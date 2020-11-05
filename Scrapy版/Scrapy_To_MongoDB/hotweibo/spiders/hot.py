# -*- coding: utf-8 -*-
import scrapy
import time
from ..items import HotItem


class HotSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/top/summary?cate=realtimehot']

    def parse(self, response):
        """
        Parse the response.

        Args:
            self: (str): write your description
            response: (todo): write your description
        """
        titles = response.xpath('//div[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/a/text()').getall()
        stars = response.xpath('//div[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]/span/text()').getall()
        # 置顶微博的star数目为-1
        stars.insert(0, '-1')
        item = HotItem()
        item['top'] = []
        item['timestamp'] = time.time()
        for k, v in zip(titles, stars):
            item['top'].append({'title': k, 'star': v})
        yield item
