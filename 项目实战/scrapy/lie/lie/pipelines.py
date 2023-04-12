# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



class LiePipeline:
    fp=None
    def open_spider(self,spider):
        print("开始爬取……")
        self.fp=open("H:/视频/episode_name.txt","wt+",encoding="utf-8")
    def process_item(self, item, spider):
        episode_name=item['episode_name']
        self.fp.write(f"{episode_name}\n")
    def close_spider(self,spider):
        self.fp.close()
        print("结束爬取!")

