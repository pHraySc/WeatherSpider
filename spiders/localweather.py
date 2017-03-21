# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from weather.items import WeatherItem

class LocalweatherSpider(scrapy.Spider):
    name = "localweather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        html_doc = response.body
        #html_doc = html_doc.decode('utf-8')
        soup = BeautifulSoup(html_doc)
        itemTemp = {}
        itemTemp['city'] = soup.find(id='slider_ct_name')
        tenDay = soup.find(id='blk_fc_c0_scroll')
        itemTemp['date'] = tenDay.findAll("p", {"class": 'wt_fc_c0_i_date'})
        itemTemp['dayDesc'] = tenDay.findAll("img", {"class": 'icons0_wt'})
        itemTemp['dayTemp'] = tenDay.findAll('p', {"class": 'wt_fc_c0_i_temp'})
        item = WeatherItem()
        for att in itemTemp:
            item[att] = []
            if att == 'city':
                item[att] = itemTemp.get(att).text
                continue
            for obj in itemTemp.get(att):
                if att == 'dayDesc':
                    item[att].append(obj['title'])
                else:
                    item[att].append(obj.text)
        return item