# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:16:54 2021

@author: linnn
"""

dict1={123:"123 Tom DTGD",456:"456 Cat CSIE",789:"789 Nana ASIE",321:"321 Lim DBA",654:"654 Won FDD"}
num=int(input("輸入查詢學號為:"))
print("學生資料為:{}".format(dict1.get(num)))