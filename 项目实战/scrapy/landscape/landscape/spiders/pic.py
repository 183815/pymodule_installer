import scrapy
from landscape.items import LandscapeItem
from lxml import etree
import os
import requests
from fake_useragent import UserAgent
class PicSpider(scrapy.Spider):
    name = 'pic'
    # allowed_domains = ['pic.netbian.com']
    start_urls = ['https://pic.netbian.com/4kfengjing/index_2.html']
    def parse(self, response):
        file_path = "H:/图片/风景"
        ua=UserAgent()
        headers={
            "User_Agent":ua.ie
        }
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        item = LandscapeItem()
        li_list=response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            pic_href=li.xpath('./a/@href').extract_first()
            pic_page_url=f"https://pic.netbian.com{pic_href}"
            html=requests.get(url=pic_page_url,headers=headers).text
            tree=etree.HTML(html)
            pic_src=tree.xpath('//*[@id="img"]/img/@src')[0]
            pic_url=f"https://pic.netbian.com/{pic_src}"
            pic_body=requests.get(url=pic_url,headers=headers).content
            pic_name=li.xpath('./a/img/@alt').extract_first().replace(' ','|')
            pic_path=f"{file_path}/{pic_name}.jpg"
            item['pic_body']=pic_body
            item['pic_path']=pic_path
            yield item

