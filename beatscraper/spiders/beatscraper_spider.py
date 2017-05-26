from scrapy import Spider
from scrapy.selector import Selector
from beatscraper.items import BeatScraperItem

class BeatScraper(Spider):
    name = "beatscraper"
    allowed_domains = ["beatport.com"]
    start_urls = [
        "https://www.beatport.com/genre/tech-house/11/top-100"
    ]

    def parse(self, response):
        song = Selector(response).xpath('//div[@id="pjax-inner-wrapper"]/section/main/div/div[2]/ul')

        for song in songs:
            item = BeatScraperItem()
            item['title'] = song.xpath(
                './li/div[3]/p[1]/a/span[1]/text()')[0].extract()
            item['artist'] = song.xpath(
                './li/div[3]/p[2]/a/text()')[0].extract()
            item['label'] = song.xpath(
                './li/div[3]/p[4]/a/text()')[0].extract()
            item['releaseDate'] = song.xpath(
                './li/div[3]/p[6]/text()')[0].extract()
            item['position'] = song.xpath(
                './li/div[2]/text()')[0].extract()
            item['url'] = song.xpath(
                './li/div[3]/p[1]/a/@href')[0].extract()
            yield item
