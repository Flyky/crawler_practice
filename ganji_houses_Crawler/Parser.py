# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      Parser
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


class Parser(object):
    def parse_page(self, url_base, house_type, crawling_page):
        dict_methods = {'fang1': self.parse_page_fang1, 'fang12': self.parse_page_fang12,
                        'fang5': self.parse_page_fang5, 'fang7': self.parse_page_fang7,
                        'fang9': self.parse_page_fang9, 'fang11': self.parse_page_fang11}
        url = urljoin(url_base, house_type) + '/o{0}'.format(crawling_page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser', from_encoding='utf-8')
        parser_method = dict_methods[house_type]
        parser_method(soup)

    @staticmethod
    def parse_page_fang1(soup):
        list_house = soup.select('.f-list > .f-list-item > .f-list-item-wrap')
        if not list_house:
            print('No house information')
            return
        for house in list_house:
            house_area1 = house.select('.size > span')[2].string.encode('utf-8')  # 爬取面积1
            house_area2 = house.select('.size > span')[4].string.encode('utf-8')  # 爬取面积2
            house_location = house.select('.address > .area > a')[0].string.encode('utf-8')  # 爬取区名称
            house_addr = house.select('.address > .area > a')[-1].string.encode('utf-8')  # 爬取租房的具体地址
            house_price = house.select('.info > .price > .num')[0].string.encode('utf-8')  # 爬取价格
            # 删除string的后三位字符
            house_area1 = house_area1[:-3]  # 去除平方米的单位m2
            house_area2 = house_area2[:-3]  # 去除平方米的单位m2
            if is_num_by_except(house_area1) == "1":  # 筛选出面积1和面积2中是数字的那一个
                house_area1 = house_area1
            else:
                house_area1 = house_area2
            return [house_location, house_addr, house_area1,house_price]

    def parse_page_fang12(self, soup):
        list_house = soup.select('.f-list > .f-list-item > .f-list-item-wrap')
        if not list_house:
            print('No house information')
            return
        for house in list_house:
            house_area1 = house.select('.size > span')[2].string.encode('utf-8')  # 爬取面积
            house_location = house.select('.address > .area > a')[0].string.encode('utf-8')  # 爬取区名称
            house_addr = house.select('.address > .area > a')[-1].string.encode('utf-8')  # 爬取租房的具体地址
            house_price = house.select('.info > .price > .num')[0].string.encode('utf-8')  # 爬取价格
            # 删除string的后三位字符
            house_area1 = house_area1[:-3]  # 去除平方米的单位m2
            house_area2 = house_area2[:-3]  # 去除平方米的单位m2

    def parse_page_fang5(self, soup):
        pass

    def parse_page_fang7(self, soup):
        pass

    def parse_page_fang9(self, soup):
        pass

    def parse_page_fang11(self, soup):
        pass
