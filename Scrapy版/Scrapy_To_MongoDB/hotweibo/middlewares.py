# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class HotweiboSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        """
        Create a new : class from a crawler.

        Args:
            cls: (todo): write your description
            crawler: (todo): write your description
        """
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Processes a response.

        Args:
            self: (todo): write your description
            response: (todo): write your description
            spider: (todo): write your description
        """
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        """
        Yield the response.

        Args:
            self: (todo): write your description
            response: (todo): write your description
            result: (todo): write your description
            spider: (todo): write your description
        """
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        : parameter response : param response

        Args:
            self: (todo): write your description
            response: (todo): write your description
            exception: (todo): write your description
            spider: (todo): write your description
        """
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        """
        Yield all requests.

        Args:
            self: (todo): write your description
            start_requests: (todo): write your description
            spider: (str): write your description
        """
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        """
        Spider the spider.

        Args:
            self: (todo): write your description
            spider: (todo): write your description
        """
        spider.logger.info('Spider opened: %s' % spider.name)


class HotweiboDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        """
        Create a new : class from a crawler.

        Args:
            cls: (todo): write your description
            crawler: (todo): write your description
        """
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        Process the request.

        Args:
            self: (str): write your description
            request: (todo): write your description
            spider: (str): write your description
        """
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        """
        Process the response.

        Args:
            self: (todo): write your description
            request: (todo): write your description
            response: (todo): write your description
            spider: (str): write your description
        """
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        """
        Handles the exception.

        Args:
            self: (todo): write your description
            request: (todo): write your description
            exception: (todo): write your description
            spider: (todo): write your description
        """
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        """
        Spider the spider.

        Args:
            self: (todo): write your description
            spider: (todo): write your description
        """
        spider.logger.info('Spider opened: %s' % spider.name)
