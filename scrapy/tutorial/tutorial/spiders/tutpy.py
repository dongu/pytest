# -*- coding: utf-8 -*-
import scrapy


class TutpySpider(scrapy.Spider):
    name = "tutpy"
    allowed_domains = ["http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"]
    start_urls = (
        'http://www.http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/',
    )

    def parse(self, response):
        pass
