# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookPipeline:
    fp = None
    def open_spider(self,spider):
        self.fp=open("H:/三国演义.txt","at+",encoding="utf-8")

    def process_item(self, item, spider):
        title=item['title']
        article=item['article']
        self.fp.write(f"{title}\n{article}")

    def close_spider(self,spider):
        self.fp.close()

