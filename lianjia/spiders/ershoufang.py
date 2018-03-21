# -*- coding: utf-8 -*-
from lianjia.items import LianjiaItem
import scrapy
import re

class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    # allowed_domains = ['https://cd.lianjia.com/ershoufang/']
    base_url = "https://cd.lianjia.com"
    start_urls = [base_url+"/ershoufang/"]

    def parse(self, response):
        path_list = response.xpath("//div[@data-role='ershoufang']/div/a/@href").extract()
        for path in path_list:
            yield scrapy.Request(self.base_url+path,callback=self.sendPageUrl)

    def sendPageUrl(self, response):
        url = re.findall(r'page-url="(.*?)"page-data=',response.text,re.S)[0]
        total_page = re.findall(r'{"totalPage":(.*?),"curPage":1}',response.text,re.S)[0]
        for i in range(1,int(total_page)+1):
            url11=self.base_url+url.format(page=i)
            yield scrapy.Request(url11,callback=self.sendUrl)

    def sendUrl(self, response):
        url_list = response.xpath("//li[@class='clear']/a/@href").extract()
        for url in url_list:
            yield scrapy.Request(url,callback=self.disposeData)

    def disposeData(self, response):
        item = LianjiaItem()
        length = response.xpath("//div[@class='base']/div[@class='content']/ul/li").extract()
        #基本属性
        if(len(length) == 12):
            item["house_type"] = response.xpath("//div[@class='content']/ul/li[1]/text()").extract()[0]
            item["floor"] = response.xpath("//div[@class='content']/ul/li[2]/text()").extract()[0]
            item["area"] = response.xpath("//div[@class='content']/ul/li[3]/text()").extract()[0]
            item["house_structure"] = response.xpath("//div[@class='content']/ul/li[4]/text()").extract()[0]
            item["inside_space"] = response.xpath("//div[@class='content']/ul/li[5]/text()").extract()[0]
            item["building_type"] = response.xpath("//div[@class='content']/ul/li[6]/text()").extract()[0]
            item["direct"] = response.xpath("//div[@class='content']/ul/li[7]/text()").extract()[0]
            item["building_structure"] = response.xpath("//div[@class='content']/ul/li[8]/text()").extract()[0]
            item["decorate_situation"] = response.xpath("//div[@class='content']/ul/li[9]/text()").extract()[0]
            item["elevator_proportion"] = response.xpath("//div[@class='content']/ul/li[10]/text()").extract()[0]
            item["equipped_escalators"] = response.xpath("//div[@class='content']/ul/li[11]/text()").extract()[0]
            item["property_term"] = response.xpath("//div[@class='content']/ul/li[12]/text()").extract()[0]
            item["villa_type"] = ""
        elif (len(length) == 9):
            item["house_type"] = response.xpath("//div[@class='content']/ul/li[1]/text()").extract()[0]
            item["floor"] = response.xpath("//div[@class='content']/ul/li[2]/text()").extract()[0]
            item["area"] = response.xpath("//div[@class='content']/ul/li[3]/text()").extract()[0]
            item["inside_space"] = response.xpath("//div[@class='content']/ul/li[4]/text()").extract()[0]
            item["direct"] = response.xpath("//div[@class='content']/ul/li[5]/text()").extract()[0]
            item["building_structure"] = response.xpath("//div[@class='content']/ul/li[6]/text()").extract()[0]
            item["decorate_situation"] = response.xpath("//div[@class='content']/ul/li[7]/text()").extract()[0]
            item["villa_type"] = response.xpath("//div[@class='content']/ul/li[8]/text()").extract()[0]
            item["property_term"] = response.xpath("//div[@class='content']/ul/li[9]/text()").extract()[0]
            item["house_structure"] = ""
            item["building_type"] = ""
            item["elevator_proportion"] = ""
            item["equipped_escalators"] = ""
        elif (len(length) == 3):
            item["floor"] = response.xpath("//div[@class='content']/ul/li[1]/text()").extract()[0]
            item["area"] = response.xpath("//div[@class='content']/ul/li[2]/text()").extract()[0]
            item["direct"] = response.xpath("//div[@class='content']/ul/li[3]/text()").extract()[0]
            item["house_type"] = ""
            item["inside_space"] = ""
            item["building_structure"] = ""
            item["decorate_situation"] = ""
            item["villa_type"] = ""
            item["property_term"] = ""
            item["house_structure"] = ""
            item["building_type"] = ""
            item["elevator_proportion"] = ""
            item["equipped_escalators"] = ""
        elif (len(length) == 15):
            item["house_type"] = response.xpath("//div[@class='content']/ul/li[1]/text()").extract()[0]
            item["floor"] = response.xpath("//div[@class='content']/ul/li[2]/text()").extract()[0]
            item["area"] = response.xpath("//div[@class='content']/ul/li[3]/text()").extract()[0]
            item["house_structure"] = response.xpath("//div[@class='content']/ul/li[4]/text()").extract()[0]
            item["inside_space"] = response.xpath("//div[@class='content']/ul/li[5]/text()").extract()[0]
            item["building_type"] = response.xpath("//div[@class='content']/ul/li[6]/text()").extract()[0]
            item["direct"] = response.xpath("//div[@class='content']/ul/li[7]/text()").extract()[0]
            item["building_structure"] = response.xpath("//div[@class='content']/ul/li[8]/text()").extract()[0]
            item["decorate_situation"] = response.xpath("//div[@class='content']/ul/li[9]/text()").extract()[0]
            item["elevator_proportion"] = response.xpath("//div[@class='content']/ul/li[10]/text()").extract()[0]
            item["equipped_escalators"] = response.xpath("//div[@class='content']/ul/li[11]/text()").extract()[0]
            item["property_term"] = response.xpath("//div[@class='content']/ul/li[12]/text()").extract()[0]
            item["water_type"] = response.xpath("//div[@class='content']/ul/li[13]/text()").extract()[0]
            item["electricity_type"] = response.xpath("//div[@class='content']/ul/li[14]/text()").extract()[0]
            item["gas_price"] = response.xpath("//div[@class='content']/ul/li[15]/text()").extract()[0]
            item["villa_type"] = ""

        #交易属性
        item["time_tone"] = response.xpath("//div[@class='content']/ul/li[1]/span[2]/text()").extract()[0]
        item["trading_ownership"] = response.xpath("//div[@class='content']/ul/li[2]/span[2]/text()").extract()[0]
        item["last_transaction"] = response.xpath("//div[@class='content']/ul/li[3]/span[2]/text()").extract()[0]
        item["house_usage"] = response.xpath("//div[@class='content']/ul/li[4]/span[2]/text()").extract()[0]
        item["house_term"] = response.xpath("//div[@class='content']/ul/li[5]/span[2]/text()").extract()[0]
        item["property_owner"] = response.xpath("//div[@class='content']/ul/li[6]/span[2]/text()").extract()[0]
        mortgage_info = response.xpath("//div[@class='content']/ul/li[7]/span[2]/text()").extract()[0]
        mortgage_info = mortgage_info.replace(' ', '')
        mortgage_info = mortgage_info.replace('\n', '')
        item["mortgage_info"] = mortgage_info
        item["house_certificate"] = response.xpath("//div[@class='content']/ul/li[8]/span[2]/text()").extract()[0]
        #其他属性
        item["total_price"] = response.xpath("//span[@class='total']/text()").extract()[0]
        item["unit_price"] = response.xpath("//span[@class='unitPriceValue']/text()").extract()[0]
        item["housing_name"] = response.xpath("//div[@class='communityName']/a[1]/text()").extract()[0]
        item["county"] = response.xpath("//div[@class='areaName']/span[2]/a[1]/text()").extract()[0]
        item["street"] = response.xpath("//div[@class='areaName']/span[2]/a[2]/text()").extract()[0]
        item["built_year"] = response.xpath("//div[@class='area']/div[2]/text()").extract()[0]
        print("爬取成功")
        yield item