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
        if options['city'] not in self.urls.city_dict:
            print('Error! City "{0}" is not exists in the website.'.format(options['city']))
            return
        # url_base = urljoin(self.urls.city_dict[options['city']], options['houseType'])
        url_base = self.urls.city_dict[options['city']]

        crawling_page = 0
        end_page = options['deepPages']
        while crawling_page < end_page:
            self.parser.parse_page(url_base, options['houseType'], crawling_page)


if __name__ == '__main__':
    # option [city, houseType, deepPages, fileName]
    options = OptionPanel.getOptions()
    objCrawler = CrawlMain()
    objCrawler.crawling(options)
