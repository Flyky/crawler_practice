# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      OptionPanel
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''


def set_city():
    city = input('''--------------------------------------
                    Please input the name of the city: ''')
    return city


def set_house_type():
    house_type = input('''--------------------------------------
                        Please input the type of the house: ''')
    return house_type


def set_deep_pages():
    return deep_pages


def set_file_name():
    return file_name


def getOptions():
    options = {}
    options['city'] = set_city()
    options['houseType'] = set_house_type()
    options['deepPages'] = set_deep_pages()
    options['fileName'] = set_file_name()
    return options