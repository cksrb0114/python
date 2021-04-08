# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from openpyxl import load_workbook
from openpyxl import workbook
import glob
import os

Myfiles = [i for i in glob('*.xlsx')]

total_student = []

for item in Myfiles:
    my_workbook = load_workbook(item, data_only = True)
    my_worksheet = my_workbook['Sheet1']
    my_list = []
    my_list.append(my_worksheet['A2'].value)
    my_list.append(my_worksheet['B2'].value)
    my_list.append(my_worksheet['C2'].value)
    my_list.append(my_worksheet['D2'].value)
    total_student.append(my_list)
    print(my_list)
