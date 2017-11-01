# -*- coding: utf-8 -*-
'''
--------------------------------------------
    File Name:      ResultOutputer
    Description:    
    Author:         flyky
    Date:           17/10/31
--------------------------------------------

'''
import csv


class Outputer(object):
    def output_csv(self, file_name):
        with open(file_name+'.csv', 'w', encoding = 'utf-8') as f:
            csv_writer = csv.writer(f, delimiter=',')
            