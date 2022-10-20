import scrapy
import json
from Sreality.items import SrealityItem

class SrealitySpider(scrapy.Spider):
    name = 'Sreality'

    start_urls = [f'https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=500&sort=0']

    def parse(self, response):
        res = response.json()
        estates = res.get("_embedded").get("estates")
        item = SrealityItem()
        for estate in estates:
            image = estate.get("_links").get("dynamicDown")[0].get("href")
            image = image.replace('{width}', "400")
            image = image.replace("{height}", "300")
            item["title"] = estate.get("name")
            item["loc"] = estate.get("locality")
            item["img_url"] = image

            yield item
            
