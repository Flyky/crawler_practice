# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      ganji_main
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''


class GanjiPanel(object):

    def __init__(self) -> None:
        super().__init__()
        self.city = self.setCity()
        self.houseType = self.setHouseType()
        self.deepTimes = self.setDeepTimes()
        self.fileName = self.setFileName()

    @classmethod
    def getSwitchs(cls):
        return self.city, self.houseType, self.deepTimes, self.fileName

    def setCity(self):
        cityTp = input('''-----------------------------------------------
            Please input the city you would crawl: ''')

    def setHouseType(self):
        pass

    def setDeepTimes(self):
        pass

    def setFileName(self):
        pass


if __name__ == '__main__':
    city, houseType, deepTimes, fileName = GanjiPanel.getSwitchs()
