﻿import scrapy
from scrapy.http import HtmlResponse
from olxparser.items import OlxparserItem
from scrapy.loader import ItemLoader

class OlxkzSpider(scrapy.Spider):
    name = 'olxkz'
    allowed_domains = ['castorama.ru']
    start_urls = ['https://www.castorama.ru/tools/power-tools/cordless-drills-and-screwdrivers']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='next i-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@class='product-card__img-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_ads)



    def products_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=OlxparserItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos', "//div[@class='product-media']//img/@data-src")
        loader.add_xpath('price', "//span[@class='regular-price']/span/span/span/text()")
        loader.add_value('url', response.url)
        yield loader.load_item()