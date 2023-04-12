import scrapy,time,pprint
from book.items import BookItem

class SanguoSpider(scrapy.Spider):
    name = 'sanguo'
    # allowed_domains = ['www.shicimingju.com']
    start_urls = ['https://www.shicimingju.com/book/sanguoyanyi.html']

    def parse(self, response):
        item=BookItem()
        page_url_list=[]
        title_list=[]
        li_list=response.xpath('//*[@id="main_left"]/div[@class="card bookmark-list"]/div[@class="book-mulu"]/ul/li')
        start=0
        if start==0:
            for li in li_list:
                href=li.xpath('./a/@href').extract_first()
                page_url=f"https://www.shicimingju.com{href}"
                page_url_list.append(page_url)
                title=li.xpath('./a/text()').extract_first()
                title_list.append(title)
            start=1
        elif start==1:
            for page_url in page_url_list:
                article = response.xpath('//*[@id="main_left"]/div[@class="card bookmark-list"]/div[@class="chapter_content"]/text()').extract_first()
                print(article)
                yield scrapy.Request(url=page_url, callback=self.parse)

        # item['title'] = title
        # item['article'] = article
        # yield item



