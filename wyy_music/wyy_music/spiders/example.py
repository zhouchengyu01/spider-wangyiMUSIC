# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['http://music.163.com/#/discover/playlist/?order=hot']
    start_urls = ['http://http://music.163.com/#/discover/playlist/?order=hot/']

    def parse(self, response):
        pass
