import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bug.items import BugItem

class sp(scrapy.Spider):

	name = "xun"

	start_urls = ['https://www.baidu.com']
	
	allowed_domains = ['baidu.com']
	
	def parse(self,response):
		it = BugItem()
		l = ItemLoader(item = it, response = response)
		
		le = LinkExtractor()
		hlinks = le.extract_links(response)
		
		l.add_value('url', response.url)
		# l.add_value('num_links', len(hlinks))
		l.load_item()
		yield it

		for hlink in hlinks:
			nextpage = response.urljoin(hlink.url)
			yield scrapy.Request(nextpage, callback=self.parse)
		


