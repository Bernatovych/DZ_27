from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scraper.spiders.quotes_spider import QuotesSpider


process = CrawlerProcess(get_project_settings())
process.crawl(QuotesSpider)
process.start()
