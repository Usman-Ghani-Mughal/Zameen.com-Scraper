# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZameenscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrapy.Field()
    Area = scrapy.Field()
    Price = scrapy.Field()
    Extra_info = scrapy.Field()
    Details = scrapy.Field()
    Link = scrapy.Field()
