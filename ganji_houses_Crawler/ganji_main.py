# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      ganji_main
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''
from ganji_houses_Crawler import OptionPanel, URL_Manager, Parser, ResultOutputer


class CrawlMain(object):
    def __init__(self) -> None:
        super().__init__()
        self.urls = URL_Manager.UrlManager()
        self.parser = Parser.Parser()
        self.outputer = ResultOutputer.Outputer()

    def crawling(self, options):
        if self.urls.isExistCity(options['city']):
            print('Error! The city "{0}" is not existed.')
            return


if __name__ == '__main__':
    #option [city, houseType, deepPages, fileName]
    options = OptionPanel.getOptions()
    objCrawler = CrawlMain()
    objCrawler.crawling(options)
