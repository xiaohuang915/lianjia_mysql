# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    county = scrapy.Field()
    street = scrapy.Field()
    house_type = scrapy.Field()
    floor = scrapy.Field()
    direct = scrapy.Field()
    built_year = scrapy.Field()
    housing_name = scrapy.Field()
    area = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    building_structure = scrapy.Field()
    inside_space = scrapy.Field()
    building_type = scrapy.Field()
    house_structure = scrapy.Field()
    decorate_situation = scrapy.Field()
    elevator_proportion = scrapy.Field()
    equipped_escalators = scrapy.Field()
    property_term = scrapy.Field()
    time_tone = scrapy.Field()
    trading_ownership = scrapy.Field()
    last_transaction = scrapy.Field()
    house_usage = scrapy.Field()
    property_owner = scrapy.Field()
    house_term = scrapy.Field()
    mortgage_info = scrapy.Field()
    house_certificate = scrapy.Field()
    villa_type = scrapy.Field()

