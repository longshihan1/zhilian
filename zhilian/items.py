# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # mongodb_id = Field()
    bussiessname = Field()
    jobname = Field()
    workaddress = Field()
    money = Field()
    education = Field()
    description = Field()
    releasetime = Field()
    bussiessaddress = Field()
    num = Field()
    bussiessurl = Field()
    pass
