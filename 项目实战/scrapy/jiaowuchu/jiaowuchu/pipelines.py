# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JiaowuchuPipeline:
    fp=None
    def open_spider(self,spider):
        print("正在爬虫……")
        self.fp=open("H:/文档/四川农业大学本科专业设置.csv","wt+",encoding="utf-8")

    def process_item(self, item, spider):
        info_dic=item['info_dic']
        serial_numbers=info_dic['serial_numbers']
        professional_code=info_dic['professional_code']
        professional_title=info_dic['professional_title']
        years_of_study=info_dic['years_of_study']
        degree_conferring_category=info_dic['degree_conferring_category']
        open_academy=info_dic['open_academy']
        self.fp.write(f'"{serial_numbers}","{professional_code}","{professional_title}","{years_of_study}","{degree_conferring_category}","{open_academy}"\n')

    def close_spider(self,spider):
        self.fp.close()
        print("结束爬虫")
