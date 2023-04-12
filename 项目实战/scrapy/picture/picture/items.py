# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PictureItem(scrapy.Item):
    # define the fields for your item here like:
    picture_url = scrapy.Field()
    picture_name=scrapy.Field()
    page_file=scrapy.Field()
