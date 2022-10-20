# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityPipeline:
    def __init__(self):
        hostname = 'db'
        username = 'postgres_dock'
        password = 'postgres_dock'
        database = 'postgres_dock'

        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        self.cur = self.connection.cursor()
        self.cur.execute(""" DROP TABLE IF EXISTS sreality""")
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sreality(
            id serial PRIMARY KEY, 
            title text,
            loc text,
            img_url text
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute(""" insert into sreality (title, loc, img_url) values (%s,%s,%s)""", (
            item["title"],
            item["loc"],
            item["img_url"]
        ))

        self.connection.commit()
        return item

    def close_spider(self, spider):

        self.cur.close()
        self.connection.close()
