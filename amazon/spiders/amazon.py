# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = [
        'https://www.amazon.com/s/ref=lp_3760911_nr_p_85_0?fst=as%3Aoff&rh=n%3A3760911%2Cp_85%3A2470955011&bbn=3760911&ie=UTF8&qid=1540481287&rnid=2470954011',
    ]

    def parse(self, response):
        for asin in response.xpath("//ul[@id='s-results-list-atf']/li/@data-asin").extract():
            yield scrapy.Request(response.urljoin("http://www.amazon.com/dp/"+asin), callback=self.parse_product_page)

    def parse_product_page(self, response):
        item = {}
        item['title'] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        item['asin'] = response.xpath("//input[@id='ASIN']/@value").extract_first()
        yield item
