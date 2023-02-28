from twisted.internet import reactor

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from project_parser_m_video.spiders.m_video import MVIDEOSpider


if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()

    runner = CrawlerRunner(settings)
    runner.crawl(HhRuSpider)

    reactor.run()