import scrapy
from jiaowuchu.items import JiaowuchuItem

class MajorSpider(scrapy.Spider):
    name = 'major'
    # allowed_domains = ['jiaowu.sicau.edu.cn']
    start_urls = ['http://jiaowu.sicau.edu.cn/web/web/web/profession/profession.asp']

    def parse(self, response):
        item=JiaowuchuItem()
        tr_list=response.xpath('//*[@id="grid"]//tr')
        for tr in tr_list:
            td_list=tr.xpath('./td')
            serial_numbers=td_list[0].xpath('./div[@align="center"]/text()').extract_first()
            professional_code= td_list[1].xpath('./div[@align="center"]/strong/text()|./div[@align="center"]/text()').extract_first()
            professional_title= td_list[2].xpath('./div[@align="center"]/strong/text()|./div[@align="center"]/text()').extract_first()
            years_of_study=td_list[3].xpath('./div[@align="center"]/strong/text()|./div[@align="center"]/text()').extract_first()
            degree_conferring_category=td_list[4].xpath('./div[@align="center"]/strong/text()|./div[@align="center"]/text()').extract_first()
            open_academy=td_list[5].xpath('./div[@align="center"]/strong/text()|./div[@align="center"]/text()').extract_first()
            info_dic={
                #序号
                'serial_numbers':serial_numbers,
                #专业代码
                'professional_code':professional_code,
                #专业名称
                'professional_title':professional_title,
                #修业年限
                'years_of_study':years_of_study,
                #学位授予门类
                'degree_conferring_category':degree_conferring_category,
                #开办学院
                'open_academy': open_academy,
            }
            item['info_dic']=info_dic
            yield item