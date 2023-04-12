import scrapy,pprint
from lie.items import LieItem

class AplieSpider(scrapy.Spider):
    name = 'aplie'
    # allowed_domains = ['www.123.com']
    start_urls = ['https://zhidao.baidu.com/question/2270612962434634108.html']

    def parse(self, response):
        item=LieItem()
        id_list=response.xpath('//*[@id="best-content-2598148994"]/text()').extract()
        for tr in id_list:
            episode_name = tr.strip()
            if episode_name:
                item['episode_name']=episode_name.replace(' ','.',1).replace(' ','|')
                yield item
