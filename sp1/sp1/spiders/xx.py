# -*- coding: utf-8 -*-
import scrapy


class XxSpider(scrapy.Spider):
    name = 'xx'
    allowed_domains = ['xx.com']
    start_urls = ['http://xx.com/']

    def parse(self, response):
        pass
