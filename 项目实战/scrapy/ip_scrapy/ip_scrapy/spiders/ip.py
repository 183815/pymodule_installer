import scrapy,time


class IpSpider(scrapy.Spider):
    name = 'ip'
    # allowed_domains = ['www.66ip.cn']
    start_urls = ['http://www.66ip.cn/']

    def parse(self, response):
        first_page_url = 'http://www.66ip.cn/'
        for page_num in range(1, 2650):
            if page_num == 1:
                page_url = f"{first_page_url}index.html"
            else:
                page_url = f"{first_page_url}{page_num}.html"
            yield scrapy.Request(url=page_url,callback=self.page_parse)


    def page_parse(self,response):
            tr_list = response.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table//tr')
            for tr in tr_list:
                ip = tr.xpath('./td[1]/text()').extract_first()
                if '.' in ip:
                    port = tr.xpath('./td[2]/text()').extract_first()
                    proxy_dic = {
                        "http": f"http://{ip}:{port}",
                        "https": f"https://{ip}:{port}"
                    }
                    yield scrapy.Request

