from scrapy.item import Item, Field


class BeatScraperItem(Item):
    title = Field()
    artist = Field()
    label = Field()
    releaseDate = Field()
    position = Field()
    url = Field()
