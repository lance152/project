# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
	#主播名
    name = scrapy.Field()
    #图片链接
    img_link = scrapy.Field()