import scrapy
from scrapy.http import HtmlResponse
from project_parser_m_video.items import ProjectParserM_videoItem


class MVIDEOSpider(scrapy.Spider):

    name = 'm_video'
    allowed_domains = ['mvideo.ru']
    start_urls = [
        'https://www.mvideo.ru/'
    ]

    def goods_parse(self, response: HtmlResponse):
        goods_name = response.css("alt::text").get()
        goods_price = response.xpath("//span[@class='price__main-value']//text()").getall()
        goods_url = response.url

        yield ProjectParserM_videoItem(
            name=goods_name,
            price=goods_price,
            url=goods_url
        )