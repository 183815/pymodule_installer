import scrapy
from picture.items import PictureItem

class PicSpider(scrapy.Spider):
    name = 'pic'
    # allowed_domains = ['fs']
    start_page_num=int(input("请输入开始页码:"))
    pages=int(input("请输入爬取多少页:"))
    for page in range(pages):
        if start_page_num<=1:
            start_urls=['https://www.3gbizhi.com/wallMV/index.html']
        else:
            start_urls=[f'https://www.3gbizhi.com/wallMV/index_{start_page_num}.html']
        start_page_num+=1


    def detail_photo_parse(self,response):
        item=PictureItem()
        picture_url=response.xpath('//*[@id="showimg"]/a[4]/img/@src').extract_first()
        picture_name=response.xpath('/html/body/div[3]/h2/text()').extract_first()
        page_file=response.xpath('//*[@id="pageNum"]/span/a[3]/text()').extract_first()
        item['picture_url']=picture_url
        item['picture_name'] = f"{picture_name}.jpg"
        item['page_file'] = f"第{page_file}页"
        yield item


    def parse(self, response):
        li_list=response.xpath('/html/body/div[5]/ul/li')
        for li in li_list:
            detail_url=li.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=detail_url,callback=self.detail_photo_parse)

