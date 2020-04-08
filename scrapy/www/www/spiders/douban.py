# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://book.douban.com/top250?icn=index-book250-all']
    start_urls = ['http://https://book.douban.com/top250?icn=index-book250-all/']

    def parse(self, response):
        pass
