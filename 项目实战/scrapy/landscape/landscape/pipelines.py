# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LandscapePipeline:
    def process_item(self, item, spider):
        pic_body=item['pic_body']
        pic_path=item['pic_path']
        with open(pic_path,"wb+") as fp:
            fp.write(pic_body)
        print(f"{pic_path}----下载成功")