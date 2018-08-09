# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

class BugPipeline(object):
	def open_spider(self, spider):
		self.file = open("output.jl", 'w+')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		#merge same domains
		############################
		domain = item['url'][0].split('/')[2]
		print("============" + domain)
		find = 0
		self.file.seek(0, os.SEEK_SET)
		for line in self.file.readlines():
			if line.split('/')[2].startswith(domain):
				# print("=================")
				find = 1
				break
		self.file.seek(0, os.SEEK_END)
		if find == 0:
			wline = json.dumps(dict(item)) + "\n"
			# print("no match=======" + wline)
			self.file.write(wline)
		############################
		#record all urls
		############################
		# line = json.dumps(dict(item)) + "\n"
		# self.file.write(line)
		############################
		return item
