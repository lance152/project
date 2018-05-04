# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from douyu.settings import IMAGES_STORE as imagestore
import shutil


class DouyuPipeline(ImagesPipeline):

	def get_media_requests(self,item,info):
		imglink = item['img_link']
		yield scrapy.Request(imglink)

	def item_completed(self, results, item, info):
		image_path = [x['path'] for ok,x in results if ok]

		os.rename(imagestore+image_path[0],imagestore+item['name']+'.jpg')

	def close_spider(self,spider):
		print("*"*40)
		shutil.rmtree('/Users/FanLance/Documents/Project/douyu/images/full')