# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 19:26:35 2021

@author: linnn
"""

n=int(input("請輸入正整數:"))
if n%2==0 and n%11==0 and n%5!=0 and n%7!=0:
    print("{}為新公倍數:Yes".format(n))
else:
    print("{}為新公倍數:No".format(n))