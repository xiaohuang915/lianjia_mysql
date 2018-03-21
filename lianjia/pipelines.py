# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LianjiaPipeline(object):
    # querStr ='''insert into lianjia_scrapy(house_type,floor) values('{house_type}','{floor}')'''
    querStr ="insert into lianjia_scrapy (house_type,floor,area,house_structure,inside_space,building_type,direct," \
      "building_structure,decorate_situation,elevator_proportion,equipped_escalators,property_term,time_tone," \
      "trading_ownership,last_transaction,house_usage,house_term,property_owner,mortgage_info," \
      "house_certificate,total_price,unit_price,built_year,housing_name,county," \
      "street,villa_type) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        self.cursor.execute(self.querStr,(item['house_type'], item['floor'], item['area'], item['house_structure'],
                                          item['inside_space'], item['building_type'], item['direct'],
                                          item['building_structure'], item['decorate_situation'], item['elevator_proportion'],
                                          item['equipped_escalators'], item['property_term'], item['time_tone'],
                                          item['trading_ownership'], item['last_transaction'], item['house_usage'],
                                          item['house_term'], item['property_owner'], item['mortgage_info'],
                                          item['house_certificate'], item['total_price'], item['unit_price'],
                                          item['built_year'], item['housing_name'], item['county'],
                                          item['street'], item['villa_type']))
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()