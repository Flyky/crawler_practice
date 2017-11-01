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
    dict_type = {'1': 'fang1', '2': 'fang12', '3': 'fang5',
                 '4': 'fang7', '5': 'fang9', '6': 'fang11'}
    print('''======================================
    Please input the type of the house: ''')
    print('''1. 租房   2. 新房   3. 二手房
    4. 商铺   5. 写字楼   6. 仓库厂房
    ------------------------------------''')
    house_type = input('Please input the number of the type: ')
    type_num = dict_type[house_type]
    # 需要检查
    return type_num


def set_deep_pages():
    deep_pages = int(input('''=========================================
    Please input the crawling total pages: '''))
    return deep_pages


def set_file_name():
    file_name = input('''===================================================================
    Please input the name of the output_cvs file (without extension): ''')
    return file_name


def getOptions():
    options = {}
    options['city'] = set_city()
    options['houseType'] = set_house_type()
    options['deepPages'] = set_deep_pages()
    options['fileName'] = set_file_name()
    return options