from scrapy.pipelines.images import ImagesPipeline
from . import settings
import scrapy,os
class image_pipelines(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['picture_url'],meta={'item':item})

    def file_path(self, request, response=None, info=None, *, item=None):
        picture_name=request.meta['item']['picture_name']
        page_file=request.meta['item']['page_file']
        page_sourse=settings.IMAGES_STORE
        page_path= f"{page_sourse}/{page_file}"
        if not os.path.exists(page_path):
            os.makedirs(page_path)
        picture_path= f"{page_path}/{picture_name}"
        return picture_path