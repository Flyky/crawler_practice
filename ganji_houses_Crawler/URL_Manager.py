# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      URL_Manager
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''
import requests
from bs4 import BeautifulSoup


class UrlManager(object):
    def __init__(self):
        self.city_dict = self.crawl_city_list()

    @staticmethod
    def crawl_city_list():
        # 获取赶集网城市列表与链接，返回字典
        dict_city = {}
        url = 'http://www.ganji.com/index.htm'
        soup = BeautifulSoup(requests.get(url))
        lista = soup.select('.all-city > dl > dd > a')

        for l in lista:
            if 'href' in l.attrs:
                dict_city[l.text] = l.attrs['href']
        return dict_city
