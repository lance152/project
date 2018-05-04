# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem 


class DouyuSpider(scrapy.Spider):
    name = 'Douyu'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0
    base = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [base+str(offset)]

    def parse(self, response):
    	data_list = json.loads(response.body)['data']
    	if len(data_list)==0:
    		return
    		
    	for data in data_list:
    		item = DouyuItem()
    		item['name']=data['nickname']
    		item['img_link']=data['vertical_src']

    		yield item

    	self.offset += 20
    	yield scrapy.Request(self.base+str(self.offset),callback=self.parse)


    		